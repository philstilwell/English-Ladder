"""Offline exact-source menu and reference-resolution regressions."""
import copy
import unittest

from lesson_evidence import evidence_choices, resolve_evidence_references
from news_quality import evidence_text, validate_evidence


class LessonEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.news = {
            'title': 'A library opens',
            'summary': 'The library opens beside the park.',
            'evidence_text': ('The library opens beside the park.\n\n'
                              'The mayor said, “It’s open.”\nVisitors can borrow books.\n\n'
                              "Staff don't charge a fee."),
        }

    def test_menu_is_stable_ordered_deduplicated_and_exact(self):
        original = copy.deepcopy(self.news)
        choices = evidence_choices(self.news)
        self.assertEqual([
            'A library opens', 'The library opens beside the park.',
            'The mayor said, “It’s open.” Visitors can borrow books.',
            "Staff don't charge a fee.",
        ], choices)
        self.assertEqual(choices, evidence_choices(self.news))
        self.assertEqual(original, self.news)
        normalized_source = ' '.join(evidence_text(self.news).split())
        for excerpt in choices:
            self.assertGreaterEqual(len(excerpt), 8)
            self.assertIn(excerpt, normalized_source)

    def test_large_blocks_are_split_into_exact_bounded_adjacent_sentence_spans(self):
        sentences = [f'The library has a useful collection for reading group {i}.' for i in range(100)]
        source = {'evidence_text': ' '.join(sentences)}
        choices = evidence_choices(source)
        self.assertGreater(len(choices), 1)
        self.assertEqual(source['evidence_text'], ' '.join(choices))
        for excerpt in choices:
            self.assertLessEqual(len(excerpt), 1200)
            self.assertTrue(excerpt.endswith('.'))
            self.assertIn(excerpt, source['evidence_text'])
        long_sentence = 'A very long statement ' + 'with more detail ' * 150 + 'ends here.'
        spans = evidence_choices({'evidence_text': long_sentence})
        self.assertGreater(len(spans), 1)
        self.assertEqual(long_sentence, ' '.join(spans))

    def test_short_empty_fields_do_not_create_unusable_choices(self):
        self.assertEqual([], evidence_choices({'title': 'Short', 'summary': None}))
        self.assertEqual(['Exactly8'], evidence_choices({'title': 'Exactly8'}))

    def test_integer_and_repeated_references_resolve_without_mutating_the_draft(self):
        lesson = {'news_brief_sentences': ['The library opens.', 'It is beside the park.'],
                  'sentence_evidence': [1, 1], 'nested': {'values': [1]}}
        original = copy.deepcopy(lesson)
        resolved = resolve_evidence_references(lesson, self.news)
        self.assertEqual([self.news['summary']] * 2, resolved['sentence_evidence'])
        self.assertEqual([], validate_evidence(resolved, self.news))
        resolved['nested']['values'].append(2)
        self.assertEqual(original, lesson)

    def test_literal_strings_are_unchanged_and_still_subject_to_evidence_validation(self):
        literal = 'The mayor said, “It’s open.”\nVisitors can borrow books.'
        lesson = {'news_brief_sentences': ['The mayor spoke.'], 'sentence_evidence': [literal]}
        resolved = resolve_evidence_references(lesson, self.news)
        self.assertEqual(literal, resolved['sentence_evidence'][0])
        self.assertEqual([], validate_evidence(resolved, self.news))
        lesson['sentence_evidence'] = ['The mayor promised a new swimming pool.']
        self.assertTrue(validate_evidence(resolve_evidence_references(lesson, self.news), self.news))

    def test_malformed_references_fail_without_partial_mutation(self):
        for invalid in (True, False, -1, len(evidence_choices(self.news)), 1.0, None, {}, []):
            with self.subTest(reference=invalid):
                lesson = {'sentence_evidence': [0, invalid]}
                original = copy.deepcopy(lesson)
                with self.assertRaises(ValueError):
                    resolve_evidence_references(lesson, self.news)
                self.assertEqual(original, lesson)
        for lesson in (None, [], {}, {'sentence_evidence': '0'}):
            with self.subTest(lesson=lesson), self.assertRaises(ValueError):
                resolve_evidence_references(lesson, self.news)
        with self.assertRaises(ValueError):
            resolve_evidence_references({'sentence_evidence': [0]}, {})


if __name__ == '__main__':
    unittest.main()
