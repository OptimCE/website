# frozen_string_literal: true

# Liquid filter: `{{ post.title | fr_spacing: lang }}`.
#
# French puts a space before : ; ! ? and », and after «. Titles are stored with
# an ordinary space, so a line break can fall right before the colon and start
# the next line with it ("Version de mai 2026" / ": registre et guide"). This
# binds those signs to their word with a no-break space (U+00A0).
#
# Applied by the layouts to French titles and to the rendered body of French
# articles, plain pages, pillar introductions and glossary definitions. Other
# languages pass through unchanged, as do the <title> and JSON-LD strings.
# Markup is safe: kramdown output has no space before these signs inside URLs
# or style attributes, and a no-break space in a title="" tooltip is harmless.
module OptimCE
  module TypographyFilter
    NBSP = " "

    def fr_spacing(input, lang = nil)
      return input unless input.is_a?(String) && lang.to_s == "fr"

      input.gsub(/ ([:;!?»])/) { "#{NBSP}#{Regexp.last_match(1)}" }
           .gsub("« ", "«#{NBSP}")
    end
  end
end

Liquid::Template.register_filter(OptimCE::TypographyFilter)
