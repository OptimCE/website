(function () {
  'use strict';

  var root = document.documentElement;
  var reduceMotion = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);

  function onMediaChange(query, handler) {
    if (!query) return;
    if (query.addEventListener) query.addEventListener('change', handler);
    else if (query.addListener) query.addListener(handler);
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  // --- Theme (light / dark) ---
  // head.html applies a stored choice before the first paint; this wires the
  // switch. Picking the system's own theme clears the stored choice, so the
  // site follows the system setting again.
  var darkQuery = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  var themeToggles = document.querySelectorAll('[data-theme-toggle]');

  function systemTheme() {
    return darkQuery && darkQuery.matches ? 'dark' : 'light';
  }

  function currentTheme() {
    return root.getAttribute('data-theme') || systemTheme();
  }

  // The browser's own UI colour (mobile address bar) follows the theme shown.
  function syncThemeColor() {
    var chosen = root.getAttribute('data-theme');
    document.querySelectorAll('meta[name="theme-color"]').forEach(function (meta) {
      var forDark = (meta.getAttribute('media') || '').indexOf('dark') !== -1;
      var theme = chosen || (forDark ? 'dark' : 'light');
      meta.setAttribute('content', theme === 'dark' ? '#0e120e' : '#ffffff');
    });
  }

  function syncThemeToggles() {
    var dark = currentTheme() === 'dark';
    themeToggles.forEach(function (btn) {
      btn.setAttribute('aria-pressed', dark ? 'true' : 'false');
    });
  }

  function setTheme(theme) {
    if (theme === systemTheme()) {
      root.removeAttribute('data-theme');
      try { localStorage.removeItem('oce-theme'); } catch (e) { /* storage blocked */ }
    } else {
      root.setAttribute('data-theme', theme);
      try { localStorage.setItem('oce-theme', theme); } catch (e) { /* storage blocked */ }
    }
    syncThemeColor();
    syncThemeToggles();
  }

  themeToggles.forEach(function (btn) {
    btn.hidden = false;
    btn.addEventListener('click', function () {
      setTheme(currentTheme() === 'dark' ? 'light' : 'dark');
    });
  });
  onMediaChange(darkQuery, function () {
    syncThemeToggles();
    syncThemeColor();
  });
  syncThemeToggles();
  syncThemeColor();

  // --- Hamburger Menu ---
  var hamburger = document.querySelector('.hamburger');
  var mobileMenu = document.getElementById('mobile-menu');

  if (hamburger && mobileMenu) {
    // Labels come from data-* because this file is not Liquid-processed and so
    // cannot read the i18n strings directly.
    var labelOpen = hamburger.getAttribute('data-label-open');
    var labelClose = hamburger.getAttribute('data-label-close');

    var setMenu = function (open) {
      hamburger.setAttribute('aria-expanded', String(open));
      mobileMenu.setAttribute('aria-hidden', String(!open));
      hamburger.classList.toggle('is-active', open);
      mobileMenu.classList.toggle('is-open', open);
      document.body.classList.toggle('menu-open', open);
      var label = open ? labelClose : labelOpen;
      if (label) hamburger.setAttribute('aria-label', label);
    };

    hamburger.addEventListener('click', function () {
      setMenu(hamburger.getAttribute('aria-expanded') !== 'true');
    });

    // Close menu when clicking a link
    mobileMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        setMenu(false);
      });
    });

    // Escape closes the menu and gives focus back to the button.
    document.addEventListener('keydown', function (e) {
      if ((e.key === 'Escape' || e.key === 'Esc') && hamburger.getAttribute('aria-expanded') === 'true') {
        setMenu(false);
        hamburger.focus();
      }
    });

    // Widening the window past the burger breakpoint closes the menu.
    var headerQuery = window.matchMedia ? window.matchMedia('(min-width: 1280px)') : null;
    onMediaChange(headerQuery, function (e) {
      if (e.matches) setMenu(false);
    });
  }

  // --- Language switcher (disclosure) ---
  // The list also opens via CSS :hover/:focus-within; this adds real state so a
  // screen reader is told whether the menu is open, and Escape closes it.
  document.querySelectorAll('.lang-switcher').forEach(function (switcher) {
    var trigger = switcher.querySelector('.lang-switcher__trigger');
    if (!trigger) return;

    var setOpen = function (open) {
      trigger.setAttribute('aria-expanded', String(open));
      switcher.classList.toggle('is-open', open);
    };

    trigger.addEventListener('click', function (e) {
      e.stopPropagation();
      setOpen(trigger.getAttribute('aria-expanded') !== 'true');
    });

    switcher.addEventListener('keydown', function (e) {
      if ((e.key === 'Escape' || e.key === 'Esc') && trigger.getAttribute('aria-expanded') === 'true') {
        // Only this list closes, not the mobile menu around it.
        e.stopPropagation();
        setOpen(false);
        trigger.focus();
      }
    });

    document.addEventListener('click', function (e) {
      if (!switcher.contains(e.target)) setOpen(false);
    });
  });

  // Anchor links scroll natively: CSS sets scroll-behavior (only without
  // reduced motion) and scroll-margin-top keeps targets below the header.

  // --- Header border once the page scrolls ---
  var header = document.querySelector('.site-header');
  if (header) {
    var scrolled = false;
    var syncHeader = function () {
      var now = window.scrollY > 10;
      if (now !== scrolled) {
        scrolled = now;
        header.classList.toggle('is-scrolled', now);
      }
    };
    window.addEventListener('scroll', syncHeader, { passive: true });
    syncHeader();
  }

  // --- Article: "On this page" ---
  // _layouts/post.html lists the article's H2s (when there are at least
  // three). Here: open on wide screens, folded on narrow ones, and mark the
  // section being read.
  var toc = document.querySelector('[data-toc]');
  var tocList = toc && toc.querySelector('[data-toc-list]');
  if (toc && tocList) {
    var tocLinks = [];
    var tocHeadings = [];
    Array.prototype.forEach.call(tocList.querySelectorAll('a[href^="#"]'), function (link) {
      var target = document.getElementById(decodeURIComponent(link.hash.slice(1)));
      if (target) {
        tocLinks.push(link);
        tocHeadings.push(target);
      }
    });
    if (tocLinks.length) {
      var tocDetails = toc.querySelector('details');
      var wideQuery = window.matchMedia ? window.matchMedia('(min-width: 1200px)') : null;
      var isWide = function () { return !wideQuery || wideQuery.matches; };
      var syncTocOpen = function () {
        if (tocDetails) tocDetails.open = isWide();
      };
      syncTocOpen();
      onMediaChange(wideQuery, syncTocOpen);

      tocLinks.forEach(function (link) {
        link.addEventListener('click', function () {
          if (!isWide() && tocDetails) tocDetails.open = false;
        });
      });

      // Scroll-spy: the current section is the last heading above the top
      // of the reading area.
      var currentIndex = -2;
      var tocTicking = false;
      var syncCurrent = function () {
        tocTicking = false;
        var line = 140;
        var index = -1;
        for (var i = 0; i < tocHeadings.length; i++) {
          if (tocHeadings[i].getBoundingClientRect().top <= line) index = i;
          else break;
        }
        if (index === currentIndex) return;
        currentIndex = index;
        tocLinks.forEach(function (link, j) {
          if (j === index) link.setAttribute('aria-current', 'true');
          else link.removeAttribute('aria-current');
        });
      };
      window.addEventListener('scroll', function () {
        if (!tocTicking) {
          tocTicking = true;
          window.requestAnimationFrame(syncCurrent);
        }
      }, { passive: true });
      syncCurrent();
    }
  }

  // --- Homepage: the quarter-hour grid ---
  var qhFigure = document.querySelector('[data-qh]');
  if (qhFigure) initQuarterHours(qhFigure);

  function initQuarterHours(fig) {
    var canvas = fig.querySelector('[data-qh-canvas]');
    var dataEl = fig.querySelector('[data-qh-data]');
    var days;
    try { days = JSON.parse(dataEl.textContent); } catch (e) { return; }
    if (!canvas || !days || days.length < 365 || !window.Intl) return;

    var ROWS = 28;
    var DAY = 86400000;
    var locale = fig.getAttribute('data-locale') || 'fr-BE';
    var step = parseInt(fig.getAttribute('data-step'), 10) || 60;
    var levels = (fig.getAttribute('data-levels') || '').split(',').map(Number);
    var members = fig.getAttribute('data-members');

    var fill = function (template, values) {
      return (template || '').replace(/\{(\w+)\}/g, function (match, key) {
        return values[key] !== undefined ? values[key] : match;
      });
    };
    var pad = function (n) { return (n < 10 ? '0' : '') + n; };
    var formatTime = function (q) {
      var h = Math.floor(q / 4);
      return fill(fig.getAttribute('data-time-format'), { h: h, hh: pad(h), m: pad((q % 4) * 15) });
    };
    var formatHour = function (h) {
      return fill(fig.getAttribute('data-hour-format'), { h: h, hh: pad(h) });
    };
    var kwh = new Intl.NumberFormat(locale, { minimumFractionDigits: 1, maximumFractionDigits: 1 });
    var shortDate = new Intl.DateTimeFormat(locale, { day: 'numeric', month: 'short', timeZone: 'UTC' });
    var longDate = new Intl.DateTimeFormat(locale, { weekday: 'short', day: 'numeric', month: 'long', timeZone: 'UTC' });

    // Now, in Brussels: the data is in local quarter-hours.
    var parts = {};
    new Intl.DateTimeFormat('en-GB', {
      timeZone: 'Europe/Brussels', year: 'numeric', month: 'numeric', day: 'numeric',
      hour: 'numeric', minute: 'numeric', hourCycle: 'h23'
    }).formatToParts(new Date()).forEach(function (p) {
      if (p.type !== 'literal') parts[p.type] = parseInt(p.value, 10);
    });
    var today = Date.UTC(parts.year, parts.month - 1, parts.day);
    var nowQ = (parts.hour % 24) * 4 + Math.floor(parts.minute / 15);

    // One string per day of the weather year (365 days): a date reads the same
    // month and day, 29 February reads 28 February.
    var dayIndex = function (utc) {
      var d = new Date(utc);
      var month = d.getUTCMonth();
      var date = d.getUTCDate();
      if (month === 1 && date === 29) date = 28;
      return Math.round((Date.UTC(2023, month, date) - Date.UTC(2023, 0, 1)) / DAY);
    };
    var wattHours = function (utc, q) {
      var s = days[dayIndex(utc)];
      return s ? parseInt(s.charAt(q), 36) * step : 0;
    };
    var levelOf = function (wh) {
      if (wh <= 0) return 0;
      var l = 1;
      for (var i = 0; i < levels.length; i++) if (wh >= levels[i]) l++;
      return l;
    };

    var rowDates = [];
    for (var r = ROWS - 1; r >= 0; r--) rowDates.push(today - r * DAY);

    // Readout for the current quarter-hour.
    var readout = fig.querySelector('[data-qh-readout]');
    if (readout) {
      var nowWh = wattHours(today, nowQ);
      readout.textContent = fill(fig.getAttribute(nowWh > 0 ? 'data-readout-day' : 'data-readout-idle'), {
        time: formatTime(nowQ),
        n: nowQ + 1,
        kwh: kwh.format(nowWh / 1000),
        members: members
      });
    }

    var geometry = null;
    var animate = !reduceMotion;
    var lastWidth = 0;

    function draw() {
      var width = Math.floor(canvas.clientWidth);
      if (!width || width === lastWidth) return;
      lastWidth = width;

      // Phones get 05:00–21:00 so the squares stay visible.
      var narrow = width < 640;
      var q0 = narrow ? 20 : 0;
      var q1 = narrow ? 84 : 96;
      var cols = q1 - q0;
      var labelW = narrow ? 46 : 64;
      var pitch = (width - labelW) / cols;
      var cell = Math.max(2, Math.round(pitch * 0.8 * 10) / 10);
      var gridH = ROWS * pitch;
      var height = Math.ceil(gridH + 24);
      geometry = { labelW: labelW, pitch: pitch, q0: q0, cols: cols };

      // Past days: one path per level (six elements, not 2 688). Today's row:
      // separate squares, so they can fill in up to now.
      var paths = ['', '', '', '', '', ''];
      var todayCells = '';
      var square = function (x, y) {
        return 'M' + x.toFixed(1) + ' ' + y.toFixed(1) + 'h' + cell + 'v' + cell + 'h-' + cell + 'z';
      };
      for (var row = 0; row < ROWS; row++) {
        var y = row * pitch;
        var isToday = row === ROWS - 1;
        for (var q = q0; q < q1; q++) {
          var x = labelW + (q - q0) * pitch;
          if (isToday && q > nowQ) {
            paths[5] += square(x, y);
          } else if (isToday) {
            var delay = animate ? ' style="animation-delay:' + ((q - q0) * 12) + 'ms"' : '';
            todayCells += '<rect class="qh__c' + levelOf(wattHours(rowDates[row], q)) + (animate ? ' qh__fill' : '') +
              '" x="' + x.toFixed(1) + '" y="' + y.toFixed(1) + '" width="' + cell + '" height="' + cell + '"' + delay + '/>';
          } else {
            paths[levelOf(wattHours(rowDates[row], q))] += square(x, y);
          }
        }
      }

      var classes = ['qh__c0', 'qh__c1', 'qh__c2', 'qh__c3', 'qh__c4', 'qh__cf'];
      var svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + width + ' ' + height + '" width="' + width +
        '" height="' + height + '" aria-hidden="true" focusable="false">';
      paths.forEach(function (d, i) {
        if (d) svg += '<path class="' + classes[i] + '" d="' + d + '"/>';
      });
      svg += todayCells;

      if (nowQ >= q0 && nowQ < q1) {
        var nx = labelW + (nowQ - q0) * pitch;
        var ny = (ROWS - 1) * pitch;
        svg += '<rect class="qh__now" x="' + (nx - 1.5).toFixed(1) + '" y="' + (ny - 1.5).toFixed(1) +
          '" width="' + (cell + 3) + '" height="' + (cell + 3) + '" rx="2"/>';
      }

      [0, 7, 14, 21, ROWS - 1].forEach(function (row) {
        svg += '<text class="qh__label" x="' + (labelW - 8) + '" y="' + (row * pitch + cell / 2).toFixed(1) +
          '" text-anchor="end" dominant-baseline="central">' + escapeHtml(shortDate.format(rowDates[row])) + '</text>';
      });

      (narrow ? [6, 12, 18] : [0, 6, 12, 18, 24]).forEach(function (h) {
        var qh = h * 4;
        var anchor = qh === q0 ? 'start' : (qh === q1 ? 'end' : 'middle');
        svg += '<text class="qh__label" x="' + (labelW + (qh - q0) * pitch).toFixed(1) + '" y="' + (gridH + 16).toFixed(1) +
          '" text-anchor="' + anchor + '">' + escapeHtml(formatHour(h)) + '</text>';
      });

      canvas.innerHTML = svg + '</svg>';
      canvas.classList.add('is-drawn');
      animate = false;
    }

    // The same numbers as a table: the accessible view of the grid.
    var tableHead = fig.querySelector('[data-qh-table-head]');
    var tableBody = fig.querySelector('[data-qh-table]');
    var tableWrap = fig.querySelector('[data-qh-table-wrap]');
    if (tableHead && tableBody && tableWrap) {
      tableHead.innerHTML = ['data-col-day', 'data-col-shared', 'data-col-best'].map(function (attr) {
        return '<th scope="col">' + escapeHtml(fig.getAttribute(attr) || '') + '</th>';
      }).join('');
      var rows = '';
      for (var i = ROWS - 1; i >= 0; i--) {
        var last = i === ROWS - 1 ? nowQ : 95;
        var total = 0;
        var best = 0;
        var bestQ = 0;
        for (var q = 0; q <= last; q++) {
          var v = wattHours(rowDates[i], q);
          total += v;
          if (v > best) { best = v; bestQ = q; }
        }
        rows += '<tr><th scope="row">' + escapeHtml(longDate.format(rowDates[i])) + '</th><td>' +
          kwh.format(total / 1000) + ' kWh</td><td>' +
          (best ? escapeHtml(fill(fig.getAttribute('data-best-format'), { kwh: kwh.format(best / 1000), time: formatTime(bestQ) })) : '–') +
          '</td></tr>';
      }
      tableBody.innerHTML = rows;
      tableWrap.hidden = false;
    }

    // Pointer: the value under the cursor.
    var tip = fig.querySelector('[data-qh-tip]');
    if (tip) {
      canvas.addEventListener('pointermove', function (e) {
        if (!geometry) return;
        var box = canvas.getBoundingClientRect();
        var col = Math.floor((e.clientX - box.left - geometry.labelW) / geometry.pitch);
        var row = Math.floor((e.clientY - box.top) / geometry.pitch);
        var q = geometry.q0 + col;
        if (col < 0 || col >= geometry.cols || row < 0 || row >= ROWS || (row === ROWS - 1 && q > nowQ)) {
          tip.hidden = true;
          return;
        }
        tip.textContent = fill(fig.getAttribute('data-tip'), {
          date: shortDate.format(rowDates[row]),
          time: formatTime(q),
          kwh: kwh.format(wattHours(rowDates[row], q) / 1000)
        });
        tip.hidden = false;
        var figBox = fig.getBoundingClientRect();
        var half = tip.offsetWidth / 2;
        var left = box.left - figBox.left + geometry.labelW + (col + 0.5) * geometry.pitch;
        tip.style.left = Math.min(Math.max(left, half), figBox.width - half) + 'px';
        tip.style.top = (box.top - figBox.top + row * geometry.pitch) + 'px';
      });
      canvas.addEventListener('pointerleave', function () {
        tip.hidden = true;
      });
    }

    draw();
    var resizeTimer = null;
    window.addEventListener('resize', function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(draw, 150);
    });
  }

  // --- News listing: legacy ?tag= links + sort ---
  var toolbar = document.querySelector('[data-blog-toolbar]');
  var grid = document.querySelector('[data-blog-grid]');

  // The listing used to filter by ?tag=. Those topics are now pillar pages;
  // send old links (bookmarks, backlinks, search results) to their new home.
  // The map is rendered by _layouts/blog.html from _data/pillars.yml.
  var legacyTag = toolbar ? new URLSearchParams(window.location.search).get('tag') : null;
  if (legacyTag) {
    var targets = {};
    try { targets = JSON.parse(toolbar.getAttribute('data-tag-redirects') || '{}'); } catch (e) { targets = {}; }
    var destination = legacyTag.split(',').map(function (tag) { return targets[tag]; })
      .filter(Boolean)[0];
    if (destination) {
      window.location.replace(destination);
    } else {
      // Announcement/news tags: this listing is already the right page.
      var params = new URLSearchParams(window.location.search);
      params.delete('tag');
      var qs = params.toString();
      window.history.replaceState(null, '', window.location.pathname + (qs ? '?' + qs : '') + window.location.hash);
    }
  }

  if (toolbar && grid && !legacyTag) {
    var sortSelect = toolbar.querySelector('[data-blog-sort]');
    var allCards = Array.prototype.slice.call(grid.querySelectorAll('.post-card'));
    var activeSort = 'newest';

    var sortParam = new URLSearchParams(window.location.search).get('sort');
    if (sortParam === 'newest' || sortParam === 'oldest' || sortParam === 'updated') {
      activeSort = sortParam;
    }

    var writeUrl = function () {
      var params = new URLSearchParams(window.location.search);
      if (activeSort !== 'newest') {
        params.set('sort', activeSort);
      } else {
        params.delete('sort');
      }
      var qs = params.toString();
      var newUrl = window.location.pathname + (qs ? '?' + qs : '') + window.location.hash;
      window.history.replaceState(null, '', newUrl);
    };

    var render = function () {
      var attr = activeSort === 'updated' ? 'data-updated' : 'data-date';
      var asc = activeSort === 'oldest';
      allCards.slice().sort(function (a, b) {
        var av = parseInt(a.getAttribute(attr) || '0', 10);
        var bv = parseInt(b.getAttribute(attr) || '0', 10);
        return asc ? av - bv : bv - av;
      }).forEach(function (card) {
        grid.appendChild(card);
      });
    };

    if (sortSelect) {
      sortSelect.value = activeSort;
      sortSelect.addEventListener('change', function () {
        activeSort = sortSelect.value;
        render();
        writeUrl();
      });
    }

    render();
  }

  // --- Glossary filter (category) + search ---
  var gToolbar = document.querySelector('[data-glossary-toolbar]');
  var gGrid = document.querySelector('[data-glossary-grid]');
  if (gToolbar && gGrid) {
    var gPills = gToolbar.querySelectorAll('.blog-toolbar__pill');
    var gSearch = gToolbar.querySelector('[data-glossary-search]');
    var gEmpty = document.querySelector('[data-glossary-empty]');
    var gCount = document.querySelector('[data-glossary-count]');
    var gCards = Array.prototype.slice.call(gGrid.querySelectorAll('.glossary-card'));

    var gCategory = '';
    var gQuery = '';

    // Lowercase + strip diacritics so "repartition" matches "répartition".
    var gNorm = function (s) {
      return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
    };

    // Alphabetical order (per-language) regardless of authoring order.
    gCards.sort(function (a, b) {
      return (a.getAttribute('data-term') || '').localeCompare(b.getAttribute('data-term') || '');
    });
    gCards.forEach(function (card) { gGrid.appendChild(card); });

    var gReadUrl = function () {
      var params = new URLSearchParams(window.location.search);
      var cat = params.get('cat');
      if (cat) gCategory = cat;
      var q = params.get('q');
      if (q) gQuery = q;
    };

    var gWriteUrl = function () {
      var params = new URLSearchParams(window.location.search);
      if (gCategory) { params.set('cat', gCategory); } else { params.delete('cat'); }
      if (gQuery) { params.set('q', gQuery); } else { params.delete('q'); }
      var qs = params.toString();
      var newUrl = window.location.pathname + (qs ? '?' + qs : '') + window.location.hash;
      window.history.replaceState(null, '', newUrl);
    };

    var gSync = function () {
      gPills.forEach(function (btn) {
        var slug = btn.getAttribute('data-category');
        var isActive = slug === '' ? gCategory === '' : gCategory === slug;
        btn.classList.toggle('blog-toolbar__pill--active', isActive);
        btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      });
      if (gSearch) gSearch.value = gQuery;
    };

    var gRender = function () {
      var nq = gNorm(gQuery.trim());
      var visible = 0;
      gCards.forEach(function (card) {
        var catOk = gCategory === '' || card.getAttribute('data-category') === gCategory;
        var searchOk = nq === '' || gNorm(card.getAttribute('data-search')).indexOf(nq) !== -1;
        var match = catOk && searchOk;
        card.hidden = !match;
        if (match) visible++;
      });
      if (gEmpty) gEmpty.hidden = visible > 0;
      if (gCount) {
        var label = gCount.getAttribute('data-count-label') || '';
        gCount.textContent = visible + (label ? ' ' + label : '');
      }
    };

    gPills.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var slug = btn.getAttribute('data-category');
        if (slug === '' || gCategory === slug) {
          gCategory = '';
        } else {
          gCategory = slug;
        }
        gSync();
        gRender();
        gWriteUrl();
      });
    });

    if (gSearch) {
      gSearch.addEventListener('input', function () {
        gQuery = gSearch.value;
        gRender();
        gWriteUrl();
      });
    }

    gReadUrl();
    gSync();
    gRender();
  }

  // --- Newsletter AJAX (Mailchimp JSONP, no backend) ---
  var newsletterForms = document.querySelectorAll('[data-newsletter-form]');
  if (newsletterForms.length) {
    var nlCallbackCount = 0;

    newsletterForms.forEach(function (form) {
      var status = form.parentNode.querySelector('[data-newsletter-status]');
      var emailInput = form.querySelector('input[type="email"]');

      var showStatus = function (message, isSuccess) {
        if (!status) return;
        status.textContent = message;
        status.classList.remove('is-success', 'is-error');
        status.classList.add(isSuccess ? 'is-success' : 'is-error');
        status.hidden = false;
      };

      form.addEventListener('submit', function (e) {
        // Let the browser's native validation handle empty/invalid emails.
        if (typeof form.reportValidity === 'function' && !form.reportValidity()) {
          return;
        }
        e.preventDefault();

        // Build the JSONP URL: Mailchimp's classic endpoint has no CORS, so we
        // swap /post? for /post-json? and hand it a callback name via &c=.
        var callbackName = 'mcCallback_' + (nlCallbackCount++);
        var action = form.getAttribute('action').replace('/post?', '/post-json?');
        var params = [];
        Array.prototype.forEach.call(form.querySelectorAll('input[name]'), function (input) {
          params.push(encodeURIComponent(input.name) + '=' + encodeURIComponent(input.value));
        });
        params.push('c=' + callbackName);
        var url = action + '&' + params.join('&');

        var script = document.createElement('script');
        var msgSuccess = form.getAttribute('data-msg-success');
        var msgError = form.getAttribute('data-msg-error');

        var cleanup = function () {
          delete window[callbackName];
          if (script.parentNode) script.parentNode.removeChild(script);
          form.classList.remove('is-loading');
        };

        window[callbackName] = function (response) {
          cleanup();
          if (response && response.result === 'success') {
            showStatus(msgSuccess, true);
            if (emailInput) emailInput.value = '';
          } else {
            // Mailchimp's raw msg (e.g. "already subscribed") can be actionable.
            var detail = response && response.msg ? response.msg.replace(/^\d+\s*-\s*/, '') : '';
            showStatus(detail ? msgError + ' (' + detail + ')' : msgError, false);
          }
        };

        // If the JSONP request never resolves (blocked/offline), surface the error.
        script.onerror = function () {
          cleanup();
          showStatus(msgError, false);
        };

        form.classList.add('is-loading');
        script.src = url;
        document.body.appendChild(script);
      });
    });
  }
})();
