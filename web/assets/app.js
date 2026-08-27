(function () {
  var btn = document.getElementById('themeBtn');
  var root = document.documentElement;
  var saved = null;
  try { saved = localStorage.getItem('spata5-theme'); } catch (e) {}
  var dark = saved ? saved === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
  apply();
  btn.addEventListener('click', function () {
    dark = !dark;
    apply();
    try { localStorage.setItem('spata5-theme', dark ? 'dark' : 'light'); } catch (e) {}
  });
  function apply() {
    if (dark) { root.setAttribute('data-theme', 'dark'); } else { root.removeAttribute('data-theme'); }
    btn.setAttribute('aria-checked', dark ? 'true' : 'false');
    btn.setAttribute('aria-label', dark ? 'Světlý režim' : 'Tmavý režim');
  }
})();
(function () {
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.term-info');
    if (btn) {
      var dlg = document.getElementById(btn.getAttribute('aria-controls'));
      if (dlg) dlg.showModal();
      return;
    }
    var close = e.target.closest('.term-close');
    if (close) {
      close.closest('dialog').close();
      return;
    }
    var open = e.target.closest('dialog.term-dialog[open]');
    if (open) {
      var r = open.getBoundingClientRect();
      var outside = e.clientX < r.left || e.clientX > r.right ||
        e.clientY < r.top || e.clientY > r.bottom;
      if (outside) open.close();
    }
  });
})();
(function () {
  var dataEl = document.getElementById('glossData');
  if (!dataEl) return;
  var terms = JSON.parse(dataEl.textContent);
  var listEl = document.getElementById('glossTerms');
  var detailEl = document.getElementById('glossDetail');
  var q = document.getElementById('glossQ');
  var current = terms[0].t;
  function norm(s) {
    return s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  }
  function esc(s) {
    return s.replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }
  function renderList() {
    var needle = norm(q.value.trim());
    var hits = terms.filter(function (x) {
      return !needle || norm(x.t).indexOf(needle) >= 0 || norm(x.plain).indexOf(needle) >= 0;
    });
    if (!hits.length) {
      listEl.innerHTML = '<div class="dict-empty">Žádný pojem neodpovídá hledání.</div>';
      return;
    }
    var html = '', lastLetter = '';
    hits.forEach(function (x) {
      var L = norm(x.t)[0].toUpperCase();
      if (L !== lastLetter) {
        html += '<div class="dict-letter">' + L + '</div>';
        lastLetter = L;
      }
      html += '<button type="button" data-t="' + esc(x.t) + '" aria-current="' +
        (x.t === current) + '">' + esc(x.t) + '</button>';
    });
    listEl.innerHTML = html;
  }
  function renderDetail() {
    var x = terms.filter(function (y) { return y.t === current; })[0];
    detailEl.innerHTML = '<div class="dict-group">' + esc(x.group) + '</div>' +
      '<h2>' + esc(x.t) + '</h2>' +
      '<p class="dict-def">' + x.def + '</p>' +
      '<h3>Kde na webu se pojem používá</h3>' +
      '<ul class="dict-uses">' + x.uses.map(function (u) {
        return '<li><a href="' + esc(u[1]) + '">' + esc(u[0]) + '</a></li>';
      }).join('') +
      '</ul>' +
      (x.rel.length ? '<h3>Související pojmy</h3><div class="dict-rel">' +
        x.rel.map(function (r) {
          return '<button type="button" data-t="' + esc(r) + '">' + esc(r) + '</button>';
        }).join('') + '</div>' : '');
  }
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.dict button[data-t]');
    if (!btn) return;
    current = btn.dataset.t;
    renderList();
    renderDetail();
  });
  q.addEventListener('input', renderList);
  renderList();
  renderDetail();
})();
