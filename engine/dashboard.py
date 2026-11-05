"""Builds dashboard/index.html: one self-contained page with the latest numbers."""
import html
import json
from datetime import date

from . import config

TEMPLATE = config.ROOT / "dashboard" / "template.html"
OUT = config.ROOT / "dashboard" / "index.html"


def build(cfg):
    summary = config.read_json(config.DATA / "summary.json", {"history": [], "latest": {}})
    pages = config.read_json(config.DATA / "pages.json", [])
    queue = config.read_json(config.DATA / "queue.json", {"candidates": []})
    data = {
        "site": cfg["site"]["domain"],
        "built": date.today().isoformat(),
        "summary": summary,
        "pages": sorted(pages, key=lambda p: p.get("published", ""), reverse=True),
        "queue": queue.get("candidates", [])[:30],
        "pages_per_day": cfg["publishing"]["pages_per_day"],
    }
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    page = TEMPLATE.read_text().replace("__DATA__", payload).replace(
        "__SITE__", html.escape(cfg["site"]["domain"]))
    OUT.write_text(page)
    return OUT
