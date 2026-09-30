"""Create reusable cloud pronunciation recordings; never run during daily publishing."""
from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
import os
import re
import subprocess
import tempfile
import threading
import time
import wave
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

from us_life_content import ROOT, AUDIO_POLICY, audio_path, terms
from vocabulary_translations import atomic_json

MODEL = 'gemini-2.5-flash-preview-tts'
MODEL_PRICES = {MODEL: (.5, 10), 'gemini-2.5-pro-preview-tts': (1, 20),
                'gemini-3.1-flash-tts-preview': (1, 20),
                # Reserve at the published 2027 rate, above the 2026 introductory rate.
                'gemini-3.8-flash-lite-tts': (1, 12)}
VOICE = 'Kore'
MAX_TOKENS = 512
RECORDS = ROOT / 'content/us-life-audio.json'


def structured_speech_payload(text, max_tokens):
    return {'contents': [{'role': 'user', 'parts': [{'text': text,
            'speechMetadata': {'style': 'Clear, relaxed educational pronunciation'}}]}],
            'generationConfig': {'responseModalities': ['AUDIO'], 'maxOutputTokens': max_tokens,
                'speechConfig': {'languageCode': 'en-US',
                    'voiceConfig': {'prebuiltVoiceConfig': {'voiceName': VOICE}}}}}


def current_speech_request(model, text, max_tokens):
    # The project's pinned SDK predates speechMetadata. Use Google's documented
    # REST schema without upgrading unrelated daily-generation dependencies.
    payload = structured_speech_payload(text, max_tokens)
    request = urllib.request.Request(
        f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent',
        data=json.dumps(payload).encode(), method='POST',
        headers={'Content-Type': 'application/json', 'x-goog-api-key': os.environ['GEMINI_API_KEY']})
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            data = json.load(response)
    except urllib.error.HTTPError as error:
        try: details = json.loads(error.read())
        except (ValueError, OSError): details = {}
        failure = RuntimeError(f'Speech provider returned HTTP {error.code}')
        failure.code, failure.details = error.code, details
        raise failure from None
    usage = data.get('usageMetadata', {})
    candidates = []
    for candidate in data.get('candidates', []):
        parts = [SimpleNamespace(inline_data=SimpleNamespace(
            mime_type=p['inlineData']['mimeType'], data=base64.b64decode(p['inlineData']['data'], validate=True)))
            for p in candidate.get('content', {}).get('parts', []) if 'inlineData' in p]
        candidates.append(SimpleNamespace(finish_reason=candidate.get('finishReason'),
                                         content=SimpleNamespace(parts=parts)))
    return SimpleNamespace(candidates=candidates, usage_metadata=SimpleNamespace(
        prompt_token_count=usage.get('promptTokenCount'), candidates_token_count=usage.get('candidatesTokenCount')))


def decode_audio(blobs):
    chunks = []
    for blob in blobs:
        mime = blob.mime_type.lower()
        data = blob.data
        if data.startswith(b'RIFF') or mime.split(';')[0] in ('audio/wav', 'audio/x-wav', 'audio/wave'):
            with wave.open(io.BytesIO(data), 'rb') as recording:
                if (recording.getnchannels(), recording.getsampwidth(), recording.getframerate()) != (1, 2, 24000):
                    raise ValueError('Expected mono, 16-bit, 24 kHz WAV audio.')
                chunks.append(recording.readframes(recording.getnframes()))
        else:
            parts = [p.strip() for p in mime.split(';')]
            parameters = dict(p.split('=', 1) for p in parts[1:] if '=' in p)
            if parts[0] not in ('audio/l16', 'audio/pcm') or parameters.get('rate') != '24000':
                raise ValueError(f'Unexpected speech audio format: {blob.mime_type}')
            chunks.append(data)
    if not chunks:
        raise ValueError('The provider returned no audio.')
    return b''.join(chunks)


def prompt_for(term, definition):
    return (f'Pronunciation reference for an adult English learner. Use a clear, natural American English accent. '
            f'Say ONLY the term below, once, at a slightly slower teaching pace. Do not say any introduction, '
            f'definition, label, spelling, or commentary. No music or sound effects. '
            f'The meaning is supplied only to choose the pronunciation: {definition}.\n'
            f'Term to speak: {term}')


def valid_record(term, definition, records, root=ROOT):
    record = records.get(term, {})
    path = root / audio_path(term)
    return (record.get('policy') == AUDIO_POLICY and record.get('model') in MODEL_PRICES
            and record.get('voice') == VOICE and record.get('term_specification', record.get('prompt')) == prompt_for(term, definition)
            and record.get('file') == audio_path(term) and .25 <= record.get('seconds', 0) <= 12
            and path.is_file() and len(path.read_bytes()) > 1000
            and hashlib.sha256(path.read_bytes()).hexdigest() == record.get('sha256'))


class AudioBudget:
    def __init__(self, path, limit):
        self.path, self.limit = Path(path), limit
        self.data = json.loads(self.path.read_text()) if self.path.exists() else {'requests': []}
        self.lock = threading.Lock()

    @property
    def spent(self):
        return sum(row['usd'] for row in self.data['requests'])

    def request(self, client, term, prompt, model=MODEL, max_tokens=MAX_TOKENS, spoken_text=None):
        # Reserve before sending. Unknown/failed requests keep their reservation.
        input_price, output_price = MODEL_PRICES[model]
        if not 1 <= max_tokens <= 4096:
            raise ValueError('Invalid speech output limit.')
        reserve = ((len(prompt.encode()) + 2048) * input_price + max_tokens * output_price) / 1_000_000
        with self.lock:
            if self.spent + reserve > self.limit:
                raise RuntimeError('Audio spending cap reached.')
            row = {'term': term, 'model': model, 'usd': reserve, 'usage': 'reserved',
                   'time': datetime.now(timezone.utc).isoformat()}
            self.data['requests'].append(row); atomic_json(self.path, self.data)
        if model == 'gemini-3.8-flash-lite-tts':
            response = current_speech_request(model, spoken_text or term, max_tokens)
        else:
            response = client.models.generate_content(model=model, contents=prompt, config={
                'response_modalities': ['AUDIO'], 'max_output_tokens': max_tokens,
                'speech_config': {'voice_config': {'prebuilt_voice_config': {'voice_name': VOICE}}}})
        usage = getattr(response, 'usage_metadata', None)
        if usage and usage.prompt_token_count is not None and usage.candidates_token_count is not None:
            with self.lock:
                row.update(usd=(usage.prompt_token_count * input_price + usage.candidates_token_count * output_price) / 1_000_000,
                           usage='reported', input_tokens=usage.prompt_token_count,
                           output_tokens=usage.candidates_token_count)
                atomic_json(self.path, self.data)
        candidates = response.candidates or []
        if not candidates or str(candidates[0].finish_reason).split('.')[-1] != 'STOP':
            raise ValueError('The pronunciation recording did not finish normally.')
        parts = candidates[0].content.parts or []
        blobs = [p.inline_data for p in parts if p.inline_data]
        return decode_audio(blobs)


def encode_mp3(pcm, destination):
    seconds = len(pcm) / 48000
    if len(pcm) % 2 or not .25 <= seconds <= 12:
        raise ValueError('Pronunciation audio is empty, truncated, or unexpectedly long.')
    destination.parent.mkdir(parents=True, exist_ok=True)
    # ffmpeg only compresses the cloud recording; it does not synthesize a voice.
    with tempfile.TemporaryDirectory() as directory:
        target = Path(directory) / 'pronunciation.mp3'
        subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-f', 's16le', '-ar', '24000',
                        '-ac', '1', '-i', 'pipe:0', '-codec:a', 'libmp3lame', '-b:a', '64k', str(target)],
                       input=pcm, check=True, timeout=30)
        data = target.read_bytes()
        if len(data) <= 1000:
            raise ValueError('Empty encoded recording.')
        temp = destination.with_suffix('.tmp'); temp.write_bytes(data); temp.replace(destination)
    return seconds, hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--budget', type=float, default=2)
    parser.add_argument('--budget-key', default='everyday-audio-20260929')
    parser.add_argument('--limit', type=int, default=0, help='Optional small pilot; zero generates all missing terms.')
    parser.add_argument('--model', choices=MODEL_PRICES, default=MODEL)
    args = parser.parse_args()
    if not 0 < args.budget <= 2 or not re.fullmatch(r'[a-zA-Z0-9-]+', args.budget_key) or args.limit < 0:
        parser.error('Use a budget up to $2, a simple budget key, and a nonnegative limit.')
    words = terms()
    records = json.loads(RECORDS.read_text()) if RECORDS.exists() else {}
    pending = [(term, definition) for term, definition in words.items() if not valid_record(term, definition, records)]
    if args.check:
        print(f'Pronunciation coverage: {len(words) - len(pending)}/{len(words)} unique terms.')
        return bool(pending)
    if not pending:
        print('All pronunciation files are cached; no paid requests.'); return 0
    from google import genai
    # Disable automatic SDK retries so every billable request has a reservation.
    client = genai.Client(api_key=os.environ['GEMINI_API_KEY'],
                         http_options={'timeout': 90000, 'retry_options': {'attempts': 1}})
    budget = AudioBudget(ROOT / 'content' / ('.audio-usage-' + args.budget_key + '.json'), args.budget)
    pending = pending[:args.limit] if args.limit else pending
    save_lock, rate_lock = threading.Lock(), threading.Lock()
    next_start = [0.0]
    def generate(term, definition):
        model = args.model
        for attempt in range(3):
            # TTS has a separate, small rate quota: keep below ten starts/minute.
            with rate_lock:
                time.sleep(max(0, next_start[0] - time.monotonic()))
                next_start[0] = time.monotonic() + 6.8
            try:
                pcm = budget.request(client, term, prompt_for(term, definition), model)
                seconds, digest = encode_mp3(pcm, ROOT / audio_path(term))
                with save_lock:
                    records[term] = {'policy': AUDIO_POLICY, 'model': model, 'voice': VOICE,
                                     'prompt': prompt_for(term, definition), 'file': audio_path(term),
                                     'seconds': seconds, 'sha256': digest}
                    atomic_json(RECORDS, records)
                return
            except Exception as error:
                code = getattr(error, 'code', None)
                if code == 429:
                    # Preserve the provider's quota identifiers, without logging request headers or credentials.
                    payload = getattr(error, 'details', {}) or {}
                    details = payload.get('error', payload).get('details', []) if isinstance(payload, dict) else []
                    quotas = [{k: v for k, v in q.items() if k in ('quotaMetric', 'quotaId', 'quotaValue', 'quotaDimensions')}
                              for detail in details for q in detail.get('violations', [])]
                    print('Quota details: ' + json.dumps(quotas), flush=True)
                    if any('PerDay' in q.get('quotaId', '') for q in quotas):
                        raise
                    # A rate-limit cooldown applies to the entire pool, not only the failed term.
                    retry_seconds = max([60.0, *[float(str(d['retryDelay']).removesuffix('s'))
                                                for d in details if re.fullmatch(r'\d+(?:\.\d+)?s', str(d.get('retryDelay', '')))]] )
                    with rate_lock:
                        next_start[0] = max(next_start[0], time.monotonic() + min(retry_seconds + 2, 180))
                # Retry only transient provider failures; do not conceal content/config errors.
                retryable = code in (429, 500, 502, 503, 504) or (code == 400 and model == 'gemini-3.1-flash-tts-preview')
                if not retryable or attempt == 2:
                    raise
                time.sleep(25 * (attempt + 1))
    errors = []
    try:
        with ThreadPoolExecutor(max_workers=3) as pool:
            jobs = {pool.submit(generate, term, definition): term for term, definition in pending}
            for job in as_completed(jobs):
                term = jobs[job]
                try:
                    job.result(); print(f'{term}: recording saved', flush=True)
                except Exception as error:
                    errors.append(term)
                    print(f'{term}: {type(error).__name__}: {str(error)[:160]}', flush=True)
                    # Stop dispatching when a model/configuration/quota issue repeats.
                    if len(errors) >= 3:
                        for future in jobs: future.cancel()
                        break
    finally:
        client.close()
    print(f'Audio cost recorded/reserved: ${budget.spent:.4f} of ${budget.limit:.2f}', flush=True)
    missing = [term for term, definition in words.items() if not valid_record(term, definition, records)]
    print(f'Pronunciation coverage: {len(words) - len(missing)}/{len(words)} unique terms.')
    return bool(errors or (missing and not args.limit))


if __name__ == '__main__':
    raise SystemExit(main())
