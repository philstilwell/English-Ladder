import json
import unittest
from pathlib import Path
from bs4 import BeautifulSoup
import power_grammar

ROOT = Path(__file__).resolve().parents[1]

class PowerGrammarTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items = power_grammar.load_exercises()
        cls.page = BeautifulSoup((ROOT / 'grammar-concepts.html').read_text(), 'html.parser')

    def test_complete_source_collection_is_published_as_text(self):
        section = self.page.select_one('#power-grammar')
        self.assertEqual(20, len(section.select('details.pg-set')))
        self.assertEqual(200, len(section.select('article.pg-exercise')))
        self.assertEqual(554, len(section.select('.pg-alternatives li')))
        self.assertEqual(654, len(section.select('.pg-correction .pg-caret')))
        self.assertIsNone(section.find('img'))
        self.assertFalse(section.select('details[open]'))
        for item in self.items:
            article = section.select_one(f'#power-grammar-{item["number"]}')
            self.assertEqual(item['original'], article.select_one('.pg-original').get_text())
            self.assertEqual(item['alternatives'], [li.get_text() for li in article.select('.pg-alternatives li')])
            self.assertEqual(item['source_caret_count'], len(article.select('.pg-correction .pg-caret')))
            self.assertEqual(64, len(item['source_sha256']))
        ids = [tag['id'] for tag in self.page.select('[id]')]
        self.assertEqual(len(ids), len(set(ids)))

    def test_partial_word_colors_and_source_notes_survive(self):
        self.assertIn('success<span class="pg-added">ful</span>', str(self.page.select_one('#power-grammar-100 .pg-correction')))
        for number in [42, 94, 158, 197]:
            self.assertIsNotNone(self.page.select_one(f'#power-grammar-{number} .pg-note'))
        self.assertEqual(3, len(self.page.select('#power-grammar-157 .pg-alternatives li')))
        self.assertEqual(3, len(self.page.select('#power-grammar-190 .pg-alternatives li')))

    def test_redecoration_preserves_existing_topics_without_duplicates(self):
        soup = BeautifulSoup(str(self.page), 'html.parser')
        before = str(soup.select_one('[data-library]'))
        for _ in range(2):
            power_grammar.enhance_page(soup, 'grammar-concepts.html')
        self.assertEqual(before, str(soup.select_one('[data-library]')))
        self.assertEqual(1, len(soup.select('#power-grammar')))
        self.assertEqual(1, len(soup.select('link[href="power-grammar.css"]')))
        self.assertEqual(1, len(soup.select('script[src="power-grammar.js"]')))
        self.assertEqual(1, len(soup.select('[data-power-grammar-jump]')))

    def test_text_cannot_inject_markup(self):
        value = power_grammar.marked_text('<script>[<b>]&^')
        self.assertNotIn('<script>', value)
        self.assertNotIn('<b>', value)
        self.assertIn('&lt;b&gt;', value)
        self.assertIn('&amp;', value)

if __name__ == '__main__':
    unittest.main()
