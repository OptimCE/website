# frozen_string_literal: true

# Liquid filter: `{{ "allocation-key-belgium" | ref_url }}` returns the URL of
# that translation family's page in the current page's language, or in the
# language given as argument: `{{ "allocation-key-belgium" | ref_url: "de" }}`.
#
# Hub pages (pillars, guide and solution indexes, features) link to articles
# by ref rather than by URL, so a moved article never leaves them with a stale
# link. An unknown ref fails the build instead of shipping a broken link.
# The lookup table is built by _plugins/site_graph.rb.
module OptimCE
  module RefUrlFilter
    def ref_url(ref, lang = nil)
      site = @context.registers[:site]
      page = @context.registers[:page]
      lang = (lang || (page && page["lang"]) || site.config["lang"]).to_s
      url = site.data.dig("translations", ref.to_s, lang)
      unless url
        where = page ? page["path"] : "?"
        raise ArgumentError, "ref_url: no #{lang} page for ref #{ref.inspect} (in #{where})"
      end

      "#{site.config["baseurl"]}#{url}"
    end
  end
end

Liquid::Template.register_filter(OptimCE::RefUrlFilter)
