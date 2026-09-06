"""Verify the published Discover feature and its exact image after deployment."""
import hashlib
import time
from pathlib import Path
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent


def feature_signature(markup):
    soup = BeautifulSoup(markup, "html.parser")
    feature = soup.select_one(".feature-story")
    if feature is None:
        raise ValueError("Missing Discover feature")
    stamp = feature.find("time")
    image = feature.find("img")
    return {
        "title": feature.select_one("#feature-title").get_text(strip=True),
        "date": stamp.get("datetime") if stamp else None,
        "start": feature.select_one("#feature-start")["href"],
        "levels": [el.get("data-lesson-href") for el in feature.select('input[name="feature-level"]')],
        "image": image["src"] if image else None,
    }


def fetch_bytes(url):
    request = Request(url, headers={"User-Agent": "English-Ladder-deploy-check", "Cache-Control": "no-cache"})
    with urlopen(request, timeout=30) as response:
        return response.read(10_000_000)


def discover_mismatches(origin, root=ROOT, fetch=fetch_bytes):
    try:
        expected = feature_signature((Path(root) / "index.html").read_text())
        live = feature_signature(fetch(f"{origin}/?deploy-check={time.time_ns()}").decode("utf-8"))
        if expected != live:
            return ["Discover: live headline, date, level links, or image do not yet match the generated feature."]
        if expected["image"]:
            local = (Path(root) / expected["image"]).read_bytes()
            remote = fetch(f'{origin}/{expected["image"]}?deploy-check={time.time_ns()}')
            if hashlib.sha256(local).digest() != hashlib.sha256(remote).digest():
                return ["Discover: the featured image has not finished deploying."]
        return []
    except Exception as error:
        return [f"Discover: could not verify deployment ({type(error).__name__})."]
