"""Validate current book content, PDF typography, navigation and revision records."""
import argparse
import hashlib
import json
from pathlib import Path
import re

import pdfplumber
from pypdf import PdfReader

from build_revised_books import configure
from books.revised_edition import inventory
from revised_book_records import stem, verify_record

ROOT = Path(__file__).resolve().parent


def normalized(text):
    return ' '.join(re.sub(r'(?<=\w)-\s+(?=\w)', '-', text).split())


def audit_heading_records(layout):
    assert layout['headingErrors'] == [], 'Continuation heading formatting changed'
    letters = {item['id']: item for item in layout['sectionLetters']}
    assert len(letters) == len(layout['sectionLetters'])
    assert letters, 'No section-letter styling records'
    for item in layout['continuationHeadings']:
        source = letters.get(item['source'])
        expected = source['letter'] if source else None
        assert item['letter'] == expected, (item['id'], 'Missing continuation letter')
        if source:
            current = letters[item['id']]
            assert current['page'] == item['page']
            for key in ('letter', 'width', 'height', 'color'):
                assert current[key] == source[key], (item['id'], 'Changed letter styling', key)
    return letters


def audit_printed_letter(page, letter):
    # Browser coordinates are CSS pixels; PDF coordinates are points (3/4 px).
    x, y, width, height = (letter[key] * .75 for key in ('x', 'y', 'width', 'height'))
    color = tuple(int(n) / 255 for n in re.findall(r'\d+', letter['color']))
    circles = [curve for curve in page.curves if curve['fill'] and
               all(abs(curve[key] - value) < .8 for key, value in
                   [('x0', x), ('top', y), ('width', width), ('height', height)])]
    assert any(len(curve.get('non_stroking_color', ())) == 3 and
               all(abs(a - b) < .001 for a, b in zip(curve['non_stroking_color'], color))
               for curve in circles), (letter['id'], 'Missing printed circle')
    chars = [char for char in page.chars if x <= char['x0'] <= char['x1'] <= x + width and
             y <= char['top'] <= char['bottom'] <= y + height]
    assert ''.join(char['text'] for char in chars) == letter['letter'], (letter['id'], 'Missing printed letter')
    assert all(char['non_stroking_color'] == (1, 1, 1) for char in chars), (letter['id'], 'Letter is not white')


def audit(slug, staged=False, published=False, geometry=True):
    meta = verify_record(slug, staged)
    book = configure(slug)
    units, supplements = book['units'], book['supplements']
    name = stem(slug, staged)
    pdf = ROOT / ('pdf/efsp' if published else 'output/pdf') / (stem(slug) + '.pdf' if published else name + '.pdf')
    assert hashlib.sha256(pdf.read_bytes()).hexdigest() == meta['sha256'], (slug, 'published bytes')
    layout = json.loads((ROOT / 'output/pdf' / (name + '-layout.json')).read_text())
    assert not any(layout[key] for key in ('overflows', 'invalidLinks', 'duplicateIds')), slug
    letters = audit_heading_records(layout)
    reader = PdfReader(pdf)
    assert len(reader.pages) == meta['pdf_pages'] == layout['pages']
    assert reader.metadata.author == 'Phil Stilwell'
    root = reader.trailer['/Root']
    assert root['/Lang'] == 'en-US' and root['/StructTreeRoot'] and root['/MarkInfo']['/Marked']
    assert reader.outline and meta['cover_resolution_dpi'] >= 300
    pages = [normalized(page.extract_text() or '') for page in reader.pages]
    all_text = ' '.join(pages)
    destinations = reader.named_destinations
    fonts, links = set(), 0
    for number, (page, text) in enumerate(zip(reader.pages, pages), 1):
        assert abs(float(page.mediabox.width) - 612) < .01 and abs(float(page.mediabox.height) - 792) < .01
        assert 'English Ladder' in text and text.count('ENGLISHLADDER.COM') == 1, (slug, number, 'brand')
        assert f'Phil Stilwell | {number:02d}' in text, (slug, number, 'footer')
        assert len(text.split()) > 25, (slug, number, 'sparse page')
        assert not re.search(r'\{\{\d+\}\}|\ufffd|approval draft|think about it', text, re.I), (slug, number)
        for reference in page['/Resources'].get('/Font', {}).get_object().values():
            font = reference.get_object()
            fonts.add(str(font['/BaseFont']))
            for descendant in font.get('/DescendantFonts', [font]):
                descriptor = descendant.get_object().get('/FontDescriptor')
                assert descriptor and any(k in descriptor.get_object() for k in ('/FontFile', '/FontFile2', '/FontFile3')), (slug, number, 'unembedded font')
        key_pages = set()
        for reference in page.get('/Annots', []):
            annotation = reference.get_object()
            destination = annotation.get('/Dest', annotation.get('/A', {}).get('/D'))
            if destination:
                assert str(destination) in destinations, (slug, number, destination)
                target = reader.get_destination_page_number(destinations[str(destination)]) + 1
                assert 1 <= target <= len(pages)
                links += 1
                if str(destination).startswith('/key-'):
                    key_pages.add(target)
        printed = {int(n) for n in re.findall(r'(?:Answers and explanations|Why these answers fit), page (\d+)', text)}
        if printed:
            assert printed == key_pages, (slug, number, 'answer page mismatch', printed, key_pages)
    for anchor, page in meta['page_map'].items():
        if '/' + anchor in destinations:
            assert reader.get_destination_page_number(destinations['/' + anchor]) + 1 == page, (slug, anchor)

    def printed(value):
        assert normalized(value) in all_text, (slug, 'missing printed content', value[:160])

    questions = []
    for unit in units:
        for entry in unit['vocabulary']:
            for part in entry:
                printed(part)
        for _, phrase in unit['phrases']:
            printed(phrase)
        questions.extend(q for group in ('checks', 'choices', 'repair') for q in unit[group])
        questions.append(unit['second_take'])
    questions.extend(q for c in book['checkpoints'] for q in c['questions'])
    assert len(questions) == 96
    for q in questions:
        for part in [q['prompt'], *q['options'], *q['reasons']]:
            printed(part)
    scenes = units + supplements + [u['transfer'] for u in units] + [s['pilot_transfer'] for s in supplements]
    expected_gaps = sum(len(s['gaps']) for s in scenes)
    assert expected_gaps == layout['blankCount'] == 142
    assert abs(layout['maxBlankWidth'] - layout['minBlankWidth']) < .01
    for scene in scenes:
        for gap in scene['gaps']:
            printed(gap['answer'])
            printed(gap['reason'])
    from books.leadership_pilot import COPYRIGHT
    printed(COPYRIGHT)
    printed('No part of this publication may be reproduced')
    if geometry:
        blanks = 0
        letters_by_page = {item['page']: item for item in letters.values()}
        with pdfplumber.open(pdf) as document:
            for page in document.pages:
                if page.page_number in letters_by_page:
                    audit_printed_letter(page, letters_by_page[page.page_number])
                for char in page.chars:
                    assert 36 <= char['x0'] <= char['x1'] <= 576, (slug, page.page_number, 'horizontal bounds', char['text'])
                    assert 18 <= char['top'] <= char['bottom'] <= 774, (slug, page.page_number, 'vertical bounds', char['text'])
                    assert char['size'] >= 7, (slug, page.page_number, 'small text')
                # Chromium snaps border edges to device pixels (up to 0.75 pt).
                blanks += sum(abs(rect['width'] - 100) < .6 and .3 < rect['height'] < 1.5
                              and len(rect.get('non_stroking_color', ())) == 3
                              and abs(rect['non_stroking_color'][0] - 39 / 255) < .001
                              for rect in page.rects)
                if page.page_number == 1:
                    art = max(page.images, key=lambda img: img['width'])
                    assert art['srcsize'][0] / (art['width'] / 72) >= 299.9
                page.close()
        assert blanks == expected_gaps, (slug, 'drawn blank count', blanks, expected_gaps)
    return dict(slug=slug, pages=len(pages), sha256=meta['sha256'], questions=96,
                extended_dialogues=11, dialogue_turns=220, blanks=expected_gaps,
                section_letters=len(letters), continuation_headings=len(layout['continuationHeadings']),
                embedded_fonts=len(fonts), internal_links=links, geometry_checked=geometry, status='passed')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('slugs', nargs='*')
    parser.add_argument('--staged', action='store_true')
    parser.add_argument('--published', action='store_true')
    parser.add_argument('--quick', action='store_true', help='Skip the PDF character and rule geometry pass.')
    args = parser.parse_args()
    results, failures = [], []
    for slug in args.slugs or ['cultural-leadership-us-branches', *inventory()]:
        try:
            result = audit(slug, args.staged, args.published, not args.quick)
            results.append(result)
            print(json.dumps(result), flush=True)
        except Exception as error:
            failures.append(dict(slug=slug, error=repr(error)))
            print(json.dumps(failures[-1]), flush=True)
    folder = ROOT / 'tmp/pdfs/revised-audit'
    folder.mkdir(parents=True, exist_ok=True)
    label = 'staged' if args.staged else 'published' if args.published else 'canonical'
    (folder / (label + '.json')).write_text(json.dumps(dict(results=results, failures=failures), indent=2) + '\n')
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
