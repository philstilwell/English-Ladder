import unittest
from pathlib import Path
from bs4 import BeautifulSoup
from reading_layout import prepare_reading_controls

ROOT = Path(__file__).resolve().parents[1]


class ReadingLayoutTests(unittest.TestCase):
    def test_rebuilding_controls_preserves_lesson_text_without_duplicates(self):
        soup = BeautifulSoup((ROOT / f'news/{max((ROOT / "archive/lessons").glob("*.json")).stem}/advanced.html').read_text(), 'html.parser')
        reading = soup.select_one('[data-stage="read"] .section').get_text()
        prepare_reading_controls(soup)
        prepared = str(soup)
        prepare_reading_controls(soup)
        self.assertEqual(prepared, str(soup))
        self.assertEqual(reading, soup.select_one('[data-stage="read"] .section').get_text())
        self.assertEqual(1, len(soup.select('script[data-reading-start]')))
        self.assertEqual(1, len(soup.select('script[data-reading-open]')))
        self.assertEqual(3, len(soup.select('.learning-flow button')))
        self.assertEqual(3, len(soup.select('.stage-actions')))
        self.assertEqual(6, len(soup.select('.vocabulary-language')))
        self.assertEqual(0, len(soup.select('.learning-panel[hidden]')))
