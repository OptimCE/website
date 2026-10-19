// GRD lookup core: postcode -> distribution system operators, in the browser.
//
// A line-for-line port of resolve() in belgian-dso-map scripts/lookup.py (the
// reference of the data contract); dso-lookup's api/dso/lookup.py is the
// other port. scripts/dso-lookup.test.mjs runs the shared vectors.csv against
// this file, on the CSV and on the JSON the build writes
// (_plugins/dso_pages.rb). Pure functions, no DOM: the page UI lives in
// grd-lookup.js.
//
// Results (same shape as the reference and the service):
//   not_found       {status, data_version}
//   choose_commune  {status, communes: [{ins, name: {fr, nl, de}}], data_version}
//   choose_section  {status, ins, commune: {fr, nl, de},
//                    sections: [{section_key, name: {fr, nl, de}, elec_operator}], data_version}
//   ok              {status, data_version, result: {postcode, ins, commune, section, region,
//                    province, regulator, elec: {operator, designated},
//                    gas: {status, operator}, flags, note_key, source_ids, valid_from, data_version}}
// Names are returned as stored (an empty nl/de stays empty); use communeName()
// and sectionName() to display them.

// Regulator of each region (monorepo reference/regulators.json codes).
export const REGION_REGULATOR = Object.freeze({
  BRU: 'BE-BRU-BRUGEL',
  VLA: 'BE-VLA-VREG',
  WAL: 'BE-WAL-CWAPE',
});

// TRIM removes exactly these characters at both ends: space, tab, CR, LF,
// U+00A0 and U+FEFF. String.prototype.trim() would also remove U+2003 and
// friends, which the contract keeps (they make the postcode invalid).
const TRIM_RE = /^[ \t\r\n ﻿]+|[ \t\r\n ﻿]+$/g;
// Exactly four ASCII digits (never \d, never full-width digits).
const POSTCODE_RE = /^[0-9]{4}$/;

export function trim(raw) {
  return (raw === null || raw === undefined ? '' : String(raw)).replace(TRIM_RE, '');
}

/** TRIM, then exactly four ASCII digits; anything else is null. */
export function normalizePostcode(raw) {
  const value = trim(raw);
  return POSTCODE_RE.test(value) ? value : null;
}

/** NFKD, drop combining marks, lower case, keep [a-z0-9]: "Marche lès Dames" -> "marchelesdames". */
export function normalizeName(raw) {
  return (raw === null || raw === undefined ? '' : String(raw))
    .normalize('NFKD')
    .replace(/\p{M}/gu, '')
    .toLowerCase()
    .replace(/[^a-z0-9]/g, '');
}

function splitList(cell) {
  return cell ? cell.split('|') : [];
}

function byString(a, b) {
  return a < b ? -1 : a > b ? 1 : 0;
}

/**
 * Index rows of dso_lookup.csv (objects keyed by its header) by postcode and
 * by INS, keeping the file order.
 */
export function buildIndex(rows) {
  const byPostcode = new Map();
  const byIns = new Map();
  let dataVersion = '';
  for (const row of rows) {
    if (!byPostcode.has(row.postcode)) byPostcode.set(row.postcode, []);
    byPostcode.get(row.postcode).push(row);
    if (!byIns.has(row.ins)) byIns.set(row.ins, []);
    byIns.get(row.ins).push(row);
    dataVersion = row.data_version;
  }
  return { byPostcode, byIns, dataVersion };
}

/**
 * Rows of the browser file assets/data/dso-<version>.json, back in the shape
 * of dso_lookup.csv (without source_ids, first_seen and changed_at, which the
 * file does not carry), indexed with buildIndex().
 */
export function rowsFromJson(json) {
  if (!json || json.format !== 1) throw new Error('dso data: unknown format');
  const cols = json.cols;
  const communeCols = json.commune_cols;
  const version = json.meta.version;
  const rows = [];
  for (const [postcode, list] of Object.entries(json.postcodes)) {
    for (const values of list) {
      if (values.length !== cols.length) throw new Error(`dso data: bad row for ${postcode}`);
      const row = { postcode };
      cols.forEach((col, i) => {
        row[col] = values[i];
      });
      const commune = json.communes[row.ins];
      if (!commune || commune.length !== communeCols.length) {
        throw new Error(`dso data: unknown commune ${row.ins}`);
      }
      communeCols.forEach((col, i) => {
        row[col] = commune[i];
      });
      row.source_ids = '';
      row.data_version = version;
      rows.push(row);
    }
  }
  rows.sort((a, b) => byString(a.postcode, b.postcode) || byString(a.ins, b.ins) || byString(a.section_key, b.section_key));
  return rows;
}

export function indexFromJson(json) {
  return buildIndex(rowsFromJson(json));
}

// --- Results ----------------------------------------------------------------------------

function names(row, prefix) {
  return { fr: row[`${prefix}_fr`], nl: row[`${prefix}_nl`], de: row[`${prefix}_de`] };
}

function notFound(index) {
  return { status: 'not_found', data_version: index.dataVersion };
}

function chooseCommune(index, rows) {
  const firstByIns = new Map();
  for (const row of rows) if (!firstByIns.has(row.ins)) firstByIns.set(row.ins, row);
  const communes = [...firstByIns.keys()]
    .sort(byString)
    .map((ins) => ({ ins, name: names(firstByIns.get(ins), 'commune') }));
  return { status: 'choose_commune', communes, data_version: index.dataVersion };
}

function chooseSection(index, rows) {
  const sections = [...rows]
    .sort((a, b) => byString(a.section_key, b.section_key))
    .map((row) => ({
      section_key: row.section_key,
      name: names(row, 'section'),
      elec_operator: row.elec_operator,
    }));
  return {
    status: 'choose_section',
    ins: rows[0].ins,
    commune: names(rows[0], 'commune'),
    sections,
    data_version: index.dataVersion,
  };
}

function ok(index, row) {
  const section = row.section_key ? { section_key: row.section_key, name: names(row, 'section') } : null;
  const result = {
    postcode: row.postcode,
    ins: row.ins,
    commune: names(row, 'commune'),
    section,
    region: row.region,
    province: row.province,
    regulator: REGION_REGULATOR[row.region],
    elec: { operator: row.elec_operator, designated: row.elec_designated },
    gas: { status: row.gas_status, operator: row.gas_operator },
    flags: splitList(row.flags),
    note_key: row.note_key,
    source_ids: splitList(row.source_ids),
    valid_from: row.valid_from,
    data_version: row.data_version,
  };
  return { status: 'ok', result, data_version: index.dataVersion };
}

/**
 * Postcode route (resolve() of the reference).
 *   1. Invalid postcode, or no row: not_found.
 *   2. An ins or section filter that matches nothing is ignored; section
 *      applies only once a single INS remains.
 *   3. Several INS: choose_commune (sorted by INS).
 *   4. One INS, several sections: choose_section (sorted by key).
 *   5. Otherwise: ok.
 */
export function lookup(index, postcode, { ins = '', section = '' } = {}) {
  const pc = normalizePostcode(postcode);
  let rows = pc ? index.byPostcode.get(pc) || [] : [];
  if (rows.length === 0) return notFound(index);
  const wantedIns = trim(ins);
  if (wantedIns) {
    const matching = rows.filter((row) => row.ins === wantedIns);
    if (matching.length) rows = matching;
  }
  if (new Set(rows.map((row) => row.ins)).size > 1) return chooseCommune(index, rows);
  const wantedSection = trim(section);
  if (wantedSection) {
    const matching = rows.filter((row) => row.section_key === wantedSection);
    if (matching.length) rows = matching;
  }
  if (rows.length > 1) return chooseSection(index, rows);
  return ok(index, rows[0]);
}

// --- Names ------------------------------------------------------------------------------

/**
 * Display name of {fr, nl, de} in a page language. An empty nl or de name is
 * the fr one. English uses the official name of the region: nl in Flanders,
 * fr in Wallonia, "fr / nl" in Brussels. _plugins/dso_pages.rb (local_name)
 * applies the same rule to the municipality table.
 */
export function localName(name, lang, region) {
  const fr = (name && name.fr) || '';
  const nl = (name && name.nl) || fr;
  const de = (name && name.de) || fr;
  if (lang === 'nl') return nl;
  if (lang === 'de') return de;
  if (lang === 'en') {
    if (region === 'VLA') return nl;
    if (region === 'BRU') return fr === nl ? fr : `${fr} / ${nl}`;
    return fr;
  }
  return fr;
}

/** Name of a commune ({fr, nl, de} from a result) in `lang`; `region` matters for English. */
export function communeName(name, lang, region) {
  return localName(name, lang, region);
}

/** Name of a section ({fr, nl, de} from a result) in `lang`; same rule as communes. */
export function sectionName(name, lang, region) {
  return localName(name, lang, region);
}
