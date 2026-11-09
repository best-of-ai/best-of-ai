(function () {
  'use strict';
  var KEY = 'bai_saved';

  function get() {
    try { return JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { return {}; }
  }
  function set(data) {
    try { localStorage.setItem(KEY, JSON.stringify(data)); } catch (e) {}
  }

  window.baiSaved = {
    get:    get,
    has:    function (slug) { return !!get()[slug]; },
    save:   function (slug, info) { var d = get(); d[slug] = info; set(d); },
    remove: function (slug) { var d = get(); delete d[slug]; set(d); },
    count:  function () { return Object.keys(get()).length; },
    toggle: function (slug, info) {
      if (this.has(slug)) { this.remove(slug); return false; }
      this.save(slug, info); return true;
    }
  };

  function applyState(btn, saved) {
    btn.classList.toggle('is-saved', saved);
    btn.setAttribute('aria-pressed', String(saved));
    var T = window.BAI_I18N || {};
    btn.title = saved ? (T.removeFromSaved || 'Remove from saved') : (T.saveTool || 'Save tool');
    var label = btn.querySelector('.save-label');
    if (label) label.textContent = saved ? (T.saved || 'Saved') : (T.save || 'Save');
  }

  function updateCount() {
    var n = window.baiSaved.count();
    document.querySelectorAll('.saved-count').forEach(function (el) {
      el.textContent = n > 0 ? String(n) : '';
      el.hidden = n === 0;
    });
  }

  function updateAll() {
    document.querySelectorAll('.js-save-btn').forEach(function (btn) {
      applyState(btn, window.baiSaved.has(btn.dataset.slug));
    });
    updateCount();
  }

  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.js-save-btn');
    if (!btn) return;
    e.preventDefault();
    e.stopPropagation();

    var slug = btn.dataset.slug;
    if (!slug) return;

    var info;
    try { info = JSON.parse(btn.dataset.info); } catch (_) { info = { slug: slug }; }

    var nowSaved = window.baiSaved.toggle(slug, info);
    applyState(btn, nowSaved);
    updateCount();

    // On /saved page: remove the card when unsaved
    if (!nowSaved && window.location.pathname.replace(/^\/(?!saved)[a-z]{2}(?=\/)/, '').replace(/\/$/, '') === '/saved') {
      var card = btn.closest('.tool-card');
      if (card) {
        card.remove();
        var grid  = document.getElementById('saved-grid');
        var empty = document.getElementById('saved-empty');
        if (grid && empty) empty.hidden = grid.children.length > 0;
      }
    }
  });

  document.addEventListener('DOMContentLoaded', updateAll);
  window.baiUpdateSaveButtons = updateAll;
})();
