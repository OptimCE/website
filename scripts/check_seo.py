#!/usr/bin/env python3
"""Post-build SEO guards for the OptimCE site.

Runs against `_site/` after `jekyll build`. Every check here protects a class of
bug that produces a *green build and a broken page* — malformed JSON-LD still
renders as valid HTML, an over-long <title> still deploys fine, and a
cross-language link still resolves. None of these fail on their own.

Usage:
    python scripts/check_seo.py [--site _site] [--warn-only]

Exit code 1 if any check fails (unless --warn-only).
"""

from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import sys
from collections import defaultdict

# SERP budgets. Google truncates by pixel width, not characters, so these are
# deliberate approximations — the point is to catch the 90+ char outliers.
TITLE_MAX = 60
DESC_MIN = 70
DESC_MAX = 160

LANG_PREFIXES = {"en": "/en/", "de": "/de/", "nl": "/nl/"}
# Language-owned path segments. A page in one language linking into another
# language's blog is a leak the link checker cannot see: the target resolves.
BLOG_PATHS = {
    "fr": "/actualites/",
    "en": "/en/news/",
    "de": "/de/aktuelles/",
    "nl": "/nl/nieuws/",
}

RE_JSONLD = re.compile(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.DOTALL | re.IGNORECASE,
)
RE_TITLE = re.compile(r"<title>(.*?)</title>", re.DOTALL | re.IGNORECASE)
RE_DESC = re.compile(
    r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>',
    re.DOTALL | re.IGNORECASE,
)
RE_HTML_LANG = re.compile(r'<html[^>]*\blang=["\']([^"\']+)["\']', re.IGNORECASE)
RE_H1 = re.compile(r"<h1[\s>]", re.IGNORECASE)
RE_CANONICAL = re.compile(
    r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']', re.IGNORECASE
)
RE_NOINDEX = re.compile(r'<meta\s+name=["\']robots["\'][^>]*noindex', re.IGNORECASE)


def text(raw: str) -> str:
    """Unescape HTML entities so character counts match what Google sees."""
    return html.unescape(re.sub(r"\s+", " ", raw)).strip()


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def check_page(path: pathlib.Path, rel: str, body: str, rep: Report) -> None:
    noindex = bool(RE_NOINDEX.search(body))

    # --- JSON-LD parses, and our own graph is @id-addressed -------------------
    blocks = RE_JSONLD.findall(body)
    if not blocks:
        rep.warn(f"{rel}: no JSON-LD at all")
    saw_graph = False
    for i, block in enumerate(blocks):
        try:
            data = json.loads(block)
        except json.JSONDecodeError as exc:
            rep.error(f"{rel}: JSON-LD block {i} is malformed: {exc}")
            continue
        if isinstance(data, dict) and "@graph" in data:
            saw_graph = True
            nodes = data["@graph"]
            if not isinstance(nodes, list) or not nodes:
                rep.error(f"{rel}: @graph is empty or not a list")
                continue
            for node in nodes:
                if not isinstance(node, dict):
                    rep.error(f"{rel}: @graph contains a non-object node")
                    continue
                if "@id" not in node:
                    rep.error(
                        f"{rel}: @graph node {node.get('@type', '?')} has no @id"
                    )
                if "@type" not in node:
                    rep.error(f"{rel}: @graph node has no @type")
    if not saw_graph:
        rep.error(f"{rel}: no @graph JSON-LD block emitted")

    # --- one H1 --------------------------------------------------------------
    h1s = len(RE_H1.findall(body))
    if h1s != 1:
        rep.error(f"{rel}: expected exactly 1 <h1>, found {h1s}")

    # --- <html lang> matches the directory -----------------------------------
    m = RE_HTML_LANG.search(body)
    if not m:
        rep.error(f"{rel}: no lang attribute on <html>")
    else:
        got = m.group(1)
        want = "fr"
        for code, prefix in LANG_PREFIXES.items():
            if rel.startswith(prefix):
                want = code
                break
        if got != want:
            rep.error(f"{rel}: <html lang='{got}'> but path implies '{want}'")

    # --- title / description budgets -----------------------------------------
    if noindex:
        return  # budgets are about SERP appearance; noindexed pages have none

    m = RE_TITLE.search(body)
    if not m:
        rep.error(f"{rel}: no <title>")
    else:
        title = text(m.group(1))
        if len(title) > TITLE_MAX:
            rep.error(f"{rel}: <title> is {len(title)} chars (max {TITLE_MAX}): {title!r}")

    m = RE_DESC.search(body)
    if not m:
        rep.error(f"{rel}: no meta description")
    else:
        desc = text(m.group(1))
        if len(desc) > DESC_MAX:
            rep.error(
                f"{rel}: meta description is {len(desc)} chars (max {DESC_MAX})"
            )
        elif len(desc) < DESC_MIN:
            rep.error(
                f"{rel}: meta description is {len(desc)} chars (min {DESC_MIN})"
            )


def check_duplicates(pages: dict[str, tuple[str, str]], rep: Report) -> None:
    """Duplicate titles/descriptions within the same language."""
    by_title: dict[tuple[str, str], list[str]] = defaultdict(list)
    by_desc: dict[tuple[str, str], list[str]] = defaultdict(list)
    for rel, (title, desc) in pages.items():
        lang = "fr"
        for code, prefix in LANG_PREFIXES.items():
            if rel.startswith(prefix):
                lang = code
                break
        if title:
            by_title[(lang, title)].append(rel)
        if desc:
            by_desc[(lang, desc)].append(rel)
    for (lang, value), rels in by_title.items():
        if len(rels) > 1:
            rep.error(f"duplicate <title> in {lang}: {value!r} on {', '.join(sorted(rels))}")
    for (lang, value), rels in by_desc.items():
        if len(rels) > 1:
            rep.error(
                f"duplicate description in {lang}: {value[:60]!r}… on {', '.join(sorted(rels))}"
            )


def check_source_links(root: pathlib.Path, rep: Report) -> None:
    """Cross-language link leaks, checked against markdown source, not output.

    A link checker cannot catch these — an English post linking to /actualites/
    points at a page that exists and returns 200. It is just the wrong language.
    """
    posts = root / "_posts"
    if not posts.is_dir():
        return
    for md in sorted(posts.glob("*.md")):
        raw = md.read_text(encoding="utf-8")
        fm = re.match(r"^---\n(.*?)\n---\n", raw, re.DOTALL)
        if not fm:
            continue
        lang_m = re.search(r"^lang:\s*(\S+)\s*$", fm.group(1), re.MULTILINE)
        if not lang_m:
            continue
        lang = lang_m.group(1).strip("\"'")
        body = raw[fm.end():]
        for other, prefix in BLOG_PATHS.items():
            if other == lang:
                continue
            for m in re.finditer(re.escape(f"]({prefix}"), body):
                line = body[: m.start()].count("\n") + 1
                rep.error(
                    f"_posts/{md.name}:{line}: lang={lang} post links into "
                    f"{other} path {prefix}"
                )


def check_glossary_freshness(root: pathlib.Path, rep: Report) -> None:
    """The glossary index pages render _data/glossary.yml but carry their own
    last_modified_at. If that date is older than the data file's newest commit,
    the sitemap lastmod is a lie and IndexNow never resubmits the page."""
    import subprocess

    data = root / "_data" / "glossary.yml"
    if not data.is_file():
        return
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(data)],
            cwd=root, capture_output=True, text=True, timeout=30,
        )
    except Exception:
        return
    newest = out.stdout.strip()
    if not newest:
        return
    pages = [
        "glossaire/index.html",
        "en/glossary/index.html",
        "de/glossar/index.html",
        "nl/woordenlijst/index.html",
    ]
    for rel in pages:
        p = root / rel
        if not p.is_file():
            continue
        m = re.search(
            r"^last_modified_at:\s*(\d{4}-\d{2}-\d{2})", p.read_text(encoding="utf-8"),
            re.MULTILINE,
        )
        if not m:
            rep.error(f"{rel}: no last_modified_at")
        elif m.group(1) < newest:
            rep.error(
                f"{rel}: last_modified_at {m.group(1)} is older than the newest "
                f"_data/glossary.yml commit ({newest}) — bump it or the sitemap "
                f"lastmod is stale and IndexNow will not resubmit"
            )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="_site")
    ap.add_argument("--root", default=".")
    ap.add_argument("--warn-only", action="store_true")
    args = ap.parse_args()

    site = pathlib.Path(args.site)
    root = pathlib.Path(args.root)
    if not site.is_dir():
        print(f"error: {site} not found — run `jekyll build` first", file=sys.stderr)
        return 1

    rep = Report()
    pages: dict[str, tuple[str, str]] = {}
    count = 0

    for path in sorted(site.rglob("*.html")):
        rel = "/" + path.relative_to(site).as_posix()
        body = path.read_text(encoding="utf-8", errors="replace")
        # jekyll-redirect-from stubs are meta-refresh only; nothing to check.
        if "http-equiv=\"refresh\"" in body and len(body) < 2000:
            continue
        count += 1
        check_page(path, rel, body, rep)
        if not RE_NOINDEX.search(body):
            t = RE_TITLE.search(body)
            d = RE_DESC.search(body)
            pages[rel] = (
                text(t.group(1)) if t else "",
                text(d.group(1)) if d else "",
            )

    check_duplicates(pages, rep)
    check_source_links(root, rep)
    check_glossary_freshness(root, rep)

    for w in rep.warnings:
        print(f"WARN  {w}")
    for e in rep.errors:
        print(f"FAIL  {e}")

    print(f"\nChecked {count} pages: {len(rep.errors)} errors, {len(rep.warnings)} warnings")
    if rep.errors and not args.warn_only:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
