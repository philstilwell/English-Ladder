"""Explicitly requested live maintenance samples; never publish their outputs."""
import argparse
import json
import os
from pathlib import Path

import us_life_audio_review as audio
import us_life_translations as translations
from vocabulary_translations import Budget, MODEL, atomic_json

CAP_USD = .15
AUDIO_TERMS = ('passport', 'baggage claim')


class PilotBudget(Budget):
    """At most one translation and one review; every phase shares this ledger."""
    def request(self, client, prompt, schema, thinking_level):
        if (self.path.parent / 'translation-error.json').exists():
            raise RuntimeError('Pilot has a previous failed translation attempt; no automatic retry.')
        text_requests = [r for r in self.data['requests'] if r.get('phase') != 'independent-audio-review']
        if len(text_requests) >= 2:
            raise RuntimeError('Pilot translation request limit reached; no extra attempts.')
        try:
            return super().request(client, prompt, schema, thinking_level)
        except Exception as error:
            atomic_json(self.path.parent / 'translation-error.json', diagnostic(error))
            # Stop translate()'s retry loop after any failed provider attempt.
            raise RuntimeError('Pilot translation stopped; see translation-error.json.') from error


def diagnostic(error):
    # Provider error messages, unlike full exceptions, omit request headers/URLs.
    message = str(getattr(error, 'message', ''))[:500]
    key = os.environ.get('GEMINI_API_KEY')
    if key:
        message = message.replace(key, '[redacted]')
    return {'type': type(error).__name__, 'code': getattr(error, 'code', None), 'message': message}


def run_pilot(client, directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    budget = PilotBudget(directory / 'usage.json', CAP_USD)
    report = {'model': MODEL, 'cap_usd': CAP_USD, 'sidebar': 'arrival', 'tests': {}}
    try:
        source = translations.sources()['arrival']
        result = translations.translate(client, source, budget, directory / 'translations')
        record = translations.read_record(source, directory / 'translations')
        report['tests']['translation'] = {'status': 'passed', 'result': result,
                                          'languages': sorted(record['translations'])}
    except Exception as error:
        report['tests']['translation'] = {'status': 'failed', 'error': diagnostic(error)}
    atomic_json(directory / 'report.json', report)
    audio_result_path = directory / 'audio-review.json'
    try:
        if any(r.get('phase') == 'independent-audio-review' for r in budget.data['requests']):
            # Never silently repeat a possibly billed request after a restart.
            results = json.loads(audio_result_path.read_text())
        else:
            records = json.loads(audio.RECORDS.read_text())
            entries = [(term, records[term]) for term in AUDIO_TERMS]
            definitions = audio.terms()
            if not all(audio.valid_record(term, definitions[term], records) for term in AUDIO_TERMS):
                raise ValueError('Pilot needs valid saved audio files.')
            results = audio.transcribe(client, entries, budget)
            atomic_json(audio_result_path, results)
        checks = [{'term': AUDIO_TERMS[r['id']], 'transcript': r['text'],
                   'clear_speech': r['clear_speech'], 'extra_speech': r['extra_speech'],
                   'passed': (audio.transcript_matches(AUDIO_TERMS[r['id']], r['text'])
                              and r['clear_speech'] and not r['extra_speech'])} for r in results]
        report['tests']['audio'] = {'status': 'passed' if all(r['passed'] for r in checks) else 'failed',
                                   'recordings': checks}
    except Exception as error:
        report['tests']['audio'] = {'status': 'failed', 'error': diagnostic(error)}
    reported = [r for r in budget.data['requests'] if r.get('usage') == 'reported']
    reserved = [r for r in budget.data['requests'] if r.get('usage') != 'reported']
    report['cost'] = {
        'reported_usage_usd': sum(r['usd'] for r in reported),
        'unconfirmed_reserved_usd': sum(r['usd'] for r in reserved),
        'total_recorded_or_reserved_usd': budget.spent,
        'requests': len(budget.data['requests']),
        'basis': 'Provider token counts at published standard rates; not an invoice.',
    }
    report['passed'] = all(t['status'] == 'passed' for t in report['tests'].values())
    atomic_json(directory / 'report.json', report)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-paid', action='store_true', help='Explicitly authorize up to $0.15 total.')
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    if not args.run_paid:
        parser.error('This live test requires --run-paid after a cost estimate and authorization.')
    from update_site import configure_gemini
    client = configure_gemini()  # SDK retries disabled by the existing client configuration.
    try:
        report = run_pilot(client, args.output_dir)
    finally:
        client.close()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return not report['passed']


if __name__ == '__main__':
    raise SystemExit(main())
