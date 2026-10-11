"""Publish the approved, consolidated learner books without altering their PDFs."""
from __future__ import annotations

import hashlib
import importlib
import json
import shutil
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
EDITION = '2026-10-10'


def book_stem(slug):
    return 'cross-cultural-leadership' if slug == 'cultural-leadership-us-branches' else slug


def book_href(slug):
    return f'pdf/efsp/{book_stem(slug)}-english-book.pdf'


def book_source(slug):
    return ROOT / 'output/pdf' / f'{book_stem(slug)}-english-book.pdf'


def book_units(slug):
    if slug == 'cultural-leadership-us-branches':
        from books.cross_cultural_leadership_content import UNITS
        return UNITS
    return importlib.import_module('books.' + slug.replace('-', '_') + '_content').BOOK['units']


def book_metadata(track, curriculum_hash):
    from build_leadership_book import TOTAL_PAGES, content_hash, validate_content
    from books.supplements import load_supplements
    from work_icons import icon_asset

    slug = track['slug']
    units = book_units(slug)
    supplements = load_supplements(slug)
    validate_content(units, [m['title'] for m in track['modules']])
    source = book_source(slug)
    reader = PdfReader(source)
    book_hash = content_hash(units, supplements)
    if book_hash not in (reader.metadata.subject or ''):
        raise ValueError('Rebuild the learner book before publishing: ' + slug)
    if len(reader.pages) != TOTAL_PAGES:
        raise ValueError('Unexpected learner-book page count: ' + slug)
    illustration = icon_asset(slug)[0]
    return dict(course=slug, kind='Learner book', revision=EDITION,
                pages=len(reader.pages), bytes=source.stat().st_size,
                sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                source=str(source.relative_to(ROOT)), content_hash=curriculum_hash,
                book_content_hash=book_hash, dialogue_count=len(units) + len(supplements),
                dialogue_turns=sum(len(u['dialogue']) for u in units + supplements),
                transfer_dialogue_count=len(units) + len(supplements),
                vocabulary_entries=sum(len(u['vocabulary']) for u in units),
                phrase_count=sum(len(u['phrases']) for u in units),
                illustration_asset=illustration,
                illustration_sha256=hashlib.sha256((ROOT / illustration).read_bytes()).hexdigest())


def publish_books(slugs=None):
    from work_curriculum import content_hash, load_tracks, validate_tracks

    tracks = load_tracks()
    validate_tracks(tracks)
    selected = set(slugs or [t['slug'] for t in tracks])
    unknown = selected - {t['slug'] for t in tracks}
    if unknown:
        raise ValueError(f'Unknown courses: {sorted(unknown)}')
    curriculum_hash = content_hash()
    # Validate the complete edition before replacing any public asset.
    documents = {book_href(t['slug']): book_metadata(t, curriculum_hash) for t in tracks}
    for href, meta in documents.items():
        target = ROOT / href
        if meta['course'] not in selected:
            if not target.exists() or hashlib.sha256(target.read_bytes()).hexdigest() != meta['sha256']:
                raise ValueError('Publish the complete set; another book is missing or stale: ' + href)
    for href, meta in documents.items():
        if meta['course'] not in selected:
            continue
        target = ROOT / href
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or hashlib.sha256(target.read_bytes()).hexdigest() != meta['sha256']:
            temporary = target.with_suffix('.pdf.tmp')
            try:
                shutil.copyfile(ROOT / meta['source'], temporary)
                temporary.replace(target)
            finally:
                temporary.unlink(missing_ok=True)
    manifest = dict(revision=EDITION, content_hash=curriculum_hash, documents=documents)
    (ROOT / 'content/work/documents.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'Published {len(selected)} learner books; {len(documents)} courses in the download manifest.')
    return manifest


def validate_publication(tracks):
    from work_curriculum import content_hash
    from build_leadership_book import content_hash as book_hash
    from books.supplements import load_supplements

    manifest = json.loads((ROOT / 'content/work/documents.json').read_text())
    if manifest['revision'] != EDITION:
        raise ValueError('Publish the current learner-book edition before generating course pages.')
    if manifest['content_hash'] != content_hash():
        raise ValueError('Publish learner books before generating course pages.')
    expected = {book_href(t['slug']) for t in tracks}
    if set(manifest['documents']) != expected:
        raise ValueError('The download manifest must contain exactly one learner book per course.')
    for href, meta in manifest['documents'].items():
        if meta['book_content_hash'] != book_hash(book_units(meta['course']), load_supplements(meta['course'])):
            raise ValueError('Rebuild and republish the edited learner book: ' + href)
        if hashlib.sha256((ROOT / href).read_bytes()).hexdigest() != meta['sha256']:
            raise ValueError('Public learner book differs from its download record: ' + href)
        if hashlib.sha256(book_source(meta['course']).read_bytes()).hexdigest() != meta['sha256']:
            raise ValueError('Republish the updated learner book: ' + href)
    return manifest
