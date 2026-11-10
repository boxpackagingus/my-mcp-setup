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


BLOG_RENDER = config.ROOT / "engine" / "art" / "blogbanner.js"
BANNER_PHOTOS = config.ROOT / "content" / "build" / "banner_photos"


def banner_text(spec):
    """Headline (yellow) and subtitle (white) for a blog banner."""
    if spec.get("banner"):
        return spec["banner"]["headline"], spec["banner"]["sub"]
    title = spec["seo"]["title"]
    if ":" in title:
        a, b = title.split(":", 1)
        return a.strip() + ":", b.strip()
    return spec.get("short_title") or title, spec.get("category", "AI search") + " for Anaheim and Orange County"


def _node(script, *argv):
    node_path = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    subprocess.run(["node", str(script), *map(str, argv)], check=True, env={**os.environ, "NODE_PATH": node_path})


def render(specs, out_dir):
    """Blog posts with a banner photo (content/build/banner_photos/<slug>.jpg) get the photo banner;
    everything else gets the branded guide image."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    blogs = [s for s in specs if s.get("kind") == "blog" and (BANNER_PHOTOS / f'{s["slug"]}.jpg').exists()]
    guides = [s for s in specs if s not in blogs]
    files = {}
    if blogs:
        jobs = []
        for s in blogs:
            h, sub = banner_text(s)
            jobs.append({"slug": s["slug"], "photo": str(BANNER_PHOTOS / f'{s["slug"]}.jpg'), "headline": h, "sub": sub})
        jf = out_dir / "blog-jobs.json"
        jf.write_text(json.dumps(jobs))
        _node(BLOG_RENDER, jf, out_dir)
        for s in blogs:
            jpg = out_dir / f"{s['slug']}-banner.jpg"
            Image.open(out_dir / f"{s['slug']}.png").convert("RGB").save(jpg, "JPEG", quality=86, optimize=True, progressive=True)
            files[s["slug"]] = jpg
    if guides:
        files.update(_render_guides(guides, out_dir))
    return files


def _render_guides(specs, out_dir):
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
    blog = jpg.name.endswith("-banner.jpg")
    alt = (f'{spec["h1"]}: banner photo' if blog else
           f'{spec["seo"]["title"]}: illustration with the AI platforms covered in this guide')
    r = requests.post(f"{base}/?rest_route=/wp/v2/media", auth=auth, data=jpg.read_bytes(), timeout=120, headers={
        "Content-Type": "image/jpeg", "Content-Disposition": f'attachment; filename="{jpg.name}"'})
    r.raise_for_status()
    m = r.json()
    requests.post(f"{base}/?rest_route=/wp/v2/media/{m['id']}", auth=auth, timeout=60,
                  json={"alt_text": alt, "title": spec["seo"]["title"], "caption": ""})
    spec["hero_image"] = {"id": m["id"], "url": m["source_url"], "alt": alt, "width": 1600, "height": 760 if blog else 840}
    return spec["hero_image"]
