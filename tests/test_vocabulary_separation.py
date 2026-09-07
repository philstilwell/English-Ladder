"""Distinct targets are required in generation, stored editions and rebuilds."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import news_quality
import site_quality
import update_site as u
from review_fixtures import approved_review, draft_response

ROOT = Path(__file__).resolve().parents[1]


class VocabularySeparationTests(unittest.TestCase):
    def setUp(self):
        self.edition = json.loads((ROOT/'archive/lessons/2026-09-06.json').read_text())
        self.lessons = {key: value['lesson'] for key, value in self.edition['levels'].items()}

    def test_reuse_includes_inflections_spelling_variants_and_reworded_phrases(self):
        pairs = [('cost', 'costs'), ('community', 'communities'), ('take swipes at', 'taking swipes at'),
                 ('mobilised', 'mobilized'), ('air defence', 'air defense systems'), ('go', 'went'),
                 ('congested', 'congestion'), ('accidents', 'accidental'), ('escalation', 'escalating'),
                 ('retaliatory tariffs', 'retaliatory measures'), ('co-operation', 'cooperation'),
                 ('warned', 'warning systems'), ('children', 'child'), ('analysis', 'analyses'),
                 ('marine threats', 'marine life')]
        for a, b in pairs:
            with self.subTest(a=a, b=b):
                self.assertTrue(u.vocabulary_conflict(a, [{'term': b, 'level': 'Earlier'}]))
                self.assertTrue(u.vocabulary_conflict(b, [{'term': a, 'level': 'Earlier'}]))

    def test_unrelated_words_and_shared_function_words_remain_available(self):
        for a, b in [('port', 'airport'), ('aid', 'said'), ('new', 'news'), ('business', 'busy'),
                     ('reach agreement', 'by choice'), ('on top of', 'a lack of'), ('delay', 'postpone')]:
            with self.subTest(a=a, b=b):
                self.assertIsNone(u.vocabulary_conflict(a, [{'term': b, 'level': 'Earlier'}]))

    def test_borrowed_items_do_not_count_towards_the_minimum(self):
        lesson = copy.deepcopy(self.lessons['intermediate'])
        lesson['vocabulary'][-1] = copy.deepcopy(self.lessons['beginner']['vocabulary'][1])
        level = dict(u.LEVELS[1], reserved_vocabulary=[{'term': i['term'], 'level': 'Beginner'} for i in self.lessons['beginner']['vocabulary']])
        issues = u.validate_vocabulary_items(lesson, level)
        self.assertTrue(any('assigned to Beginner' in e for e in issues))
        self.assertTrue(any('at least 8' in e for e in issues))
        choices = u.reading_vocabulary_choices(lesson, level)
        self.assertTrue(choices)
        self.assertFalse(any(u.vocabulary_conflict(t, level['reserved_vocabulary']) for t in choices))

    def test_borrowed_vocabulary_can_be_repaired_but_still_requires_independent_review(self):
        level = dict(u.LEVELS[1], reserved_vocabulary=[{'term': i['term'], 'level': 'Beginner'} for i in self.lessons['beginner']['vocabulary']])
        good = self.lessons['intermediate']; bad = copy.deepcopy(good)
        bad['vocabulary'][-1] = copy.deepcopy(self.lessons['beginner']['vocabulary'][1])
        values = iter([bad, good, approved_review()]); calls = []
        def generate(**request):
            calls.append(request); value = next(values)
            if 'quiz' in value:
                value = draft_response(value, request, bad, level)
            return SimpleNamespace(text=json.dumps(value))
        client = SimpleNamespace(models=SimpleNamespace(generate_content=generate))
        saved, _ = u.generate_lesson(client, self.edition['source'], level, u.release_datetime_from_date('2026-09-06'))
        self.assertEqual([], u.validate_vocabulary_items(saved, level))
        self.assertEqual(3, len(calls))
        for request in calls:
            self.assertIn('Beginner', request['contents'])
        self.assertIn('reserved_vocabulary', calls[-1]['contents'])

    def test_one_borrowed_target_prevents_overwriting_an_archive(self):
        lessons = copy.deepcopy(self.lessons)
        lessons['advanced']['vocabulary'][-1] = copy.deepcopy(lessons['beginner']['vocabulary'][0])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'2026-09-06.json'; path.write_text('previous edition')
            with self.assertRaisesRegex(ValueError, 'Refusing to archive overlapping vocabulary'):
                u.archive_daily_lessons(self.edition['source'], lessons, u.release_datetime_from_date('2026-09-06'), directory)
            self.assertEqual('previous edition', path.read_text())

    def test_overlap_in_an_unreviewed_archive_stops_rebuild_before_page_changes(self):
        data = copy.deepcopy(self.edition); data.pop('editorial_review', None)
        data['levels']['advanced']['lesson']['vocabulary'][-1] = copy.deepcopy(self.lessons['beginner']['vocabulary'][0])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); archive = root/'archive/lessons'; archive.mkdir(parents=True)
            (archive/'2026-09-06.json').write_text(json.dumps(data))
            for level in u.LEVELS: (root/level['file_path']).write_text('previous page')
            with patch.object(site_quality, 'ROOT', root), self.assertRaisesRegex(ValueError, 'each level needs distinct targets'):
                site_quality.rebuild_news_levels()
            for level in u.LEVELS: self.assertEqual('previous page', (root/level['file_path']).read_text())

    def test_generation_passes_approved_targets_forward_without_mutating_global_levels(self):
        original = copy.deepcopy(u.LEVELS); calls = []
        def generate(client, news, config, date, **resume):
            calls.append(copy.deepcopy(config))
            return copy.deepcopy(self.lessons[config['name'].lower()]), '<details></details>'
        args = SimpleNamespace(refresh_feature=False, refresh_pages=False, release_date='2026-09-06', skip_existing=False)
        client = SimpleNamespace(close=lambda: None)
        with patch.object(u, 'parse_args', return_value=args), \
             patch.object(u, 'get_daily_news', return_value=self.edition['source']), \
             patch.object(u, 'configure_gemini', return_value=client), \
             patch.object(u, 'generate_lesson', side_effect=generate), \
             patch.object(u, 'archive_daily_lessons', return_value=Path('synthetic.json')), \
             patch.object(u, 'update_level_page'), \
             patch('daily_images.ensure_daily_image'), \
             patch('editorial.publish_editorial_pages'):
            u.main()
        self.assertEqual([0, 6, 14], [len(c['reserved_vocabulary']) for c in calls])
        self.assertEqual({'Beginner', 'Intermediate'}, {i['level'] for i in calls[2]['reserved_vocabulary']})
        self.assertEqual(original, u.LEVELS)

    def test_every_archived_edition_has_separate_lists_and_retains_all_minimums(self):
        paths = sorted((ROOT/'archive/lessons').glob('*.json'))
        self.assertGreaterEqual(len(paths), 64)
        for path in paths:
            data = json.loads(path.read_text())
            lessons = {key: value['lesson'] for key, value in data['levels'].items()}
            with self.subTest(edition=path.stem):
                self.assertEqual([], u.validate_edition_vocabulary(lessons))
                for config in u.LEVELS:
                    self.assertEqual([], u.validate_daily_minimums(lessons[config['name'].lower()], config))


if __name__ == '__main__':
    unittest.main()
