#!/usr/bin/env python3
"""Build the site's web fonts from the OFL variable sources, and the fallback metrics.

    python scripts/subset_fonts.py            # writes assets/fonts/*-var.woff2
    python scripts/subset_fonts.py --check    # rebuilds in memory, compares, writes nothing

The site uses two families: Plus Jakarta Sans (headings, UI) and Source Sans 3
(text). Each is taken from the variable TTF published in google/fonts, its
weight axis is narrowed to the weights the stylesheet uses, and it is subset
to the characters the four languages need. That subset is what the previous
static files lacked: italics, the arrows and the maths signs the articles use
(→ ≈ ≤ ≥ −), sub- and superscripts, the non-breaking hyphen, and the case,
tabular and fraction features.

Two older static files stay untouched on purpose: scripts/generate_og_cards.py
loads plus-jakarta-sans-700.woff2 and source-sans-3-400.woff2 by name, and the
social cards must keep rendering exactly as before.

The script also prints the @font-face overrides for the metric-matched Arial
fallbacks (size-adjust, ascent/descent/line-gap overrides), so the text keeps
its place while the web font loads. Paste them into _sass/_fonts.scss.
"""
import argparse
import io
import sys
import tempfile
import urllib.request
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = Path(__file__).resolve().parent.parent
FONTS_DIR = ROOT / "assets" / "fonts"
CACHE = Path(tempfile.gettempdir()) / "optimce-font-sources"

GF = "https://github.com/google/fonts/raw/main/ofl"
SOURCES = {
    "plus-jakarta-sans": f"{GF}/plusjakartasans/PlusJakartaSans%5Bwght%5D.ttf",
    "source-sans-3": f"{GF}/sourcesans3/SourceSans3%5Bwght%5D.ttf",
    "source-sans-3-italic": f"{GF}/sourcesans3/SourceSans3-Italic%5Bwght%5D.ttf",
}

# output file -> (source, weight range kept on the wght axis)
BUILDS = {
    "plus-jakarta-sans-var.woff2": ("plus-jakarta-sans", (500, 800)),
    "source-sans-3-var.woff2": ("source-sans-3", (400, 600)),
    "source-sans-3-italic-var.woff2": ("source-sans-3-italic", (400, 600)),
}

UNICODES = (
    "U+0000-00FF,"        # Basic Latin + Latin-1 (« » × ÷ ± · ¹ ² ³ °)
    "U+0100-017F,"        # Latin Extended-A (œ, ŀ, č …)
    "U+0192,U+0218-021B,U+02BB-02BC,U+02C6,U+02DA,U+02DC,"
    "U+2000-206F,"        # General Punctuation: – — ‘ ’ “ ” „ … ‰ ‑ and the narrow no-break space
    "U+2070-209F,"        # superscripts and subscripts (₂ in CO₂)
    "U+20AC,U+2113,U+2116,U+2122,"
    "U+2190-2195,"        # arrows ← ↑ → ↓
    "U+2212,U+2215,U+2219,U+221E,U+2248,U+2260,U+2264-2265,"  # − ∕ ∙ ∞ ≈ ≠ ≤ ≥
    "U+FEFF,U+FFFD"
)

FEATURES = [
    "kern", "liga", "calt", "ccmp", "locl", "mark", "mkmk", "rlig",
    "case", "sups", "subs", "sinf", "frac", "numr", "dnom", "ordn",
    "pnum", "tnum", "lnum", "zero",
]

# Text used to compare average glyph widths with Arial (French and English,
# the two languages most pages are read in; letters, spaces and digits).
WIDTH_SAMPLE = (
    "La communauté d'énergie partage l'électricité produite par les panneaux "
    "solaires entre ses membres, quart d'heure par quart d'heure. "
    "The energy community shares the electricity its members produce, "
    "quarter-hour by quarter-hour, 2026 kWh 850 € 4 250 €."
)


def parse_unicodes(spec):
    out = set()
    for part in spec.split(","):
        part = part.strip().upper().replace("U+", "")
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-")
            out.update(range(int(a, 16), int(b, 16) + 1))
        else:
            out.add(int(part, 16))
    return out


def source_bytes(name):
    CACHE.mkdir(parents=True, exist_ok=True)
    cached = CACHE / f"{name}.ttf"
    if not cached.exists():
        print(f"downloading {name} …", file=sys.stderr)
        with urllib.request.urlopen(SOURCES[name], timeout=120) as r:
            cached.write_bytes(r.read())
    return cached.read_bytes()


def build(source, weights):
    font = TTFont(io.BytesIO(source_bytes(source)))
    instancer.instantiateVariableFont(font, {"wght": weights}, inplace=True)
    # Round-trip before subsetting: the instancer leaves gvar partly lazy, and
    # the subsetter then fails on glyphs it cannot find (.notdef).
    staged = io.BytesIO()
    font.save(staged)
    font = TTFont(io.BytesIO(staged.getvalue()))
    options = subset.Options()
    options.layout_features = FEATURES
    options.notdef_outline = True
    options.name_IDs = ["*"]
    options.name_languages = ["*"]
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(unicodes=parse_unicodes(UNICODES))
    subsetter.subset(font)
    font.flavor = "woff2"
    buf = io.BytesIO()
    font.save(buf)
    return buf.getvalue()


def vertical_metrics(font):
    upm = font["head"].unitsPerEm
    os2 = font["OS/2"]
    if os2.fsSelection & (1 << 7):  # USE_TYPO_METRICS
        return upm, os2.sTypoAscender, -os2.sTypoDescender, os2.sTypoLineGap
    hhea = font["hhea"]
    return upm, hhea.ascent, -hhea.descent, hhea.lineGap


def average_width(font):
    upm = font["head"].unitsPerEm
    cmap = font.getBestCmap()
    hmtx = font["hmtx"]
    widths = [hmtx[cmap[ord(c)]][0] for c in WIDTH_SAMPLE if ord(c) in cmap]
    return sum(widths) / len(widths) / upm


def fallback_overrides(source, weight, arial_file):
    font = TTFont(io.BytesIO(source_bytes(source)))
    instancer.instantiateVariableFont(font, {"wght": weight}, inplace=True)
    arial = TTFont(arial_file)
    size_adjust = average_width(font) / average_width(arial)
    upm, asc, desc, gap = vertical_metrics(font)
    pct = lambda v: f"{v / upm / size_adjust * 100:.2f}%"
    return {
        "size-adjust": f"{size_adjust * 100:.2f}%",
        "ascent-override": pct(asc),
        "descent-override": pct(desc),
        "line-gap-override": pct(gap),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="rebuild in memory and compare, write nothing")
    args = ap.parse_args()

    status = 0
    for out_name, (source, weights) in BUILDS.items():
        data = build(source, weights)
        target = FONTS_DIR / out_name
        if args.check:
            same = target.exists() and target.read_bytes() == data
            print(f"{'OK      ' if same else 'MISMATCH'} {out_name}")
            status |= 0 if same else 1
        else:
            target.write_bytes(data)
            print(f"wrote {out_name}: {len(data) / 1024:.1f} KB (wght {weights[0]}–{weights[1]})")

    windows_fonts = Path("C:/Windows/Fonts")
    arial = {400: windows_fonts / "arial.ttf", 700: windows_fonts / "arialbd.ttf"}
    if all(p.exists() for p in arial.values()):
        print("\n// Metric-matched fallbacks (paste into _sass/_fonts.scss)")
        for family, source, weight in (
            ("Source Sans 3 Fallback", "source-sans-3", 400),
            ("Plus Jakarta Sans Fallback", "plus-jakarta-sans", 700),
        ):
            o = fallback_overrides(source, weight, arial[weight])
            print(f"// {family}: {source} at {weight} against Arial {weight}")
            for k, v in o.items():
                print(f"//   {k}: {v};")
    else:
        print("\n(Arial not found: fallback metrics not computed)", file=sys.stderr)
    return status


if __name__ == "__main__":
    sys.exit(main())
