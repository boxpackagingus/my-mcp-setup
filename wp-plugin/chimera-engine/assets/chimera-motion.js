/* Chimera pages: scroll reveals, growing bars, count-up figures and interactive line charts.
   Content is fully visible without this script; it only adds motion and interaction. */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var root = document.documentElement;
  root.classList.add('cp-js');

  function ready(fn) { document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', fn) : fn(); }

  /* ---------- count-up for stat figures like "800M", "2B", "650M" ---------- */
  function countUp(el) {
    var text = el.textContent.trim();
    var m = text.match(/^([^0-9]*)([0-9]+(?:\.[0-9]+)?)(.*)$/);
    if (!m || reduce) return;
    var target = parseFloat(m[2]), decimals = (m[2].split('.')[1] || '').length, start = null, dur = 1100;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min(1, (ts - start) / dur), e = 1 - Math.pow(1 - p, 3);
      el.textContent = m[1] + (target * e).toFixed(decimals) + m[3];
      if (p < 1) requestAnimationFrame(step); else el.textContent = text;
    }
    requestAnimationFrame(step);
  }

  /* ---------- line chart ---------- */
  var NS = 'http://www.w3.org/2000/svg';
  function svg(tag, attrs) { var n = document.createElementNS(NS, tag); for (var k in attrs) n.setAttribute(k, attrs[k]); return n; }
  function fmt(v, unit) { return (Math.round(v * 10) / 10).toString().replace(/\.0$/, '') + (unit || ''); }

  function drawLine(box) {
    var pts; try { pts = JSON.parse(box.getAttribute('data-points')); } catch (e) { return; }
    if (!pts || pts.length < 2) return;
    var unit = box.getAttribute('data-unit') || '';
    var W = Math.max(320, box.clientWidth), H = Math.round(Math.min(340, Math.max(220, W * 0.42)));
    var m = { t: 26, r: 24, b: 40, l: 54 };
    var max = Math.max.apply(null, pts.map(function (p) { return p.v; }));
    var top = niceMax(max), ticks = 4;
    var x = function (i) { return m.l + i * (W - m.l - m.r) / (pts.length - 1); };
    var y = function (v) { return H - m.b - v / top * (H - m.t - m.b); };
    box.innerHTML = '';
    var s = svg('svg', { viewBox: '0 0 ' + W + ' ' + H, width: '100%', 'aria-hidden': 'true' });
    var id = 'g' + Math.random().toString(36).slice(2, 8);
    var defs = svg('defs', {});
    var grad = svg('linearGradient', { id: id, x1: 0, x2: 0, y1: 0, y2: 1 });
    [['0', '.38'], ['1', '0']].forEach(function (st) { grad.appendChild(svg('stop', { offset: st[0], 'stop-color': '#8b5cf6', 'stop-opacity': st[1] })); });
    var lg = svg('linearGradient', { id: id + 'l', x1: 0, x2: 1, y1: 0, y2: 0 });
    [['0', '#5b6cff'], ['.6', '#c95cff'], ['1', '#f7c443']].forEach(function (st) { lg.appendChild(svg('stop', { offset: st[0], 'stop-color': st[1] })); });
    defs.appendChild(grad); defs.appendChild(lg); s.appendChild(defs);
    for (var k = 0; k <= ticks; k++) {
      var tv = top * k / ticks, ty = y(tv);
      s.appendChild(svg('line', { x1: m.l, x2: W - m.r, y1: ty, y2: ty, class: 'cp-ln-grid' }));
      var tl = svg('text', { x: m.l - 10, y: ty + 4, 'text-anchor': 'end', class: 'cp-ln-tick' }); tl.textContent = fmt(tv, unit); s.appendChild(tl);
    }
    pts.forEach(function (p, i) {
      var xl = svg('text', { x: x(i), y: H - 12, 'text-anchor': i === 0 ? 'start' : (i === pts.length - 1 ? 'end' : 'middle'), class: 'cp-ln-tick' });
      xl.textContent = p.l; s.appendChild(xl);
    });
    var d = pts.map(function (p, i) { return (i ? 'L' : 'M') + x(i) + ' ' + y(p.v); }).join(' ');
    var area = svg('path', { d: d + ' L' + x(pts.length - 1) + ' ' + y(0) + ' L' + x(0) + ' ' + y(0) + ' Z', fill: 'url(#' + id + ')', class: 'cp-ln-area' });
    var path = svg('path', { d: d, fill: 'none', stroke: 'url(#' + id + 'l)', 'stroke-width': 3.5, 'stroke-linecap': 'round', 'stroke-linejoin': 'round', class: 'cp-ln-path' });
    s.appendChild(area); s.appendChild(path);
    var tip = document.createElement('div'); tip.className = 'cp-ln-tip'; tip.hidden = true;
    pts.forEach(function (p, i) {
      var g = svg('g', { class: 'cp-ln-pt', tabindex: '0' });
      g.appendChild(svg('circle', { cx: x(i), cy: y(p.v), r: 14, fill: 'transparent' }));
      g.appendChild(svg('circle', { cx: x(i), cy: y(p.v), r: 6, class: 'cp-ln-dot' }));
      var vl = svg('text', { x: x(i), y: y(p.v) - 14, 'text-anchor': 'middle', class: 'cp-ln-val' }); vl.textContent = fmt(p.v, unit); g.appendChild(vl);
      function show() { tip.hidden = false; tip.innerHTML = '<span>' + p.l + '</span><b>' + fmt(p.v, unit) + '</b>';
        tip.style.left = Math.min(Math.max(0, x(i) / W * box.clientWidth - 50), box.clientWidth - 110) + 'px'; tip.style.top = (y(p.v) / H * box.clientHeight - 64) + 'px'; }
      g.addEventListener('mouseenter', show); g.addEventListener('focus', show);
      g.addEventListener('mouseleave', function () { tip.hidden = true; }); g.addEventListener('blur', function () { tip.hidden = true; });
      s.appendChild(g);
    });
    box.appendChild(s); box.appendChild(tip);
    if (!reduce && !box.dataset.played) {
      var len = path.getTotalLength();
      path.style.strokeDasharray = len; path.style.strokeDashoffset = len;
      area.style.opacity = 0;
      requestAnimationFrame(function () { box.classList.add('is-drawing'); path.style.strokeDashoffset = 0; area.style.opacity = 1; });
      box.dataset.played = '1';
    }
  }
  function niceMax(v) { var p = Math.pow(10, Math.floor(Math.log10(v))); var n = v / p; return (n <= 1 ? 1 : n <= 2 ? 2 : n <= 2.5 ? 2.5 : n <= 5 ? 5 : 10) * p; }

  ready(function () {
    var lines = [].slice.call(document.querySelectorAll('.cp-line'));
    var targets = [].slice.call(document.querySelectorAll('.cp > section, .cp > figure, .cp > nav'));
    if (!('IntersectionObserver' in window) || reduce) {
      targets.forEach(function (el) { el.classList.add('is-in'); });
      lines.forEach(drawLine);
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target; io.unobserve(el); el.classList.add('is-in');
        el.querySelectorAll('.cp-stat-value, .cp-glance dd').forEach(countUp);
        el.querySelectorAll('.cp-line').forEach(drawLine);
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
    targets.forEach(function (el) { io.observe(el); });
    var t; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(function () {
      lines.forEach(function (b) { if (b.dataset.played) drawLine(b); }); }, 200); });
  });
})();
