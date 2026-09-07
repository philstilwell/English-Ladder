"""Restore a compatible daily-generation checkpoint from a trusted workflow run.

Only this repository's scheduled/manual daily workflow is eligible. Restored
content still requires the generation pipeline's factual and approval checks.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

from lesson_checkpoint import CheckpointStore

LOGGER = logging.getLogger(__name__)
MAX_ARTIFACT_BYTES = 5 * 1024 * 1024
MAX_CANDIDATES = 10
WORKFLOW_PATH = '.github/workflows/cron.yml'
RETRY_DELAYS = (2, 4)


class InvalidCheckpoint(ValueError):
    """Downloaded state is unsafe, damaged, or incompatible with this run."""


def _temporary_command_failure(error):
    if isinstance(error, subprocess.TimeoutExpired):
        return True
    if not isinstance(error, subprocess.CalledProcessError):
        return False
    # Inspect only a bounded amount of diagnostics, and never emit them. A
    # stated HTTP status takes precedence over incidental words in the body.
    detail = error.stderr or ''
    if not isinstance(detail, (str, bytes)):
        return False
    if len(detail) > 4096:
        # gh commonly appends the actual HTTP status after the response body.
        detail = detail[:2048] + detail[-2048:]
    if isinstance(detail, bytes):
        detail = detail.decode('utf-8', errors='replace')
    statuses = list(re.finditer(r'\bHTTP(?:/\d(?:\.\d)?)?\s+([1-5]\d{2})\b', detail, re.IGNORECASE))
    if statuses:
        code = int(statuses[-1].group(1))
        return code in (408, 429) or 500 <= code <= 599
    detail = detail.casefold()
    return any(message in detail for message in (
        'connection reset by peer', 'connection timed out', 'i/o timeout',
        'tls handshake timeout', 'context deadline exceeded',
        'temporary failure in name resolution', 'temporary failure resolving',
        'temporary dns failure',
    ))


def _command(run_command, arguments, _sleep=None):
    sleep = time.sleep if _sleep is None else _sleep
    for attempt in range(len(RETRY_DELAYS) + 1):
        try:
            return run_command(arguments, check=True, capture_output=True, text=True, timeout=60)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
            if attempt == len(RETRY_DELAYS) or not _temporary_command_failure(error):
                raise
            delay = RETRY_DELAYS[attempt]
            LOGGER.warning('Temporary checkpoint service failure (%s); retrying in %ss.',
                           type(error).__name__, delay)
            sleep(delay)


def _api(run_command, path, _sleep=None):
    return json.loads(_command(run_command, ['gh', 'api', path], _sleep).stdout)


def _same_id(value, expected):
    return type(value) is int and value > 0 and value == expected


def _eligible_artifact(artifact, repository_id, branch):
    if not isinstance(artifact, dict):
        return False
    run = artifact.get('workflow_run')
    size = artifact.get('size_in_bytes')
    return (
        isinstance(artifact.get('name'), str)
        and artifact['name'].startswith('lesson-state-')
        and artifact.get('expired') is False
        and type(size) is int and 0 < size <= MAX_ARTIFACT_BYTES
        and isinstance(run, dict)
        and type(run.get('id')) is int and run['id'] > 0
        and _same_id(run.get('repository_id'), repository_id)
        and _same_id(run.get('head_repository_id'), repository_id)
        and run.get('head_branch') == branch
    )


def _eligible_run(run, repository_id, run_id, branch):
    if not isinstance(run, dict):
        return False
    repository = run.get('repository')
    head_repository = run.get('head_repository')
    path = run.get('path')
    return (
        _same_id(run.get('id'), run_id)
        and isinstance(repository, dict) and _same_id(repository.get('id'), repository_id)
        and isinstance(head_repository, dict) and _same_id(head_repository.get('id'), repository_id)
        and run.get('head_branch') == branch
        and run.get('event') in ('schedule', 'workflow_dispatch')
        and isinstance(path, str) and path.split('@', 1)[0] == WORKFLOW_PATH
    )


def restore_checkpoint(repo, branch, release_date, directory, policy_fingerprint,
                       current_run_id='', run_command=subprocess.run, _sleep=None):
    """Restore at most one valid date file, returning whether state was found.

    GitHub failures propagate after bounded transient retries: an unavailable
    checkpoint service must not silently trigger paid generation from scratch. An invalid
    artifact is skipped so an older valid checkpoint can still be recovered.

    ``current_run_id`` remains accepted for workflow CLI compatibility. A
    failed-job rerun retains that ID and may reuse its earlier attempt's state.
    Restoration must run before the current attempt uploads its own artifact.
    """
    if not isinstance(repo, str) or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo):
        raise ValueError('Repository must use owner/name.')
    if not isinstance(branch, str) or not branch:
        raise ValueError('A branch is required.')
    if directory is None:
        raise ValueError('A checkpoint destination is required.')
    destination = CheckpointStore(directory, release_date, policy_fingerprint)
    repository = _api(run_command, f'repos/{repo}', _sleep)
    repository_id = repository.get('id') if isinstance(repository, dict) else None
    if (type(repository_id) is not int or repository_id <= 0
            or not isinstance(repository.get('full_name'), str)
            or repository['full_name'].casefold() != repo.casefold()):
        raise ValueError('GitHub did not identify the requested repository.')
    listing = _api(run_command, f'repos/{repo}/actions/artifacts?per_page=100', _sleep)
    if not isinstance(listing, dict) or not isinstance(listing.get('artifacts'), list):
        raise ValueError('GitHub returned an invalid artifact listing.')
    candidates = sorted(
        (artifact for artifact in listing['artifacts']
         if _eligible_artifact(artifact, repository_id, branch)),
        key=lambda artifact: str(artifact.get('created_at', '')), reverse=True,
    )[:MAX_CANDIDATES]
    for artifact in candidates:
        run_id = artifact['workflow_run']['id']
        metadata = _api(run_command, f'repos/{repo}/actions/runs/{run_id}', _sleep)
        if not _eligible_run(metadata, repository_id, run_id, branch):
            continue
        with tempfile.TemporaryDirectory(prefix='englishladder-checkpoint-') as temporary:
            _command(run_command, ['gh', 'run', 'download', str(run_id), '--repo', repo,
                                   '--name', artifact['name'], '--dir', temporary], _sleep)
            saved = CheckpointStore(temporary, release_date, policy_fingerprint)
            try:
                path = saved.path
                if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_ARTIFACT_BYTES:
                    raise InvalidCheckpoint()
                if path.resolve().parent != Path(temporary).resolve():
                    raise InvalidCheckpoint()
                checkpoint = saved.load()
                if checkpoint is None:
                    raise InvalidCheckpoint()
            except (OSError, ValueError) as error:
                LOGGER.warning('Skipping unusable checkpoint artifact (%s).', type(error).__name__)
                continue
            # Re-save only the validated date's sections through the atomic
            # store. Other archive files are never copied into the workspace.
            destination.save(checkpoint['source'], checkpoint['levels'], checkpoint['drafts'])
            LOGGER.info('Restored generation checkpoint for %s.', release_date)
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True)
    parser.add_argument('--branch', required=True)
    parser.add_argument('--date', required=True, dest='release_date')
    parser.add_argument('--directory', required=True)
    parser.add_argument('--policy-fingerprint')
    parser.add_argument('--current-run-id', default=os.environ.get('GITHUB_RUN_ID', ''))
    arguments = parser.parse_args()
    if arguments.policy_fingerprint is None:
        from update_site import generation_policy_fingerprint
        arguments.policy_fingerprint = generation_policy_fingerprint()
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    try:
        restored = restore_checkpoint(**vars(arguments))
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        LOGGER.error('Checkpoint restoration failed (%s).', type(error).__name__)
        return 1
    if not restored:
        LOGGER.info('No compatible generation checkpoint found for %s.', arguments.release_date)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
