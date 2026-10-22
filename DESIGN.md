# OptimCE website: design system

This file is the reference for anyone changing how optimce.be looks: tokens,
type, components, and the markup conventions the stylesheet relies on. The
source of truth for values is `_sass/_variables.scss`; this file explains the
roles and the rules.

## Concept

Belgian energy sharing is settled per quarter-hour: 96 slots a day. The site's
one bold element is the homepage grid, 28 days by 96 quarter-hours of shared
energy. A household reads it as data; a developer recognises the GitHub
contribution graph. Everything else stays quiet.

- **One bold element.** The grid is the only motion that the reader does not
  trigger. Today's row fills up to "now" once, and it is static under
  `prefers-reduced-motion`.
- **Left-aligned, editorial.** No centred hero, gradients, ALL-CAPS eyebrows,
  monospace labels, `→` appended to link text, or hover lifts.
- **Structure carries information.** Numbered markers are used only for a real
  sequence (the three steps). Cards are used only for collections of like
  objects (news, glossary terms). Lists of guides are rows. A thick rule opens
  a topic.
- **Flat.** Hairline borders, no shadows. The one exception is the floating
  language menu. Radius follows hierarchy: 6px chips, 8px controls, 12px cards
  and panels.
- **Sentence case, plain words.** Buttons say what happens. Product claims
  match what the app does.

## Colour

Only the existing chart is used:

- the OptimCE greens, shared with the logo and the app (Material Green);
- the Bootstrap-derived greys;
- for the dark theme, the app's own dark surfaces;
- one accent, the app's surplus amber.

Every text/background pair is WCAG AA.

| Role | Light | Dark |
|---|---|---|
| Page / alternate / raised | `#FFFFFF` / `#F8FAF8` / `#FFFFFF` | `#0E120E` / `#181E18` / `#252D26` |
| Heading, text | `#0E120E`, `#212529` | `#F0F4F0` |
| Muted text | `#495057` (8.2:1) | `#9BA89D` (7.6:1) |
| Border: decorative / controls | `#DEE2E6` / `#868E96` (3:1) | `#374038` / `#6E7E70` |
| Primary (buttons, links) | `#1B5E20` (7.9:1 with white) | `#66BB6A` (8.0:1 with `#0E120E`) |
| Tint (callouts, chips) | `#E8F5E9` | `#152A16` |
| Sun, "now" | `#F59E0B` | `#F59E0B` |

Rules:

- **Amber is never text on white** (2.2:1). It marks "now" in the grid and
  surplus in charts.
- **Energy series:** shared `#2E7D32`, surplus `#F59E0B` (`#D97706` in dark
  mode, where direct labels are required). Both pairs were checked for
  colour-blind separation.
- **Quarter-hour ramp (ordinal):**

  | | Empty | Level 1 | Level 2 | Level 3 | Level 4 |
  |---|---|---|---|---|---|
  | Light | `#ECEFF1` | `#81C784` | `#43A047` | `#2E7D32` | `#1B5E20` |
  | Dark | `#252D26` | `#145218` | `#2E7D32` | `#43A047` | `#81C784` |

  The palest green (`#C8E6C9`) is too faint to be a level.
- **Keep old token names.** Inline styles still use `--text-5xl`,
  `--weight-bold`, `--color-primary`, `--space-4`, `--space-8` and
  `--text-sm`.

### Dark mode

- Tokens are overridden under `@media (prefers-color-scheme: dark)`
  (`:root:not([data-theme="light"])`) and under `:root[data-theme="dark"]`.
- `head.html` applies a stored choice (`localStorage['oce-theme']`, the key
  guide.optimce.be uses) before the first paint, so there is no flash.
- The header switch stores the other theme. Picking the system's own theme
  clears the choice, so the site follows the system again.
- Diagrams keep their white canvas and read as paper figures in both themes.

## Type

Two families, self-hosted:

- **Plus Jakarta Sans** (500–800) for headings and interface text.
- **Source Sans 3** (400–600, upright and italic) for text.

`scripts/subset_fonts.py` builds the variable woff2 files from the OFL sources
in google/fonts. It narrows the weight axis and subsets to Latin plus the
arrows, maths signs, sub- and superscripts the articles use. It also prints the
metric-matched Arial fallbacks, which go in `_sass/_fonts.scss`.

`plus-jakarta-sans-700.woff2` and `source-sans-3-400.woff2` stay only for
`scripts/generate_og_cards.py`, which loads them by name. The site no longer
uses them.

| Level | Size |
|---|---|
| Display (home h1) | 2.5 → 4rem, 700, tracking −0.03em |
| h1 | 2 → 2.75rem |
| h2 | 1.5 → 1.875rem |
| h3 | 1.25rem |
| Body | 17px |
| Article text | 18px, line-height 1.65, column 38rem (about 72 characters) |

**Figures.** Source Sans 3 figures are tabular by default. Prose switches to
proportional figures; tables keep tabular ones.

**French spacing.** `_plugins/typography.rb` (the `fr_spacing` filter) binds
`: ; ! ? »` to the word before, and `«` to the word after, with a no-break
space. The layouts apply it to French titles and bodies. Source files keep
ordinary spaces. Thousands still take a plain space (`3 500 kWh`), as the
content rules require.

## Layout

- One container, 1320px (`.container`), for the header and the content.
  Article pages centre a 38rem column and a 15rem rail.
- Page openers use the full width on desktop, the title on the left and the
  lead on the right; below that they stack.
  - Home hero, from 1280px (`$bp-header`): the title and the lead share a
    last line, and the buttons fill the lead. When the labels are too long
    for one row (German, Dutch), the buttons stack at equal width.
  - Guide, solution, news and glossary indexes, from 1200px (`$bp-xl`): the
    header repeats the columns of the grid below it. The title takes the
    first column and the lead starts on the second.
- The full header shows from 1280px (`$bp-header`); the GitHub icon joins from
  1440px.
- The header was measured on 2026-09-29. Dutch is the longest: 1 172px without
  the GitHub icon, 1 210px with it. Adding a menu entry or lengthening a label
  means measuring again, for example with Playwright at 1280 and 1440px.
- The "Tools" entry shows only where the tools hub exists. Measured with it on
  2026-10-18, at 1280px (1 216px available): French 1 155px, English 1 005px,
  Dutch 1 222px, German 1 242px with "Werkzeuge"; at 1440px, with the GitHub
  icon (1 256px available), Dutch needs 1 260px and German 1 280px. German
  therefore labels the entry "Tools" (1 206px at 1280, 1 244px at 1440), and
  Dutch lists Tools in the footer only, like the pricing link
  (`nav.tools_footer_only` in `_data/i18n/nl.yml`); French, English and German
  show it in both menus.

## Components

### Buttons

- `.btn` with `.btn-primary` or `.btn-outline`, and sizes `.btn--sm` or
  `.btn--lg`.
- `.btn-white` and `.btn-white-outline` are aliases kept for old markup.
- There is at most one primary button per block.

### Chips

`.post__tag`, `.post-card__tag` and `.glossary-card__category`.

### Cards and rows

- `post-card.html` takes `variant="card"` (news, home) or `variant="row"`
  (pillar pages).
- The title link covers the card. Language badges sit above it.

### Hub blocks

`.hub-block` on the guide and solution indexes.

### Product shot (homepage)

- The manager's dashboard from the user guide's tour captures, built by
  `scripts/build_product_shots.py`. Rerun it when the tour is captured again.
- Phones (below 768px) get the phone capture, at about its real size (24rem
  at most). From 768px, visitors get the desktop capture.
- It is one `<picture>`: the browser downloads only the image it shows, and
  each source declares its size, so nothing moves while it loads.
- Both images show the same screen, so one alt text serves both. Keep it to
  what the shorter phone crop shows.

### Hosting cards (homepage)

Two cards of equal weight: app.optimce.be, and self-hosting. The self-hosting
card has no install commands: the development monorepo is not the way to
deploy. Its "Developer documentation" button reads `developers_url` in
`_config.yml` and stays hidden while that is empty, so the site never links to
a documentation site that is not online yet.

### Newsletter (homepage)

The same Mailchimp form (`_includes/newsletter-form.html`) appears twice on the
page.

- In the hero, under the buttons and the open-source line, above the
  quarter-hour grid. It sits behind a hairline at the lead's 36rem measure,
  with the title and a one-line lead. The title is a `<strong>`, not a
  heading, because the foot band holds the h2 with the same words. From
  1280px it takes a second row in the lead's column, so the title still lines
  up with the open-source line. The button stays beside the field on phones.
- At the foot, the band with the benefits list.

### Article rail

The rail holds "On this page" and a call to action.

- `_layouts/post.html` lists the article's own H2s when there are at least
  three, so the list works without JavaScript.
- `main.js` opens it in the rail from 1200px, folds it above the text below
  that width, and marks the section being read.

### Product pages

- `layout: page` with `product_page: true` (billing, CWaPE filing, allocation
  key…). They read like guides, so they reuse the article grid: the breadcrumb
  and title over a centred 38rem column, and the rail with "On this page" and
  a card that opens the application.
- Screenshots go through `_includes/product-shot.html`, built by
  `scripts/build_feature_shots.py` from the published user guide and cropped
  to the part of the screen the text talks about. French pages show the
  French capture, the other languages the English one. Each links to its
  full-size file.
- They end with `_includes/product-cta.html`: the application as the one
  primary button, "Try the demo" only when `cta.demo_url` is set, and the
  step-by-step guide.

### Callouts in articles

Articles are never edited for styling: `_sass/_prose.scss` recognises the
markdown shapes below.

| Markdown | Role |
|---|---|
| `> ### Heading`, text, `> **[Démarrer… →](https://app.optimce.be)**` | Product call to action (tinted panel; the bold link becomes a button) |
| `> **[Guide title](/guides/…)**`, a blank `>` line, `> summary` | Related-guide card |
| Any other blockquote | Quote, notice or formula |
| `<div class="post-cta" markdown="0">` … `.btn` | Call to action with buttons |
| `## FAQ` then `### Question` | FAQ, questions separated by hairlines |
| `## Sources` / `## Quellen` / `## Bronnen` then a list | Smaller, muted references |
| `## Ce qu'il faut retenir` (and the EN/DE/NL equivalents) then `1.` | Key takeaways panel |
| `*Hypothèses : …*` right after a table | Small muted note |

The key-takeaways panel keys on the heading id, so write one of the headings
already used. The ids are listed in `_prose.scss`.

### Diagrams

- They are `<img>` SVGs with a white canvas and a hairline frame.
- Below 600px they keep a readable size and scroll sideways.

## Tools

The tools section (`tools_path`: `/outils/`, `/en/tools/`, `/de/werkzeuge/`,
`/nl/tools/`) holds pages that answer a question from data. Its hub
(`ref: tools`, `_layouts/tools.html`) lists its children
(`breadcrumb_parent: tools`) in `tool_order` order, with the hub-block markup
of the guide and solution indexes. The menu entry shows only in the languages
where the hub exists; in German and Dutch, only in the footer (see Layout).

The first tool is the GRD lookup, "Quel est mon GRD ?" (`ref: tool-dso`), with
its municipality table (`ref: tool-dso-list`).

### Data flow

1. `belgian-dso-map` publishes a release. `scripts/sync_dso.py` checks it
   against its `SHA256SUMS` and the data contract, then copies it byte for byte
   into `_data/dso/` and writes `meta.yml`. This is the only way those files
   change; the weekly `dso-data-bump.yml` workflow opens the pull request.
   `.gitattributes` keeps them LF (`-text`).
2. `_plugins/dso_pages.rb` validates the data on every build and fails it on
   any inconsistency. It writes `assets/data/dso-<version>.json`, gives the
   table page its data and dates the table page.
3. The tool page (`_layouts/tool.html` with `tool: dso`) carries no data.
   `_includes/dso-tool.html` holds the form, the strings (`grd_tool` of
   `_data/i18n/<lang>.yml`, as inline JSON in `data-dso-i18n`) and one
   `<template data-dso-region>` per region for the regulator, tariff and
   energy-sharing text.
4. `assets/js/grd-lookup.js`, an ES module loaded on that page only, fetches
   the JSON named by `data-dso-src` on the first focus or input, or at load
   when the address holds `#cp=`. The lookup itself is
   `assets/js/dso-lookup-core.js`, a port of `lookup.py`;
   `scripts/dso-lookup.test.mjs` runs the release's vectors through it, on the
   CSV and on the built JSON. Text is set with `textContent` only.
5. The table page (`_layouts/tool-dso-list.html`) is the no-JavaScript view:
   every commune by region and province, then the sources (`#sources`, the
   target of the result's "Sources" link) and the release's `ATTRIBUTION.md`.

Privacy: the search runs in the browser. The form names no control, so a
native submit (no JavaScript, or Enter before the module runs) cannot put the
postcode in the address or the server logs; it stays invisible
(`data-dso-pending`, its room kept) until the module has wired it, and
without JavaScript it leaves the page for the noscript notice.
`scripts/check_dso_dates.py` fails on a named control. The address keeps
`#cp=…&ins=…&s=…` so a result can be shared (also opened in the same tab:
`hashchange`), and on that page the Umami tag has `data-exclude-search` and
`data-exclude-hash`. The module sends one `grd-lookup` event per displayed
result, with `{region, elec, gas}` (operator ids) only. "Report an error" is
a `mailto:` without the postcode.

### Dates

- **Table page:** max(its front matter, `DSO_TEMPLATE_REVISION` in
  `_plugins/dso_pages.rb`, the data date). The data date is the latest
  `changed_at` of the rows, of the operators and notes they use (with the
  `dataset-<region>-…` notes of the regions present) and of every source, or
  `removed_max` of `meta.yml`.
- **Tool page:** its front matter only. **Hub:** max(its own and its
  children's front matter), never the table page's data date.
- `datePublished` comes from `date_published:`. Never `date:` on a page:
  jekyll-seo-tag would type it as a blog post (`og:type` article, a
  `BlogPosting` node), which `scripts/check_seo.py` refuses.
- No clock, file date or git: `scripts/check_dso_dates.py` recomputes every
  date with `scripts/dso_dates.py`, compares it with the sitemap, and greps
  the plugin for anything that could read one.
- **Editing strings or templates moves a date by hand:**
  - `_layouts/tool-dso-list.html`, or `grd_tool.table`, `regions`,
    `provinces`, `regulators` or `flags`: set `DSO_TEMPLATE_REVISION` to the
    day of the change;
  - the tool page's text, `_includes/dso-tool.html`, `grd-lookup.js`, or
    `grd_tool.ui` or `regional`: bump the tool page's `last_modified_at` in
    each language concerned.

### Choice: radio group

When a postcode covers several communes, or a commune several operators, the
tool asks with a radio group and never submits on its own:

- `fieldset.dso-choice__fieldset` with a `legend`, then one
  `label.dso-radio` per option wrapping `input.dso-radio__input` and its text;
- the whole row is the target, at least 44px high, with a
  `--color-border-strong` border and `--radius-md`;
- checked: the tint background and a 2px `--color-primary` border (no
  shadow); `accent-color: var(--color-primary)` on the input;
- focus: the shared 2px ring, drawn around the whole row
  (`:has(:focus-visible)`);
- an "Afficher" button (`.btn-outline`) shows the answer.

### Result and table

- The result is a tinted panel, like `.post-cta`, with two surface panels
  (electricity, gas), then the notes, the regulator and tariffs, how to check,
  energy sharing and a footer (data version, sources, report an error, copy
  the link). `valid_from` dates the whole row, so it goes with the notes,
  never in a panel.
- An invalid postcode: `aria-invalid`, and the message in the field's
  `role="alert"` paragraph (always in the page, empty until then), so it is
  announced while the focus stays on the field.
- Tables keep the same five columns everywhere (`table-layout: fixed`). On a
  phone they scroll inside `.dso-table-wrap`, never the page, and the commune
  column stays in view. Rows carry `id="ins-<INS>"`; headers are
  `th scope="col"` and the commune is `th scope="row"`.

## The homepage grid

`scripts/build_quarter_hours.py` writes `_data/quarter_hours.json` and the
no-JavaScript poster `assets/images/quarter-hours-poster.svg`. The data is:

- **Production:** PVGIS for a 24 kWc roof in Namur, with the weather of 2023.
- **Consumption:** a documented profile of 3 500 kWh a year for each of 12
  households.
- **Shared:** min(production, consumption) in each quarter-hour.

`main.js` draws the 28 days that end today (Brussels time) at the same calendar
dates, marks the current quarter-hour, and builds the table that is the
accessible view. The page labels it as an example and names the sources.

## Motion and accessibility

- Focus: a 2px ring with a 2px offset, `--color-focus`, on every interactive
  element.
- `prefers-reduced-motion`: no smooth scrolling, no transitions, no grid
  animation.
- Links in running text are underlined. Glossary links are dotted and use the
  help cursor.
- Headings have `scroll-margin-top`, so anchor jumps clear the sticky header.
- The mobile menu scrolls on its own and closes with Escape. Focus returns to
  the burger.

## Checks

```bash
node --test scripts/dso-lookup.test.mjs            # Node 22.7 or later
bundle exec jekyll build
python scripts/check_seo.py --site _site
python scripts/check_site.py --site _site --allow-placeholders
python scripts/check_dso_dates.py --site _site    # CI adds --require-release
DSO_JSON_DIR=_site/assets/data node --test scripts/dso-lookup.test.mjs
```

Keep exactly one `<h1>` per page. Never put Liquid in a post body. Keep every
`data-*` hook that `assets/js/main.js` reads.
