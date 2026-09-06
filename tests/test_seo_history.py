import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch
import seo


class SearchPublishingTests(unittest.TestCase):
    def test_rebuild_preserves_dates_and_only_changed_content_gets_a_new_date(self):
        class LaterDate(date):
            @classmethod
            def today(cls):
                return cls(2026, 9, 7)

        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'content/work').mkdir(parents=True)
            (root / 'content/grammar-curriculum.json').write_text('{"concepts":[]}')
            (root / 'content/work/documents.json').write_text(json.dumps({'revision': '2026-09-05', 'documents': {'guide.pdf': {}}}))
            (root / 'guide.pdf').write_bytes(b'unchanged document')
            page = '<html><head><title>A lesson</title><meta name="description" content="A lesson description"><link rel="canonical" href="https://englishladder.com/"></head><body><main>Original teaching text</main></body></html>'
            (root / 'index.html').write_text(page)
            (root / '404.html').write_text(page)
            with patch.object(seo, 'ROOT', root):
                seo.write_sitemaps()
                before = json.loads((root / 'content/seo-index.json').read_text())
                self.assertNotIn('404.html', before['resources'])
                self.assertEqual('2026-09-05', before['resources']['guide.pdf']['lastmod'])
                with patch.object(seo, 'date', LaterDate):
                    seo.write_sitemaps()
                    self.assertEqual(before, json.loads((root / 'content/seo-index.json').read_text()))
                    (root / 'index.html').write_text(page.replace('Original teaching text', 'Revised teaching text'))
                    seo.write_sitemaps()
                    after = json.loads((root / 'content/seo-index.json').read_text())
                self.assertEqual('2026-09-07', after['resources']['index.html']['lastmod'])
                self.assertEqual(before['resources']['guide.pdf'], after['resources']['guide.pdf'])

    def test_grammar_recommendations_use_reviewed_topics_and_cover_all_communication_functions(self):
        from work_curriculum import load_tracks
        functions = {m['function'] for t in load_tracks() for m in t['modules']}
        self.assertEqual(functions, set(seo.FUNCTION_GRAMMAR))
        for numbers in [*seo.FUNCTION_GRAMMAR.values(), *[c['grammar'] for c in seo.CATEGORIES.values()]]:
            self.assertTrue(set(numbers) <= set(seo.grammar()))


if __name__ == '__main__':
    unittest.main()
