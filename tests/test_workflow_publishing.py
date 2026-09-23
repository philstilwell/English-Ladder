"""Exercise runner authentication and the real cleanup shell with disposable Git repos."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest

WORKFLOW = (Path(__file__).resolve().parents[1] / '.github/workflows/cron.yml').read_text()


def step_script(name):
    lines = WORKFLOW.splitlines()
    start = lines.index('      - name: ' + name)
    run = next(i for i in range(start + 1, len(lines)) if lines[i].startswith('        run:'))
    if lines[run] != '        run: |':
        return lines[run].removeprefix('        run: ')
    end = run + 1
    while end < len(lines) and (not lines[end].strip() or lines[end].startswith('          ')):
        end += 1
    return textwrap.dedent('\n'.join(lines[run + 1:end]))


def job_condition(job, values):
    section = WORKFLOW.split('\n  ' + job + ':\n', 1)[1]
    expression = next(line[8:] for line in section.splitlines() if line.startswith('    if: '))
    expression = expression.replace('always()', 'True').replace('&&', ' and ').replace('||', ' or ')
    for key in sorted(values, key=len, reverse=True):
        expression = expression.replace(key, repr(values[key]))
    return eval(expression, {'__builtins__': {}}, {})


@unittest.skipUnless(shutil.which('git') and shutil.which('gh'), 'Git and GitHub CLI are required')
class WorkflowPublishingTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.repo = self.root / 'checkout'
        self.remote = self.root / 'remote.git'
        self.bin = self.root / 'bin'
        self.bin.mkdir()
        self.git = shutil.which('git')
        self.env = {**os.environ, 'GH_TOKEN': 'synthetic-offline-test-token',
                    'GH_CONFIG_DIR': str(self.root / 'gh'), 'GIT_CONFIG_GLOBAL': str(self.root / 'gitconfig'),
                    'GIT_CONFIG_NOSYSTEM': '1', 'GIT_TERMINAL_PROMPT': '0',
                    'GITHUB_REF_NAME': 'main', 'GITHUB_OUTPUT': str(self.root / 'outputs'),
                    'TEST_ROOT': str(self.root), 'REAL_GIT': self.git}
        subprocess.run([self.git, 'init', '--bare', str(self.remote)], check=True, capture_output=True, env=self.env)
        subprocess.run([self.git, 'init', '-b', 'main', str(self.repo)], check=True, capture_output=True, env=self.env)
        for name in ('index.html', 'archive/keep.json', 'news/expired/beginner.html', 'assets/news/keep.json',
                     'data/vocabulary-translations/keep.json', 'lesson-data.json', 'sitemap.xml',
                     'sitemaps/keep.xml', 'content/seo-index.json', 'robots.txt'):
            path = self.repo / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('Before cleanup\n')
        self.run_git('config', 'user.name', 'Test')
        self.run_git('config', 'user.email', 'test@example.invalid')
        self.run_git('add', '.')
        self.run_git('commit', '-m', 'Initial edition')
        self.run_git('remote', 'add', 'origin', str(self.remote))
        self.run_git('push', '-u', 'origin', 'main')
        self.initial = self.run_git('rev-parse', 'HEAD').stdout.strip()
        self.executable('sleep', '#!/bin/sh\nexit 0\n')
        self.executable('git', f'''#!{sys.executable}
import json, os, pathlib, sys
root = pathlib.Path(os.environ['TEST_ROOT'])
args = sys.argv[1:]
with (root / 'git-calls').open('a') as log: log.write(json.dumps(args) + '\\n')
if args and args[0] in ('fetch', 'push'):
    operation = args[0]
    counter = root / (operation + '-count')
    count = int(counter.read_text()) + 1 if counter.exists() else 1
    counter.write_text(str(count))
    if count <= int(os.environ.get('FAIL_' + operation.upper(), '0')):
        print('fatal: simulated transport failure', file=sys.stderr)
        sys.exit(128)
os.execv(os.environ['REAL_GIT'], [os.environ['REAL_GIT']] + args)
''')
        self.executable('python', f'''#!{sys.executable}
import os, pathlib, sys
root = pathlib.Path(os.environ['TEST_ROOT'])
with (root / 'python-calls').open('a') as log: log.write(' '.join(sys.argv[1:]) + '\\n')
if sys.argv[1:] == ['update_site.py', '--refresh-pages']:
    pathlib.Path('news/expired/beginner.html').unlink(missing_ok=True)
    pathlib.Path('index.html').write_text('Retained edition\\n')
elif sys.argv[1:] == ['audit_site.py']:
    sys.exit(int(os.environ.get('FAIL_AUDIT', '0')))
else:
    raise SystemExit('Unexpected generation command in cleanup-only flow')
''')
        self.env['PATH'] = str(self.bin) + os.pathsep + self.env['PATH']

    def executable(self, name, source):
        path = self.bin / name
        path.write_text(source)
        path.chmod(0o700)

    def run_git(self, *args):
        return subprocess.run([self.git, *args], cwd=self.repo, env=self.env, text=True, capture_output=True, check=True)

    def cleanup(self, **failures):
        return subprocess.run(['bash', '-e', '-o', 'pipefail', '-c',
                               step_script('Rebuild and save the retained archive')],
                              cwd=self.repo, env={**self.env, **failures}, text=True, capture_output=True, timeout=20)

    def test_credential_helper_works_without_checkout_credentials(self):
        # Use the workflow's actual setup command, with a synthetic token and no user config.
        setup = next(line.strip() for line in step_script('Rebuild and save the retained archive').splitlines()
                     if line.strip().startswith('gh auth setup-git'))
        subprocess.run(['bash', '-e', '-c', setup], cwd=self.repo, env=self.env, check=True, capture_output=True)
        result = subprocess.run([self.git, 'credential', 'fill'], input='protocol=https\nhost=github.com\n\n',
                                cwd=self.repo, env=self.env, text=True, capture_output=True, check=True, timeout=15)
        self.assertIn('password=' + self.env['GH_TOKEN'], result.stdout)
        self.assertNotIn(self.env['GH_TOKEN'], (self.root / 'gitconfig').read_text())

    def test_transient_fetch_failure_retries_then_publishes_cleanup(self):
        result = self.cleanup(FAIL_FETCH='1')
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual('2', (self.root / 'fetch-count').read_text())
        self.assertEqual('Retained edition', self.run_git('show', 'origin/main:index.html').stdout.strip())
        self.assertNotIn('news/expired/beginner.html', self.run_git('ls-tree', '-r', '--name-only', 'origin/main').stdout)
        self.assertNotIn(self.env['GH_TOKEN'], result.stdout + result.stderr + (self.root / 'git-calls').read_text())

    def test_transient_push_failure_rebuilds_after_refreshing_branch(self):
        result = self.cleanup(FAIL_PUSH='1')
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertEqual('2', (self.root / 'push-count').read_text())
        self.assertEqual(2, (self.root / 'python-calls').read_text().count('update_site.py --refresh-pages'))
        self.assertEqual(self.run_git('rev-parse', 'HEAD').stdout, self.run_git('rev-parse', 'origin/main').stdout)

    def test_permanent_fetch_failure_is_bounded_and_explains_authentication(self):
        result = self.cleanup(FAIL_FETCH='99')
        self.assertNotEqual(0, result.returncode)
        self.assertEqual('3', (self.root / 'fetch-count').read_text())
        self.assertIn('::error::Archive cleanup could not fetch', result.stdout)
        self.assertIn('LESSON_PUBLISH_TOKEN', result.stdout)
        self.assertFalse((self.root / 'python-calls').exists())
        self.assertEqual(self.initial, self.run_git('rev-parse', 'origin/main').stdout.strip())

    def test_failed_audit_never_pushes(self):
        result = self.cleanup(FAIL_AUDIT='1')
        self.assertNotEqual(0, result.returncode)
        self.assertFalse((self.root / 'push-count').exists())
        self.assertEqual(self.initial, self.run_git('rev-parse', 'origin/main').stdout.strip())

    def test_checked_revision_is_recorded_even_without_a_cleanup_commit(self):
        result = subprocess.run(['bash', '-e', '-c', step_script('Record checked archive revision')],
                                cwd=self.repo, env=self.env, text=True, capture_output=True)
        self.assertEqual(0, result.returncode)
        self.assertEqual('revision=' + self.initial, (self.root / 'outputs').read_text().strip())


class WorkflowRoutingTests(unittest.TestCase):
    def test_manual_maintenance_never_enters_content_generation(self):
        for event, maintenance, email, result, expected in (
            ('workflow_dispatch', 'true', 'false', 'success', (True, False)),
            ('workflow_dispatch', 'true', 'true', 'skipped', (False, False)),
            ('schedule', '', '', 'success', (True, True)),
            ('schedule', '', '', 'failure', (True, False)),
            ('push', '', '', 'skipped', (False, True)),
            ('workflow_dispatch', 'false', 'false', 'skipped', (False, True)),
        ):
            values = {'github.event_name': event, 'github.event.inputs.maintenance_only': maintenance,
                      'github.event.inputs.test_email': email, 'needs.maintain_archive.result': result}
            with self.subTest(event=event, maintenance=maintenance, email=email, result=result):
                self.assertEqual(expected, tuple(job_condition(job, values)
                                 for job in ('maintain_archive', 'build_and_deploy')))


if __name__ == '__main__':
    unittest.main()
