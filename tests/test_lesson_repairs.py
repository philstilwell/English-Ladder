"""Simulate drafting failures without paid generation or weakened publishing checks."""
import copy
import json
import os
import tempfile
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

    def test_diagnostics_keep_rejected_and_approved_drafts_outside_public_archive(self):
        bad = copy.deepcopy(self.lesson)
        bad['vocabulary'].pop()
        client, _ = self.simulate([bad, lambda req: draft_response(self.lesson, req, bad), approved_review()])
        source = dict(self.news, api_key='never copy arbitrary source fields')
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {'LESSON_DIAGNOSTICS_DIR': directory}):
            saved, _ = u.generate_lesson(client, source, self.level, self.date)
            folder = Path(directory) / '2026-09-06'
            rejected = json.loads((folder / 'beginner-1.json').read_text())
            approved = json.loads((folder / 'beginner-2.json').read_text())
            self.assertEqual('rejected', rejected['status'])
            self.assertTrue(rejected['issues'])
            self.assertEqual(bad, rejected['lesson'])
            self.assertEqual('approved', approved['status'])
            self.assertEqual([], approved['issues'])
            self.assertEqual(saved, approved['lesson'])
            self.assertNotIn('api_key', approved['source'])
            self.assertEqual(source['evidence_text'], approved['source']['evidence_text'])

    def test_diagnostics_are_disabled_unless_explicitly_configured(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(u.Path, 'mkdir') as mkdir:
            u.save_lesson_diagnostic(self.lesson, self.news, self.level, self.date, 1, [])
        mkdir.assert_not_called()

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
        self.assertIn('reading', calls[1]['config']['response_json_schema']['required'])
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
        self.assertIn('reading', calls[3]['config']['response_json_schema']['required'])
        self.assertIn('Previous draft data', calls[3]['contents'])

    def test_no_available_vocabulary_requires_new_reading_not_an_invalid_schema(self):
        bad = copy.deepcopy(self.lesson); bad['vocabulary'].pop()
        level = dict(self.level, reserved_vocabulary=[{'term': term, 'level': 'Earlier'} for term in u.reading_vocabulary_choices(bad)])
        self.assertEqual([], u.reading_vocabulary_choices(bad, level))
        issues = u.validate_lesson_data(bad, level)
        self.assertEqual((), u.local_repair_fields(bad, self.news, level, issues))

    def test_numbered_source_evidence_is_resolved_before_every_review(self):
        from lesson_evidence import evidence_choices
        choices = evidence_choices(self.news)
        drafts = []
        def full_draft(request):
            drafts.append(draft_response(self.lesson, request, news=self.news))
            return drafts[-1]
        client, calls = self.simulate([full_draft, approved_review()])
        saved, _ = u.generate_lesson(client, self.news, self.level, self.date)
        schema = calls[0]['config']['response_json_schema']
        source_id = schema['properties']['reading']['items']['properties']['source_id']
        self.assertEqual('integer', source_id['type'])
        self.assertEqual(len(choices) - 1, source_id['maximum'])
        self.assertNotIn('sentence_evidence', schema['properties'])
        self.assertNotIn('news_brief_sentences', schema['properties'])
        self.assertNotIn('example_quote', schema['properties']['grammar']['properties'])
        self.assertEqual(set(schema['required']), set(drafts[0]))
        self.assertEqual(self.lesson['news_brief_sentences'], saved['news_brief_sentences'])
        self.assertEqual(len(saved['news_brief_sentences']), len(saved['sentence_evidence']))
        self.assertEqual([choices[entry['source_id']] for entry in drafts[0]['reading']], saved['sentence_evidence'])
        self.assertEqual(self.lesson['grammar']['example_quote'], saved['grammar']['example_quote'])
        self.assertNotIn('example_sentence_index', saved['grammar'])
        self.assertNotIn('reading', saved)
        self.assertTrue(all(isinstance(quote, str) for quote in saved['sentence_evidence']))
        self.assertEqual([], news_quality.validate_evidence(saved, self.news))
        payload = json.loads(calls[1]['contents'].rsplit('\nDATA:\n', 1)[1])
        self.assertEqual(saved['sentence_evidence'], payload['lesson']['sentence_evidence'])
        self.assertEqual(saved['grammar'], payload['lesson']['grammar'])

    def test_evidence_errors_are_reported_even_when_vocabulary_also_fails(self):
        bad = copy.deepcopy(self.lesson)
        bad['vocabulary'].pop()
        bad['sentence_evidence'][0] = 'This quote was never in the source.'
        client, calls = self.simulate([bad, self.lesson, approved_review()])
        u.generate_lesson(client, self.news, self.level, self.date)
        self.assertIn('Beginner vocabulary has', calls[1]['contents'])
        self.assertIn('Sentence 1 has no valid exact source excerpt', calls[1]['contents'])

    def test_overlong_discussion_is_repaired_without_rewriting_the_lesson(self):
        bad = copy.deepcopy(self.lesson)
        bad['discussion'][1] = 'An excessively long discussion prompt. ' * 8
        client, calls = self.simulate([bad, lambda req: draft_response(self.lesson, req, bad), approved_review()])
        saved, _ = u.generate_lesson(client, self.news, self.level, self.date)
        self.assertEqual(['discussion'], calls[1]['config']['response_json_schema']['required'])
        self.assertIn('Discussion prompt 2', calls[1]['contents'])
        self.assertIn('10 and 220 characters', calls[1]['contents'])
        for field in ('news_brief_sentences', 'sentence_evidence', 'vocabulary', 'grammar', 'quiz'):
            self.assertEqual(self.lesson[field], saved[field])
        self.assertEqual(self.lesson['discussion'], saved['discussion'])


if __name__ == '__main__':
    unittest.main()
