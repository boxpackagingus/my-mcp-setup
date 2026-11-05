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

Take candidates from the top of `data/queue.json`. Skip any query that:
- has nothing to do with the business in `config/site.json`,
- is a person's name, a competitor's brand name, or someone else's product,
- you cannot answer well and honestly, or
- asks the same thing as an existing page in `content/published/`.

## 5. Write one draft per query

For each query, write `content/drafts/<slug>.json` in the same shape as `content/examples/is-geo-bring-sales.json`.

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

## 6. Quality gate, then publish

```bash
python -m engine quality content/drafts/*.json
```

Fix every FAIL and run it again. A draft that still fails after two fixes stays in `content/drafts/`.

```bash
python -m engine publish
python -m engine dashboard
```

## 7. Save and report

1. Write `data/last-run.md` with:
   - pages published today, with their URLs
   - pages that failed and why
   - the key numbers from `track`
   - anything that needs a human
2. Commit everything with the message `Daily run YYYY-MM-DD` and push to `main`.
3. Republish the dashboard artifact from `dashboard/index.html` (same artifact URL each day).
