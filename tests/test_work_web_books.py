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
        from revised_book_records import record
        for track in load_tracks():
            pages = record(track['slug'])['page_map']
            for index, module in enumerate(web_track(track)['modules']):
                self.assertEqual(module['book_page'], pages[f'u{index + 1}-a'])
                self.assertEqual(module['book_key_page'], pages[f'key-u{index + 1}-d'])
                self.assertEqual(module['book_dialogue_page'], pages[f'u{index + 1}-e'])
            self.assertEqual(web_track(track)['book_additional_pages'], [pages[f'additional-{i}'] for i in range(1, 4)])

    def test_all_courses_preserve_every_reviewed_dialogue_answer_and_language_bank(self):
        from revised_book_records import record
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
                self.assertEqual(len(module.select('.work-language > details > .work-language-notes > div')), 6)
                self.assertEqual(len(module.select('.work-focus-list > div')), 4)
                for term, definition, collocation in unit['vocabulary']:
                    for text in (term, definition, collocation):
                        self.assertIn(text, module.get_text())
                for purpose, phrase in unit['phrases']:
                    self.assertIn(phrase, module.get_text())
                for group in (unit['focus'], unit['registers']):
                    for row in group:
                        for value in row:
                            self.assertIn(value, module.get_text())
                self.assertIn(unit['delivery'], module.get_text())
                questions = unit['a'] + unit['d'] + unit['transfer']['lines'] + unit['repair'] + [unit['second_take']]
                self.assertEqual(len(questions), 14)
                for source, published in zip(questions, module.select('[data-work-quiz]')):
                    choices = [label.span.get_text() for label in published.select('label')]
                    self.assertEqual(choices[int(published['data-correct'])], source['options'][source['answer']])
                    self.assertEqual(published['data-explanation'], source['reason'])
                    self.assertEqual(set(choices), set(source['options']))
                    if len(set(source.get('reasons', []))) > 1:
                        expected = dict(zip(source['options'], source['reasons'], strict=True))
                        for choice, reason in zip(choices, published.select('.work-answer-reasons li span'), strict=True):
                            self.assertEqual(reason.get_text(), expected[choice])
                script = unit['transfer']['script']
                expected = [f'{role}: {completed_turn(words, script["gaps"])}' for role, words in script['dialogue']]
                self.assertEqual([li.get_text() for li in module.select('.work-transfer-script li')], expected)
                for speaker, words in script['dialogue']:
                    if '{{' not in words:
                        self.assertIn(f'{speaker}: {words}', module.select_one('.work-transfer-questions').get_text())
            for index, (checkpoint, section) in enumerate(zip(track['book_checkpoints'], soup.select('.work-review'), strict=True), 1):
                self.assertNotIn('open', section.attrs)
                self.assertEqual(section['id'], f'review-{index}')
                self.assertEqual(section.find_previous_sibling('details', class_='work-module')['id'], f'module-{checkpoint["after"]}')
                self.assertIn(checkpoint['facts'], section.get_text())
                for question, published in zip(checkpoint['questions'], section.select('[data-work-quiz]'), strict=True):
                    self.assertIn(question['prompt'], published.get_text())
                    choices = [label.span.get_text() for label in published.select('label')]
                    self.assertEqual(choices, question['options'])
                    self.assertEqual(int(published['data-correct']), question['answer'])
                    for reason in question['reasons']:
                        self.assertIn(reason, published.get_text())
            for _, explanation, example in track['book_field_notes'].get('field_notes', []):
                self.assertIn(explanation, soup.select_one('.work-field-notes').get_text())
                self.assertIn(example, soup.select_one('.work-field-notes').get_text())
            activities = soup.select('[data-work-cloze]')
            self.assertEqual(len(activities), 11)
            for scene, section in zip(track['supplemental_scenarios'], soup.select('.work-additional-scene')):
                if track['slug'] != 'cultural-leadership-us-branches':
                    self.assertEqual(len(section.select('.work-additional-language dt')), 6)
                    for gap in scene['gaps']:
                        self.assertIn(gap['answer'], section.select_one('.work-additional-language').get_text())
                        self.assertIn(gap['reason'], section.select_one('.work-additional-language').get_text())
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
                # The approved pilot includes a complete five-word distinction:
                # "It promises consideration, not approval."
                self.assertGreaterEqual(len(quiz['data-explanation']), 15)
                total_questions += 1
            for link in soup.select('a[href*="#page="]'):
                self.assertTrue(1 <= int(urlparse(link['href']).fragment.split('=')[1]) <= record(track['slug'])['pdf_pages'])
            for unwanted in ('write a 70-110 word', 'ask me to write my own sentence', 'draft a two-sentence response'):
                self.assertNotIn(unwanted, soup.get_text().lower())
        self.assertEqual(len(fingerprints), 880)
        self.assertEqual(total_questions, 11200)

    def test_option_explanations_remain_attached_after_shuffling(self):
        from work_web_lessons import checks
        source = dict(prompt='Which action?', options=['A', 'B', 'C', 'D'], answer=2,
                      reasons=['Reason A', 'Reason B', 'Reason C', 'Reason D'], reason='Reason C')
        for index in range(20):
            soup = BeautifulSoup(checks([source], str(index), shuffle=True), 'html.parser')
            quiz = soup.select_one('[data-work-quiz]')
            choices = [label.span.get_text() for label in quiz.select('label')]
            reasons = [span.get_text() for span in quiz.select('.work-answer-reasons li span')]
            self.assertEqual(dict(zip(choices, reasons)), dict(zip(source['options'], source['reasons'])))
            self.assertEqual(choices[int(quiz['data-correct'])], 'C')

    def test_all_web_illustrations_come_from_the_published_book_cover(self):
        import hashlib
        from PIL import Image
        from work_web_art import art_records
        from work_web_content import publication_documents
        records = art_records()
        self.assertEqual(set(records), {t['slug'] for t in load_tracks()})
        for slug, record in records.items():
            published = publication_documents()[slug]
            self.assertEqual(record['source'], published['illustration_asset'])
            self.assertEqual(record['source_sha256'], published['illustration_sha256'])
            with Image.open(ROOT / record['source']) as original:
                ratio = original.width / original.height
            soup = BeautifulSoup((ROOT / f'efsp-{slug}.html').read_text(), 'html.parser')
            image = soup.select_one('.work-book-art img')
            self.assertTrue(image['alt'])
            self.assertEqual(int(image['width']), record['versions'][-1]['width'])
            self.assertEqual(int(image['height']), record['versions'][-1]['height'])
            for variant in record['versions']:
                path = ROOT / variant['src']
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), variant['sha256'])
                self.assertIn(variant['src'], image['srcset'])
                with Image.open(path) as art:
                    self.assertEqual(art.size, (variant['width'], variant['height']))
                    self.assertAlmostEqual(art.width / art.height, ratio, places=2)


if __name__ == '__main__':
    unittest.main()
