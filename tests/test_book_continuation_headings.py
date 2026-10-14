"""Guard the circular section letters on automatically continued PDF pages."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

from bs4 import BeautifulSoup

from audit_revised_books import audit_heading_records
from books.revised_edition import inventory
from revised_book_records import stem

ROOT = Path(__file__).resolve().parents[1]


class ContinuationHeadingTests(unittest.TestCase):
    def test_all_books_preserve_continuation_letter_styling(self):
        total = 0
        for slug in ['cultural-leadership-us-branches', *inventory()]:
            with self.subTest(slug=slug):
                layout = json.loads((ROOT / 'output/pdf' / (stem(slug) + '-layout.json')).read_text())
                audit_heading_records(layout)
                total += sum(item['letter'] is not None for item in layout['continuationHeadings'])
        self.assertGreater(total, 0)

    def test_financial_advice_guided_speaking_continuation(self):
        layout = json.loads((ROOT / 'output/pdf/financial-advice-english-book-layout.json').read_text())
        item = next(h for h in layout['continuationHeadings'] if h['source'] == 'u3-transfer')
        self.assertEqual(item['letter'], 'F')
        for key, value in [('letter', None), ('color', 'rgb(0, 0, 0)')]:
            broken = deepcopy(layout)
            if key == 'letter':
                next(h for h in broken['continuationHeadings'] if h['id'] == item['id'])[key] = value
            else:
                next(h for h in broken['sectionLetters'] if h['id'] == item['id'])[key] = value
            with self.assertRaises(AssertionError):
                audit_heading_records(broken)

    def test_paginated_headings_retain_markup_and_single_suffix(self):
        html = ROOT / 'output/pdf/cross-cultural-leadership-english-book-revised.html'
        soup = BeautifulSoup(html.read_text(), 'html.parser')
        continuations = soup.select('[data-continued-from]')
        self.assertTrue(continuations)
        for page in continuations:
            original = soup.find(id=page['data-continued-from']).select_one('.flow-heading')
            continued = page.select_one('.flow-heading')
            self.assertEqual(continued.decode_contents(), original.decode_contents() + ' / continued')


if __name__ == '__main__':
    unittest.main()
