# frozen_string_literal: true

require "set"

# One page per glossary term and language, at <glossary_path><page_slug>/.
# Called by the build orchestrator (_plugins/site_graph.rb) before the i18n,
# translation and hub steps, so the pages it creates go through them.
#
# Which terms get a page (all four languages or none, so that hreflang stays
# reciprocal): a French definition longer than MIN_WORDS words, or at least
# one post, in any language, where the term is auto-linked. The others stay
# on the glossary index only, and links to them keep pointing at its anchor.
#
# Usage is known before rendering: each post body goes through the same
# markdown converter the renderer uses (Jekyll caches the result, so the
# render reuses it) and through the glossary scanner, whose tokens are
# memoised for the render-time filter. A post containing Liquid would be
# rendered differently from what was scanned here, so it fails the build.
module OptimCE
  module GlossaryPages
    MIN_WORDS = 30
    TITLE_MAX = 50
    DESC_MIN = 70
    DESC_MAX = 160
    LANGS = %w[fr en de nl].freeze

    def self.apply(site)
      terms = Array(site.data["glossary"])
      return if terms.empty?

      languages = site.config["languages"] || []
      autolink = Jekyll::GlossaryAutolink
      converter = site.find_converter_instance(Jekyll::Converters::Markdown)

      # --- usage: which posts link which term -----------------------------
      usage = Hash.new { |h, k| h[k] = [] } # slug => [posts], all languages
      site.posts.docs.each do |post|
        if post.content.include?("{{") || post.content.include?("{%")
          raise BuildError, "#{post.relative_path}: Liquid in a post body — the glossary " \
                            "usage scan would not match the rendered page"
        end

        html = converter.convert(post.content)
        autolink.linked_slugs(html, site, post.data["lang"]).each { |slug| usage[slug] << post }
      end

      with_page = terms.select do |term|
        words = term.dig("definition", "fr").to_s.split.size
        words > MIN_WORDS || usage.key?(term["slug"])
      end
      page_keys = with_page.map { |t| t["slug"] }.to_set

      # --- URLs, registered before any definition is rendered -------------
      urls = Hash.new { |h, k| h[k] = {} }
      with_page.each do |term|
        LANGS.each do |lang|
          slug = term.dig("page_slug", lang)
          raise BuildError, "_data/glossary.yml: #{term["slug"]} has no page_slug.#{lang}" if slug.to_s.empty?

          path = languages.find { |l| l["code"] == lang }["glossary_path"]
          urls[lang][term["slug"]] = "#{path}#{slug}/"
        end
      end
      autolink.term_urls = urls
      site.data["glossary_pages"] = urls

      dates = block_dates(site, terms)
      pillar_of = pillar_resolver(site)
      by_slug = terms.to_h { |t| [t["slug"], t] }

      with_page.each do |term|
        LANGS.each do |lang|
          site.pages << build_page(site, term, lang, urls, by_slug, terms,
                                   usage[term["slug"]], dates[term["slug"]], pillar_of)
        end
      end
      site.data["glossary_index_only"] = terms.map { |t| t["slug"] }.reject { |s| page_keys.include?(s) }
    end

    def self.build_page(site, term, lang, urls, by_slug, terms, backlinks_all, block_date, pillar_of)
      key = term["slug"]
      t = site.data.dig("i18n", lang, "glossary") || {}
      name = (term.dig("terme", lang) || term.dig("terme", "fr")).to_s.strip
      definition = (term.dig("definition", lang) || term.dig("definition", "fr")).to_s.strip
      autolink = Jekyll::GlossaryAutolink

      page = Jekyll::PageWithoutAFile.new(site, site.source, "", "#{key}-#{lang}.html")
      data = page.data
      data["layout"] = "glossary-term"
      data["lang"] = lang
      data["ref"] = "glossary-term-#{key}"
      data["permalink"] = urls[lang][key]
      data["breadcrumb_parent"] = "glossary"
      data["breadcrumb_title"] = name
      data["title"] = title_for(name, t)
      data["description"] = description_for(definition, t)
      data["image"] = {
        "path" => "/assets/images/og/og-glossary-#{lang}.png", "width" => 1200, "height" => 630
      }

      # Terms cited in the definition, linked in place; never the term itself.
      data["term_definition_html"] = autolink.process(definition, site, lang, key)
      cited = autolink.linked_slugs(definition, site, lang, key)
      data["term_cited"] = cited.map { |slug| term_link(site, by_slug[slug], lang, urls) }
      data["term_related"] = terms
        .select { |o| o["categorie"] == term["categorie"] && o["slug"] != key && !cited.include?(o["slug"]) }
        .map { |o| term_link(site, o, lang, urls) }
        .sort_by { |l| l["name"].downcase }

      backlinks = backlinks_all.select { |p| p.data["lang"] == lang }.sort_by { |p| -p.date.to_i }
      data["term_key"] = key
      data["term_name"] = name
      data["term_definition"] = definition
      data["term_aliases"] = Array(term.dig("alias", lang)).map(&:to_s)
      data["term_category"] = site.data.dig("i18n", lang, "glossary", "categories", term["categorie"]) || term["categorie"]
      data["term_backlinks"] = backlinks
      data["term_pillar"] = pillar_of.call(term, backlinks_all, lang)
      data["term_source"] = source_for(site, term, lang)
      stamps = [block_date] + backlinks_all.map(&:date)
      data["last_modified_at"] = stamps.compact.max || Dates.to_time(glossary_index_date(site, lang))
      page
    end

    def self.term_link(site, term, lang, urls)
      name = (term.dig("terme", lang) || term.dig("terme", "fr")).to_s.strip
      url = urls[lang][term["slug"]]
      url ||= "#{site.config["languages"].find { |l| l["code"] == lang }["glossary_path"]}##{term["slug"]}"
      { "name" => name, "url" => url }
    end

    # `source_ref` names one of our own pages by translation ref. The
    # translations map is only built after this step, so look the page up.
    def self.source_for(site, term, lang)
      ref = term["source_ref"].to_s
      unless ref.empty?
        page = site.pages.find { |p| p.data["ref"].to_s == ref && p.data["lang"] == lang }
        return { "name" => term["source_nom"], "url" => page.url, "external" => false } if page
      end
      return nil if term["source_url"].to_s.empty?

      { "name" => term["source_nom"], "url" => term["source_url"], "external" => true }
    end

    # "<name> : définition" in the page's language, or the bare name when the
    # suffix would push the <title> past the SERP budget.
    def self.title_for(name, t)
      format = t.dig("term", "title_format").to_s
      titled = format.empty? ? name : format.sub("%{name}", name)
      titled.length <= TITLE_MAX ? titled : name
    end

    # The definition itself, cut at a word boundary to fit 160 characters, or
    # completed with a sentence when shorter than 70.
    def self.description_for(definition, t)
      text = definition.gsub(/\s+/, " ").strip
      if text.length > DESC_MAX
        cut = text[0, DESC_MAX - 1]
        cut = cut[0, cut.rindex(" ") || cut.length].sub(/[\s,;:.–—-]+\z/, "")
        text = "#{cut}…"
      end
      if text.length < DESC_MIN
        suffix = t.dig("term", "description_suffix").to_s
        text = "#{text} #{suffix}".strip
      end
      text
    end

    # The most relevant pillar is an editorial choice, not a vote: counting
    # the guides that cite a term favours the pillar with the most guides and
    # scatters cross-cutting terms (CWaPE, VAT) at random. A term recommends
    # its own `pilier:` when set, else the pillar whose `categories` list the
    # term's category (_data/pillars.yml).
    def self.pillar_resolver(site)
      pillars = Array(site.data["pillars"])
      keys = pillars.map { |p| p["key"] }
      pages = site.pages.select { |p| p.data["layout"] == "pillar" }
      lambda do |term, _backlinks, lang|
        key = term["pilier"]
        if key && !keys.include?(key)
          raise BuildError, "_data/glossary.yml: #{term["slug"]} has unknown pilier #{key.inspect}"
        end

        key ||= pillars.find { |p| Array(p["categories"]).include?(term["categorie"]) }&.dig("key")
        next nil unless key

        pages.find { |p| p.data["pillar"] == key && p.data["lang"] == lang }
      end
    end

    # Last commit date of each term's block in _data/glossary.yml, from one
    # `git blame`. Lines not yet committed, or cut off by a shallow clone
    # (boundary), give no date; a term with no dated line falls back to the
    # glossary index date.
    def self.block_dates(site, terms)
      out = IO.popen(%w[git blame -w --line-porcelain -- _data/glossary.yml],
                     chdir: site.source, err: File::NULL, &:read)
      return {} unless $?.success? && !out.to_s.empty?

      line_time = {}
      final = nil
      stamp = nil
      skip = false
      out.each_line do |line|
        if (m = line.match(/\A(\h{40}) \d+ (\d+)/))
          final = m[2].to_i
          skip = m[1].match?(/\A0+\z/)
          stamp = nil
        elsif line.start_with?("committer-time ")
          stamp = line.split[1].to_i
        elsif line.start_with?("boundary")
          skip = true
        elsif line.start_with?("\t")
          line_time[final] = Time.at(stamp) if stamp && !skip
        end
      end

      source = File.readlines(File.join(site.source, "_data", "glossary.yml"), chomp: true)
      dates = {}
      current = nil
      source.each_with_index do |text, i|
        if (m = text.match(/\A- slug:\s*(\S+)/))
          current = m[1]
        end
        next unless current

        t = line_time[i + 1]
        dates[current] = [dates[current], t].compact.max if t
      end
      dates
    end

    def self.glossary_index_date(site, lang)
      path = site.config["languages"].find { |l| l["code"] == lang }["glossary_path"]
      page = site.pages.find { |p| p.url == path }
      page && page.data["last_modified_at"]
    end
  end
end
