# frozen_string_literal: true
#
# Glossary auto-linking (Round 2)
# --------------------------------
# Liquid filter `glossary_autolink` applied to the post body in _layouts/post.html.
# For each article it links the FIRST occurrence of each glossary term (or alias)
# to that language's glossary anchor (/glossaire/#slug, /en/glossary/#slug, ...).
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

require "strscan"

module Jekyll
  module GlossaryAutolink
    SKIP_TAGS = %w[a h1 h2 h3 h4 h5 h6 code pre].freeze
    # Slugs we never auto-link (too short / ambiguous / generic in running prose).
    BLOCKLIST = %w[ce].freeze

    @cache = {}

    def self.index_for(site, lang)
      @cache[lang] ||= build_index(site, lang)
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
      path = glossary_path(site, lang)
      seen = {}
      entries = []

      add = lambda do |phrase, slug, definition|
        return if phrase.nil?
        phrase = phrase.to_s.strip
        return if phrase.empty?
        key = phrase.downcase
        return if seen[key]
        seen[key] = true
        entries << {
          slug: slug,
          definition: definition.to_s,
          regex: build_regex(phrase, !acronym?(phrase)),
          length: phrase.length
        }
      end

      # Pass 1: canonical term names (preferred owner of a phrase).
      data.each do |term|
        slug = term["slug"]
        next if slug.nil? || BLOCKLIST.include?(slug)
        name = term.dig("terme", lang) || term.dig("terme", "fr")
        definition = term.dig("definition", lang) || term.dig("definition", "fr")
        add.call(name, slug, definition)
      end
      # Pass 2: aliases (only if the phrase isn't already owned).
      data.each do |term|
        slug = term["slug"]
        next if slug.nil? || BLOCKLIST.include?(slug)
        definition = term.dig("definition", lang) || term.dig("definition", "fr")
        Array(term.dig("alias", lang)).each { |a| add.call(a, slug, definition) }
      end

      # Longest phrases first: "communauté d'énergie renouvelable" beats "communauté".
      entries.sort_by! { |e| -e[:length] }
      { entries: entries, path: path }
    end

    def self.escape_attr(str)
      str.gsub("&", "&amp;").gsub('"', "&quot;").gsub("<", "&lt;").gsub(">", "&gt;")
    end

    # Link the first occurrence of each not-yet-linked phrase within one text run.
    def self.link_text(text, entries, linked, path)
      out = +""
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
            best = { start: ms, finish: me, slug: e[:slug], definition: e[:definition] }
          end
        end
        break if best.nil?
        out << text[pos...best[:start]]
        matched = text[best[:start]...best[:finish]]
        out << %(<a class="glossary-link" href="#{path}##{best[:slug]}" title="#{escape_attr(best[:definition])}">#{matched}</a>)
        linked[best[:slug]] = true
        pos = best[:finish]
      end
      out << text[pos..-1] if pos < len
      out
    end

    def self.process(html, site, lang)
      return html if html.nil? || html.empty?
      idx = index_for(site, lang)
      entries = idx[:entries]
      return html if entries.empty?
      path = idx[:path]

      linked = {}
      result = +""
      scanner = StringScanner.new(html)
      skip_depth = 0

      until scanner.eos?
        if (tag = scanner.scan(/<[^>]+>/))
          result << tag
          name = tag[/\A<\s*\/?\s*([a-zA-Z][a-zA-Z0-9]*)/, 1]&.downcase
          if name && SKIP_TAGS.include?(name) && !tag.end_with?("/>")
            if tag =~ /\A<\s*\//
              skip_depth -= 1 if skip_depth > 0
            else
              skip_depth += 1
            end
          end
        elsif (text = scanner.scan(/[^<]+/))
          result << (skip_depth > 0 ? text : link_text(text, entries, linked, path))
        else
          result << scanner.getch
        end
      end
      result
    end
  end

  module GlossaryFilter
    def glossary_autolink(html, lang = nil)
      site = @context.registers[:site]
      lang ||= site.config["lang"] || "fr"
      Jekyll::GlossaryAutolink.process(html.to_s, site, lang)
    end
  end
end

Liquid::Template.register_filter(Jekyll::GlossaryFilter)
