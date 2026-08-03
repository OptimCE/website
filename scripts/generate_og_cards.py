#!/usr/bin/env python3
"""Generate the social cards in `assets/images/og/`.

Every card is `og-<ref>-<lang>.png`, the exact filename `_plugins/i18n_metadata.rb`
looks for. A typo there is *silent*: the page falls back to the site-wide default
image and nothing warns you. That is the whole reason this script exists — the
geometry below was reverse-engineered pixel by pixel from the 88 cards committed
in one block by `4403a58`, and re-derived from scratch on three separate
occasions before anyone thought to version it.

Usage:
    # one article, all four languages (title read from the post front matter)
    python scripts/generate_og_cards.py --ref choose-electricity-tariff-belgium

    # explicit titles instead of reading _posts/
    python scripts/generate_og_cards.py --ref my-ref --title fr="Mon titre" --title en="My title"

    # regenerate an existing card and compare against the committed one
    python scripts/generate_og_cards.py --verify --ref read-electricity-bill-belgium

`--verify` never writes: it re-renders the card and compares the vertical bands
of non-white pixels against the file on disk. Use it after touching this script.

Known limit of `--verify`: exact reproduction is unattainable. The woff2 files in
`assets/fonts/` are subsetted, so their metrics and kerning differ from the
original Plus Jakarta Sans, and no title size reproduces the committed cards'
line-width ratios. A spot check over seven article refs (28 cards) matched 22
exactly; the six misses are all line-breaking decisions on titles whose full
single-line ink width exceeds ~1600px, where a few pixels of metric drift flip a
break point. Titles that fit two lines under ~1000px per line reproduce reliably.
Treat a MISMATCH on a long title as "look at it", not "it is broken".

Requires `fonttools[woff]` (to decode the repo's woff2) and `Pillow`.
"""

from __future__ import annotations

import argparse
import io
import pathlib
import re
import sys

try:
    from fontTools.ttLib import TTFont
    from PIL import Image, ImageDraw, ImageFont
except ImportError as exc:  # pragma: no cover - environment problem, not logic
    sys.exit(f"missing dependency: {exc}. Install with: pip install 'fonttools[woff]' Pillow")

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
OG_DIR = ROOT / "assets" / "images" / "og"
POSTS = ROOT / "_posts"

LANGS = ("fr", "en", "de", "nl")

# --- Geometry, measured on og-why-electricity-bill-stays-high-fr.png -----------
# Note the declared size in _plugins/i18n_metadata.rb is 1200x630. The files are
# 1600x840 — same 1.905 ratio at 2x density. Do not "fix" one to match the other.
W, H = 1600, 840
BG = "#FFFFFF"
BAR = ("#2e7d32", (0, 0, 24, 829))          # left vertical bar, x 0-23, y 0-828
FOOT = ("#e8f5e9", (0, 829, W, 840))        # bottom band, y 829-839
TITLE_X, TITLE_Y, TITLE_LEADING = 125, 305, 101
TITLE_INK = "#212529"
TITLE_SIZE = 78                             # calibrated 2026-07-30; see note below
BASELINE_X, BASELINE_Y = 123, 715
BASELINE_INK = "#495057"
DOMAIN_RIGHT, DOMAIN_Y = 1478, 717
DOMAIN_INK = "#66bb6a"
BODY_SIZE = 36
TITLE_MAX_W = DOMAIN_RIGHT - TITLE_X        # usable ink width for the title

# The lockup (clover + "OptimCE" wordmark) is cropped from an existing card
# rather than rebuilt: assets/images/logo-512.png is an opaque P-mode square,
# not a cut-out logo, so compositing it does not reproduce the original.
LOCKUP_BOX = (100, 90, 420, 180)
LOCKUP_SOURCE = "og-home-fr.png"

# Baselines live in _data/i18n/<lang>.yml as "OptimCE — plateforme open source…";
# the card shows the tail with an initial capital and a typographic apostrophe.
BASELINES = {
    "fr": "Plateforme open source pour les communautés d'énergie",
    "en": "Open-source platform for energy communities",
    "de": "Open-Source-Plattform für Energiegemeinschaften",
    "nl": "Opensource-platform voor energiegemeenschappen",
}


def load_font(stem: str, size: int) -> ImageFont.FreeTypeFont:
    """Decode one of the repo's subsetted woff2 files into a usable TTF."""
    src = FONTS / f"{stem}.woff2"
    if not src.exists():
        sys.exit(f"font not found: {src}")
    f = TTFont(str(src))
    f.flavor = None
    buf = io.BytesIO()
    f.save(buf)
    buf.seek(0)
    return ImageFont.truetype(buf, size)


def ink_width(font: ImageFont.FreeTypeFont, text: str) -> int:
    box = font.getbbox(text)
    return box[2] - box[0]


def wrap_balanced(font: ImageFont.FreeTypeFont, text: str, max_w: int) -> list[str]:
    """Break into the fewest lines, then minimise the widest line.

    A greedy fill is wrong here. On the reference card, greedy at 1360px gives
    "Facture d'électricité : pourquoi elle reste" / "élevée"; the committed card
    reads "Facture d'électricité :" / "pourquoi elle reste élevée".
    """
    words = text.split()
    if ink_width(font, text) <= max_w:
        return [text]

    for n in range(2, len(words) + 1):
        best, best_cost = None, None
        # choose n-1 break points minimising the widest resulting line
        def search(start: int, remaining: int, acc: list[str]) -> None:
            nonlocal best, best_cost
            if remaining == 1:
                line = " ".join(words[start:])
                w = ink_width(font, line)
                if w > max_w:
                    return
                cost = max([ink_width(font, x) for x in acc] + [w])
                if best_cost is None or cost < best_cost:
                    best, best_cost = acc + [line], cost
                return
            for end in range(start + 1, len(words) - remaining + 2):
                line = " ".join(words[start:end])
                if ink_width(font, line) > max_w:
                    break
                search(end, remaining - 1, acc + [line])

        search(0, n, [])
        if best:
            return best

    return words  # one word per line; the title is pathologically long


def draw_ink(draw: ImageDraw.ImageDraw, xy, text, font, fill, anchor_right=False):
    """Place text by its ink box, not its em box.

    Using the em box shifts everything by a few pixels against the existing
    cards, which is immediately visible when they sit side by side in a share
    gallery.
    """
    box = font.getbbox(text)
    x, y = xy
    if anchor_right:
        x -= box[2] - box[0]
    draw.text((x - box[0], y - box[1]), text, font=font, fill=fill)


def render(title: str, lang: str) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    colour, box = BAR
    draw.rectangle([box[0], box[1], box[2] - 1, box[3] - 1], fill=colour)
    colour, box = FOOT
    draw.rectangle([box[0], box[1], box[2] - 1, box[3] - 1], fill=colour)

    source = OG_DIR / LOCKUP_SOURCE
    if not source.exists():
        sys.exit(f"lockup source card not found: {source}")
    img.paste(Image.open(source).convert("RGB").crop(LOCKUP_BOX), LOCKUP_BOX[:2])

    title_font = load_font("plus-jakarta-sans-700", TITLE_SIZE)
    body_font = load_font("source-sans-3-400", BODY_SIZE)

    lines = wrap_balanced(title_font, title, TITLE_MAX_W)
    # Centre the block on the reference two-line position.
    y = TITLE_Y - (len(lines) - 2) * TITLE_LEADING // 2
    for line in lines:
        draw_ink(draw, (TITLE_X, y), line, title_font, TITLE_INK)
        y += TITLE_LEADING

    baseline = BASELINES[lang].replace("'", "’")
    draw_ink(draw, (BASELINE_X, BASELINE_Y), baseline, body_font, BASELINE_INK)
    draw_ink(draw, (DOMAIN_RIGHT, DOMAIN_Y), "optimce.be", body_font, DOMAIN_INK,
             anchor_right=True)
    return img


def save(img: Image.Image, path: pathlib.Path) -> None:
    """Palettised PNG, like the committed cards (18-26 KB rather than ~200)."""
    img.convert("P", palette=Image.ADAPTIVE, colors=255).save(path, optimize=True)


def ink_bands(img: Image.Image) -> list[tuple[int, int]]:
    """Vertical runs of rows containing non-white pixels, ignoring the left bar."""
    px = img.convert("RGB").crop((40, 0, W, 828)).load()
    rows = []
    for y in range(828):
        if any(px[x, y] != (255, 255, 255) for x in range(0, W - 40, 3)):
            rows.append(y)
    bands, start, prev = [], None, None
    for y in rows:
        if start is None:
            start = prev = y
        elif y - prev > 4:
            bands.append((start, prev))
            start = y
        prev = y
    if start is not None:
        bands.append((start, prev))
    return bands


def titles_from_posts(ref: str) -> dict[str, str]:
    found = {}
    for path in POSTS.glob("*.md"):
        head = path.read_text(encoding="utf-8").split("---", 2)[1]
        if not re.search(rf"^ref: {re.escape(ref)}\s*$", head, re.M):
            continue
        lang = re.search(r"^lang: (\w+)$", head, re.M)
        title = re.search(r'^title: "(.*)"$', head, re.M)
        if lang and title:
            found[lang.group(1)] = title.group(1)
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", required=True, help="article ref, e.g. read-electricity-bill-belgium")
    ap.add_argument("--title", action="append", default=[], metavar="LANG=TITLE",
                    help="override the title for one language (repeatable)")
    ap.add_argument("--lang", action="append", choices=LANGS,
                    help="restrict to these languages (default: all four)")
    ap.add_argument("--verify", action="store_true",
                    help="re-render and compare against the committed card; writes nothing")
    args = ap.parse_args()

    titles = titles_from_posts(args.ref)
    for override in args.title:
        lang, _, value = override.partition("=")
        if lang not in LANGS:
            sys.exit(f"--title expects LANG=TITLE with LANG in {LANGS}, got {override!r}")
        titles[lang] = value

    langs = args.lang or list(LANGS)
    missing = [lg for lg in langs if lg not in titles]
    if missing:
        sys.exit(f"no title for {', '.join(missing)} — no post with ref={args.ref!r} "
                 f"and pass --title {missing[0]}=... to supply one")

    OG_DIR.mkdir(parents=True, exist_ok=True)
    failures = 0
    for lang in langs:
        path = OG_DIR / f"og-{args.ref}-{lang}.png"
        img = render(titles[lang], lang)
        if args.verify:
            if not path.exists():
                print(f"MISSING  {path.name}")
                failures += 1
                continue
            got, want = ink_bands(img), ink_bands(Image.open(path))
            ok = len(got) == len(want) and all(
                abs(a[0] - b[0]) <= 6 and abs(a[1] - b[1]) <= 6 for a, b in zip(got, want)
            )
            print(f"{'OK      ' if ok else 'MISMATCH'} {path.name}")
            if not ok:
                print(f"         rendered {got}")
                print(f"         on disk  {want}")
                failures += 1
        else:
            save(img, path)
            print(f"wrote {path.relative_to(ROOT)}  "
                  f"({path.stat().st_size // 1024} KB, "
                  f"{len(wrap_balanced(load_font('plus-jakarta-sans-700', TITLE_SIZE), titles[lang], TITLE_MAX_W))} lines)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
