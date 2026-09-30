import hashlib
import io
import json
import tempfile
import unittest
import wave
from contextlib import ExitStack
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from bs4 import BeautifulSoup
import us_life_content as content
import us_life_audio as audio
import us_life_audio_review as review
import us_life_audio_batch as batch_audio
from us_life_translations import sources, read_record


class EverydayContentTests(unittest.TestCase):
    def test_all_units_publish_fifteen_sentences_and_twelve_recorded_terms(self):
        soup = BeautifulSoup((content.ROOT / 'us-life.html').read_text(), 'html.parser')
        records = json.loads(audio.RECORDS.read_text())
        for key, unit in content.content().items():
            blocks = soup.find(id=key).select('.us-life-main .module-block')
            self.assertEqual(unit['sentences'], [li.get_text(' ', strip=True) for li in blocks[0].select('li')])
            self.assertEqual(12, len(blocks[1].select('dt')))
            for word, dt in zip(unit['vocabulary'], blocks[1].select('dt')):
                self.assertEqual(word['term'], dt.select_one('[data-vocabulary-term]').text)
                self.assertEqual(word['definition'], dt.find_next_sibling('dd').text)
                self.assertEqual(content.audio_path(word['term']), dt.a['href'])
                self.assertIn(word['term'], dt.a['aria-label'])
                self.assertTrue(audio.valid_record(word['term'], content.terms()[word['term']], records), word['term'])
                self.assertTrue(review.reviewed(records[word['term']]), word['term'])
            self.assertEqual('none', blocks[1].audio['preload'])
            self.assertFalse(blocks[1].audio.has_attr('src'))
            self.assertFalse(blocks[1].audio.has_attr('autoplay'))
            for prompt in soup.find(id=key).select('.ai-prompt-text'):
                self.assertNotIn('▶ Listen', prompt.text)
                self.assertIn(unit['vocabulary'][-1]['term'], prompt.text)
        for source in sources(soup).values():
            self.assertIsNotNone(read_record(source), source['unit'])
            self.assertNotIn('Select Listen', source['english_context'])

    def test_rebuild_preserves_other_lesson_sections_and_has_stable_translation_context(self):
        soup = BeautifulSoup((content.ROOT / 'us-life.html').read_text(), 'html.parser')
        def unchanged_sections():
            return [str(block) for u in soup.select('.us-life-module') for block in u.select('.module-block')[2:]]
        before = unchanged_sections()
        content.enhance_page(soup)
        rendered, context = str(soup), sources(soup)
        content.enhance_page(soup)
        self.assertEqual(rendered, str(soup))
        self.assertEqual(context, sources(soup))
        self.assertEqual(before, unchanged_sections())
        for control in soup.select('[data-pronunciation-ui]'):
            control.decompose()
        self.assertEqual(context, sources(soup))

    def test_audio_cache_rejects_missing_corrupt_and_outdated_files(self):
        term, definition = 'gas pump', 'a machine that supplies gas'
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); path = root / content.audio_path(term)
            path.parent.mkdir(parents=True); path.write_bytes(b'recording' * 200)
            record = {'policy': content.AUDIO_POLICY, 'model': audio.MODEL, 'voice': audio.VOICE,
                      'prompt': audio.prompt_for(term, definition), 'file': content.audio_path(term),
                      'seconds': 2, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
            self.assertTrue(audio.valid_record(term, definition, {term: record}, root))
            record['model'] = 'unknown-speech-model'
            self.assertFalse(audio.valid_record(term, definition, {term: record}, root))
            record['model'] = 'gemini-3.1-flash-tts-preview'
            self.assertTrue(audio.valid_record(term, definition, {term: record}, root))
            self.assertFalse(audio.valid_record(term, definition + ' changed', {term: record}, root))
            path.write_bytes(b'corrupt' * 200)
            self.assertFalse(audio.valid_record(term, definition, {term: record}, root))
            path.unlink()
            self.assertFalse(audio.valid_record(term, definition, {term: record}, root))

    def test_audio_budget_reserves_failed_calls_and_survives_restarts(self):
        class Model:
            calls = 0
            def generate_content(self, **kwargs):
                self.calls += 1
                raise OSError('temporary failure')
        client = SimpleNamespace(models=Model())
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'usage.json'
            budget = audio.AudioBudget(path, .007)
            with self.assertRaises(OSError): budget.request(client, 'term', 'say term')
            self.assertGreater(budget.spent, 0)
            resumed = audio.AudioBudget(path, .007)
            with self.assertRaises(RuntimeError): resumed.request(client, 'term', 'say term')
            self.assertEqual(1, client.models.calls)
            self.assertEqual(budget.spent, resumed.spent)

    def test_review_is_bound_to_exact_recording_and_rejects_pending_results(self):
        record = {'sha256': 'new'}
        self.assertFalse(review.reviewed(record))
        record['review'] = {'policy': review.POLICY, 'status': 'passed', 'audio_sha256': 'old'}
        self.assertFalse(review.reviewed(record))
        record['review']['audio_sha256'] = 'new'
        self.assertTrue(review.reviewed(record))
        record['review']['status'] = 'needs-review'
        self.assertFalse(review.reviewed(record))
        self.assertEqual(review.normalized('Wi-Fi'), review.normalized('wifi'))
        self.assertNotEqual(review.normalized('custom'), review.normalized('customs'))

    def test_speech_model_selection_uses_its_own_price_and_shared_cap(self):
        calls = []
        class Model:
            def generate_content(self, **kwargs):
                calls.append(kwargs['model'])
                raise OSError('temporary failure')
        client = SimpleNamespace(models=Model())
        with tempfile.TemporaryDirectory() as folder:
            budget = audio.AudioBudget(Path(folder) / 'usage.json', .025)
            with self.assertRaises(OSError): budget.request(client, 'term', 'say term')
            first = budget.spent
            with self.assertRaises(OSError):
                budget.request(client, 'term', 'say term', 'gemini-3.1-flash-tts-preview')
            self.assertAlmostEqual(first * 3, budget.spent)
            self.assertEqual([audio.MODEL, 'gemini-3.1-flash-tts-preview'], calls)
            with self.assertRaises(RuntimeError):
                budget.request(client, 'term', 'say term', 'gemini-3.1-flash-tts-preview')
            self.assertEqual(2, len(calls))

    def test_google_pcm_and_wav_formats_decode_to_the_same_samples(self):
        pcm = b'\x10\x00' * 24000
        buffer = io.BytesIO()
        with wave.open(buffer, 'wb') as stream:
            stream.setnchannels(1); stream.setsampwidth(2); stream.setframerate(24000); stream.writeframes(pcm)
        for mime, data in [('audio/L16;codec=pcm;rate=24000', pcm),
                           ('audio/L16; rate=24000; codec=pcm', pcm),
                           ('audio/wav', buffer.getvalue())]:
            self.assertEqual(pcm, audio.decode_audio([SimpleNamespace(mime_type=mime, data=data)]))
        with self.assertRaises(ValueError):
            audio.decode_audio([SimpleNamespace(mime_type='audio/L16;rate=48000', data=pcm)])
        with self.assertRaises(ValueError): audio.decode_audio([])

    def test_current_speech_separates_delivery_instructions_from_spoken_text(self):
        payload = audio.structured_speech_payload('weather alert. <long pause> shelter.', 1024)
        part = payload['contents'][0]['parts'][0]
        self.assertEqual('weather alert. <long pause> shelter.', part['text'])
        self.assertNotIn('educational', part['text'])
        self.assertIn('educational', part['speechMetadata']['style'])
        self.assertEqual('en-US', payload['generationConfig']['speechConfig']['languageCode'])
        self.assertEqual(1024, payload['generationConfig']['maxOutputTokens'])

    def test_word_list_splits_only_at_silent_boundaries_and_rejects_missing_terms(self):
        speech = b'\xdc\x05' * 14400
        silence = b'\x00\x00' * 36000
        pcm = silence + speech + silence + speech + silence + speech + silence
        clips, bounds, gap = batch_audio.split_recording(pcm, 3)
        self.assertEqual(3, len(clips))
        for clip in clips: self.assertIn(speech, clip)
        for left, right in zip(bounds, bounds[1:]): self.assertLessEqual(left[1], right[0])
        with self.assertRaises(ValueError): batch_audio.split_recording(pcm, 4)
        with self.assertRaises(ValueError): batch_audio.split_recording(silence, 1)
        with self.assertRaises(ValueError): batch_audio.split_recording(speech[:-1], 1)

    def test_batch_output_limit_is_reserved_before_any_paid_call(self):
        class Model:
            def generate_content(self, **kwargs): raise AssertionError('Must not send this request')
        with tempfile.TemporaryDirectory() as folder:
            budget = audio.AudioBudget(Path(folder)/'usage.json', .025)
            with self.assertRaises(RuntimeError):
                budget.request(SimpleNamespace(models=Model()), 'list', 'say these terms',
                               'gemini-3.1-flash-tts-preview', max_tokens=2048)
            self.assertEqual(0, budget.spent)

    def test_incomplete_word_list_recovers_without_repeating_completed_requests(self):
        pcm = b'\x00\x00' * 4800 + b'\xdc\x05' * 14400 + b'\x00\x00' * 4800
        calls = []
        def request(*args, **kwargs):
            calls.append(kwargs['spoken_text'])
            return pcm  # The two-term request is intentionally incomplete.
        def encode(data, destination):
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            return len(data)/48000, hashlib.sha256(data).hexdigest()
        with tempfile.TemporaryDirectory() as folder, ExitStack() as stack:
            root = Path(folder)
            (root/'content').mkdir()
            records = root/'content/records.json'
            budget = SimpleNamespace(request=request, spent=0, limit=2)
            client = SimpleNamespace(close=lambda: None)
            replacements = {'ROOT': root, 'RECORDS': records, 'terms': lambda: {'first': 'one', 'second': 'two'},
                'valid_record': lambda t, d, saved: t in saved and (root/saved[t]['file']).is_file(),
                'AudioBudget': lambda *args: budget, 'encode_mp3': encode}
            for name, value in replacements.items(): stack.enter_context(patch.object(batch_audio, name, value))
            stack.enter_context(patch.dict('sys.modules', {'google': SimpleNamespace(genai=SimpleNamespace(Client=lambda **k: client))}))
            stack.enter_context(patch.dict('os.environ', {'GEMINI_API_KEY': 'test-only'}))
            stack.enter_context(patch('sys.argv', ['audio', '--batch-size', '2']))
            stack.enter_context(patch.object(batch_audio.time, 'sleep'))
            self.assertEqual(0, batch_audio.main())
            self.assertEqual(['first. <long pause> second.', 'first.', 'second.'], calls)
            self.assertEqual({'first', 'second'}, set(json.loads(records.read_text())))
            self.assertEqual(0, batch_audio.main())
            self.assertEqual(3, len(calls))

    def test_missing_audio_check_is_offline_and_daily_build_never_generates_speech(self):
        workflow = (content.ROOT / '.github/workflows/cron.yml').read_text()
        self.assertNotIn('us_life_audio.py --budget', workflow)
        source = (content.ROOT / 'us-life-audio.js').read_text()
        self.assertNotIn('speechSynthesis', source)
        self.assertNotIn('apiKey', source)


if __name__ == '__main__':
    unittest.main()
