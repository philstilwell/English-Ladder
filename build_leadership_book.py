"""Build the standalone learner book without changing published course downloads.

Run: python3 build_leadership_book.py
Uses the existing embedded fonts and course illustration. No paid services.
"""
from __future__ import annotations

import html
import hashlib
import json
import math
import re
from collections import defaultdict
from itertools import combinations
from pathlib import Path

from PIL import Image
from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph

from books.cross_cultural_leadership_content import (
    TITLE, EDITION, AUTHOR, COPYRIGHT, REPRODUCTION_NOTICE, SLUG, UNITS, WEB_ORDER,
)
from work_icons import icon_asset

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output/pdf/cross-cultural-leadership-english-book.pdf'
W, H = 612, 792
LEFT, RIGHT, BOTTOM = 46, 566, 54
WIDTH = RIGHT - LEFT
INK = '#22243A'
MUTED = '#565B70'
LINE = '#DCE0ED'
PAPER = '#F2F4FC'
ACCENTS = ['#294EDB', '#984261', '#4857A6', '#895E10', '#5B4BB2', '#854B96', '#315EB3', '#A24738']
FRONT_PAGES = 3
UNIT_PAGES = 9
KEY_START = FRONT_PAGES + len(UNITS) * UNIT_PAGES + 1
PHRASES_START = KEY_START + len(UNITS) * 2
INDEX_START = PHRASES_START + 2
INDEX_PAGES = math.ceil(sum(len(u['vocabulary']) for u in UNITS) / 24)
SOURCES_PAGE = INDEX_START + INDEX_PAGES
TOTAL_PAGES = SOURCES_PAGE

for name, file in [('Book', 'Vera.ttf'), ('BookBold', 'VeraBd.ttf'), ('BookItalic', 'VeraIt.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(ROOT / 'assets/fonts' / file)))
pdfmetrics.registerFontFamily('Book', normal='Book', bold='BookBold', italic='BookItalic', boldItalic='BookBold')


def esc(text):
    return html.escape(str(text), quote=False)


def paragraph(text, width, size=10.5, leading=15, color=INK, bold=False):
    p = Paragraph(text, ParagraphStyle('p', fontName='BookBold' if bold else 'Book',
                  fontSize=size, leading=leading, textColor=colors.HexColor(color),
                  allowWidows=0, allowOrphans=0, spaceAfter=0))
    _, height = p.wrap(width, 1000)
    return p, height


def blank(number, answer, accent, size=10):
    """Keep each gap number attached and leave enough space for its phrase."""
    answer_width = pdfmetrics.stringWidth(answer, 'Book', size)
    count = max(11, math.ceil(answer_width * 1.15 / pdfmetrics.stringWidth('_', 'Book', size)))
    return f'<super><font size="6.5" color="{accent}">{number}</font></super>&nbsp;' + '_' * count


def unit_page(index):
    return FRONT_PAGES + 1 + index * UNIT_PAGES


def key_page(index, conversation=False):
    return KEY_START + index * 2 + int(conversation)


def content_hash():
    return hashlib.sha256(json.dumps(UNITS, sort_keys=True).encode('utf-8')).hexdigest()


def validate_layout(boxes):
    by_page = defaultdict(list)
    for box in boxes:
        assert box['bottom'] >= BOTTOM - .1, box
        assert LEFT <= box['x'] and box['x'] + box['width'] <= RIGHT + .1, box
        by_page[box['page']].append(box)
    for page, page_boxes in by_page.items():
        for a, b in combinations(page_boxes, 2):
            horizontal = min(a['x'] + a['width'], b['x'] + b['width']) - max(a['x'], b['x'])
            vertical = min(a['top'], b['top']) - max(a['bottom'], b['bottom'])
            assert horizontal <= .5 or vertical <= .5, (page, a['text'], b['text'])


def validate_content():
    assert len(UNITS) == 8
    assert [u['title'] for u in UNITS] == WEB_ORDER
    for i, u in enumerate(UNITS, 1):
        assert len(u['dialogue']) == 20, i
        assert len(u['gaps']) == 10, i
        assert len(u['vocabulary']) == 24 and len(u['phrases']) == 16, i
        assert len({t.lower() for t, _, _ in u['vocabulary']}) == 24, i
        assert len({phrase for _, phrase in u['phrases']}) == 16, i
        assert len(u['language_extra']) == 3 and u['precision_extra'], i
        assert [len(u[k]) for k in ('a', 'd')] == [3, 4], i
        assert len(u['transfer']['lines']) == 4, i
        assert len({g['answer'].lower() for g in u['gaps']}) == 10, i
        all_numbers = []
        cast = {name for name, _ in u['cast']}
        for turn, (speaker, text) in enumerate(u['dialogue'], 1):
            assert speaker in cast, (i, speaker)
            for n in re.findall(r'\{\{(\d+)\}\}', text):
                all_numbers.append(int(n))
                assert u['gaps'][int(n) - 1]['turn'] == turn, (i, turn, n)
        assert sorted(all_numbers) == list(range(1, 11)), (i, all_numbers)
        for q in u['a'] + u['d'] + u['transfer']['lines']:
            assert len(q['options']) == 4 and len(set(q['options'])) == 4, q
            assert 0 <= q['answer'] < 4 and q['reason'], q


class Book:
    def __init__(self):
        OUT.parent.mkdir(parents=True, exist_ok=True)
        self.c = Canvas(str(OUT), pagesize=(W, H), initialFontName='Book', invariant=1)
        self.c.setTitle(TITLE + ' | Learner book')
        self.c.setAuthor(AUTHOR)
        self.c.setCreator('English Ladder')
        self.c.setSubject('Eight workplace scenarios, vocabulary, phrases, and structured practice. Content SHA-256: ' + content_hash())
        self.c.setKeywords('English Ladder, international managers, workplace English, cross-cultural leadership, B2, C1')
        self.page = 0
        self.y = 0
        self.accent = ACCENTS[0]
        self.boxes = []

    def new_page(self, section, title='', unit=None, anchor=None):
        if self.page:
            self.c.showPage()
        self.page += 1
        c = self.c
        self.accent = ACCENTS[unit % 8] if unit is not None else ACCENTS[0]
        c.setFillColor(colors.HexColor(self.accent))
        c.rect(0, H - 7, W, 7, fill=1, stroke=0)
        c.drawImage(str(ROOT / 'assets/brand/ladder-mark.png'), LEFT, H - 40, 19, 19, mask='auto')
        c.setFont('BookBold', 9)
        c.setFillColor(colors.HexColor(INK))
        c.drawString(LEFT + 26, H - 33, 'English Ladder')
        c.setFont('Book', 8)
        c.setFillColor(colors.HexColor(MUTED))
        c.drawRightString(RIGHT, H - 32, 'ENGLISH FOR WORK  /  ' + section.upper())
        c.setStrokeColor(colors.HexColor(LINE))
        c.line(LEFT, 39, RIGHT, 39)
        c.setFont('Book', 7.3)
        c.drawString(LEFT, 25, 'Cross-Cultural Leadership English')
        c.drawRightString(RIGHT, 25, f'Phil Stilwell  |  {self.page:02d}')
        self.y = H - 62
        if anchor:
            c.bookmarkPage(anchor)
            c.addOutlineEntry(title or section, anchor, level=0)
        if unit is not None:
            c.setFillColor(colors.HexColor(self.accent))
            c.rect(RIGHT + 18, H - 80 - unit * 23, 28, 22, fill=1, stroke=0)
            c.setFont('BookBold', 8)
            c.setFillColor(colors.white)
            c.drawCentredString(RIGHT + 31, H - 73 - unit * 23, f'{unit + 1:02d}')
        if title:
            self.text(title, size=23, leading=28, bold=True, after=15)

    def text(self, text, size=10.5, leading=15, color=INK, bold=False, after=8,
             x=LEFT, width=WIDTH, rich=False):
        return self.block(text if rich else esc(text), x, self.y, width, size, leading, color, bold, after)

    def block(self, text, x, top, width, size=10.5, leading=15, color=INK,
              bold=False, after=0, track=True):
        p, height = paragraph(text, width, size, leading, color, bold)
        if top - height < BOTTOM - .1:
            raise ValueError(f'Page {self.page} overflows by {BOTTOM - top + height:.1f} pt: {text[:100]}')
        p.drawOn(self.c, x, top - height)
        if track:
            self.boxes.append(dict(page=self.page, text=re.sub('<[^>]+>', '', text)[:80],
                                   x=x, top=top, width=width, bottom=top - height))
        self.y = top - height - after
        return height

    def label(self, letter, title):
        c = self.c
        c.setFillColor(colors.HexColor(self.accent))
        c.circle(LEFT + 12, self.y - 12, 12, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont('BookBold', 11)
        c.drawCentredString(LEFT + 12, self.y - 16, letter)
        self.block(esc(title), LEFT + 35, self.y - 3, WIDTH - 35, 12.3, 17,
                   self.accent, True, 0)
        self.y -= 15

    def panel(self, label, text, fill=PAPER, size=10.2, leading=14.5, after=14):
        rich = esc(text).replace('\n', '<br/>')
        body, h = paragraph(rich, WIDTH - 28, size, leading)
        height = h + 40
        top = self.y
        if top - height < BOTTOM:
            raise ValueError(f'Panel overflow page {self.page}: {label}')
        c = self.c
        c.setFillColor(colors.HexColor(fill))
        c.rect(LEFT, top - height, WIDTH, height, fill=1, stroke=0)
        self.block(esc(label.upper()), LEFT + 14, top - 11, WIDTH - 28,
                   8, 11, self.accent, True)
        self.block(rich, LEFT + 14, top - 29, WIDTH - 28, size, leading)
        self.y = top - height - after

    def rule(self, gap=12):
        self.c.setStrokeColor(colors.HexColor(LINE))
        self.c.line(LEFT, self.y, RIGHT, self.y)
        self.y -= gap

    def mcq(self, number, q, size=10.3, after=12, compact=False):
        self.text(f'<b>{number}.</b> {esc(q["prompt"])}', rich=True, size=size, leading=14.2, after=6)
        if compact:
            col_width = (WIDTH - 28) / 2
            for row in range(2):
                top = self.y
                bottoms = []
                for col in range(2):
                    index = row * 2 + col
                    self.block(f'<b>{chr(65 + index)}</b>  {esc(q["options"][index])}',
                               LEFT + 13 + col * (col_width + 15), top, col_width,
                               size=9.3, leading=13, after=5)
                    bottoms.append(self.y)
                self.y = min(bottoms)
            self.y -= after
            return
        for index, choice in enumerate(q['options']):
            self.text(f'<b>{chr(65 + index)}</b>  {esc(choice)}', rich=True, size=9.7, leading=13.2,
                      x=LEFT + 13, width=WIDTH - 13, after=3)
        self.y -= after

    def bank(self, answers, small=False):
        order = ([5, 2, 8, 0, 9, 4, 7, 1, 6, 3] if len(answers) == 10 else [2, 0, 3, 1])
        words = '   /   '.join(answers[n] for n in order)
        self.panel('Word + phrase bank', words, size=10 if small else 10.5, leading=15, after=12)

    def answer_strip(self, answers, unit, bottom=False):
        text = '   |   '.join(f'{i}. {answer}' for i, answer in enumerate(answers, 1))
        p, h = paragraph(esc(text), WIDTH - 24, 8.8, 12.5)
        height = h + 30
        top = BOTTOM + height if bottom else self.y
        if bottom and self.y < top + 8:
            raise ValueError(f'Answer strip collides with dialogue on page {self.page}')
        self.c.setFillColor(colors.HexColor('#F5F0DF'))
        self.c.rect(LEFT, top - height, WIDTH, height, fill=1, stroke=0)
        self.block(f'ANSWERS  /  EXPLANATIONS: PAGE {key_page(unit, True)}', LEFT + 12, top - 8,
                   WIDTH - 24, 7.2, 10, '#765514', True)
        self.c.linkRect('', f'key-{unit + 1}-conversations',
                        (LEFT + 12, top - 20, RIGHT - 12, top - 7), relative=0, thickness=0)
        self.block(esc(text), LEFT + 12, top - 23, WIDTH - 24, 8.8, 12.5)
        self.y = top - height - 15

    def answer_link(self, unit):
        top = self.y
        self.text(f'Answers and explanations: page {key_page(unit)}.',
                  size=9.5, leading=14, color=self.accent, after=8)
        self.c.linkRect('', f'key-{unit + 1}-checks',
                        (LEFT, self.y + 8, RIGHT, top), relative=0, thickness=0)

    def save(self):
        validate_layout(self.boxes)
        self.c.save()
        qa = ROOT / 'tmp/pdfs/leadership-book-layout.json'
        qa.parent.mkdir(parents=True, exist_ok=True)
        qa.write_text(json.dumps(dict(pages=self.page, boxes=self.boxes), indent=2))


def front(b):
    b.new_page('Learner book', anchor='cover')
    b.y -= 35
    b.text('INTERNATIONAL MANAGERS  /  US WORKPLACES', size=9, leading=13, color=b.accent, bold=True, after=25)
    b.text(f'Cross-Cultural<br/>Leadership<br/><font color="{b.accent}">English</font>', rich=True, size=39, leading=46, bold=True, after=25)
    b.text('Clear language for decisive,<br/>respectful leadership.', rich=True, size=18, leading=25,
           color=b.accent, after=30)
    asset, cols, rows, index = icon_asset(SLUG)
    with Image.open(ROOT / asset) as atlas:
        cell_w, cell_h = atlas.width / cols, atlas.height / rows
        left, top = (index % cols) * cell_w, (index // cols) * cell_h
        cell = atlas.crop((round(left), round(top), round(left + cell_w), round(top + cell_h)))
        b.c.drawImage(ImageReader(cell), RIGHT - 163, 352, 160, 160, mask='auto')
    b.y = 408
    b.text(AUTHOR, size=15, leading=20, bold=True, after=6, width=325)
    b.text(COPYRIGHT, size=8.2, leading=12, color=MUTED, after=4, width=325)
    b.text(REPRODUCTION_NOTICE, size=8, leading=11, color=MUTED, after=0, width=325)
    b.y = 306
    b.rule(18)
    b.text('Eight scenarios. Eight extended conversations.',
           size=15, leading=21, bold=True, after=18)
    b.panel('Inside the book', '192 vocabulary entries  /  128 reusable phrases\n160 dialogue turns  /  80 numbered dialogue gaps\nWord banks and explained answer keys', size=11, leading=17)
    b.text('Upper-intermediate to advanced (B2-C1). For international managers, cross-border teams, and workplace English learners.',
           size=10, leading=15, color=MUTED, after=12)
    b.text(EDITION,
           size=8.3, leading=12, color=MUTED)

    b.new_page('Book map', 'Eight scenarios. Eight skills.', anchor='contents')
    b.text('Build the language of clear decisions, constructive disagreement, and trusted working relationships.', after=18)
    for i, unit in enumerate(UNITS):
        top = b.y
        b.text(f'{i + 1:02d}  {unit["title"]}', size=11.1, leading=15, bold=True, after=5)
        b.text(unit['scene'] + '  |  ' + unit['skill'], size=9, leading=12.5,
               width=WIDTH - 42, color=MUTED, after=13)
        b.c.setFont('BookBold', 11)
        b.c.setFillColor(colors.HexColor(ACCENTS[i]))
        b.c.drawRightString(RIGHT, top - 11, str(unit_page(i)))
        b.c.linkRect('', f'unit-{i + 1}', (LEFT, b.y + 7, RIGHT, top), relative=0, thickness=0)
    b.rule()
    for label, page, anchor in [('Directness, disagreement, and boundaries', 3, 'culture'),
                                ('Answers and explanations', KEY_START, 'key-1-checks'),
                                ('Fast-access phrase pages', PHRASES_START, 'quick-phrases'),
                                ('Vocabulary index', INDEX_START, 'index'),
                                ('Sources and publication notes', SOURCES_PAGE, 'sources')]:
        top = b.y
        b.text(label, size=9.4, leading=13, after=5)
        b.c.setFont('Book', 9.4)
        b.c.drawRightString(RIGHT, top - 10, str(page))
        b.c.linkRect('', anchor, (LEFT, b.y, RIGHT, top), relative=0, thickness=0)

    b.new_page('Cultural field notes', 'Direct is not the same as hostile.', anchor='culture')
    b.text('A colleague can strongly challenge an idea without disliking its author. A friendly manner can also hide a real objection. Words, follow-up behavior, power, and context matter more than nationality. Ask what a statement means before deciding what the speaker intended.', size=11, leading=16, after=16)
    b.panel('The practical distinction', 'Accept a testable challenge. Clarify an ambiguous message. Set a boundary around personal contempt, threats, or repeated interruption. You do not need to infer a hidden motive to name an observable problem.', size=10.3, leading=15)
    examples = [
        ('Strong task disagreement', '"I do not buy that estimate. The trial took twice as long."', 'Ask: "Which part of the trial is comparable, and what estimate does it support?"'),
        ('Ambiguous assent', '"Fine. Let us move on."', 'Check: "Does that approve the date, or only the approach? What remains conditional?"'),
        ('Personal disrespect', '"You clearly do not understand your job."', 'Set a limit: "Please address the evidence, not my competence. Which claim are you disputing?"'),
        ('Threat or intimidation', '"You will regret raising this."', 'Pause the exchange if needed. Use the appropriate workplace reporting or support route. An English exercise is not a substitute for a safety or conduct process.'),
    ]
    for label, phrase, response in examples:
        b.text(label, size=11, leading=15, bold=True, color=b.accent, after=4)
        b.text(phrase, size=10.3, leading=14.5, after=4)
        b.text(response, size=9.8, leading=14, after=15)
    b.rule()
    b.text('Check the local norm explicitly', size=12, leading=16, bold=True, after=8)
    b.text('First names do not remove decision authority. An invitation to debate is not a transfer of approval rights. Silence does not establish consent. "I will try" does not specify a deliverable. A private conversation does not remove the need for an accurate shared decision record.', size=10.2, leading=15, after=10)
    b.text('Communication practice, not a national personality guide: individuals and organizations vary. Psychological-safety research concerns whether teams can take interpersonal risks, such as asking questions; it does not require the absence of disagreement [3]. Language activities draw on interaction and mediation themes in the Common European Framework of Reference for Languages (CEFR) [1].', size=8.6, leading=12.3, color=MUTED)


def briefing(b, u, i):
    b.new_page(f'Lesson {i + 1:02d}', u['scene'], i, f'unit-{i + 1}')
    b.label('A', 'Read the situation')
    b.text(u['skill'], size=10.5, leading=15, bold=True, after=12)
    b.text(u['brief'], size=10.2, leading=14.5, after=11)
    b.text('PEOPLE  /  ' + '  |  '.join(f'{name}: {role}' for name, role in u['cast']), size=8.6, leading=12.5, color=MUTED, after=11)
    b.panel(*u['culture'], size=9.7, leading=13.5, after=13)
    b.text('Briefing checks', size=12, leading=16, bold=True, after=5)
    b.text('Circle one answer in each item. Use the briefing.', size=9.2, leading=13, color=MUTED, after=10)
    for number, q in enumerate(u['a'], 1):
        b.mcq(number, q, size=9.7, after=6, compact=True)
    b.answer_link(i)


def vocabulary(b, u, i, part=0):
    b.new_page(f'Lesson {i + 1:02d}', 'The vocabulary that does the work', i)
    b.c.bookmarkPage(f'vocabulary-{i + 1}-{part + 1}')
    b.label('B', f'Find the words  /  {part + 1} of 2')
    b.text('Read the definitions and say the common word combinations aloud.', size=10.1, leading=14.5, after=16)
    start = b.y
    col_width = (WIDTH - 28) / 2
    bottoms = []
    for col in range(2):
        b.y = start
        x = LEFT + col * (col_width + 28)
        offset = part * 12 + col * 6
        for term, meaning, collocation in u['vocabulary'][offset:offset + 6]:
            b.text(term, x=x, width=col_width, size=11.5, leading=15, bold=True, color=b.accent, after=5)
            b.text(meaning, x=x, width=col_width, size=10, leading=14.1, after=6)
            b.text('IN USE  ' + collocation, x=x, width=col_width, size=8.8, leading=12.5, bold=True, after=11)
            b.c.setStrokeColor(colors.HexColor(LINE))
            b.c.line(x, b.y + 5, x + col_width, b.y + 5)
        bottoms.append(b.y)
    if min(bottoms) < 126:
        raise ValueError(f'Vocabulary footer overlaps a column on page {b.page}')
    b.y = 119
    b.text('Precision check', size=10.5, leading=14, bold=True, color=b.accent, after=5)
    b.text(u['precision'] if part == 0 else u['precision_extra'], size=9.4, leading=13.5)


def language(b, u, i, part=0):
    b.new_page(f'Lesson {i + 1:02d}', 'Phrases you can actually use', i)
    b.label('C', f'Notice the language  /  {part + 1} of 2')
    b.y -= 10
    col_width = (WIDTH - 26) / 2
    for row in range(4):
        top = b.y
        bottoms = []
        for col in range(2):
            purpose, phrase = u['phrases'][part * 8 + row * 2 + col]
            x = LEFT + col * (col_width + 26)
            b.block(esc(purpose.upper()), x, top, col_width, 8, 11.2, b.accent, True)
            b.y -= 6
            b.text('"' + phrase + '"', x=x, width=col_width, size=10.6, leading=15, after=18)
            bottoms.append(b.y)
        b.y = min(bottoms)
    b.rule(16)
    for label, note in (u['language'] if part == 0 else u['language_extra']):
        b.text(label, size=10.7, leading=14.5, color=b.accent, bold=True, after=4)
        b.text(note, size=10, leading=14.5, after=13)


def checks(b, u, i):
    b.new_page(f'Lesson {i + 1:02d}', 'Choose the precise message', i)
    b.label('D', 'Check your understanding')
    b.text('Circle one best answer for each item. Use the stated purpose and case facts, not the option that merely sounds most polite.', size=10.3, leading=15, after=20)
    for number, q in enumerate(u['d'], 1):
        b.mcq(number, q, size=11, after=20)
    b.answer_link(i)


def dialogue(b, u, i, second=False):
    b.new_page(f'Lesson {i + 1:02d} / conversation', u['scene'] if not second else 'The conversation, continued', i)
    b.label('E', 'Conversations  /  ' + ('turns 11-20' if second else 'turns 1-10'))
    answers = [g['answer'] for g in u['gaps']]
    if not second:
        b.text('Complete the numbered gaps. Use each bank entry once, without changing its form. Cover the answers at the end until you finish.', size=9.2, leading=13, after=8)
        b.bank(answers, small=True)
    else:
        b.text(f'Continue with the word bank on page {unit_page(i) + 6}.', size=9.2, leading=13, after=15)
    start = 10 if second else 0
    for turn, (speaker, text) in enumerate(u['dialogue'][start:start + 10], start + 1):
        rich = re.sub(r'\{\{(\d+)\}\}', lambda m: blank(m[1], answers[int(m[1]) - 1], b.accent), esc(text))
        top = b.y
        b.block(f'{turn:02d}', LEFT, top - 1, 20, 7.7, 11, MUTED)
        b.block(f'<b>{esc(speaker)}:</b> {rich}', LEFT + 26, top, WIDTH - 26,
                size=10, leading=14, after=10)
    if second:
        b.answer_strip(answers, i, bottom=True)


def transfer(b, u, i):
    b.new_page(f'Lesson {i + 1:02d}', u['transfer']['title'], i)
    b.label('F', 'Say it')
    b.text(u['transfer']['setup'], size=10.5, leading=15, after=12)
    b.text('Complete the four gaps. Use each bank entry once.', size=9.7, leading=14, after=10)
    items = u['transfer']['lines']
    answers = [q['options'][q['answer']] for q in items]
    b.bank(answers)
    for n, q in enumerate(items, 1):
        prompt = esc(q['prompt']).replace('___', blank(n, answers[n - 1], b.accent, size=11))
        b.text(prompt, size=11, leading=16, after=15, rich=True)
    b.answer_strip(answers, i)
    b.text('Rehearse with a fixed script', size=13, leading=18, bold=True, after=10)
    for n, instruction in enumerate(u['rehearsal'], 1):
        b.text(f'{n}. {instruction}', size=10, leading=14.5, after=12)
    b.panel('Working alone', 'Read both roles, pausing for two seconds when the speaker changes. Repeat with the bank covered, then check any missed expressions.', size=9.5, leading=13.5)


def explanations(b, u, i):
    b.new_page(f'Answers / {i + 1:02d}', f'{i + 1:02d}  Briefing and language checks', i, f'key-{i + 1}-checks')
    b.text(u['title'], size=10.5, leading=15, color=b.accent, bold=True, after=17)
    for label, items, source_page in [('A  Briefing checks', u['a'], unit_page(i)),
                                      ('D  Language checks', u['d'], unit_page(i) + 5)]:
        b.text(f'{label}  /  page {source_page}', size=11, leading=15, bold=True, after=12)
        for n, q in enumerate(items, 1):
            b.text(f'<b>{n}.</b> {esc(q["prompt"])}', rich=True, size=9.5, leading=13.5, after=4)
            b.text(f'<b>{chr(65 + q["answer"])}. {esc(q["options"][q["answer"]])}</b><br/>'
                   + esc(q['reason']), rich=True, size=9.5, leading=13.5,
                   x=LEFT + 13, width=WIDTH - 13, after=13)
        b.y -= 4

    b.new_page(f'Answers / {i + 1:02d}', f'{i + 1:02d}  Conversation answers', i, f'key-{i + 1}-conversations')
    b.text(u['title'], size=10.5, leading=15, color=b.accent, bold=True, after=17)
    top = b.y
    col_width = (WIDTH - 26) / 2
    b.text('E  Dialogue gaps', width=col_width, size=11, leading=15, bold=True, after=5)
    b.text(f'Pages {unit_page(i) + 6}-{unit_page(i) + 7}', width=col_width,
           size=8.8, leading=12, color=MUTED, after=12)
    for n, g in enumerate(u['gaps'], 1):
        b.text(f'<b>{n}. {esc(g["answer"])}.</b> <font color="{MUTED}">Turn {g["turn"]}.</font> {esc(g["reason"])}',
               rich=True, width=col_width, size=9.2, leading=13.2, after=10)
    b.y = top
    x = LEFT + col_width + 26
    b.text('F  Transfer conversation', x=x, width=col_width, size=11, leading=15, bold=True, after=5)
    b.text(f'Page {unit_page(i) + 8}', x=x, width=col_width,
           size=8.8, leading=12, color=MUTED, after=12)
    for n, q in enumerate(u['transfer']['lines'], 1):
        answer = q['options'][q['answer']]
        b.text(f'<b>{n}. {esc(answer)}</b>', rich=True, x=x, width=col_width,
               size=9.2, leading=13.2, after=5)
        b.text(q['prompt'].replace('___', answer), x=x, width=col_width,
               size=9.2, leading=13.2, after=6)
        b.text(q['reason'], x=x, width=col_width, size=9.2, leading=13.2, after=16)


def reference(b):
    for half in range(2):
        b.new_page('Fast-access phrases', 'Find the move you need' if half == 0 else 'Keep the conversation productive',
                   anchor='quick-phrases' if half == 0 else None)
        b.text('Use these as precise language models. Replace details only when you know the actual facts, authority, and agreed conditions.', size=10.2, leading=14.5, after=18)
        for i in range(half * 4, half * 4 + 4):
            u = UNITS[i]
            b.accent = ACCENTS[i]
            b.text(f'{i + 1:02d}  {u["title"]}', size=12, leading=16, color=b.accent, bold=True, after=8)
            for purpose, phrase in [u['phrases'][0], u['phrases'][3], u['phrases'][7]]:
                b.text(f'<b>{esc(purpose)}:</b> {esc(phrase)}', rich=True, size=10.2, leading=15, after=8)
            b.text(f'Full phrase set: pages {unit_page(i) + 3}-{unit_page(i) + 4}  |  Dialogue: pages {unit_page(i) + 6}-{unit_page(i) + 7}',
                   size=8, leading=11, color=MUTED, after=18)
    entries = sorted([(term, i, n // 12, collocation) for i, u in enumerate(UNITS)
                      for n, (term, _meaning, collocation) in enumerate(u['vocabulary'])], key=lambda item: item[0].lower())
    for page in range(INDEX_PAGES):
        b.new_page('Vocabulary index', 'Find a term and its context', anchor='index' if page == 0 else None)
        b.text('The page number leads to the definition and a typical word combination. Repeated terms have separate entries when they serve different lesson contexts.', size=9.5, leading=13.5, after=20)
        for term, index, part, collocation in entries[page * 24:page * 24 + 24]:
            top = b.y
            b.text(f'<b>{esc(term)}</b>  <font color="{MUTED}">{esc(collocation)}</font>', rich=True,
                   width=WIDTH - 44, size=9.3, leading=13, after=8)
            b.c.setFont('BookBold', 9.3)
            b.c.setFillColor(colors.HexColor(ACCENTS[index]))
            b.c.drawRightString(RIGHT, top - 10, str(unit_page(index) + 1 + part))
            b.c.linkRect('', f'vocabulary-{index + 1}-{part + 1}', (LEFT, b.y + 2, RIGHT, top), relative=0, thickness=0)


def sources(b):
    b.new_page('Sources and publication notes', 'Original cases. Clear boundaries.', anchor='sources')
    b.text('The scenarios, dialogues, vocabulary explanations, tasks, and answer rationales are original English Ladder teaching material. They are not transcripts of real employees or research interviews. They illustrate language choices, not a universal American communication style.', size=10.5, leading=15, after=18)
    refs = [
        ('1', 'Council of Europe. Common European Framework of Reference for Languages: mediation resources.',
         'https://www.coe.int/en/web/common-european-framework-reference-languages/mediation',
         'Used for the broad learning aims of collaborative interaction, clarification, turn-taking, and helping people establish shared meaning. The B2-C1 study range is an editorial choice, not an official endorsement or assessment.'),
        ('2', 'Center for Creative Leadership. Use Situation-Behavior-Impact (SBI) to Understand Intent (2025).',
         'https://www.ccl.org/articles/leading-effectively-articles/closing-the-gap-between-intent-vs-impact-sbii/',
         'Informs the distinction between observed behavior, impact, and assumed intent in Lesson 6. SBI is attributed to its originator; the cases and dialogue wording here are original.'),
        ('3', 'Amy Edmondson. Psychological Safety and Learning Behavior in Work Teams (1999). Administrative Science Quarterly, 44(2), 350-383.',
         'https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f',
         'Provides background on interpersonal risk and team learning. The study does not establish national personality types, and this book does not treat its results as rules about individuals.'),
    ]
    for number, title, url, note in refs:
        b.text(f'[{number}] {title}', size=10.2, leading=14.5, bold=True, after=6)
        b.text(f'<link href="{html.escape(url, quote=True)}" color="{b.accent}">Open the original source</link>',
               rich=True, size=9.5, leading=13, after=7)
        b.text(note, size=9.5, leading=13.5, after=18)
    b.rule(15)
    b.text(AUTHOR, size=12, leading=16, bold=True, after=6)
    b.text(COPYRIGHT, size=9.4, leading=13.5, after=6)
    b.text(REPRODUCTION_NOTICE, size=9.4, leading=13.5, after=12)
    b.text('English Ladder | English for Work | ' + EDITION + '. References checked 30 September 2026. All characters, organizations, figures, and conversations are fictional.', size=9.4, leading=13.5, after=12)
    b.text('For workplace conduct, safety, employment, or legal questions, use the appropriate qualified support and current organizational procedures. Do not treat a successful language exercise as authorization for a real decision.', size=9.4, leading=13.5, after=12)
    url = f'https://englishladder.com/efsp-{SLUG}.html'
    b.text(f'<link href="{url}" color="{b.accent}">Open the matching English Ladder course</link>', rich=True, size=10, leading=14)


def build():
    validate_content()
    b = Book()
    front(b)
    for i, u in enumerate(UNITS):
        assert b.page + 1 == unit_page(i)
        briefing(b, u, i)
        vocabulary(b, u, i)
        vocabulary(b, u, i, part=1)
        language(b, u, i)
        language(b, u, i, part=1)
        checks(b, u, i)
        dialogue(b, u, i)
        dialogue(b, u, i, second=True)
        transfer(b, u, i)
    for i, u in enumerate(UNITS):
        assert b.page + 1 == key_page(i)
        explanations(b, u, i)
    assert b.page + 1 == PHRASES_START
    reference(b)
    assert b.page + 1 == SOURCES_PAGE
    sources(b)
    assert b.page == TOTAL_PAGES
    b.save()
    reader = PdfReader(OUT)
    assert len(reader.pages) == TOTAL_PAGES
    assert all('English Ladder' in (page.extract_text() or '') for page in reader.pages)
    print(json.dumps(dict(path=str(OUT), pages=len(reader.pages), bytes=OUT.stat().st_size,
                         units=8, extended_dialogue_turns=160, dialogue_gaps=80,
                         vocabulary_entries=192, set_phrases=128, structured_items=168), indent=2))


if __name__ == '__main__':
    build()
