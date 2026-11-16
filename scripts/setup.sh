#!/usr/bin/env bash
# One-command setup for the Chimera engine in a fresh Claude Code cloud session.
# Safe to run more than once. It installs, connects and checks; it never publishes or sends anything.
#   bash scripts/setup.sh
set -u
cd "$(dirname "$0")/.."
ok()   { printf '  [ok]   %s\n' "$1"; }
warn() { printf '  [todo] %s\n' "$1"; }

echo "1. Python packages"
if pip install -q -r requirements.txt >/dev/null 2>&1; then ok "requirements.txt installed (incl. advertools)"; else warn "pip install failed: run 'pip install -r requirements.txt' and read the error"; fi

echo "2. Claude Code plugins (project scope, see .claude/settings.json)"
if command -v claude >/dev/null 2>&1; then
  claude plugin marketplace add AgriciDaniel/claude-seo >/dev/null 2>&1
  claude plugin install claude-seo@agricidaniel-claude-seo --scope project >/dev/null 2>&1 && ok "claude-seo" || warn "claude-seo plugin did not install"
  claude plugin marketplace add GoogleChrome/modern-web-guidance >/dev/null 2>&1
  claude plugin install modern-web-guidance@googlechrome --scope project >/dev/null 2>&1 && ok "modern-web-guidance" || warn "modern-web-guidance plugin did not install"
else
  warn "claude CLI not found; plugins load from .claude/settings.json when a session opens the repo"
fi
ok "24 vendored skills are already in .claude/skills/ (local-*, mkt-*, gsc-*)"

echo "3. Git remotes (daily runs push to both)"
git remote get-url buildup >/dev/null 2>&1 || git remote add buildup https://github.com/boxpackagingus/main-build-up
git config branch.main.remote origin; git config branch.main.merge refs/heads/main
ok "origin = $(git remote get-url origin)"; ok "buildup = $(git remote get-url buildup)"

echo "4. Environment variables (cloud environment settings > Edit)"
for v in WP_URL WP_USER WP_APP_PASSWORD; do [ -n "${!v:-}" ] && ok "$v" || warn "$v missing (required to publish)"; done
for v in CHIMERA_CONTACT_NAME CHIMERA_CONTACT_PHONE CHIMERA_CONTACT_EMAIL; do [ -n "${!v:-}" ] && ok "$v" || warn "$v missing (outreach sign-off)"; done
for v in GSC_SERVICE_ACCOUNT_KEY_JSON GA4_PROPERTY_ID; do [ -n "${!v:-}" ] && ok "$v" || warn "$v not set (optional: without it Search Console data comes through Site Kit)"; done

echo "5. Network and secrets"
code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 https://thechimeraai.com/wp-json/chimera/v1) ; [ "$code" = 200 ] && ok "thechimeraai.com reachable (plugin REST route answers)" || warn "thechimeraai.com/wp-json/chimera/v1 returned $code"
code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 https://openrouter.ai/api/v1/key) ; [ "$code" = 200 ] && ok "OpenRouter key (network secret) works" || warn "OpenRouter returned $code: add the key with request_credential for host openrouter.ai"

echo "6. Engine self-check"
python -m engine check >/dev/null 2>&1 && ok "python -m engine check passed" || warn "python -m engine check failed: run it to see why"
python -m engine status 2>/dev/null | head -5 | sed 's/^/         /'

echo
echo "Not checkable from a script (do these in Claude): scheduled task (prompts/scheduled-task.md), Gmail connector,"
echo "dashboard artifact access (https://claude.ai/artifact/Dd9pgZazE6LyFGzXSp8seV). See HANDBOOK.md section 3."
