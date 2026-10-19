"""The one lastmod formula of the GRD tool pages (stdlib only).

_plugins/dso_pages.rb computes the same values at build time; this module is
the copy that scripts/sync_dso.py (which URLs a data bump moves) and
scripts/check_dso_dates.py (the built sitemap agrees) use. Change both or
neither.

  data_date      max of: changed_at of every dso_lookup row; changed_at of the
                 operators and notes the rows reference (elec_operator,
                 elec_designated, gas_operator, note_key, plus the
                 dataset-<region>-… notes of the regions present); changed_at
                 of ALL sources rows (the table page lists them); meta.yml
                 removed_max
  table page     (ref tool-dso-list) max(its own front-matter
                 last_modified_at, DSO_TEMPLATE_REVISION, data_date)
  tool page      (ref tool-dso) its front matter only
  tools hub      (ref tools) max(its own front matter, the front matter of
                 its children: pages with breadcrumb_parent: tools in the
                 same language)

Every value is a date (YYYY-MM-DD); the build renders it as 00:00 in
Europe/Brussels. No clock, no file mtime, no git: the result depends only on
the files.

Usage: python scripts/dso_dates.py [--root .] [--data-dir _data/dso]
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import dso_data

PLUGIN = Path("_plugins") / "dso_pages.rb"
TEMPLATE_REVISION_RE = re.compile(
    r"""^\s*DSO_TEMPLATE_REVISION\s*=\s*["']([0-9]{4}-[0-9]{2}-[0-9]{2})["']""", re.M
)
LIST_REF = "tool-dso-list"
TOOL_REF = "tool-dso"
HUB_REF = "tools"
HUB_PARENT = "tools"
# Language from the URL prefix, as _plugins/i18n_metadata.rb decides it (the
# prefixes of _config.yml `languages`).
LANG_PREFIXES = (("/en/", "en"), ("/de/", "de"), ("/nl/", "nl"))
# What Jekyll never reads as a page: _config.yml `exclude`, plus every name
# starting with "_" or "." (Jekyll's own rule).
EXCLUDED = {"node_modules", "vendor", "scripts", "gemfiles", "README.md", "DESIGN.md", "LICENSE"}
PAGE_SUFFIXES = (".md", ".markdown", ".html")
FRONT_MATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.S)
FM_KEYS = ("ref", "lang", "permalink", "last_modified_at", "breadcrumb_parent")


class DatesError(ValueError):
    pass


@dataclass(frozen=True)
class SourcePage:
    path: str  # relative to the root, for messages
    ref: str
    url: str
    lang: str
    last_modified_at: str  # YYYY-MM-DD, or "" when absent
    breadcrumb_parent: str


def _fm_value(raw: str) -> str:
    value = raw.strip()
    if value[:1] in ('"', "'"):
        quote = value[0]
        end = value.find(quote, 1)
        return value[1:end] if end > 0 else value[1:]
    return re.sub(r"\s+#.*$", "", value).strip()


def front_matter(text: str) -> dict[str, str] | None:
    """The top-level scalar keys this formula needs, or None without front matter."""
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None
    found: dict[str, str] = {}
    for line in re.split(r"\r?\n", match.group(1)):
        key_match = re.match(r"([A-Za-z_][A-Za-z0-9_]*):(.*)$", line)
        if key_match and key_match.group(1) in FM_KEYS:
            found[key_match.group(1)] = _fm_value(key_match.group(2))
    return found


def lang_of(url: str) -> str:
    for prefix, lang in LANG_PREFIXES:
        if url.startswith(prefix):
            return lang
    return "fr"


def scan_pages(root: Path) -> list[SourcePage]:
    """Source pages that belong to the tools section (hub, tool pages, children)."""
    pages = []
    stack = [root]
    while stack:
        directory = stack.pop()
        for entry in sorted(directory.iterdir()):
            name = entry.name
            if name.startswith(("_", ".")) or name in EXCLUDED:
                continue
            if entry.is_dir():
                stack.append(entry)
                continue
            if entry.suffix not in PAGE_SUFFIXES:
                continue
            fm = front_matter(entry.read_text(encoding="utf-8", errors="replace"))
            if fm is None:
                continue
            ref = fm.get("ref", "")
            parent = fm.get("breadcrumb_parent", "")
            if ref not in (LIST_REF, TOOL_REF, HUB_REF) and parent != HUB_PARENT:
                continue
            relative = entry.relative_to(root).as_posix()
            url = fm.get("permalink", "")
            if not url:
                raise DatesError(f"{relative}: a tools page needs a permalink")
            modified = fm.get("last_modified_at", "")
            if not dso_data.is_date(modified):
                raise DatesError(f"{relative}: last_modified_at {modified!r} is not a date (YYYY-MM-DD)")
            pages.append(SourcePage(relative, ref, url, lang_of(url), modified, parent))
    return sorted(pages, key=lambda page: page.url)


def template_revision(root: Path) -> str:
    source = (root / PLUGIN).read_text(encoding="utf-8")
    match = TEMPLATE_REVISION_RE.search(source)
    if not match:
        raise DatesError(f"{PLUGIN}: no DSO_TEMPLATE_REVISION = 'YYYY-MM-DD'")
    return match.group(1)


def data_date(tables: dict[str, list[dict[str, str]]], meta: dict) -> str:
    """See the module docstring. `tables` are the parsed CSV files of _data/dso."""
    rows = tables["dso_lookup.csv"]
    stamps = [row["changed_at"] for row in rows]
    operator_ids = {
        row[column]
        for row in rows
        for column in ("elec_operator", "elec_designated", "gas_operator")
        if row[column]
    }
    stamps += [op["changed_at"] for op in tables["operators.csv"] if op["id"] in operator_ids]
    regions = {row["region"] for row in rows}
    note_keys = {row["note_key"] for row in rows if row["note_key"]}
    for note in tables["notes.csv"]:
        if note["key"] in note_keys or dso_data.dataset_note_region(note["key"]) in regions:
            stamps.append(note["changed_at"])
    stamps += [source["changed_at"] for source in tables["sources.csv"]]
    if meta.get("removed_max"):
        stamps.append(meta["removed_max"])
    return max(stamps)


def read_tables(data_dir: Path) -> tuple[dict[str, list[dict[str, str]]], dict] | None:
    """The four dated tables and meta.yml of a data directory, or None if it holds no data."""
    if not (data_dir / "dso_lookup.csv").is_file():
        return None
    meta = dso_data.read_meta(data_dir)
    if meta is None:
        raise DatesError(f"{data_dir}: {dso_data.META} is missing (run scripts/sync_dso.py)")
    tables = {
        name: dso_data.parse_csv((data_dir / name).read_bytes(), name, dso_data.CSV_HEADERS[name])
        for name in dso_data.VERSIONED_FILES
    }
    return tables, meta


def expected(root: Path, data_dir: Path) -> tuple[dict[str, str], str | None]:
    """({url: lastmod date} for every tools page, data_date or None without data).

    A table page is left out when there are no data (it cannot be dated).
    """
    pages = scan_pages(root)
    loaded = read_tables(data_dir)
    stamp = data_date(*loaded) if loaded else None
    result: dict[str, str] = {}
    for page in pages:
        if page.ref == LIST_REF:
            if stamp is not None:
                result[page.url] = max(page.last_modified_at, template_revision(root), stamp)
        elif page.ref == HUB_REF:
            children = [
                child.last_modified_at
                for child in pages
                if child.breadcrumb_parent == HUB_PARENT and child.lang == page.lang
            ]
            result[page.url] = max([page.last_modified_at, *children])
        else:
            result[page.url] = page.last_modified_at
    return result, stamp


def main(argv: list[str] | None = None) -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Print the expected lastmod of the tools pages.")
    parser.add_argument("--root", default=".", type=Path)
    parser.add_argument("--data-dir", type=Path, help="default: ROOT/_data/dso")
    args = parser.parse_args(argv)
    data_dir = args.data_dir or args.root / "_data" / "dso"
    try:
        dates, stamp = expected(args.root, data_dir)
    except (DatesError, dso_data.DsoDataError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"data_date {stamp or '-'}")
    for url, value in dates.items():
        print(f"{value}  {url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
