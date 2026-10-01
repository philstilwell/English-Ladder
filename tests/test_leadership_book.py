"""Checks for the unpublished Cross-Cultural Leadership learner-book pilot."""
import re
import unittest
from collections import Counter

from pypdf import PdfReader

try:
    import pdfplumber
except ImportError:
    pdfplumber = None

from books.cross_cultural_leadership_content import UNITS, SLUG, AUTHOR, COPYRIGHT, REPRODUCTION_NOTICE
from build_leadership_book import (
    OUT, content_hash, validate_content, validate_layout, unit_page, key_page,
    TOTAL_PAGES, KEY_START, PHRASES_START, INDEX_START, INDEX_PAGES, SOURCES_PAGE,
    CLOZE_UNDERSCORES, CLOZE_FONT_SIZE, blank,
)
from work_curriculum import load_tracks


class LeadershipBookContentTests(unittest.TestCase):
    def test_cloze_template_has_one_fixed_width(self):
        for number in range(1, 11):
            markup = blank(number, '#294EDB')
            self.assertEqual(re.findall(r'_+', markup), ['_' * CLOZE_UNDERSCORES])
            self.assertIn(f'size="{CLOZE_FONT_SIZE}">', markup)
            self.assertIn('&nbsp;', markup)

    def test_course_outline_and_content_shape(self):
        validate_content()
        track = next(t for t in load_tracks() if t['slug'] == SLUG)
        self.assertEqual([u['title'] for u in UNITS], [m['title'] for m in track['modules']])
        self.assertEqual(len({u['scene'] for u in UNITS}), 8)
        self.assertEqual(len({u['skill'] for u in UNITS}), 8)
        for unit in UNITS:
            self.assertGreaterEqual(sum(len(line.split()) for _, line in unit['dialogue']), 350)
            self.assertEqual(len(unit['language']), 3)
            self.assertEqual(len(unit['language_extra']), 3)
            self.assertEqual(len(unit['rehearsal']), 3)

    def test_word_banks_and_keys_are_complete(self):
        for unit in UNITS:
            gaps = unit['gaps']
            text = ' '.join(line for _, line in unit['dialogue'])
            self.assertEqual(re.findall(r'\{\{(\d+)\}\}', text), [str(n) for n in range(1, 11)])
            for gap in gaps:
                self.assertEqual(set(gap), {'turn', 'answer', 'reason'})
            transfer = unit['transfer']['lines']
            self.assertTrue(all(q['prompt'].count('___') == 1 for q in transfer))
            answers = [q['options'][q['answer']] for q in transfer]
            self.assertEqual(len(set(answers)), 4)

    def test_numbered_layout_references(self):
        self.assertEqual([unit_page(i) for i in range(8)], [4, 13, 22, 31, 40, 49, 58, 67])
        self.assertEqual([key_page(i) for i in range(8)], list(range(76, 92, 2)))
        self.assertEqual([key_page(i, True) for i in range(8)], list(range(77, 92, 2)))
        self.assertEqual((KEY_START, PHRASES_START, INDEX_START, INDEX_PAGES, SOURCES_PAGE),
                         (76, 92, 94, 8, 102))

    def test_layout_guard_rejects_overlaps_and_overflow(self):
        valid = dict(page=1, text='example', x=46, width=100, top=120, bottom=100)
        validate_layout([valid])
        with self.assertRaises(AssertionError):
            validate_layout([valid, dict(valid, text='overlap', top=110, bottom=90)])
        with self.assertRaises(AssertionError):
            validate_layout([dict(valid, bottom=20)])


class LeadershipBookPDFTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reader = PdfReader(OUT)
        cls.text = [' '.join(p.extract_text().split()) for p in cls.reader.pages]

    def test_branding_page_count_and_placeholder_cleanup(self):
        self.assertIn(content_hash(), self.reader.metadata.subject)
        self.assertEqual(len(self.reader.pages), TOTAL_PAGES)
        self.assertEqual(TOTAL_PAGES, 102)
        for number, text in enumerate(self.text, 1):
            self.assertIn('English Ladder', text)
            self.assertIn(f'Phil Stilwell | {number:02d}', text)
            self.assertNotRegex(text, r'\{\{\d+\}\}|\ufffd')
            self.assertNotRegex(text.lower(), r'approval draft|review copy|think about it|use the book, not a blank page')
            self.assertGreater(len(text), 400)
        self.assertIn('international managers', self.text[0].lower())
        self.assertGreaterEqual(len(list(self.reader.pages[0].images)), 2)
        self.assertEqual(self.reader.metadata.author, AUTHOR)
        self.assertNotIn('draft', self.reader.metadata.title.lower())
        for page in (self.text[0], self.text[-1]):
            self.assertIn(COPYRIGHT, page)
            self.assertIn(REPRODUCTION_NOTICE, page)
            self.assertIn(AUTHOR + ' ' + COPYRIGHT, page)

    def test_doubled_vocabulary_and_phrases_are_printed_in_full(self):
        self.assertEqual(sum(len(u['vocabulary']) for u in UNITS), 192)
        self.assertEqual(sum(len(u['phrases']) for u in UNITS), 128)
        for i, unit in enumerate(UNITS):
            for n, entry in enumerate(unit['vocabulary']):
                page = self.text[unit_page(i) + n // 12]
                for text in entry:
                    self.assertIn(' '.join(text.split()), page)
            for n, (label, phrase) in enumerate(unit['phrases']):
                page = self.text[unit_page(i) + 2 + n // 8]
                self.assertIn(label.upper(), page)
                self.assertIn(phrase, page)

    def test_dialogue_banks_answers_and_turns_are_printed(self):
        for i, unit in enumerate(UNITS):
            first = self.text[unit_page(i) + 5]
            second = self.text[unit_page(i) + 6]
            self.assertIn('WORD + PHRASE BANK', first)
            self.assertIn(f'ANSWERS / EXPLANATIONS: PAGE {key_page(i, True)}', second)
            for number, gap in enumerate(unit['gaps'], 1):
                self.assertIn(gap['answer'], first)
                self.assertIn(f'{number}. {gap["answer"]}', second)
            for turn, (speaker, _) in enumerate(unit['dialogue'], 1):
                self.assertIn(f'{turn:02d} {speaker}:', first if turn <= 10 else second)
            self.assertIn(unit['title'], self.text[key_page(i) - 1])

    def test_every_question_has_an_explained_key_and_page_reference(self):
        for i, unit in enumerate(UNITS):
            checks = self.text[key_page(i) - 1]
            conversations = self.text[key_page(i, True) - 1]
            for q in unit['a'] + unit['d']:
                self.assertIn(q['prompt'], checks)
                self.assertIn(q['options'][q['answer']], checks)
                self.assertIn(q['reason'], checks)
            for q in unit['transfer']['lines']:
                answer = q['options'][q['answer']]
                self.assertIn(q['prompt'].replace('___', answer), conversations)
                self.assertIn(q['reason'], conversations)
            for gap in unit['gaps']:
                self.assertIn(gap['answer'], conversations)
                self.assertIn(gap['reason'], conversations)
            for offset in (0, 5, 7, 8):
                number = unit_page(i) + offset
                target = key_page(i, offset >= 7)
                text = self.text[number - 1]
                self.assertIn(f'page {target}', text.lower())
                target_ref = self.reader.pages[target - 1].indirect_reference.idnum
                links = [a.get_object().get('/Dest') for a in self.reader.pages[number - 1].get('/Annots', [])]
                self.assertIn(target_ref, [d[0].idnum for d in links if d])

    def test_all_fonts_are_embedded(self):
        seen = set()
        for page in self.reader.pages:
            links = [ref.get_object().get('/A', {}).get('/URI') for ref in page.get('/Annots', [])]
            self.assertEqual(links.count('https://englishladder.com/'), 1)
            self.assertEqual(page.extract_text().count('ENGLISHLADDER.COM'), 1)
            for font_ref in page['/Resources']['/Font'].values():
                font = font_ref.get_object()
                name = str(font['/BaseFont'])
                if name in seen:
                    continue
                seen.add(name)
                for descendant in font.get('/DescendantFonts', [font]):
                    descriptor = descendant.get_object().get('/FontDescriptor')
                    self.assertIsNotNone(descriptor, name)
                    self.assertTrue(any(key in descriptor.get_object() for key in ('/FontFile', '/FontFile2', '/FontFile3')), name)
        self.assertGreaterEqual(len(seen), 2)

    def test_index_links_reach_definitions(self):
        targets = Counter()
        for page in self.reader.pages[INDEX_START - 1:INDEX_START - 1 + INDEX_PAGES]:
            for annotation in page.get('/Annots', []):
                dest = annotation.get_object().get('/Dest')
                if dest:
                    targets[dest[0].idnum] += 1
        for i in range(8):
            for part in range(2):
                definition_page = self.reader.pages[unit_page(i) + part]
                self.assertEqual(targets[definition_page.indirect_reference.idnum], 12)
        self.assertEqual(sum(targets.values()), 192)

    @unittest.skipIf(pdfplumber is None, 'Optional local visual-audit dependency is not installed')
    def test_rendered_cloze_widths_are_identical_and_unbroken(self):
        widths = []
        with pdfplumber.open(OUT) as pdf:
            for i, unit in enumerate(UNITS):
                for offset in (6, 7, 8):
                    page = pdf.pages[unit_page(i) + offset - 1]
                    spans = []
                    for char in page.chars:
                        if char['text'] != '_':
                            continue
                        if (spans and abs(spans[-1][-1]['x1'] - char['x0']) < .1
                                and abs(spans[-1][-1]['top'] - char['top']) < .1):
                            spans[-1].append(char)
                        else:
                            spans.append([char])
                    if offset == 8:
                        expected = 4
                    else:
                        turns = unit['dialogue'][0:10] if offset == 6 else unit['dialogue'][10:20]
                        expected = sum(len(re.findall(r'\{\{\d+\}\}', line)) for _, line in turns)
                    self.assertEqual(len(spans), expected, page.page_number)
                    for span in spans:
                        self.assertEqual(len(span), CLOZE_UNDERSCORES, page.page_number)
                        self.assertTrue(all(abs(char['size'] - CLOZE_FONT_SIZE) < .01 for char in span))
                        widths.append(span[-1]['x1'] - span[0]['x0'])
        self.assertEqual(len(widths), 112)
        self.assertAlmostEqual(min(widths), max(widths), places=3)

    @unittest.skipIf(pdfplumber is None, 'Optional local visual-audit dependency is not installed')
    def test_printed_text_stays_on_page(self):
        with pdfplumber.open(OUT) as pdf:
            for page in pdf.pages:
                for char in page.chars:
                    self.assertGreaterEqual(char['x0'], 0, page.page_number)
                    self.assertLessEqual(char['x1'], page.width, page.page_number)
                    self.assertGreaterEqual(char['top'], 0, page.page_number)
                    self.assertLessEqual(char['bottom'], page.height, page.page_number)


if __name__ == '__main__':
    unittest.main()
