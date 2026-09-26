# frozen_string_literal: true
#
# Glossary auto-linking
# ---------------------
# Liquid filter `glossary_autolink` applied to the post body in _layouts/post.html.
# For each article it links the FIRST occurrence of each glossary term (or alias)
# to that term's page (/glossaire/<slug>/, /en/glossary/<slug>/, ...) when the
# term has one, and to its anchor on the glossary index otherwise. The link
# keeps the definition as its title attribute.
#
# Non-destructive: it transforms rendered HTML only, never the markdown source,
# and auto-applies to future posts. Remove this file to disable the feature.
#
# Rules:
#  - First occurrence per term per article; longest phrase first; left-to-right.
#  - Never links inside <a>, <h1>-<h6>, <code> or <pre> (HTML-safe scanner that
#    skips those contexts) — so existing links and headings are left untouched.
#  - Acronym-like terms (no spaces, >=2 uppercase letters: CWaPE, GRD, VREG, ...)
#    match case-sensitively to avoid false positives (e.g. "VA" vs French "va").
#  - Straight (') and curly (’) apostrophes are treated as equivalent.
#  - Canonical terms win over aliases when a phrase maps to several entries.
#  - A small blocklist skips over-generic / ambiguous slugs.
#
# Scanning is the expensive part (it dominated the build before this was
# split), so it is done once per (language, HTML) and memoised as tokens: plain
# text runs and matched terms. _plugins/glossary_pages.rb scans every post
# before rendering to learn which terms are used where; the filter then only
# turns the memoised tokens into links. Both caches are dropped on every
# rebuild (`jekyll serve`), so glossary edits are never served stale.

require "strscan"

module Jekyll
  module GlossaryAutolink
    SKIP_TAGS = %w[a h1 h2 h3 h4 h5 h6 code pre].freeze
    # Slugs we never auto-link (too short / ambiguous / generic in running prose).
    BLOCKLIST = %w[ce].freeze

    @index = {}
    @tokens = {}
    # { lang => { slug => url } } for terms that have their own page; set by
    # _plugins/glossary_pages.rb. Terms missing here link to the index anchor.
    @term_urls = {}

    class << self
      attr_accessor :term_urls

      def reset
        @index = {}
        @tokens = {}
        @term_urls = {}
      end
    end

    def self.index_for(site, lang)
      @index[lang] ||= build_index(site, lang)
    end

    def self.glossary_path(site, lang)
      langs = site.config["languages"] || []
      entry = langs.find { |l| l["code"] == lang }
      (entry && entry["glossary_path"]) || "/glossaire/"
    end

    # Acronym/proper-noun heuristic: no spaces and at least two uppercase letters.
    def self.acronym?(phrase)
      !phrase.include?(" ") && phrase.scan(/\p{Lu}/).length >= 2
    end

    def self.build_regex(phrase, case_insensitive)
      escaped = Regexp.escape(phrase)
      # Treat straight and curly apostrophes as interchangeable.
      escaped = escaped.gsub(/['‘’]/, "['‘’]")
      opts = case_insensitive ? Regexp::IGNORECASE : 0
      # Unicode-aware word boundaries so accented letters count as word characters.
      Regexp.new("(?<![\\p{L}\\p{N}])#{escaped}(?![\\p{L}\\p{N}])", opts)
    end

    def self.build_index(site, lang)
      data = site.data["glossary"] || []
      seen = {}
      entries = []
      definitions = {}

      add = lambda do |phrase, slug|
        return if phrase.nil?

        phrase = phrase.to_s.strip
        return if phrase.empty?

        key = phrase.downcase
        return if seen[key]

        seen[key] = true
        entries << { slug: slug, regex: build_regex(phrase, !acronym?(phrase)), length: phrase.length }
      end

      # Pass 1: canonical term names (preferred owner of a phrase).
      data.each do |term|
        slug = term["slug"]
        next if slug.nil? || BLOCKLIST.include?(slug)

        definitions[slug] = (term.dig("definition", lang) || term.dig("definition", "fr")).to_s
        add.call(term.dig("terme", lang) || term.dig("terme", "fr"), slug)
      end
      # Pass 2: aliases (only if the phrase isn't already owned).
      data.each do |term|
        slug = term["slug"]
        next if slug.nil? || BLOCKLIST.include?(slug)

        Array(term.dig("alias", lang)).each { |a| add.call(a, slug) }
      end

      # Longest phrases first: "communauté d'énergie renouvelable" beats "communauté".
      entries.sort_by! { |e| -e[:length] }
      { entries: entries, definitions: definitions, path: glossary_path(site, lang) }
    end

    def self.escape_attr(str)
      str.gsub("&", "&amp;").gsub('"', "&quot;").gsub("<", "&lt;").gsub(">", "&gt;")
    end

    # Split one text run into plain strings and { slug:, text: } matches, each
    # not-yet-linked term matched at its first occurrence.
    def self.scan_text(text, entries, linked, out)
      pos = 0
      len = text.length
      while pos < len
        best = nil
        entries.each do |e|
          next if linked[e[:slug]]

          m = e[:regex].match(text, pos)
          next unless m

          ms = m.begin(0)
          me = m.end(0)
          if best.nil? || ms < best[:start] || (ms == best[:start] && (me - ms) > (best[:finish] - best[:start]))
            best = { start: ms, finish: me, slug: e[:slug] }
          end
        end
        break if best.nil?

        out << text[pos...best[:start]] if best[:start] > pos
        out << { slug: best[:slug], text: text[best[:start]...best[:finish]] }
        linked[best[:slug]] = true
        pos = best[:finish]
      end
      out << text[pos..-1] if pos < len
    end

    # Tokens for one HTML fragment: an array of strings (markup and text,
    # emitted verbatim) and { slug:, text: } hashes (terms to link). `exclude`
    # is a slug never to link — a term page must not link to itself.
    def self.tokens(html, site, lang, exclude = nil)
      key = [lang, exclude, html]
      @tokens[key] ||= begin
        idx = index_for(site, lang)
        linked = {}
        linked[exclude] = true if exclude
        out = []
        scanner = StringScanner.new(html)
        skip_depth = 0
        until scanner.eos?
          if (tag = scanner.scan(/<[^>]+>/))
            out << tag
            name = tag[/\A<\s*\/?\s*([a-zA-Z][a-zA-Z0-9]*)/, 1]&.downcase
            if name && SKIP_TAGS.include?(name) && !tag.end_with?("/>")
              if tag =~ /\A<\s*\//
                skip_depth -= 1 if skip_depth.positive?
              else
                skip_depth += 1
              end
            end
          elsif (text = scanner.scan(/[^<]+/))
            skip_depth.positive? ? out << text : scan_text(text, idx[:entries], linked, out)
          else
            out << scanner.getch
          end
        end
        out.freeze
      end
    end

    # Slugs the filter would link in this HTML.
    def self.linked_slugs(html, site, lang, exclude = nil)
      tokens(html, site, lang, exclude).filter_map { |t| t[:slug] if t.is_a?(Hash) }
    end

    def self.href(site, lang, slug)
      url = @term_urls.dig(lang, slug)
      return "#{site.config["baseurl"]}#{url}" if url

      "#{site.config["baseurl"]}#{glossary_path(site, lang)}##{slug}"
    end

    def self.process(html, site, lang, exclude = nil)
      return html if html.nil? || html.empty?

      idx = index_for(site, lang)
      tokens(html, site, lang, exclude).map do |t|
        next t if t.is_a?(String)

        %(<a class="glossary-link" href="#{href(site, lang, t[:slug])}" ) +
          %(title="#{escape_attr(idx[:definitions][t[:slug]])}">#{t[:text]}</a>)
      end.join
    end
  end

  module GlossaryFilter
    def glossary_autolink(html, lang = nil, exclude = nil)
      site = @context.registers[:site]
      lang ||= site.config["lang"] || "fr"
      Jekyll::GlossaryAutolink.process(html.to_s, site, lang, exclude)
    end
  end
end

Jekyll::Hooks.register :site, :after_reset do |_site|
  Jekyll::GlossaryAutolink.reset
end

Liquid::Template.register_filter(Jekyll::GlossaryFilter)
