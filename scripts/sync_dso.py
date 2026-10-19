#!/usr/bin/env python3
"""Sync _data/dso/ with a published version of belgian-dso-map (stdlib only).

The GRD tool pages are generated from _data/dso/ (_plugins/dso_pages.rb). This
script is the only way that directory changes: it fetches a version, checks it
against the data contract (scripts/dso_data.py), copies its files byte for
byte, writes meta.yml and prints the pull-request body of the bump.

Sources:
  --version X | --latest      a GitHub Release of --repo, through the REST API
                              (gh is not needed). The repository is public:
                              no token is needed. DSO_MAP_TOKEN, if set and
                              not empty (any GitHub token), only lifts the
                              anonymous rate limit (60 requests an hour per
                              IP address). It is sent as an unredirected
                              header, so it never follows the asset download
                              to its storage host, and it is never printed.
  --from-dir PATH             a local build (belgian-dso-map dist/ or .build/*).
                              --version, if given, must equal its release.json.

Checks (any failure exits 1 and leaves _data/dso/ untouched): SHA256SUMS
(every file present is listed and matches, the required set is present,
REPORT.md optional), UTF-8 without BOM, LF, exact headers, data_version equal
to the release.json version on every row, every date on or before the version
date, sorted unique keys, CHANGES.md grammar, counts. A -draft version is
refused unless --from-dir is used with --allow-draft.

Written to _data/dso/: dso_lookup.csv, operators.csv, notes.csv, sources.csv,
vectors.csv, CHANGES.md, release.json, ATTRIBUTION.md, SHA256SUMS (as
published; REPORT.md is not copied) and meta.yml (version, date, draft,
dso_lookup_sha256, counts, removed_max = the latest removal date ever synced).

Usage:
    python scripts/sync_dso.py --latest --if-newer --pr-body pr.md --github-output
    python scripts/sync_dso.py --version 2026.10.0
    python scripts/sync_dso.py --from-dir ../belgian-dso-map/.build/mini --allow-draft

Exit codes: 0 synced or up to date, 1 refused data or download error, 2 usage.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import quote, urlsplit

import dso_data
import dso_dates

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REPO = "OptimCE/belgian-dso-map"
API = "https://api.github.com"
USER_AGENT = "optimce-website-sync-dso"
TOKEN_ENV = "DSO_MAP_TOKEN"
MAX_ASSET_BYTES = 64 * 1024 * 1024


class SyncError(Exception):
    pass


# --- GitHub -----------------------------------------------------------------------------


class _HttpsOnlyRedirect(urllib.request.HTTPRedirectHandler):
    """Follow redirects (asset downloads go to a storage host) over https only.

    urllib copies only the ordinary headers to the redirected request; the
    Authorization header is added with add_unredirected_header and is dropped.
    """

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urlsplit(newurl).scheme != "https":
            raise SyncError(f"refused a redirect to a non-https URL (HTTP {code})")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


_OPENER = urllib.request.build_opener(_HttpsOnlyRedirect())


def _get(url: str, accept: str, token: str | None) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": accept,
            "User-Agent": USER_AGENT,
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    if token:
        request.add_unredirected_header("Authorization", f"Bearer {token}")
    label = urlsplit(url).path
    try:
        with _OPENER.open(request, timeout=60) as response:
            data = response.read(MAX_ASSET_BYTES + 1)
    except urllib.error.HTTPError as exc:
        hint = ""
        if exc.code == 401 and token:
            hint = f" ({TOKEN_ENV} refused; unset it to read the public repository anonymously)"
        elif exc.code in (403, 429):
            hint = " (rate limit?)" if token else (
                f" (rate limit? set {TOKEN_ENV} to any GitHub token to lift the anonymous one)"
            )
        elif exc.code == 404:
            hint = " (no such repository, release or asset)"
        raise SyncError(f"GET {label}: HTTP {exc.code} {exc.reason}{hint}") from None
    except urllib.error.URLError as exc:
        raise SyncError(f"GET {label}: {exc.reason}") from None
    if len(data) > MAX_ASSET_BYTES:
        raise SyncError(f"GET {label}: larger than {MAX_ASSET_BYTES} bytes")
    return data


def github_release(repo: str, version: str | None, token: str | None) -> dict:
    """The release object of tag `version`, or of the latest release."""
    path = f"/repos/{repo}/releases/latest" if version is None else (
        f"/repos/{repo}/releases/tags/{quote(version, safe='')}"
    )
    release = json.loads(_get(API + path, "application/vnd.github+json", token))
    tag = release.get("tag_name", "")
    try:
        dso_data.version_key(tag)
    except ValueError as exc:
        raise SyncError(f"release tag {tag!r}: {exc}") from None
    if dso_data.is_draft(tag) or release.get("draft") or release.get("prerelease"):
        raise SyncError(f"release {tag} is a draft or a prerelease: refused")
    if version is not None and tag != version:
        raise SyncError(f"asked for {version}, GitHub answered {tag}")
    return release


def download_assets(repo: str, release: dict, target: Path, token: str | None) -> None:
    """Download the required assets and SHA256SUMS (REPORT.md is optional and skipped)."""
    assets = {asset.get("name"): asset for asset in release.get("assets", [])}
    prefix = f"{API}/repos/{repo}/releases/assets/"
    missing = [name for name in dso_data.COPIED_FILES if name not in assets]
    if missing:
        raise SyncError(f"release {release['tag_name']} lacks the assets {', '.join(missing)}")
    for name in dso_data.COPIED_FILES:
        url = assets[name].get("url", "")
        if not url.startswith(prefix):
            raise SyncError(f"asset {name}: unexpected API URL")
        (target / name).write_bytes(_get(url, "application/octet-stream", token))


# --- Local directory ----------------------------------------------------------------------


def copy_from_dir(source: Path, target: Path) -> None:
    """Copy every regular file of `source`: the integrity rule then sees all of them."""
    if not source.is_dir():
        raise SyncError(f"--from-dir {source}: not a directory")
    for entry in sorted(source.iterdir()):
        if entry.is_file():
            shutil.copyfile(entry, target / entry.name)
        else:
            raise SyncError(f"--from-dir {source}: unexpected entry {entry.name}")


def peek_version(source: Path) -> str:
    try:
        return json.loads((source / "release.json").read_text(encoding="utf-8"))["version"]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise SyncError(f"--from-dir {source}: cannot read release.json ({exc})") from None


# --- Report -------------------------------------------------------------------------------


def _key(row: dict[str, str]) -> tuple[str, ...]:
    return tuple(row[column] for column in dso_data.DSO_LOOKUP_KEY)


def row_changes(old_rows: list[dict[str, str]], new_rows: list[dict[str, str]]) -> dict[str, int]:
    """Rows added, changed (any data column) and removed, by (postcode, ins, section_key)."""
    old = {_key(row): row for row in old_rows}
    new = {_key(row): row for row in new_rows}

    def data(row: dict[str, str]) -> tuple[str, ...]:
        return tuple(v for k, v in row.items() if k not in dso_data.UNCOMPARED)

    return {
        "added": len(new.keys() - old.keys()),
        "changed": sum(1 for k in new.keys() & old.keys() if data(new[k]) != data(old[k])),
        "removed": len(old.keys() - new.keys()),
    }


def _flat_counts(counts: dict, prefix: str = "") -> dict[str, object]:
    flat: dict[str, object] = {}
    for key, value in counts.items():
        if isinstance(value, dict):
            flat.update(_flat_counts(value, f"{prefix}{key}."))
        else:
            flat[f"{prefix}{key}"] = value
    return flat


def pr_body(
    old_version: str,
    release: dso_data.Release,
    old_counts: dict,
    changes: dict[str, int] | None,
    old_dates: dict[str, str],
    new_dates: dict[str, str],
    old_stamp: str | None,
    new_stamp: str | None,
) -> str:
    lines = [f"# dso data {old_version or '(none)'} → {release.version}", ""]
    lines += [
        f"Data release `{release.version}` of belgian-dso-map, dated {release.date}"
        + (f" (previous: `{release.previous}`)." if release.previous else "."),
        "Synced with `scripts/sync_dso.py`: SHA256SUMS, headers, versions and dates checked.",
        "",
        "## Counts",
        "",
        "| | before | after |",
        "|---|---:|---:|",
    ]
    before, after = _flat_counts(old_counts), _flat_counts(release.counts)
    for key in after:
        lines.append(f"| {key} | {before.get(key, '-')} | {after[key]} |")
    if changes is not None:
        lines += [
            "",
            f"Rows of dso_lookup.csv: {changes['added']} added, {changes['changed']} changed, "
            f"{changes['removed']} removed.",
        ]
    lines += ["", "## Sitemap lastmod", ""]
    lines.append(f"Data date: {old_stamp or '-'} → {new_stamp or '-'}")
    lines.append("")
    urls = sorted(set(old_dates) | set(new_dates))
    moved = [url for url in urls if old_dates.get(url) != new_dates.get(url)]
    if not urls:
        lines.append("No tools page in the site yet.")
    elif not moved:
        lines.append("No URL changes its lastmod.")
    else:
        lines.append("These URLs change their lastmod (IndexNow resubmits them after the deploy):")
        lines.append("")
        for url in moved:
            lines.append(f"- `{url}`: {old_dates.get(url, '-')} → {new_dates.get(url, '-')}")
    lines += ["", f"## Changes in {dso_data.base_version(release.version)}", ""]
    lines.append(dso_data.render_section(release.changes[0]))
    return "\n".join(lines) + "\n"


# --- Main ---------------------------------------------------------------------------------


def _write_github_output(values: dict[str, str]) -> None:
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        raise SyncError("--github-output: GITHUB_OUTPUT is not set")
    with open(path, "a", encoding="utf-8", newline="\n") as handle:
        for key, value in values.items():
            handle.write(f"{key}={value}\n")


def _replace_dir(stage: Path, dest: Path) -> None:
    """Swap dest for stage. dest may only hold files this script manages."""
    managed = set(dso_data.COPIED_FILES) | {dso_data.META, dso_data.REPORT}
    if dest.exists():
        unknown = sorted(entry.name for entry in dest.iterdir() if entry.name not in managed)
        if unknown:
            raise SyncError(f"{dest} holds files this script does not manage: {', '.join(unknown)}")
    fresh = dest.with_name(".dso.new")
    stale = dest.with_name(".dso.old")
    for leftover in (fresh, stale):
        if leftover.exists():
            shutil.rmtree(leftover)
    shutil.copytree(stage, fresh)
    if dest.exists():
        dest.rename(stale)
    fresh.rename(dest)
    if stale.exists():
        shutil.rmtree(stale)


def _same_files(left: Path, right: Path) -> bool:
    if not right.is_dir():
        return False
    names = sorted(entry.name for entry in left.iterdir())
    if names != sorted(entry.name for entry in right.iterdir()):
        return False
    return all((left / name).read_bytes() == (right / name).read_bytes() for name in names)


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync _data/dso/ with a version of belgian-dso-map.",
        epilog="Exit codes: 0 synced or up to date, 1 refused or failed, 2 usage error.",
    )
    which = parser.add_mutually_exclusive_group()
    which.add_argument("--version", help="the version to sync (YYYY.MM.N; a -draft only with --from-dir)")
    which.add_argument("--latest", action="store_true", help="the latest GitHub release")
    parser.add_argument("--from-dir", type=Path, help="a local build instead of GitHub")
    parser.add_argument(
        "--allow-draft", action="store_true", help="accept a -draft version (--from-dir only)"
    )
    parser.add_argument("--repo", default=DEFAULT_REPO, help=f"GitHub repository (default {DEFAULT_REPO})")
    parser.add_argument("--if-newer", action="store_true", help="do nothing unless the version is newer")
    parser.add_argument("--pr-body", type=Path, help="also write the pull-request body to this file")
    parser.add_argument(
        "--github-output", action="store_true", help="append changed/from/to to $GITHUB_OUTPUT"
    )
    parser.add_argument("--dry-run", action="store_true", help="check and report, write nothing")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.from_dir is None and not (args.version or args.latest):
        parser.error("give --version X, --latest or --from-dir PATH")
    if args.from_dir is not None and args.latest:
        parser.error("--latest reads GitHub; it cannot be combined with --from-dir")
    if args.allow_draft and args.from_dir is None:
        parser.error("--allow-draft needs --from-dir: a published release is never a draft")
    if args.version:
        try:
            dso_data.version_key(args.version)
        except ValueError as exc:
            parser.error(str(exc))
        if dso_data.is_draft(args.version) and args.from_dir is None:
            parser.error("a -draft version is only read with --from-dir ... --allow-draft")
    return args


def run(args: argparse.Namespace) -> int:
    root: Path = args.root
    dest = root / "_data" / "dso"
    try:
        current = dso_data.read_meta(dest)
    except dso_data.DsoDataError as exc:
        print(f"warning: ignoring the current {dso_data.META}: {exc}", file=sys.stderr)
        current = None
    old_version = current["version"] if current else ""
    token = (os.environ.get(TOKEN_ENV) or "").strip() or None

    def up_to_date(candidate: str) -> bool:
        if not (args.if_newer and old_version):
            return False
        return dso_data.version_key(candidate) <= dso_data.version_key(old_version)

    with tempfile.TemporaryDirectory(prefix="sync-dso-") as tmp:
        fetched, stage = Path(tmp) / "fetched", Path(tmp) / "stage"
        fetched.mkdir()
        stage.mkdir()
        if args.from_dir is not None:
            candidate = peek_version(args.from_dir)
            if args.version and candidate != args.version:
                raise SyncError(f"--version {args.version} but {args.from_dir} holds {candidate}")
        else:
            release_info = github_release(args.repo, None if args.latest else args.version, token)
            candidate = release_info["tag_name"]
        if up_to_date(candidate):
            print(f"up to date: _data/dso is {old_version}, the candidate is {candidate}")
            if args.github_output:
                _write_github_output({"changed": "false", "from": old_version, "to": old_version})
            return 0

        if args.from_dir is not None:
            copy_from_dir(args.from_dir, fetched)
        else:
            download_assets(args.repo, release_info, fetched, token)
        release = dso_data.load_release(fetched, allow_draft=args.allow_draft)
        if release.version != candidate:
            raise SyncError(f"release.json says {release.version}, expected {candidate}")

        for name in dso_data.COPIED_FILES:
            (stage / name).write_bytes((fetched / name).read_bytes())
        meta = dso_data.build_meta(release, current)
        (stage / dso_data.META).write_bytes(dso_data.render_meta(meta))
        problems = dso_data.check_meta(meta, release)
        if problems:
            raise dso_data.DsoDataError(problems)

        new_dates, new_stamp = dso_dates.expected(root, stage)
        # The current copy only feeds the report: a broken one must not block its repair.
        old_dates: dict[str, str] = {}
        old_stamp = None
        changes = None
        try:
            old_dates, old_stamp = dso_dates.expected(root, dest)
            if dso_dates.read_tables(dest):
                old_rows = dso_data.parse_csv(
                    (dest / "dso_lookup.csv").read_bytes(), "dso_lookup.csv", dso_data.DSO_LOOKUP_HEADER
                )
                changes = row_changes(old_rows, release.rows)
        except (dso_data.DsoDataError, dso_dates.DatesError) as exc:
            print(f"warning: the current _data/dso cannot be compared: {exc}", file=sys.stderr)
        body = pr_body(
            old_version,
            release,
            current["counts"] if current else {},
            changes,
            old_dates,
            new_dates,
            old_stamp,
            new_stamp,
        )
        changed = not _same_files(stage, dest)
        if old_version and dso_data.version_key(release.version) < dso_data.version_key(old_version):
            print(f"note: {release.version} is older than {old_version}", file=sys.stderr)
        if not args.dry_run and changed:
            _replace_dir(stage, dest)

    print(body, end="")
    if args.pr_body:
        args.pr_body.write_text(body, encoding="utf-8", newline="\n")
    if args.github_output:
        _write_github_output(
            {"changed": "true" if changed else "false", "from": old_version, "to": release.version}
        )
    verb = "would sync" if args.dry_run else ("synced" if changed else "already synced")
    print(f"\n{verb}: _data/dso {old_version or '(none)'} -> {release.version}", file=sys.stderr)
    return 0


def main(argv: list[str] | None = None) -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    args = parse_args(argv)
    try:
        return run(args)
    except dso_data.DsoDataError as exc:
        print("error: the data break the contract:", file=sys.stderr)
        for problem in exc.problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1
    except (SyncError, dso_dates.DatesError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
