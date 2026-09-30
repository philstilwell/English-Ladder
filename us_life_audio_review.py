"""Independently transcribe saved pronunciation files before publication."""
import argparse
import json
import math
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

from us_life_audio import AudioBudget, RECORDS, valid_record
from us_life_content import ROOT, terms
from vocabulary_translations import atomic_json

MODEL = 'gemini-2.5-flash'
POLICY = 'blind-pronunciation-transcription-v1'


def normalized(text):
    return re.sub(r'[^a-z0-9]', '', text.casefold())


def reviewed(record):
    review = record.get('review', {})
    return (review.get('policy') == POLICY and review.get('status') == 'passed'
            and review.get('audio_sha256') == record['sha256'])


def transcribe(client, entries, budget):
    from google.genai import types
    prompt = ('Independently check these English pronunciation recordings. Each clip is labeled with an ID. '
              'Transcribe exactly the audible words in each clip, without adding punctuation or explanations. '
              'Do not guess from filenames: you have not been supplied the intended words. '
              'Set clear_speech false if speech is cut off, inaudible, or difficult to understand. '
              'Set extra_speech true for any introduction, spoken instructions, or commentary beyond a single '
              'isolated word or short vocabulary phrase. Return all IDs once, with their transcripts.')
    parts = [types.Part.from_text(text=prompt)]
    for index, (_, record) in enumerate(entries):
        parts.append(types.Part.from_text(text=f'Clip {index}'))
        parts.append(types.Part.from_bytes(data=(ROOT / record['file']).read_bytes(), mime_type='audio/mpeg'))
    schema = {'type': 'object', 'properties': {'transcripts': {'type': 'array',
              'minItems': len(entries), 'maxItems': len(entries), 'items': {'type': 'object',
              'properties': {'id': {'type': 'integer'}, 'text': {'type': 'string'},
                             'clear_speech': {'type': 'boolean'}, 'extra_speech': {'type': 'boolean'}},
              'required': ['id', 'text', 'clear_speech', 'extra_speech'], 'additionalProperties': False}}},
              'required': ['transcripts'], 'additionalProperties': False}
    # Budget input at the more expensive audio rate, including text/schema overhead.
    reserve = ((len(prompt.encode()) + len(json.dumps(schema)) + 2048 +
                sum(math.ceil(r['seconds'] * 32) + 256 for _, r in entries)) + 2048 * 2.5) / 1_000_000
    with budget.lock:
        if budget.spent + reserve > budget.limit:
            raise RuntimeError('Combined pronunciation generation/review cap reached.')
        row = {'phase': 'independent-audio-review', 'usd': reserve, 'usage': 'reserved',
               'time': datetime.now(timezone.utc).isoformat()}
        budget.data['requests'].append(row); atomic_json(budget.path, budget.data)
    response = client.models.generate_content(model=MODEL, contents=parts, config={
        'response_mime_type': 'application/json', 'response_json_schema': schema,
        'max_output_tokens': 2048, 'thinking_config': {'thinking_budget': 0}})
    usage = response.usage_metadata
    if usage and usage.prompt_token_count is not None and usage.candidates_token_count is not None:
        with budget.lock:
            row.update(usd=(usage.prompt_token_count + usage.candidates_token_count * 2.5) / 1_000_000,
                       usage='reported-tokens-conservative-input-rate', input_tokens=usage.prompt_token_count,
                       output_tokens=usage.candidates_token_count)
            atomic_json(budget.path, budget.data)
    results = json.loads(response.text)['transcripts']
    if len(results) != len(entries) or {r['id'] for r in results} != set(range(len(entries))):
        raise ValueError('Review did not account for every recording exactly once.')
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--budget', type=float, default=2)
    parser.add_argument('--budget-key', default='everyday-audio-20260929')
    args = parser.parse_args()
    if not 0 < args.budget <= 2 or not re.fullmatch(r'[a-zA-Z0-9-]+', args.budget_key):
        parser.error('Use a cumulative budget up to $2 and a simple budget key.')
    records = json.loads(RECORDS.read_text())
    if any(not valid_record(t, d, records) for t, d in terms().items()):
        raise RuntimeError('Complete the pronunciation recordings before review.')
    pending = [(term, records[term]) for term in terms() if not reviewed(records[term])]
    if not args.check and pending:
        from google import genai
        client = genai.Client(api_key=os.environ['GEMINI_API_KEY'],
                             http_options={'timeout': 90000, 'retry_options': {'attempts': 1}})
        budget = AudioBudget(ROOT / 'content' / ('.audio-usage-' + args.budget_key + '.json'), args.budget)
        try:
            with ThreadPoolExecutor(max_workers=3) as pool:
                batches = [pending[i:i+8] for i in range(0, len(pending), 8)]
                jobs = {pool.submit(transcribe, client, batch, budget): batch for batch in batches}
                for job in as_completed(jobs):
                    batch = jobs[job]
                    try:
                        for result in job.result():
                            term, record = batch[result['id']]
                            passed = (normalized(term) == normalized(result['text'])
                                      and result['clear_speech'] and not result['extra_speech'])
                            record['review'] = {'policy': POLICY, 'model': MODEL,
                                'status': 'passed' if passed else 'needs-review', 'transcript': result['text'],
                                'clear_speech': result['clear_speech'], 'extra_speech': result['extra_speech'],
                                'audio_sha256': record['sha256']}
                            print(f'{term}: {record["review"]["status"]}' + (f' (heard: {result["text"]})' if not passed else ''), flush=True)
                        atomic_json(RECORDS, records)
                    except Exception as error:
                        print(f'Audio review batch unavailable: {type(error).__name__}', flush=True)
        finally:
            client.close()
        print(f'Combined audio cost recorded/reserved: ${budget.spent:.4f} of ${budget.limit:.2f}', flush=True)
    missing = [t for t in terms() if not reviewed(records[t])]
    print(f'Independently checked pronunciation: {len(terms()) - len(missing)}/{len(terms())}.')
    if missing: print('Needs review: ' + ', '.join(missing))
    return bool(missing)


if __name__ == '__main__':
    raise SystemExit(main())
