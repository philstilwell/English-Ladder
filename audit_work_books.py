"""Reproducible structural PDF audit; editorial review is recorded separately."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import pdfplumber
from pypdf import PdfReader

import build_leadership_book as design
from build_industry_books import load_book, validate_book
from books.cross_cultural_leadership_content import SLUG, UNITS, WEB_ORDER
from books.supplements import load_supplements
from work_curriculum import load_tracks

ROOT = Path(__file__).resolve().parent


def normalized(text):
    return re.sub(r'\s+', ' ', text).strip()


def book_data(track):
    if track['slug'] == SLUG:
        design.validate_content(UNITS, WEB_ORDER)
        return UNITS
    book = load_book(track['slug'])
    validate_book(book, track)
    return book['units']


def blank_runs(chars):
    runs = []
    for char in sorted((c for c in chars if c['text'] == '_'),
                       key=lambda c: (round(c['top'], 2), c['x0'])):
        if (runs and abs(char['top'] - runs[-1][-1]['top']) < .02
                and abs(char['x0'] - runs[-1][-1]['x1']) < .02):
            runs[-1].append(char)
        else:
            runs.append([char])
    return [run for run in runs if len(run) >= 8]


def audit_blank_geometry(path, units, supplements):
    expected = {}
    for i, unit in enumerate(units):
        first = design.unit_page(i) + 6
        expected[first] = sum(g['turn'] <= 10 for g in unit['gaps'])
        expected[first + 1] = sum(g['turn'] > 10 for g in unit['gaps'])
        expected[first + 2] = len(unit['transfer']['lines'])
    for i, unit in enumerate(supplements):
        first = design.supplement_page(i)
        expected[first] = sum(g['turn'] <= 10 for g in unit['gaps'])
        expected[first + 1] = sum(g['turn'] > 10 for g in unit['gaps'])
        expected[first + 2] = len(unit['transfer']['lines'])
    target = design.pdfmetrics.stringWidth('_' * design.CLOZE_UNDERSCORES,
                                          'Book', design.CLOZE_FONT_SIZE)
    widths = []
    with pdfplumber.open(path) as pdf:
        for number, count in expected.items():
            page = pdf.pages[number - 1]
            runs = blank_runs(page.chars)
            assert len(runs) == count, (path.stem, number, 'printed blank count', len(runs), count)
            for run in runs:
                width = run[-1]['x1'] - run[0]['x0']
                assert len(run) == design.CLOZE_UNDERSCORES, (path.stem, number, 'split blank')
                assert abs(width - target) < .05, (path.stem, number, 'blank width', width, target)
                assert all(abs(c['size'] - design.CLOZE_FONT_SIZE) < .01 for c in run), (path.stem, number, 'blank font size')
                assert design.LEFT <= run[0]['x0'] < run[-1]['x1'] <= design.RIGHT + .05, (path.stem, number, 'blank overflow')
                widths.append(width)
            page.close()
    return dict(count=len(widths), min_width_pt=round(min(widths), 3),
                max_width_pt=round(max(widths), 3))


def audit(track, published=False):
    slug = track['slug']
    stem = 'cross-cultural-leadership' if slug == SLUG else slug
    path = ROOT / ('pdf/efsp' if published else 'output/pdf') / f'{stem}-english-book.pdf'
    units = book_data(track)
    supplements = load_supplements(slug)
    reader = PdfReader(path)
    pages = [normalized(page.extract_text() or '') for page in reader.pages]
    expected_pages = design.TOTAL_PAGES
    assert len(pages) == expected_pages, (slug, 'page count', len(pages))
    assert design.content_hash(units, supplements) in reader.metadata.subject, (slug, 'stale source')
    if not published:
        layout_name = 'leadership' if slug == SLUG else slug
        layout = json.loads((ROOT / 'tmp/pdfs' / f'{layout_name}-book-layout.json').read_text())
        design.validate_layout(layout['boxes'])
        assert layout['pages'] == len(pages)
    page_ids = {page.indirect_reference.idnum for page in reader.pages}
    font_count, internal_links, external_links = 0, 0, 0
    for n, (page, text) in enumerate(zip(reader.pages, pages), 1):
        assert 'English Ladder' in text and text.count('ENGLISHLADDER.COM') == 1, (slug, n, 'branding')
        assert f'Phil Stilwell | {n:02d}' in text, (slug, n, 'page number')
        assert not re.search(r'\{\{|\[\[|\ufffd|\bdraft edition\b', text, re.I), (slug, n, 'placeholder')
        for font in page['/Resources'].get('/Font', {}).get_object().values():
            obj = font.get_object()
            descriptor = obj.get('/FontDescriptor')
            assert descriptor and any(k in descriptor.get_object() for k in ('/FontFile', '/FontFile2', '/FontFile3')), (slug, n, 'unembedded font')
            font_count += 1
        footer_links = 0
        for annotation in page.get('/Annots', []):
            annotation = annotation.get_object()
            action = annotation.get('/A', {})
            destination = annotation.get('/Dest', action.get('/D'))
            if destination:
                assert destination[0].idnum in page_ids, (slug, n, 'broken internal link')
                internal_links += 1
            if action.get('/URI'):
                external_links += 1
                if action['/URI'] == design.FOOTER_URL:
                    footer_links += 1
        assert footer_links == 1, (slug, n, 'footer link')
    for i, unit in enumerate(units):
        key = pages[design.key_page(i) - 1]
        conversation_key = pages[design.key_page(i, True) - 1]
        for question in unit['a'] + unit['d']:
            assert normalized(question['reason']) in key, (slug, i, 'question explanation')
        for gap in unit['gaps']:
            assert normalized(gap['reason']) in conversation_key, (slug, i, 'gap explanation')
        for question in unit['transfer']['lines']:
            answer = question['options'][question['answer']]
            assert normalized(question['prompt'].replace('___', answer)) in conversation_key
            assert normalized(question['reason']) in conversation_key
        for n, (term, definition, collocation) in enumerate(unit['vocabulary']):
            page = pages[design.unit_page(i) + n // 12]
            assert all(normalized(value) in page for value in (term, definition, collocation)), (slug, i, term)
        for n, (_, phrase) in enumerate(unit['phrases']):
            assert normalized(phrase) in pages[design.unit_page(i) + 2 + n // 8], (slug, i, phrase)
    for i, unit in enumerate(supplements):
        first, second = pages[design.supplement_page(i) - 1:design.supplement_page(i) + 1]
        key = pages[design.SUPPLEMENT_KEYS_START + i - 1]
        for gap in unit['gaps']:
            assert normalized(gap['answer']) in first and normalized(gap['answer']) in second
            assert normalized(gap['reason']) in key
        for question in unit['transfer']['lines']:
            answer = question['options'][question['answer']]
            assert normalized(question['prompt'].replace('___', answer)) in key
            assert normalized(question['reason']) in key
        if unit.get('reference'):
            title, url = unit['reference']
            assert normalized(title) in key
            key_page = reader.pages[design.SUPPLEMENT_KEYS_START + i - 1]
            links = [a.get_object().get('/A', {}).get('/URI') for a in key_page.get('/Annots', [])]
            assert url in links, (slug, i, 'supplement source link')
    expected_gaps = 112 + 30
    assert len(re.findall('_' * design.CLOZE_UNDERSCORES, ' '.join(pages))) == expected_gaps, (slug, 'gap count')
    geometry = audit_blank_geometry(path, units, supplements)
    assert geometry['count'] == expected_gaps, (slug, 'printed gap count')
    return dict(slug=slug, pages=len(pages), sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                extended_dialogues=len(units) + len(supplements),
                transfer_dialogues=len(units) + len(supplements),
                embedded_font_instances=font_count, internal_links=internal_links,
                external_links=external_links, printed_blanks=geometry,
                structural_status='passed')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('slugs', nargs='*')
    parser.add_argument('--published', action='store_true', help='Audit the current public downloads instead of the master files.')
    args = parser.parse_args()
    tracks = [track for track in load_tracks() if not args.slugs or track['slug'] in args.slugs]
    assert tracks and (not args.slugs or len(tracks) == len(set(args.slugs)))
    report = dict(scope='Structural checks only; see books/AUDIT-2026-10.md for editorial review.',
                  published=args.published, books=[], failures=[])
    for track in tracks:
        try:
            result = audit(track, args.published)
            report['books'].append(result)
            print(track['slug'] + ': passed', flush=True)
        except Exception as error:
            failure = dict(slug=track['slug'], error=repr(error))
            report['failures'].append(failure)
            print(json.dumps(failure), flush=True)
    directory = ROOT / 'tmp/pdfs/audit'
    directory.mkdir(parents=True, exist_ok=True)
    label = 'published' if args.published else 'revised'
    if args.slugs:
        label += '-' + '-'.join(args.slugs)
    (directory / (label + '.json')).write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(dict(passed=len(report['books']), failed=len(report['failures']))))
    raise SystemExit(bool(report['failures']))


if __name__ == '__main__':
    main()
