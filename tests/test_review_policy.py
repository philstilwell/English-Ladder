"""Offline review-contract regressions; synthetic responses do not test model accuracy."""
import copy
import json
import unittest
from types import SimpleNamespace
from unittest.mock import Mock

import news_quality
import update_site
from lesson_levels import LEVEL_CHECKS, format_language_policy
from review_fixtures import approved_review


class ReviewPolicyTests(unittest.TestCase):
    def setUp(self):
        self.source = {
            'title': 'A new library',
            'summary': 'A library opens beside a park.',
            'link': 'https://example.invalid/synthetic-library',
            'evidence_text': 'The library opened on Monday beside the park. Visitors can borrow books.',
        }
        self.lesson = {
            'news_brief_sentences': [
                'The library opened on Monday.',
                'It is beside the park.',
                'Visitors can borrow books.',
            ],
            'sentence_evidence': [
                'The library opened on Monday beside the park.',
                'The library opened on Monday beside the park.',
                'Visitors can borrow books.',
            ],
            'grammar': {
                'concept': 'can + verb',
                'explanation': 'Use can and a verb to say what someone is allowed to do.',
                'example_quote': 'Visitors can borrow books.',
            },
        }

    def capture_review(self, level=None, review=None):
        """Inspect the actual submitted request without a model or network client."""
        generate = Mock(return_value=SimpleNamespace(text=json.dumps(
            approved_review() if review is None else review)))
        client = SimpleNamespace(models=SimpleNamespace(generate_content=generate))
        record = {}
        issues = news_quality.review_lesson(
            client, self.source, self.lesson, level or update_site.LEVELS[0],
            'synthetic-reviewer', review_record=record)
        generate.assert_called_once()
        return generate.call_args.kwargs, issues, record

    def test_writer_and_reviewer_share_all_three_uncapped_minimums(self):
        fields = (
            ('news_brief_sentences', 'minimum_reading_sentences'),
            ('vocabulary', 'minimum_vocabulary_items'),
            ('quiz', 'minimum_quiz_items'),
        )
        for level, minimum in zip(update_site.LEVELS, (6, 8, 10)):
            with self.subTest(level=level['name']):
                request, _, record = self.capture_review(level)
                prompt, data = request['contents'].rsplit('\nDATA:\n', 1)
                payload = json.loads(data)
                schema = update_site.build_response_schema(level)
                for field, payload_key in fields:
                    self.assertEqual(minimum, payload[payload_key])
                    self.assertEqual(minimum, schema['properties'][field]['minItems'])
                    self.assertNotIn('maxItems', schema['properties'][field])
                self.assertIn('lower bounds, not exact counts or upper limits', prompt)
                self.assertIn('seven valid quiz questions satisfy a minimum of six', prompt)
                policy = format_language_policy(level)
                self.assertIn(policy, prompt)
                self.assertIn(policy, update_site.build_prompt(self.source, level))
                self.assertEqual(level['cefr'], record['target_level'])

    def test_source_excerpts_may_repeat_but_must_remain_exact(self):
        self.assertEqual([], news_quality.validate_evidence(self.lesson, self.source))
        request, _, _ = self.capture_review()
        self.assertIn('same source excerpt may support multiple distinct reading sentences',
                      request['contents'])
        self.lesson['sentence_evidence'][1] = 'The library opened on Monday. It is beside the park.'
        self.assertTrue(any('exact source excerpt' in issue for issue in
                            news_quality.validate_evidence(self.lesson, self.source)))
        # Reusing supporting evidence never permits duplicate reading entries.
        self.assertTrue(update_site.validate_reading_length(
            ['The library opened on Monday.'] * 6, update_site.LEVELS[0]))

    def test_grammar_quote_is_required_reuse_and_changes_are_rejected(self):
        self.assertEqual([], update_site.validate_grammar_section(self.lesson))
        request, _, _ = self.capture_review()
        self.assertIn('grammar example_quote must be copied exactly from the News Brief',
                      request['contents'])
        self.assertIn('required quotation is not redundant padding', request['contents'])
        writer = update_site.build_prompt(self.source, update_site.LEVELS[0])
        self.assertIn('grammar example quote must be copied exactly from the News Brief', writer)
        self.lesson['grammar']['example_quote'] = 'Visitors could borrow books.'
        self.assertTrue(update_site.validate_grammar_section(self.lesson))

    def test_contextual_language_questions_and_natural_beginner_words_are_allowed(self):
        request, _, _ = self.capture_review()
        prompt = request['contents']
        self.assertIn('Contextual vocabulary and grammar questions count toward the quiz minimum', prompt)
        self.assertIn('Different learning targets can use the same reading sentence', prompt)
        self.assertIn('common beginner words such as "ideas" are acceptable vocabulary targets', prompt)
        self.assertIn('sentence frames such as "I think ..." are acceptable', prompt)
        self.assertIn('Do not demand "I believe ..."', prompt)
        self.assertIn('new real-world claims unsupported by the evidence', prompt)

    def test_review_boundaries_do_not_filter_out_a_returned_rejection(self):
        # Prevent a prompt calibration from becoming a failed-review bypass.
        issue = 'Reduce the seven quiz questions to exactly six.'
        rejected = dict(approved_review(), approved=False, issues=[issue])
        request, issues, record = self.capture_review(review=rejected)
        self.assertIn('Do not invent additional requirements', request['contents'])
        self.assertIn('Optional polish is not a blocking issue', request['contents'])
        self.assertEqual([issue], issues)
        self.assertEqual({}, record)

    def test_material_factual_errors_still_block_even_with_an_overall_pass(self):
        issue = ('Reading sentence 2 changes "would not directly set energy prices" '
                 'to "cannot set prices now". Preserve directness, timing and ability.')
        request, issues, record = self.capture_review(
            review=dict(approved_review(), issues=[issue]))
        self.assertIn('does not entail "cannot set prices now"', request['contents'])
        self.assertIn('These are factual errors, not stylistic preferences', request['contents'])
        self.assertEqual([issue], issues)
        self.assertEqual({}, record)

    def test_each_level_check_still_needs_an_explicit_pass_and_reason(self):
        request, issues, record = self.capture_review()
        self.assertEqual([], issues)
        self.assertEqual(approved_review()['level_checks'], record['level_checks'])
        schema = request['config']['response_json_schema']['properties']['level_checks']
        self.assertEqual(set(LEVEL_CHECKS), set(schema['required']))
        for name in LEVEL_CHECKS:
            with self.subTest(check=name):
                rejected = approved_review()
                rejected['level_checks'][name] = {
                    'passed': False, 'reason': 'Revise a concrete level error in this field.'}
                _, issues, record = self.capture_review(review=rejected)
                self.assertTrue(any(f'({name})' in issue for issue in issues))
                self.assertEqual({}, record)
                missing = copy.deepcopy(rejected)
                del missing['level_checks'][name]['reason']
                with self.assertRaises(ValueError):
                    self.capture_review(review=missing)

    def test_common_word_permission_does_not_waive_distinct_targets(self):
        level = dict(update_site.LEVELS[1], reserved_vocabulary=[
            {'term': 'ideas', 'level': 'Beginner'}])
        request, _, _ = self.capture_review(level)
        payload = json.loads(request['contents'].rsplit('\nDATA:\n', 1)[1])
        self.assertEqual(level['reserved_vocabulary'], payload['reserved_vocabulary'])
        self.assertIn('taught vocabulary sets must be distinct', request['contents'])
        self.assertIsNotNone(update_site.vocabulary_conflict('idea', level['reserved_vocabulary']))


if __name__ == '__main__':
    unittest.main()
