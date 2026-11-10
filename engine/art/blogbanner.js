// Blog banners: a photo with the headline written on it (yellow), a white subtitle and the Chimera mark.
// Usage: node blogbanner.js jobs.json outDir
// jobs: [{slug, photo (absolute path), headline, sub}]
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

const page = (job, img) => `<!doctype html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
body{width:1600px;height:760px;overflow:hidden;position:relative;font-family:Inter,system-ui,sans-serif;background:#0D0D12}
.bg{position:absolute;inset:0;background:url(${img}) center/cover no-repeat}
.shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,8,12,.86) 0%,rgba(8,8,12,.62) 34%,rgba(8,8,12,.08) 62%,transparent 75%)}
.copy{position:absolute;left:90px;top:50%;transform:translateY(-50%);width:760px}
.brand{font-weight:800;letter-spacing:.06em;color:#FFC727;font-size:30px;margin-bottom:34px}
h1{color:#FFC727;font-weight:800;font-size:${job.headline.length > 34 ? 64 : 80}px;line-height:1.04;letter-spacing:-.02em;text-shadow:0 2px 18px rgba(0,0,0,.35)}
.sub{color:#fff;font-size:32px;font-weight:500;line-height:1.3;margin-top:22px;text-shadow:0 2px 12px rgba(0,0,0,.4)}
.loc{position:absolute;left:90px;bottom:54px;color:rgba(255,255,255,.82);font-size:20px;letter-spacing:.04em}
.loc b{color:#fff;font-weight:600}
</style></head><body><div class="bg"></div><div class="shade"></div>
<div class="copy"><div class="brand">CHIMERA</div><h1>${esc(job.headline)}</h1><div class="sub">${esc(job.sub)}</div></div>
<div class="loc"><b>thechimeraai.com</b> · Anaheim, Orange County, CA</div></body></html>`;

(async () => {
  const [jobsFile, outDir] = process.argv.slice(2);
  const jobs = JSON.parse(fs.readFileSync(jobsFile, 'utf8'));
  const browser = await chromium.launch();
  const p = await browser.newPage({ viewport: { width: 1600, height: 760 } });
  for (const job of jobs) {
    const img = 'data:image/jpeg;base64,' + fs.readFileSync(job.photo).toString('base64');
    await p.setContent(page(job, img), { waitUntil: 'load' });
    await p.screenshot({ path: path.join(outDir, `${job.slug}.png`) });
    console.log('rendered', job.slug);
  }
  await browser.close();
})();
