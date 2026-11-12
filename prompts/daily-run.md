# Daily engine run

You are running the Chimera growth engine for the site in `config/site.json`.
Work in this repository. Do every step in order and stop if a step fails.

## 1. Setup

```bash
pip install -q -r requirements.txt
python -m engine check
python -m engine status
```

If `check` fails, do not publish. Write the failure to `data/last-run.md`, commit it, push, and stop.

## 2. Track yesterday

```bash
python -m engine track
```

## 3. Research

```bash
python -m engine research
```

This writes `data/queue.json`, sorted by score. `status` tells you how many pages are allowed today (N).

## 4. Pick N queries

First use `data/topic_plan.json` (the 50-page plan). Take the first N topics with `"status": "planned"`.
Skip a planned topic, and take the next one, if a page in `content/published/` already answers the same question.
When the plan has no planned topics left, take candidates from the top of `data/queue.json` instead.

Skip any query that:
- has nothing to do with the business in `config/site.json`,
- is a person's name, a competitor's brand name, or someone else's product,
- you cannot answer well and honestly, or
- asks the same thing as an existing page in `content/published/`.

## 5. Write one draft per query

Write the day's pages as one build file, `content/build/batchN.py` (copy the pattern of the latest batch file: `page(...)` specs, `visuals_lib` charts, `save_all`). Run it to write `content/drafts/<slug>.json`.

Before using any statistic, download its source page with curl and confirm the exact number, wording and date. Add new sources to `SRC` in the batch file. Use only facts you confirmed.

Each page gets 2–4 visuals (charts, flows, timelines, scorecards, engine logos). Use data charts only with sourced numbers.

Rules for every page:
- **Answer first.** `answer` is 40–60 words, answers the query directly, and contains the primary keyword.
- **Real substance.** At least 1,200 words across 5 or more sections. Give specific steps, examples, comparisons, numbers you can source, and trade-offs. Say who the advice is not for.
- **No made-up facts.** Every statistic needs a source in `sources`. If you can't source a number, leave it out. Never invent case studies, clients, reviews or results.
- **Keywords:** put the primary keyword in the SEO title, H1, short answer, and at least one section heading. Use secondary keywords naturally. Never repeat a keyword just to fill space.
- **Slug:** the query in lowercase with hyphens, e.g. `/is-geo-bring-sales/`. Fix spelling and grammar in the H1 and title, but keep the slug close to the query people search for.
- **SEO title:** 30–60 characters. **Meta description:** 120–160 characters, ending with a reason to click.
- **FAQs:** 5–8 real follow-up questions people ask about this query, each with a 2–4 sentence answer.
- **Internal links:** 3–6 links to existing pages on the site (core service pages and earlier engine pages), with descriptive anchor text.
- **Lead:** connect the topic to the offer in `config/site.json` → `lead`. The page template adds the form twice. Don't add another form.
- Follow `site.tone`, and never use any phrase in `site.never_say`.
- Write HTML in `body_html` using only `<p> <h3> <ul> <ol> <li> <strong> <em> <a> <table> <tr> <th> <td> <blockquote> <code>`. No scripts, no inline styles.

## 6. Images

```bash
python -m engine heroes      # renders and uploads a hero image for each draft
```

Then try one Kittl photo per page (Kittl tool `kittl-generate-media`, model `cmkwr4rin0s11df0iqwaibffd`, workspace `cmw3ss0u90wf20j8zh8ygbry6`, 16:9, editorial style: "navy and violet tones with golden accents, realistic, no readable text, no logos"). Download from cache.kittl.com, blur any garbled text, upload to WordPress media, and set `photo` in the draft (see `content/build/photos.json` for the shape). If Kittl is out of credits, use Figma instead: `generate_image` in file `Xz8xqIbMRL3u73rhaSJwXj` (model `gemini-3.1-flash-lite-image`, 1536×864, same style prompt), download `image.url` from www.figma.com, and use the caption "Illustrative image created for Chimera with Figma AI". Canva's generate-image only returns a small preview, so it is not usable for page photos. Check every image for logos or garbled text and blur them before upload.

## 7. Quality gate, then publish

```bash
python -m engine quality content/drafts/*.json
```

Fix every FAIL and run it again. A draft that still fails after two fixes stays in `content/drafts/`.

```bash
python -m engine publish      # also notifies Bing via IndexNow and logs the run
python -m engine sitecheck    # checks llms.txt, llms-full.txt, robots.txt, sitemap and every page
python -m engine dashboard
```

## 8. Save and report

1. Write `data/last-run.md` with:
   - pages published today, with their URLs
   - pages that failed and why
   - the key numbers from `track`
   - anything that needs a human
   - progress on the 50-page plan (mark published topics in `data/topic_plan.json` with `"status": "published"` and the date)
2. Commit everything with the message `Daily run YYYY-MM-DD` and push to `main`.
3. Refresh the dashboard at https://claude.ai/artifact/Dd9pgZazE6LyFGzXSp8seV:
   - Run `python -m engine export`. It writes ten files in `dashboard/export/`: `totals`, `pages`, `blogs`, `keywords`, `daily`, `upcoming`, `site_files`, `page_checks`, `indexing` and `runs`. Each one matches the `datasets/<name>` document with the same name.
   - Upload each file as an asset to that artifact, one call per file (Artifact tool, `asset: true`).
   - For each upload, `update` the matching `datasets/<name>` document with `source.url` set to the new `/_blob/...` URL, `updated: {at: <now UTC>, by: "Chimera engine"}` and `edit: {via: "claude", at: <now UTC>}`. Use ArtifactData, and pin each write with `if_version` from a fresh read.
   - Then delete the old assets.
   - Don't change `files/index.html` unless the page itself needs to change.

## Location lock (every page and every blog post)

Chimera is in **Anaheim, California**, serving **Orange County, California**. Every page and post must name both.
The template already adds them (hero eyebrow, a "Local help in Anaheim and Orange County, California" section,
Organization address and areaServed in the schema, and the Markdown copy), from `site.location` and `site.region`
in `config/site.json`. In the writing itself, also mention Anaheim and Orange County in the short answer and where
they fit naturally. Never invent local facts: use only figures checked at a source (for example the 2020 census
figures on the Anaheim and Orange County Wikipedia articles).

## Daily guides: 30 new pages a day

> **Image credits (checked 2026-11-11):** Figma's AI image credits are a monthly allowance and are used up until
> **2026-12-01**. Until then, do not call Figma `generate_image`. Blog posts without a banner photo automatically get
> the rendered Chimera banner from `python -m engine heroes`, and guide pages keep their rendered banners. From
> 2026-12-01, resume: blog banner photos first, then pages in `data/photos_todo.json`, at about 25 images per day
> until the month's allowance runs out.
>
> **Blog banner photos until then (Unsplash):** every blog post still gets a real photo banner. Kittl has no tokens
> and Canva only returns thumbnails, so use free Unsplash photos (license allows commercial use, no attribution
> needed): download from `https://images.unsplash.com/photo-<id>?w=2400&q=85&fm=jpg` (the search API needs a key, so
> pick known photo IDs and check each one visually; never use plus.unsplash.com images). Crop to 1600x760 with the
> subject on the right (mirror if needed), blur any logo or readable text with a soft-edged mask, save as
> `content/build/banner_photos/<slug>.jpg`, then run `python -m engine heroes`. If the SEO title has no colon, set
> `"banner": {"headline": ..., "sub": ...}` on the spec. Photos used on 2026-11-11 are listed in
> `data/banner_photos_used.json`; do not reuse them.


Every day, research, write and publish **30 new guide pages**, in addition to the 5 blog posts below.

1. **Research.** Run `python -m engine research`, pull Search Console queries through Site Kit (queries with impressions
   where you rank below position 5 are the fastest wins), and collect Google autocomplete suggestions for local and
   industry seeds such as "seo for <industry>", "<service> <Orange County city>", "how to <local task>". Prefer searches
   with buying intent and local relevance to Anaheim and Orange County. Skip anything an existing page or post covers
   (check `content/published/`).
2. **Plan 30 topics** in `data/topic_plan_YYYY_MM_DD.json`: a mix of industry pages (use `industry()` in
   `content/build/local_lib.py`), how-to guides (use the `guide()` pattern in `content/build/batch17.py`) and AI-search
   topics. City pages only when the city has genuinely new local substance; Google's spam policies treat near-identical
   city pages as doorway abuse. Do not reuse a topic.
3. **Write** `content/build/batchN.py` files of 10 pages each. Every fact checked at its source with curl and listed in
   `sources`. Each page passes the quality gate (1,200+ words, 5+ sections, 5+ FAQs, keyword in title, H1 and answer,
   similarity at most 0.6) and stays under about 40% overlap with other pages from the same day.
4. **Images.** `python -m engine heroes` renders a banner for every page. Add a Figma photo where credits allow; Figma's
   daily AI credits run out after roughly 30 images, so give the 5 blog banner photos priority and add page photos with
   whatever remains, listing the rest in `data/photos_todo.json` for the next day.
5. **Internal links, then publish.** Run `python3 content/build/interlink.py` after all of today's drafts are written
   and pass the quality gate. It links key phrases in the text to the page that covers them (max 5 per page, Google
   Business Profile topics only from sections about the Business Profile), links the first "Chimera" to the homepage,
   adds related pages and a homepage card to every page, and stages any older page whose links changed. Spot-check a
   few links in `data/interlink_report.json`, then publish everything staged with
   `python -m engine publish --max $(ls content/drafts | wc -l)`.
   (Previously: publish with `python -m engine publish --max 35` (30 pages plus 5 posts).) Then **push for indexing**: publishing
   already sends every new URL to IndexNow and updates the sitemap; also add links to the new pages from 5-10 related
   existing pages and republish those, and run `python -m engine sitecheck` to confirm every page is live, in the
   sitemap and in llms.txt. Google has no request-indexing API; if `GSC_SERVICE_ACCOUNT_KEY_JSON` is set, the engine
   also resubmits the sitemap to Search Console.
6. **Dashboard.** Run the quick dashboard refresh below, then commit with the message `Daily run YYYY-MM-DD`.

## Daily blog: 5 posts a day at /blog/

Blog posts are WordPress pages under the `/blog/` parent page. A spec with `"kind": "blog"` is published there,
gets the Blog breadcrumb and BlogPosting schema, and triggers a rebuild of the `/blog/` index (cards with banner,
date, topic and summary, newest first). Build files live in `content/build/blog_YYYY_MM_DD.py`; copy the
`blog(slot, category, ...)` helper and pattern from `content/build/blog_2026_11_10.py`.

1. **Pick the 5 best titles of the day.** Sources, in this order: the latest posts on the Google Search blog RSS
   (`https://blog.google/products-and-platforms/products/search/rss/`) and Google Search Central, new AI search
   news you can verify at the source, high-impression questions in Search Console that no page answers yet,
   and seasonal or local angles for Anaheim and Orange County (tourism, hotels, restaurants, retail, home services,
   healthcare, legal). Each title must give an Anaheim or Orange County business a reason to read. Do not repeat
   a topic already covered by a guide or a post: check `content/published/`.
2. **Write each post** with the same quality rules as guides: 1,200+ words (write 12+ sections and 8+ FAQs), a
   25-80 word answer that contains the keyword and Anaheim or Orange County, at least one table in the body, and
   2-3 visuals (bars or line chart with real numbers, stats tiles, flow or timeline). Blog posts do not show
   scorecards, "Local data" charts or a Sources list (the template hides them), so don't add them. Every number
   is still checked at its source with curl and recorded in `sources` in the spec, even though it is not shown. Keep SEO titles at 30-60 characters and meta
   descriptions at 120-160.
3. **Images (one Figma banner photo per post).**
   - **Banner photo**: Figma `generate_image` (file `Xz8xqIbMRL3u73rhaSJwXj`, model `gemini-3.1-flash-lite-image`,
     1600x760) with the subject on the right third and calm, dark empty space on the left half for the headline,
     no text or logos. Check it, blur any logo, and save it as `content/build/banner_photos/<slug>.jpg`.
     `python -m engine heroes` then writes the headline on it in the Chimera style (yellow headline, white
     subtitle, CHIMERA mark, "Anaheim, Orange County, CA"), taken from the SEO title split at the colon, or from
     `"banner": {"headline": ..., "sub": ...}` in the spec. It becomes the featured image, the /blog/ card image
     and the Related Articles image.
   - **No in-post photo.** Blog posts show only the banner image; do not set `photo` on blog drafts.
   - Blog posts use the editorial layout in `engine/blogpage.py` (dark title band, banner, reading column, grey
     FAQ accordions, previous post, Related Articles, form band); `/blog/` uses the card grid in `engine/blog.py`.
4. **Quality gate and publish.** `python -m engine quality content/drafts/*.json`, fix any failures, then
   `python -m engine publish --max 5`. Publishing purges the cache, rebuilds `/blog/`, and sends the new posts,
   `/blog/` and the homepage to IndexNow. Google has no request-indexing API: new posts reach Google through the
   sitemap, which updates automatically.
5. **Verify** each post and `/blog/` load, show Anaheim, and appear in `wp-sitemap-posts-page-1.xml`.
6. **Dashboard.** Run the quick dashboard refresh below; the Blog section reads the `blogs` and `totals` datasets.
7. Add the 5 posts to `data/last-run.md` and commit with the message `Daily blog YYYY-MM-DD`.

## Quick dashboard refresh (once a day, as part of the daily run)

1. `git pull`, then `python -m engine refresh`. It runs `track` and `export`, then prints the dashboard files that changed (`changed`), each with its `old_blob`.
2. For each changed file: upload it as an asset to https://claude.ai/artifact/Dd9pgZazE6LyFGzXSp8seV, then update the matching `datasets/<name>` document (`source.url` = new `/_blob/...`, `updated`, `edit`) in one ArtifactData batch pinned with `if_version` from a fresh list.
3. Delete each `old_blob` asset, and write the new blob id and sha into `data/dashboard_assets.json`.
4. If nothing changed, do nothing else. Commit `data/` and push. Do not publish pages in this step.
