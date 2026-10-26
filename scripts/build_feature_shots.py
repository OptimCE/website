#!/usr/bin/env python3
"""Build the product pages' screenshots from the user guide's captures.

    python scripts/build_feature_shots.py [--guide PATH] [--langs fr en de nl]

The user guide (sibling repository, ../user-guide by default) captures each
scenario in French, English, German and Dutch on a 1440x900 desktop. Use a
checkout of what guide.optimce.be publishes (origin/main of OptimCE/user-guide),
or the Steppy build it is exported from (../e2e/output/static/generated): the
step numbers below are those of the 2026-09-04 capture (French, English) and of
the 2026-10-24 one (German, Dutch). --langs rebuilds some languages only.

Each shot is one step of one scenario, cropped to the part of the screen the
page talks about, without the app's sidebar (no toasts, no Steppy highlight, no
untranslated keys): the pages show it in a 38rem column, where a full-width
capture would be too small to read.
Each page uses the capture in its own language (_includes/product-shot.html
picks it).

Writes, in assets/images/product/features/, for each shot and language:
  <shot>-<lang>.webp       the crop at its own width (1x on a wide screen)
  <shot>-<lang>-800.webp   the same, 800px wide
and _data/feature_shots.json, the size of each shot in each language, which
the include reads so that the page reserves the image's space before it loads
(the languages not rebuilt keep their entry).

Rerun it when the guide is captured again, look at every crop, and move a
step number or a crop box if the screen changed.
"""
import argparse
import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "assets" / "images" / "product" / "features"
DATA = ROOT / "_data" / "feature_shots.json"
LANGS = ("fr", "en", "de", "nl")
WIDTHS = (None, 800)  # None: the crop's own width (the base file)
QUALITY = 82

# Shot: (scenario, capture, crop box on the 1440x900 desktop capture).
SHOTS = {
    # The two prices of an operation: kind, scope, price per kWh, validity.
    "billing-tariffs": ("billing-tarification-pay", "step-38.png", (240, 0, 1270, 450)),
    # A member's "My invoices": number, status, amount, structured communication.
    "billing-member": ("billing-member-view", "step-20.png", (350, 140, 1160, 470)),
    # A dossier's page: status, allowed transitions, documents, deadlines, history.
    "cwape-dossier": ("admin-doc-dossier-create", "step-32.png", (230, 0, 1280, 560)),
    # The deadline board: due date, type, dossier, status.
    "cwape-deadlines": ("admin-doc-submit-deadline", "step-34.png", (240, 0, 1270, 540)),
    # Starting a generation: the algorithm, its description, the data file.
    "key-generation": ("algorithm-generate", "step-34.png", (110, 0, 1400, 520)),
    # The wizard's review grid: iterations, percentages, consumers, pro rata.
    "key-wizard": ("key-create-wizard", "step-38.png", (110, 225, 1400, 790)),
    # A new community's dashboard: what is left to fill in, sharing operations.
    "start-dashboard": ("community-create", "step-26.png", (240, 0, 1280, 560)),
    # The member wizard's first step: individual or company, then three steps.
    "start-member": ("member-create", "step-32.png", (300, 240, 1140, 665)),
}

# (shot, lang): a crop box for a language whose screen is laid out differently.
BOXES = {
    # The longer labels wrap the filters on two rows: go down to the structured communication.
    ("billing-member", "de"): (350, 140, 1160, 560),
    ("billing-member", "nl"): (350, 140, 1160, 560),
    # The wizard's dialog is wider (its steps are joined by lines).
    ("start-member", "de"): (250, 240, 1190, 665),
    ("start-member", "nl"): (250, 240, 1190, 665),
}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--guide", type=Path, default=ROOT.parent / "user-guide",
                    help="the user guide repository (default: ../user-guide)")
    ap.add_argument("--langs", nargs="+", choices=LANGS, default=LANGS,
                    help="the languages to build (default: all)")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sizes = json.loads(DATA.read_text(encoding="utf-8")) if DATA.exists() else {}
    for shot, (scenario, step, default_box) in SHOTS.items():
        for lang in args.langs:
            box = BOXES.get((shot, lang), default_box)
            src = args.guide / "assets" / scenario / lang / "desktop" / step
            if not src.exists():
                sys.exit(f"missing capture: {src}")
            capture = Image.open(src).convert("RGB")
            if capture.width < box[2] or capture.height < box[3]:
                sys.exit(f"{src} is {capture.width}x{capture.height}, smaller than the crop {box}")
            crop = capture.crop(box)
            sizes.setdefault(shot, {})[lang] = {"width": crop.width, "height": crop.height}
            for width in WIDTHS:
                if width is None:
                    image, name = crop, f"{shot}-{lang}.webp"
                else:
                    height = round(crop.height * width / crop.width)
                    image, name = crop.resize((width, height), Image.LANCZOS), f"{shot}-{lang}-{width}.webp"
                out = OUT_DIR / name
                image.save(out, "WEBP", quality=QUALITY, method=6)
                print(f"wrote {out.relative_to(ROOT)}: {image.width}x{image.height}, "
                      f"{out.stat().st_size / 1024:.1f} KB")

    DATA.write_text(json.dumps(sizes, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {DATA.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
