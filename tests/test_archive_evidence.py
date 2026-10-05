import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

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

    def test_completed_edition_round_trip_retains_quantity_support(self):
        source, lessons = self.edition()
        source['evidence_text'] += '\n\nThe report surveyed 3,400 travellers.'
        lessons['advanced']['news_brief_sentences'][-1] += ' The report surveyed 3,400 travellers.'
        with tempfile.TemporaryDirectory() as directory:
            path = update_site.archive_daily_lessons(source, lessons,
                update_site.release_datetime_from_date('2026-10-05'), directory)
            saved = json.loads(path.read_text())
        for entry in saved['levels'].values():
            self.assertEqual([], validate_evidence(entry['lesson'], saved['source']))

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
