"""Daily quiz minimums must survive drafting, storage, rebuilding and rendering."""
from review_fixtures import approved_review, draft_response
import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from bs4 import BeautifulSoup
import audit_site
import editorial
import site_quality
import update_site

ROOT = Path(__file__).resolve().parents[1]


class QuizMinimumTests(unittest.TestCase):
    def setUp(self):
        self.archive = json.loads((ROOT/'archive/lessons/2026-09-06.json').read_text())

    def lesson(self, config):
        return copy.deepcopy(self.archive['levels'][config['name'].lower()]['lesson'])

    def test_below_at_and_above_each_minimum_without_a_ceiling(self):
        for config, minimum in zip(update_site.LEVELS, (6, 8, 10)):
            with self.subTest(level=config['name']):
                self.assertEqual(minimum, config['min_quiz_count'])
                lesson = self.lesson(config)
                self.assertEqual(minimum, len(lesson['quiz']))
                self.assertEqual([], update_site.validate_lesson_data(lesson, config))
                removed = lesson['quiz'].pop()
                self.assertTrue(any(f'at least {minimum}' in issue for issue in update_site.validate_lesson_data(lesson, config)))
                lesson['quiz'].append(removed)
                lesson['quiz'].append(dict(removed, question='Which word in the reading describes the path of a flight?'))
                self.assertEqual([], update_site.validate_quiz_items(lesson, config))
                schema = update_site.build_response_schema(config)['properties']['quiz']
                self.assertEqual(minimum, schema['minItems'])
                self.assertNotIn('maxItems', schema)
                prompt = update_site.build_prompt(self.archive['source'], config)
                self.assertIn(f'quiz MUST contain at least {minimum}', prompt)
                self.assertNotIn('4-6', prompt)

    def test_incomplete_items_do_not_satisfy_the_count(self):
        for config in update_site.LEVELS:
            original = self.lesson(config)
            bad_items = [None, '', {}, 'a quiz item']
            for field in ('question', 'options', 'correct_option_index', 'option_feedback'):
                for value in (None, '', '    ', '________', 42, [], {}):
                    bad_items.append(dict(original['quiz'][-1], **{field:value}))
            for bad in bad_items:
                with self.subTest(level=config['name'], bad=bad):
                    lesson = copy.deepcopy(original); lesson['quiz'][-1] = bad
                    self.assertTrue(any(f'at least {config["min_quiz_count"]}' in issue for issue in update_site.validate_quiz_items(lesson, config)))
            for bad in (None, {}, 10, 'six complete questions'):
                self.assertTrue(update_site.validate_quiz_items(dict(original, quiz=bad), config))

    def test_duplicates_cannot_be_hidden_by_case_spacing_punctuation_or_numbering(self):
        config = update_site.LEVELS[0]; original = self.lesson(config)
        first = original['quiz'][0]
        for prompt in (first['question'], first['question'].upper(), '  '+first['question'].replace(' ', '   '),
                       first['question'].rstrip('?')+'!', '6. '+first['question'], 'Question 6: '+first['question'], '(6) '+first['question']):
            lesson = copy.deepcopy(original); lesson['quiz'][-1] = dict(first, question=prompt)
            issues = update_site.validate_quiz_items(lesson, config)
            self.assertTrue(any('duplicates' in issue for issue in issues), prompt)
            self.assertTrue(any('at least 6' in issue for issue in issues), prompt)
        self.assertNotEqual(update_site.quiz_question_key('What happened in 2025?'), update_site.quiz_question_key('What happened in 2026?'))

    def test_choices_answer_keys_and_feedback_must_be_complete_and_unambiguous_in_structure(self):
        config = update_site.LEVELS[2]; original = self.lesson(config)
        for field, values in {
            'options': [['one','two'], ['one','two','three','four'], ['One!',' one ','Two'], ['one',42,'three'], ['one','___','three']],
            'correct_option_index': [True, False, 0.0, -1, 3, '0'],
            'option_feedback': [['A useful explanation.']*2, ['A useful explanation.']*4,
                                ['A useful explanation.','', 'Another explanation.'],
                                ['A useful explanation.',{}, 'Another explanation.'],
                                ['A useful explanation.','!!!!!!!!','Another explanation.']]
        }.items():
            for value in values:
                lesson = copy.deepcopy(original); lesson['quiz'][-1][field] = value
                issues = update_site.validate_quiz_items(lesson, config)
                self.assertTrue(any('at least 10' in issue for issue in issues), (field,value))
        # Extra valid questions must not excuse a malformed or duplicated extra item.
        for extra in ({}, original['quiz'][0]):
            lesson = copy.deepcopy(original); lesson['quiz'].append(extra)
            self.assertTrue(update_site.validate_quiz_items(lesson, config))

    def test_short_quiz_is_retried_three_times_and_never_rendered(self):
        for config in update_site.LEVELS:
            lesson = self.lesson(config); lesson['quiz'].pop(); calls = []
            def generate(**kwargs):
                calls.append(kwargs)
                return SimpleNamespace(text=json.dumps(draft_response(lesson, kwargs)))
            client = SimpleNamespace(models=SimpleNamespace(generate_content=generate))
            with patch.object(update_site, 'render_lesson_html') as render:
                with self.assertRaisesRegex(RuntimeError, 'after 3 attempts.*quiz'):
                    update_site.generate_lesson(client, self.archive['source'], config, update_site.release_datetime_from_date('2026-09-06'))
                render.assert_not_called()
            self.assertEqual(3, len(calls))
            self.assertIn('quiz has', calls[1]['contents'])

    def test_fixed_draft_still_requires_an_independent_editorial_review(self):
        config = update_site.LEVELS[2]; lesson = self.lesson(config)
        short = copy.deepcopy(lesson); short['quiz'].pop()
        responses = iter([short, lesson, approved_review()]); calls=[]
        def generate(**kwargs):
            calls.append(kwargs)
            value = next(responses)
            return SimpleNamespace(text=json.dumps(draft_response(value, kwargs, short) if 'quiz' in value else value))
        client = SimpleNamespace(models=SimpleNamespace(generate_content=generate))
        saved, rendered = update_site.generate_lesson(client, self.archive['source'], config, update_site.release_datetime_from_date('2026-09-06'))
        self.assertEqual(10, len(saved['quiz']))
        self.assertIn('"minimum_quiz_items": 10', calls[-1]['contents'])
        self.assertIn('never waive the minimum', calls[-1]['contents'])
        self.assertEqual(10, len(BeautifulSoup(rendered, 'html.parser').select('.quiz-question')))

    def test_one_short_level_prevents_overwriting_an_existing_archive(self):
        lessons = {k:copy.deepcopy(v['lesson']) for k,v in self.archive['levels'].items()}
        lessons['intermediate']['quiz'].pop()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'2026-09-06.json'; path.write_text('previous approved release')
            with self.assertRaisesRegex(ValueError, 'Intermediate quiz.*at least 8'):
                update_site.archive_daily_lessons(self.archive['source'], lessons, update_site.release_datetime_from_date('2026-09-06'), directory)
            self.assertEqual('previous approved release', path.read_text())

    def test_unreviewed_old_short_archive_stops_rebuild_before_page_changes(self):
        data = copy.deepcopy(self.archive); data.pop('editorial_review', None)
        data['levels']['beginner']['lesson']['quiz'].pop()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); archive = root/'archive/lessons'; archive.mkdir(parents=True)
            # An archive older than the rolling feed is still subject to the gate.
            for index in range(15):
                (archive/f'2026-08-{index+1:02}.json').write_text(json.dumps(self.archive))
            (archive/'2026-07-01.json').write_text(json.dumps(data))
            for config in update_site.LEVELS:(root/config['file_path']).write_text('previous page')
            with patch.object(site_quality, 'ROOT', root):
                with self.assertRaisesRegex(ValueError, 'Beginner quiz.*at least 6'):
                    site_quality.rebuild_news_levels()
            for config in update_site.LEVELS:self.assertEqual('previous page', (root/config['file_path']).read_text())

    def test_publication_audit_catches_lost_questions_wrong_totals_and_misaligned_feedback(self):
        config = update_site.LEVELS[2]; lesson = self.lesson(config)
        markup = update_site.render_lesson_html(lesson, config, update_site.release_datetime_from_date('2026-09-06'))
        node = BeautifulSoup(markup, 'html.parser').select_one('.daily-lesson')
        editorial.enhance_lesson(node, 'advanced')
        self.assertEqual([], audit_site.validate_rendered_quiz(node, lesson))
        mutations = [
            lambda n: n.select('.quiz-question')[-1].decompose(),
            lambda n: setattr(n.select_one('.practice-progress'), 'string', '0 of 4 questions answered'),
            lambda n: n.select_one('.quiz-question button').__setitem__('data-feedback','Correct: A mismatched explanation.'),
            lambda n: n.select_one('.quiz-question button[data-bg="#ffe6e6"]').__setitem__('data-bg','#e6ffe6'),
            lambda n: setattr(n.select_one('.quiz-question p'), 'string', '1. An unrelated question?'),
        ]
        for mutate in mutations:
            broken = copy.deepcopy(node); mutate(broken)
            self.assertTrue(audit_site.validate_rendered_quiz(broken, lesson))


if __name__ == '__main__':
    unittest.main()
