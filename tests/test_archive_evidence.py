import json
import stat
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from archive_privacy import clean_archives, public_archive, require_public_archive
from lesson_evidence import archive_evidence
from news_quality import validate_evidence
import update_site


class ArchiveEvidenceTests(unittest.TestCase):
    def test_reviewed_quantity_survives_short_selected_excerpt(self):
        source = {'evidence_text': 'The region is an AI growth zone.\n\n£8bn of investment and 3,400 jobs were promised.\n\nAn unrelated paragraph.'}
        lesson = {'news_brief_sentences': ['The AI growth zone was promised £8bn and 3,400 jobs.'],
                  'sentence_evidence': ['The region is an AI growth zone.']}
        self.assertEqual([], validate_evidence(lesson, source))
        saved = archive_evidence(source, {'advanced': lesson})
        self.assertEqual([], validate_evidence(lesson, {'evidence_text': saved}))
        self.assertNotIn('An unrelated paragraph.', saved)

    def test_invented_quantity_still_fails(self):
        source = {'evidence_text': 'The region is an AI growth zone.'}
        lesson = {'news_brief_sentences': ['The AI growth zone promises 9,999 jobs.'],
                  'sentence_evidence': ['The region is an AI growth zone.']}
        saved = archive_evidence(source, {'advanced': lesson})
        self.assertIn('Sentence 1 adds the unsupported number 9,999.',
                      validate_evidence(lesson, {'evidence_text': saved}))

    def edition(self):
        fixture = Path(__file__).parent / 'fixtures/reviewed-edition.json'
        data = json.loads(fixture.read_text())
        lessons = {key: entry['lesson'] for key, entry in data['levels'].items()}
        for lesson in lessons.values():
            lesson['editorial_check'] = {'status': 'passed'}
        return data['source'], lessons

    def test_public_edition_omits_evidence_while_private_record_retains_support(self):
        source, lessons = self.edition()
        source['evidence_text'] += '\n\nThe report surveyed 3,400 travellers.'
        lessons['advanced']['news_brief_sentences'][-1] += ' The report surveyed 3,400 travellers.'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            private = root / 'state'
            path = update_site.archive_daily_lessons(source, lessons,
                update_site.release_datetime_from_date('2026-10-05'), root / 'public',
                evidence_dir=private)
            saved = json.loads(path.read_text())
            evidence_path = private / 'editorial-evidence.json'
            record = json.loads(evidence_path.read_text())
            self.assertEqual(0o600, stat.S_IMODE(evidence_path.stat().st_mode))
            self.assertEqual(public_archive(record), saved)
            require_public_archive(saved, path.name)
            for name, entry in saved['levels'].items():
                self.assertEqual(lessons[name]['news_brief_sentences'],
                                 entry['lesson']['news_brief_sentences'])
                self.assertNotIn('sentence_evidence', entry['lesson'])
                self.assertEqual([], validate_evidence(record['levels'][name]['lesson'],
                                                       record['source']))
            self.assertNotIn('evidence_text', saved['source'])
            self.assertEqual(source['link'], saved['source']['link'])

    def test_public_destination_cannot_hold_private_evidence(self):
        source, lessons = self.edition()
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            with self.assertRaisesRegex(ValueError, 'Private evidence'):
                update_site.archive_daily_lessons(source, lessons,
                    update_site.release_datetime_from_date('2026-10-05'), public,
                    evidence_dir=public / 'subdir')
            self.assertEqual([], list(public.iterdir()))

    def test_existing_cleanup_preserves_attribution_and_is_idempotent(self):
        original = {'source': {'link': 'https://example.org', 'evidence_text': 'private'},
                    'levels': [{'lesson': {'sentence_evidence': ['private'],
                                          'news_brief_sentences': ['Public sentence.']}}]}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / '2026-10-05.json'
            path.write_text(json.dumps(original))
            with self.assertRaisesRegex(ValueError, 'private editorial evidence'):
                require_public_archive(original, path.name)
            self.assertEqual(1, clean_archives(directory))
            self.assertEqual({'source': {'link': 'https://example.org'},
                              'levels': [{'lesson': {'news_brief_sentences': ['Public sentence.']}}]},
                             json.loads(path.read_text()))
            self.assertEqual(0, clean_archives(directory))

    def test_failed_archive_preserves_existing_completed_date_file(self):
        source, lessons = self.edition()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / '2026-10-05.json'
            path.write_text('Previous complete edition')
            # Simulate a future trimming regression: fail before replacing the
            # completed-date marker, rather than discovering loss at site audit.
            with patch('lesson_evidence.archive_evidence', return_value='Missing evidence'), \
                 self.assertRaisesRegex(ValueError, 'Refusing to archive unsupported'):
                update_site.archive_daily_lessons(source, lessons,
                    update_site.release_datetime_from_date('2026-10-05'), directory)
            self.assertEqual('Previous complete edition', path.read_text())
