"""Loads config/site.json and the secrets from environment variables."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DRAFTS = ROOT / "content" / "drafts"
PUBLISHED = ROOT / "content" / "published"


def load():
    with open(ROOT / "config" / "site.json") as f:
        return json.load(f)


def env(name, required=True):
    value = os.environ.get(name, "").strip()
    if required and not value:
        raise SystemExit(
            f"Missing environment variable {name}. "
            "Add it in the cloud environment settings (title bar menu → Edit)."
        )
    return value


def read_json(path, default):
    path = Path(path)
    if not path.exists():
        return default
    with open(path) as f:
        return json.load(f)


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    tmp.replace(path)
