"""Generate small cloud word lists and split them into independently checked MP3 files."""
import argparse
import array
import hashlib
import json
import os
import re
import sys
import time
import zlib

from us_life_audio import (AudioBudget, MODEL_PRICES, VOICE, RECORDS, encode_mp3,
                          prompt_for, valid_record)
from us_life_content import ROOT, AUDIO_POLICY, audio_path, terms
from vocabulary_translations import atomic_json


def batch_prompt(words):
    spoken = '\n\n'.join(term + '.' for term, _ in words)
    return ('Read this vocabulary list in clear American English at a relaxed teaching pace. '
            'Pause silently for two seconds between entries. Read each entry once, '
            'without an introduction or commentary:\n\n' + spoken)


def split_recording(pcm, count):
    if len(pcm) % 2 or not .25 <= len(pcm) / 48000 <= 120:
        raise ValueError('Invalid batch audio length.')
    samples = array.array('h'); samples.frombytes(pcm)
    if sys.byteorder != 'little': samples.byteswap()
    frame = 480  # 20 ms at 24 kHz
    voiced = [index for index in range(0, len(samples), frame)
              if sum(x*x for x in samples[index:index+frame]) / len(samples[index:index+frame]) > 180**2]
    if not voiced:
        raise ValueError('No speech detected in the word list.')
    # Long silent gaps mark words. The independent transcript check below publishing
    # rejects a wrong boundary even when the number of detected clips happens to match.
    for gap_seconds in (.65, .45, .85, .35, 1.0, .25):
        groups = [[voiced[0], voiced[0] + frame]]
        for start in voiced[1:]:
            if start - groups[-1][1] >= int(gap_seconds * 24000):
                groups.append([start, min(start + frame, len(samples))])
            else:
                groups[-1][1] = min(start + frame, len(samples))
        if len(groups) != count:
            continue
        clips, bounds = [], []
        for index, (start, end) in enumerate(groups):
            left = (groups[index-1][1] + start) // 2 if index else 0
            right = (end + groups[index+1][0]) // 2 if index + 1 < count else len(samples)
            start, end = max(left, start - 3840), min(right, end + 3840)
            if not .25 <= (end-start)/24000 <= 12:
                break
            clips.append(pcm[start*2:end*2]); bounds.append([start/24000, end/24000])
        if len(clips) == count:
            return clips, bounds, gap_seconds
    raise ValueError(f'Could not find exactly {count} separated pronunciations; raw recording saved for review.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--budget', type=float, default=2)
    parser.add_argument('--budget-key', default='everyday-audio-20260929')
    parser.add_argument('--limit', type=int, default=0)
    parser.add_argument('--batch-size', type=int, default=8)
    parser.add_argument('--model', choices=MODEL_PRICES, default='gemini-3.8-flash-lite-tts')
    args = parser.parse_args()
    if not 0 < args.budget <= 2 or not 2 <= args.batch_size <= 8 or args.limit < 0 or not re.fullmatch(r'[a-zA-Z0-9-]+', args.budget_key):
        parser.error('Use a budget up to $2, batch size 2–8, and a simple budget key.')
    words = terms(); records = json.loads(RECORDS.read_text()) if RECORDS.exists() else {}
    pending = [(term, definition) for term, definition in words.items() if not valid_record(term, definition, records)]
    pending = pending[:args.limit] if args.limit else pending
    if not pending:
        print('All requested recordings are already saved.'); return 0
    from google import genai
    client = genai.Client(api_key=os.environ['GEMINI_API_KEY'], http_options={'timeout': 180000, 'retry_options': {'attempts': 1}})
    budget = AudioBudget(ROOT/'content'/('.audio-usage-' + args.budget_key + '.json'), args.budget)
    directory = ROOT/'content/audio-batches'; directory.mkdir(parents=True, exist_ok=True)
    failed = False
    try:
        queue = [pending[offset:offset + args.batch_size]
                 for offset in range(0, len(pending), args.batch_size)]
        while queue:
            batch = queue.pop(0)
            prompt = batch_prompt(batch)
            identity = {'model': args.model, 'voice': VOICE, 'prompt': prompt, 'words': batch}
            key = hashlib.sha256(json.dumps(identity, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
            raw_path, info_path = directory/(key + '.pcm.zlib'), directory/(key + '.json')
            pcm = None
            if raw_path.exists() and info_path.exists():
                info = json.loads(info_path.read_text())
                raw = zlib.decompress(raw_path.read_bytes())
                if info['pcm_sha256'] == hashlib.sha256(raw).hexdigest() and info['prompt'] == prompt and info['model'] == args.model:
                    pcm = raw
            if pcm is None:
                for attempt in range(3):
                    try:
                        pcm = budget.request(client, 'Word list: ' + ', '.join(t for t, _ in batch), prompt,
                            args.model, max_tokens=max(512, 256 * len(batch)),
                            spoken_text=' <long pause> '.join(t + '.' for t, _ in batch))
                        raw_path.write_bytes(zlib.compress(pcm))
                        atomic_json(info_path, {**identity, 'pcm_sha256': hashlib.sha256(pcm).hexdigest()})
                        break
                    except Exception as error:
                        code = getattr(error, 'code', None)
                        payload = getattr(error, 'details', {}) or {}
                        details = payload.get('error', payload).get('details', []) if isinstance(payload, dict) else []
                        daily = any('PerDay' in q.get('quotaId', '') for d in details for q in d.get('violations', []))
                        if daily or code not in (400, 429, 500, 502, 503, 504) or attempt == 2:
                            raise
                        print(f'Word list: provider {code}; bounded retry {attempt+1}.', flush=True)
                        time.sleep(62 if code == 429 else 10)
            try:
                clips, bounds, gap = split_recording(pcm, len(batch))
            except ValueError:
                if len(batch) == 1:
                    raise
                # A provider can end a word list early with a normal STOP.
                # Keep the rejected source for diagnostics, then use smaller
                # lists instead of replaying the same bad cached recording.
                middle = len(batch) // 2
                queue[0:0] = [batch[:middle], batch[middle:]]
                print(f'Incomplete {len(batch)}-term word list; retrying as '
                      f'{middle} and {len(batch)-middle} terms.', flush=True)
                time.sleep(7)
                continue
            for (term, definition), clip, boundary in zip(batch, clips, bounds):
                seconds, digest = encode_mp3(clip, ROOT/audio_path(term))
                records[term] = {'policy': AUDIO_POLICY, 'model': args.model, 'voice': VOICE,
                    'term_specification': prompt_for(term, definition), 'prompt': prompt,
                    'file': audio_path(term), 'seconds': seconds, 'sha256': digest,
                    'batch_source': info_path.relative_to(ROOT).as_posix(), 'batch_interval_seconds': boundary,
                    'silence_gap_seconds': gap}
                print(f'{term}: recording saved from word list', flush=True)
            atomic_json(RECORDS, records)
            if queue: time.sleep(7)
    except Exception as error:
        failed = True
        print(f'Word-list preparation paused: {type(error).__name__}: {str(error)[:180]}', flush=True)
    finally:
        client.close()
    print(f'Combined audio cost recorded/reserved: ${budget.spent:.4f} of ${budget.limit:.2f}', flush=True)
    missing = [term for term, definition in words.items() if not valid_record(term, definition, records)]
    print(f'Pronunciation coverage: {len(words)-len(missing)}/{len(words)} unique terms.')
    return bool(failed or (missing and not args.limit))


if __name__ == '__main__':
    raise SystemExit(main())
