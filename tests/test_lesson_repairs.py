"""Simulate drafting failures without paid generation or weakened publishing checks."""
import copy
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import news_quality
import update_site as u
from review_fixtures import approved_review, draft_response

ROOT = Path(__file__).resolve().parents[1]


class LessonRepairTests(unittest.TestCase):
    def setUp(self):
        self.edition = json.loads((ROOT/'archive/lessons/2026-09-06.json').read_text())
        self.level = u.LEVELS[0]
        self.lesson = self.edition['levels']['beginner']['lesson']
        self.news = self.edition['source']
        self.date = u.release_datetime_from_date('2026-09-06')

    def simulate(self, responses):
        calls = []
        values = iter(responses)
        def generate(**request):
            calls.append(request)
            value = next(values)
            if callable(value):
                value = value(request)
            return SimpleNamespace(text=json.dumps(value))
        return SimpleNamespace(models=SimpleNamespace(generate_content=generate)), calls

    def test_absent_inflection_is_repaired_without_rewriting_reading_or_grammar(self):
        bad = copy.deepcopy(self.lesson)
        bad['vocabulary'][2]['term'] = 'route'  # The reading says "routes".
        before = copy.deepcopy(bad)
        client, calls = self.simulate([bad, lambda req: draft_response(self.lesson, req, bad), approved_review()])
        saved, _ = u.generate_lesson(client, self.news, self.level, self.date)
        self.assertEqual(['vocabulary'], calls[1]['config']['response_json_schema']['required'])
        self.assertIn('vocabulary_choices', calls[1]['contents'])
        self.assertEqual(before, bad)
        for field in ('news_brief_sentences', 'sentence_evidence', 'grammar', 'quiz'):
            self.assertEqual(before[field], saved[field])
        self.assertEqual('routes', saved['vocabulary'][2]['term'].casefold())
        self.assertIn('level_checks', calls[2]['config']['response_json_schema']['required'])
        self.assertEqual(2, saved['editorial_check']['generation_attempts'])
        self.assertEqual(['vocabulary'], saved['editorial_check']['repaired_sections'])

    def test_grammar_repair_copies_the_selected_reading_sentence_exactly(self):
        bad = copy.deepcopy(self.lesson)
        bad['grammar']['example_quote'] = 'This quotation does not appear in the story.'
        fixed = copy.deepcopy(self.lesson)
        fixed['grammar']['example_quote'] = self.lesson['news_brief_sentences'][0]
        client, calls = self.simulate([bad, lambda req: draft_response(fixed, req, bad), approved_review()])
        saved, _ = u.generate_lesson(client, self.news, self.level, self.date)
        self.assertEqual(['grammar'], calls[1]['config']['response_json_schema']['required'])
        self.assertEqual(fixed['grammar']['example_quote'], saved['grammar']['example_quote'])
        self.assertNotIn('example_sentence_index', saved['grammar'])
        self.assertEqual(self.lesson['vocabulary'], saved['vocabulary'])
        self.assertEqual(self.lesson['quiz'], saved['quiz'])

    def test_multiple_local_failures_are_repaired_together(self):
        bad = copy.deepcopy(self.lesson)
        bad['vocabulary'].pop()
        bad['quiz'].pop()
        bad['grammar']['example_quote'] = 'Not in this reading.'
        issues = u.validate_lesson_data(bad, self.level)
        self.assertEqual(('vocabulary', 'grammar', 'quiz'), u.local_repair_fields(bad, self.news, self.level, issues))

    def test_invalid_patch_cannot_change_a_locked_field_and_next_attempt_can_recover(self):
        bad = copy.deepcopy(self.lesson); bad['vocabulary'].pop()
        def invalid(req):
            result = draft_response(self.lesson, req, bad)
            result['news_brief_sentences'] = ['Invented replacement.']
            return result
        client, calls = self.simulate([bad, invalid, lambda req: draft_response(self.lesson, req, bad), approved_review()])
        saved, _ = u.generate_lesson(client, self.news, self.level, self.date)
        self.assertEqual(bad['news_brief_sentences'], saved['news_brief_sentences'])
        self.assertIn('locked sections cannot be changed', calls[2]['contents'])
        self.assertEqual(3, saved['editorial_check']['generation_attempts'])

    def test_invalid_references_are_rejected_without_mutating_the_previous_draft(self):
        previous = copy.deepcopy(self.lesson)
        for field, reference in [('vocabulary', 'term_id'), ('grammar', 'example_sentence_index')]:
            schema = u.build_repair_schema(previous, self.level, (field,))
            good = draft_response(self.lesson, {'config': {'response_json_schema': schema}}, previous)
            for bad in (True, False, -1, 999999, '0', None):
                replacement = copy.deepcopy(good)
                item = replacement[field][0] if field == 'vocabulary' else replacement[field]
                item[reference] = bad
                with self.subTest(field=field, bad=bad), self.assertRaises(ValueError):
                    u.apply_lesson_repair(previous, replacement, (field,))
                self.assertEqual(self.lesson, previous)

    def test_menu_contains_exact_whole_strings_and_cannot_cross_punctuation(self):
        lesson = dict(news_brief_sentences=['Teams checked 12 routes. Pilots waited, then left.', 'Costs rose. Communities responded.'])
        choices = u.reading_vocabulary_choices(lesson)
        for valid in ('routes', 'Costs', 'Communities', 'Pilots waited'):
            self.assertIn(valid, choices)
        for invalid in ('route', 'cost', 'community', 'checked routes', 'routes Pilots', 'waited then', 'rose Communities'):
            self.assertNotIn(invalid, choices)

    def test_source_or_reading_failure_requires_a_full_revision(self):
        for field, value in [('sentence_evidence', []), ('news_brief_sentences', ['Too short.'])]:
            bad = copy.deepcopy(self.lesson); bad[field] = value; bad['vocabulary'].pop()
            issues = u.validate_lesson_data(bad, self.level) + news_quality.validate_evidence(bad, self.news)
            self.assertEqual((), u.local_repair_fields(bad, self.news, self.level, issues))
        bad = copy.deepcopy(self.lesson); bad['sentence_evidence'] = []
        client, calls = self.simulate([bad, self.lesson, approved_review()])
        u.generate_lesson(client, self.news, self.level, self.date)
        self.assertIn('news_brief_sentences', calls[1]['config']['response_json_schema']['required'])
        self.assertIn('Previous draft data', calls[1]['contents'])

    def test_successful_repair_cannot_bypass_a_failed_editorial_review(self):
        bad = copy.deepcopy(self.lesson); bad['vocabulary'].pop()
        rejected = approved_review()
        rejected['level_checks']['vocabulary'] = {'passed': False, 'reason': 'Synthetic rejection: the definition is too difficult for this level.'}
        client, calls = self.simulate([bad, lambda req: draft_response(self.lesson, req, bad), rejected, self.lesson, rejected])
        with patch.object(u, 'render_lesson_html') as render:
            with self.assertRaisesRegex(RuntimeError, 'after 3 attempts.*too difficult'):
                u.generate_lesson(client, self.news, self.level, self.date)
            render.assert_not_called()
        self.assertEqual(5, len(calls))
        self.assertIn('news_brief_sentences', calls[3]['config']['response_json_schema']['required'])
        self.assertIn('Previous draft data', calls[3]['contents'])

    def test_no_available_vocabulary_requires_new_reading_not_an_invalid_schema(self):
        bad = copy.deepcopy(self.lesson); bad['vocabulary'].pop()
        level = dict(self.level, reserved_vocabulary=[{'term': term, 'level': 'Earlier'} for term in u.reading_vocabulary_choices(bad)])
        self.assertEqual([], u.reading_vocabulary_choices(bad, level))
        issues = u.validate_lesson_data(bad, level)
        self.assertEqual((), u.local_repair_fields(bad, self.news, level, issues))


if __name__ == '__main__':
    unittest.main()
