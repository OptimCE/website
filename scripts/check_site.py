#!/usr/bin/env python3
"""Post-build integrity checks for the OptimCE site.

Complements scripts/check_seo.py (per-page SEO budgets) with checks that need
the whole built site at once. Each one guards a failure that still deploys
green:

  redirects  every row of _data/redirects.csv produced a stub that points
             straight (no chain) at a real page, and no stub is unaccounted for
  links      no internal link is broken, points at a redirect stub, or targets
             a #fragment that does not exist on the target page
  hreflang   every indexable page lists fr/en/de/nl + x-default (= fr), the
             group is reciprocal, and og:locale:alternate names the other three
             locales
  sitemap    lists every indexable page, nothing else, and no redirected URL
  indexnow   every URL in .indexnow/submitted.json is still in the sitemap or is
             a redirect source, so no indexed URL disappears silently
  jsonld     per-type required properties, and every {"@id": ...} reference
             resolves to a node defined somewhere on the site
  markers    no "[À VÉRIFIER]" / "[À COMPLÉTER" editorial marker is published

stdlib only, so CI needs no extra install.

Usage:
    python scripts/check_site.py [--site _site] [--root .] [--allow-placeholders]

Exit code 1 if any check fails.
"""

from __future__ import annotations

import argparse
import csv
import json
import pathlib
import re
import sys
from collections import defaultdict
from datetime import datetime
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
LANGS = ("fr", "en", "de", "nl")
MARKERS = ("[À VÉRIFIER", "[À COMPLÉTER")
RE_REFRESH = re.compile(r'http-equiv="refresh"\s+content="0;\s*url=([^"]+)"', re.I)

# Required properties per schema.org type, for the nodes we emit ourselves.
REQUIRED = {
    "Organization": ("name", "url", "logo"),
    "WebSite": ("name", "url", "inLanguage", "publisher"),
    "SoftwareApplication": ("name", "applicationCategory", "operatingSystem", "offers"),
    "Person": ("name",),
    "Article": ("headline", "datePublished", "dateModified", "author", "publisher",
                "inLanguage", "mainEntityOfPage"),
    "AboutPage": ("name", "url", "inLanguage", "isPartOf"),
    "CollectionPage": ("name", "url", "inLanguage", "isPartOf"),
    "ProfilePage": ("name", "url", "inLanguage", "isPartOf", "mainEntity"),
    "WebPage": ("name", "url", "inLanguage", "isPartOf"),
    "FAQPage": ("mainEntity",),
    "DefinedTermSet": ("name", "url", "inLanguage"),
    "DefinedTerm": ("name", "description", "inDefinedTermSet"),
    "BreadcrumbList": ("itemListElement",),
    "ItemList": ("itemListElement",),
}
DATE_KEYS = ("datePublished", "dateModified")


class Page(HTMLParser):
    """Everything the checks need from one HTML file, in a single pass."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.lang = ""
        self.ids: set[str] = set()
        self.links: list[tuple[str, str]] = []  # (tag.attr, url)
        self.hreflang: dict[str, str] = {}
        self.og_locale = ""
        self.og_alternates: list[str] = []
        self.canonical = ""
        self.noindex = False
        self.jsonld: list[str] = []
        self._in_jsonld = False
        self._buf: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang") or ""
        for key in ("id",):
            if a.get(key):
                self.ids.add(a[key])
        if tag == "a" and a.get("name"):
            self.ids.add(a["name"])
        if tag == "a" and a.get("href"):
            self.links.append(("a.href", a["href"]))
        elif tag in ("img", "script", "source", "iframe") and a.get("src"):
            self.links.append((f"{tag}.src", a["src"]))
        elif tag == "link":
            rel = (a.get("rel") or "").lower()
            href = a.get("href") or ""
            if rel == "alternate" and a.get("hreflang"):
                self.hreflang[a["hreflang"]] = href
            elif rel == "canonical":
                self.canonical = href
            elif rel in ("stylesheet", "icon", "preload") and href:
                self.links.append((f"link[{rel}]", href))
        elif tag == "meta":
            prop = a.get("property") or ""
            if prop == "og:locale":
                self.og_locale = a.get("content") or ""
            elif prop == "og:locale:alternate":
                self.og_alternates.append(a.get("content") or "")
            elif prop == "og:image" and a.get("content"):
                self.links.append(("meta.og:image", a["content"]))
            elif (a.get("name") or "").lower() == "robots" and "noindex" in (a.get("content") or ""):
                self.noindex = True
        elif tag == "script" and (a.get("type") or "") == "application/ld+json":
            self._in_jsonld = True
            self._buf = []

    def handle_endtag(self, tag):
        if tag == "script" and self._in_jsonld:
            self.jsonld.append("".join(self._buf))
            self._in_jsonld = False

    def handle_data(self, data):
        if self._in_jsonld:
            self._buf.append(data)


class Report:
    def __init__(self) -> None:
        self.errors: dict[str, list[str]] = defaultdict(list)
        self.warnings: dict[str, list[str]] = defaultdict(list)
        self.stats: dict[str, str] = {}

    def error(self, check: str, msg: str) -> None:
        self.errors[check].append(msg)

    def warn(self, check: str, msg: str) -> None:
        self.warnings[check].append(msg)


def url_path(site_file: pathlib.Path, site: pathlib.Path) -> str:
    rel = site_file.relative_to(site).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def resolve(path: str, site: pathlib.Path) -> pathlib.Path | None:
    """Map a URL path to the file GitHub Pages would serve, or None."""
    path = unquote(path)
    if path.endswith("/"):
        candidate = site / path.lstrip("/") / "index.html"
        return candidate if candidate.is_file() else None
    candidate = site / path.lstrip("/")
    if candidate.is_file():
        return candidate
    candidate = site / path.lstrip("/") / "index.html"
    return candidate if candidate.is_file() else None


def is_stub(body: str) -> bool:
    return 'http-equiv="refresh"' in body and len(body) < 2000


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="_site")
    ap.add_argument("--root", default=".")
    ap.add_argument("--allow-placeholders", action="store_true",
                    help="report editorial markers as warnings instead of errors")
    args = ap.parse_args()
    # Windows consoles default to cp1252, which cannot encode every character
    # a page path or message may carry.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    site = pathlib.Path(args.site)
    root = pathlib.Path(args.root)
    if not (site / "sitemap.xml").is_file():
        print(f"error: {site}/sitemap.xml not found — run `jekyll build` first", file=sys.stderr)
        return 1

    rep = Report()

    # --- sitemap first: it gives us the site's own origin ---------------------
    sm_root = ElementTree.parse(site / "sitemap.xml").getroot()
    sitemap_urls = [
        (el.findtext(f"{SITEMAP_NS}loc") or "").strip()
        for el in sm_root.findall(f"{SITEMAP_NS}url")
    ]
    if not sitemap_urls:
        print("error: empty sitemap", file=sys.stderr)
        return 1
    first = urlsplit(sitemap_urls[0])
    origin = f"{first.scheme}://{first.netloc}"

    def internal_path(url: str) -> str | None:
        """Path of an internal URL, or None for external / non-http links."""
        parts = urlsplit(url)
        if parts.scheme in ("mailto", "tel", "javascript", "data"):
            return None
        if parts.scheme or parts.netloc:
            if f"{parts.scheme}://{parts.netloc}" != origin:
                return None
        return parts.path or None

    # --- parse every HTML file once --------------------------------------------
    pages: dict[str, Page] = {}
    stubs: dict[str, str] = {}  # path -> absolute target
    bodies: dict[str, str] = {}
    for f in sorted(site.rglob("*.html")):
        body = f.read_text(encoding="utf-8", errors="replace")
        path = url_path(f, site)
        if is_stub(body):
            m = RE_REFRESH.search(body)
            stubs[path] = m.group(1) if m else ""
            continue
        p = Page()
        p.feed(body)
        pages[path] = p
        bodies[path] = body
    rep.stats["pages"] = str(len(pages))
    rep.stats["stubs"] = str(len(stubs))

    # --- redirects ---------------------------------------------------------------
    table_file = root / "_data" / "redirects.csv"
    rows: list[tuple[str, str]] = []
    if table_file.is_file():
        with table_file.open(encoding="utf-8", newline="") as fh:
            for row in csv.DictReader(fh):
                rows.append((row["from"].strip(), row["to"].strip()))
    froms = {f for f, _ in rows}
    for src, dst in rows:
        if src not in stubs:
            rep.error("redirects", f"{src}: no redirect stub in _site")
            continue
        if stubs[src] != origin + dst:
            rep.error("redirects", f"{src}: stub points to {stubs[src]}, table says {origin + dst}")
        if dst in froms:
            rep.error("redirects", f"{src} -> {dst}: chain (target is itself redirected)")
        if dst not in pages:
            rep.error("redirects", f"{src} -> {dst}: target is not a page")
    for path in stubs:
        if path not in froms:
            rep.error("redirects", f"{path}: redirect stub not declared in _data/redirects.csv")
    rj = site / "redirects.json"
    if rj.is_file():
        declared = json.loads(rj.read_text(encoding="utf-8"))
        expected = {src: origin + dst for src, dst in rows}
        if declared != expected:
            rep.error("redirects", "redirects.json differs from _data/redirects.csv")
    rep.stats["redirects"] = f"{len(rows)} rows"

    # --- internal links ----------------------------------------------------------
    checked = 0
    for path, p in pages.items():
        for kind, href in p.links:
            ip = internal_path(href)
            if ip is None:
                continue
            checked += 1
            if not ip.startswith("/"):
                base = path if path.endswith("/") else path.rsplit("/", 1)[0] + "/"
                ip = base + ip
            target_file = resolve(ip, site)
            frag = urlsplit(href).fragment
            if target_file is None:
                rep.error("links", f"{path}: broken {kind} -> {href}")
                continue
            target = url_path(target_file, site)
            if target in stubs:
                rep.error("links", f"{path}: {kind} -> {href} goes through a redirect")
                continue
            if not ip.endswith("/") and target_file.name == "index.html":
                rep.warn("links", f"{path}: {href} lacks its trailing slash")
            if frag and target in pages and unquote(frag) not in pages[target].ids:
                rep.error("links", f"{path}: {href} — no #{frag} on {target}")
    rep.stats["links"] = f"{checked} internal links"

    # --- sitemap -----------------------------------------------------------------
    sitemap_paths = set()
    for url in sitemap_urls:
        ip = internal_path(url)
        if ip is None:
            rep.error("sitemap", f"{url}: not on {origin}")
            continue
        sitemap_paths.add(ip)
        if ip in froms or ip in stubs:
            rep.error("sitemap", f"{url}: redirected URL listed")
        elif ip not in pages and not ip.endswith((".pdf", ".xml")):
            rep.error("sitemap", f"{url}: no such page")
        elif ip in pages and pages[ip].noindex:
            rep.error("sitemap", f"{url}: page is noindex")
    indexable = {path for path, p in pages.items() if not p.noindex}
    for path in sorted(indexable - sitemap_paths):
        rep.error("sitemap", f"{path}: indexable page missing from the sitemap")
    rep.stats["sitemap"] = f"{len(sitemap_urls)} URLs"

    # --- indexnow state coverage -----------------------------------------------
    state_file = root / ".indexnow" / "submitted.json"
    if state_file.is_file():
        state = json.loads(state_file.read_text(encoding="utf-8"))
        for url in sorted(state):
            ip = internal_path(url)
            if ip is None or ip in sitemap_paths or ip in froms:
                continue
            rep.error("indexnow", f"{url}: was submitted to IndexNow, is gone from the sitemap "
                                  f"and has no redirect — add a row to _data/redirects.csv")
        rep.stats["indexnow"] = f"{len(state)} URLs in state"

    # --- hreflang + og:locale:alternate -------------------------------------------
    locale_of: dict[str, str] = {}
    for p in pages.values():
        if p.lang in LANGS and p.og_locale:
            locale_of.setdefault(p.lang, p.og_locale)
    groups = 0
    for path in sorted(indexable):
        p = pages[path]
        if not p.hreflang:
            rep.error("hreflang", f"{path}: no hreflang group")
            continue
        codes = set(p.hreflang)
        if codes != set(LANGS) | {"x-default"}:
            rep.error("hreflang", f"{path}: hreflang set is {sorted(codes)}")
        if p.hreflang.get("x-default") != p.hreflang.get("fr"):
            rep.error("hreflang", f"{path}: x-default is not the French page")
        if internal_path(p.hreflang.get(p.lang, "")) != path:
            rep.error("hreflang", f"{path}: no self-referencing hreflang for '{p.lang}'")
        for code in LANGS:
            other = internal_path(p.hreflang.get(code, ""))
            if other is None:
                continue
            if other not in pages:
                rep.error("hreflang", f"{path}: hreflang {code} -> {other} is not a page")
            elif pages[other].hreflang != p.hreflang:
                rep.error("hreflang", f"{path}: group differs on its {code} page {other} (not reciprocal)")
        want = sorted(v for k, v in locale_of.items() if k != p.lang)
        if sorted(p.og_alternates) != want:
            rep.error("hreflang", f"{path}: og:locale:alternate {sorted(p.og_alternates)} != {want}")
        if p.canonical and internal_path(p.canonical) != path:
            rep.error("hreflang", f"{path}: canonical points to {p.canonical}")
        groups += 1
    rep.stats["hreflang"] = f"{groups} pages"

    # --- JSON-LD ------------------------------------------------------------------
    # A node is "defined" when it carries an @id plus at least one other
    # property, at any depth; a bare {"@id": ...} is a reference. All pages are
    # collected before any reference is checked, since a node may be defined on
    # one page (the glossary index's DefinedTermSet) and referenced from another.
    defined: set[str] = set()
    graphs: dict[str, list[dict]] = {}

    def collect(value) -> None:
        if isinstance(value, dict):
            if "@id" in value and len(value) > 1:
                defined.add(value["@id"])
            for v in value.values():
                collect(v)
        elif isinstance(value, list):
            for v in value:
                collect(v)

    def references(value):
        if isinstance(value, dict):
            if set(value) == {"@id"}:
                yield value["@id"]
            else:
                for v in value.values():
                    yield from references(v)
        elif isinstance(value, list):
            for v in value:
                yield from references(v)

    for path, p in pages.items():
        nodes: list[dict] = []
        for block in p.jsonld:
            try:
                data = json.loads(block)
            except json.JSONDecodeError as exc:
                rep.error("jsonld", f"{path}: malformed JSON-LD ({exc})")
                continue
            if isinstance(data, dict) and isinstance(data.get("@graph"), list):
                nodes.extend(n for n in data["@graph"] if isinstance(n, dict))
        graphs[path] = nodes
        collect(nodes)

    type_counts: dict[str, int] = defaultdict(int)
    for path, nodes in graphs.items():
        for n in nodes:
            types = n.get("@type")
            types = types if isinstance(types, list) else [types]
            for t in types:
                type_counts[t] += 1
                for key in REQUIRED.get(t, ()):
                    if n.get(key) in (None, "", []):
                        rep.error("jsonld", f"{path}: {t} without {key}")
            for key in DATE_KEYS:
                if key in n:
                    try:
                        datetime.fromisoformat(str(n[key]))
                    except ValueError:
                        rep.error("jsonld", f"{path}: {key} {n[key]!r} is not ISO 8601")
            if "BreadcrumbList" in types:
                items = n.get("itemListElement") or []
                for i, item in enumerate(items, start=1):
                    if item.get("position") != i:
                        rep.error("jsonld", f"{path}: breadcrumb position {item.get('position')} != {i}")
                    if not item.get("name"):
                        rep.error("jsonld", f"{path}: breadcrumb item {i} has no name")
                    crumb = item.get("item")
                    if i < len(items):
                        ip = internal_path(crumb or "")
                        if not crumb or ip not in pages:
                            rep.error("jsonld", f"{path}: breadcrumb item {i} -> {crumb} is not a page")
    for path, nodes in graphs.items():
        for ref in sorted(set(references(nodes))):
            if ref not in defined:
                rep.error("jsonld", f"{path}: @id reference {ref} resolves nowhere on the site")
    rep.stats["jsonld"] = ", ".join(f"{t} {c}" for t, c in sorted(type_counts.items()))

    # --- editorial markers --------------------------------------------------------
    marker_hits = 0
    for path, body in bodies.items():
        for marker in MARKERS:
            n = body.count(marker)
            if n:
                marker_hits += n
                msg = f"{path}: {n} × {marker}…]"
                (rep.warn if args.allow_placeholders else rep.error)("markers", msg)
    rep.stats["markers"] = f"{marker_hits} marker(s)"

    # --- report -------------------------------------------------------------------
    checks = ("redirects", "links", "sitemap", "indexnow", "hreflang", "jsonld", "markers")
    for check in checks:
        for msg in rep.warnings.get(check, []):
            print(f"WARN  [{check}] {msg}")
        for msg in rep.errors.get(check, []):
            print(f"FAIL  [{check}] {msg}")
    print()
    for check in checks:
        status = "FAIL" if rep.errors.get(check) else "ok"
        print(f"{check:10} {status:5} {len(rep.errors.get(check, [])):4} error(s)  {rep.stats.get(check, '')}")
    total = sum(len(v) for v in rep.errors.values())
    print(f"\n{rep.stats['pages']} pages, {rep.stats['stubs']} redirect stubs: {total} error(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
