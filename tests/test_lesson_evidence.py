"""Offline exact-source menu and reference-resolution regressions."""
import copy
import unittest

from lesson_evidence import evidence_choices, generation_schema, resolve_evidence_references
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

    def wire_lesson(self):
        return {
            'reading': [{'text': 'The library opens.', 'source_id': 1},
                        {'text': 'It is beside the park.', 'source_id': 1}],
            'vocabulary': [{'term': 'beside', 'part_of_speech': 'preposition',
                            'definition': 'Next to something.'}],
            'grammar': {'concept': 'The verb be',
                        'explanation': 'Is describes where the library is.',
                        'example_sentence_index': 1},
        }

    def test_generation_schema_binds_reading_and_source_and_preserves_base_constraints(self):
        import update_site
        for level in update_site.LEVELS:
            with self.subTest(level=level['name']):
                base = update_site.build_response_schema(level)
                original = copy.deepcopy(base)
                schema = generation_schema(base, self.news)
                self.assertEqual(original, base)
                for old in ('news_brief_sentences', 'sentence_evidence'):
                    self.assertNotIn(old, schema['required'])
                    self.assertNotIn(old, schema['properties'])
                self.assertIn('reading', schema['required'])
                reading = schema['properties']['reading']
                self.assertEqual(level['min_sentence_count'], reading['minItems'])
                self.assertNotIn('maxItems', reading)
                self.assertEqual({'text', 'source_id'}, set(reading['items']['required']))
                self.assertFalse(reading['items']['additionalProperties'])
                fields = reading['items']['properties']
                self.assertEqual(original['properties']['news_brief_sentences']['items'], fields['text'])
                self.assertEqual({'type': 'integer', 'minimum': 0,
                                  'maximum': len(evidence_choices(self.news)) - 1}, fields['source_id'])
                grammar = schema['properties']['grammar']
                self.assertNotIn('example_quote', grammar['properties'])
                self.assertNotIn('example_quote', grammar['required'])
                self.assertIn('example_sentence_index', grammar['required'])
                self.assertEqual({'type': 'integer', 'minimum': 0},
                                 grammar['properties']['example_sentence_index'])
                self.assertEqual(original['properties']['vocabulary'], schema['properties']['vocabulary'])
                schema['properties']['vocabulary']['minItems'] = 999
                self.assertEqual(original, base)
        with self.assertRaises(ValueError):
            generation_schema(base, {})

    def test_paired_reading_resolves_equal_length_arrays_and_exact_grammar_quote(self):
        wire = self.wire_lesson()
        original = copy.deepcopy(wire)
        resolved = resolve_evidence_references(wire, self.news)
        self.assertNotIn('reading', resolved)
        self.assertEqual([entry['text'] for entry in wire['reading']], resolved['news_brief_sentences'])
        self.assertEqual([self.news['summary']] * 2, resolved['sentence_evidence'])
        self.assertEqual(len(resolved['news_brief_sentences']), len(resolved['sentence_evidence']))
        self.assertEqual(resolved['news_brief_sentences'][1], resolved['grammar']['example_quote'])
        self.assertNotIn('example_sentence_index', resolved['grammar'])
        self.assertEqual([], validate_evidence(resolved, self.news))
        self.assertEqual(original, wire)
        resolved['vocabulary'][0]['definition'] = 'A changed nested value.'
        self.assertEqual(original, wire)

    def test_grammar_index_copies_actual_text_including_quotation_marks_and_whitespace(self):
        wire = self.wire_lesson()
        wire['reading'][1] = {'text': 'The mayor said, “It’s open.”\n', 'source_id': 2}
        resolved = resolve_evidence_references(wire, self.news)
        self.assertEqual(wire['reading'][1]['text'], resolved['grammar']['example_quote'])
        for index in (True, False, -1, 2, 1.0, '1', None, [], {}):
            with self.subTest(index=index):
                bad = self.wire_lesson()
                bad['grammar']['example_sentence_index'] = index
                original = copy.deepcopy(bad)
                with self.assertRaises(ValueError):
                    resolve_evidence_references(bad, self.news)
                self.assertEqual(original, bad)

    def test_malformed_paired_reading_cannot_produce_partly_resolved_lesson(self):
        bad_entries = [None, 'A sentence.', [], {}, {'text': 'A sentence.'},
                       {'text': 'A sentence.', 'source_id': 0, 'extra': 'unexpected'},
                       {'text': True, 'source_id': 0}, {'text': None, 'source_id': 0}]
        bad_entries.extend({'text': 'A sentence.', 'source_id': index}
                           for index in (True, False, -1, 4, '1', 1.0, None, {}, []))
        for entry in bad_entries:
            with self.subTest(entry=entry):
                wire = self.wire_lesson()
                wire['reading'][1] = entry
                original = copy.deepcopy(wire)
                with self.assertRaises(ValueError):
                    resolve_evidence_references(wire, self.news)
                self.assertEqual(original, wire)
        for reading in (None, {}, 'A sentence.', []):
            with self.subTest(reading=reading):
                wire = self.wire_lesson()
                wire['reading'] = reading
                with self.assertRaises(ValueError):
                    resolve_evidence_references(wire, self.news)

    def test_mixed_wire_and_canonical_fields_are_rejected(self):
        for field in ('news_brief_sentences', 'sentence_evidence'):
            with self.subTest(field=field):
                wire = self.wire_lesson()
                wire[field] = []
                with self.assertRaises(ValueError):
                    resolve_evidence_references(wire, self.news)
        for grammar in (None, {}, {'concept': 'A concept', 'explanation': 'An explanation',
                                  'example_quote': 'It is beside the park.'}):
            with self.subTest(grammar=grammar):
                wire = self.wire_lesson()
                wire['grammar'] = grammar
                with self.assertRaises(ValueError):
                    resolve_evidence_references(wire, self.news)
        wire = self.wire_lesson()
        wire['grammar']['example_quote'] = 'It is beside the park.'
        with self.assertRaises(ValueError):
            resolve_evidence_references(wire, self.news)

    def test_legacy_canonical_reading_and_literal_grammar_quote_remain_supported(self):
        lesson = {'news_brief_sentences': ['Visitors can borrow books.'],
                  'sentence_evidence': ['Visitors can borrow books.'],
                  'grammar': {'concept': 'can + verb', 'explanation': 'Can expresses permission here.',
                              'example_quote': 'Visitors can borrow books.'}}
        original = copy.deepcopy(lesson)
        self.assertEqual(original, resolve_evidence_references(lesson, self.news))
        self.assertEqual(original, lesson)
        lesson['grammar']['example_sentence_index'] = 0
        with self.assertRaises(ValueError):
            resolve_evidence_references(lesson, self.news)


if __name__ == '__main__':
    unittest.main()
