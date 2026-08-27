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
