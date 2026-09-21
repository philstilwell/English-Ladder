"""Wait for Cloudflare's GitHub integration and explain stale deployments safely."""
import argparse
import json
import math
import re
import subprocess
import time
from pathlib import Path
from urllib.parse import urlsplit


DEFAULT_TIMEOUT = 12 * 60
DEFAULT_INTERVAL = 20
REQUEST_TIMEOUT = 30
MAX_DIFFERENCES = 5


def fetch_json(url, timeout=REQUEST_TIMEOUT):
    result = subprocess.run(
        ['curl', '--fail', '--silent', '--show-error', '--max-time', str(timeout),
         '--user-agent', 'English-family-deploy-check', url],
        capture_output=True, text=True, check=True, timeout=timeout,
    )
    return json.loads(result.stdout)


def validate_manifest(manifest):
    if not isinstance(manifest, dict):
        raise ValueError('Deployment manifest must be an object.')
    revision = manifest.get('revision')
    files = manifest.get('files')
    if not isinstance(revision, str) or not re.fullmatch(r'(?:[0-9a-f]{40}|[0-9a-f]{64})', revision):
        raise ValueError('Deployment manifest has an invalid revision.')
    if not isinstance(files, dict) or not files:
        raise ValueError('Deployment manifest has no public files.')
    if any(not isinstance(file, str) or not isinstance(digest, str)
           or not re.fullmatch(r'[0-9a-f]{64}', digest)
           for file, digest in files.items()):
        raise ValueError('Deployment manifest has invalid file hashes.')
    return manifest


def differences(expected, live):
    missing = sorted(set(expected) - set(live))
    changed = sorted(file for file in set(expected) & set(live)
                     if expected[file] != live[file])
    unexpected = sorted(set(live) - set(expected))
    samples = [{'file': file, 'difference': kind}
               for kind, paths in [('missing', missing), ('changed', changed),
                                   ('unexpected', unexpected)]
               for file in paths][:MAX_DIFFERENCES]
    return {'missing': len(missing), 'changed': len(changed),
            'unexpected': len(unexpected), 'examples': samples}


def wait_for_publishing(origin, expected, *, timeout=DEFAULT_TIMEOUT,
                        interval=DEFAULT_INTERVAL, fetch=fetch_json,
                        clock=time.monotonic, sleep=time.sleep, log=print):
    """Return a bounded, secret-free report; a matching full file map is success."""
    validate_manifest(expected)
    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError('Timeout must be a finite positive number.')
    if not math.isfinite(interval) or interval <= 0:
        raise ValueError('Interval must be a finite positive number.')
    origin = origin.rstrip('/')
    started = clock()
    deadline = started + timeout
    report = {
        'status': 'waiting', 'origin': origin,
        'expected_revision': expected['revision'],
        'expected_file_count': len(expected['files']),
        'expected_revision_seen': False, 'attempts': 0,
        'last_live_revision': None, 'last_live_file_count': None,
        'differences': None, 'last_fetch_error': None,
    }
    log(f"Waiting for Cloudflare: expected revision {expected['revision']}, "
        f"{len(expected['files'])} public files (up to {timeout:g} seconds).")
    last_message = None
    while (remaining := deadline - clock()) > 0:
        report['attempts'] += 1
        try:
            # The current-lesson verifier separately checks the ordinary public
            # URLs. Here a fresh manifest shows the build Cloudflare has received.
            live = validate_manifest(fetch(
                f'{origin}/deployment.json?verify={time.time_ns()}-{report["attempts"]}',
                timeout=min(REQUEST_TIMEOUT, remaining),
            ))
            report['last_live_revision'] = live['revision']
            report['last_live_file_count'] = len(live['files'])
            report['expected_revision_seen'] |= live['revision'] == expected['revision']
            report['last_fetch_error'] = None
            report['differences'] = differences(expected['files'], live['files'])
            # A newer code-only commit may have identical public files. Accept
            # those files, but report the actual revision instead of claiming it
            # is the expected commit. Never accept revision alone as proof.
            if live['files'] == expected['files']:
                report['status'] = 'success'
                report['elapsed_seconds'] = round(clock() - started, 3)
                log(f"Cloudflare publishes all {len(expected['files'])} expected public files; "
                    f"live revision {live['revision']}.")
                return report
            delta = report['differences']
            message = (f"Live revision {live['revision']} has {len(live['files'])} public files; "
                       f"{delta['missing']} missing, {delta['changed']} changed, "
                       f"{delta['unexpected']} unexpected. Examples: "
                       f"{json.dumps(delta['examples'], ensure_ascii=True)}")
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, ValueError) as error:
            if isinstance(error, subprocess.CalledProcessError):
                problem = f'HTTP or connection failure (curl exit {error.returncode})'
            elif isinstance(error, subprocess.TimeoutExpired):
                problem = 'request timed out'
            else:
                problem = 'invalid deployment manifest'
            # Never copy response bodies, curl stderr, or exception text into
            # logs/artifacts; only known diagnostic categories are retained.
            report['last_fetch_error'] = problem
            message = f'Cloudflare deployment check: {problem}; retrying within the remaining time.'
        if message != last_message:
            log(message)
            last_message = message
        remaining = deadline - clock()
        if remaining > 0:
            sleep(min(interval, remaining))
    report['status'] = 'timed_out'
    report['elapsed_seconds'] = round(clock() - started, 3)
    log(f"Cloudflare did not publish the expected public files within {timeout:g} seconds. "
        f"Expected revision {expected['revision']}; last valid live revision "
        f"{report['last_live_revision'] or 'unavailable'}. GitHub source is saved. "
        'Inspect the Cloudflare build for this commit and retry the failed build. '
        'Then rerun only the failed publishing job, or run the Daily ESL Lesson Generator with deploy_only=true, to verify publishing '
        'without paid lesson, translation, or image generation.')
    return report


def positive_seconds(value):
    try:
        number = float(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError('must be a positive number of seconds') from error
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError('must be a finite positive number of seconds')
    return number


def site_origin(value):
    parsed = urlsplit(value)
    if (parsed.scheme not in ('http', 'https') or not parsed.netloc
            or parsed.path not in ('', '/') or parsed.query or parsed.fragment
            or parsed.username is not None or parsed.password is not None):
        raise argparse.ArgumentTypeError('provide an HTTP(S) site origin without credentials, path, or query')
    return value.rstrip('/')


def write_report(path, report):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    temporary.replace(path)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('origin', type=site_origin)
    parser.add_argument('--timeout', type=positive_seconds, default=DEFAULT_TIMEOUT,
                        help='maximum wait in seconds (default: 720)')
    parser.add_argument('--interval', type=positive_seconds, default=DEFAULT_INTERVAL,
                        help='seconds between requests (default: 20)')
    parser.add_argument('--report', type=Path, help='write a JSON publishing report')
    args = parser.parse_args(argv)
    expected = json.loads(Path('.cf-site/deployment.json').read_text())
    report = wait_for_publishing(args.origin, expected, timeout=args.timeout, interval=args.interval)
    if args.report:
        write_report(args.report, report)
    return 0 if report['status'] == 'success' else 1


if __name__ == '__main__':
    raise SystemExit(main())
