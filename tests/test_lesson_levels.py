"""Every future lesson needs explicit vocabulary and register approval."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import lesson_levels
import news_quality
import update_site
from review_fixtures import approved_review

ROOT = Path(__file__).resolve().parents[1]


class LessonLevelTests(unittest.TestCase):
    def setUp(self):
        self.archive = json.loads((ROOT/'archive/lessons/2026-09-06.json').read_text())

    def test_drafter_and_reviewer_receive_the_same_level_specific_policy(self):
        policies = set()
        for config in update_site.LEVELS:
            lesson = self.archive['levels'][config['name'].lower()]['lesson']
            policy = lesson_levels.format_language_policy(config)
            policies.add(policy)
            self.assertIn(policy, update_site.build_prompt(self.archive['source'], config))
            calls = []
            def generate(**kwargs):
                calls.append(kwargs)
                return SimpleNamespace(text=json.dumps(approved_review()))
            record = {}
            client = SimpleNamespace(models=SimpleNamespace(generate_content=generate))
            self.assertEqual([], news_quality.review_lesson(client, self.archive['source'], lesson, config, 'fake', review_record=record))
            self.assertIn(policy, calls[0]['contents'])
            self.assertIn('all three options', policy)
            self.assertIn('every feedback explanation', policy)
            self.assertIn('definition', policy.lower())
            schema = calls[0]['config']['response_json_schema']
            self.assertIn('level_checks', schema['required'])
            self.assertEqual(set(lesson_levels.LEVEL_CHECKS), set(schema['properties']['level_checks']['required']))
            self.assertEqual(config['cefr'], record['target_level'])
        self.assertEqual(3, len(policies))

    def test_an_overall_approval_cannot_override_any_failed_level_check(self):
        for name in lesson_levels.LEVEL_CHECKS:
            review = approved_review()
            review['level_checks'][name] = {'passed':False, 'reason':'Revise this wording to fit the target level.'}
            issues = news_quality.validate_editorial_review(review)
            self.assertTrue(any(f'({name})' in issue for issue in issues))
            self.assertTrue(any('Revise this wording' in issue for issue in issues))

    def test_missing_malformed_or_unexplained_checks_never_count_as_approval(self):
        bad_checks = [None, {}, [], True]
        for name in lesson_levels.LEVEL_CHECKS:
            checks = approved_review()['level_checks']; del checks[name]; bad_checks.append(checks)
            for value in [None, {}, {'passed':'true','reason':'This explanation is long enough.'},
                          {'passed':1,'reason':'This explanation is long enough.'},
                          {'passed':True,'reason':''}, {'passed':True,'reason':'       '},
                          {'passed':True,'reason':42}, {'reason':'There is no explicit decision.'}]:
                checks = approved_review()['level_checks']; checks[name] = value; bad_checks.append(checks)
        for checks in bad_checks:
            with self.subTest(checks=checks), self.assertRaises(ValueError):
                news_quality.validate_editorial_review(dict(approved_review(), level_checks=checks))
        with self.assertRaises(ValueError):
            news_quality.validate_editorial_review({'approved':True, 'issues':[]})

    def test_bad_register_causes_revision_then_retains_the_successful_assessments(self):
        for config in update_site.LEVELS:
            lesson = copy.deepcopy(self.archive['levels'][config['name'].lower()]['lesson'])
            failed = approved_review()
            failed['level_checks']['register'] = {'passed':False, 'reason':'Revise the overly formal teaching explanation into natural language.'}
            responses = iter([lesson, failed, lesson, approved_review()]); calls=[]
            def generate(**kwargs):
                calls.append(kwargs)
                return SimpleNamespace(text=json.dumps(next(responses)))
            client = SimpleNamespace(models=SimpleNamespace(generate_content=generate))
            saved, rendered = update_site.generate_lesson(client, self.archive['source'], config, update_site.release_datetime_from_date('2026-09-06'))
            self.assertEqual(4, len(calls))
            self.assertIn('Level suitability failed (register)', calls[2]['contents'])
            self.assertIn('Revise the overly formal', calls[2]['contents'])
            self.assertTrue(rendered)
            record = saved['editorial_check']
            self.assertEqual(lesson_levels.LANGUAGE_POLICY_VERSION, record['language_policy_version'])
            self.assertEqual(config['cefr'], record['target_level'])
            self.assertEqual(approved_review()['level_checks'], record['level_checks'])
            lessons={key:copy.deepcopy(value['lesson']) for key,value in self.archive['levels'].items()}
            lessons[config['name'].lower()] = saved
            with tempfile.TemporaryDirectory() as directory:
                path=update_site.archive_daily_lessons(self.archive['source'], lessons, update_site.release_datetime_from_date('2026-09-06'), directory)
                restored=json.loads(path.read_text())['levels'][config['name'].lower()]['lesson']['editorial_check']
                self.assertEqual(record, restored)

    def test_repeated_vocabulary_failures_or_missing_reviews_never_reach_the_renderer(self):
        config = update_site.LEVELS[0]
        lesson = self.archive['levels']['beginner']['lesson']
        failed = approved_review()
        failed['level_checks']['vocabulary'] = {'passed':False, 'reason':'Replace unnecessary specialist terms or explain essential terms simply.'}
        for review in (failed, {'approved':True, 'issues':[]}):
            calls=[]
            def generate(**kwargs):
                calls.append(kwargs)
                return SimpleNamespace(text=json.dumps(lesson if len(calls)%2 else review))
            client = SimpleNamespace(models=SimpleNamespace(generate_content=generate))
            with patch.object(update_site, 'render_lesson_html') as render:
                with self.assertRaisesRegex(RuntimeError, 'after 3 attempts'):
                    update_site.generate_lesson(client, self.archive['source'], config, update_site.release_datetime_from_date('2026-09-06'))
                render.assert_not_called()
            self.assertEqual(6, len(calls))

    def test_a_failed_review_does_not_leave_an_approval_record(self):
        review = approved_review(); review['level_checks']['challenge']['passed'] = False
        client = SimpleNamespace(models=SimpleNamespace(generate_content=lambda **kwargs: SimpleNamespace(text=json.dumps(review))))
        record = {}
        self.assertTrue(news_quality.review_lesson(client, self.archive['source'], self.archive['levels']['advanced']['lesson'], update_site.LEVELS[2], 'fake', review_record=record))
        self.assertEqual({}, record)


if __name__ == '__main__':
    unittest.main()
