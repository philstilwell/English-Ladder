"""Verify revision records against the authored content and the delivered bytes."""
import hashlib
import json
from pathlib import Path

import build_leadership_pilot as design
from build_revised_books import configure

ROOT = Path(__file__).resolve().parent


def stem(slug, staged=False):
    name = 'cross-cultural-leadership' if slug == 'cultural-leadership-us-branches' else slug
    return name + '-english-book' + ('-revised' if staged else '')


def record(slug, staged=False, root=ROOT):
    name = stem(slug, staged)
    path = root / 'output/pdf' / (name + '-manifest.json')
    return json.loads(path.read_text())


def verify_record(slug, staged=False, root=ROOT):
    configure(slug)
    metadata = record(slug, staged, root)
    if metadata['source_hash'] != design.source_hash():
        raise ValueError('Rebuild and republish the edited learner book: ' + slug)
    pdf = root / 'output/pdf' / (stem(slug, staged) + '.pdf')
    if hashlib.sha256(pdf.read_bytes()).hexdigest() != metadata['sha256']:
        raise ValueError('Learner book differs from its revision record: ' + slug)
    return metadata
