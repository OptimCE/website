"""The belgian-dso-map data contract, as the website consumes it (stdlib only).

The contract is belgian-dso-map's README.md ("Data contract"); its scripts
csvio.py, schema.py and changes.py are the reference. This module ports what
the website needs, and nothing more:

  files       the release file set, and which files land in _data/dso/
  dialect     UTF-8 without BOM, LF, a final newline, RFC 4180, exact headers
  integrity   SHA256SUMS: every file present (other than SHA256SUMS and our own
              meta.yml) is listed and matches, the required set is present,
              REPORT.md is optional; never a plain `sha256sum -c`
  CHANGES.md  the strict grammar (any other line is an error)
  release     release.json, data_version on every row, dates never after the
              version date, counts, drafts refused unless allowed
  URLs        a source url is http(s), an operator's website and tariffs_url
              https or empty: the rules of the contract and of the build
              (_plugins/dso_pages.rb), so a synced release never fails the
              build on a URL
  meta.yml    written by sync_dso.py in a fixed key order; read back here

scripts/sync_dso.py, scripts/dso_dates.py and scripts/check_dso_dates.py share
it; _plugins/dso_pages.rb re-checks the same rules at build time.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import unicodedata
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

# --- Files ------------------------------------------------------------------------------

SUMS = "SHA256SUMS"
META = "meta.yml"
REPORT = "REPORT.md"
# Required assets of a version, all copied into _data/dso/ (with SHA256SUMS).
RELEASE_FILES = (
    "dso_lookup.csv",
    "operators.csv",
    "notes.csv",
    "sources.csv",
    "vectors.csv",
    "CHANGES.md",
    "release.json",
    "ATTRIBUTION.md",
)
OPTIONAL_FILES = (REPORT,)  # listed in SHA256SUMS, never copied
COPIED_FILES = (*RELEASE_FILES, SUMS)
TEXT_FILES = (*RELEASE_FILES, REPORT, SUMS)

# --- Headers (belgian-dso-map scripts/schema.py) ----------------------------------------

DATE_COLUMNS = ("first_seen", "changed_at", "data_version")
DSO_LOOKUP_HEADER = (
    "postcode",
    "ins",
    "commune_fr",
    "commune_nl",
    "commune_de",
    "region",
    "province",
    "section_key",
    "section_fr",
    "section_nl",
    "section_de",
    "elec_operator",
    "elec_designated",
    "gas_status",
    "gas_operator",
    "flags",
    "note_key",
    "source_ids",
    "valid_from",
    *DATE_COLUMNS,
)
OPERATORS_HEADER = (
    "id",
    "kind",
    "name",
    "legal_name",
    "region",
    "elec",
    "gas",
    "website",
    "regulator",
    "tariffs_url",
    "lookup",
    "replaced_by",
    *DATE_COLUMNS,
)
NOTES_HEADER = ("key", "fr", "nl", "de", "en", *DATE_COLUMNS)
SOURCES_HEADER = (
    "id",
    "role",
    "publisher",
    "title",
    "url",
    "retrieved_at",
    "sha256",
    "license",
    "note",
    *DATE_COLUMNS,
)
VECTORS_HEADER = (
    "name",
    "kind",
    "postcode",
    "ins",
    "section_key",
    "post_name",
    "ean",
    "expect_status",
    "expect_key",
    "expect_elec",
    "expect_gas_status",
    "expect_gas",
    "expect_flags",
)
# Input cells of vectors.csv keep their padding: they test the TRIM rule.
VECTOR_INPUT_COLUMNS = ("postcode", "ins", "section_key", "post_name", "ean")
CSV_HEADERS = {
    "dso_lookup.csv": DSO_LOOKUP_HEADER,
    "operators.csv": OPERATORS_HEADER,
    "notes.csv": NOTES_HEADER,
    "sources.csv": SOURCES_HEADER,
    "vectors.csv": VECTORS_HEADER,
}
VERSIONED_FILES = ("dso_lookup.csv", "operators.csv", "notes.csv", "sources.csv")
DSO_LOOKUP_KEY = ("postcode", "ins", "section_key")
# Columns that never count when comparing two versions of a row.
UNCOMPARED = set(DATE_COLUMNS)

# --- Patterns (ASCII only: Python's \d also matches full-width digits) ------------------

POSTCODE_RE = re.compile(r"[0-9]{4}")
INS_RE = re.compile(r"[1-9][0-9]{4}")
DATE_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
VERSION_RE = re.compile(r"([0-9]{4})\.(0[1-9]|1[0-2])\.(0|[1-9][0-9]*)")
DRAFT_SUFFIX = "-draft"
SHA256_LINE_RE = re.compile(r"([0-9a-f]{64})  ([A-Za-z0-9._-]+)")
CHANGES_TITLE = "# Changes"
CHANGES_HEADING_RE = re.compile(r"## ([0-9]{4}\.[0-9]{2}\.[0-9]+) — ([0-9]{4}-[0-9]{2}-[0-9]{2})")
CHANGES_ENTRY_RE = re.compile(
    r"- (added|changed|removed) (dso_lookup|operators|notes|sources) (\S+)( — .*)?"
)
CHANGES_SPECIAL = ("- initial release", "- no changes")
DATASET_NOTE_RE = re.compile(r"dataset-(bru|vla|wal)-")
# belgian-dso-map schema.URL_RE: a sources.csv url is http or https; an
# operator's website and tariffs_url are https or empty (validate.py).
# _plugins/dso_pages.rb applies the same rules at build time.
URL_RE = re.compile(r"https?://\S+")
HTTPS_COLUMNS = ("website", "tariffs_url")

BOM = b"\xef\xbb\xbf"


class DsoDataError(ValueError):
    """The data break the contract. `problems` lists every one found."""

    def __init__(self, problems: list[str]):
        super().__init__("\n".join(problems))
        self.problems = problems


# --- Small helpers ----------------------------------------------------------------------


def is_date(value: str) -> bool:
    """A real calendar date written YYYY-MM-DD."""
    if not DATE_RE.fullmatch(value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def version_key(version: str) -> tuple[int, int, int, int]:
    """Sort key of `YYYY.MM.N` or `YYYY.MM.N-draft`: a draft sorts before its release."""
    draft = version.endswith(DRAFT_SUFFIX)
    base = version[: -len(DRAFT_SUFFIX)] if draft else version
    match = VERSION_RE.fullmatch(base)
    if not match:
        raise ValueError(f"version {version!r} is not YYYY.MM.N")
    return int(match.group(1)), int(match.group(2)), int(match.group(3)), 0 if draft else 1


def is_draft(version: str) -> bool:
    return version.endswith(DRAFT_SUFFIX)


def base_version(version: str) -> str:
    return version[: -len(DRAFT_SUFFIX)] if is_draft(version) else version


def split_list(cell: str) -> list[str]:
    return cell.split("|") if cell else []


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def check_text_bytes(data: bytes, name: str) -> str:
    """UTF-8, no BOM, no CR, a final newline when not empty."""
    if data.startswith(BOM):
        raise DsoDataError([f"{name}: starts with a UTF-8 BOM"])
    if b"\r" in data:
        raise DsoDataError([f"{name}: contains a CR (line endings must be LF)"])
    if data and not data.endswith(b"\n"):
        raise DsoDataError([f"{name}: does not end with a newline"])
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise DsoDataError([f"{name}: not valid UTF-8 ({exc.reason} at byte {exc.start})"]) from exc


def _cell_problem(value: str, *, raw: bool) -> str | None:
    """Port of csvio._cell_problem: control/format characters, padding, NFC."""
    for char in value:
        category = unicodedata.category(char)
        if category in ("Cc", "Zl", "Zp") or (category == "Cf" and not raw):
            return f"control, format or line separator character U+{ord(char):04X}"
    if raw:
        return None
    if value != value.strip():
        return "leading or trailing whitespace"
    if not unicodedata.is_normalized("NFC", value):
        return "text is not in Unicode NFC form"
    return None


def parse_csv(data: bytes, name: str, header: tuple[str, ...]) -> list[dict[str, str]]:
    """Strict read of one published CSV file whose header must be exactly `header`."""
    text = check_text_bytes(data, name)
    if not text:
        raise DsoDataError([f"{name}: empty file (the header row is required)"])
    reader = csv.reader(io.StringIO(text, newline=""), strict=True)
    try:
        parsed = list(reader)
    except csv.Error as exc:
        raise DsoDataError([f"{name}: line {reader.line_num}: {exc}"]) from exc
    found = tuple(parsed[0])
    if found != header:
        raise DsoDataError([f"{name}: header is {','.join(found)!r}, expected {','.join(header)!r}"])
    raw_columns = VECTOR_INPUT_COLUMNS if name == "vectors.csv" else ()
    problems = []
    rows = []
    for number, cells in enumerate(parsed[1:], start=2):
        if len(cells) != len(header):
            problems.append(f"{name}: line {number}: {len(cells)} fields, expected {len(header)}")
            continue
        for column, value in zip(header, cells, strict=True):
            problem = _cell_problem(value, raw=column in raw_columns)
            if problem:
                problems.append(f"{name}: line {number}, column {column}: {problem}")
        rows.append(dict(zip(header, cells, strict=True)))
    if problems:
        raise DsoDataError(problems)
    return rows


# --- SHA256SUMS -------------------------------------------------------------------------


def parse_sums(data: bytes) -> dict[str, str]:
    """name -> sha256 of a `sha256sum` file (two spaces, sorted by name, no duplicate)."""
    text = check_text_bytes(data, SUMS)
    sums: dict[str, str] = {}
    problems = []
    names = []
    for number, line in enumerate(text.split("\n")[:-1], start=1):
        match = SHA256_LINE_RE.fullmatch(line)
        if not match:
            problems.append(f"{SUMS}: line {number} is not '<sha256>  <name>': {line!r}")
            continue
        digest, name = match.groups()
        if name in sums:
            problems.append(f"{SUMS}: {name} is listed twice")
        sums[name] = digest
        names.append(name)
    if names != sorted(names):
        problems.append(f"{SUMS}: names are not sorted")
    if problems:
        raise DsoDataError(problems)
    return sums


def verify_integrity(directory: Path, *, own_files: tuple[str, ...] = ()) -> list[str]:
    """Problems of the SHA256SUMS rule in `directory` (empty list = OK).

    Every regular file present, other than SHA256SUMS and `own_files` (the
    website's meta.yml), is listed and matches; every listed name is a release
    file; the required set is present; REPORT.md is optional.
    """
    sums_path = directory / SUMS
    if not sums_path.is_file():
        return [f"{SUMS} is missing in {directory}"]
    try:
        sums = parse_sums(sums_path.read_bytes())
    except DsoDataError as exc:
        return exc.problems
    problems = []
    allowed = set(RELEASE_FILES) | set(OPTIONAL_FILES)
    for name in sums:
        if name not in allowed:
            problems.append(f"{SUMS} lists {name}, which is not a release file")
    for name in RELEASE_FILES:
        if name not in sums:
            problems.append(f"{SUMS} does not list the required file {name}")
        if not (directory / name).is_file():
            problems.append(f"required file {name} is missing")
    for entry in sorted(directory.iterdir()):
        if entry.name in (SUMS, *own_files):
            continue
        if not entry.is_file():
            problems.append(f"{entry.name}: unexpected entry (not a regular file)")
            continue
        if entry.name not in sums:
            problems.append(f"{entry.name} is present but not listed in {SUMS}")
            continue
        if sha256_bytes(entry.read_bytes()) != sums[entry.name]:
            problems.append(f"{entry.name}: sha256 does not match {SUMS}")
    return problems


# --- CHANGES.md -------------------------------------------------------------------------


@dataclass(frozen=True)
class ChangesSection:
    version: str
    date: str
    entries: tuple[str, ...]


def parse_changes(text: str) -> list[ChangesSection]:
    """Port of belgian-dso-map changes.parse_changes(): sections newest first."""
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    if not lines or lines[0] != CHANGES_TITLE:
        raise DsoDataError([f"CHANGES.md: line 1: expected {CHANGES_TITLE!r}"])
    sections: list[ChangesSection] = []
    current: tuple[str, str, list[str]] | None = None
    problems = []
    for number, line in enumerate(lines[1:], start=2):
        if line == "":
            continue
        heading = CHANGES_HEADING_RE.fullmatch(line)
        if heading:
            if current:
                sections.append(ChangesSection(current[0], current[1], tuple(current[2])))
            current = (heading.group(1), heading.group(2), [])
        elif CHANGES_ENTRY_RE.fullmatch(line) or line in CHANGES_SPECIAL:
            if current is None:
                problems.append(f"CHANGES.md: line {number}: entry before any version heading")
            else:
                current[2].append(line)
        else:
            problems.append(f"CHANGES.md: line {number}: not a heading or an entry: {line!r}")
    if current:
        sections.append(ChangesSection(current[0], current[1], tuple(current[2])))
    for section in sections:
        title = f"## {section.version} — {section.date}"
        if not section.entries:
            problems.append(f"CHANGES.md: {title}: no entries")
        if not is_date(section.date):
            problems.append(f"CHANGES.md: {title}: invalid date")
        try:
            version_key(section.version)
        except ValueError as exc:
            problems.append(f"CHANGES.md: {title}: {exc}")
    if not problems:
        for newer, older in zip(sections, sections[1:]):
            if version_key(newer.version) <= version_key(older.version):
                problems.append(f"CHANGES.md: {newer.version}: versions must be listed newest first")
            if newer.date < older.date:
                problems.append(f"CHANGES.md: {newer.version}: dated before {older.version}")
    if problems:
        raise DsoDataError(problems)
    return sections


def removal_dates(sections: list[ChangesSection]) -> list[str]:
    """Dates of the versions that removed something: a removal is dated by its heading."""
    return [
        section.date
        for section in sections
        if any(CHANGES_ENTRY_RE.fullmatch(e) and e.startswith("- removed ") for e in section.entries)
    ]


def render_section(section: ChangesSection) -> str:
    return "\n".join((f"## {section.version} — {section.date}", *section.entries))


# --- meta.yml ---------------------------------------------------------------------------

META_KEYS = ("version", "date", "draft", "dso_lookup_sha256", "counts", "removed_max")
META_HEADER = (
    "# Written by scripts/sync_dso.py from release.json and CHANGES.md. Do not edit.\n"
    "# removed_max: the latest removal date ever synced; it never goes down, so a\n"
    "# removal moves the table page's lastmod forward (scripts/dso_dates.py).\n"
)


def _scalar(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    raise TypeError(f"meta.yml cannot hold {value!r}")


def _render_mapping(mapping: dict, indent: int) -> list[str]:
    lines = []
    for key, value in mapping.items():
        if isinstance(value, dict):
            lines.append(f"{' ' * indent}{key}:")
            lines.extend(_render_mapping(value, indent + 2))
        else:
            lines.append(f"{' ' * indent}{key}: {_scalar(value)}")
    return lines


def render_meta(meta: dict) -> bytes:
    """meta.yml in the fixed key order of META_KEYS (block YAML, JSON scalars)."""
    if tuple(meta) != META_KEYS:
        raise ValueError(f"meta keys {tuple(meta)} != {META_KEYS}")
    return (META_HEADER + "\n".join(_render_mapping(meta, 0)) + "\n").encode("utf-8")


def parse_meta(data: bytes) -> dict:
    """Read back what render_meta() writes (and nothing else)."""
    text = check_text_bytes(data, META)
    root: dict = {}
    stack: list[tuple[int, dict]] = [(-1, root)]
    for number, line in enumerate(text.split("\n")[:-1], start=1):
        if not line or line.startswith("#"):
            continue
        match = re.fullmatch(r"( *)([A-Za-z_][A-Za-z0-9_]*):(?: (.+))?", line)
        if not match:
            raise DsoDataError([f"{META}: line {number} is not 'key: value': {line!r}"])
        indent = len(match.group(1))
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        key, raw = match.group(2), match.group(3)
        if raw is None:
            child: dict = {}
            parent[key] = child
            stack.append((indent, child))
            continue
        try:
            parent[key] = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise DsoDataError([f"{META}: line {number}: bad value {raw!r}"]) from exc
    if tuple(root) != META_KEYS:
        raise DsoDataError([f"{META}: keys {tuple(root)} != {META_KEYS}"])
    return root


# --- A whole version --------------------------------------------------------------------


@dataclass
class Release:
    directory: Path
    version: str
    date: str
    previous: str
    counts: dict
    tables: dict[str, list[dict[str, str]]]
    changes: list[ChangesSection]
    raw: dict[str, bytes] = field(default_factory=dict)

    @property
    def draft(self) -> bool:
        return is_draft(self.version)

    @property
    def rows(self) -> list[dict[str, str]]:
        return self.tables["dso_lookup.csv"]


def computed_counts(tables: dict[str, list[dict[str, str]]]) -> dict:
    rows = tables["dso_lookup.csv"]
    by_region: dict[str, set[str]] = {"BRU": set(), "VLA": set(), "WAL": set()}
    for row in rows:
        by_region.setdefault(row["region"], set()).add(row["ins"])
    return {
        "communes": len({row["ins"] for row in rows}),
        "communes_by_region": {region: len(ins) for region, ins in by_region.items()},
        "postcodes": len({row["postcode"] for row in rows}),
        "rows": len(rows),
        "sections": len({(row["ins"], row["section_key"]) for row in rows if row["section_key"]}),
        "operators": len(tables["operators.csv"]),
        "notes": len(tables["notes.csv"]),
        "sources": len(tables["sources.csv"]),
    }


def _check_release_json(data: dict) -> list[str]:
    problems = []
    for key in ("version", "date", "previous", "counts"):
        if key not in data:
            problems.append(f"release.json: missing {key!r}")
    if problems:
        return problems
    version, day, previous = data["version"], data["date"], data["previous"]
    if not isinstance(version, str):
        return ["release.json: version is not a string"]
    try:
        version_key(version)
    except ValueError as exc:
        problems.append(f"release.json: {exc}")
    if not isinstance(day, str) or not is_date(day):
        problems.append(f"release.json: date {day!r} is not YYYY-MM-DD")
    if not isinstance(previous, str):
        problems.append("release.json: previous is not a string")
    elif previous:
        try:
            version_key(previous)
        except ValueError as exc:
            problems.append(f"release.json: previous: {exc}")
    if not isinstance(data["counts"], dict):
        problems.append("release.json: counts is not an object")
    return problems


def load_release(directory: Path, *, allow_draft: bool, own_files: tuple[str, ...] = ()) -> Release:
    """Read and check a whole version in `directory`. DsoDataError lists every problem.

    Checks: SHA256SUMS rule, dialect and headers, release.json, data_version on
    every row, first_seen <= changed_at <= version date, sorted unique keys,
    postcodes, URLs, CHANGES.md grammar and newest heading, counts, and the
    draft rule.
    """
    problems = verify_integrity(directory, own_files=own_files)
    if problems:
        raise DsoDataError(problems)
    raw = {name: (directory / name).read_bytes() for name in RELEASE_FILES}
    for name in ("CHANGES.md", "ATTRIBUTION.md", "release.json"):
        try:
            check_text_bytes(raw[name], name)
        except DsoDataError as exc:
            problems += exc.problems
    tables: dict[str, list[dict[str, str]]] = {}
    for name, header in CSV_HEADERS.items():
        try:
            tables[name] = parse_csv(raw[name], name, header)
        except DsoDataError as exc:
            problems += exc.problems
    if problems:
        raise DsoDataError(problems)

    try:
        release = json.loads(raw["release.json"].decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise DsoDataError([f"release.json: not JSON ({exc})"]) from exc
    if not isinstance(release, dict):
        raise DsoDataError(["release.json: not an object"])
    problems += _check_release_json(release)
    if problems:
        raise DsoDataError(problems)
    version, day = release["version"], release["date"]

    if is_draft(version) and not allow_draft:
        problems.append(
            f"version {version} is a draft: refused (only `--from-dir ... --allow-draft` syncs one)"
        )

    # data_version and content dates, on every row of the four versioned files.
    for name in VERSIONED_FILES:
        for number, row in enumerate(tables[name], start=2):
            where = f"{name}: line {number}"
            if row["data_version"] != version:
                problems.append(f"{where}: data_version {row['data_version']!r} != {version!r}")
            first_seen, changed_at = row["first_seen"], row["changed_at"]
            if not is_date(first_seen) or not is_date(changed_at):
                problems.append(f"{where}: first_seen/changed_at is not YYYY-MM-DD")
                continue
            if first_seen > changed_at:
                problems.append(f"{where}: first_seen {first_seen} is after changed_at {changed_at}")
            if changed_at > day:
                problems.append(f"{where}: changed_at {changed_at} is after the version date {day}")

    rows = tables["dso_lookup.csv"]
    keys = [tuple(row[c] for c in DSO_LOOKUP_KEY) for row in rows]
    if keys != sorted(keys):
        problems.append("dso_lookup.csv: rows are not sorted by (postcode, ins, section_key)")
    if len(set(keys)) != len(keys):
        problems.append("dso_lookup.csv: duplicate (postcode, ins, section_key)")
    for number, row in enumerate(rows, start=2):
        if not POSTCODE_RE.fullmatch(row["postcode"]):
            problems.append(f"dso_lookup.csv: line {number}: postcode {row['postcode']!r}")
        if not INS_RE.fullmatch(row["ins"]):
            problems.append(f"dso_lookup.csv: line {number}: ins {row['ins']!r}")
        if row["valid_from"] and (not is_date(row["valid_from"]) or row["valid_from"] > day):
            problems.append(f"dso_lookup.csv: line {number}: valid_from {row['valid_from']!r}")
    for name, key in (("operators.csv", "id"), ("notes.csv", "key"), ("sources.csv", "id")):
        ids = [row[key] for row in tables[name]]
        if len(set(ids)) != len(ids):
            problems.append(f"{name}: duplicate {key}")
        if name != "operators.csv" and ids != sorted(ids):
            problems.append(f"{name}: not sorted by {key}")
    for row in tables["sources.csv"]:
        retrieved = row["retrieved_at"]
        if not is_date(retrieved) or retrieved > day:
            problems.append(f"sources.csv: {row['id']}: retrieved_at {retrieved!r}")
        if not URL_RE.fullmatch(row["url"]):
            problems.append(f"sources.csv: {row['id']}: url {row['url']!r} is not an http(s) URL")
    for row in tables["operators.csv"]:
        for column in HTTPS_COLUMNS:
            value = row[column]
            if value and not (value.startswith("https://") and URL_RE.fullmatch(value)):
                problems.append(f"operators.csv: {row['id']}: {column} {value!r} is not an https URL (nor empty)")

    try:
        changes = parse_changes(raw["CHANGES.md"].decode("utf-8"))
    except DsoDataError as exc:
        problems += exc.problems
        changes = []
    if changes:
        newest = changes[0]
        if (newest.version, newest.date) != (base_version(version), day):
            problems.append(
                f"CHANGES.md: newest heading is {newest.version} — {newest.date}, "
                f"expected {base_version(version)} — {day}"
            )
    elif not problems:
        problems.append("CHANGES.md: no version heading")

    counts = computed_counts(tables)
    if release["counts"] != counts:
        problems.append(f"release.json: counts {release['counts']} != files {counts}")

    if problems:
        raise DsoDataError(problems)
    return Release(
        directory=directory,
        version=version,
        date=day,
        previous=release["previous"],
        counts=release["counts"],
        tables=tables,
        changes=changes,
        raw=raw,
    )


def read_meta(directory: Path) -> dict | None:
    path = directory / META
    return parse_meta(path.read_bytes()) if path.is_file() else None


def build_meta(release: Release, previous_meta: dict | None) -> dict:
    """meta.yml for `release`; removed_max never goes down."""
    candidates = removal_dates(release.changes)
    if previous_meta and previous_meta.get("removed_max"):
        candidates.append(previous_meta["removed_max"])
    return {
        "version": release.version,
        "date": release.date,
        "draft": release.draft,
        "dso_lookup_sha256": sha256_bytes(release.raw["dso_lookup.csv"]),
        "counts": release.counts,
        "removed_max": max(candidates) if candidates else "",
    }


def check_meta(meta: dict, release: Release) -> list[str]:
    """meta.yml agrees with the release it sits next to."""
    problems = []
    expected = {
        "version": release.version,
        "date": release.date,
        "draft": release.draft,
        "dso_lookup_sha256": sha256_bytes(release.raw["dso_lookup.csv"]),
        "counts": release.counts,
    }
    for key, value in expected.items():
        if meta.get(key) != value:
            problems.append(f"meta.yml: {key} is {meta.get(key)!r}, expected {value!r}")
    removed_max = meta.get("removed_max")
    if not isinstance(removed_max, str) or (removed_max and not is_date(removed_max)):
        problems.append(f"meta.yml: removed_max {removed_max!r} is not '' or YYYY-MM-DD")
    else:
        if removed_max and removed_max > release.date:
            problems.append(f"meta.yml: removed_max {removed_max} is after the version date")
        for removed in removal_dates(release.changes):
            if removed > removed_max:
                problems.append(f"meta.yml: removed_max {removed_max!r} is before a removal of {removed}")
    return problems


def dataset_note_region(key: str) -> str | None:
    """'dataset-vla-…' -> 'VLA' (a note about a whole region), else None."""
    match = DATASET_NOTE_RE.match(key)
    return match.group(1).upper() if match else None
