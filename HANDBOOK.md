# Chimera Engine: Complete Handbook

Everything needed to run, rebuild or hand over the engine that grows **thechimeraai.com**: what it is, how it is set
up, what runs every day, the rules it follows, and where every file lives. A new Claude Code chat should read this
file first (see `prompts/new-chat.md`).

Last updated: 2026-11-16.

---

## 1. What the engine is

Chimera is a Generative Engine Optimization (GEO) and SEO agency in **Anaheim, California**, serving **Orange County,
California**. The engine is a Python package (`engine/`) plus build scripts (`content/build/`) that, every day:

1. **Measures:** Search Console and GA4 numbers via Site Kit, indexing, site files, money-query positions.
2. **Finds opportunities:** buyer-intent searches, pages competing with each other, CTR gaps, competitor topic gaps,
   what AI assistants recommend, local link opportunities.
3. **Publishes:** fixes to existing pages, new local buyer-intent pages and 5 blog posts to WordPress, with schema,
   Markdown copies, llms.txt, rendered banners and internal links.
4. **Pushes for indexing** (IndexNow and sitemap) and checks every page is live.
5. **Does outreach:** up to 3 free pitches a day to published submission addresses.
6. **Reports:** refreshes the dashboard artifact and writes `data/last-run.md`.

| Thing | Where |
|---|---|
| Website | https://thechimeraai.com (WordPress + Elementor on Hostinger) |
| Main repo | https://github.com/boxpackagingus/my-mcp-setup (remote `origin`, branch `main`) |
| Mirror repo | https://github.com/boxpackagingus/Main-Build-Up (remote `buildup`, same `main`) |
| Dashboard | https://claude.ai/artifact/Dd9pgZazE6LyFGzXSp8seV (Dashboard artifact type) |
| Daily schedule | 4:42 AM Pacific, scheduled task "Chimera daily run" (`prompts/scheduled-task.md`) |
| Daily instructions | `prompts/daily-run.md` (the run follows this file step by step) |

---

## 2. Quick start in a new session

```bash
cd /home/user/my-mcp-setup        # or wherever the repo is cloned
git pull
bash scripts/setup.sh             # installs, connects and checks; never publishes or sends
```

Every line should say `[ok]`. Fix each `[todo]` with section 3, then tell Claude: **"Follow HANDBOOK.md and
prompts/daily-run.md."** To start the automation again, recreate the scheduled task from
`prompts/scheduled-task.md`.

---

## 3. Setup, piece by piece

### 3.1 Cloud environment (Claude Code on the web)

Environment: **Default** (personal). Settings live in the environment menu in the session title bar, then Edit.

**Environment variables** (names only; values are in the environment, never in the repo or chat):

| Variable | Needed for | Notes |
|---|---|---|
| `WP_URL` | publishing | `https://thechimeraai.com` |
| `WP_USER` | publishing | WordPress user with Editor role |
| `WP_APP_PASSWORD` | publishing | Application Password (Users > Profile) |
| `CHIMERA_CONTACT_NAME` / `_PHONE` / `_EMAIL` | outreach sign-off | Never write the values into the repo |
| `GSC_SERVICE_ACCOUNT_KEY_JSON` | optional | Direct Search Console API; without it the engine uses Site Kit |
| `GA4_PROPERTY_ID` | optional | Direct GA4 API |

**Network secret:** an OpenRouter API key for host `openrouter.ai`, injected by the proxy. Code sends the placeholder
`Bearer proxy-injected`. Add or replace it with the `request_credential` tool, never in chat. The account is on the
free tier on purpose: only `:free` models, about 50 requests a day.

**Network allowlist (limited access; package registries and MCP servers allowed).** Hosts the engine needs:
`thechimeraai.com`, `googleapis.com`, `www.googleapis.com`, `oauth2.googleapis.com`, `searchconsole.googleapis.com`,
`analyticsdata.googleapis.com`, `suggestqueries.google.com`, `api.indexnow.org`, `blog.google`,
`developers.google.com`, `support.google.com`, `support.apple.com`, `schema.org`, `en.wikipedia.org`, `api.census.gov`,
`images.unsplash.com`, `unsplash.com`, `www.figma.com`, `figma.com`, `openrouter.ai`, `public-api.wordpress.com`,
plus the competitor and outreach sites: `zupo.co`, `brandastic.com`, `milemarkmedia.com`, `hexxen.com`,
`theadfirm.net`, `ignitedigital.com`, `gnporangecounty.com`, `ocstartupcouncil.org` (each with its `www.` version).
Blocked and not needed: Bing Places, Yelp, Nextdoor, the Unsplash search API, businessconnect.apple.com.
Add hosts with `update_environment` only when a request is actually refused by the proxy.

### 3.2 Claude Code plugins, skills and MCP servers

- **Plugins** (`.claude/settings.json`, project scope): `claude-seo@agricidaniel-claude-seo` (AgriciDaniel/claude-seo)
  and `modern-web-guidance@googlechrome` (GoogleChrome/modern-web-guidance). `scripts/setup.sh` reinstalls them after a
  container reset.
- **Vendored skills** in `.claude/skills/` (MIT, each folder keeps its LICENSE):
  - from garrettjsmith/localseoskills: `local-keyword-research`, `local-landing-pages`, `service-area-seo`,
    `local-content-strategy`, `local-link-building`, `local-citations`, `ai-local-search`, `geogrid-analysis`,
    `review-management`, `local-schema`, `local-competitor-analysis`
  - from coreyhaines31/marketingskills: `mkt-cro`, `mkt-copywriting`, `mkt-programmatic-seo`, `mkt-ai-seo`,
    `mkt-site-architecture`, `mkt-lead-magnets`, `mkt-link-building`, `mkt-offers`, `mkt-free-tools`, `mkt-competitors`
  - from AminForou/mcp-gsc: `gsc-cannibalization-check`, `gsc-content-opportunities`, `gsc-indexing-audit`
  - also `qwoted-seo-backlinks`
- **MCP servers** in `.mcp.json`: see `MCP-SETUP.md` (fetch, memory, lighthouse, web-meta-scraper, context7, semrush,
  cite42, Search Console servers and others). Semrush answers 403 at the moment; cite42 needs a paid balance.
- **Python library from GitHub:** `advertools==0.18.0` (eliasdabbas/advertools, MIT), in `requirements.txt`, used by
  `engine/competitors.py` to read competitor sitemaps.

### 3.3 Connectors (claude.ai account)

- **Gmail:** sends outreach from the user's Gmail (replies arrive there).
- **Artifacts:** the dashboard (`Artifact` and `ArtifactData` tools).
- **Figma, Kittl, Canva:** image generation. Figma credits are used up until **2026-12-01** (do not call Figma before);
  Kittl has no tokens; Canva only returns thumbnails.

### 3.4 WordPress

- Plugin **Chimera Engine 1.7.8** (`wp-plugin/chimera-engine/`, zips in `dist/`). Install or update via Plugins > Add New >
  Upload Plugin > Replace current. The engine cannot upload plugins itself; build a new zip and send it to the user.
- It registers page meta for the engine, prints schema, Markdown alternates, Open Graph, and (since 1.7.7) uses the
  engine's SEO title as the page `<title>` when no SEO plugin is active. REST routes: `chimera/v1/indexnow`, `/pages`,
  `/leads-summary`, `/purge-cache`. It also tracks AI referrals and form leads into GA4 and Site Kit.
- No Yoast or Rank Math is installed; the plugin covers titles, descriptions and social tags.

### 3.5 Scheduled task

Recreate from `prompts/scheduled-task.md` with the claude-code-remote `create_trigger` tool: cron
`CRON_TZ=America/Los_Angeles 42 4 * * *`, the prompt copied exactly. The dashboard refresh runs inside the daily run;
the old 3-hourly refresh task is disabled.

---

## 4. Engine commands

```bash
python -m engine check            # test Google, WordPress and site access
python -m engine status           # today's page limit, queue size, drafts waiting
python -m engine track            # pull Search Console + GA4 numbers (Site Kit unless the service-account key is set)
python -m engine research         # build the query queue (data/queue.json)
python -m engine opportunities    # money queries, striking distance, CTR fixes, cannibalization -> data/opportunities.json
python -m engine competitors      # topic gaps from competitor sitemaps (config/competitors.json) -> data/competitor_gaps.json
python -m engine visibility       # ask free AI models buyer questions; who gets named -> data/ai_visibility/
python -m engine prospects        # merge and rank link opportunities (data/link_prospects_raw.json -> data/link_prospects.json)
python -m engine quality FILE...  # quality gate on draft specs
python -m engine heroes           # render and upload banners for drafts
python -m engine publish --max N  # publish drafts that pass; upserts to WordPress, sends IndexNow, logs the run
python -m engine sitecheck        # llms.txt, robots.txt, sitemap and every page
python -m engine export           # write dashboard data files (dashboard/export/)
python -m engine refresh          # track + export, then list dashboard files that changed (with old blob ids)
python3 content/build/interlink.py  # contextual + related internal links; stages changed older pages as drafts
```

---

## 5. The daily run (what happens each morning)

Full detail: `prompts/daily-run.md`. In order:

1. `git pull`, `pip install -r requirements.txt`, `engine check`, `engine track`, `engine sitecheck`.
2. **Opportunities:** `engine opportunities` (and `engine competitors` when competitors are listed).
3. **Free workers:** `engine visibility`; 3-4 web searches for real Anaheim/Orange County link opportunities, added
   with evidence to `data/link_prospects_raw.json`; `engine prospects`.
4. **Outreach:** up to 3 emails a day from Gmail, only to published submission or news-tip addresses; facts checked;
   no paid routes, no accounts, no repeats, no personal addresses; status set to `contacted`. Paid or broken routes
   become `skip` with the reason. Copy goes in `data/outreach/YYYY-MM-DD.md` with `[brackets]` for contact details.
5. **30 pages:** up to 15 existing pages fixed from `data/opportunities.json` (cannibalization, CTR and
   striking-distance rewrites, money-page CRO) and about 15 new local buyer-intent pages (service or industry x Orange
   County city, with genuine city-specific detail). No new national "seo for <industry>" pages unless a money query
   asks for one.
6. **5 blog posts** from verified news (Google Search blog, Search Central, Google Ads & Commerce, Maps).
7. Banners (`engine heroes`), `interlink.py`, quality gate, `engine publish`, `engine sitecheck`.
8. **Dashboard refresh** (section 7), `data/last-run.md`, commit `Daily run YYYY-MM-DD`, push to `origin` and `buildup`.
9. **Report to the user:** new pages and posts with URLs, pages fixed and why, money-query positions today vs
   yesterday, whether AI named Chimera, outreach sent and replies, top 3 link opportunities, indexed pages,
   impressions, clicks, visits, leads, failures, and anything the user must do.

---

## 6. Content system

- **Specs:** each page is a JSON spec. Drafts in `content/drafts/`, published copies in `content/published/`.
  Fields include `slug`, `query`, `primary_keyword`, `secondary_keywords`, `seo.title`, `seo.meta_description`, `h1`,
  `answer`, `key_takeaways`, `sections[{heading, body_html}]`, `faqs`, `internal_links`, `sources`, `visuals`,
  `hero_image`, `kind` (`guide` or `blog`).
- **Builders** in `content/build/`: `guide()` (batch17) with `finish(i, secs, checklist, example, week)` (batch26);
  `industry(slot, dict)` in `local_lib.py`; `blog(slot, category, **kw)` in `blog_2026_11_10.py`; visuals via
  `V.flow(...)` and bars-chart dicts; `SRC` holds every source. One file per batch: `batchN.py`, `blog_YYYY_MM_DD.py`,
  with `*_extra.py` files adding sections before "The short version". Run a builder with `python3 content/build/<file>.py`.
- **Quality gate:** 1,200+ words, 5+ sections, 5+ FAQs; the keyword's tokens in title, H1 and answer; title 30-60
  characters; meta 120-160; similarity to existing pages at most 0.6 (publish refuses above that; keep pages built the
  same day distinct). Lists and tables count for little, so add prose when short.
- **Interlinking:** `content/build/interlink.py` has `PHRASES` (phrase -> slug) and `CLUSTERS` (regex groups). Add
  phrases for every new topic family. Changed older pages are written back to drafts and republished.
- **Banners:** rendered by `engine heroes` (headline from the SEO title split at the colon, or `banner` in the spec).
  Blog posts get a photo banner: Unsplash photos cropped to 1600x760 (subject right; never mirror photos with text;
  blur logos and readable text), saved as `content/build/banner_photos/<slug>.jpg`; used photos are recorded in
  `data/banner_photos_used.json` and never reused. Blog posts have no in-post photo, no scorecards, no "Local data"
  charts, and sources are recorded but not shown.
- **Topic plans:** `data/topic_plan_YYYY_MM_DD.json` lists each day's topics; never repeat a topic.

---

## 7. Dashboard (Dashboard artifact type)

The page (`files/index.html` in the artifact's store, copy in `dashboard/artifact/index.html`) reads datasets, each an
attached JSON file:

`totals`, `pages`, `blogs`, `keywords`, `daily`, `upcoming`, `site_files`, `page_checks`, `indexing`, `runs`,
`opp_money`, `opp_fixes`, `ai_visibility`, `link_prospects`.

Refresh (once a day, inside the daily run):
1. `python -m engine refresh` prints each changed file with its `old_blob`.
2. Upload each changed file: `Artifact` publish with `url`, `asset: true`, `file_path`.
3. Update the matching `datasets/<name>` documents in one `ArtifactData` batch (`source.url` = new `/_blob/...`,
   `updated: {at, by: "Chimera engine"}`, `edit: {via: "claude", at}`), each pinned with `if_version` from a fresh list.
4. Delete each old blob, and record new blob ids and sha256 in `data/dashboard_assets.json`.

Page edits follow the one-writer rule (`<meta name="dash-one-writer">`): fixed text in HTML, data drawn by
`dash.draw` into empty elements. Re-read `files/index.html` before changing it.

---

## 8. Rules the engine always follows

- **Location lock:** every page and post names Anaheim, California and Orange County, California.
- **No made-up facts:** every statistic is checked at its source with curl and listed in `sources`; unverifiable claims
  are removed. Never invent opportunities, contacts, prices or local facts.
- **No repeated topics, no near-identical city pages** (Google treats them as doorway abuse).
- **Free only** for workers and outreach: free OpenRouter models, no paid listings, no credits bought.
- **Secrets never in chat or the repo:** use `request_credential` or environment settings. The user declined to provide
  a Brave Search key; do not ask again.
- **Big design or template changes:** show the user before publishing.
- **Don't run downloaded or external code** without the user's approval; review a package before installing it.
- **Never spoof user agents.**
- **No model names in commits.** Commit trailer:
  `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and `Claude-Session: <session link>`.
- **Push every daily run to both repos** (`origin`, then `buildup`).
- **Outreach:** at most 3 emails a day, published submission addresses only, signed from the `CHIMERA_CONTACT_*`
  variables, nothing paid, no accounts, no repeats, no personal addresses, every send listed in the report.

---

## 9. Data files

| File | What it holds |
|---|---|
| `config/site.json` | Brand, services, location, tone, never-say list, publishing limits, quality thresholds |
| `config/competitors.json` | Competitor domains for `engine competitors` |
| `config/visibility.json` | Buyer questions, free models and tracked brands for `engine visibility` |
| `data/pages.json`, `data/summary.json`, `data/metrics/` | Page registry and daily metrics |
| `data/opportunities.json`, `data/money_positions/` | Opportunity finder output and daily money-query positions |
| `data/competitor_gaps.json` | Topics competitors cover that we don't |
| `data/ai_visibility/` | Daily AI answers, named agencies, summary |
| `data/link_prospects.json` (+ `_raw`) | Link opportunities with status: new / ready / contacted / listed / skip |
| `data/outreach/` | Outreach copy and images, contact details as [brackets] |
| `data/topic_plan_*.json` | Daily topic plans |
| `data/banner_photos_used.json` | Banner photos used, by day |
| `data/dashboard_assets.json` | Current dashboard blob ids and sha256 |
| `data/last-run.md`, `data/runs.json` | Latest report and run log |
| `data/sitecheck.json`, `data/interlink_report.json` | Site check and internal-link reports |

---

## 10. State on 2026-11-18 (for context)

- 419 pages live; 239 indexed; last 28 days: 5,324 impressions, 10 clicks, 103 visits, 5 leads (3 are Claude test
  leads named "... (ignore)" that can be deleted in WordPress).
- 147 money queries tracked, 14 in the top 20. Strategy since 2026-11-16: fix money pages and add local
  buyer-intent pages (city pages now cover most Orange County cities; see `content/published/seo-*.json`).
- Plugin 1.7.8 live: short SEO titles (1.7.7) and the lead form fix (1.7.8: the hidden `action` input shadowed
  `form.action`, so leads posted to "[object HTMLInputElement]" from Nov 5 to Nov 18).
- AI visibility: Chimera named in 0 of 24 answers; Coalition Technologies, Directive Consulting, Titan Growth and
  Single Grain named most.
- Outreach sent so far: Orange County Business Journal and OC Startup Council (2026-11-16), no replies yet.
  Verified but not yet used: Fullerton Observer, contact@fullertonobserver.com (Fullerton-related stories only).
- Banner photo pool is nearly used up; fetch new Unsplash photos before the next runs.
- The Main-Build-Up repo now lives at https://github.com/boxpackagingus/Main-Build-Up.git (the old lowercase URL
  still redirects).
- The authority gap (links and mentions) is the main limit; local link building is the priority.

---

## 11. Troubleshooting

| Symptom | Fix |
|---|---|
| `request blocked: no rule allows host` / proxy 403 | Add the exact host with `update_environment` (one-time approval) |
| OpenRouter 401/403 | Re-add the key with `request_credential` for `openrouter.ai` |
| OpenRouter 429 on one model | Provider is busy; swap that model in `config/visibility.json` for another `:free` model |
| Publish refuses a page at 0.6+ similarity | Make the page's takeaways, sections and FAQs distinct; don't republish already-published duplicates |
| Page too short in quality gate | Add prose sections (lists and tables count little) |
| `claude-seo` skills missing after a reset | `bash scripts/setup.sh` |
| `rm -rf` with variables blocked | Use literal paths or Python `shutil` |
| Titles look wrong on the live site | Check the plugin is 1.7.7+ and `seo.title` in the spec |
| Dashboard shows "Failed to load" | A dataset's blob was deleted before its document was updated; re-upload and update the dataset |
