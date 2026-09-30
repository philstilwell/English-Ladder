"""Checks for the unpublished Cross-Cultural Leadership learner-book pilot."""
import re
import unittest
from collections import Counter

from pypdf import PdfReader

try:
    import pdfplumber
except ImportError:
    pdfplumber = None

from books.cross_cultural_leadership_content import UNITS, SLUG
from build_leadership_book import OUT, content_hash, validate_content, validate_layout, unit_page, key_page
from work_curriculum import load_tracks


class LeadershipBookContentTests(unittest.TestCase):
    def test_course_outline_and_content_shape(self):
        validate_content()
        track = next(t for t in load_tracks() if t['slug'] == SLUG)
        self.assertEqual([u['title'] for u in UNITS], [m['title'] for m in track['modules']])
        self.assertEqual(len({u['scene'] for u in UNITS}), 8)
        self.assertEqual(len({u['skill'] for u in UNITS}), 8)
        for unit in UNITS:
            self.assertGreaterEqual(sum(len(line.split()) for _, line in unit['dialogue']), 350)
            self.assertEqual(len(unit['language']), 3)
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
        self.assertEqual([unit_page(i) for i in range(8)], [5, 12, 19, 26, 33, 40, 47, 54])
        self.assertEqual([key_page(i) for i in range(8)], list(range(61, 69)))

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
        self.assertEqual(len(self.reader.pages), 75)
        for number, text in enumerate(self.text, 1):
            self.assertIn('English Ladder', text)
            self.assertIn(f'Approval draft 01 | {number:02d}', text)
            self.assertNotRegex(text, r'\{\{\d+\}\}|\ufffd')
            self.assertGreater(len(text), 400)
        self.assertIn('international managers', self.text[0].lower())
        self.assertGreaterEqual(len(list(self.reader.pages[0].images)), 2)

    def test_dialogue_banks_answers_and_turns_are_printed(self):
        for i, unit in enumerate(UNITS):
            first = self.text[unit_page(i) + 3]
            second = self.text[unit_page(i) + 4]
            self.assertIn('WORD + PHRASE BANK', first)
            self.assertIn('ANSWERS / COVER THIS STRIP UNTIL YOU FINISH', second)
            for number, gap in enumerate(unit['gaps'], 1):
                self.assertIn(gap['answer'], first)
                self.assertIn(f'{number}. {gap["answer"]}', second)
            for turn, (speaker, _) in enumerate(unit['dialogue'], 1):
                self.assertIn(f'{turn:02d} {speaker}:', first if turn <= 10 else second)
            self.assertIn(unit['title'], self.text[key_page(i) - 1])

    def test_all_fonts_are_embedded(self):
        seen = set()
        for page in self.reader.pages:
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
        for page in self.reader.pages[70:74]:
            for annotation in page.get('/Annots', []):
                dest = annotation.get_object()['/Dest']
                targets[dest[0].idnum] += 1
        for i in range(8):
            definition_page = self.reader.pages[unit_page(i)]
            self.assertEqual(targets[definition_page.indirect_reference.idnum], 12)
        self.assertEqual(sum(targets.values()), 96)

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
