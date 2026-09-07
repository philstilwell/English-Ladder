"""Vocabulary minimums are publication requirements, not optional prompt targets."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from bs4 import BeautifulSoup
import update_site
import site_quality

ROOT = Path(__file__).resolve().parents[1]


class VocabularyMinimumTests(unittest.TestCase):
    def setUp(self):
        self.archive = json.loads((ROOT/'archive/lessons/2026-09-06.json').read_text())

    def lesson(self, config):
        return copy.deepcopy(self.archive['levels'][config['name'].lower()]['lesson'])

    def test_below_at_and_above_each_minimum(self):
        for config, minimum in zip(update_site.LEVELS, (6, 8, 10)):
            with self.subTest(level=config['name']):
                self.assertEqual(minimum, config['min_vocabulary_count'])
                lesson = self.lesson(config)
                self.assertEqual([], update_site.validate_vocabulary_items(lesson, config))
                removed = lesson['vocabulary'].pop()
                self.assertTrue(any(f'at least {minimum}' in issue for issue in update_site.validate_lesson_data(lesson, config)))
                lesson['vocabulary'].append(removed)
                lesson['vocabulary'].append(dict(term='weather', part_of_speech='noun', definition='conditions such as rain, wind and temperature'))
                self.assertEqual([], update_site.validate_vocabulary_items(lesson, config))
                schema = update_site.build_response_schema(config)['properties']['vocabulary']
                self.assertEqual(minimum, schema['minItems'])
                self.assertNotIn('maxItems', schema)
                prompt = update_site.build_prompt(self.archive['source'], config)
                self.assertIn(f'vocabulary list MUST contain at least {minimum}', prompt)
                self.assertNotIn('3-5', prompt)

    def test_empty_malformed_and_undefined_items_cannot_pad_the_count(self):
        for config in update_site.LEVELS:
            original = self.lesson(config)
            bad_items = [None, '', {}, 'a vocabulary item']
            for field in ('term', 'part_of_speech', 'definition'):
                for bad in ('', '   ', None, 42, [], {}, '!!!'):
                    item = dict(original['vocabulary'][-1]); item[field] = bad
                    bad_items.append(item)
            echo = dict(original['vocabulary'][-1], definition=original['vocabulary'][-1]['term'])
            bad_items.append(echo)
            for bad in bad_items:
                lesson = copy.deepcopy(original); lesson['vocabulary'][-1] = bad
                with self.subTest(level=config['name'], bad=bad):
                    self.assertTrue(any('at least' in issue for issue in update_site.validate_vocabulary_items(lesson, config)))
            for bad_list in (None, {}, 'one two three four five six', 10):
                lesson = dict(original, vocabulary=bad_list)
                self.assertTrue(update_site.validate_vocabulary_items(lesson, config))

    def test_duplicates_ignore_case_spacing_and_presentation_punctuation(self):
        config = update_site.LEVELS[0]
        original = self.lesson(config)
        first = original['vocabulary'][0]
        for term in (first['term'], first['term'].upper(), '  '+first['term']+'  ', first['term']+'!'):
            lesson = copy.deepcopy(original)
            lesson['vocabulary'][-1] = dict(first, term=term)
            issues = update_site.validate_vocabulary_items(lesson, config)
            self.assertTrue(any('duplicated' in issue for issue in issues))
            self.assertTrue(any('at least 6' in issue for issue in issues))
        self.assertEqual(update_site.vocabulary_term_key('Air–traffic'), update_site.vocabulary_term_key('air traffic'))

    def test_only_complete_words_or_phrases_in_the_reading_count(self):
        for term, reading in [('aid', 'The pilot said hello.'), ('port', 'The airport is busy.'), ('plane', 'Several planes landed.'),
                              ('traffic teams', 'There was traffic. Teams waited.'), ('traffic teams', 'He saw traffic, teams and aircraft.')]:
            self.assertFalse(update_site.vocabulary_term_in_reading(term, reading))
        self.assertTrue(update_site.vocabulary_term_in_reading('air traffic', 'Air traffic is busy.'))
        self.assertTrue(update_site.vocabulary_term_in_reading('selfish response', 'She described a “selfish” response.'))
        lesson = self.lesson(update_site.LEVELS[0])
        lesson['title'] = 'Helicopters in the sky'
        lesson['overview'] = 'Helicopters are useful in this story.'
        lesson['vocabulary'][-1] = dict(term='helicopters', part_of_speech='plural noun', definition='aircraft with rotating blades')
        self.assertTrue(any('News Brief' in issue for issue in update_site.validate_vocabulary_items(lesson, update_site.LEVELS[0])))

    def test_short_vocabulary_is_retried_and_never_rendered(self):
        for config in update_site.LEVELS:
            lesson = self.lesson(config); lesson['vocabulary'].pop()
            calls = []
            def generate(**kwargs):
                calls.append(kwargs)
                return SimpleNamespace(text=json.dumps(lesson))
            client = SimpleNamespace(models=SimpleNamespace(generate_content=generate))
            with patch.object(update_site, 'render_lesson_html') as render:
                with self.assertRaisesRegex(RuntimeError, 'after 3 attempts.*vocabulary'):
                    update_site.generate_lesson(client, self.archive['source'], config, update_site.release_datetime_from_date('2026-09-06'))
                render.assert_not_called()
            self.assertEqual(3, len(calls))
            self.assertIn('vocabulary has', calls[1]['contents'])

    def test_fixed_draft_still_requires_independent_review(self):
        config = update_site.LEVELS[2]; lesson = self.lesson(config)
        short = copy.deepcopy(lesson); short['vocabulary'].pop()
        responses = iter([short, lesson, {'approved': True, 'issues': []}]); calls = []
        def generate(**kwargs):
            calls.append(kwargs)
            return SimpleNamespace(text=json.dumps(next(responses)))
        client = SimpleNamespace(models=SimpleNamespace(generate_content=generate))
        saved, rendered = update_site.generate_lesson(client, self.archive['source'], config, update_site.release_datetime_from_date('2026-09-06'))
        self.assertEqual(10, len(saved['vocabulary']))
        self.assertIn('minimum_vocabulary_items', calls[-1]['contents'])
        self.assertEqual(10, len(BeautifulSoup(rendered, 'html.parser').select('.vocab-term')))

    def test_one_short_level_prevents_overwriting_an_existing_archive(self):
        lessons = {k: copy.deepcopy(v['lesson']) for k, v in self.archive['levels'].items()}
        lessons['intermediate']['vocabulary'].pop()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'2026-09-06.json'; path.write_text('previous approved release')
            with self.assertRaisesRegex(ValueError, 'Intermediate vocabulary.*at least 8'):
                update_site.archive_daily_lessons(self.archive['source'], lessons, update_site.release_datetime_from_date('2026-09-06'), directory)
            self.assertEqual('previous approved release', path.read_text())

    def test_unreviewed_short_archive_stops_rebuild_before_any_page_changes(self):
        data = copy.deepcopy(self.archive); data.pop('editorial_review', None)
        data['levels']['beginner']['lesson']['vocabulary'].pop()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); archive = root/'archive/lessons'; archive.mkdir(parents=True)
            (archive/'2026-09-06.json').write_text(json.dumps(data))
            for config in update_site.LEVELS:(root/config['file_path']).write_text('previous page')
            with patch.object(site_quality, 'ROOT', root):
                with self.assertRaisesRegex(ValueError, 'Beginner vocabulary.*at least 6'):
                    site_quality.rebuild_news_levels()
            for config in update_site.LEVELS:self.assertEqual('previous page', (root/config['file_path']).read_text())


if __name__ == '__main__':
    unittest.main()
