"""Every published course must preserve the reviewed books' cases and answers."""
import json
import unittest
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from work_curriculum import ROOT, load_tracks
from work_web_content import completed_turn, web_track


class WebBookTests(unittest.TestCase):
    def test_follow_up_answers_do_not_follow_a_fixed_position_sequence(self):
        from work_web_lessons import transfer
        sequences = []
        for source in load_tracks():
            track = web_track(source)
            scenes = [m['book_unit'] for m in track['modules']] + track['supplemental_scenarios']
            for index, scene in enumerate(scenes):
                soup = BeautifulSoup(transfer(scene['transfer'], f'{track["slug"]}-{index}'), 'html.parser')
                sequences.append(tuple(int(q['data-correct']) for q in soup.select('[data-work-quiz]')))
        self.assertGreater(sum(order != (0, 1, 2, 3) for order in sequences), len(sequences) * .95)
        self.assertEqual({position for sequence in sequences for position in sequence}, {0, 1, 2, 3})

    def test_pdf_page_links_follow_the_print_layout(self):
        from build_leadership_book import key_page, supplement_page, unit_page
        for track in load_tracks():
            for index, module in enumerate(web_track(track)['modules']):
                self.assertEqual(module['book_page'], unit_page(index))
                self.assertEqual(module['book_key_page'], key_page(index))
        self.assertEqual([supplement_page(i) for i in range(3)], [76, 79, 82])

    def test_all_courses_preserve_every_reviewed_dialogue_answer_and_language_bank(self):
        fingerprints = set()
        total_questions = 0
        for original in load_tracks():
            track = web_track(original)
            self.assertEqual(web_track(track), track)
            self.assertNotIn('book_unit', original['modules'][0])
            soup = BeautifulSoup((ROOT / f'efsp-{track["slug"]}.html').read_text(), 'html.parser')
            units = [m['book_unit'] for m in track['modules']]
            scenes = units + track['supplemental_scenarios']
            graph = json.loads(soup.select_one('[data-seo-schema]').string)['@graph']
            resource = next(item for item in graph if item['@type'] == 'LearningResource')
            self.assertEqual(resource['teaches'], [unit['skill'] for unit in units])
            self.assertEqual([part['teaches'] for part in resource['hasPart']], [unit['skill'] for unit in units])
            self.assertEqual(len(soup.select('[data-work-term]')), 192)
            self.assertEqual(len(soup.select('.work-conversation')), 24)
            self.assertEqual(len(soup.select('.work-extended-conversation')), 8)
            self.assertEqual(len(soup.select('.work-additional-scene')), 3)
            self.assertFalse(soup.select('.work-extended-conversation[open], .work-conversation[open], .work-additional-scene[open]'))
            for unit, module in zip(units, soup.select('.work-module')):
                self.assertEqual(len(module.select('.work-lesson-vocabulary > div')), 24)
                self.assertEqual(len(module.select('.work-phrase-list > div')), 16)
                self.assertEqual(len(module.select('.work-language-notes > div')), 6)
                for term, definition, collocation in unit['vocabulary']:
                    for text in (term, definition, collocation):
                        self.assertIn(text, module.get_text())
                for purpose, phrase in unit['phrases']:
                    self.assertIn(phrase, module.get_text())
                questions = unit['a'] + unit['d'] + unit['transfer']['lines']
                self.assertEqual(len(questions), 11)
                for source, published in zip(questions, module.select('[data-work-quiz]')):
                    choices = [label.span.get_text() for label in published.select('label')]
                    self.assertEqual(choices[int(published['data-correct'])], source['options'][source['answer']])
                    self.assertEqual(published['data-explanation'], source['reason'])
                    self.assertEqual(set(choices), set(source['options']))
            activities = soup.select('[data-work-cloze]')
            self.assertEqual(len(activities), 11)
            for scene, section in zip(track['supplemental_scenarios'], soup.select('.work-additional-scene')):
                if scene.get('reference'):
                    self.assertIn(scene['reference'][1], [link['href'] for link in section.select('a[href]')])
            for scene, activity in zip(scenes, activities):
                self.assertEqual(json.loads(activity.select_one('[data-cloze-answers]').string), scene['gaps'])
                self.assertEqual(len(activity.select('.work-extended-lines > li')), 20)
                self.assertEqual(len(activity.select('[data-cloze-gap]')), len(scene['gaps']))
                answers = {gap['answer'] for gap in scene['gaps']}
                for number, select in enumerate(activity.select('[data-cloze-gap]'), 1):
                    self.assertEqual(select['data-cloze-gap'], str(number))
                    self.assertEqual({o['value'] for o in select.select('option') if o['value']}, answers)
                    self.assertEqual(select.select_one('option')['value'], '')
                    self.assertIsNotNone(soup.find(id=select['aria-describedby']))
                completed = [f'{role}: {completed_turn(line, scene["gaps"])}' for role, line in scene['dialogue']]
                self.assertEqual([li.get_text() for li in activity.select('.work-completed-script li')], completed)
                fingerprint = tuple(completed)
                self.assertNotIn(fingerprint, fingerprints)
                fingerprints.add(fingerprint)
            for quiz in soup.select('[data-work-quiz]'):
                self.assertEqual(len(quiz.select('input[type=radio]')), 4)
                self.assertGreaterEqual(len(quiz['data-explanation'].split()), 6)
                total_questions += 1
            for link in soup.select('a[href*="#page="]'):
                self.assertTrue(1 <= int(urlparse(link['href']).fragment.split('=')[1]) <= 114)
            for unwanted in ('write a 70-110 word', 'ask me to write my own sentence', 'draft a two-sentence response'):
                self.assertNotIn(unwanted, soup.get_text().lower())
        self.assertEqual(len(fingerprints), 726)
        self.assertEqual(total_questions, 6600)


if __name__ == '__main__':
    unittest.main()
