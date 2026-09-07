"""Offline persistence and recovery checks for unfinished daily editions."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from lesson_checkpoint import CheckpointStore


class LessonCheckpointTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.directory = Path(self.temporary_directory.name) / 'checkpoints'
        self.store = CheckpointStore(self.directory, '2026-09-07', 'policy-v1')
        self.source = {'title': 'A library opens', 'evidence_text': 'Readers can borrow books.'}
        self.levels = {'beginner': {'news_brief_sentences': ['The library is open.'],
                                    'editorial_checks': {'passed': True}}}
        self.drafts = {'intermediate': {'lesson': {'vocabulary': []},
                                         'issues': ['Provide at least eight terms.']}}

    def test_round_trip_preserves_partial_progress_and_input_immutability(self):
        original = copy.deepcopy((self.source, self.levels, self.drafts))
        self.assertTrue(self.store.save(self.source, self.levels, self.drafts))
        self.assertEqual(original, (self.source, self.levels, self.drafts))
        restored = self.store.load()
        self.assertEqual('2026-09-07', restored['release_date'])
        self.assertEqual('policy-v1', restored['policy_fingerprint'])
        self.assertEqual(self.source, restored['source'])
        self.assertEqual(self.levels, restored['levels'])
        self.assertEqual(self.drafts, restored['drafts'])
        restored['levels']['beginner']['news_brief_sentences'].append('Changed locally.')
        self.assertEqual(self.levels, self.store.load()['levels'])
        self.assertEqual(original, (self.source, self.levels, self.drafts))

    def test_new_checkpoint_can_contain_only_the_source(self):
        self.assertIsNone(self.store.load())
        self.assertFalse(self.directory.exists())
        self.store.save(self.source, {})
        self.assertEqual({}, self.store.load()['levels'])
        self.assertEqual({}, self.store.load()['drafts'])
        self.assertEqual(self.directory / '2026-09-07.json', self.store.path)

    def test_changed_policy_date_or_schema_does_not_reuse_data(self):
        self.store.save(self.source, self.levels, self.drafts)
        different_policy = CheckpointStore(self.directory, '2026-09-07', 'policy-v2')
        self.assertIsNone(different_policy.load())
        original = self.store.load()
        for field, value in [('release_date', '2026-09-08'), ('schema_version', 2),
                             ('schema_version', True), ('policy_fingerprint', 'policy-v2')]:
            with self.subTest(field=field, value=value):
                changed = dict(original, **{field: value})
                self.store.path.write_text(json.dumps(changed), encoding='utf-8')
                self.assertIsNone(self.store.load())

    def test_damaged_data_and_invalid_shapes_are_ignored(self):
        self.store.save(self.source, self.levels, self.drafts)
        original = self.store.load()
        changed = copy.deepcopy(original)
        changed['levels']['beginner']['editorial_checks']['passed'] = False
        malformed = [json.dumps(changed), '{"schema_version":1', 'null', '[]',
                     json.dumps(dict(original, integrity_hash='damaged')),
                     json.dumps(dict(original, source=[])),
                     json.dumps(dict(original, levels=None)),
                     json.dumps(dict(original, drafts=[]))]
        for contents in malformed:
            with self.subTest(contents=contents):
                self.store.path.write_text(contents, encoding='utf-8')
                self.assertIsNone(self.store.load())
        self.store.path.write_bytes(b'\xff\xfe')
        self.assertIsNone(self.store.load())

    def test_interrupted_atomic_replace_preserves_previous_checkpoint(self):
        self.store.save(self.source, self.levels, self.drafts)
        original = self.store.path.read_bytes()
        with patch('lesson_checkpoint.os.replace', side_effect=OSError('Disk unavailable')):
            with self.assertRaisesRegex(OSError, 'Disk unavailable'):
                self.store.save(self.source, {'beginner': {'new': 'content'}}, {})
        self.assertEqual(original, self.store.path.read_bytes())
        self.assertEqual(self.levels, self.store.load()['levels'])
        self.assertEqual([self.store.path], list(self.directory.iterdir()))

    def test_interrupted_write_preserves_previous_checkpoint(self):
        self.store.save(self.source, self.levels)
        original = self.store.path.read_bytes()
        with patch('lesson_checkpoint.os.fsync', side_effect=OSError('Write failed')):
            with self.assertRaisesRegex(OSError, 'Write failed'):
                self.store.save(self.source, {}, self.drafts)
        self.assertEqual(original, self.store.path.read_bytes())
        self.assertEqual([self.store.path], list(self.directory.iterdir()))

    def test_invalid_new_data_cannot_replace_an_existing_checkpoint(self):
        self.store.save(self.source, self.levels)
        original = self.store.path.read_bytes()
        for invalid in (float('nan'), float('inf'), object()):
            with self.subTest(invalid=invalid), self.assertRaises((TypeError, ValueError)):
                self.store.save({'invalid': invalid}, self.levels)
            self.assertEqual(original, self.store.path.read_bytes())
        with self.assertRaises(ValueError):
            self.store.save(self.source, [])
        self.assertEqual(original, self.store.path.read_bytes())

    def test_disabled_store_does_not_touch_the_filesystem(self):
        disabled = CheckpointStore(None, '2026-09-07', 'policy-v1')
        with patch('lesson_checkpoint.Path.mkdir', side_effect=AssertionError('Unexpected write')):
            self.assertIsNone(disabled.path)
            self.assertIsNone(disabled.load())
            self.assertFalse(disabled.save(self.source, self.levels, self.drafts))
        self.assertFalse(self.directory.exists())

    def test_release_date_is_strict_and_cannot_escape_the_directory(self):
        for release_date in ('../2026-09-07', '2026/09/07', '2026-9-7', '2026-02-30',
                             '2026-09-07/../../outside', '', None, 20260907):
            with self.subTest(release_date=release_date), self.assertRaises(ValueError):
                CheckpointStore(self.directory, release_date, 'policy-v1')
        for fingerprint in ('', '  ', None, 1):
            with self.subTest(fingerprint=fingerprint), self.assertRaises(ValueError):
                CheckpointStore(self.directory, '2026-09-07', fingerprint)
        self.assertFalse(self.directory.exists())


if __name__ == '__main__':
    unittest.main()
