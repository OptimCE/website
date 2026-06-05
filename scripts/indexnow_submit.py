#!/usr/bin/env python3
"""Incremental IndexNow submitter for a Jekyll site.

Parses a built sitemap.xml, diffs it against a small JSON state file, and POSTs
only the new/changed URLs to the IndexNow API (Bing/Yandex/Naver/Seznam). Google
does NOT use IndexNow; this is purely additive and never touches the sitemap or
robots.txt.

stdlib only (Python 3.11+). No third-party packages.

IMPORTANT - three values must match for IndexNow to validate the submission:
  1. the key file name at the site root:  <KEY>.txt
  2. the key file *contents*:              <KEY>
  3. the GitHub Actions secret:            INDEXNOW_KEY
If any of the three differ, the verifying crawlers reject the batch.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from xml.etree import ElementTree

SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
BATCH_SIZE = 10_000
HTTP_TIMEOUT = 30


def parse_sitemap(path):
    """Return {url: lastmod_or_None} for every <url> entry in the sitemap."""
    root = ElementTree.parse(path).getroot()
    urls = {}
    for url_el in root.findall(f"{{{SITEMAP_NS}}}url"):
        loc_el = url_el.find(f"{{{SITEMAP_NS}}}loc")
        if loc_el is None or not (loc_el.text or "").strip():
            continue
        loc = loc_el.text.strip()
        mod_el = url_el.find(f"{{{SITEMAP_NS}}}lastmod")
        lastmod = mod_el.text.strip() if (mod_el is not None and mod_el.text) else None
        urls[loc] = lastmod
    return urls


def apply_excludes(urls, excludes):
    if not excludes:
        return dict(urls)
    return {u: m for u, m in urls.items() if not any(frag in u for frag in excludes)}


def load_state(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def compute_diff(sitemap_urls, state):
    """Submit URLs absent from state, or whose lastmod changed.

    A URL with no lastmod is submitted once (when first seen) and never again.
    """
    to_submit = []
    for url, lastmod in sitemap_urls.items():
        if url not in state:
            to_submit.append(url)
        elif lastmod is not None and state.get(url) != lastmod:
            to_submit.append(url)
    removed = [u for u in state if u not in sitemap_urls]
    return to_submit, removed


def post_batch(payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        INDEXNOW_ENDPOINT, data=data, method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
        return resp.status, resp.read().decode("utf-8", "replace")


def write_state(path, state):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2, sort_keys=True, ensure_ascii=False)
        fh.write("\n")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Incremental IndexNow submitter.")
    parser.add_argument("--sitemap", required=True, help="Path to built sitemap.xml")
    parser.add_argument("--host", required=True, help="Site host, e.g. www.optimce.be")
    parser.add_argument("--state", default=".indexnow/submitted.json",
                        help="JSON state file (url -> lastmod). Missing = first run.")
    parser.add_argument("--exclude", action="append", default=[],
                        help="Substring filter (repeatable); matching URLs are skipped.")
    parser.add_argument("--key", default=os.environ.get("INDEXNOW_KEY", ""),
                        help="IndexNow key (default: env INDEXNOW_KEY).")
    parser.add_argument("--key-location", default=None,
                        help="Default: https://<host>/<key>.txt")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the diff and exit 0; no network, no state write.")
    args = parser.parse_args(argv)

    key_location = args.key_location or f"https://{args.host}/{args.key}.txt"

    sitemap_urls = apply_excludes(parse_sitemap(args.sitemap), args.exclude)
    state = load_state(args.state)
    to_submit, removed = compute_diff(sitemap_urls, state)

    print(f"[indexnow] sitemap={args.sitemap} host={args.host} state={args.state}")
    print(f"[indexnow] total={len(sitemap_urls)} known={len(state)} "
          f"to_submit={len(to_submit)} stale_in_state={len(removed)}")
    for u in to_submit:
        print(f"[indexnow]   + {u}  (lastmod={sitemap_urls[u]})")

    if args.dry_run:
        print("[indexnow] dry-run: no network call, state left unchanged.")
        return 0

    # Rebuild state from the current (filtered) sitemap so removed URLs are pruned.
    new_state = dict(sitemap_urls)

    if not to_submit:
        print("[indexnow] Nothing to submit.")
        if new_state != state:
            write_state(args.state, new_state)
            print(f"[indexnow] Pruned {len(removed)} stale URL(s) from state.")
        return 0

    if not args.key:
        print("[indexnow] ERROR: no key (set INDEXNOW_KEY or --key).", file=sys.stderr)
        return 1

    for i in range(0, len(to_submit), BATCH_SIZE):
        batch = to_submit[i:i + BATCH_SIZE]
        payload = {"host": args.host, "key": args.key,
                   "keyLocation": key_location, "urlList": batch}
        print(f"[indexnow] POST {len(batch)} URL(s) -> {INDEXNOW_ENDPOINT}")
        try:
            status, body = post_batch(payload)
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")
            print(f"[indexnow] ERROR: HTTP {exc.code} {exc.reason}: {detail}",
                  file=sys.stderr)
            return 1
        except urllib.error.URLError as exc:
            print(f"[indexnow] ERROR: {exc}", file=sys.stderr)
            return 1
        print(f"[indexnow] response: HTTP {status}")
        if status not in (200, 202):
            print(f"[indexnow] ERROR: unexpected status {status}; "
                  f"state left unchanged.", file=sys.stderr)
            return 1

    write_state(args.state, new_state)
    print(f"[indexnow] Submitted {len(to_submit)} URL(s); state updated "
          f"({len(new_state)} tracked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
