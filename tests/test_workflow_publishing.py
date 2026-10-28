"""Guard the no-API daily trigger and offline publication workflow."""
from pathlib import Path
import os
import re
import shutil
import subprocess
import tempfile
import textwrap
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = (ROOT / ".github/workflows/cron.yml").read_text()


class WorkflowPublishingTests(unittest.TestCase):
    def test_github_workflow_has_no_daily_schedule_or_model_generation_path(self):
        self.assertNotRegex(WORKFLOW, r"(?m)^\s*schedule:\s*$")
        forbidden = [
            "GEMINI" + "_API_KEY",
            "OPENAI" + "_API_KEY",
            "generate_" + "daily_lessons",
            "ensure_" + "daily_image",
            "vocabulary_" + "translations.py --budget",
        ]
        for value in forbidden:
            with self.subTest(value=value):
                self.assertNotIn(value, WORKFLOW)

    def test_push_runs_complete_offline_checks_and_hosting_verification(self):
        for required in (
            "python -m unittest discover -s tests -p 'test_*.py'",
            "npm run check:js",
            "node --test tests/*.test.cjs",
            "python audit_site.py",
            "cloudflare/verify-publishing.py",
            "cloudflare/verify-current-lesson.cjs https://englishladder.philstilwell.workers.dev",
            "cloudflare/verify-current-lesson.cjs https://englishladder.com",
        ):
            with self.subTest(required=required):
                self.assertIn(required, WORKFLOW)

    def test_full_offline_suite_has_a_realistic_bounded_deadline(self):
        timeout = int(re.search(
            r"(?ms)^  check_and_verify:.*?^    timeout-minutes: (\d+)$", WORKFLOW
        ).group(1))
        self.assertGreaterEqual(timeout, 60)

    def test_publication_pipelines_preserve_verifier_status_and_logs(self):
        steps = (
            ("Wait for Cloudflare publishing", "publishing-manifest.log"),
            ("Verify current lesson on Cloudflare", "publishing-current-lesson.log"),
            ("Verify current lesson on public domain", "publishing-public-domain.log"),
        )
        bash = shutil.which("bash")
        self.assertIsNotNone(bash, "Publication workflow tests require Bash")
        for name, log_name in steps:
            step = re.search(
                rf"(?m)^      - name: {re.escape(name)}\n((?:        .*\n|\n)+)",
                WORKFLOW,
            ).group(1)
            script = textwrap.dedent(re.search(
                r"(?m)^        run: \|\n((?:          .*\n)+)", step
            ).group(1))
            shell = re.search(r"(?m)^        shell: (.+)$", step)
            # Match GitHub Actions: implicit Bash uses -e; explicit shell: bash
            # also enables pipefail. Removing the workflow fix must fail here.
            command = [bash, "--noprofile", "--norc", "-e"]
            if shell:
                self.assertEqual("bash", shell.group(1))
                command.extend(["-o", "pipefail"])
            for exit_code in (0, 1, 124):
                with self.subTest(step=name, verifier_exit=exit_code), \
                        tempfile.TemporaryDirectory(prefix="publishing checks ") as temp:
                    root = Path(temp)
                    stub_bin = root / "bin"
                    stub_bin.mkdir()
                    # Stub only the verifiers; run the real workflow script and tee.
                    for executable in ("python", "node"):
                        stub = stub_bin / executable
                        stub.write_text(
                            '#!/bin/sh\n'
                            'printf "verifier stdout\\n"\n'
                            'printf "verifier stderr\\n" >&2\n'
                            'exit "$VERIFIER_EXIT_CODE"\n'
                        )
                        stub.chmod(0o755)
                    script_path = root / "step.sh"
                    script_path.write_text(script)
                    result = subprocess.run(
                        [*command, str(script_path)], cwd=root,
                        env={"PATH": f"{stub_bin}{os.pathsep}{os.defpath}",
                             "RUNNER_TEMP": temp, "VERIFIER_EXIT_CODE": str(exit_code)},
                        capture_output=True, text=True, timeout=10,
                    )
                    output = "verifier stdout\nverifier stderr\n"
                    self.assertEqual(output, result.stdout)
                    self.assertEqual("", result.stderr)
                    self.assertEqual(output, (root / log_name).read_text())
                    self.assertEqual(exit_code, result.returncode)

    def test_publication_failures_remain_fatal_and_diagnostics_are_retained(self):
        self.assertNotIn("continue-on-error:", WORKFLOW)
        diagnostics = re.search(
            r"(?m)^      - name: Retain publishing diagnostics\n((?:        .*\n|\n)+)",
            WORKFLOW,
        ).group(1)
        self.assertIn("if: always() && github.event_name == 'push'", diagnostics)
        self.assertIn("${{ runner.temp }}/publishing-*.log", diagnostics)

    def test_manual_workflow_can_only_verify_or_test_email(self):
        inputs = re.search(r"(?ms)^  workflow_dispatch:\n    inputs:\n(.*?)\n\nconcurrency:",
                           WORKFLOW).group(1)
        names = re.findall(r"^      ([a-z_]+):$", inputs, re.M)
        self.assertEqual(["verify_only", "test_email"], names)
        self.assertIn("python daily_publication.py --require-published", WORKFLOW)

    def test_audio_workflow_no_longer_backfills_daily_vocabulary(self):
        audio = (ROOT / ".github/workflows/translate-us-life.yml").read_text()
        self.assertNotIn("include_vocabulary", audio)
        self.assertNotIn("vocabulary_translations.py", audio)
        self.assertNotIn("data/vocabulary-translations", audio)

    def test_repository_skill_is_the_declared_producer(self):
        skill = (ROOT / ".agents/skills/english-ladder-daily-producer/SKILL.md").read_text()
        self.assertIn("plan_daily_runner.py", skill)
        self.assertIn("22:30, 23:30, and 00:30", skill)
        self.assertIn("no paid api fallback", skill.lower())
        self.assertIn("node cloudflare/check-daily-publication.cjs", skill)
        self.assertIn(".venv/bin/python daily_schedule.py --wait-for-start", skill)
        self.assertLess(skill.index("daily_schedule.py --wait-for-start"),
                        skill.index("daily_publication.py --date"))

    def test_desktop_schedule_uses_local_checkout_and_three_idempotent_opportunities(self):
        with (ROOT / "ops/english-ladder-daily.automation.toml").open("rb") as stream:
            automation = tomllib.load(stream)
        self.assertEqual("local", automation["execution_environment"])
        self.assertEqual("gpt-6.1-sol", automation["model"])
        self.assertEqual("high", automation["reasoning_effort"])
        self.assertIn("daily_schedule.py", automation["prompt"])
        self.assertIn("daily_schedule.py --wait-for-start", automation["prompt"])
        self.assertEqual(["/Users/philstilwell/.local/share/EnglishLadder/English-Ladder"],
                         automation["cwds"])
        self.assertEqual(
            "DTSTART;TZID=America/New_York:20261025T223000\n"
            "RRULE:FREQ=DAILY;BYHOUR=0,22,23;BYMINUTE=30;BYSECOND=0",
            automation["rrule"],
        )


if __name__ == "__main__":
    unittest.main()
