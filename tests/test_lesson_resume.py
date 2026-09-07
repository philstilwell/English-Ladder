"""Recover interrupted editions and reviews without paid calls or weaker checks."""
import copy
import io
import json
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch
from contextlib import redirect_stdout

import lesson_run
from lesson_checkpoint import CheckpointStore
from lesson_evidence import evidence_choices, resolve_evidence_references
from lesson_levels import LANGUAGE_POLICY_VERSION
import update_site as u
from review_fixtures import approved_review


ROOT = Path(__file__).resolve().parents[1]


class LessonResumeTests(unittest.TestCase):
    def setUp(self):
        edition = json.loads((ROOT / 'archive/lessons/2026-09-06.json').read_text())
        self.source = edition['source']
        self.lessons = {name: entry['lesson'] for name, entry in edition['levels'].items()}
        self.date = u.release_datetime_from_date('2026-09-06')
        self.level = u.LEVELS[0]
        self.lesson = self.lessons['beginner']
        choices = evidence_choices(self.source)
        self.model_draft = copy.deepcopy(self.lesson)
        # Historical editions include a retired field that new drafts no longer request.
        self.model_draft.pop('prediction', None)
        sentences = self.model_draft.pop('news_brief_sentences')
        evidence = self.model_draft.pop('sentence_evidence')
        self.model_draft['reading'] = [
            {'text': sentence, 'source_id': next(index for index, text in enumerate(choices)
                                                 if ' '.join(quote.split()) in text)}
            for sentence, quote in zip(sentences, evidence)]
        self.model_draft['grammar']['example_sentence_index'] = sentences.index(
            self.model_draft['grammar'].pop('example_quote'))
        self.resolved_draft = resolve_evidence_references(self.model_draft, self.source)
        self.state_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.state_directory.cleanup)
        self.enterContext(patch.dict(os.environ, {'LESSON_STATE_DIR': self.state_directory.name}))
        # Concurrent editing of policy files must not affect this offline fixture.
        self.enterContext(patch.object(lesson_run, 'generation_policy_fingerprint', return_value='test-policy'))
        self.enterContext(patch.object(u, 'save_lesson_diagnostic'))
        self.enterContext(redirect_stdout(io.StringIO()))
        self.store = CheckpointStore(self.state_directory.name, '2026-09-06', 'test-policy')

    def approved(self, name, source=None, level=None):
        lesson = copy.deepcopy(self.lessons[name])
        level = level or next(item for item in u.LEVELS if item['name'].lower() == name)
        lesson['editorial_check'] = {
            'status': 'passed', 'target_level': level['cefr'],
            'language_policy_version': LANGUAGE_POLICY_VERSION,
            'level_checks': approved_review()['level_checks'],
        }
        lesson['editorial_check']['content_digest'] = u.lesson_approval_digest(
            lesson, source or self.source, level)
        return lesson

    def client(self, responses):
        calls = []
        values = iter(responses)

        def generate(**request):
            calls.append(request)
            value = next(values)
            if isinstance(value, Exception):
                raise value
            if callable(value):
                value = value(request)
            return SimpleNamespace(text=value if isinstance(value, str) else json.dumps(value))

        return SimpleNamespace(models=SimpleNamespace(generate_content=generate)), calls

    def test_next_run_keeps_source_and_approved_levels_and_resumes_the_current_draft(self):
        unfinished = copy.deepcopy(self.lessons['intermediate'])
        unfinished['vocabulary'].pop()
        draft_state = {'lesson': unfinished, 'attempts': 1, 'phase': 'draft',
                       'issues': ['Intermediate vocabulary needs at least eight items.'],
                       'repaired_sections': []}
        first_calls = []
        first_client = SimpleNamespace(close=Mock())

        def first_generate(client, source, level, date, *, initial_state, checkpoint):
            name = level['name'].lower()
            first_calls.append(name)
            self.assertEqual(self.source, source)
            self.assertIsNone(initial_state)
            if name == 'beginner':
                return self.approved(name, level=level), '<lesson>'
            self.assertEqual('intermediate', name)
            checkpoint(draft_state)
            raise RuntimeError('Synthetic interrupted intermediate generation')

        with patch.object(u, 'get_daily_news', return_value=self.source) as fetch, \
                patch.object(u, 'configure_gemini', return_value=first_client), \
                patch.object(u, 'generate_lesson', side_effect=first_generate):
            with self.assertRaisesRegex(RuntimeError, 'interrupted intermediate'):
                lesson_run.generate_daily_lessons(self.date)
            fetch.assert_called_once_with(self.date)
        first_client.close.assert_called_once()
        self.assertEqual(['beginner', 'intermediate'], first_calls)
        saved = self.store.load()
        self.assertEqual(self.source, saved['source'])
        self.assertEqual({'beginner'}, set(saved['levels']))
        self.assertEqual(draft_state, saved['drafts']['intermediate'])

        next_calls = []
        next_client = SimpleNamespace(close=Mock())

        def next_generate(client, source, level, date, *, initial_state, checkpoint):
            name = level['name'].lower()
            next_calls.append(name)
            self.assertEqual(self.source, source)
            self.assertEqual(draft_state if name == 'intermediate' else None, initial_state)
            expected_reserved = list(self.lessons['beginner']['vocabulary'])
            if name == 'advanced':
                expected_reserved += self.lessons['intermediate']['vocabulary']
            self.assertEqual([item['term'] for item in expected_reserved],
                             [item['term'] for item in level['reserved_vocabulary']])
            return self.approved(name, level=level), '<lesson>'

        with patch.object(u, 'get_daily_news') as fetch, \
                patch.object(u, 'configure_gemini', return_value=next_client), \
                patch.object(u, 'generate_lesson', side_effect=next_generate):
            source, lessons = lesson_run.generate_daily_lessons(self.date)
            fetch.assert_not_called()
        next_client.close.assert_called_once()
        self.assertEqual(['intermediate', 'advanced'], next_calls)
        self.assertEqual(self.source, source)
        self.assertEqual({'beginner', 'intermediate', 'advanced'}, set(lessons))
        self.assertEqual({}, self.store.load()['drafts'])
        self.assertEqual(lessons, self.store.load()['levels'])

    def test_complete_saved_edition_needs_no_provider_or_source_request(self):
        lessons, reserved = {}, []
        for base in u.LEVELS:
            name = base['name'].lower()
            lessons[name] = self.approved(name, level=dict(base, reserved_vocabulary=list(reserved)))
            reserved.extend({'term': item['term'], 'level': base['name']}
                            for item in lessons[name]['vocabulary'])
        self.store.save(self.source, lessons)
        with patch.object(u, 'configure_gemini') as configure, \
                patch.object(u, 'get_daily_news') as fetch, \
                patch.object(u, 'generate_lesson') as generate:
            source, restored = lesson_run.generate_daily_lessons(self.date)
        configure.assert_not_called()
        fetch.assert_not_called()
        generate.assert_not_called()
        self.assertEqual(self.source, source)
        self.assertEqual(lessons, restored)

    def test_reuse_rejects_changed_content_source_or_policy(self):
        approved = self.approved('beginner')
        self.assertTrue(lesson_run.reusable_lesson(approved, self.source, self.level))
        changed = copy.deepcopy(approved)
        changed['overview'] += ' Changed after approval.'
        self.assertFalse(lesson_run.reusable_lesson(changed, self.source, self.level))
        changed_source = dict(self.source, title='A different source article')
        self.assertFalse(lesson_run.reusable_lesson(approved, changed_source, self.level))
        with patch.object(lesson_run, 'generation_policy_fingerprint', return_value='new-policy'):
            self.assertFalse(lesson_run.reusable_lesson(approved, self.source, self.level))

    def test_reuse_requires_passed_complete_level_checks_and_correct_target(self):
        approved = self.approved('beginner')
        variants = []
        missing = copy.deepcopy(approved)
        del missing['editorial_check']['level_checks']['vocabulary']
        variants.append(missing)
        failed = copy.deepcopy(approved)
        failed['editorial_check']['level_checks']['register']['passed'] = False
        variants.append(failed)
        for key, value in [('status', 'failed'), ('target_level', 'C1+'),
                           ('language_policy_version', 'old-policy'), ('content_digest', 'invalid')]:
            changed = copy.deepcopy(approved)
            changed['editorial_check'][key] = value
            variants.append(changed)
        variants.append(self.lesson)
        for lesson in variants:
            with self.subTest(check=lesson.get('editorial_check')):
                self.assertFalse(lesson_run.reusable_lesson(lesson, self.source, self.level))

    def test_reuse_rechecks_current_reserved_vocabulary_and_local_minimums(self):
        approved = self.approved('beginner')
        level = dict(self.level, reserved_vocabulary=[
            {'term': approved['vocabulary'][0]['term'], 'level': 'Another level'}])
        self.assertFalse(lesson_run.reusable_lesson(approved, self.source, level))
        approved['vocabulary'].pop()
        # Even a matching digest cannot bypass the independent structural gates.
        approved['editorial_check']['content_digest'] = u.lesson_approval_digest(
            approved, self.source, self.level)
        self.assertFalse(lesson_run.reusable_lesson(approved, self.source, self.level))

    def test_changed_vocabulary_reservations_require_a_fresh_semantic_review(self):
        approved = self.approved('beginner')
        level = dict(self.level, reserved_vocabulary=[
            {'term': 'a new target from another level', 'level': 'Another level'}])
        # Local matching finds no overlap; the prior review still did not see
        # these reservations and cannot establish their semantic separation.
        self.assertEqual([], u.validate_lesson_data(approved, level))
        self.assertFalse(lesson_run.reusable_lesson(approved, self.source, level))

    def test_review_transport_outage_resumes_review_without_a_new_draft(self):
        client, first_calls = self.client([self.model_draft, TimeoutError('Temporary review outage'),
                                           TimeoutError('Temporary review outage'),
                                           TimeoutError('Temporary review outage')])
        states = []
        with patch('generation_retry.time.sleep') as sleep, patch('generation_retry.LOGGER.warning'), \
                patch.object(u, 'render_lesson_html') as render:
            with self.assertRaises(TimeoutError):
                u.generate_lesson(client, self.source, self.level, self.date,
                                  checkpoint=lambda state: states.append(copy.deepcopy(state)))
            render.assert_not_called()
        self.assertEqual(2, sleep.call_count)
        self.assertEqual(4, len(first_calls))
        self.assertEqual('review', states[-1]['phase'])
        self.assertEqual(1, states[-1]['attempts'])
        self.assertEqual(self.resolved_draft, states[-1]['lesson'])
        client, next_calls = self.client([approved_review()])
        saved, _ = u.generate_lesson(client, self.source, self.level, self.date,
                                    initial_state=states[-1])
        self.assertEqual(1, len(next_calls))
        self.assertIn('level_checks', next_calls[0]['config']['response_json_schema']['required'])
        self.assertEqual(self.lesson['news_brief_sentences'], saved['news_brief_sentences'])
        self.assertEqual(1, saved['editorial_check']['generation_attempts'])
        self.assertTrue(lesson_run.reusable_lesson(saved, self.source, self.level))

    def test_two_malformed_reviews_retain_the_same_draft_for_the_next_run(self):
        client, calls = self.client([self.model_draft, '{malformed', '{still malformed'])
        states = []
        with patch.object(u, 'render_lesson_html') as render:
            with self.assertRaisesRegex(RuntimeError, 'invalid data twice'):
                u.generate_lesson(client, self.source, self.level, self.date,
                                  checkpoint=lambda state: states.append(copy.deepcopy(state)))
            render.assert_not_called()
        self.assertEqual(3, len(calls))
        self.assertIn('reading', calls[0]['config']['response_json_schema']['required'])
        for request in calls[1:]:
            self.assertIn('level_checks', request['config']['response_json_schema']['required'])
        self.assertEqual('review', states[-1]['phase'])
        self.assertEqual(1, states[-1]['attempts'])
        self.assertEqual(self.resolved_draft, states[-1]['lesson'])
        client, resumed_calls = self.client([approved_review()])
        saved, _ = u.generate_lesson(client, self.source, self.level, self.date,
                                    initial_state=states[-1])
        self.assertEqual(1, len(resumed_calls))
        self.assertEqual(1, saved['editorial_check']['generation_attempts'])

    def test_rejections_never_auto_approve_and_draft_limits_persist_across_runs(self):
        rejection = approved_review()
        rejection['approved'] = False
        rejection['issues'] = ['Synthetic rejection: the grammar explanation has the wrong meaning.']
        state = None
        for run_number in (1, 2):
            client, calls = self.client([self.model_draft, rejection] * 3)
            states = []
            with patch.object(u, 'render_lesson_html') as render:
                with self.assertRaisesRegex(RuntimeError, 'after 3 attempts in this run'):
                    u.generate_lesson(client, self.source, self.level, self.date,
                                      initial_state=state,
                                      checkpoint=lambda value: states.append(copy.deepcopy(value)))
                render.assert_not_called()
            self.assertEqual(6, len(calls))
            state = states[-1]
            self.assertEqual(3 * run_number, state['attempts'])
            self.assertEqual('draft', state['phase'])
            self.assertIn('wrong meaning', state['issues'][0])
            self.assertNotIn('editorial_check', state['lesson'])
        client, calls = self.client([])
        with self.assertRaisesRegex(RuntimeError, 'daily limit of 6 draft attempts'):
            u.generate_lesson(client, self.source, self.level, self.date, initial_state=state)
        self.assertEqual([], calls)

    def test_a_pending_review_can_complete_at_the_daily_draft_limit(self):
        state = {'lesson': self.lesson, 'attempts': 6, 'phase': 'review', 'issues': [],
                 'repaired_sections': []}
        client, calls = self.client([approved_review()])
        saved, _ = u.generate_lesson(client, self.source, self.level, self.date, initial_state=state)
        self.assertEqual(1, len(calls))
        self.assertIn('level_checks', calls[0]['config']['response_json_schema']['required'])
        self.assertEqual(6, saved['editorial_check']['generation_attempts'])


if __name__ == '__main__':
    unittest.main()
