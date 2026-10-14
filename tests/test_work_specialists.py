"""Publication and content checks for the eight specialist expansions."""
import json
import unittest
from urllib.parse import urlsplit

from bs4 import BeautifulSoup
from PIL import Image

from books.supplements import load_supplements
from build_industry_books import validate_book
from work_curriculum import ROOT, load_tracks
from work_icons import icon_asset, directory_collage, SPECIALIST_ICON_CROPS
from work_lesson_conversations import load_course
from work_medical import completed
from work_specialists import SPECIALIST_SLUGS, book
from work_web_content import web_track


class SpecialistExpansionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tracks = {track['slug']: track for track in load_tracks()}

    def test_eight_courses_complete_the_eighty_course_inventory(self):
        self.assertEqual(len(self.tracks), 80)
        self.assertEqual(len(set(SPECIALIST_SLUGS)), 8)
        for slug in SPECIALIST_SLUGS:
            self.assertEqual(len(self.tracks[slug]['modules']), 8)
            self.assertEqual(self.tracks[slug]['pdfs'],
                             [['Learner book', f'pdf/efsp/{slug}-english-book.pdf']])

    def test_books_have_full_independently_authored_content(self):
        scripts = set()
        for slug in SPECIALIST_SLUGS:
            data = book(slug)
            validate_book(data, self.tracks[slug])
            self.assertTrue(data['balanced_answer_columns'])
            self.assertEqual(sum(len(u['vocabulary']) for u in data['units']), 192)
            self.assertEqual(sum(len(u['phrases']) for u in data['units']), 128)
            self.assertGreaterEqual(len({v[0].casefold() for u in data['units'] for v in u['vocabulary']}), 144)
            for u in data['units'] + load_supplements(slug):
                script = completed(u)
                self.assertEqual(len(script), 20)
                self.assertTrue(all(a[0] != b[0] for a, b in zip(script, script[1:])))
                self.assertGreaterEqual(len(' '.join(line for _, line in script).split()), 220)
                fingerprint = json.dumps(script)
                self.assertNotIn(fingerprint, scripts)
                scripts.add(fingerprint)
        self.assertEqual(len(scripts), 88)

    def test_short_dialogues_are_unique_and_substantial(self):
        scripts = set()
        for slug in SPECIALIST_SLUGS:
            for lesson in load_course(slug).values():
                self.assertEqual(len(lesson['conversations']), 3)
                for conversation in lesson['conversations']:
                    turns = conversation['turns']
                    self.assertEqual(len(turns), 10)
                    self.assertGreaterEqual(len(' '.join(line for _, line in turns).split()), 100)
                    fingerprint = json.dumps(turns)
                    self.assertNotIn(fingerprint, scripts)
                    scripts.add(fingerprint)
        self.assertEqual(len(scripts), 192)

    def test_vocabulary_is_specific_to_each_profession(self):
        expected = {
            'nutrition-dietetics': ['dietary history', 'nutrition facts panel', 'dietary supplement'],
            'sports-medicine': ['mechanism of injury', 'concussion', 'training load'],
            'international-law': ['service of process', 'arbitral award', 'treaty'],
            'patent-law': ['invention disclosure', 'prior art', 'freedom to operate'],
            'university-professors': ['rubric', 'seminar', 'academic integrity'],
            'investment-management-banking': ['investment mandate', 'enterprise value', 'material nonpublic information'],
            'cross-border-ma-integration': ['legal close', 'cutover', 'synergy'],
            'localization-qa': ['placeholder', 'pseudolocalization', 'bidirectional text'],
        }
        for slug, terms in expected.items():
            vocabulary = {term.casefold() for u in book(slug)['units'] for term, _, _ in u['vocabulary']}
            self.assertTrue(set(terms) <= vocabulary, slug)

    def test_illustrations_are_individual_transparent_assets_with_equal_envelopes(self):
        collage = BeautifulSoup(directory_collage(), 'html.parser')
        self.assertEqual(len(collage.select('.work-collage-cell')), 80)
        for slug in SPECIALIST_SLUGS:
            asset, columns, rows, index = icon_asset(slug)
            self.assertEqual((columns, rows, index), (1, 1, 0))
            self.assertEqual(asset, f'assets/work/specialists/{slug}.png')
            with Image.open(ROOT / asset) as image:
                self.assertEqual(image.size, (1254, 1254))
                self.assertEqual(image.getchannel('A').getextrema(), (0, 255))
            with Image.open((ROOT / asset).with_suffix('.webp')) as image:
                self.assertEqual(image.size, (384, 384))
                self.assertIn('A', image.getbands())
            x, y, width, height = SPECIALIST_ICON_CROPS[slug]
            self.assertTrue(0 <= x < x + width <= 1254)
            self.assertTrue(0 <= y < y + height <= 1254)
            art = collage.select_one(f'[data-work-icon="{slug}"]')
            style = dict(part.split(':', 1) for part in art['style'].split(';'))
            sizes = [float(style[key].rstrip('%')) for key in ('width', 'height')]
            self.assertAlmostEqual(max(sizes), 80)
            self.assertAlmostEqual(sizes[0] / sizes[1], width / height, places=6)

    def test_webpages_match_the_books_and_keep_guarded_activities(self):
        manifest = json.loads((ROOT / 'content/work/documents.json').read_text())['documents']
        for slug in SPECIALIST_SLUGS:
            page = BeautifulSoup((ROOT / f'efsp-{slug}.html').read_text(), 'html.parser')
            href = f'pdf/efsp/{slug}-english-book.pdf'
            self.assertIn(href, [urlsplit(a['href']).path for a in page.select('#downloads a[href]')])
            from revised_book_records import record
            self.assertEqual(manifest[href]['pages'], record(slug)['pdf_pages'])
            self.assertEqual(manifest[href]['dialogue_count'], 11)
            self.assertEqual(manifest[href]['illustration_asset'], icon_asset(slug)[0])
            self.assertEqual(len(page.select(f'[data-work-icon="{slug}"]')), 2)
            self.assertEqual(len(page.select('.work-module')), 8)
            self.assertEqual(len(page.select('[data-work-quiz]')), 140)
            self.assertEqual(len(page.select('[data-cloze-gap]')), 98)
            self.assertIsNone(page.select_one('textarea:not([readonly])'))
            self.assertIsNone(page.select_one('input[type="checkbox"]'))
            self.assertEqual(len(web_track(self.tracks[slug])['web_glossary']), 192)
            for module_id, lesson in load_course(slug).items():
                module = page.find(id=module_id)
                for conversation in lesson['conversations']:
                    summary = next(s for s in module.select('summary') if conversation['title'] in s.get_text())
                    self.assertFalse(summary.parent.has_attr('open'))

    def test_combined_investment_course_keeps_both_distinct_workflows(self):
        titles = [u['title'] for u in book('investment-management-banking')['units']]
        text = ' '.join(titles).lower()
        self.assertIn('portfolio', text)
        self.assertIn('enterprise value', text)
        self.assertIn('capital', text)
        self.assertEqual(sum('investment-management-banking' == slug for slug in self.tracks), 1)

    def test_localization_numeric_and_directional_examples_remain_precise(self):
        units = book('localization-qa')['units']
        answers = lambda u: [q['options'][q['answer']] for q in u['transfer']['lines']]
        self.assertEqual(answers(units[2]), ['one', 'few', 'many', 'untested'])
        self.assertEqual(answers(units[4])[:2], ['AB-123', '321-BA'])
        self.assertIn('1.8 seconds', units[6]['precision'])
        self.assertIn('4.2 minus 2.4', units[6]['precision'])
        self.assertIn('No universal', units[6]['brief'])

    def test_sources_and_scope_notes_are_present(self):
        for slug in SPECIALIST_SLUGS:
            data = book(slug)
            self.assertIn('fictional', data['scope_note'].lower())
            for source in data['sources']:
                self.assertTrue(source['url'].startswith('https://'))
                self.assertEqual(source['checked'], '11 October 2026')


if __name__ == '__main__':
    unittest.main()
