import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from bs4 import BeautifulSoup
import vocabulary_translations as translations
from story_lessons import STORIES
from update_site import LEVELS, render_lesson_html, release_datetime_from_date


class VocabularyTranslationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.lesson = copy.deepcopy(STORIES[0]['levels']['beginner'])
        self.source = translations.source_data(self.lesson, 'beginner')
        self.entries = [dict(id=i, ja='物の大きさや量を小さくすること。', ko='어떤 것의 크기나 양을 줄이는 것.',
                             **{'zh-Hans': '使某事物的大小或数量减少。', 'es': 'Hacer algo más pequeño.',
                                'pt-BR': 'Tornar algo menor.'}) for i in range(3)]

    def store(self):
        translations.atomic_json(self.directory / (translations.source_key(self.source) + '.json'),
                                 {'source': self.source, 'entries': self.entries, 'review': {'status': 'reviewed'}})

    def test_unreviewed_wrong_context_and_corrupt_records_fall_back_to_english(self):
        self.assertEqual([], translations.lesson_definitions(self.lesson, 'beginner', self.directory))
        self.store()
        self.assertEqual(3, len(translations.lesson_definitions(self.lesson, 'beginner', self.directory)))
        for field in ('definition', 'term', 'part_of_speech'):
            changed = copy.deepcopy(self.lesson)
            changed['vocabulary'][0][field] += ' changed'
            self.assertEqual([], translations.lesson_definitions(changed, 'beginner', self.directory))
        changed = copy.deepcopy(self.lesson)
        changed['news_brief_sentences'][0] += ' Changed context.'
        self.assertEqual([], translations.lesson_definitions(changed, 'beginner', self.directory))
        self.assertEqual([], translations.lesson_definitions(self.lesson, 'advanced', self.directory))
        path = self.directory / (translations.source_key(self.source) + '.json')
        record = json.loads(path.read_text()); record['review']['status'] = 'draft'
        translations.atomic_json(path, record)
        self.assertIsNone(translations.read_record(self.source, self.directory))
        path.write_text('{bad JSON')
        self.assertIsNone(translations.read_record(self.source, self.directory))

    def test_missing_languages_wrong_order_and_wrong_scripts_are_rejected(self):
        invalid = []
        wrong = copy.deepcopy(self.entries); wrong[0].pop('pt-BR'); invalid.append(wrong)
        wrong = copy.deepcopy(self.entries); wrong[0]['id'] = 2; invalid.append(wrong)
        wrong = copy.deepcopy(self.entries); wrong[0]['ko'] = 'This is English.'; invalid.append(wrong)
        wrong = copy.deepcopy(self.entries); wrong[0]['zh-Hans'] = 'これは中国語ではありません。'; invalid.append(wrong)
        wrong = copy.deepcopy(self.entries); wrong[0]['es'] = '<script>bad()</script>'; invalid.append(wrong)
        wrong = copy.deepcopy(self.entries); wrong[0]['ja'] = ''; invalid.append(wrong)
        invalid.append(self.entries[:2])
        for entries in invalid:
            with self.assertRaises(ValueError): translations.validate_entries(entries, self.source)

    def test_english_renders_without_javascript_and_translations_are_escaped(self):
        self.entries[0]['es'] = 'Una definición con "comillas" y un signo <.'
        self.store()
        with patch.object(translations, 'CACHE_DIR', self.directory):
            markup = render_lesson_html(self.lesson, LEVELS[0], release_datetime_from_date('2026-09-08'))
        soup = BeautifulSoup(markup, 'html.parser')
        span = soup.select_one('.vocab-definition')
        self.assertEqual(self.lesson['vocabulary'][0]['definition'], span.get_text())
        self.assertEqual('en', span['lang'])
        self.assertEqual(self.entries[0]['es'], json.loads(span['data-translations'])['es'])
        self.assertEqual(3, len(soup.select('.vocab-definition')))

    def test_separate_review_and_retry_reuse_saved_draft(self):
        class FakeBudget:
            def __init__(self, entries, fail_review): self.calls = []; self.entries = entries; self.fail_review = fail_review
            def request(self, client, prompt, schema, thinking):
                self.calls.append(prompt)
                if 'INDEPENDENT REVIEW:' in prompt and self.fail_review: raise ValueError('temporary review failure')
                return {'entries': self.entries}
        failed = FakeBudget(self.entries, True)
        with self.assertRaises(RuntimeError):
            translations.translate_lesson(None, self.source, failed, self.directory)
        self.assertEqual(1, sum('INDEPENDENT REVIEW:' not in prompt for prompt in failed.calls))
        self.assertIsNone(translations.read_record(self.source, self.directory))
        recovered = FakeBudget(self.entries, False)
        translations.translate_lesson(None, self.source, recovered, self.directory)
        self.assertEqual(1, len(recovered.calls))
        self.assertIn('INDEPENDENT REVIEW:', recovered.calls[0])
        self.assertIsNotNone(translations.read_record(self.source, self.directory))
        self.assertEqual('cached', translations.translate_lesson(None, self.source, recovered, self.directory))
        self.assertEqual(1, len(recovered.calls))

    def test_budget_survives_restart_and_never_sends_over_budget_request(self):
        calls = []
        def fail(**kwargs): calls.append(kwargs); raise TimeoutError()
        client = SimpleNamespace(models=SimpleNamespace(generate_content=fail))
        budget = translations.Budget(self.directory / '.usage-test.json', .04)
        with self.assertRaises(TimeoutError): budget.request(client, 'Translate.', {}, 0)
        restarted = translations.Budget(budget.path, .04)
        self.assertGreater(restarted.spent, 0)
        with self.assertRaisesRegex(RuntimeError, 'spending limit'): restarted.request(client, 'Translate.', {}, 0)
        self.assertEqual(1, len(calls))

    def test_offline_archive_inventory_includes_all_daily_and_evergreen_lessons(self):
        sources = list(translations.lessons_to_translate(True))
        expected = len(list((translations.ROOT / 'archive/lessons').glob('*.json'))) * 3 + len(STORIES) * 3
        self.assertEqual(expected, len(sources))
        self.assertEqual(len(sources), len({translations.source_key(source) for _, source in sources}))

