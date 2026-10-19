// Tests of assets/js/dso-lookup-core.js (node:test, no dependencies).
//
//   node --test scripts/dso-lookup.test.mjs
//       unit cases, then every kind=postcode row of _data/dso/vectors.csv
//       against an index built from _data/dso/dso_lookup.csv
//   DSO_JSON_DIR=_site/assets/data node --test scripts/dso-lookup.test.mjs
//       also: exactly one dso-*.json there, the same vectors through
//       indexFromJson(), as many rows as the CSV, and every postcode answered
//       as the CSV answers it (this catches serialisation bugs in
//       _plugins/dso_pages.rb)
//
// Vector semantics (belgian-dso-map README, "Test vectors"): "*" is not
// asserted, an empty cell must be empty, expect_key and expect_flags are
// compared as sets of their |-separated values.
//
// Node 22.7+ (ESM detection of the .js module without a package.json).

import assert from 'node:assert/strict';
import { readdirSync, readFileSync } from 'node:fs';
import path from 'node:path';
import { test } from 'node:test';
import { fileURLToPath } from 'node:url';

import {
  REGION_REGULATOR,
  buildIndex,
  communeName,
  indexFromJson,
  lookup,
  normalizeName,
  normalizePostcode,
  sectionName,
  trim,
} from '../assets/js/dso-lookup-core.js';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const DATA = path.join(ROOT, '_data', 'dso');
const ANY = '*';

// --- RFC 4180 -------------------------------------------------------------------------

/** Parse RFC 4180 text (quotes, doubled quotes, LF or CRLF) into arrays of strings. */
function parseCsv(text) {
  if (text.charCodeAt(0) === 0xfeff) throw new Error('CSV starts with a BOM');
  const records = [];
  let record = [];
  let field = '';
  let i = 0;
  let quoted = false;
  let atFieldStart = true;
  while (i < text.length) {
    const ch = text[i];
    if (quoted) {
      if (ch === '"') {
        if (text[i + 1] === '"') {
          field += '"';
          i += 2;
          continue;
        }
        quoted = false;
        i += 1;
        const next = text[i];
        if (next !== undefined && next !== ',' && next !== '\n' && next !== '\r') {
          throw new Error(`CSV: character after a closing quote in record ${records.length + 1}`);
        }
        continue;
      }
      field += ch;
      i += 1;
      continue;
    }
    if (ch === '"') {
      if (!atFieldStart) throw new Error(`CSV: quote inside an unquoted field in record ${records.length + 1}`);
      quoted = true;
      atFieldStart = false;
      i += 1;
      continue;
    }
    if (ch === ',') {
      record.push(field);
      field = '';
      atFieldStart = true;
      i += 1;
      continue;
    }
    if (ch === '\n' || ch === '\r') {
      record.push(field);
      records.push(record);
      record = [];
      field = '';
      atFieldStart = true;
      i += ch === '\r' && text[i + 1] === '\n' ? 2 : 1;
      continue;
    }
    field += ch;
    atFieldStart = false;
    i += 1;
  }
  if (quoted) throw new Error('CSV: unterminated quoted field');
  if (!atFieldStart || field !== '' || record.length) {
    record.push(field);
    records.push(record);
  }
  return records;
}

function readTable(file) {
  const [header, ...records] = parseCsv(readFileSync(file, 'utf8'));
  return records.map((cells, n) => {
    assert.equal(cells.length, header.length, `${path.basename(file)}: record ${n + 2} has ${cells.length} fields`);
    return Object.fromEntries(header.map((column, i) => [column, cells[i]]));
  });
}

// --- Vectors --------------------------------------------------------------------------

/** What a postcode vector observes, in the terms of its expect_* columns (lookup.py observe()). */
function observe(index, vector) {
  const found = lookup(index, vector.postcode, { ins: vector.ins, section: vector.section_key });
  const observed = { status: found.status, key: '', elec: '', gas_status: '', gas: '', flags: '' };
  if (found.status === 'ok') {
    const { result } = found;
    observed.key = result.ins + (result.section ? `/${result.section.section_key}` : '');
    observed.elec = result.elec.operator;
    observed.gas_status = result.gas.status;
    observed.gas = result.gas.operator;
    observed.flags = result.flags.join('|');
  } else if (found.status === 'choose_commune') {
    observed.key = found.communes.map((c) => c.ins).join('|');
  } else if (found.status === 'choose_section') {
    observed.key = found.sections.map((s) => s.section_key).join('|');
  }
  return observed;
}

function asSet(cell) {
  return [...new Set(cell ? cell.split('|') : [])].sort();
}

/** Mismatches of one vector (lookup.py check_vector()). */
function checkVector(index, vector) {
  const problems = [];
  for (const [field, actual] of Object.entries(observe(index, vector))) {
    const expected = vector[`expect_${field}`];
    if (expected === ANY) continue;
    const same = field === 'key' || field === 'flags'
      ? JSON.stringify(asSet(expected)) === JSON.stringify(asSet(actual))
      : expected === actual;
    if (!same) problems.push(`${vector.name}: ${field} expected ${JSON.stringify(expected)}, got ${JSON.stringify(actual)}`);
  }
  return problems;
}

const csvRows = readTable(path.join(DATA, 'dso_lookup.csv'));
const vectors = readTable(path.join(DATA, 'vectors.csv'));
const postcodeVectors = vectors.filter((v) => v.kind === 'postcode');
const csvIndex = buildIndex(csvRows);

function runVectors(index) {
  return postcodeVectors.flatMap((vector) => checkVector(index, vector));
}

// --- Unit cases -----------------------------------------------------------------------

test('normalizePostcode: TRIM of exactly space, tab, CR, LF, NBSP and BOM', () => {
  assert.equal(normalizePostcode(' 5020 '), '5020');
  assert.equal(normalizePostcode('\t5020\r\n'), '5020');
  assert.equal(normalizePostcode(' 5020 '), '5020');
  assert.equal(normalizePostcode('﻿5020'), '5020');
  assert.equal(normalizePostcode('5020'), '5020');
});

test('normalizePostcode: anything but four ASCII digits is null', () => {
  for (const raw of ['', null, undefined, '502', '50200', '50a0', '5O20', '50 20', '-502',
    ' 5020', '5020 ', '　5020', '​5020', '５０２０',
    '٥٠٢٠']) {
    assert.equal(normalizePostcode(raw), null, JSON.stringify(raw));
  }
  assert.equal(normalizePostcode(5020), '5020'); // a number is read as its digits
});

test('trim keeps U+2003 and U+3000 (unlike String.prototype.trim)', () => {
  assert.equal(trim(' x '), ' x ');
  assert.equal(trim('　x'), '　x');
  assert.equal(trim('  ﻿x\t\r\n'), 'x');
});

test('normalizeName: NFKD, no marks, lower case, [a-z0-9] only', () => {
  assert.equal(normalizeName('Marche lès Dames'), 'marchelesdames');
  assert.equal(normalizeName('MARCHE-LES-DAMES'), 'marchelesdames');
  assert.equal(normalizeName("Braine-l'Alleud"), 'brainelalleud');
  assert.equal(normalizeName('Namür'), 'namur');
  assert.equal(normalizeName(''), '');
});

const synthetic = buildIndex([
  { postcode: '1000', ins: '21004', commune_fr: 'Bruxelles', commune_nl: 'Brussel', commune_de: 'Brüssel', region: 'BRU', province: '', section_key: '', section_fr: '', section_nl: '', section_de: '', elec_operator: 'sibelga', elec_designated: 'sibelga', gas_status: 'designated', gas_operator: 'sibelga', flags: '', note_key: '', source_ids: 'a|b', valid_from: '', data_version: 'v1' },
  { postcode: '1040', ins: '21005', commune_fr: 'Etterbeek', commune_nl: 'Etterbeek', commune_de: '', region: 'BRU', province: '', section_key: '', section_fr: '', section_nl: '', section_de: '', elec_operator: 'sibelga', elec_designated: 'sibelga', gas_status: 'designated', gas_operator: 'sibelga', flags: '', note_key: '', source_ids: '', valid_from: '', data_version: 'v1' },
  { postcode: '1040', ins: '21004', commune_fr: 'Bruxelles', commune_nl: 'Brussel', commune_de: 'Brüssel', region: 'BRU', province: '', section_key: '', section_fr: '', section_nl: '', section_de: '', elec_operator: 'sibelga', elec_designated: 'sibelga', gas_status: 'designated', gas_operator: 'sibelga', flags: '', note_key: '', source_ids: '', valid_from: '', data_version: 'v1' },
  { postcode: '5020', ins: '92094', commune_fr: 'Namur', commune_nl: 'Namen', commune_de: 'Namür', region: 'WAL', province: 'BE-WNA', section_key: 'flawinne', section_fr: 'Flawinne', section_nl: '', section_de: '', elec_operator: 'aieg', elec_designated: 'ores', gas_status: 'designated', gas_operator: 'ores', flags: 'transition|operator_differs', note_key: 'n', source_ids: '', valid_from: '2026-07-01', data_version: 'v1' },
  { postcode: '5020', ins: '92094', commune_fr: 'Namur', commune_nl: 'Namen', commune_de: 'Namür', region: 'WAL', province: 'BE-WNA', section_key: 'champion', section_fr: 'Champion', section_nl: '', section_de: '', elec_operator: 'ores', elec_designated: 'ores', gas_status: 'designated', gas_operator: 'ores', flags: '', note_key: '', source_ids: '', valid_from: '', data_version: 'v1' },
]);

test('lookup: choose_commune sorted by INS, first row of each', () => {
  const found = lookup(synthetic, '1040');
  assert.deepEqual(found, {
    status: 'choose_commune',
    communes: [
      { ins: '21004', name: { fr: 'Bruxelles', nl: 'Brussel', de: 'Brüssel' } },
      { ins: '21005', name: { fr: 'Etterbeek', nl: 'Etterbeek', de: '' } },
    ],
    data_version: 'v1',
  });
});

test('lookup: choose_section sorted by key, each with its electricity operator', () => {
  const found = lookup(synthetic, '5020');
  assert.equal(found.status, 'choose_section');
  assert.equal(found.ins, '92094');
  assert.deepEqual(found.commune, { fr: 'Namur', nl: 'Namen', de: 'Namür' });
  assert.deepEqual(found.sections, [
    { section_key: 'champion', name: { fr: 'Champion', nl: '', de: '' }, elec_operator: 'ores' },
    { section_key: 'flawinne', name: { fr: 'Flawinne', nl: '', de: '' }, elec_operator: 'aieg' },
  ]);
});

test('lookup: a filter that matches nothing is ignored', () => {
  assert.equal(lookup(synthetic, '1040', { ins: '99999' }).status, 'choose_commune');
  assert.equal(lookup(synthetic, '1000', { ins: '21005' }).result.ins, '21004');
  assert.equal(lookup(synthetic, '5020', { section: 'zzz' }).status, 'choose_section');
  assert.equal(lookup(synthetic, '5020', { ins: '21004' }).status, 'choose_section');
  assert.equal(lookup(synthetic, '1040', { ins: ' 21005 ' }).result.ins, '21005');
  assert.equal(lookup(synthetic, '5020', { section: ' flawinne' }).result.section.section_key, 'flawinne');
});

test('lookup: section applies only once a single INS remains', () => {
  assert.equal(lookup(synthetic, '1040', { section: 'flawinne' }).status, 'choose_commune');
});

test('lookup: ok has the reference result shape', () => {
  const found = lookup(synthetic, '5020', { ins: '92094', section: 'flawinne' });
  assert.deepEqual(found, {
    status: 'ok',
    data_version: 'v1',
    result: {
      postcode: '5020',
      ins: '92094',
      commune: { fr: 'Namur', nl: 'Namen', de: 'Namür' },
      section: { section_key: 'flawinne', name: { fr: 'Flawinne', nl: '', de: '' } },
      region: 'WAL',
      province: 'BE-WNA',
      regulator: 'BE-WAL-CWAPE',
      elec: { operator: 'aieg', designated: 'ores' },
      gas: { status: 'designated', operator: 'ores' },
      flags: ['transition', 'operator_differs'],
      note_key: 'n',
      source_ids: [],
      valid_from: '2026-07-01',
      data_version: 'v1',
    },
  });
  assert.deepEqual(lookup(synthetic, '1000').result.source_ids, ['a', 'b']);
  assert.equal(lookup(synthetic, '1000').result.section, null);
});

test('lookup: invalid or unknown postcode is not_found', () => {
  for (const raw of ['9999', '502', '', null, ' 5020', '５０２０']) {
    assert.deepEqual(lookup(synthetic, raw), { status: 'not_found', data_version: 'v1' });
  }
});

test('REGION_REGULATOR is the contract table', () => {
  assert.deepEqual({ ...REGION_REGULATOR }, { BRU: 'BE-BRU-BRUGEL', VLA: 'BE-VLA-VREG', WAL: 'BE-WAL-CWAPE' });
});

test('communeName / sectionName: nl/de fall back to fr; English uses the official name', () => {
  const brussels = { fr: 'Bruxelles', nl: 'Brussel', de: 'Brüssel' };
  assert.equal(communeName(brussels, 'fr', 'BRU'), 'Bruxelles');
  assert.equal(communeName(brussels, 'nl', 'BRU'), 'Brussel');
  assert.equal(communeName(brussels, 'de', 'BRU'), 'Brüssel');
  assert.equal(communeName(brussels, 'en', 'BRU'), 'Bruxelles / Brussel');
  assert.equal(communeName({ fr: 'Etterbeek', nl: 'Etterbeek', de: '' }, 'en', 'BRU'), 'Etterbeek');
  assert.equal(communeName({ fr: 'Etterbeek', nl: 'Etterbeek', de: '' }, 'de', 'BRU'), 'Etterbeek');
  assert.equal(communeName({ fr: 'Baerle-Duc', nl: 'Baarle-Hertog', de: '' }, 'en', 'VLA'), 'Baarle-Hertog');
  assert.equal(communeName({ fr: 'Namur', nl: 'Namen', de: 'Namür' }, 'en', 'WAL'), 'Namur');
  assert.equal(sectionName({ fr: 'Saint-Marc', nl: '', de: '' }, 'nl', 'WAL'), 'Saint-Marc');
  assert.equal(sectionName({ fr: 'Namur (centre)', nl: 'Namen (centrum)', de: '' }, 'nl', 'WAL'), 'Namen (centrum)');
});

test('parseCsv: quotes, doubled quotes, commas and CRLF', () => {
  assert.deepEqual(parseCsv('a,b\r\n"x, ""y""",\n'), [['a', 'b'], ['x, "y"', '']]);
  assert.deepEqual(parseCsv('a\n"multi\nline"\n'), [['a'], ['multi\nline']]);
  assert.throws(() => parseCsv('﻿a,b\n'));
  assert.throws(() => parseCsv('a"b\n'));
  assert.throws(() => parseCsv('"a\n'));
});

// --- The data release in _data/dso -----------------------------------------------------

test('vectors.csv has postcode vectors', () => {
  assert.ok(postcodeVectors.length > 0, 'no kind=postcode row in _data/dso/vectors.csv');
});

test('every postcode vector passes on dso_lookup.csv', () => {
  assert.deepEqual(runVectors(csvIndex), []);
});

// --- The built JSON (DSO_JSON_DIR) -------------------------------------------------------

const jsonDir = process.env.DSO_JSON_DIR;

test('built JSON: one file, same rows, same answers as the CSV', { skip: !jsonDir && 'DSO_JSON_DIR is not set' }, () => {
  const files = readdirSync(jsonDir).filter((name) => /^dso-.+\.json$/.test(name));
  assert.equal(files.length, 1, `expected exactly one dso-*.json in ${jsonDir}, found ${files.join(', ') || 'none'}`);
  const json = JSON.parse(readFileSync(path.join(jsonDir, files[0]), 'utf8'));
  const version = csvRows[0].data_version;
  assert.equal(files[0], `dso-${version}.json`);
  assert.equal(json.meta.version, version);
  const rowCount = Object.values(json.postcodes).reduce((sum, list) => sum + list.length, 0);
  assert.equal(rowCount, csvRows.length, 'row count differs from dso_lookup.csv');

  const jsonIndex = indexFromJson(json);
  assert.deepEqual(runVectors(jsonIndex), []);

  // Every postcode, and every INS and section filter of it, answered alike
  // (source_ids is not in the browser file).
  const strip = (found) => {
    if (found.status !== 'ok') return found;
    const { source_ids: _ignored, ...result } = found.result;
    return { ...found, result };
  };
  let compared = 0;
  for (const [postcode, rows] of csvIndex.byPostcode) {
    const queries = [{}, ...rows.map((row) => ({ ins: row.ins })), ...rows.map((row) => ({ ins: row.ins, section: row.section_key }))];
    for (const query of queries) {
      assert.deepEqual(strip(lookup(jsonIndex, postcode, query)), strip(lookup(csvIndex, postcode, query)), `${postcode} ${JSON.stringify(query)}`);
      compared += 1;
    }
  }
  assert.ok(compared > 0);
});
