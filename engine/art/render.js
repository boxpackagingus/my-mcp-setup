// Renders hero images for engine pages. Usage: node render.js jobs.json outDir iconsDir
// jobs.json: [{slug, title, eyebrow, query, engines: ["chatgpt", ...], hue}]
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const NAMES = { chatgpt: 'ChatGPT', claude: 'Claude', perplexity: 'Perplexity', gemini: 'Gemini', google: 'AI Overviews',
  meta: 'Meta AI', grok: 'Grok', mistral: 'Le Chat', copilot: 'Copilot', deepseek: 'DeepSeek' };
const LETTERS = { copilot: 'Co', deepseek: 'DS' };
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

function page(job, iconsDir) {
  const hue = job.hue || 230;
  const tiles = job.engines.slice(0, 6).map((e, i) => {
    const icon = LETTERS[e]
      ? `<span class="mono">${LETTERS[e]}</span>`
      : `<img src="data:image/svg+xml;base64,${fs.readFileSync(path.join(iconsDir, e + '.svg')).toString('base64')}" alt="">`;
    return `<div class="tile t${i}">${icon}<b>${esc(NAMES[e] || e)}</b></div>`;
  }).join('');
  return `<!doctype html><html><head><meta charset="utf-8"><style>
  *{box-sizing:border-box;margin:0}
  body{width:1600px;height:840px;overflow:hidden;font-family:Inter,"Segoe UI",system-ui,sans-serif;background:#0b0c11;color:#f4f2ec;position:relative}
  .glow{position:absolute;inset:0;background:
    radial-gradient(55% 80% at 82% 18%, hsla(${hue},95%,62%,.55), transparent 60%),
    radial-gradient(45% 70% at 6% 100%, rgba(247,196,67,.42), transparent 60%),
    radial-gradient(40% 60% at 60% 95%, hsla(${(hue + 60) % 360},85%,62%,.38), transparent 60%)}
  .grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:56px 56px;mask-image:radial-gradient(70% 80% at 70% 40%,#000,transparent)}
  .left{position:absolute;left:88px;top:84px;width:780px}
  .brand{font-weight:800;letter-spacing:.12em;color:#f7c443;font-size:30px}
  .eyebrow{margin-top:56px;display:inline-flex;align-items:center;gap:12px;font-size:20px;letter-spacing:.16em;text-transform:uppercase;color:#a9abb7;font-weight:600}
  .eyebrow:before{content:"";width:11px;height:11px;border-radius:50%;background:#f7c443}
  h1{margin-top:22px;font-size:${job.title.length > 60 ? 54 : 64}px;line-height:1.07;letter-spacing:-.025em;font-weight:700}
  .site{position:absolute;left:88px;bottom:70px;font-size:22px;color:#a9abb7;display:flex;gap:14px;align-items:center}
  .site b{color:#f4f2ec;font-weight:600}
  .chat{position:absolute;right:96px;top:120px;width:560px;background:rgba(20,22,30,.78);border:1px solid rgba(255,255,255,.12);border-radius:28px;padding:30px;backdrop-filter:blur(8px);box-shadow:0 40px 80px rgba(0,0,0,.45)}
  .q{display:flex;gap:14px;align-items:center;background:#fff;color:#16171c;border-radius:18px;padding:18px 20px;font-size:23px;font-weight:600}
  .q:before{content:"";width:22px;height:22px;flex:none;border-radius:50%;border:3px solid #16171c;box-shadow:12px 12px 0 -8px #16171c}
  .lines{margin-top:24px;display:grid;gap:12px}
  .lines i{display:block;height:14px;border-radius:8px;background:linear-gradient(90deg,rgba(255,255,255,.28),rgba(255,255,255,.08))}
  .lines i:nth-child(2){width:88%}.lines i:nth-child(3){width:72%}
  .tiles{margin-top:28px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
  .tile{display:flex;align-items:center;gap:12px;background:#fff;color:#16171c;border-radius:16px;padding:12px 14px;font-size:18px}
  .tile img{width:34px;height:34px}
  .tile .mono{width:34px;height:34px;border-radius:10px;display:grid;place-items:center;font-weight:800;font-size:15px;color:#fff;background:linear-gradient(135deg,#2563eb,#7c3aed)}
  </style></head><body><div class="glow"></div><div class="grid"></div>
  <div class="left"><div class="brand">CHIMERA</div><div class="eyebrow">${esc(job.eyebrow)}</div><h1>${esc(job.title)}</h1></div>
  <div class="site"><b>thechimeraai.com</b> · Generative Engine Optimization · Anaheim, Orange County, CA</div>
  <div class="chat"><div class="q">${esc(job.query)}</div><div class="lines"><i></i><i></i><i></i></div><div class="tiles">${tiles}</div></div>
  </body></html>`;
}

(async () => {
  const [jobsFile, outDir, iconsDir] = process.argv.slice(2);
  const jobs = JSON.parse(fs.readFileSync(jobsFile, 'utf8'));
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const p = await browser.newPage({ viewport: { width: 1600, height: 840 }, deviceScaleFactor: 1 });
  for (const job of jobs) {
    await p.setContent(page(job, iconsDir), { waitUntil: 'load' });
    await p.screenshot({ path: path.join(outDir, job.slug + '.png'), type: 'png' });
    console.log('rendered', job.slug);
  }
  await browser.close();
})();
