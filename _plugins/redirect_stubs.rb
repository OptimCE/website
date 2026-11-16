# frozen_string_literal: true

require "uri"

# Gives every redirect stub the language and the title of the page it points to.
#
# GitHub Pages cannot answer a moved URL with an HTTP 301, so each row of
# _data/redirects.csv ends as a jekyll-redirect-from stub: an HTML page served
# with a 200 (meta refresh, canonical, noindex). Bing keeps such a page as a URL
# of its own. With the plugin's template, all 121 stubs were titled
# "Redirecting…" and claimed lang="en-US", and Bing Webmaster Tools reported
# them as duplicate titles of one another (report of 2026-11-14).
#
# _layouts/redirect.html replaces that template; this hook feeds it. It runs at
# :site :pre_render, after every generator (jekyll-redirect-from included), so
# the stubs exist and their targets are final. Each stub gets:
#   lang                   the target's language, so <html lang> matches the
#                          path and the template picks the right strings
#   redirect_target_title  the target's title, so each stub title is unique
#                          ("Page déplacée → <title>") without copying the
#                          target's own <title>
#   redirect_variant       2, 3… when several old URLs lead to the same page
#                          (/actualites/2026/05/25/ and /05/26/, from the
#                          timezone shift fixed in July), so their titles
#                          still differ; nil for the first, by path order
module OptimCE
  module RedirectStubs
    def self.apply(site)
      stubs, docs = (site.pages + site.docs_to_write).partition do |doc|
        doc.is_a?(JekyllRedirectFrom::RedirectPage)
      end
      by_url = docs.to_h { |doc| [doc.url, doc] }

      groups = stubs.group_by { |stub| URI.parse(stub.data.dig("redirect", "to").to_s).path }
      groups.each do |to, group|
        target = by_url[to]
        raise BuildError, "redirect stub #{group.first.url}: target #{to} is not a page" unless target

        group.sort_by(&:url).each_with_index do |stub, i|
          stub.data["lang"] = target.data["lang"]
          stub.data["redirect_target_title"] = target.data["title"].to_s
          stub.data["redirect_variant"] = i.zero? ? nil : i + 1
        end
      end
    end
  end
end

Jekyll::Hooks.register :site, :pre_render do |site, _payload|
  OptimCE::RedirectStubs.apply(site)
end
