"""Quality checks for the complete, authored learner books currently on disk."""
import unittest
from pathlib import Path

import pdfplumber
from pypdf import PdfReader

import build_leadership_book as design
from build_industry_books import load_book, validate_book
from books.cross_cultural_leadership_content import COPYRIGHT, REPRODUCTION_NOTICE
from work_curriculum import load_tracks

ROOT = Path(__file__).resolve().parents[1]
TRACKS = {t['slug']: t for t in load_tracks()[1:]}
COMPLETE = sorted(p.name.removesuffix('-english-book.pdf') for p in (ROOT / 'output/pdf').glob('*-english-book.pdf')
                  if p.name.removesuffix('-english-book.pdf') in TRACKS)


class IndustryBookTests(unittest.TestCase):
    def test_complete_sources_and_rendered_content(self):
        self.assertTrue(COMPLETE)
        for slug in COMPLETE:
            with self.subTest(slug=slug):
                book = load_book(slug)
                validate_book(book, TRACKS[slug])
                reader = PdfReader(ROOT / f'output/pdf/{slug}-english-book.pdf')
                pages = [' '.join(page.extract_text().split()) for page in reader.pages]
                self.assertEqual(len(pages), 102)
                self.assertIn(design.content_hash(book['units']), reader.metadata.subject)
                self.assertEqual(reader.metadata.author, 'Phil Stilwell')
                self.assertGreaterEqual(len(list(reader.pages[0].images)), 2)
                for i, text in enumerate(pages, 1):
                    self.assertIn('English Ladder', text)
                    self.assertIn(f'Phil Stilwell | {i:02d}', text)
                    self.assertNotRegex(text, r'\{\{\d+\}\}|\[\[|\ufffd|review copy|approval draft')
                for text in (pages[0], pages[-1]):
                    self.assertIn(COPYRIGHT, text)
                    self.assertIn(REPRODUCTION_NOTICE, text)
                for i, unit in enumerate(book['units']):
                    start = design.unit_page(i) - 1
                    key = pages[design.key_page(i) - 1]
                    conversation_key = pages[design.key_page(i, True) - 1]
                    for n, entry in enumerate(unit['vocabulary']):
                        for value in entry:
                            self.assertIn(' '.join(value.split()), pages[start + 1 + n // 12])
                    for n, (label, phrase) in enumerate(unit['phrases']):
                        self.assertIn(label.upper(), pages[start + 3 + n // 8])
                        self.assertIn(phrase, pages[start + 3 + n // 8])
                        if phrase.startswith('"') and phrase.endswith('"'):
                            self.assertNotIn('"' + phrase + '"', pages[start + 3 + n // 8])
                    for q in unit['a'] + unit['d']:
                        self.assertIn(q['prompt'], key)
                        self.assertIn(q['reason'], key)
                    for n, g in enumerate(unit['gaps'], 1):
                        self.assertIn(g['answer'], pages[start + 6])
                        self.assertIn(f'{n}. {g["answer"]}', pages[start + 7])
                        self.assertIn(g['reason'], conversation_key)
                    for q in unit['transfer']['lines']:
                        answer = q['options'][q['answer']]
                        self.assertIn(q['prompt'].replace('___', answer), conversation_key)
                        self.assertIn(q['reason'], conversation_key)
                    for turn, (speaker, _) in enumerate(unit['dialogue'], 1):
                        self.assertIn(f'{turn:02d} {speaker}:', pages[start + 6 + (turn > 10)])

    def test_fonts_and_link_destinations(self):
        for slug in COMPLETE:
            with self.subTest(slug=slug):
                reader = PdfReader(ROOT / f'output/pdf/{slug}-english-book.pdf')
                seen = set()
                page_ids = {p.indirect_reference.idnum for p in reader.pages}
                for page in reader.pages:
                    for ref in page['/Resources']['/Font'].values():
                        font = ref.get_object()
                        if str(font['/BaseFont']) in seen:
                            continue
                        seen.add(str(font['/BaseFont']))
                        descriptor = font['/FontDescriptor'].get_object()
                        self.assertTrue(any(k in descriptor for k in ('/FontFile', '/FontFile2', '/FontFile3')))
                    for ref in page.get('/Annots', []):
                        dest = ref.get_object().get('/Dest')
                        if dest:
                            self.assertIn(dest[0].idnum, page_ids)
                for i in range(8):
                    for offset in (0, 5, 7, 8):
                        page = reader.pages[design.unit_page(i) + offset - 1]
                        target = reader.pages[design.key_page(i, offset >= 7) - 1].indirect_reference.idnum
                        self.assertIn(target, [a.get_object()['/Dest'][0].idnum for a in page.get('/Annots', []) if a.get_object().get('/Dest')])

    def test_uniform_gaps_and_page_bounds(self):
        for slug in COMPLETE:
            with self.subTest(slug=slug), pdfplumber.open(ROOT / f'output/pdf/{slug}-english-book.pdf') as pdf:
                widths = []
                cloze_pages = {design.unit_page(i) + offset for i in range(8) for offset in (6, 7, 8)}
                for page in pdf.pages:
                    spans = []
                    for char in page.chars:
                        self.assertGreaterEqual(char['x0'], 0)
                        self.assertLessEqual(char['x1'], page.width)
                        self.assertGreaterEqual(char['top'], 0)
                        self.assertLessEqual(char['bottom'], page.height)
                        if char['text'] != '_' or page.page_number not in cloze_pages:
                            continue
                        if spans and abs(spans[-1][-1]['x1'] - char['x0']) < .1 and abs(spans[-1][-1]['top'] - char['top']) < .1:
                            spans[-1].append(char)
                        else:
                            spans.append([char])
                    for span in spans:
                        self.assertEqual(len(span), design.CLOZE_UNDERSCORES)
                        self.assertTrue(all(abs(c['size'] - design.CLOZE_FONT_SIZE) < .01 for c in span))
                        widths.append(span[-1]['x1'] - span[0]['x0'])
                self.assertEqual(len(widths), 112)
                self.assertAlmostEqual(min(widths), max(widths), places=3)


if __name__ == '__main__':
    unittest.main()
