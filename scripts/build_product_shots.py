#!/usr/bin/env python3
"""Build the homepage's product shots from the user guide's captures.

    python scripts/build_product_shots.py [--guide PATH] [--langs fr en de nl]

The user guide (sibling repository, ../user-guide by default, or the Steppy
build it is exported from, ../e2e/output/static/generated) captures the
manager's dashboard tour in French, English, German and Dutch, on a desktop
(1440x900) and on a phone (390x844 at 3x). Step 9 is the dashboard.
_includes/modules.html shows the phone shot below 768px and the desktop shot
from there, in the page's language. --langs rebuilds some languages only.

Writes, in assets/images/product/, for each language:
  dashboard-<lang>.webp            desktop: the top-left 1290x712 of the capture
  dashboard-<lang>-800.webp        the same, 800px wide
  dashboard-<lang>-phone.webp      phone: the top of the screen, down to the
                                   end of the "energy at a glance" card,
                                   1170px wide (3x)
  dashboard-<lang>-phone-780.webp  the same, 780px wide (2x)

Rerun it when the tour is captured again. Then check that the phone crop
still ends between two cards, and update the sizes in modules.html if they
changed.
"""
import argparse
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "assets" / "images" / "product"
LANGS = ("fr", "en", "de", "nl")
STEP = "step-09.png"
QUALITY = 82

# Shot: (capture folder, crop box, widths written; the first is the base file).
SHOTS = {
    "desktop": ("desktop", (0, 0, 1290, 712), (1290, 800)),
    # 2022 is the middle of the gap under the third card, at 3x (674 CSS px).
    "phone": ("mobile", (0, 0, 1170, 2022), (1170, 780)),
}


def file_name(lang, shot, width, base_width):
    stem = f"dashboard-{lang}" if shot == "desktop" else f"dashboard-{lang}-{shot}"
    return f"{stem}.webp" if width == base_width else f"{stem}-{width}.webp"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--guide", type=Path, default=ROOT.parent / "user-guide",
                    help="the user guide repository (default: ../user-guide)")
    ap.add_argument("--langs", nargs="+", choices=LANGS, default=LANGS,
                    help="the languages to build (default: all)")
    args = ap.parse_args()
    tour = args.guide / "assets" / "dashboard-manager-tour"

    for lang in args.langs:
        for shot, (folder, box, widths) in SHOTS.items():
            src = tour / lang / folder / STEP
            if not src.exists():
                sys.exit(f"missing capture: {src}")
            capture = Image.open(src).convert("RGB")
            if capture.width < box[2] or capture.height < box[3]:
                sys.exit(f"{src} is {capture.width}x{capture.height}, smaller than the crop {box}")
            crop = capture.crop(box)
            for width in widths:
                height = round(crop.height * width / crop.width)
                image = crop if width == crop.width else crop.resize((width, height), Image.LANCZOS)
                out = OUT_DIR / file_name(lang, shot, width, widths[0])
                image.save(out, "WEBP", quality=QUALITY, method=6)
                print(f"wrote {out.relative_to(ROOT)}: {width}x{height}, {out.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
