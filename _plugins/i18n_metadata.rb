# frozen_string_literal: true

require "set"

# Derives per-page language metadata that _config.yml `defaults` cannot express.
#
# All 68 posts live in one flat _posts/ directory, so a `defaults` scope cannot
# discriminate them by language — only by path, which is identical for all of
# them. Without this generator the site-wide `lang: "fr"` default silently
# applies to any EN/DE/NL file whose front matter forgets `lang:`, producing a
# wrong <html lang>, a wrong hreflang group and a wrong inLanguage, with no
# build error.
#
# Sets, for every page and document:
#   lang    - corrected from the URL prefix when front matter disagrees
#   locale  - Open Graph territory code (fr_BE, en_GB, ...). jekyll-seo-tag reads
#             page.locale before falling back to page.lang, so this is the clean
#             hook for og:locale — no hand-rolled meta tag, no duplication.
#   image.alt - localised, so og:image:alt and twitter:image:alt render at all.
module OptimCE
  class I18nMetadata < Jekyll::Generator
    safe true
    priority :high

    DEFAULT_LANG = "fr"

    def generate(site)
      @site = site
      @languages = site.config["languages"] || []
      @default_locale = locale_for(DEFAULT_LANG)
      @og_dir = File.join(site.source, "assets", "images", "og")
      @og_available = Dir.exist?(@og_dir) ? Dir.children(@og_dir).to_set : Set.new

      (site.pages + site.documents).each { |doc| apply(doc) }
    end

    private

    # Language implied by where the file actually lives, which is the thing the
    # crawler sees. Front matter is advisory; the URL is authoritative.
    def lang_from_url(url)
      @languages.each do |entry|
        prefix = entry["prefix"].to_s
        next if prefix.empty?
        return entry["code"] if url.start_with?("#{prefix}/")
      end
      DEFAULT_LANG
    end

    def locale_for(code)
      entry = @languages.find { |l| l["code"] == code }
      entry && entry["locale"]
    end

    def apply(doc)
      data = doc.data
      url = doc.url.to_s
      expected = lang_from_url(url)
      declared = data["lang"]

      if declared.nil? || declared.to_s.empty?
        Jekyll.logger.warn "i18n:", "#{doc.relative_path} has no `lang:` — using #{expected}"
        data["lang"] = expected
      elsif declared.to_s != expected
        # Loud on purpose: a mismatch here means hreflang, og:locale and the
        # blog listing filter are all pointing at the wrong language.
        Jekyll.logger.warn "i18n:", "#{doc.relative_path} declares lang=#{declared} " \
                                    "but lives at #{url} — correcting to #{expected}"
        data["lang"] = expected
      end

      lang = data["lang"]
      data["locale"] ||= locale_for(lang) || @default_locale

      apply_image(data, lang)
    end

    # The `image` hash comes from a single `defaults` entry in _config.yml, so
    # every page starts out pointing at the SAME Hash object. Mutating it in
    # place leaks one page's language into all the others — which is exactly
    # what happened: the first French page processed set og:image:alt for the
    # whole site. Always work on a per-page copy.
    def apply_image(data, lang)
      image = data["image"]
      image = image.is_a?(Hash) ? image.dup : {}

      # Per-(ref, lang) social card, generated from the page title. Resolved
      # here rather than in front matter so 92 files do not each need an
      # `image:` key; a missing card falls back to the site-wide default.
      ref = data["ref"]
      unless ref.nil? || ref.to_s.empty?
        file = "og-#{ref}-#{lang}.png"
        if @og_available.include?(file)
          image["path"] = "/assets/images/og/#{file}"
          image["width"] = 1200
          image["height"] = 630
        end
      end

      # jekyll-seo-tag emits og:image:alt / twitter:image:alt only when the
      # image hash carries an `alt`.
      i18n = @site.data.dig("i18n", lang)
      alt = i18n && i18n.dig("og", "image_alt")
      image["alt"] = alt if alt

      data["image"] = image
    end
  end
end
