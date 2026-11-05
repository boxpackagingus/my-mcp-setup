# Chimera Growth Engine

A daily engine for **thechimeraai.com** that finds the questions buyers search for, publishes a landing page for each one, and tracks traffic, AI-search visits and leads.

```
research → write → quality gate → publish to WordPress → llms.txt / sitemap → track → dashboard
```

| Step | What happens | Code |
|---|---|---|
| Research | Pulls queries from Search Console (impressions, weak rank) and Google Autocomplete, adds volume and difficulty from DataForSEO, and scores them | `engine/research.py` |
| Write | A scheduled Claude session writes one page spec per query, following `prompts/daily-run.md` | `content/drafts/*.json` |
| Quality gate | Checks length, structure, FAQs, keyword placement, banned phrases and overlap with existing pages. Failing pages are not published. | `engine/quality.py` |
| Publish | Builds the HTML, schema (Article, FAQPage, BreadcrumbList) and Markdown copy, then creates or updates the page in WordPress | `engine/page.py`, `engine/wp.py`, `engine/publish.py` |
| Track | Search Console clicks, impressions, position and index status per page; GA4 visits, AI-search visits and leads | `engine/track.py` |
| Dashboard | One page with the latest numbers | `engine/dashboard.py` → `dashboard/index.html` |

## Publishing pace

The engine starts at **3 pages a day**. After 14 days, if at least half of the checked pages are indexed, it moves to **10 a day**. Change this in `config/site.json` → `publishing`. The ramp protects the domain from Google's scaled-content spam rules.

## WordPress plugin (install once)

Zip `wp-plugin/chimera-engine/` and upload it in **Plugins → Add New → Upload Plugin**, then activate it. It:

- serves `/llms.txt`, `/llms-full.txt` and a Markdown copy of every engine page at `/<slug>.md`
- adds AI crawler rules and the sitemap to `robots.txt`. This only works when there is no physical `robots.txt` file on the server.
- prints each page's schema in `<head>`, plus a meta description when no SEO plugin is installed
- keeps engine pages out of automatic menus, and lists them all with the `[chimera_hub]` shortcode. Put that on an "Insights" page, so Google can find every page through links.
- records the first source of each visit (AI engine, referrer, UTM), sends an `ai_referral` event to GA4, fills hidden form fields named `chimera_landing`, `chimera_referrer`, `chimera_utm_source`, `chimera_ai_engine` and so on, and sends `generate_lead` when a form succeeds. It handles Contact Form 7, WPForms, Gravity Forms, Elementor and Fluent Forms.
- exposes Yoast or Rank Math title, description and focus keyword to the API, so the engine can set them

## Secrets (cloud environment settings → Edit)

| Variable | What it is |
|---|---|
| `GSC_SERVICE_ACCOUNT_KEY_JSON` | Google service account JSON key, with Full access in Search Console |
| `GA4_PROPERTY_ID` | GA4 property number. The service account needs Viewer access. |
| `WP_URL` | `https://thechimeraai.com` |
| `WP_USER` | A WordPress user with the Editor role |
| `WP_APP_PASSWORD` | Application Password for that user (Users → Profile) |
| `DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD` | Optional. Adds search volume and difficulty. |

Allowed domains: `thechimeraai.com`, `googleapis.com`, `oauth2.googleapis.com`, `searchconsole.googleapis.com`, `analyticsdata.googleapis.com`, `suggestqueries.google.com`, `api.dataforseo.com`.

## Commands

```bash
pip install -r requirements.txt
python -m engine check               # test every connection
python -m engine research            # build today's query queue
python -m engine quality content/drafts/*.json
python -m engine publish --dry-run   # preview into content/preview/
python -m engine publish
python -m engine track
python -m engine dashboard
python -m pytest -q tests
```

## Folders

- `config/site.json`: business details, offer, form shortcode, pace and quality rules
- `content/examples/`: a reference page spec (`is-geo-bring-sales.json`)
- `content/drafts/`: pages waiting to publish
- `content/published/`: specs of pages that are live
- `data/`: queue, page records, daily metrics
- `prompts/daily-run.md`: instructions for the daily scheduled run
- `MCP-SETUP.md`: the MCP servers available to Claude in this repo
