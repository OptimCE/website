# frozen_string_literal: true

# Build orchestrator.
#
# Jekyll sorts generators by priority only, and with an unstable sort: two
# generators of equal priority run in no guaranteed order. Every step below
# reads the output of the one before it, so they run here, in one fixed
# sequence, instead of as separate generators:
#
#   1. i18n metadata    lang / locale / OG image on every page and post
#   2. sections         every post is a guide, a solution or a news item, and
#                       must live under that section's path in its language
#   3. redirect table   _data/redirects.csv -> redirect_from on the target page
#   4. translations     data["translations"] = { lang => url } for every ref
#   5. hubs             pages that list other pages (pillars, guide index, news
#                       listings) get their resolved lists and a
#                       last_modified_at that moves when a listed page changes
#   6. URL guard        two files writing the same URL fail the build
#
# jekyll-redirect-from (:normal) then turns redirect_from into stub pages, and
# jekyll-sitemap / jekyll-feed (:lowest) run after that.
module OptimCE
  class SiteGraph < Jekyll::Generator
    safe true
    priority :highest

    def generate(site)
      I18nMetadata.apply(site)
      Sections.apply(site)
      RedirectsTable.apply(site)
      Translations.apply(site)
      Hubs.apply(site)
      UrlGuard.apply(site)
    end
  end

  # Coerces the date types YAML front matter produces (Date, Time or String)
  # to Time, so that they compare.
  module Dates
    def self.to_time(value)
      case value
      when Time then value
      when Date then value.to_time
      when String then Jekyll::Utils.parse_date(value)
      end
    end

    # The later of the page's own last_modified_at and the dates of the pages
    # it lists. A hub's content changes when a listed page appears or changes,
    # so its sitemap lastmod (and IndexNow) must follow.
    def self.latest(own, docs)
      stamps = docs.map { |d| to_time(d.data["last_modified_at"]) || to_time(d.data["date"]) }
      ([to_time(own)] + stamps).compact.max
    end
  end

  # Resolves what hub pages list, once, in Ruby rather than with Liquid `where`
  # scans, and fails the build on a section entry that matches no guide.
  #
  #   layout: pillar   hub_sections = [{ "title", "posts" }], from the page's
  #                    `sections` front matter; guides of the pillar that no
  #                    section lists land in a trailing "more guides" group,
  #                    so a new guide is never invisible. hub_neighbours = the
  #                    other pillar pages of the same language.
  #   layout: guides   hub_pillars = [{ "page", "label", "posts" }] in
  #                    _data/pillars.yml order.
  #   layout: solutions  the solution posts, in _data/solutions.yml order.
  #   layout: blog     the news posts, newest first.
  #
  # Both also get hub_items (flat list of listed pages, for the ItemList in
  # the JSON-LD) and a computed last_modified_at.
  module Hubs
    def self.apply(site)
      posts = site.posts.docs
      pillars = Array(site.data["pillars"])
      pillar_keys = pillars.map { |p| p["key"] }

      posts.each do |post|
        key = post.data["pillar"]
        next if key.nil? || pillar_keys.include?(key)

        raise BuildError, "#{post.relative_path}: unknown pillar #{key.inspect} (see _data/pillars.yml)"
      end

      pillar_pages = site.pages.select { |p| p.data["layout"] == "pillar" }
      pillar_pages.each { |page| resolve_pillar(site, page, posts) }
      pillar_pages.each do |page|
        page.data["hub_neighbours"] = pillar_keys.filter_map do |key|
          next if key == page.data["pillar"]

          pillar_pages.find { |p| p.data["pillar"] == key && p.data["lang"] == page.data["lang"] }
        end
      end

      solution_keys = Array(site.data["solutions"]).map { |s| s["key"] }
      site.pages.select { |p| p.data["layout"] == "solutions" }.each do |page|
        mine = posts.select { |p| p.data["solution"] && p.data["lang"] == page.data["lang"] }
        page.data["hub_items"] = mine.sort_by { |p| solution_keys.index(p.data["solution"]) || solution_keys.size }
        page.data["last_modified_at"] = Dates.latest(page.data["last_modified_at"], page.data["hub_items"])
      end

      site.pages.select { |p| p.data["layout"] == "blog" }.each do |page|
        news = posts.select { |p| p.data["section"] == "actualites" && p.data["lang"] == page.data["lang"] }
        page.data["hub_items"] = news.sort_by { |p| -p.date.to_i }
        page.data["last_modified_at"] = Dates.latest(page.data["last_modified_at"], page.data["hub_items"])
      end

      site.pages.select { |p| p.data["layout"] == "guides" }.each do |page|
        lang = page.data["lang"]
        entries = pillars.filter_map do |pillar|
          pillar_page = pillar_pages.find { |p| p.data["pillar"] == pillar["key"] && p.data["lang"] == lang }
          next unless pillar_page

          { "page" => pillar_page, "label" => pillar.dig("label", lang),
            "posts" => pillar_page.data["hub_items"] }
        end
        page.data["hub_pillars"] = entries
        page.data["hub_items"] = entries.map { |e| e["page"] }
        page.data["last_modified_at"] = Dates.latest(page.data["last_modified_at"], page.data["hub_items"])
      end
    end

    def self.resolve_pillar(site, page, posts)
      key = page.data["pillar"]
      lang = page.data["lang"]
      mine = posts.select { |p| p.data["pillar"] == key && p.data["lang"] == lang }
      by_ref = mine.to_h { |p| [p.data["ref"], p] }

      sections = Array(page.data["sections"]).map do |section|
        docs = Array(section["refs"]).map do |ref|
          by_ref[ref] || raise(BuildError, "#{page.relative_path}: section #{section["title"].inspect} " \
                                           "lists #{ref.inspect}, which is not a #{lang} guide of pillar #{key}")
        end
        { "title" => section["title"], "posts" => docs }
      end

      listed = sections.flat_map { |s| s["posts"] }
      rest = (mine - listed).sort_by { |p| -p.date.to_i }
      unless rest.empty?
        title = site.data.dig("i18n", lang, "guides", "more_guides")
        sections << { "title" => title, "posts" => rest }
      end

      page.data["hub_sections"] = sections
      page.data["hub_items"] = sections.flat_map { |s| s["posts"] }
      page.data["last_modified_at"] = Dates.latest(page.data["last_modified_at"], page.data["hub_items"])
    end
  end

  # Raised for content errors that must stop the build: a green build that
  # deploys a broken redirect or a duplicate URL is worse than a red one.
  class BuildError < StandardError; end

  # A post is a guide when it names a pillar, a solution when it names a
  # solution, and a news item otherwise. Its URL must sit under that section's
  # path for its language, so a guide cannot silently keep a dated /actualites/
  # URL (or a news item land under /guides/) because its permalink was
  # forgotten.
  module Sections
    PATH_KEYS = { "guides" => "guides_path", "solutions" => "solutions_path", "actualites" => "blog_path" }.freeze

    def self.apply(site)
      languages = site.config["languages"] || []
      solution_keys = Array(site.data["solutions"]).map { |s| s["key"] }
      site.posts.docs.each do |post|
        key = post.data["solution"]
        if key && !solution_keys.include?(key)
          raise BuildError, "#{post.relative_path}: unknown solution #{key.inspect} (see _data/solutions.yml)"
        end

        section = if post.data["pillar"] then "guides"
                  elsif post.data["solution"] then "solutions"
                  else "actualites"
                  end
        post.data["section"] = section
        entry = languages.find { |l| l["code"] == post.data["lang"] } || {}
        prefix = entry[PATH_KEYS[section]].to_s
        next if !prefix.empty? && post.url.start_with?(prefix)

        raise BuildError, "#{post.relative_path}: a #{section} post must live under #{prefix} "                           "(its URL is #{post.url}) — set `permalink:`"
      end
    end
  end

  # `_data/redirects.csv` is the single source of truth for moved URLs. Each
  # row (from, to) becomes a `redirect_from` entry on the page that now lives
  # at `to`; jekyll-redirect-from writes the stub. Keeping the table in one
  # file means a move is one CSV row, and scripts/check_site.py can verify
  # every row against the built site.
  module RedirectsTable
    def self.apply(site)
      rows = Array(site.data["redirects"])
      targets = {}
      (site.pages + site.docs_to_write).each { |doc| targets[doc.url] = doc }

      # Front-matter redirect_from would be a second, unchecked source.
      targets.each_value do |doc|
        next unless doc.data.key?("redirect_from")

        raise BuildError, "#{doc.relative_path}: declare redirects in _data/redirects.csv, " \
                          "not in front matter (redirect_from)"
      end

      froms = rows.map { |row| path(row["from"]) }
      rows.each_with_index do |row, i|
        line = i + 2 # header is line 1
        from = path(row["from"])
        to = path(row["to"])
        target = targets[to]
        raise BuildError, "redirects.csv:#{line}: target #{to} is not a page" unless target
        raise BuildError, "redirects.csv:#{line}: #{from} is still a live page" if targets.key?(from)
        raise BuildError, "redirects.csv:#{line}: #{to} is itself redirected (chain)" if froms.include?(to)
        raise BuildError, "redirects.csv:#{line}: duplicate source #{from}" if froms.count(from) > 1

        target.data["redirect_from"] = Array(target.data["redirect_from"]) + [from]
      end
    end

    def self.path(value)
      value = value.to_s.strip
      raise BuildError, "redirects.csv: empty path" if value.empty?

      value.start_with?("/") ? value : "/#{value}"
    end
  end

  # One lookup table for everything that links a page to its translations:
  # hreflang, the language switcher, the post translation nav, card badges and
  # glossary sources. It replaces `site.pages | where: "ref"` scans, which cost
  # a pass over every page each time and returned translations in collection
  # order rather than language order.
  module Translations
    def self.apply(site)
      docs = site.pages + site.posts.docs
      map = {}
      docs.each do |doc|
        ref = doc.data["ref"].to_s
        next if ref.empty?

        lang = doc.data["lang"].to_s
        by_lang = (map[ref] ||= {})
        if by_lang.key?(lang)
          raise BuildError, "ref #{ref.inspect} has two #{lang} pages: #{by_lang[lang]} and #{doc.url}"
        end

        by_lang[lang] = doc.url
      end

      docs.each do |doc|
        ref = doc.data["ref"].to_s
        doc.data["translations"] = map[ref] unless ref.empty?
      end
      site.data["translations"] = map
    end
  end

  module UrlGuard
    def self.apply(site)
      seen = {}
      (site.pages + site.docs_to_write).each do |doc|
        url = doc.url
        if seen.key?(url)
          raise BuildError, "#{url} is written by both #{seen[url]} and #{doc.relative_path}"
        end

        seen[url] = doc.relative_path
      end
    end
  end
end
