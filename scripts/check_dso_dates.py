#!/usr/bin/env python3
"""Post-build checks of the GRD tool: data release, sitemap dates, browser JSON.

Complements check_seo.py and check_site.py for the pages generated from
_data/dso/ (_plugins/dso_pages.rb). Each check guards a failure that would
still deploy green:

  guard     _plugins/dso_pages.rb calls nothing that could read the clock, a
            file date or a command (backtick, %x, IO.popen, Open3, system(,
            spawn/exec/fork, Kernel#open, IO.read and the other IO class
            readers and writers, Time.now/Time.new, Date.today, DateTime.now,
            mtime/ctime/atime/birthtime, File.stat, site.time): the dates
            below then depend only on the files, and two builds give the
            same sitemap
  data      _data/dso/ is a whole release: SHA256SUMS rule, headers,
            data_version, dates on or before the version date, CHANGES.md,
            meta.yml. --require-release (CI) refuses a draft
  sitemap   each tools page's lastmod is the date scripts/dso_dates.py
            computes from the files (table page: max(front matter,
            DSO_TEMPLATE_REVISION, data date); tool page: front matter; hub:
            max of its own and its children's front matter), at 00:00:00
  json      exactly one _site/assets/data/dso-<version>.json, of the synced
            version and data date, with every row of dso_lookup.csv
  pages     every tool page's data-dso-src points at that file, and every
            table page's data-dso-data-date is the data date. The lookup form
            names no control: a native submit (no JavaScript, or Enter before
            the module runs) would otherwise put the postcode in the address
            and the server logs. With --require-release the hub, tool and
            table pages exist in fr, en, de and nl

Dates are compared on their date part and time. The UTC offset is checked
only off Windows: there Jekyll fixes one offset for the whole build from the
DST state of the build day (jekyll/utils/win_tz.rb), so a winter date shows
+02:00 locally while CI renders +01:00.

stdlib only. Usage:
    python scripts/check_dso_dates.py --site _site [--root .] [--require-release]

Exit code 1 if any check fails.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree

import dso_data
import dso_dates

SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
LASTMOD_RE = re.compile(r"([0-9]{4}-[0-9]{2}-[0-9]{2})T([0-9]{2}:[0-9]{2}:[0-9]{2})(Z|[+-][0-9]{2}:[0-9]{2})")
LANGS = ("fr", "en", "de", "nl")
# Calls that could make a date depend on the build rather than on the files.
# Full-line comments are skipped; the plugin keeps these words out of strings.
GUARD_PATTERNS = (
    ("backtick", re.compile(r"`")),
    ("%x", re.compile(r"%x\W")),
    ("IO.popen", re.compile(r"\bIO\.popen\b")),
    ("Open3", re.compile(r"\bOpen3\b")),
    ("system/spawn/exec/fork", re.compile(r"\b(?:system|spawn|exec|fork)\s*[(\"']")),
    # Kernel#open runs a command for a "|cmd" name; File.open never does.
    ("Kernel#open", re.compile(r"(?<![\w.:])(?:Kernel\.)?open\s*[(\"']")),
    # So do the IO class methods (File's never): IO.read("|cmd") and the like.
    ("IO read/write", re.compile(r"\bIO\.(?:read|readlines|foreach|write|binread|binwrite)\b")),
    ("Time.now", re.compile(r"\bTime\.(?:now|new)\b")),
    ("Date.today", re.compile(r"\bDate\.today\b")),
    ("DateTime.now", re.compile(r"\bDateTime\.now\b")),
    ("file times", re.compile(r"\b(?:[mca]time|birthtime)\b")),
    ("File.stat", re.compile(r"\bFile\.l?stat\b|\bFile::Stat\b")),
    ("site.time", re.compile(r"\bsite\.time\b")),
    ("clock", re.compile(r"\bProcess\.clock_gettime\b")),
)


class Attributes(HTMLParser):
    """Values of the data-dso-* attributes of one HTML file, and the named
    controls of its lookup form ([data-dso-form])."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.values: dict[str, list[str]] = defaultdict(list)
        self.forms = 0
        self.form_names: list[str] = []
        self._in_form = False

    def handle_starttag(self, tag, attrs):
        names = dict(attrs)
        for name, value in attrs:
            if name in ("data-dso-src", "data-dso-data-date"):
                self.values[name].append(value or "")
        if tag == "form" and "data-dso-form" in names:
            self.forms += 1
            self._in_form = True
        elif self._in_form and names.get("name"):
            self.form_names.append(f"<{tag} name={names['name']!r}>")

    def handle_endtag(self, tag):
        if tag == "form":
            self._in_form = False


def static_guard(source: str) -> list[str]:
    problems = []
    for number, line in enumerate(source.split("\n"), start=1):
        if line.lstrip().startswith("#"):
            continue
        for label, pattern in GUARD_PATTERNS:
            if pattern.search(line):
                problems.append(f"{dso_dates.PLUGIN.as_posix()}:{number}: {label} ({line.strip()[:80]})")
    return problems


def brussels_offset(day: str) -> str | None:
    """+01:00 / +02:00 at 00:00 Europe/Brussels on `day`, or None where it cannot be trusted."""
    if sys.platform == "win32":
        return None
    try:
        from zoneinfo import ZoneInfo

        midnight = datetime.fromisoformat(f"{day}T00:00:00")
        offset = midnight.replace(tzinfo=ZoneInfo("Europe/Brussels")).utcoffset()
    except Exception:  # noqa: BLE001 - no tz database: the offset is not checked
        return None
    if offset is None:
        return None
    minutes = int(offset.total_seconds() // 60)
    sign = "+" if minutes >= 0 else "-"
    return f"{sign}{abs(minutes) // 60:02d}:{abs(minutes) % 60:02d}"


def built_file(site: Path, url: str) -> Path:
    path = urlsplit(url).path
    return site / path.lstrip("/") / "index.html" if path.endswith("/") else site / path.lstrip("/")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--site", default="_site", type=Path)
    ap.add_argument("--root", default=".", type=Path)
    ap.add_argument("--require-release", action="store_true",
                    help="refuse draft data and require the tools pages in all four languages (CI)")
    args = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    site, root = args.site, args.root
    data_dir = root / "_data" / "dso"
    errors: dict[str, list[str]] = defaultdict(list)
    notes: list[str] = []

    # --- guard ------------------------------------------------------------------------
    plugin = root / dso_dates.PLUGIN
    if plugin.is_file():
        errors["guard"] += static_guard(plugin.read_text(encoding="utf-8"))
    else:
        errors["guard"].append(f"{dso_dates.PLUGIN.as_posix()} is missing")

    # --- data -------------------------------------------------------------------------
    release = None
    try:
        release = dso_data.load_release(
            data_dir, allow_draft=not args.require_release, own_files=(dso_data.META,)
        )
        meta = dso_data.read_meta(data_dir)
        if meta is None:
            errors["data"].append("_data/dso/meta.yml is missing (run scripts/sync_dso.py)")
        else:
            errors["data"] += dso_data.check_meta(meta, release)
        if args.require_release and release.draft:
            errors["data"].append(f"{release.version} is a draft: CI deploys published releases only")
    except dso_data.DsoDataError as exc:
        errors["data"] += exc.problems
    except OSError as exc:
        errors["data"].append(f"cannot read _data/dso: {exc}")

    expected: dict[str, str] = {}
    stamp = None
    pages: list[dso_dates.SourcePage] = []
    try:
        pages = dso_dates.scan_pages(root)
        if release is not None:
            expected, stamp = dso_dates.expected(root, data_dir)
    except (dso_dates.DatesError, dso_data.DsoDataError, OSError) as exc:
        errors["data"].append(str(exc))
    if release is not None and stamp is not None and stamp > release.date:
        errors["data"].append(f"data date {stamp} is after the version date {release.date}")

    if args.require_release:
        for ref in (dso_dates.HUB_REF, dso_dates.TOOL_REF, dso_dates.LIST_REF):
            langs = sorted(page.lang for page in pages if page.ref == ref)
            if langs != sorted(LANGS):
                found = langs or "no language"
                errors["pages"].append(f"ref {ref}: pages in {found}, expected {list(LANGS)}")
    if not pages:
        notes.append("no tools page in the site yet: sitemap and page checks skipped")

    # --- sitemap ----------------------------------------------------------------------
    sitemap = site / "sitemap.xml"
    lastmods: dict[str, str] = {}
    if not sitemap.is_file():
        errors["sitemap"].append(f"{sitemap} not found: run jekyll build first")
    else:
        for element in ElementTree.parse(sitemap).getroot().findall(f"{SITEMAP_NS}url"):
            loc = (element.findtext(f"{SITEMAP_NS}loc") or "").strip()
            lastmods[urlsplit(loc).path] = (element.findtext(f"{SITEMAP_NS}lastmod") or "").strip()
    offsets_checked = False
    for url, day in sorted(expected.items()):
        if url not in lastmods:
            errors["sitemap"].append(f"{url}: not in the sitemap")
            continue
        match = LASTMOD_RE.fullmatch(lastmods[url])
        if not match:
            errors["sitemap"].append(f"{url}: lastmod {lastmods[url]!r} is not a timestamp")
            continue
        if match.group(1) != day:
            errors["sitemap"].append(f"{url}: lastmod {match.group(1)}, expected {day}")
        if match.group(2) != "00:00:00":
            errors["sitemap"].append(f"{url}: lastmod time {match.group(2)}, expected 00:00:00")
        offset = brussels_offset(day)
        if offset is not None:
            offsets_checked = True
            if match.group(3) != offset:
                errors["sitemap"].append(f"{url}: lastmod offset {match.group(3)}, Brussels is {offset}")
    if expected and not offsets_checked:
        notes.append("UTC offsets not checked (Windows, or no tz database): date and time only")

    # --- json -------------------------------------------------------------------------
    json_url = None
    if release is not None:
        data_out = site / "assets" / "data"
        found = sorted(p.name for p in data_out.glob("dso-*.json")) if data_out.is_dir() else []
        name = f"dso-{release.version}.json"
        json_url = f"/assets/data/{name}"
        if found != [name]:
            errors["json"].append(f"_site/assets/data holds {found or 'no dso-*.json'}, expected [{name!r}]")
        else:
            payload = json.loads((data_out / name).read_text(encoding="utf-8"))
            meta_out = payload.get("meta", {})
            if meta_out.get("version") != release.version:
                errors["json"].append(f"{name}: meta.version {meta_out.get('version')!r}")
            if stamp is not None and meta_out.get("data_date") != stamp:
                got = meta_out.get("data_date")
                errors["json"].append(f"{name}: meta.data_date {got!r}, expected {stamp}")
            rows = sum(len(group) for group in payload.get("postcodes", {}).values())
            if rows != len(release.rows):
                errors["json"].append(f"{name}: {rows} rows, dso_lookup.csv has {len(release.rows)}")

    # --- pages ------------------------------------------------------------------------
    for page in pages:
        if page.ref not in (dso_dates.TOOL_REF, dso_dates.LIST_REF):
            continue
        html = built_file(site, page.url)
        if not html.is_file():
            errors["pages"].append(f"{page.url}: not built ({html})")
            continue
        parser = Attributes()
        parser.feed(html.read_text(encoding="utf-8", errors="replace"))
        if page.ref == dso_dates.TOOL_REF:
            values = parser.values["data-dso-src"]
            if not values:
                errors["pages"].append(f"{page.url}: no data-dso-src attribute")
            for value in values:
                if json_url is not None and urlsplit(value).path != json_url:
                    errors["pages"].append(f"{page.url}: data-dso-src {value!r}, expected {json_url}")
            if parser.forms != 1:
                errors["pages"].append(f"{page.url}: {parser.forms} lookup forms (data-dso-form), expected 1")
            for control in parser.form_names:
                errors["pages"].append(
                    f"{page.url}: the lookup form names {control}: a native submit would send the postcode"
                )
        else:
            values = parser.values["data-dso-data-date"]
            if not values:
                errors["pages"].append(f"{page.url}: no data-dso-data-date attribute")
            for value in values:
                if stamp is not None and value != stamp:
                    errors["pages"].append(f"{page.url}: data-dso-data-date {value!r}, expected {stamp}")

    # --- report -----------------------------------------------------------------------
    checks = ("guard", "data", "sitemap", "json", "pages")
    for check in checks:
        for message in errors.get(check, []):
            print(f"FAIL  [{check}] {message}")
    for note in notes:
        print(f"NOTE  {note}")
    print()
    if release is not None:
        print(f"data      {release.version} of {release.date}, data date {stamp or '-'}")
    for url, day in sorted(expected.items()):
        print(f"expected  {day}  {url}")
    for check in checks:
        status = "FAIL" if errors.get(check) else "ok"
        print(f"{check:8} {status:5} {len(errors.get(check, [])):3} error(s)")
    total = sum(len(v) for v in errors.values())
    print(f"\n{total} error(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
