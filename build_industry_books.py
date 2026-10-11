"""Render authored English for Work books using the approved learner-book design.

Run with one or more course slugs, or --all after every source is complete.
Existing published PDF downloads are deliberately left unchanged.
"""
from __future__ import annotations

import argparse
import html
import importlib
import json
import re
from pathlib import Path

from PIL import Image
from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader

import build_leadership_book as design
from books.cross_cultural_leadership_content import AUTHOR, COPYRIGHT, REPRODUCTION_NOTICE, EDITION
from work_curriculum import load_tracks
from work_icons import icon_asset, icon_bottom_trim, icon_right_trim

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output/pdf'


def load_book(slug):
    module = importlib.import_module('books.' + slug.replace('-', '_') + '_content')
    return module.BOOK


def validate_book(book, track):
    assert book['slug'] == track['slug']
    assert book['title'] == track['title']
    units = book['units']
    design.validate_content(units, [m['title'] for m in track['modules']])
    assert len({u['scene'] for u in units}) == 8
    assert len({u['skill'] for u in units}) == 8
    assert len({t.casefold() for u in units for t, _, _ in u['vocabulary']}) >= 144
    assert len(book['field_notes']) == 4 and 2 <= len(book['sources']) <= 4
    for i, u in enumerate(units):
        assert 220 <= sum(len(line.split()) for _, line in u['dialogue']) <= 520, (i, 'dialogue length')
        assert [len(u[k]) for k in ('language', 'language_extra', 'rehearsal')] == [3, 3, 3]
        numbers = re.findall(r'\{\{(\d+)\}\}', ' '.join(line for _, line in u['dialogue']))
        assert numbers == [str(n) for n in range(1, 11)]
        assert all(q['prompt'].count('___') == 1 for q in u['transfer']['lines'])
        assert len({q['options'][q['answer']] for q in u['transfer']['lines']}) == 4
        assert all(len(g['reason'].split()) >= 8 for g in u['gaps'])
        assert all(len(q['reason'].split()) >= 8 for q in u['a'] + u['d'] + u['transfer']['lines'])
        assert not re.search(r'write (?:an? |your )|think about|consider how|invent your', ' '.join(u['rehearsal']), re.I)
    for source in book['sources']:
        assert source['url'].startswith('https://') and source['checked']


def illustration(b):
    asset, cols, rows, index = icon_asset(b.slug)
    with Image.open(ROOT / asset) as atlas:
        cw, ch = atlas.width / cols, atlas.height / rows
        left, top = index % cols * cw, index // cols * ch
        cell = atlas.crop((round(left), round(top), round(left + cw), round(top + ch)))
        right_trim = icon_right_trim(b.slug) * 160 / 104
        bottom_trim = icon_bottom_trim(b.slug) * 160 / 104
        b.c.saveState()
        if right_trim or bottom_trim:
            clip = b.c.beginPath()
            clip.rect(design.RIGHT - 163, 352 + bottom_trim, 160 - right_trim, 160 - bottom_trim)
            b.c.clipPath(clip, stroke=0, fill=0)
        b.c.drawImage(ImageReader(cell), design.RIGHT - 163, 352, 160, 160, mask='auto')
        b.c.restoreState()


def front(b, book):
    b.new_page('Learner book', anchor='cover')
    b.y -= 30
    b.text(book['cover_label'].upper(), size=9, leading=13, color=b.accent, bold=True, after=24)
    title = design.esc(book['cover_title']).replace('\n', '<br/>')
    b.text(title + f'<br/><font color="{b.accent}">English</font>', rich=True,
           size=book.get('cover_size', 34), leading=book.get('cover_size', 34) + 7, bold=True, after=20)
    b.text(book['tagline'], size=17, leading=23, color=b.accent, width=340, after=20)
    if b.y < 435:
        raise ValueError('Cover title or tagline needs shortening: ' + b.slug)
    illustration(b)
    b.y = 408
    b.text(AUTHOR, size=15, leading=20, bold=True, after=6, width=325)
    b.text(COPYRIGHT, size=8.2, leading=12, color=design.MUTED, after=4, width=325)
    b.text(REPRODUCTION_NOTICE, size=8, leading=11, color=design.MUTED, after=0, width=325)
    b.y = 306
    b.rule(18)
    b.text('Eight lessons. Eleven extended conversations.', size=15, leading=21, bold=True, after=18)
    b.panel('Inside the book', '192 vocabulary entries  /  128 reusable phrases\n220 extended-dialogue turns  /  11 transfer exchanges\nWord banks and explained answer keys', size=11, leading=17)
    b.text('Upper-intermediate to advanced (B2-C1). ' + book['audience'], size=10, leading=15, color=design.MUTED, after=12)
    b.text(EDITION, size=8.3, leading=12, color=design.MUTED)

    b.new_page('Book map', 'Eight scenarios. Eight skills.', anchor='contents')
    b.text(book['map_intro'], after=18)
    for i, u in enumerate(b.units):
        top = b.y
        b.text(f'{i + 1:02d}  {u["title"]}', size=10.5, leading=14, bold=True, after=4, width=design.WIDTH - 36)
        b.text(u['scene'] + '  |  ' + u['skill'], size=8.8, leading=12,
               width=design.WIDTH - 42, color=design.MUTED, after=10)
        b.c.setFont('BookBold', 11)
        b.c.setFillColor(colors.HexColor(design.ACCENTS[i]))
        b.c.drawRightString(design.RIGHT, top - 11, str(design.unit_page(i)))
        b.c.linkRect('', f'unit-{i + 1}', (design.LEFT, b.y + 4, design.RIGHT, top), relative=0, thickness=0)
    b.rule()
    for label, page, anchor in [('Communication field notes', 3, 'culture'),
                                ('Three more workplace conversations', design.SUPPLEMENT_START, 'additional-1'),
                                ('Answers and explanations', design.KEY_START, 'key-1-checks'),
                                ('Fast-access phrase pages', design.PHRASES_START, 'quick-phrases'),
                                ('Vocabulary index', design.INDEX_START, 'index'),
                                ('Sources and publication notes', design.SOURCES_PAGE, 'sources')]:
        top = b.y
        b.text(label, size=9.4, leading=13, after=5)
        b.c.setFont('Book', 9.4)
        b.c.drawRightString(design.RIGHT, top - 10, str(page))
        b.c.linkRect('', anchor, (design.LEFT, b.y, design.RIGHT, top), relative=0, thickness=0)

    b.new_page('Communication field notes', book['notes_title'], anchor='culture')
    b.text(book['notes_intro'], size=11, leading=16, after=18)
    for label, explanation, example in book['field_notes']:
        b.text(label, size=12, leading=16, bold=True, color=b.accent, after=7)
        b.text(explanation, size=10.3, leading=15, after=7)
        b.text(example, size=10, leading=14, after=18)
    b.panel('Professional boundaries', book['scope_note'], size=9.5, leading=13.5)


def sources(b, book):
    b.new_page('Sources and publication notes', 'Original cases. Clear boundaries.', anchor='sources')
    b.text('These are original fictional teaching conversations, not transcripts of real workers. Names, figures, organizations, and incidents are invented. Sources support terminology and communication aims, not the fictional results or an endorsement of this book.', size=10.2, leading=14.5, after=16)
    for i, source in enumerate(book['sources'], 1):
        b.text(f'[{i}] {source["title"]}', size=10, leading=14, bold=True, after=5)
        b.text(f'<link href="{html.escape(source["url"], quote=True)}" color="{b.accent}">Open the original source</link>', rich=True, size=9.4, leading=13, after=5)
        b.text(source['note'] + ' Checked ' + source['checked'] + '.', size=9.3, leading=13, after=15)
    b.rule(14)
    b.text(AUTHOR, size=12, leading=16, bold=True, after=6)
    b.text(COPYRIGHT, size=9.4, leading=13.5, after=6)
    b.text(REPRODUCTION_NOTICE, size=9.4, leading=13.5, after=12)
    b.text(book['scope_note'], size=9.4, leading=13.5, after=12)
    b.text('English Ladder | English for Work | ' + EDITION + '. The B2-C1 range is an editorial study recommendation, not a proficiency certification.', size=9, leading=13, after=12)
    b.text(f'<link href="https://englishladder.com/efsp-{b.slug}.html" color="{b.accent}">Open the matching English Ladder course</link>', rich=True, size=10, leading=14)


def build(slug):
    book = load_book(slug)
    track = next(t for t in load_tracks() if t['slug'] == slug)
    validate_book(book, track)
    out = OUT / f'{slug}-english-book.pdf'
    b = design.Book(title=book['title'], slug=slug, units=book['units'], out=out)
    b.key_gap_spacing = 6
    b.bank_seed = slug
    front(b, book)
    for i, unit in enumerate(b.units):
        assert b.page + 1 == design.unit_page(i)
        design.briefing(b, unit, i)
        for part in range(2):
            design.vocabulary(b, unit, i, part)
        for part in range(2):
            design.language(b, unit, i, part)
        design.checks(b, unit, i)
        design.dialogue(b, unit, i)
        design.dialogue(b, unit, i, second=True)
        design.transfer(b, unit, i)
    for i, unit in enumerate(b.supplements):
        assert b.page + 1 == design.supplement_page(i)
        design.additional_conversation(b, unit, i)
    for i, unit in enumerate(b.units):
        assert b.page + 1 == design.key_page(i)
        design.explanations(b, unit, i)
    for i, unit in enumerate(b.supplements):
        assert b.page + 1 == design.SUPPLEMENT_KEYS_START + i
        design.additional_answers(b, unit, i)
    assert b.page + 1 == design.PHRASES_START
    design.reference(b)
    assert b.page + 1 == design.SOURCES_PAGE
    sources(b, book)
    assert b.page == design.TOTAL_PAGES
    b.save()
    reader = PdfReader(out)
    assert len(reader.pages) == design.TOTAL_PAGES
    assert all('English Ladder' in p.extract_text() for p in reader.pages)
    return dict(slug=slug, title=book['title'], pages=b.page, path=str(out), bytes=out.stat().st_size)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('slugs', nargs='*')
    parser.add_argument('--all', action='store_true')
    args = parser.parse_args()
    slugs = [t['slug'] for t in load_tracks()[1:]] if args.all else args.slugs
    if not slugs:
        parser.error('Supply course slugs or --all.')
    missing = [slug for slug in slugs if not (ROOT / 'books' / (slug.replace('-', '_') + '_content.py')).exists()]
    if missing:
        parser.error('Books still requiring authored content: ' + ', '.join(missing))
    for slug in slugs:
        print(json.dumps(build(slug)), flush=True)
