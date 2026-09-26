# frozen_string_literal: true

# Build orchestrator.
#
# Jekyll sorts generators by priority only, and with an unstable sort: two
# generators of equal priority run in no guaranteed order. Every step below
# reads the output of the one before it, so they run here, in one fixed
# sequence, instead of as separate generators:
#
#   1. i18n metadata    lang / locale / OG image on every page and post
#   2. redirect table   _data/redirects.csv -> redirect_from on the target page
#   3. translations     data["translations"] = { lang => url } for every ref
#   4. URL guard        two files writing the same URL fail the build
#
# jekyll-redirect-from (:normal) then turns redirect_from into stub pages, and
# jekyll-sitemap / jekyll-feed (:lowest) run after that.
module OptimCE
  class SiteGraph < Jekyll::Generator
    safe true
    priority :highest

    def generate(site)
      I18nMetadata.apply(site)
      RedirectsTable.apply(site)
      Translations.apply(site)
      UrlGuard.apply(site)
    end
  end

  # Raised for content errors that must stop the build: a green build that
  # deploys a broken redirect or a duplicate URL is worse than a red one.
  class BuildError < StandardError; end

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
