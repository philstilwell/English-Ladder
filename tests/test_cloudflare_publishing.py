"""Offline coverage for waiting on a deployment without regenerating lessons."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().parents[1] / 'cloudflare' / 'verify-publishing.py'
SPEC = importlib.util.spec_from_file_location('cloudflare_publishing', MODULE_PATH)
publishing = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(publishing)
EXPECTED_REVISION = 'a' * 40
OLDER_REVISION = 'b' * 40
NEWER_REVISION = 'c' * 40
HASH = '1' * 64
OTHER_HASH = '2' * 64
ORIGIN = 'https://englishladder.example'


def manifest(revision=EXPECTED_REVISION, files=None):
    return {'revision': revision, 'files': {'index.html': HASH} if files is None else files}


class Clock:
    def __init__(self):
        self.now = 0
        self.sleeps = []

    def __call__(self):
        return self.now

    def sleep(self, seconds):
        self.sleeps.append(seconds)
        self.now += seconds


class PublishingTests(unittest.TestCase):
    def run_wait(self, responses, **options):
        clock = Clock()
        messages = []
        requests = []
        responses = iter(responses)

        def fetch(url, timeout):
            requests.append((url, timeout))
            result = next(responses)
            if isinstance(result, Exception):
                raise result
            return result

        report = publishing.wait_for_publishing(
            ORIGIN, options.pop('expected', manifest()),
            clock=clock, sleep=clock.sleep, fetch=fetch, log=messages.append,
            timeout=options.pop('timeout', 45), interval=options.pop('interval', 20), **options)
        return report, clock, messages, requests

    def test_success_requires_all_files_and_reports_expected_and_live_revisions(self):
        expected = manifest(files={'index.html': HASH, 'lesson-data.json': OTHER_HASH})
        report, clock, messages, requests = self.run_wait([expected], expected=expected)
        self.assertEqual('success', report['status'])
        self.assertEqual(EXPECTED_REVISION, report['expected_revision'])
        self.assertEqual(EXPECTED_REVISION, report['last_live_revision'])
        self.assertEqual(2, report['last_live_file_count'])
        self.assertTrue(report['expected_revision_seen'])
        self.assertEqual(1, report['attempts'])
        self.assertEqual([], clock.sleeps)
        self.assertEqual(30, requests[0][1])
        self.assertTrue(requests[0][0].startswith(ORIGIN + '/deployment.json?verify='))

    def test_newer_code_only_revision_with_identical_files_is_success(self):
        report, _, messages, _ = self.run_wait([manifest(NEWER_REVISION)])
        self.assertEqual('success', report['status'])
        self.assertFalse(report['expected_revision_seen'])
        self.assertEqual(NEWER_REVISION, report['last_live_revision'])
        self.assertIn(NEWER_REVISION, messages[-1])

    def test_revision_alone_does_not_conceal_missing_changed_or_extra_files(self):
        expected = manifest(files={'index.html': HASH, 'lesson-data.json': HASH})
        live = manifest(files={'index.html': OTHER_HASH, 'extra.html': HASH})
        report, clock, messages, _ = self.run_wait([live, live, live], expected=expected)
        self.assertEqual('timed_out', report['status'])
        self.assertTrue(report['expected_revision_seen'])
        self.assertEqual([20, 20, 5], clock.sleeps)
        self.assertEqual({'missing': 1, 'changed': 1, 'unexpected': 1,
                          'examples': [{'file': 'lesson-data.json', 'difference': 'missing'},
                                       {'file': 'index.html', 'difference': 'changed'},
                                       {'file': 'extra.html', 'difference': 'unexpected'}]}, report['differences'])
        self.assertIn('deploy_only=true', messages[-1])
        self.assertIn('retry the failed build', messages[-1])

    def test_stale_deployment_recovers_without_losing_full_hash_check(self):
        old = manifest(OLDER_REVISION, {'index.html': OTHER_HASH})
        report, clock, _, requests = self.run_wait([old, manifest()])
        self.assertEqual('success', report['status'])
        self.assertEqual([20], clock.sleeps)
        self.assertEqual(2, len(requests))
        self.assertNotEqual(requests[0][0], requests[1][0])

    def test_network_and_malformed_response_recover_without_exposing_details(self):
        errors = [subprocess.CalledProcessError(22, ['curl'], stderr='secret token'),
                  subprocess.TimeoutExpired(['curl', 'secret token'], 30),
                  ValueError('secret response'), [], {}, manifest(files={'index.html': 'invalid'})]
        for error in errors:
            with self.subTest(error=type(error).__name__):
                report, clock, messages, _ = self.run_wait([error, manifest()])
                self.assertEqual('success', report['status'])
                self.assertEqual([20], clock.sleeps)
                self.assertIsNone(report['last_fetch_error'])
                self.assertNotIn('secret', json.dumps(report) + '\n'.join(messages))

    def test_timeout_retains_last_good_live_manifest_after_fetch_errors(self):
        old = manifest(OLDER_REVISION, {'index.html': OTHER_HASH})
        report, clock, messages, requests = self.run_wait([old, ValueError('secret'), []])
        self.assertEqual('timed_out', report['status'])
        self.assertEqual(OLDER_REVISION, report['last_live_revision'])
        self.assertEqual(1, report['last_live_file_count'])
        self.assertFalse(report['expected_revision_seen'])
        self.assertEqual('invalid deployment manifest', report['last_fetch_error'])
        self.assertEqual([30, 25, 5], [request[1] for request in requests])
        self.assertEqual(45, report['elapsed_seconds'])
        self.assertIn(EXPECTED_REVISION, messages[-1])
        self.assertIn(OLDER_REVISION, messages[-1])

    def test_fetch_time_reduces_remaining_poll_budget(self):
        clock = Clock()
        calls = []

        def fetch(url, timeout):
            calls.append(timeout)
            clock.now += timeout
            raise subprocess.TimeoutExpired(['curl'], timeout)

        report = publishing.wait_for_publishing(
            ORIGIN, manifest(), timeout=35, interval=3, fetch=fetch,
            clock=clock, sleep=clock.sleep, log=lambda message: None)
        self.assertEqual([30, 2], calls)
        self.assertEqual([3], clock.sleeps)
        self.assertEqual(35, report['elapsed_seconds'])
        self.assertIsNone(report['last_live_revision'])

    def test_difference_examples_are_bounded(self):
        delta = publishing.differences({f'file{i}': HASH for i in range(30)}, {})
        self.assertEqual(30, delta['missing'])
        self.assertEqual(publishing.MAX_DIFFERENCES, len(delta['examples']))

    def test_invalid_expected_manifest_and_unbounded_timings_fail_before_fetch(self):
        for expected in [[], {}, manifest(files={}), manifest(revision='bad')]:
            with self.subTest(expected=expected), self.assertRaises(ValueError):
                self.run_wait([], expected=expected)
        for key in ['timeout', 'interval']:
            for value in [0, -1, float('inf'), float('nan')]:
                with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                    self.run_wait([], **{key: value})

    def test_fetch_uses_bounded_curl_and_process_timeouts(self):
        with patch.object(publishing.subprocess, 'run') as run:
            run.return_value.stdout = json.dumps(manifest())
            self.assertEqual(manifest(), publishing.fetch_json(ORIGIN, timeout=7))
        args, kwargs = run.call_args
        self.assertEqual('7', args[0][args[0].index('--max-time') + 1])
        self.assertEqual(7, kwargs['timeout'])
        self.assertTrue(kwargs['check'])
        self.assertEqual(ORIGIN, args[0][-1])

    def test_cli_report_is_written_for_success_and_timeout(self):
        with tempfile.TemporaryDirectory() as directory:
            for status, code in [('success', 0), ('timed_out', 1)]:
                path = Path(directory) / status / 'publishing.json'
                report = {'status': status, 'expected_revision': EXPECTED_REVISION}
                with patch.object(publishing.Path, 'read_text', return_value=json.dumps(manifest())), \
                     patch.object(publishing, 'wait_for_publishing', return_value=report) as wait:
                    result = publishing.main([ORIGIN, '--timeout', '91', '--interval', '7', '--report', str(path)])
                self.assertEqual(code, result)
                self.assertEqual(report, json.loads(path.read_text()))
                self.assertFalse(path.with_name(path.name + '.tmp').exists())
                wait.assert_called_once_with(ORIGIN, manifest(), timeout=91, interval=7)

    def test_cli_rejects_credentials_paths_queries_and_infinite_waits(self):
        invalid = [[ORIGIN, '--timeout', 'nan'], [ORIGIN, '--interval', '0'],
                   ['https://user:password@example.com'], [ORIGIN + '/page'],
                   [ORIGIN + '?secret=value'], ['file:///tmp/site']]
        for argv in invalid:
            with self.subTest(argv=argv), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as caught:
                publishing.main(argv)
            self.assertEqual(2, caught.exception.code)


if __name__ == '__main__':
    unittest.main()
