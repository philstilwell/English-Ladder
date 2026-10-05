import unittest

from lesson_evidence import archive_evidence
from news_quality import validate_evidence


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
