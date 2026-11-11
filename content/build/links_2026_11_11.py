"""Add links to today's new pages from related published pages, and move those pages back to drafts for republishing."""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUB, DRAFTS = ROOT / "content" / "published", ROOT / "content" / "drafts"
BASE = "https://thechimeraai.com/"

# existing page -> [(anchor, new slug), ...]
LINKS = {
    "seo-for-restaurants-orange-county": [("SEO for bakeries", "seo-for-bakeries"), ("SEO for coffee shops", "seo-for-coffee-shops")],
    "geo-for-restaurants": [("SEO for coffee shops", "seo-for-coffee-shops")],
    "seo-for-auto-detailing": [("SEO for car washes", "seo-for-car-washes")],
    "seo-for-salons": [("SEO for tattoo shops", "seo-for-tattoo-shops"), ("SEO for massage therapists", "seo-for-massage-therapists")],
    "seo-for-chiropractors": [("SEO for massage therapists", "seo-for-massage-therapists")],
    "seo-for-gyms": [("SEO for yoga studios", "seo-for-yoga-studios")],
    "seo-for-private-schools": [("SEO for tutoring centers", "seo-for-tutoring-centers")],
    "seo-for-moving-companies": [("SEO for self storage", "seo-for-self-storage")],
    "seo-for-plumbers": [("SEO for water damage restoration", "seo-for-water-damage-restoration")],
    "geo-for-home-services": [("SEO for water damage restoration", "seo-for-water-damage-restoration"), ("SEO for pressure washing", "seo-for-pressure-washing")],
    "seo-for-contractors": [("SEO for kitchen remodelers", "seo-for-kitchen-remodelers"), ("SEO for fence companies", "seo-for-fence-companies")],
    "seo-for-bathroom-remodelers": [("SEO for kitchen remodelers", "seo-for-kitchen-remodelers")],
    "seo-for-landscapers": [("SEO for fence companies", "seo-for-fence-companies")],
    "seo-for-window-cleaning": [("SEO for pressure washing", "seo-for-pressure-washing")],
    "seo-for-law-firms-orange-county": [("SEO for estate planning attorneys", "seo-for-estate-planning-attorneys"),
                                        ("SEO for criminal defense lawyers", "seo-for-criminal-defense-lawyers"),
                                        ("SEO for immigration lawyers", "seo-for-immigration-lawyers")],
    "geo-for-law-firms": [("SEO for estate planning attorneys", "seo-for-estate-planning-attorneys"), ("SEO for immigration lawyers", "seo-for-immigration-lawyers")],
    "seo-for-personal-injury-lawyers": [("SEO for criminal defense lawyers", "seo-for-criminal-defense-lawyers")],
    "ai-search-for-b2b-lead-generation": [("SEO for IT companies", "seo-for-it-companies"), ("SEO for staffing agencies", "seo-for-staffing-agencies")],
    "seo-for-hotels-orange-county": [("SEO for wedding venues", "seo-for-wedding-venues"), ("SEO for event planners", "seo-for-event-planners")],
    "seo-for-home-builders": [("SEO for architects", "seo-for-architects")],
    "seo-for-interior-designers": [("SEO for architects", "seo-for-architects")],
    "google-business-profile-optimization-orange-county": [
        ("Google Business Profile verification", "google-business-profile-verification"),
        ("Google Business Profile categories", "google-business-profile-categories"),
        ("fixing a suspended Google Business Profile", "google-business-profile-suspended"),
        ("Google Business Profile photos", "google-business-profile-photos"),
        ("Google Business Profile posts", "google-business-profile-posts"),
        ("Google Business Profile holiday hours", "google-business-profile-holiday-hours")],
    "service-area-business-seo": [("Google Business Profile service areas", "google-business-profile-service-area")],
    "local-seo-checklist": [("Google Business Profile service areas", "google-business-profile-service-area"),
                            ("Core Web Vitals for local businesses", "core-web-vitals-for-local-businesses")],
    "how-to-respond-to-google-reviews": [("removing fake Google reviews", "how-to-remove-fake-google-reviews")],
    "how-to-get-more-google-reviews": [("removing fake Google reviews", "how-to-remove-fake-google-reviews")],
    "geo-vs-ppc": [("Local Services Ads vs SEO", "google-local-services-ads-vs-seo")],
    "local-seo-orange-county": [("Local Services Ads vs SEO", "google-local-services-ads-vs-seo"),
                                ("Google Business Profile verification", "google-business-profile-verification")],
    "ai-search-optimization-checklist": [("Core Web Vitals for local businesses", "core-web-vitals-for-local-businesses")],
    "robots-txt-for-ai-crawlers": [("Google's shared AI training control", "google-ai-training-control-robots-txt")],
    "ai-crawler-user-agents": [("Google's shared AI training control", "google-ai-training-control-robots-txt")],
    "how-to-optimize-for-google-ai-mode": [("Gemini 4 Carbon in AI Mode", "gemini-4-carbon-ai-mode-local-business")],
    "how-to-track-ai-visibility": [("Search Console's generative AI performance report", "search-console-generative-ai-performance-report")],
    "how-to-measure-geo-results": [("Search Console's generative AI performance report", "search-console-generative-ai-performance-report")],
    "product-pages-for-ai-shopping": [("multimodal search in Search Console", "search-console-multimodal-search-report")],
    "ai-seo-for-small-business": [("Google's free SEO learning paths", "google-seo-learning-paths-small-business")],
}
BLOGS = {"google-ai-training-control-robots-txt", "gemini-4-carbon-ai-mode-local-business", "search-console-generative-ai-performance-report",
         "search-console-multimodal-search-report", "google-seo-learning-paths-small-business"}


def url(slug):
    return BASE + ("blog/" if slug in BLOGS else "") + slug + "/"


if __name__ == "__main__":
    moved = 0
    for slug, adds in LINKS.items():
        f = PUB / f"{slug}.json"
        if not f.exists():
            print("missing", slug)
            continue
        spec = json.loads(f.read_text())
        have = {l["url"] for l in spec.get("internal_links", [])}
        new = [{"anchor": a, "url": url(s)} for a, s in adds if url(s) not in have]
        if not new:
            continue
        spec["internal_links"] = spec.get("internal_links", []) + new
        (DRAFTS / f.name).write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n")
        f.unlink()
        moved += 1
    print("moved back to drafts:", moved)
