"""Hero images: render a branded image per page, upload it to WordPress, record it in the spec."""
import hashlib
import json
import os
import subprocess
from pathlib import Path

import requests
from PIL import Image

from . import config

ICONS = config.ROOT / "wp-plugin" / "chimera-engine" / "assets" / "icons"
RENDER = config.ROOT / "engine" / "art" / "render.js"


def _job(spec):
    hue = 200 + int(hashlib.md5(spec["slug"].encode()).hexdigest(), 16) % 90  # blue → violet range
    title = spec.get("short_title") or spec["seo"]["title"]
    return {"slug": spec["slug"], "title": title, "eyebrow": spec.get("eyebrow", "GEO guide"),
            "query": spec.get("hero_query") or spec["query"][:1].upper() + spec["query"][1:] + "?",
            "engines": spec.get("hero_engines") or ["chatgpt", "perplexity", "gemini", "claude", "google", "copilot"],
            "hue": hue}


def render(specs, out_dir):
    out_dir = Path(out_dir)
    jobs_file = out_dir / "jobs.json"
    out_dir.mkdir(parents=True, exist_ok=True)
    jobs_file.write_text(json.dumps([_job(s) for s in specs]))
    node_path = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    subprocess.run(["node", str(RENDER), str(jobs_file), str(out_dir), str(ICONS)], check=True,
                   env={**os.environ, "NODE_PATH": node_path})
    files = {}
    for s in specs:
        png = out_dir / f"{s['slug']}.png"
        jpg = out_dir / f"{s['slug']}-chimera.jpg"
        Image.open(png).convert("RGB").save(jpg, "JPEG", quality=86, optimize=True, progressive=True)
        files[s["slug"]] = jpg
    return files


def upload(spec, jpg):
    base = config.env("WP_URL").rstrip("/")
    auth = (config.env("WP_USER"), config.env("WP_APP_PASSWORD"))
    alt = f'{spec["seo"]["title"]}: illustration with the AI platforms covered in this guide'
    r = requests.post(f"{base}/?rest_route=/wp/v2/media", auth=auth, data=jpg.read_bytes(), timeout=120, headers={
        "Content-Type": "image/jpeg", "Content-Disposition": f'attachment; filename="{jpg.name}"'})
    r.raise_for_status()
    m = r.json()
    requests.post(f"{base}/?rest_route=/wp/v2/media/{m['id']}", auth=auth, timeout=60,
                  json={"alt_text": alt, "title": spec["seo"]["title"], "caption": ""})
    spec["hero_image"] = {"id": m["id"], "url": m["source_url"], "alt": alt, "width": 1600, "height": 840}
    return spec["hero_image"]
