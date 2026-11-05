"""Command line for the Chimera engine.

  python -m engine check              Test Google, WordPress and site access
  python -m engine research           Build today's query queue (data/queue.json)
  python -m engine quality FILE...    Run the quality gate on draft specs
  python -m engine publish [--dry-run] Publish drafts that pass (respects the daily limit)
  python -m engine track              Pull Search Console + GA4 numbers
  python -m engine dashboard          Rebuild dashboard/index.html
  python -m engine status             Show today's limit and queue size
"""
import json
import sys

from . import config


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, args = argv[0], argv[1:]
    cfg = config.load()

    if cmd == "check":
        return check(cfg)
    if cmd == "research":
        from . import research
        queue = research.run(cfg, use_gsc="--no-gsc" not in args)
        print(f"{len(queue)} candidate queries. Top 15:")
        for c in queue[:15]:
            extra = c.get("volume", c.get("impressions", "?"))
            print(f"  {c['score']:>8}  {c['query']}  ({c['source']}, demand {extra})")
        return 0
    if cmd == "quality":
        from . import publish, quality
        texts = publish.existing_texts()
        failed = 0
        for f in args:
            ok, problems, stats = quality.check(config.read_json(f, {}), cfg, texts)
            print(f"{'PASS' if ok else 'FAIL'}  {f}  {stats}")
            for p in problems:
                print(f"   - {p}")
            failed += not ok
        return 1 if failed else 0
    if cmd == "publish":
        from . import publish
        print(json.dumps(publish.run(cfg, dry_run="--dry-run" in args), indent=2))
        return 0
    if cmd == "track":
        from . import track
        print(json.dumps(track.run(cfg), indent=2))
        return 0
    if cmd == "dashboard":
        from . import dashboard
        print(dashboard.build(cfg))
        return 0
    if cmd == "status":
        from . import publish
        remaining, limit = publish.pages_allowed_today(cfg)
        queue = config.read_json(config.DATA / "queue.json", {"candidates": []})["candidates"]
        drafts = list(config.DRAFTS.glob("*.json"))
        print(f"Daily limit {limit}, {remaining} left today. Queue: {len(queue)}. Drafts waiting: {len(drafts)}.")
        return 0
    print(f"Unknown command: {cmd}\n{__doc__}")
    return 2


def check(cfg):
    import requests
    ok = True
    site = cfg["site"]["base_url"]
    try:
        r = requests.get(site, timeout=20)
        print(f"[ok]   Website reachable ({r.status_code})")
    except requests.RequestException as e:
        ok = False
        print(f"[fail] Website not reachable: {e}. Add {cfg['site']['domain']} to Allowed domains.")
    try:
        from . import google_api
        prop = google_api.gsc_property(cfg["site"]["domain"])
        print(f"[ok]   Search Console property: {prop}")
    except (SystemExit, Exception) as e:
        ok = False
        print(f"[fail] Search Console: {e}")
    try:
        from . import google_api
        google_api.ga4_report("7daysAgo", "yesterday", ["date"], ["sessions"])
        print("[ok]   Google Analytics 4")
    except (SystemExit, Exception) as e:
        ok = False
        print(f"[fail] Google Analytics 4: {e}")
    try:
        from .wp import WordPress
        info = WordPress().check()
        print(f"[ok]   WordPress login as {info['user']} {info['roles']}")
        if not info["plugin_active"]:
            ok = False
            print("[fail] Chimera Engine plugin is not active in WordPress")
    except (SystemExit, Exception) as e:
        ok = False
        print(f"[fail] WordPress: {e}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
