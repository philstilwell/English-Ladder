"""Offline migration and spending checks; clients never contact a provider."""
import json
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

from google.genai import types

import us_life_audio_review as audio
import vocabulary_translations as translations


class MaintenanceRequestTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name)
        (self.root / 'clip.mp3').write_bytes(b'offline test recording')
        root_patch = patch.object(audio, 'ROOT', self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)
        self.entries = [('seam', {'file': 'clip.mp3', 'seconds': 2})]

    def client(self, text, usage):
        return SimpleNamespace(models=SimpleNamespace(generate_content=Mock(
            return_value=SimpleNamespace(text=json.dumps(text), usage_metadata=usage))))

    def audio_result(self):
        return {'transcripts': [{'id': 0, 'text': 'seam', 'clear_speech': True, 'extra_speech': False}]}

    def assert_request(self, client, level, output_limit):
        request = client.models.generate_content.call_args.kwargs
        self.assertEqual('gemini-3.5-flash-lite', request['model'])
        # Validate with the installed SDK as well as inspecting our request.
        config = types.GenerateContentConfig(**request['config'])
        self.assertEqual(level.upper(), config.thinking_config.thinking_level.value)
        self.assertIsNone(config.thinking_config.thinking_budget)
        self.assertEqual(output_limit, config.max_output_tokens)
        self.assertEqual('application/json', config.response_mime_type)
        self.assertIsNotNone(config.response_json_schema)

    def test_translation_prices_include_reasoning_and_keep_prior_spend(self):
        path = self.root / 'translations.json'
        prior = {'usd': .01, 'usage': 'reported', 'model': 'gemini-2.5-flash'}
        translations.atomic_json(path, {'requests': [prior]})
        budget = translations.Budget(path, .30)
        client = self.client({'entries': []}, SimpleNamespace(
            prompt_token_count=1000, candidates_token_count=200, thoughts_token_count=300))
        schema = {'type': 'object', 'properties': {'entries': {'type': 'array', 'items': {'type': 'string'}}}}
        self.assertEqual({'entries': []}, budget.request(client, 'Translate.', schema, 'medium'))
        self.assert_request(client, 'medium', 12288)
        self.assertAlmostEqual(.01155, budget.spent)
        self.assertEqual(prior, budget.data['requests'][0])
        self.assertEqual(500, budget.data['requests'][1]['output_tokens'])
        self.assertAlmostEqual(budget.spent, translations.Budget(path, .30).spent)

    def test_audio_prices_include_reasoning_and_share_generation_spend(self):
        path = self.root / 'audio.json'
        prior = {'phase': 'generation', 'usd': .50, 'usage': 'reported'}
        translations.atomic_json(path, {'requests': [prior]})
        budget = audio.AudioBudget(path, 2)
        client = self.client(self.audio_result(), SimpleNamespace(
            prompt_token_count=1000, candidates_token_count=200, thoughts_token_count=300))
        self.assertEqual(self.audio_result()['transcripts'], audio.transcribe(client, self.entries, budget))
        self.assert_request(client, 'minimal', 2048)
        self.assertAlmostEqual(.50155, budget.spent)
        self.assertEqual(prior, budget.data['requests'][0])
        self.assertEqual(500, budget.data['requests'][1]['output_tokens'])
        self.assertAlmostEqual(budget.spent, audio.AudioBudget(path, 2).spent)

    def test_audio_failure_is_saved_before_request_and_blocks_retry_at_cap(self):
        path = self.root / 'audio.json'
        budget = audio.AudioBudget(path, .01)
        client = self.client(self.audio_result(), None)
        def fail(**kwargs):
            self.assertEqual('reserved', json.loads(path.read_text())['requests'][0]['usage'])
            raise TimeoutError('offline simulated failure')
        client.models.generate_content.side_effect = fail
        with self.assertRaises(TimeoutError): audio.transcribe(client, self.entries, budget)
        resumed = audio.AudioBudget(path, .01)
        self.assertGreater(resumed.spent, .005)
        with self.assertRaisesRegex(RuntimeError, 'cap reached'):
            audio.transcribe(client, self.entries, resumed)
        self.assertEqual(1, client.models.generate_content.call_count)

    def test_partial_or_absent_usage_keeps_full_reservation(self):
        for usage in (None, SimpleNamespace(prompt_token_count=100),
                      SimpleNamespace(prompt_token_count=None, candidates_token_count=20)):
            for kind in ('translation', 'audio'):
                with self.subTest(kind=kind, usage=usage):
                    path = self.root / f'{kind}.json'
                    path.unlink(missing_ok=True)
                    if kind == 'translation':
                        budget = translations.Budget(path, .30)
                        client = self.client({'entries': []}, usage)
                        budget.request(client, 'Translate.', {}, 'medium')
                        self.assertGreater(budget.spent, .03)
                    else:
                        budget = audio.AudioBudget(path, 2)
                        client = self.client(self.audio_result(), usage)
                        audio.transcribe(client, self.entries, budget)
                        self.assertGreater(budget.spent, .005)
                    self.assertEqual('reserved', budget.data['requests'][0]['usage'])

    def test_concurrent_audio_reviews_cannot_overbook_remaining_budget(self):
        path = self.root / 'audio.json'
        prior = {'phase': 'generation', 'usd': 1.99}
        translations.atomic_json(path, {'requests': [prior]})
        budget = audio.AudioBudget(path, 2)
        client = self.client(self.audio_result(), None)
        def request(_):
            try:
                audio.transcribe(client, self.entries, budget)
                return True
            except RuntimeError:
                return False
        with ThreadPoolExecutor(max_workers=3) as pool:
            outcomes = list(pool.map(request, range(3)))
        self.assertEqual(1, sum(outcomes))
        self.assertEqual(1, client.models.generate_content.call_count)
        self.assertLessEqual(budget.spent, 2)
        self.assertEqual(prior, budget.data['requests'][0])

    def test_previous_successful_audio_review_is_still_reusable(self):
        self.assertTrue(audio.reviewed({'sha256': 'saved', 'review': {
            'model': 'gemini-2.5-flash', 'policy': audio.POLICY,
            'status': 'passed', 'audio_sha256': 'saved'}}))

    def test_invalid_audio_response_retains_reported_charge(self):
        budget = audio.AudioBudget(self.root / 'audio.json', 2)
        client = self.client({'transcripts': []}, SimpleNamespace(
            prompt_token_count=1000, candidates_token_count=200, thoughts_token_count=300))
        with self.assertRaisesRegex(ValueError, 'every recording'):
            audio.transcribe(client, self.entries, budget)
        self.assertAlmostEqual(.00155, budget.spent)
