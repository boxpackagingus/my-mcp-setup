"""WordPress REST API client (uses an Application Password, never the admin password)."""
import requests

from . import config


class WordPress:
    def __init__(self):
        self.base = config.env("WP_URL").rstrip("/")
        self.auth = (config.env("WP_USER"), config.env("WP_APP_PASSWORD"))
        self.api = f"{self.base}/wp-json/wp/v2"

    def _req(self, method, path, **kw):
        r = requests.request(method, f"{self.api}{path}", auth=self.auth, timeout=60, **kw)
        if r.status_code >= 400:
            raise RuntimeError(f"WordPress {method} {path} failed ({r.status_code}): {r.text[:500]}")
        return r.json()

    def check(self):
        """Confirms login works and the Chimera Engine plugin is active."""
        me = self._req("GET", "/users/me", params={"context": "edit"})
        root = requests.get(f"{self.base}/wp-json/", timeout=30).json()
        plugin = "chimera/v1" in root.get("namespaces", [])
        return {"user": me.get("name"), "roles": me.get("roles"), "plugin_active": plugin}

    def find_page(self, slug):
        pages = self._req("GET", "/pages", params={"slug": slug, "status": "any", "context": "edit"})
        return pages[0] if pages else None

    def all_engine_pages(self):
        """Every page the engine made (served by the Chimera Engine plugin)."""
        r = requests.get(f"{self.base}/wp-json/chimera/v1/pages", auth=self.auth, timeout=60)
        r.raise_for_status()
        return r.json()

    def site_pages(self):
        """Published pages and posts, used to choose internal links."""
        out = []
        for kind in ("pages", "posts"):
            page = 1
            while True:
                r = requests.get(f"{self.api}/{kind}", params={"per_page": 100, "page": page,
                                 "_fields": "id,link,title,slug"}, timeout=60)
                if r.status_code == 400 or not r.ok:
                    break
                items = r.json()
                out += [{"url": i["link"], "title": i["title"]["rendered"], "slug": i["slug"]} for i in items]
                if len(items) < 100:
                    break
                page += 1
        return out

    def upsert_page(self, spec, html, markdown, schema_json, status="publish"):
        """Creates the page, or updates it if the slug already exists."""
        seo = spec["seo"]
        meta = {
            "_chimera_engine": True,
            "_chimera_query": spec["query"],
            "_chimera_markdown": markdown,
            "_chimera_schema": schema_json,
            "_chimera_meta_description": seo["meta_description"],
            # Yoast and Rank Math fields (the plugin exposes them to the API).
            "_yoast_wpseo_title": seo["title"],
            "_yoast_wpseo_metadesc": seo["meta_description"],
            "_yoast_wpseo_focuskw": spec["primary_keyword"],
            "rank_math_title": seo["title"],
            "rank_math_description": seo["meta_description"],
            "rank_math_focus_keyword": ",".join([spec["primary_keyword"]] + spec.get("secondary_keywords", [])[:4]),
        }
        body = {
            "title": spec["h1"],
            "slug": spec["slug"],
            "content": html,
            "excerpt": seo["meta_description"],
            "status": status,
            "meta": meta,
        }
        existing = self.find_page(spec["slug"])
        if existing:
            return self._req("POST", f"/pages/{existing['id']}", json=body), "updated"
        return self._req("POST", "/pages", json=body), "created"
