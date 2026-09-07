"""Publication must never accept a daily reading below the 6/8/10 minimums."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import update_site

ROOT = Path(__file__).resolve().parents[1]


class ReadingLengthTests(unittest.TestCase):
    def setUp(self):
        self.archive = json.loads((ROOT/'archive/lessons/2026-09-06.json').read_text())

    def test_every_level_rejects_below_minimum_and_accepts_minimum_and_longer(self):
        for config, minimum in zip(update_site.LEVELS, (6, 8, 10)):
            lesson = self.archive['levels'][config['name'].lower()]['lesson']
            sentences = lesson['news_brief_sentences']
            with self.subTest(level=config['name']):
                self.assertEqual(minimum, config['min_sentence_count'])
                self.assertTrue(update_site.validate_reading_length(sentences[:minimum-1], config))
                self.assertEqual([], update_site.validate_reading_length(sentences[:minimum], config))
                self.assertEqual([], update_site.validate_reading_length(sentences+['The airline published a revised timetable.'], config))
                schema = update_site.build_response_schema(config)['properties']
                for field in ('news_brief_sentences', 'sentence_evidence'):
                    self.assertEqual(minimum, schema[field]['minItems'])
                    self.assertNotIn('maxItems', schema[field])
                self.assertIn(f'at least {minimum}', update_site.build_prompt(self.archive['source'], config))

    def test_blank_non_text_punctuation_and_duplicate_entries_do_not_count(self):
        for config in update_site.LEVELS:
            original = self.archive['levels'][config['name'].lower()]['lesson']['news_brief_sentences']
            for bad in ('', '   ', None, 42, '.', '!!!', 'Delays.',
                        'This lacks terminal punctuation', original[0], original[0].upper(),
                        '  '+original[0].replace(' ', '   ')+'  '):
                with self.subTest(level=config['name'], bad=bad):
                    self.assertTrue(update_site.validate_reading_length(original[:-1]+[bad], config))
        self.assertTrue(update_site.validate_reading_length('Six sentences are not a list.', update_site.LEVELS[0]))

    def test_other_lesson_fields_cannot_make_a_short_reading_pass(self):
        for config in update_site.LEVELS:
            lesson = copy.deepcopy(self.archive['levels'][config['name'].lower()]['lesson'])
            lesson['news_brief_sentences'] = lesson['news_brief_sentences'][:-1]
            lesson['overview'] = 'A long overview. With extra sentences. And still more.'
            self.assertTrue(any('at least' in issue for issue in update_site.validate_lesson_data(lesson, config)))

    def test_generation_retries_short_drafts_then_fails_without_rendering(self):
        for config in update_site.LEVELS:
            lesson = copy.deepcopy(self.archive['levels'][config['name'].lower()]['lesson'])
            lesson['news_brief_sentences'] = lesson['news_brief_sentences'][:-1]
            with patch.object(update_site, 'render_lesson_html') as render:
                client = SimpleNamespace(models=SimpleNamespace(generate_content=lambda **kw: SimpleNamespace(text=json.dumps(lesson))))
                with self.assertRaisesRegex(RuntimeError, 'after 3 attempts.*at least'):
                    update_site.generate_lesson(client, self.archive['source'], config, update_site.release_datetime_from_date('2026-09-06'))
                render.assert_not_called()

    def test_revision_can_pass_after_a_short_draft_is_rejected(self):
        config = update_site.LEVELS[2]
        valid = self.archive['levels']['advanced']['lesson']
        short = dict(valid, news_brief_sentences=valid['news_brief_sentences'][:-1])
        responses = iter([short, valid, {'approved': True, 'issues': []}])
        calls = []
        def generate(**kwargs):
            calls.append(kwargs)
            return SimpleNamespace(text=json.dumps(next(responses)))
        client = SimpleNamespace(models=SimpleNamespace(generate_content=generate))
        lesson, markup = update_site.generate_lesson(client, self.archive['source'], config, update_site.release_datetime_from_date('2026-09-06'))
        self.assertEqual(10, len(lesson['news_brief_sentences']))
        self.assertIn('at least 10 are required', calls[1]['contents'])
        self.assertIn('minimum_reading_sentences', calls[2]['contents'])
        self.assertIn('daily-lesson', markup)

    def test_archive_writer_preserves_existing_release_when_one_level_is_short(self):
        lessons = {k: copy.deepcopy(v['lesson']) for k, v in self.archive['levels'].items()}
        lessons['advanced']['news_brief_sentences'].pop()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'2026-09-06.json'
            path.write_text('existing approved edition')
            with self.assertRaisesRegex(ValueError, 'Refusing to archive'):
                update_site.archive_daily_lessons(self.archive['source'], lessons,
                    update_site.release_datetime_from_date('2026-09-06'), archive_dir=directory)
            self.assertEqual('existing approved edition', path.read_text())

    def test_rebuild_gate_checks_unreviewed_archives_too(self):
        data = copy.deepcopy(self.archive)
        data.pop('editorial_review', None)
        data['levels']['intermediate']['lesson']['news_brief_sentences'].pop()
        with tempfile.TemporaryDirectory() as directory:
            (Path(directory)/'2026-09-06.json').write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, 'Intermediate.*at least 8'):
                update_site.require_archive_reading_lengths(directory)

    def test_one_failed_level_prevents_the_whole_daily_edition_from_being_saved(self):
        args = SimpleNamespace(refresh_feature=False, refresh_pages=False,
                               release_date='2026-09-06', skip_existing=False)
        client = SimpleNamespace(close=lambda: None)
        calls = []
        def generate(client, news, config, date):
            calls.append(config['name'])
            if config['name'] == 'Advanced':
                raise RuntimeError('Advanced reading is below the ten-sentence minimum.')
            return self.archive['levels'][config['name'].lower()]['lesson'], '<details></details>'
        with patch.object(update_site, 'parse_args', return_value=args), \
             patch.object(update_site, 'get_daily_news', return_value=self.archive['source']), \
             patch.object(update_site, 'configure_gemini', return_value=client), \
             patch.object(update_site, 'generate_lesson', side_effect=generate), \
             patch.object(update_site, 'archive_daily_lessons') as archive, \
             patch.object(update_site, 'update_level_page') as publish:
            with self.assertRaisesRegex(RuntimeError, 'below'):
                update_site.main()
            archive.assert_not_called()
            publish.assert_not_called()
        self.assertEqual(['Beginner', 'Intermediate', 'Advanced'], calls)

    def test_news_selection_tries_another_article_when_the_first_has_no_body(self):
        entries = [dict(title='A new discovery', summary='Researchers describe their discovery.', link='https://www.bbc.co.uk/news/articles/first'),
                   dict(title='A second discovery', summary='Another team shares its results.', link='https://www.bbc.co.uk/news/articles/second')]
        class Response:
            def __enter__(self):return self
            def __exit__(self, *args):pass
            def read(self, limit):return b'feed'
        with tempfile.TemporaryDirectory() as directory, \
             patch.object(update_site, 'ARCHIVE_DIR', Path(directory)), \
             patch.object(update_site, 'urlopen', return_value=Response()), \
             patch.object(update_site.feedparser, 'parse', return_value=SimpleNamespace(entries=entries)), \
             patch.object(update_site, 'fetch_article_evidence', side_effect=[ValueError('Article body unavailable'), 'Detailed reporting.']) as fetch:
            source = update_site.get_daily_news(update_site.release_datetime_from_date('2026-09-06'))
        self.assertEqual(entries[1]['link'], source['link'])
        self.assertEqual('Detailed reporting.', source['evidence_text'])
        self.assertEqual(2, fetch.call_count)

    def test_article_extraction_excludes_navigation_and_rejects_thin_sources(self):
        text = 'The reporting describes a new transport project with changes to local services. '
        paragraphs = ''.join(f'<p class="ssrcss-Paragraph">Section {i}: {text*3}</p>' for i in range(8))
        source = f'<nav>Outside the story.</nav><article><figure><p class="ssrcss-Paragraph">A caption that must not enter the evidence.</p></figure>{paragraphs}</article>'
        evidence = update_site.extract_article_evidence(source)
        self.assertIn('Section 7', evidence)
        self.assertNotIn('Outside the story', evidence)
        self.assertNotIn('A caption', evidence)
        with self.assertRaisesRegex(ValueError, 'Not enough'):
            update_site.extract_article_evidence('<article><p class="ssrcss-Paragraph">A brief headline with too little evidence for a story.</p></article>')
        with self.assertRaisesRegex(ValueError, 'unavailable'):
            update_site.extract_article_evidence('<p>This is a consent screen.</p>')


if __name__ == '__main__':
    unittest.main()
