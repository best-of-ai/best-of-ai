// Language select (partials/lang-switcher.html): saves the choice, then opens the same page in the other language.
(function () {
  var T = window.BAI_I18N || {};
  var langs = T.langs || [];

  function prefixOf(code) {
    for (var i = 0; i < langs.length; i++) if (langs[i].lang === code) return langs[i].prefix;
    return '';
  }

  document.querySelectorAll('[data-lang-switch]').forEach(function (sel) {
    sel.addEventListener('change', function () {
      var next = sel.value;
      if (!next || next === T.lang) return;
      try { localStorage.setItem('bai-lang', next); } catch (e) {}

      var path = location.pathname;
      var cur = prefixOf(T.lang);
      if (cur && (path === cur || path.indexOf(cur + '/') === 0)) path = path.slice(cur.length) || '/';
      location.assign(prefixOf(next) + path + location.search + location.hash);
    });
  });
})();
