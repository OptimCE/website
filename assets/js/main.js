(function () {
  'use strict';

  // --- Hamburger Menu ---
  var hamburger = document.querySelector('.hamburger');
  var mobileMenu = document.getElementById('mobile-menu');

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', function () {
      var isOpen = hamburger.getAttribute('aria-expanded') === 'true';
      hamburger.setAttribute('aria-expanded', String(!isOpen));
      mobileMenu.setAttribute('aria-hidden', String(isOpen));
      hamburger.classList.toggle('is-active');
      mobileMenu.classList.toggle('is-open');
      document.body.classList.toggle('menu-open');
    });

    // Close menu when clicking a link
    mobileMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        hamburger.setAttribute('aria-expanded', 'false');
        mobileMenu.setAttribute('aria-hidden', 'true');
        hamburger.classList.remove('is-active');
        mobileMenu.classList.remove('is-open');
        document.body.classList.remove('menu-open');
      });
    });
  }

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
})();
