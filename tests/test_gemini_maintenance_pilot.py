"""Exercise the paid-pilot route entirely with simulated provider responses."""
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import gemini_maintenance_pilot as pilot
from vocabulary_translations import atomic_json


class PilotTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.directory = Path(folder.name)

    def client(self, responses):
        return SimpleNamespace(models=SimpleNamespace(generate_content=Mock(side_effect=responses)))

    def response(self, data):
        return SimpleNamespace(text=json.dumps(data), usage_metadata=SimpleNamespace(
            prompt_token_count=1000, candidates_token_count=200, thoughts_token_count=300))

    def test_translation_review_and_audio_share_one_ledger_and_resume_without_calls(self):
        source = pilot.translations.sources()['arrival']
        saved = pilot.translations.read_record(source)
        translated = self.response({'translations': saved['translations']})
        transcribed = self.response({'transcripts': [
            {'id': i, 'text': term, 'clear_speech': True, 'extra_speech': False}
            for i, term in enumerate(pilot.AUDIO_TERMS)]})
        client = self.client([translated, translated, transcribed])
        report = pilot.run_pilot(client, self.directory)
        self.assertTrue(report['passed'])
        self.assertEqual(3, client.models.generate_content.call_count)
        self.assertEqual(3, report['cost']['requests'])
        self.assertAlmostEqual(.00465, report['cost']['reported_usage_usd'])
        self.assertEqual(0, report['cost']['unconfirmed_reserved_usd'])
        self.assertTrue(pilot.run_pilot(client, self.directory)['passed'])
        self.assertEqual(3, client.models.generate_content.call_count)

    def test_existing_spending_blocks_both_phases_before_provider_call(self):
        atomic_json(self.directory / 'usage.json', {'requests': [{'usd': .149, 'usage': 'reported'}]})
        client = self.client([])
        report = pilot.run_pilot(client, self.directory)
        self.assertFalse(report['passed'])
        self.assertEqual(0, client.models.generate_content.call_count)
        self.assertEqual(.149, report['cost']['total_recorded_or_reserved_usd'])

    def test_failures_keep_reservations_and_do_not_retry(self):
        client = self.client([TimeoutError(), TimeoutError()])
        report = pilot.run_pilot(client, self.directory)
        self.assertFalse(report['passed'])
        self.assertEqual(2, client.models.generate_content.call_count)
        self.assertEqual(0, report['cost']['reported_usage_usd'])
        self.assertGreater(report['cost']['unconfirmed_reserved_usd'], 0)
        self.assertLess(report['cost']['total_recorded_or_reserved_usd'], .15)
        # Restart cannot replay the failed calls or discard their reservations.
        pilot.run_pilot(client, self.directory)
        self.assertEqual(2, client.models.generate_content.call_count)
