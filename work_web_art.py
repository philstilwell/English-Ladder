"""Small, uncropped web copies of the approved learner-book illustrations."""
import hashlib
import html
import json
from functools import lru_cache

from PIL import Image, ImageOps

from work_curriculum import ROOT
from work_web_content import publication_documents

DESTINATION = ROOT / 'assets/work/course-art'


def build_art():
    DESTINATION.mkdir(parents=True, exist_ok=True)
    manifest = DESTINATION / 'manifest.json'
    previous = json.loads(manifest.read_text()) if manifest.exists() else {}
    records = {}
    for slug, publication in publication_documents().items():
        source = ROOT / publication['illustration_asset']
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if digest != publication['illustration_sha256']:
            raise ValueError('Book illustration has changed: ' + slug)
        old = previous.get(slug, {})
        if (old.get('source_sha256') == digest and len(old.get('versions', [])) == 2
                and all((ROOT / r['src']).exists() and hashlib.sha256((ROOT / r['src']).read_bytes()).hexdigest() == r['sha256']
                        for r in old['versions'])):
            records[slug] = old
            continue
        with Image.open(source) as original:
            art = ImageOps.exif_transpose(original)
            if art.mode not in ('RGB', 'RGBA'):
                art = art.convert('RGBA')
            versions = []
            for width in (480, 960):
                copy = art.copy()
                copy.thumbnail((width, width), Image.Resampling.LANCZOS)
                target = DESTINATION / f'{slug}-{width}.webp'
                copy.save(target, format='WEBP', quality=88, method=6)
                versions.append(dict(src=target.relative_to(ROOT).as_posix(),
                                     width=copy.width, height=copy.height,
                                     sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
            records[slug] = dict(source=publication['illustration_asset'], source_sha256=digest, versions=versions)
    (DESTINATION / 'manifest.json').write_text(json.dumps(records, indent=2) + '\n')
    art_records.cache_clear()
    return records


@lru_cache(maxsize=1)
def art_records():
    return json.loads((DESTINATION / 'manifest.json').read_text())


def course_illustration(track, book_url):
    records = art_records()[track['slug']]['versions']
    largest = records[-1]
    srcset = ', '.join(f'{r["src"]}?v={r["sha256"][:12]} {r["width"]}w' for r in records)
    esc = html.escape
    return (f'<figure class="work-book-art"><img src="{largest["src"]}?v={largest["sha256"][:12]}" '
            f'srcset="{srcset}" sizes="(max-width:700px) calc(100vw - 40px), (max-width:1280px) 40vw, 480px" '
            f'width="{largest["width"]}" height="{largest["height"]}" fetchpriority="high" decoding="async" '
            f'alt="{esc(track["title"], quote=True)}: illustration from the revised learner book.">'
            f'<figcaption><a href="{esc(book_url, quote=True)}">Open learner book (PDF) ↗</a></figcaption></figure>')


if __name__ == '__main__':
    print(f'Prepared web illustrations for {len(build_art())} courses.')
