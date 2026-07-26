(function () {
  'use strict';

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
      if (e.key === 'Escape' || e.key === 'Esc') {
        setOpen(false);
        trigger.focus();
      }
    });

    document.addEventListener('click', function (e) {
      if (!switcher.contains(e.target)) setOpen(false);
    });
  });

  // --- Smooth Scroll for anchor links ---
  document.querySelectorAll('a[href*="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var href = this.getAttribute('href');
      // Only handle links with a hash fragment
      var hashIndex = href.indexOf('#');
      if (hashIndex === -1) return;
      var hash = href.substring(hashIndex);
      if (hash === '#') return;

      var target = document.querySelector(hash);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        history.pushState(null, '', hash);
      }
    });
  });

  // --- Header scroll shadow ---
  var header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 10) {
        header.classList.add('is-scrolled');
      } else {
        header.classList.remove('is-scrolled');
      }
    }, { passive: true });
  }

  // --- Blog filter + sort ---
  var toolbar = document.querySelector('[data-blog-toolbar]');
  var grid = document.querySelector('[data-blog-grid]');
  var empty = document.querySelector('[data-blog-empty]');
  if (toolbar && grid) {
    var pillButtons = toolbar.querySelectorAll('.blog-toolbar__pill');
    var sortSelect = toolbar.querySelector('[data-blog-sort]');
    var allCards = Array.prototype.slice.call(grid.querySelectorAll('.post-card'));

    var activeTags = new Set();
    var activeSort = 'newest';

    function readUrl() {
      var params = new URLSearchParams(window.location.search);
      var tagParam = params.get('tag');
      if (tagParam) {
        tagParam.split(',').forEach(function (t) {
          if (t) activeTags.add(t);
        });
      }
      var sortParam = params.get('sort');
      if (sortParam === 'newest' || sortParam === 'oldest' || sortParam === 'updated') {
        activeSort = sortParam;
      }
    }

    function writeUrl() {
      var params = new URLSearchParams(window.location.search);
      if (activeTags.size > 0) {
        params.set('tag', Array.from(activeTags).join(','));
      } else {
        params.delete('tag');
      }
      if (activeSort !== 'newest') {
        params.set('sort', activeSort);
      } else {
        params.delete('sort');
      }
      var qs = params.toString();
      var newUrl = window.location.pathname + (qs ? '?' + qs : '') + window.location.hash;
      window.history.replaceState(null, '', newUrl);
    }

    function syncControls() {
      pillButtons.forEach(function (btn) {
        var slug = btn.getAttribute('data-tag');
        var isActive = slug === '' ? activeTags.size === 0 : activeTags.has(slug);
        btn.classList.toggle('blog-toolbar__pill--active', isActive);
        btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      });
      if (sortSelect) sortSelect.value = activeSort;
    }

    function cardMatches(card) {
      if (activeTags.size === 0) return true;
      var cardTags = (card.getAttribute('data-tags') || '').split(',').filter(Boolean);
      var cardSet = new Set(cardTags);
      var values = Array.from(activeTags);
      for (var i = 0; i < values.length; i++) {
        if (!cardSet.has(values[i])) return false;
      }
      return true;
    }

    function render() {
      var attr = activeSort === 'updated' ? 'data-updated'
        : activeSort === 'oldest' ? 'data-date'
        : 'data-date';
      var asc = activeSort === 'oldest';
      var sorted = allCards.slice().sort(function (a, b) {
        var av = parseInt(a.getAttribute(attr) || '0', 10);
        var bv = parseInt(b.getAttribute(attr) || '0', 10);
        return asc ? av - bv : bv - av;
      });
      var visibleCount = 0;
      sorted.forEach(function (card) {
        var match = cardMatches(card);
        card.hidden = !match;
        grid.appendChild(card);
        if (match) visibleCount++;
      });
      if (empty) empty.hidden = visibleCount > 0;
    }

    pillButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var slug = btn.getAttribute('data-tag');
        if (slug === '') {
          activeTags.clear();
        } else if (activeTags.has(slug)) {
          activeTags.delete(slug);
        } else {
          activeTags.add(slug);
        }
        syncControls();
        render();
        writeUrl();
      });
    });

    if (sortSelect) {
      sortSelect.addEventListener('change', function () {
        activeSort = sortSelect.value;
        render();
        writeUrl();
      });
    }

    readUrl();
    syncControls();
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
    function gNorm(s) {
      return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
    }

    // Alphabetical order (per-language) regardless of authoring order.
    gCards.sort(function (a, b) {
      return (a.getAttribute('data-term') || '').localeCompare(b.getAttribute('data-term') || '');
    });
    gCards.forEach(function (card) { gGrid.appendChild(card); });

    function gReadUrl() {
      var params = new URLSearchParams(window.location.search);
      var cat = params.get('cat');
      if (cat) gCategory = cat;
      var q = params.get('q');
      if (q) gQuery = q;
    }

    function gWriteUrl() {
      var params = new URLSearchParams(window.location.search);
      if (gCategory) { params.set('cat', gCategory); } else { params.delete('cat'); }
      if (gQuery) { params.set('q', gQuery); } else { params.delete('q'); }
      var qs = params.toString();
      var newUrl = window.location.pathname + (qs ? '?' + qs : '') + window.location.hash;
      window.history.replaceState(null, '', newUrl);
    }

    function gSync() {
      gPills.forEach(function (btn) {
        var slug = btn.getAttribute('data-category');
        var isActive = slug === '' ? gCategory === '' : gCategory === slug;
        btn.classList.toggle('blog-toolbar__pill--active', isActive);
        btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      });
      if (gSearch) gSearch.value = gQuery;
    }

    function gRender() {
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
    }

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

      function showStatus(message, isSuccess) {
        if (!status) return;
        status.textContent = message;
        status.classList.remove('is-success', 'is-error');
        status.classList.add(isSuccess ? 'is-success' : 'is-error');
        status.hidden = false;
      }

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

        function cleanup() {
          delete window[callbackName];
          if (script.parentNode) script.parentNode.removeChild(script);
          form.classList.remove('is-loading');
        }

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
