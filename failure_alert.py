"""Send the final daily failure report using an existing, TLS-secured mail account.

The workflow decides when an alert is due. This helper never reads raw job logs,
never sends without mail configuration, and can render a report with --dry-run.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from email.utils import format_datetime
import json
import os
import re
import smtplib
import ssl
import sys
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener

EST = timezone(timedelta(hours=-5), name='EST')
FAILED = {'failure', 'timed_out', 'cancelled', 'action_required', 'startup_failure', 'stale'}
MAX_RESPONSE_BYTES = 1024 * 1024
MAX_FAILED_JOBS = 8
MAX_ANNOTATIONS = 3
API_ROOT = 'https://api.github.com'
DEFAULT_ADDRESS = 'philstilwell@gmail.com'


class ConfigurationError(ValueError):
    """A required setting is missing or unsafe."""


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Diagnostic requests must not forward the workflow token elsewhere.
        return None


def clean_text(value, env, limit=500):
    """Bound untrusted diagnostic text and redact any known credential values."""
    text = str(value or '')[:20000]
    sensitive = [str(value) for name, value in env.items() if value and (
        name.endswith(('_PASSWORD', '_TOKEN', '_KEY', '_SECRET'))
        or name in {'SMTP_USERNAME', 'SMTP_PASSWORD'}
    )]
    for secret in sorted(sensitive, key=len, reverse=True):
        text = text.replace(secret, '[redacted]')
    text = re.sub(r'(?i)\b(?:bearer|basic)\s+\S+', '[redacted authorization]', text)
    text = re.sub(r'[\x00-\x1f\x7f-\x9f]', ' ', text)
    text = ' '.join(text.split())
    return text[:limit] + ('…' if len(text) > limit else '')


def run_context(env):
    repo = env.get('GITHUB_REPOSITORY', '')
    run_id = env.get('GITHUB_RUN_ID', '')
    attempt = env.get('GITHUB_RUN_ATTEMPT', '1')
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo):
        raise ConfigurationError('GITHUB_REPOSITORY must be owner/repository.')
    if not re.fullmatch(r'[1-9][0-9]*', run_id):
        raise ConfigurationError('GITHUB_RUN_ID must be a positive number.')
    if not re.fullmatch(r'[1-9][0-9]*', attempt):
        raise ConfigurationError('GITHUB_RUN_ATTEMPT must be a positive number.')
    return repo, run_id, attempt


def api_json(path, env):
    headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2026-03-10',
               'User-Agent': 'English-Ladder-failure-alert'}
    token = env.get('GITHUB_TOKEN') or env.get('GH_TOKEN')
    if token:
        headers['Authorization'] = 'Bearer ' + token
    request = Request(API_ROOT + path, headers=headers)
    with build_opener(NoRedirect()).open(request, timeout=20) as response:
        payload = response.read(MAX_RESPONSE_BYTES + 1)
    if len(payload) > MAX_RESPONSE_BYTES:
        raise ValueError('GitHub diagnostic response exceeded the size limit.')
    return json.loads(payload)


def collect_diagnostics(env, fetch=api_json):
    repo, run_id, attempt = run_context(env)
    details = []
    warnings = []
    try:
        payload = fetch(f'/repos/{repo}/actions/runs/{run_id}/attempts/{attempt}/jobs?per_page=100', env)
        jobs = payload['jobs']
        if not isinstance(jobs, list):
            raise ValueError('Invalid job list.')
        if payload.get('total_count', len(jobs)) > len(jobs):
            warnings.append('Only the first 100 jobs were inspected.')
    except (HTTPError, URLError, OSError, ValueError, KeyError, TypeError):
        return [], ['GitHub could not provide detailed failure information; use the run link below.']
    for job in jobs:
        if not isinstance(job, dict):
            continue
        failed_steps = [s for s in job.get('steps', []) if isinstance(s, dict) and s.get('conclusion') in FAILED]
        step_only = job.get('conclusion') not in FAILED
        if step_only:
            # A translation failure is allowed to keep English publication going.
            # Exclude unrelated recovered steps such as the fallback checkout.
            failed_steps = [s for s in failed_steps if 'translat' in str(s.get('name', '')).lower()]
            if env.get('TRANSLATIONS_RESULT') not in FAILED or not failed_steps:
                continue
        steps = [clean_text(s.get('name', 'Unknown step'), env, 180) for s in failed_steps][:5]
        detail = {'name': clean_text(job.get('name', 'Unknown job'), env, 180),
                  'conclusion': 'failure' if step_only else job['conclusion'],
                  'step_only': step_only, 'steps': steps, 'annotations': []}
        check_url = job.get('check_run_url', '')
        match = re.fullmatch(re.escape(f'{API_ROOT}/repos/{repo}/check-runs/') + r'([1-9][0-9]*)', check_url or '')
        if match:
            try:
                annotations = fetch(f'/repos/{repo}/check-runs/{match.group(1)}/annotations?per_page=100', env)
                if not isinstance(annotations, list):
                    raise ValueError('Invalid annotations.')
                for annotation in annotations:
                    if isinstance(annotation, dict) and annotation.get('annotation_level') == 'failure':
                        message = clean_text(annotation.get('message', ''), env)
                        if message and message not in detail['annotations']:
                            detail['annotations'].append(message)
                    if len(detail['annotations']) >= MAX_ANNOTATIONS:
                        break
            except (HTTPError, URLError, OSError, ValueError, TypeError):
                warnings.append('GitHub could not provide error notes for ' + detail['name'] + '.')
        details.append(detail)
        if len(details) >= MAX_FAILED_JOBS:
            break
    return details, warnings


def explain_failure(detail):
    """Describe the failed stage without claiming to know an unavailable cause."""
    stage = ' '.join(detail['steps'] or [detail['name']]).lower()
    if detail['conclusion'] == 'timed_out':
        return 'This job exceeded its allowed running time.'
    if detail['conclusion'] == 'cancelled':
        return 'This job was cancelled before it completed.'
    if any(word in stage for word in ('cloudflare', 'publishing', 'public domain', 'current lesson')):
        return 'The saved lessons could not be confirmed on the live website. The hosting service may still be serving an older version.'
    if any(word in stage for word in ('retention', 'cleanup', 'expired', 'older lessons', 'maintenance')):
        return 'The daily removal of lessons older than the 50-day window did not finish successfully.'
    if any(word in stage for word in ('commit', 'push', 'save checked', 'save generated')):
        return 'The updated lesson files could not be saved to GitHub for publication.'
    if any(word in stage for word in ('install', 'set up', 'checkout', 'dependencies')):
        return 'The job could not prepare the tools or site files needed to run.'
    if any(word in stage for word in ('check', 'audit', 'test', 'validate')):
        return 'A required quality check failed, so the update was stopped for review.'
    if 'translat' in stage:
        return 'Vocabulary translation did not finish. English lessons may already be live, but translated vocabulary support is incomplete.'
    if any(word in stage for word in ('generat', 'lesson')):
        return 'Lesson preparation or review did not finish successfully, so a complete new edition could not be confirmed.'
    return 'This part of the daily update did not complete successfully; the error notes below provide any available cause.'


def build_report(env, details, warnings, now=None):
    repo, run_id, attempt = run_context(env)
    now = now or datetime.now(EST)
    date = now.astimezone(EST).date().isoformat()
    subject = f'English Ladder: final daily attempt failed ({date} EST)'
    lines = [
        'English Ladder needs attention.', '',
        'The final daily attempt, scheduled for 03:15 fixed EST (UTC-5), did not complete successfully.',
        'The scheduled attempts are 01:15, 02:15 and 03:15 fixed EST. Earlier failures do not send email.', '',
    ]
    labels = [('MAINTENANCE_RESULT', '50-day cleanup'), ('GENERATION_RESULT', 'Lesson preparation and saving'),
              ('PUBLISHING_RESULT', 'Live website verification'),
              ('TRANSLATIONS_RESULT', 'Vocabulary translations'), ('IMAGE_RESULT', 'Daily lesson illustration')]
    for key, label in labels:
        if env.get(key):
            result = clean_text(env[key], env, 40)
            suffix = ' (a required earlier stage may have failed)' if result == 'skipped' else ''
            lines.append(f'{label}: {result}{suffix}')
    if env.get('TRANSLATIONS_RESULT') in FAILED:
        lines.extend(['', 'Vocabulary translations did not finish successfully. English lessons may already be live, '
                      'but some translated vocabulary support is missing. Review the vocabulary translation step in the run below.'])
    if env.get('IMAGE_RESULT') in FAILED:
        lines.extend(['', 'The daily lesson illustration is still missing or could not be verified after the final attempt. '
                      'The saved English lesson may already be live. Review the image health check and generation diagnostics in the run below.'])
    for detail in details:
        label = 'Failed step within job' if detail.get('step_only') else 'Failed job'
        lines.extend(['', f"{label}: {detail['name']} ({detail['conclusion']})", explain_failure(detail)])
        if detail['steps']:
            lines.append('Failed step(s): ' + '; '.join(detail['steps']))
        lines.extend('GitHub error note: ' + note for note in detail['annotations'])
    if not details:
        lines.extend(['', 'No more specific error details were available when this email was prepared.'])
    lines.extend([''] + warnings if warnings else [])
    lines.extend(['', f'View this run: https://github.com/{repo}/actions/runs/{run_id}/attempts/{attempt}',
                  '', 'Open the failed job to review its diagnostics. If lesson files were saved but publishing failed, '
                  'retry publication of those saved lessons rather than generating them again.',
                  'No further daily retry is scheduled until 01:15 fixed EST tomorrow.'])
    return subject, '\n'.join(lines) + '\n'


def mail_settings(env):
    required = ('SMTP_HOST', 'SMTP_USERNAME', 'SMTP_PASSWORD', 'ALERT_FROM', 'ALERT_TO')
    missing = [key for key in required if not env.get(key)]
    if missing:
        raise ConfigurationError('Email delivery is not configured. Missing: ' + ', '.join(missing) + '.')
    security = env.get('SMTP_SECURITY', 'starttls').lower()
    if security not in ('starttls', 'ssl'):
        raise ConfigurationError('SMTP_SECURITY must be starttls or ssl; unencrypted mail is not supported.')
    host = env['SMTP_HOST']
    if not re.fullmatch(r'[A-Za-z0-9.-]+', host):
        raise ConfigurationError('SMTP_HOST must be a hostname without a URL or port.')
    try:
        port = int(env.get('SMTP_PORT') or ('465' if security == 'ssl' else '587'))
    except ValueError as error:
        raise ConfigurationError('SMTP_PORT must be a number.') from error
    if not 1 <= port <= 65535:
        raise ConfigurationError('SMTP_PORT must be between 1 and 65535.')
    # A single bare address prevents recipient lists and mail-header injection.
    address = r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?\.[A-Za-z]{2,63}"
    for field in ('ALERT_FROM', 'ALERT_TO'):
        if not re.fullmatch(address, env[field]):
            raise ConfigurationError(field + ' must be one plain email address.')
    return host, port, security


def send_report(env, subject, body):
    host, port, security = mail_settings(env)
    _, run_id, attempt = run_context(env)
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = env['ALERT_FROM']
    message['To'] = env['ALERT_TO']
    message['Date'] = format_datetime(datetime.now(timezone.utc))
    message['Message-ID'] = f'<englishladder-failure-{run_id}-{attempt}@englishladder.com>'
    message.set_content(body)
    context = ssl.create_default_context()
    client = smtplib.SMTP_SSL(host, port, timeout=30, context=context) if security == 'ssl' else smtplib.SMTP(host, port, timeout=30)
    with client as smtp:
        smtp.ehlo()
        if security == 'starttls':
            smtp.starttls(context=context)
            smtp.ehlo()
        smtp.login(env['SMTP_USERNAME'], env['SMTP_PASSWORD'])
        refused = smtp.send_message(message)
        if refused:
            raise smtplib.SMTPRecipientsRefused(refused)
    # Deliberately do not retry: a lost confirmation could otherwise send duplicates.


def main(argv=None, env=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dry-run', action='store_true', help='Print the report without connecting to the email service.')
    parser.add_argument('--test', action='store_true', help='Send a clearly labeled setup test without checking jobs.')
    args = parser.parse_args(argv)
    env = dict(os.environ if env is None else env)
    env.setdefault('ALERT_FROM', DEFAULT_ADDRESS)
    env.setdefault('ALERT_TO', DEFAULT_ADDRESS)
    try:
        run_context(env)
        if not args.dry_run:
            mail_settings(env)
        if args.test:
            repo, run_id, attempt = run_context(env)
            subject = 'English Ladder: failure email setup test'
            body = ('This is a requested test of English Ladder failure notifications.\n\n'
                    'If this email arrived, the configured sending service accepted the test.\n'
                    'This message does not mean a lesson or website update failed.\n\n'
                    'Future failure reports are sent only when the final 03:15 fixed EST (UTC-5) daily attempt fails.\n'
                    f'Test run: https://github.com/{repo}/actions/runs/{run_id}/attempts/{attempt}\n')
        else:
            details, warnings = collect_diagnostics(env)
            subject, body = build_report(env, details, warnings)
        if args.dry_run:
            print(subject + '\n\n' + body)
        else:
            send_report(env, subject, body)
            print('Failure report accepted by the configured email service.')
        return 0
    except ConfigurationError as error:
        print(str(error), file=sys.stderr)
    except smtplib.SMTPAuthenticationError:
        print('Email delivery failed: the sending service rejected its login credentials.', file=sys.stderr)
    except (smtplib.SMTPException, OSError, ValueError) as error:
        print('Email delivery failed (' + type(error).__name__ + '). Check the sending service settings and availability.', file=sys.stderr)
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
