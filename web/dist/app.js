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
