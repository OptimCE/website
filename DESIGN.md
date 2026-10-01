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

### Hosting cards (homepage)

Two cards of equal weight: app.optimce.be, and self-hosting. The self-hosting
card has no install commands: the development monorepo is not the way to
deploy. Its "Developer documentation" button reads `developers_url` in
`_config.yml` and stays hidden while that is empty, so the site never links to
a documentation site that is not online yet.

### Article rail

The rail holds "On this page" and a call to action.

- `_layouts/post.html` lists the article's own H2s when there are at least
  three, so the list works without JavaScript.
- `main.js` opens it in the rail from 1200px, folds it above the text below
  that width, and marks the section being read.

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
bundle exec jekyll build
python scripts/check_seo.py --site _site
python scripts/check_site.py --site _site --allow-placeholders
```

Keep exactly one `<h1>` per page. Never put Liquid in a post body. Keep every
`data-*` hook that `assets/js/main.js` reads.
