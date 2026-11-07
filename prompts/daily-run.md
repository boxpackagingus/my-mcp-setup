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
   - Run `python -m engine export`. It writes nine files in `dashboard/export/`: `totals`, `pages`, `keywords`, `daily`, `upcoming`, `site_files`, `page_checks`, `indexing` and `runs`. Each one matches the `datasets/<name>` document with the same name.
   - Upload each file as an asset to that artifact, one call per file (Artifact tool, `asset: true`).
   - For each upload, `update` the matching `datasets/<name>` document with `source.url` set to the new `/_blob/...` URL, `updated: {at: <now UTC>, by: "Chimera engine"}` and `edit: {via: "claude", at: <now UTC>}`. Use ArtifactData, and pin each write with `if_version` from a fresh read.
   - Then delete the old assets.
   - Don't change `files/index.html` unless the page itself needs to change.

## Quick dashboard refresh (every 3 hours)

1. `git pull`, then `python -m engine refresh`. It runs `track` and `export`, then prints the dashboard files that changed (`changed`), each with its `old_blob`.
2. For each changed file: upload it as an asset to https://claude.ai/artifact/Dd9pgZazE6LyFGzXSp8seV, then update the matching `datasets/<name>` document (`source.url` = new `/_blob/...`, `updated`, `edit`) in one ArtifactData batch pinned with `if_version` from a fresh list.
3. Delete each `old_blob` asset, and write the new blob id and sha into `data/dashboard_assets.json`.
4. If nothing changed, do nothing else. Commit `data/` and push. Do not publish pages in this step.
