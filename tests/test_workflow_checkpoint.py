"""Offline GitHub-artifact recovery checks with no downloads or paid calls."""
import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from lesson_checkpoint import CheckpointStore
import workflow_checkpoint as workflow

REPO = 'owner/English-Ladder'
DATE = '2026-09-07'
POLICY = 'policy-v1'
REPOSITORY_ID = 123


def artifact(run_id=42, **changes):
    result = {'name': f'lesson-state-{run_id}', 'expired': False, 'size_in_bytes': 2000,
              'created_at': f'2026-09-07T10:{run_id % 60:02}:00Z',
              'workflow_run': {'id': run_id, 'repository_id': REPOSITORY_ID,
                               'head_repository_id': REPOSITORY_ID, 'head_branch': 'main'}}
    result.update(changes)
    return result


def metadata(run_id=42, **changes):
    result = {'id': run_id, 'repository': {'id': REPOSITORY_ID},
              'head_repository': {'id': REPOSITORY_ID}, 'head_branch': 'main',
              'path': '.github/workflows/cron.yml', 'event': 'schedule'}
    result.update(changes)
    return result


class FakeGitHub:
    def __init__(self, artifacts=None, runs=None, downloads=None, failure=None):
        self.artifacts = [artifact()] if artifacts is None else artifacts
        self.runs = {} if runs is None else runs
        self.downloads = {} if downloads is None else downloads
        self.failure = failure
        self.calls = []

    def __call__(self, command, **options):
        self.calls.append(command)
        if options != {'check': True, 'capture_output': True, 'text': True, 'timeout': 60}:
            raise AssertionError(f'Unexpected subprocess settings: {options}')
        if self.failure:
            self.failure(command)
        if command == ['gh', 'api', f'repos/{REPO}']:
            return SimpleNamespace(stdout=json.dumps({'id': REPOSITORY_ID, 'full_name': REPO}))
        if command == ['gh', 'api', f'repos/{REPO}/actions/artifacts?per_page=100']:
            return SimpleNamespace(stdout=json.dumps({'artifacts': self.artifacts}))
        if command[:2] == ['gh', 'api']:
            run_id = int(command[2].rsplit('/', 1)[-1])
            return SimpleNamespace(stdout=json.dumps(self.runs.get(run_id, metadata(run_id))))
        if command[:3] == ['gh', 'run', 'download']:
            run_id = int(command[3])
            directory = Path(command[command.index('--dir') + 1])
            creator = self.downloads.get(run_id, self.valid_checkpoint)
            creator(directory)
            return SimpleNamespace(stdout='')
        raise AssertionError(command)

    @staticmethod
    def valid_checkpoint(directory):
        CheckpointStore(directory, DATE, POLICY).save(
            {'title': 'Source for today'}, {'beginner': {'lesson': 'approved content'}},
            {'advanced': {'lesson': {'draft': 'unfinished'}}})
        (directory / 'unrelated.txt').write_text('must not copy')


class WorkflowCheckpointTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name) / 'restored'

    def restore(self, github, **changes):
        request = {'repo': REPO, 'branch': 'main', 'release_date': DATE,
                   'directory': self.directory, 'policy_fingerprint': POLICY,
                   'current_run_id': '100', 'run_command': github, '_sleep': Mock()}
        request.update(changes)
        return workflow.restore_checkpoint(**request)

    def test_restores_only_validated_date_file_and_removes_download_directory(self):
        github = FakeGitHub()
        self.assertTrue(self.restore(github))
        checkpoint = CheckpointStore(self.directory, DATE, POLICY).load()
        self.assertEqual('Source for today', checkpoint['source']['title'])
        self.assertIn('beginner', checkpoint['levels'])
        self.assertIn('advanced', checkpoint['drafts'])
        self.assertEqual([self.directory / f'{DATE}.json'], list(self.directory.iterdir()))
        download = github.calls[-1]
        self.assertFalse(Path(download[download.index('--dir') + 1]).exists())

    def test_filters_expired_wrong_branch_fork_and_oversized_artifacts(self):
        candidates = [artifact(name='other-data'), artifact(expired=True),
                      artifact(size_in_bytes=workflow.MAX_ARTIFACT_BYTES + 1), artifact(size_in_bytes=True)]
        for key, value in (('repository_id', 999), ('head_repository_id', 999), ('head_branch', 'other')):
            item = artifact()
            item['workflow_run'][key] = value
            candidates.append(item)
        github = FakeGitHub(artifacts=candidates)
        self.assertFalse(self.restore(github))
        self.assertEqual(2, len(github.calls))
        self.assertFalse(self.directory.exists())

    def test_rerun_can_restore_an_earlier_attempt_with_the_same_run_id(self):
        # GitHub keeps the run ID when a failed job is rerun. Restore happens
        # before the new attempt uploads state, so this is the earlier attempt.
        github = FakeGitHub(artifacts=[artifact(100)])
        self.assertTrue(self.restore(github, current_run_id='100'))
        self.assertEqual('100', github.calls[-1][3])

    def test_run_metadata_must_confirm_workflow_event_repository_and_branch(self):
        for change in ({'event': 'pull_request'}, {'event': 'push'}, {'head_branch': 'other'},
                       {'path': '.github/workflows/unrelated.yml'}, {'id': 77},
                       {'repository': {'id': 999}}, {'head_repository': {'id': 999}}):
            with self.subTest(change=change):
                github = FakeGitHub(runs={42: metadata(**change)})
                self.assertFalse(self.restore(github))
                self.assertEqual(3, len(github.calls))
        github = FakeGitHub(runs={42: metadata(event='workflow_dispatch',
                                             path='.github/workflows/cron.yml@refs/heads/main')})
        self.assertTrue(self.restore(github))

    def test_wrong_date_policy_and_corrupt_data_are_skipped_for_older_valid_state(self):
        def wrong_date(directory):
            CheckpointStore(directory, '2026-09-06', POLICY).save({}, {})
        def wrong_policy(directory):
            CheckpointStore(directory, DATE, 'old-policy').save({}, {})
        def corrupt(directory):
            (directory / f'{DATE}.json').write_text('{broken secret content')
        for creator in (wrong_date, wrong_policy, corrupt):
            with self.subTest(creator=creator.__name__):
                github = FakeGitHub(artifacts=[artifact(41), artifact(42)], downloads={42: creator})
                with self.assertLogs(workflow.LOGGER, level='WARNING') as messages:
                    self.assertTrue(self.restore(github))
                self.assertNotIn('secret content', ''.join(messages.output))
                downloads = [call[3] for call in github.calls if call[:3] == ['gh', 'run', 'download']]
                self.assertEqual(['42', '41'], downloads)

    def test_symlink_and_oversized_date_files_are_not_restored(self):
        external = Path(self.temporary.name) / 'outside'
        external.mkdir()
        FakeGitHub.valid_checkpoint(external)
        def symlink(directory):
            (directory / f'{DATE}.json').symlink_to(external / f'{DATE}.json')
        def oversized(directory):
            (directory / f'{DATE}.json').write_bytes(b' ' * (workflow.MAX_ARTIFACT_BYTES + 1))
        for creator in (symlink, oversized):
            with self.subTest(creator=creator.__name__), patch.object(workflow.LOGGER, 'warning'):
                self.assertFalse(self.restore(FakeGitHub(downloads={42: creator})))
                self.assertFalse(self.directory.exists())

    def test_remote_failures_propagate_instead_of_silently_starting_fresh(self):
        for stage in ('repository', 'listing', 'metadata', 'download'):
            def failure(command):
                matches = {'repository': command[-1] == f'repos/{REPO}',
                           'listing': command[-1].endswith('artifacts?per_page=100'),
                           'metadata': '/actions/runs/' in command[-1],
                           'download': command[:3] == ['gh', 'run', 'download']}
                if matches[stage]:
                    raise subprocess.CalledProcessError(1, command, stderr='private error detail')
            with self.subTest(stage=stage), self.assertRaises(subprocess.CalledProcessError):
                self.restore(FakeGitHub(failure=failure))
        with patch.object(workflow.LOGGER, 'warning'), self.assertRaises(subprocess.TimeoutExpired):
            self.restore(FakeGitHub(failure=lambda command: (_ for _ in ()).throw(
                subprocess.TimeoutExpired(command, 60))))
        self.assertFalse(self.directory.exists())

    def test_only_ten_newest_eligible_artifacts_are_considered(self):
        candidates = [artifact(index, created_at=f'2026-09-07T10:{index:02}:00Z') for index in range(1, 21)]
        runs = {index: metadata(index, event='push') for index in range(1, 21)}
        github = FakeGitHub(artifacts=candidates, runs=runs)
        self.assertFalse(self.restore(github))
        metadata_calls = [call for call in github.calls if '/actions/runs/' in call[-1]]
        self.assertEqual(10, len(metadata_calls))
        self.assertEqual(list(range(20, 10, -1)), [int(call[-1].rsplit('/', 1)[-1]) for call in metadata_calls])

    def test_recovery_does_not_overwrite_existing_state_if_destination_write_fails(self):
        existing = CheckpointStore(self.directory, DATE, POLICY)
        existing.save({'title': 'Previous state'}, {})
        original = existing.path.read_bytes()
        real_save = CheckpointStore.save
        def save(store, *arguments):
            if store.path.parent == self.directory:
                raise OSError('disk failed')
            return real_save(store, *arguments)
        with patch.object(CheckpointStore, 'save', save), self.assertRaises(OSError):
            self.restore(FakeGitHub())
        self.assertEqual(original, existing.path.read_bytes())

    def test_temporary_failures_recover_at_each_github_read_stage(self):
        for stage in ('repository', 'listing', 'metadata', 'download'):
            failed = False
            def failure(command):
                nonlocal failed
                matches = {'repository': command[-1] == f'repos/{REPO}',
                           'listing': command[-1].endswith('artifacts?per_page=100'),
                           'metadata': '/actions/runs/' in command[-1],
                           'download': command[:3] == ['gh', 'run', 'download']}
                if matches[stage] and not failed:
                    failed = True
                    raise subprocess.CalledProcessError(1, command, stderr='private detail (HTTP 503)')
            with self.subTest(stage=stage), self.assertLogs(workflow.LOGGER, level='WARNING') as messages:
                github = FakeGitHub(failure=failure)
                sleep = Mock()
                self.assertTrue(self.restore(github, _sleep=sleep))
            self.assertEqual(5, len(github.calls))
            sleep.assert_called_once_with(2)
            self.assertNotIn('private detail', ''.join(messages.output))

    def test_http_and_clear_network_outages_retry_without_logging_diagnostics(self):
        diagnostics = [f'gh: temporary error (HTTP {status})' for status in (408, 429, 500, 502, 503, 504, 599)]
        diagnostics += ['connection reset by peer', 'dial tcp: i/o timeout', 'connection timed out',
                        'TLS handshake timeout', 'context deadline exceeded',
                        'temporary failure in name resolution', 'temporary failure resolving github.com']
        for detail in diagnostics:
            with self.subTest(detail=detail):
                arguments = ['gh', 'api', f'repos/{REPO}']
                error = subprocess.CalledProcessError(1, arguments, stderr=f'private token: {detail}')
                result = SimpleNamespace(stdout='response')
                command = Mock(side_effect=[error, result])
                sleep = Mock()
                with self.assertLogs(workflow.LOGGER, level='WARNING') as messages:
                    self.assertIs(result, workflow._command(command, arguments, sleep))
                self.assertEqual(2, command.call_count)
                sleep.assert_called_once_with(2)
                self.assertNotIn('private token', ''.join(messages.output))

    def test_permanent_http_and_unknown_errors_fail_once(self):
        for detail in ['HTTP 401 connection timed out', 'HTTP 403 i/o timeout',
                       'HTTP 404', 'HTTP 422', 'invalid command', 'no artifact found',
                       'connection timed out' + 'x' * 10000 + ' (HTTP 403)']:
            with self.subTest(detail=detail):
                arguments = ['gh', 'api', f'repos/{REPO}']
                error = subprocess.CalledProcessError(1, arguments, stderr=detail)
                command = Mock(side_effect=error)
                sleep = Mock()
                with self.assertRaises(subprocess.CalledProcessError) as caught:
                    workflow._command(command, arguments, sleep)
                self.assertIs(error, caught.exception)
                self.assertEqual(1, command.call_count)
                sleep.assert_not_called()

    def test_exhausted_timeouts_preserve_last_error_with_three_calls_and_two_waits(self):
        arguments = ['gh', 'api', f'repos/{REPO}']
        errors = [subprocess.TimeoutExpired(arguments, 60),
                  subprocess.CalledProcessError(1, arguments, stderr='gh: HTTP 502'),
                  subprocess.TimeoutExpired(arguments, 60)]
        command = Mock(side_effect=errors)
        sleep = Mock()
        with patch.object(workflow.LOGGER, 'warning'), self.assertRaises(subprocess.TimeoutExpired) as caught:
            workflow._command(command, arguments, sleep)
        self.assertIs(errors[-1], caught.exception)
        self.assertEqual(3, command.call_count)
        self.assertEqual([2, 4], [call.args[0] for call in sleep.call_args_list])
        for call in command.call_args_list:
            self.assertEqual((arguments,), call.args)
            self.assertEqual({'check': True, 'capture_output': True, 'text': True, 'timeout': 60}, call.kwargs)


if __name__ == '__main__':
    unittest.main()
