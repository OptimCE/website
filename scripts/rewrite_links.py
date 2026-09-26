#!/usr/bin/env python3
"""Rewrite internal links that point at a redirected URL.

Reads _data/redirects.csv (from,to) and, in every tracked text file, replaces a
link to `from` with a link to `to`, so that no page links through a redirect
stub. Run it after adding rows to the table; scripts/check_site.py fails the
build if a link still goes through a redirect.

Matches the path only in link position — after `(`, a quote, `=` or
whitespace, optionally preceded by the site origin — and keeps any #fragment or
?query. Line endings and encoding are preserved byte for byte.

Never touched:
  _data/redirects.csv         the table itself (its `from` column must stay)
  .indexnow/submitted.json    the IndexNow state must keep the old URLs so that
                              scripts/indexnow_submit.py notifies them once

Usage:
    python scripts/rewrite_links.py [--dry-run]
"""

from __future__ import annotations

import argparse
import csv
import pathlib
import re
import subprocess
import sys

ORIGIN = "https://www.optimce.be"
TEXT_SUFFIXES = {".md", ".markdown", ".html", ".yml", ".yaml", ".xml", ".txt", ".js", ".json", ".svg"}
EXCLUDED = {"_data/redirects.csv", ".indexnow/submitted.json"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    with open("_data/redirects.csv", encoding="utf-8", newline="") as fh:
        table = {row["from"].strip(): row["to"].strip() for row in csv.DictReader(fh)}
    if not table:
        print("empty redirect table")
        return 0

    # One alternation, longest path first. Every path ends with "/", so none is
    # a prefix of another; the ordering is belt and braces.
    paths = sorted(table, key=len, reverse=True)
    pattern = re.compile(
        r"(?<=[(\"'=\s])(" + re.escape(ORIGIN) + r")?("
        + "|".join(re.escape(p) for p in paths)
        + r")(?=[)\"'#?\s]|$)",
        re.MULTILINE,
    )

    files = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout.split("\n")
    total = 0
    for name in files:
        if not name or name in EXCLUDED or pathlib.PurePosixPath(name).suffix not in TEXT_SUFFIXES:
            continue
        path = pathlib.Path(name)
        with path.open(encoding="utf-8", newline="") as fh:
            text = fh.read()
        new_text, n = pattern.subn(lambda m: (m.group(1) or "") + table[m.group(2)], text)
        if n:
            total += n
            print(f"{n:4}  {name}")
            if not args.dry_run:
                with path.open("w", encoding="utf-8", newline="") as fh:
                    fh.write(new_text)
    print(f"{total} link(s) rewritten{' (dry run)' if args.dry_run else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
