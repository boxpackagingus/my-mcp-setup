# MCP servers: setup notes

`.mcp.json` (next to this file) lists 13 MCP servers built from your starred repos.

Search Console is covered by two servers with different jobs:
- **google-search-console** (thenavidm): everyday Search Console data. It takes the key as an inline secret, so it needs no file.
- **seo-audit-console** (houtini): full site audits (65 tools).

AminForou/mcp-gsc and GiorgiKemo/mcp-seo-audit were dropped because they repeat the same Search Console tools. mcp-seo-audit was also the most fragile: it needed a version pin to start.
Commit both files to a GitHub repo. Every Claude Code session that opens that repo then loads the servers.

## Servers that work with no key (tested)

| Name | From repo | Tools |
|---|---|---|
| maxaeo-ai-visibility | maxaeo/maxaeo-ai-visibility-mcp | 3 |
| lighthouse | danielsogl/lighthouse-mcp-server | 11 |
| web-meta-scraper | cmg8431/web-meta-scraper | 7 |
| npmjs | YawLabs/npmjs-mcp | 64 |
| fetch, memory, sequential-thinking, time | modelcontextprotocol/servers | 1 / 9 / 1 / 3 |
| context7 | upstash/context7 | works without a key; a key gives higher limits |

## Servers that need keys (they start, but need a key before they return data)

Add these as environment variables in the cloud environment settings
(environment menu in the session title bar, then Edit). Never put keys in `.mcp.json` or in chat.

| Variable | Used by | Where to get it |
|---|---|---|
| `GSC_SERVICE_ACCOUNT_KEY_JSON` | google-search-console | Google Cloud service account JSON key (paste the whole JSON). Add the service account's email as a user in Search Console. |
| `GSC_CREDENTIALS_PATH` | seo-audit-console | Path to that same JSON key on disk (see note below) |
| `CITE42_API_KEY` | cite42 | https://www.cite42.dev/app/keys |
| `SEMRUSH_API_KEY` | semrush | Semrush account, API section (needs a paid API plan) |
| `CONTEXT7_API_KEY` | context7 (optional, higher limits) | https://context7.com/dashboard. If you get one, run: `claude mcp add -s project -t http context7 https://mcp.context7.com/mcp -H 'Authorization: Bearer ${CONTEXT7_API_KEY}'` |

Note on `GSC_CREDENTIALS_PATH`: cloud sessions have no file upload. To use seo-audit-console, add this line to the environment's setup script. It saves the JSON secret to a file:

```bash
echo "$GSC_SERVICE_ACCOUNT_KEY_JSON" > /root/gsc-key.json
```

Then set `GSC_CREDENTIALS_PATH=/root/gsc-key.json`.

## Repos not added, and why

- **mgsrevolver/seo-inspector-mcp**: built for Cursor only. It isn't published as a package and runs as a local server you start by hand.
- **bzsasson/screaming-frog-mcp**: needs the licensed Screaming Frog desktop app installed on the same machine, so it won't run in the cloud. It works on your own computer if you have Screaming Frog.
- **Skobyn/dataforseo-mcp-server**: not published, and it needs a build step. The official DataForSEO server (`npx -y dataforseo-mcp-server`, with `DATAFORSEO_USERNAME` / `DATAFORSEO_PASSWORD`) can replace it.

## Fixes already applied

- `semrush` installs from GitHub (`github:mrkooblu/semrush-mcp`), because the npm package with that name belongs to someone else.
- Semrush and Cite42 also have hosted versions that sign in with your account instead of an API key: `https://mcp.semrush.com/v1/mcp` and `https://mcp.cite42.dev`.
