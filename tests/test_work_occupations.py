"""Regression checks for the 25 occupation courses and their published assets."""
import copy
import json
import unittest

from bs4 import BeautifulSoup
from pypdf import PdfReader

from work_curriculum import ROOT, WORKSHOPS, load_tracks
from work_icons import ICON_SLUGS, LEGACY_ICON_SLUGS, icon_asset, icon_bottom_trim
from work_occupations import OCCUPATION_SLUGS, load_occupation, validate_occupation


class OccupationSourceTests(unittest.TestCase):
    def test_complete_distinct_inventory_and_authoring_contract(self):
        self.assertEqual(len(OCCUPATION_SLUGS), 25)
        self.assertFalse(set(OCCUPATION_SLUGS) & set(LEGACY_ICON_SLUGS))
        self.assertEqual(len(set(ICON_SLUGS)), 66)
        categories = {
            'Business & professional services', 'Customers & creative work',
            'Education & public service', 'Health & life sciences',
            'Industry & infrastructure', 'Technology & data',
        }
        questions, cases = set(), set()
        for slug in OCCUPATION_SLUGS:
            with self.subTest(slug=slug):
                data = load_occupation(slug)
                validate_occupation(data)
                course = data['course']
                self.assertIn(course['category'], categories)
                self.assertTrue(course['title'].endswith('English'))
                self.assertTrue(all(source['url'].startswith('https://') for source in course['sources']))
                self.assertGreaterEqual(len({s['url'] for s in course['sources']}), 2)
                for module in course['modules']:
                    self.assertIn(module['case']['function'], WORKSHOPS)
                    self.assertNotIn(module['case']['brief'], cases)
                    cases.add(module['case']['brief'])
                    for question in module['workshop']['questions']:
                        self.assertNotIn(question['prompt'], questions)
                        questions.add(question['prompt'])
                        self.assertTrue(all(len(f.split()) >= 5 for f in question['feedback']))
        self.assertEqual(len(cases), 200)
        self.assertEqual(len(questions), 400)

    def test_loaded_sources_are_not_mutated_by_consumers(self):
        source = load_occupation(OCCUPATION_SLUGS[0])
        title = source['course']['title']
        source['course']['title'] = 'Changed in memory'
        self.assertEqual(load_occupation(OCCUPATION_SLUGS[0])['course']['title'], title)

    def test_option_rotation_preserves_authored_answers_and_feedback(self):
        for track in load_tracks():
            if not track.get('is_occupation'):
                continue
            source = load_occupation(track['slug'])['course']
            for original, published in zip(source['modules'], track['modules']):
                for before, after in zip(original['workshop']['questions'], published['workshop']['questions']):
                    with self.subTest(slug=track['slug'], module=published['id'], prompt=before['prompt']):
                        self.assertEqual(after['answer'], before['options'][before['correct_index']])
                        self.assertEqual(dict(zip(before['options'], before['feedback'])),
                                         dict(zip(after['options'], after['feedback'])))
                        self.assertEqual(after['feedback'][after['correct_index']],
                                         before['feedback'][before['correct_index']])

    def test_missing_choices_and_non_alternating_scripts_are_rejected(self):
        data = load_occupation(OCCUPATION_SLUGS[0])
        broken = copy.deepcopy(data)
        broken['course']['modules'][0]['workshop']['questions'][0]['options'].pop()
        with self.assertRaises(AssertionError):
            validate_occupation(broken)
        broken = copy.deepcopy(data)
        turns = broken['lesson_conversations']['module-1']['conversations'][0]['turns']
        turns[1][0] = turns[0][0]
        with self.assertRaises(AssertionError):
            validate_occupation(broken)

    def test_every_new_illustration_maps_to_its_own_atlas_cell(self):
        for index, slug in enumerate(OCCUPATION_SLUGS):
            self.assertEqual(icon_asset(slug), ('assets/work/occupation-icons.png', 5, 5, index))
            self.assertGreater(icon_bottom_trim(slug), 0)
            self.assertLess(icon_bottom_trim(slug), 26)
        for index, slug in enumerate(LEGACY_ICON_SLUGS):
            self.assertEqual(icon_asset(slug), ('assets/work/professional-icons.png', 7, 6, index))
            self.assertEqual(icon_bottom_trim(slug), 0)


class OccupationPublicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tracks = [track for track in load_tracks() if track.get('is_occupation')]

    def test_pages_keep_collocations_and_four_choices_with_guided_ai_modes(self):
        for track in self.tracks:
            page = BeautifulSoup((ROOT / f'efsp-{track["slug"]}.html').read_text(), 'html.parser')
            self.assertIsNotNone(page.select_one('.work-hero .work-occupation-icon'))
            self.assertIn('English Ladder', page.get_text())
            self.assertEqual(len(page.select('.work-quiz')), 16)
            for quiz in page.select('.work-quiz'):
                self.assertEqual(len(quiz.select('input[type="radio"]')), 4)
            for module in track['modules']:
                text = page.find(id=module['id']).get_text()
                for expression in module['collocations']:
                    self.assertIn(expression, text)
            data = json.loads(page.select_one('[data-ai-data]').string)
            modes = {mode['id']: mode for mode in data['modes']}
            self.assertEqual(modes['writing']['title'], 'Choose a clear message')
            for name in ('vocabulary', 'grammar', 'writing', 'register', 'review', 'teacher'):
                self.assertIn('four', modes[name]['instructions'].lower())
            for unwanted in ('write a 70-110 word', 'ask me to write my own sentence', 'paste my own fictional or anonymized draft'):
                self.assertNotIn(unwanted, page.get_text().lower())

    def test_new_pdf_collocations_and_no_composition_assignment(self):
        from generate_work_documents import clean
        for track in self.tracks:
            for index, (_, href) in enumerate(track['pdfs']):
                reader = PdfReader(ROOT / href)
                text = ' '.join(' '.join(page.extract_text().split()) for page in reader.pages)
                self.assertIn('English Ladder', text)
                self.assertNotIn('writes a 70-110 word message', text)
                self.assertNotIn('ask me to write my own sentence', text)
                if index in (1, 3):
                    for module in track['modules']:
                        for expression in module['collocations']:
                            self.assertIn(' '.join(clean(expression).split()), text)


if __name__ == '__main__':
    unittest.main()
