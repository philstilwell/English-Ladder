"""Checks for the expanded Cross-Cultural Leadership learner book."""
import re
import unittest
from collections import Counter

from pypdf import PdfReader

try:
    import pdfplumber
except ImportError:
    pdfplumber = None

from books.cross_cultural_leadership_content import UNITS, SLUG, AUTHOR, COPYRIGHT, REPRODUCTION_NOTICE
from books.supplements import load_supplements
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
        self.assertEqual([key_page(i) for i in range(8)], list(range(85, 101, 2)))
        self.assertEqual([key_page(i, True) for i in range(8)], list(range(86, 102, 2)))
        self.assertEqual((KEY_START, PHRASES_START, INDEX_START, INDEX_PAGES, SOURCES_PAGE),
                         (85, 104, 106, 8, 114))

    def test_layout_guard_rejects_overlaps_and_overflow(self):
        valid = dict(page=1, text='example', x=46, width=100, top=120, bottom=100)
        validate_layout([valid])
        with self.assertRaises(AssertionError):
            validate_layout([valid, dict(valid, text='overlap', top=110, bottom=90)])
        with self.assertRaises(AssertionError):
            validate_layout([dict(valid, bottom=20)])


class LeadershipBookPDFTests(unittest.TestCase):
    def test_published_book_matches_the_approved_revised_edition(self):
        from pathlib import Path
        from audit_revised_books import audit
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(OUT.read_bytes(),
                         (root / 'output/pdf/cross-cultural-leadership-english-book-revised.pdf').read_bytes())
        result = audit(SLUG, geometry=False)
        self.assertEqual(result['questions'], 96)
        self.assertEqual(result['extended_dialogues'], 11)
        self.assertEqual(result['blanks'], 142)


if __name__ == '__main__':
    unittest.main()
