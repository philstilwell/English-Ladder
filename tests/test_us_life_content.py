import hashlib
import io
import json
import tempfile
import unittest
import wave
from pathlib import Path
from types import SimpleNamespace

from bs4 import BeautifulSoup
import us_life_content as content
import us_life_audio as audio
import us_life_audio_review as review
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

    def test_missing_audio_check_is_offline_and_daily_build_never_generates_speech(self):
        workflow = (content.ROOT / '.github/workflows/cron.yml').read_text()
        self.assertNotIn('us_life_audio.py --budget', workflow)
        source = (content.ROOT / 'us-life-audio.js').read_text()
        self.assertNotIn('speechSynthesis', source)
        self.assertNotIn('apiKey', source)


if __name__ == '__main__':
    unittest.main()
