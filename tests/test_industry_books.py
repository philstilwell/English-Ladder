"""Quality checks for every revised field-specific learner book."""
import hashlib
import json
import unittest
from pathlib import Path

from audit_revised_books import audit
from books.revised_edition import inventory, load_edition
from revised_book_records import record, stem

ROOT = Path(__file__).resolve().parents[1]


class IndustryBookTests(unittest.TestCase):
    def test_every_field_has_substantial_distinct_material(self):
        fingerprints = set()
        for slug in inventory():
            book = load_edition(slug)
            self.assertEqual(sum(len(u['vocabulary']) for u in book['units']), 192)
            self.assertEqual(len({p[1] for u in book['units'] for p in u['phrases']}), 128)
            for scene in book['units'] + book['supplements']:
                self.assertEqual(len(scene['dialogue']), 20)
                signature = tuple(scene['dialogue'])
                self.assertNotIn(signature, fingerprints, slug)
                fingerprints.add(signature)
            for u in book['units']:
                self.assertEqual(len(u['choices']), 4)
                self.assertIn('Rebuild the exchange', u['second_take']['prompt'])
                for scene in (u, u['transfer']):
                    self.assertTrue(all(g['reason'] for g in scene['gaps']))
        self.assertEqual(len(fingerprints), 79 * 11)

    def test_complete_sources_fonts_links_and_rendered_content(self):
        for slug in inventory():
            with self.subTest(slug=slug):
                result = audit(slug, geometry=False)
                self.assertEqual(result['questions'], 96)
                self.assertEqual(result['blanks'], 142)
                self.assertGreater(result['internal_links'], 200)
                self.assertGreaterEqual(record(slug)['cover_resolution_dpi'], 300)

    def test_full_geometry_audit_matches_the_exact_delivered_files(self):
        report = json.loads((ROOT / 'books/REVISED-2026-10-results.json').read_text())['automated_checks']
        self.assertEqual(report['failures'], [])
        passed = {r['slug']: r for r in report['results']}
        self.assertEqual(len(passed), 80)
        for slug in inventory():
            pdf = ROOT / 'output/pdf' / (stem(slug) + '.pdf')
            self.assertTrue(passed[slug]['geometry_checked'])
            self.assertEqual(passed[slug]['sha256'], hashlib.sha256(pdf.read_bytes()).hexdigest())


if __name__ == '__main__':
    unittest.main()
