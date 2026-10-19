// "Quel est mon GRD ?": the page UI of the GRD lookup (_includes/dso-tool.html).
//
// An ES module, loaded on the tool page only. The lookup itself is
// dso-lookup-core.js (a port of belgian-dso-map's lookup.py); this file reads
// the form, fetches the data file named by data-dso-src, and renders the
// answer. Rules:
//   - the data file is fetched on the first focus or input of the field, or
//     when the address holds #cp= (a shared link, at load or opened in the
//     same tab);
//   - the search runs in the browser; the postcode is never sent anywhere and
//     never logged. The form names no control and stays invisible until
//     init() has wired it, so it never submits natively. The address keeps
//     #cp=…&ins=…&s=… so a result can be shared, and the page's Umami tag
//     excludes the hash and query string;
//   - one Umami event per displayed result, with the region and the operator
//     ids only: umami.track('grd-lookup', {region, elec, gas});
//   - a choice between communes or sections is a radio group with a
//     "Show" button: nothing is submitted on its own;
//   - every string comes from the inline JSON (grd_tool in
//     _data/i18n/<lang>.yml), every text node is set with textContent.

import { indexFromJson, localName, lookup, normalizePostcode, trim } from './dso-lookup-core.js';

const DATASET_NOTE_RE = /^dataset-(bru|vla|wal)-/;
const DATE_RE = /^([0-9]{4})-([0-9]{2})-([0-9]{2})$/;
const ERROR_ID = 'dso-postcode-error';
const HINT_ID = 'dso-postcode-hint';

/** Replaces {key} with values[key]; unknown keys stay as they are. */
function fill(template, values) {
  return String(template || '').replace(/\{([a-z_]+)\}/g, (match, key) =>
    Object.prototype.hasOwnProperty.call(values, key) ? String(values[key]) : match,
  );
}

// French binds : ; ! ? » to the word before, and « to the word after, with a
// no-break space (the fr_spacing filter of _plugins/typography.rb).
let frenchSpacing = false;
function typo(text) {
  return frenchSpacing ? text.replace(/ ([:;!?»])/g, '\u00a0$1').replace(/« /g, '«\u00a0') : text;
}

/** Element with attributes and children (strings become text nodes). */
function h(tag, attrs, ...children) {
  const node = document.createElement(tag);
  for (const [name, value] of Object.entries(attrs || {})) {
    if (value === null || value === undefined || value === false) continue;
    if (name === 'class') node.className = value;
    else node.setAttribute(name, value === true ? '' : String(value));
  }
  for (const child of children.flat()) {
    if (child === null || child === undefined || child === false || child === '') continue;
    node.append(typeof child === 'string' ? document.createTextNode(typo(child)) : child);
  }
  return node;
}

function trackResult(region, elec, gas) {
  try {
    if (window.umami && typeof window.umami.track === 'function') {
      window.umami.track('grd-lookup', { region, elec, gas });
    }
  } catch (error) {
    // Measurement must never break the tool.
  }
}

function init(root) {
  const script = root.querySelector('script[data-dso-src]');
  const source = script ? script.getAttribute('data-dso-src') : '';
  let strings;
  try {
    strings = JSON.parse(root.querySelector('[data-dso-i18n]').textContent);
  } catch (error) {
    return;
  }
  const ui = strings.ui || {};
  const lang = root.getAttribute('data-lang') || 'fr';
  frenchSpacing = lang === 'fr';
  const locale = root.getAttribute('data-locale') || 'fr-BE';
  const listUrl = root.getAttribute('data-list-url') || '';
  const email = root.getAttribute('data-report-email') || '';
  const form = root.querySelector('[data-dso-form]');
  const input = root.querySelector('[data-dso-input]');
  const error = root.querySelector('[data-dso-error]');
  const status = root.querySelector('[data-dso-status]');
  const body = root.querySelector('[data-dso-body]');
  if (!source || !form || !input || !error || !status || !body) return;

  const dateFormat = new Intl.DateTimeFormat(locale, {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    timeZone: 'UTC',
  });
  const formatDate = (iso) => {
    const match = DATE_RE.exec(iso || '');
    return match ? dateFormat.format(new Date(Date.UTC(+match[1], +match[2] - 1, +match[3]))) : iso;
  };

  // --- data ---------------------------------------------------------------------------
  let loading = null;
  let loaded = null;
  const load = () => {
    if (loaded) return Promise.resolve(loaded);
    if (!loading) {
      loading = fetch(source, { credentials: 'same-origin' })
        .then((response) => {
          if (!response.ok) throw new Error(`HTTP ${response.status}`);
          return response.json();
        })
        .then((json) => {
          loaded = { json, index: indexFromJson(json) };
          return loaded;
        })
        .catch((reason) => {
          loading = null; // the next search tries again
          throw reason;
        });
    }
    return loading;
  };
  const preload = () => {
    load().catch(() => {});
  };

  // --- form state ---------------------------------------------------------------------
  const setStatus = (text) => {
    status.textContent = typo(text || '');
  };
  // The error element is a role="alert" region that stays in the page: the
  // message is announced even though the focus is already on the field.
  const showError = (message) => {
    error.textContent = typo(message);
    input.setAttribute('aria-invalid', 'true');
    input.setAttribute('aria-describedby', `${HINT_ID} ${ERROR_ID}`);
  };
  const clearError = () => {
    if (!error.textContent) return;
    error.textContent = '';
    input.removeAttribute('aria-invalid');
    input.setAttribute('aria-describedby', HINT_ID);
  };
  // The address of the displayed answer ('' when there is none): "Copy the
  // link" copies it even after an in-page anchor (#faq) replaced the hash.
  let shareHash = '';
  const setHash = (params) => {
    const pairs = Object.entries(params || {}).filter(([, value]) => value);
    const hash = pairs.length ? `#${new URLSearchParams(pairs).toString()}` : '';
    shareHash = hash;
    try {
      window.history.replaceState(window.history.state, '', `${window.location.pathname}${window.location.search}${hash}`);
    } catch (reason) {
      // An address that cannot be rewritten only loses the share link.
    }
  };
  const show = (...nodes) => {
    body.replaceChildren(...nodes);
  };

  // --- names --------------------------------------------------------------------------
  const communeRegion = (json, ins) => {
    const commune = json.communes[ins];
    const at = json.commune_cols.indexOf('region');
    return commune && at >= 0 ? commune[at] : '';
  };
  const operator = (json, id) => (id && json.operators[id]) || null;
  // "www.ores.be" -> "ores.be": the link text of an operator's website.
  const siteName = (url) => {
    try {
      return new URL(url).hostname.replace(/^www\./, '');
    } catch (reason) {
      return url;
    }
  };

  // --- results ------------------------------------------------------------------------
  const tableLink = () => h('p', null, h('a', { href: listUrl }, ui.table_link));

  function renderChoice(legend, name, options, onPick) {
    const fieldset = h(
      'fieldset',
      { class: 'dso-choice__fieldset' },
      h('legend', { class: 'dso-choice__legend' }, legend),
      h(
        'div',
        { class: 'dso-choice__options' },
        options.map((option, i) =>
          h(
            'label',
            { class: 'dso-radio', for: `dso-choice-${i}` },
            h('input', { class: 'dso-radio__input', type: 'radio', name, id: `dso-choice-${i}`, value: option.value }),
            h('span', { class: 'dso-radio__label' }, option.label),
          ),
        ),
      ),
    );
    const choice = h(
      'form',
      { class: 'dso-choice', novalidate: true },
      fieldset,
      h('button', { class: 'btn btn-outline dso-choice__submit', type: 'submit' }, ui.show),
    );
    choice.addEventListener('submit', (event) => {
      event.preventDefault();
      const picked = choice.querySelector('input[type="radio"]:checked');
      if (!picked) {
        setStatus(ui.choose_missing);
        const first = choice.querySelector('input[type="radio"]');
        if (first) first.focus();
        return;
      }
      onPick(picked.value);
    });
    show(choice);
    return choice;
  }

  function renderOk(result, postcode, data) {
    const { json } = data;
    const region = result.region;
    const commune = localName(result.commune, lang, region);
    const section = result.section ? localName(result.section.name, lang, region) : '';
    const place = section ? `${commune} — ${section}` : commune;
    const flags = result.flags || [];
    const flagLabel = (flag) => (strings.flags && strings.flags[flag]) || flag;

    // Meta line: postcode, region, province.
    const meta = [postcode, (strings.regions && strings.regions[region]) || region];
    if (result.province && strings.provinces && strings.provinces[result.province]) {
      meta.push(fill(ui.meta_province, { province: strings.provinces[result.province] }));
    }

    // Electricity: the operator, then why it may differ from the designated DSO.
    const elec = operator(json, result.elec.operator);
    const designated = operator(json, result.elec.designated);
    const elecPanel = h(
      'section',
      { class: 'dso-panel', 'aria-labelledby': 'dso-elec-title' },
      h('h3', { class: 'dso-panel__title', id: 'dso-elec-title' }, ui.elec_title),
      h('p', { class: 'dso-panel__name' }, elec ? elec.name : result.elec.operator),
      region === 'VLA' && elec && elec.legal_name && elec.legal_name !== elec.name
        ? h('p', { class: 'dso-panel__detail' }, fill(ui.legal_name, { legal_name: elec.legal_name }))
        : null,
      elec && elec.website
        ? h('p', { class: 'dso-panel__detail' }, h('a', { href: elec.website, rel: 'noopener' }, fill(ui.website, { site: siteName(elec.website) })))
        : null,
      result.elec.operator !== result.elec.designated
        ? h(
            'p',
            { class: 'dso-panel__note' },
            fill(ui.operator_differs, {
              operator: elec ? elec.name : result.elec.operator,
              designated: designated ? designated.name : result.elec.designated,
            }),
          )
        : null,
    );

    // Gas: the operator, or no designated gas DSO.
    const gas = operator(json, result.gas.operator);
    const gasChildren = [h('h3', { class: 'dso-panel__title', id: 'dso-gas-title' }, ui.gas_title)];
    if (result.gas.status === 'none' || !gas) {
      gasChildren.push(h('p', { class: 'dso-panel__name dso-panel__name--none' }, ui.gas_none));
    } else {
      gasChildren.push(h('p', { class: 'dso-panel__name' }, gas.name));
      if (gas.website) {
        gasChildren.push(
          h('p', { class: 'dso-panel__detail' }, h('a', { href: gas.website, rel: 'noopener' }, fill(ui.website, { site: siteName(gas.website) }))),
        );
      }
      if (result.gas.status === 'foreign') gasChildren.push(h('p', { class: 'dso-panel__note' }, ui.gas_foreign));
      gasChildren.push(h('p', { class: 'dso-panel__note' }, ui.gas_street));
    }
    if (flags.includes('propane_note')) gasChildren.push(h('p', { class: 'dso-panel__note' }, flagLabel('propane_note')));
    const gasPanel = h('section', { class: 'dso-panel', 'aria-labelledby': 'dso-gas-title' }, gasChildren);

    // What else to know: open questions, the row's note, the region's notes.
    const notes = [];
    if (flags.includes('to_confirm')) notes.push(ui.to_confirm);
    if (flags.includes('transition')) notes.push(`${flagLabel('transition')}.`);
    // valid_from dates the whole row (electricity and gas), not the operator.
    if (result.valid_from) notes.push(fill(ui.valid_from, { date: formatDate(result.valid_from) }));
    const noteText = (key) => {
      const note = json.notes[key];
      return note ? note[lang] || note.fr : '';
    };
    if (result.note_key) notes.push(noteText(result.note_key));
    Object.keys(json.notes)
      .sort()
      .forEach((key) => {
        const match = DATASET_NOTE_RE.exec(key);
        if (match && match[1].toUpperCase() === region) notes.push(noteText(key));
      });
    const notesBlock = notes.filter(Boolean).length
      ? h(
          'section',
          { class: 'dso-result__notes', 'aria-labelledby': 'dso-notes-title' },
          h('h3', { class: 'dso-result__subtitle', id: 'dso-notes-title' }, ui.notes_title),
          h('ul', { class: 'dso-result__list' }, notes.filter(Boolean).map((text) => h('li', null, text))),
        )
      : null;

    // Region blocks: regulator and tariffs, how to check, energy sharing.
    const template = root.querySelector(`template[data-dso-region="${region}"]`);
    const part = (name) => {
      const found = template && template.content.querySelector(`[data-dso-part="${name}"]`);
      return found ? found.cloneNode(true) : null;
    };
    const regulatorCode = result.regulator;
    const regulator = (strings.regulators && strings.regulators[regulatorCode]) || null;
    const checkTemplate = root.querySelector('template[data-dso-check]');
    const block = (id, title, ...content) =>
      h(
        'section',
        { class: 'dso-result__block', 'aria-labelledby': id },
        h('h3', { class: 'dso-result__subtitle', id }, title),
        ...content,
      );

    // Footer: data version, sources, error report (never with the postcode), share link.
    const version = json.meta.version;
    const subject = encodeURIComponent(ui.report_subject || '');
    const mailBody = encodeURIComponent(fill(ui.report_body, { version }));
    const copy = h('button', { class: 'btn btn-outline btn--sm', type: 'button' }, ui.copy_link);
    copy.addEventListener('click', () => {
      const done = () => setStatus(ui.copied);
      const failed = () => setStatus(ui.copy_failed);
      const link = `${window.location.origin}${window.location.pathname}${window.location.search}${shareHash}`;
      if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
        navigator.clipboard.writeText(link).then(done, failed);
      } else {
        failed();
      }
    });
    const footer = h(
      'footer',
      { class: 'dso-result__footer' },
      h(
        'p',
        { class: 'dso-result__meta-line' },
        fill(ui.data_line, { date: formatDate(json.meta.date), version }),
        ' · ',
        h('a', { href: `${listUrl}#sources` }, ui.sources),
        ' · ',
        email ? h('a', { href: `mailto:${email}?subject=${subject}&body=${mailBody}` }, ui.report) : null,
      ),
      json.meta.draft ? h('p', { class: 'dso-result__draft' }, ui.draft) : null,
      copy,
    );

    const card = h(
      'article',
      { class: 'dso-result', 'aria-labelledby': 'dso-result-title' },
      h('h2', { class: 'dso-result__title', id: 'dso-result-title' }, place),
      h('p', { class: 'dso-result__meta' }, meta.join(' · ')),
      h('div', { class: 'dso-result__panels' }, elecPanel, gasPanel),
      notesBlock,
      block(
        'dso-regulator-title',
        ui.regulator_title,
        regulator
          ? h('p', null, regulator.url ? h('a', { href: regulator.url, rel: 'noopener' }, regulator.name) : regulator.name)
          : null,
        part('regulator'),
      ),
      block('dso-check-title', ui.check_title, checkTemplate ? checkTemplate.content.cloneNode(true) : null),
      block('dso-sharing-title', ui.sharing_title, part('sharing')),
      footer,
    );
    show(card);
    setStatus(fill(ui.status_ok, { place }));
    trackResult(region, result.elec.operator, result.gas.operator || result.gas.status);
  }

  // Only the latest search renders: one started while the data load (a
  // second Enter, a hashchange) makes the earlier one drop its answer, so a
  // displayed result is tracked once.
  let latest = 0;
  async function search(raw, filters, options) {
    const ticket = ++latest;
    const opts = options || {};
    const postcode = normalizePostcode(raw);
    if (!postcode) {
      show();
      setStatus('');
      setHash(null);
      showError(ui.invalid);
      if (!opts.quiet) input.focus();
      return;
    }
    clearError();
    input.value = postcode;
    if (!loaded) setStatus(ui.loading);
    let data;
    try {
      data = await load();
    } catch (reason) {
      if (ticket !== latest) return;
      setStatus(ui.load_error);
      show(tableLink());
      return;
    }
    if (ticket !== latest) return;
    const answer = lookup(data.index, postcode, filters || {});
    switch (answer.status) {
      case 'choose_commune': {
        setHash({ cp: postcode });
        const options = answer.communes.map((commune) => ({
          value: commune.ins,
          label: localName(commune.name, lang, communeRegion(data.json, commune.ins)),
        }));
        const choice = renderChoice(fill(ui.choose_commune, { postcode }), 'dso-commune', options, (ins) =>
          search(postcode, { ins }),
        );
        setStatus(ui.choose_status);
        if (!opts.quiet) choice.querySelector('input').focus();
        break;
      }
      case 'choose_section': {
        setHash({ cp: postcode, ins: answer.ins });
        const region = communeRegion(data.json, answer.ins);
        const options = answer.sections.map((section) => ({
          value: section.section_key,
          label: localName(section.name, lang, region),
        }));
        const legend = fill(ui.choose_section, { commune: localName(answer.commune, lang, region) });
        const choice = renderChoice(legend, 'dso-section', options, (key) =>
          search(postcode, { ins: answer.ins, section: key }),
        );
        setStatus(ui.choose_status);
        if (!opts.quiet) choice.querySelector('input').focus();
        break;
      }
      case 'ok': {
        const result = answer.result;
        setHash({ cp: postcode, ins: result.ins, s: result.section ? result.section.section_key : '' });
        renderOk(result, postcode, data);
        break;
      }
      default: {
        setHash(null);
        const message = fill(ui.not_found, { postcode });
        show(h('p', { class: 'dso-output__message' }, message), tableLink());
        setStatus(message);
      }
    }
  }

  // --- events -------------------------------------------------------------------------
  input.addEventListener('focus', preload, { once: true });
  input.addEventListener('input', () => {
    preload();
    clearError();
  });
  // A pasted " 5020 " or "5020\n" keeps its digits: maxlength would cut the
  // text before TRIM could run, and could turn "50200" into a valid "5020".
  input.addEventListener('paste', (event) => {
    const text = event.clipboardData ? event.clipboardData.getData('text') : null;
    if (typeof text !== 'string') return;
    event.preventDefault();
    const start = input.selectionStart === null ? input.value.length : input.selectionStart;
    const end = input.selectionEnd === null ? input.value.length : input.selectionEnd;
    input.setRangeText(trim(text), start, end, 'end');
    input.dispatchEvent(new Event('input', { bubbles: true }));
  });
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    search(input.value, {});
  });

  // A shared link: #cp=…&ins=…&s=…, at load and when one is opened in the
  // same tab (hashchange; setHash's replaceState fires none). Other anchors
  // (#faq) are ignored, and so is the hash of the answer on display (Back
  // from #faq to it).
  const fromHash = () => {
    const hash = window.location.hash;
    if (hash === shareHash || !/(^|&)cp=/.test(hash.slice(1))) return;
    const params = new URLSearchParams(hash.slice(1));
    const postcode = params.get('cp') || '';
    input.value = postcode;
    search(postcode, { ins: params.get('ins') || '', section: params.get('s') || '' }, { quiet: true });
  };
  window.addEventListener('hashchange', fromHash);
  fromHash();
  form.removeAttribute('data-dso-pending');
}

const tool = document.querySelector('[data-dso-tool]');
if (tool) init(tool);
