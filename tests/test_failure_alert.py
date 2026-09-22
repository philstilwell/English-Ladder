"""Checks for useful final-attempt reports and secure, explicit email delivery."""
import contextlib
from datetime import datetime, timezone
import io
import smtplib
import unittest
from unittest.mock import patch
from urllib.error import URLError

import failure_alert as alert


CONTEXT = {'GITHUB_REPOSITORY': 'philstilwell/English-Ladder', 'GITHUB_RUN_ID': '12345',
           'GITHUB_RUN_ATTEMPT': '2', 'MAINTENANCE_RESULT': 'success',
           'GENERATION_RESULT': 'success', 'PUBLISHING_RESULT': 'failure'}
MAIL = {**CONTEXT, 'SMTP_HOST': 'smtp.gmail.com', 'SMTP_USERNAME': 'philstilwell@gmail.com',
        'SMTP_PASSWORD': 'test-only-password', 'ALERT_FROM': 'philstilwell@gmail.com',
        'ALERT_TO': 'philstilwell@gmail.com'}


class FailureAlertTests(unittest.TestCase):
    def test_report_explains_publishing_and_redacts_annotations(self):
        requests = []

        def fetch(path, env):
            requests.append(path)
            if '/jobs?' in path:
                return {'jobs': [
                    {'name': 'Generate and save checked lessons', 'conclusion': 'success'},
                    {'name': 'Verify publishing', 'conclusion': 'failure',
                     'steps': [{'name': 'Wait for Cloudflare publishing', 'conclusion': 'failure'}],
                     'check_run_url': alert.API_ROOT + '/repos/philstilwell/English-Ladder/check-runs/67'}]}
            return [{'annotation_level': 'failure',
                     'message': 'Deployment timed out. token-secret test-only-password\n\x1bMore detail.'}]

        env = {**MAIL, 'GITHUB_TOKEN': 'token-secret'}
        details, warnings = alert.collect_diagnostics(env, fetch)
        subject, body = alert.build_report(env, details, warnings, datetime(2026, 9, 23, 2, tzinfo=timezone.utc))
        self.assertIn('2026-09-22 EST', subject)
        self.assertIn('03:15 fixed EST', body)
        self.assertIn('could not be confirmed on the live website', body)
        self.assertIn('Wait for Cloudflare publishing', body)
        self.assertIn('Deployment timed out.', body)
        self.assertNotIn('token-secret', body)
        self.assertNotIn('test-only-password', body)
        self.assertIn('[redacted]', body)
        self.assertIn('/attempts/2', body)
        self.assertIn('/attempts/2/jobs?', requests[0])
        self.assertEqual(len(requests), 2)

    def test_diagnostics_stay_on_same_repository_and_avoid_logs(self):
        paths = []

        def fetch(path, env):
            paths.append(path)
            return {'jobs': [{'name': 'Cleanup', 'conclusion': 'failure', 'steps': [],
                              'check_run_url': 'https://example.org/check-runs/6'}]}

        details, _ = alert.collect_diagnostics(CONTEXT, fetch)
        self.assertEqual(len(paths), 1)
        self.assertNotIn('logs', paths[0])
        self.assertIn('50-day window', alert.explain_failure(details[0]))

    def test_api_failure_still_produces_useful_alert(self):
        def fetch(*_):
            raise URLError('sensitive credentials must not be copied')

        details, warnings = alert.collect_diagnostics(CONTEXT, fetch)
        _, body = alert.build_report(CONTEXT, details, warnings)
        self.assertIn('Live website verification: failure', body)
        self.assertIn('GitHub could not provide detailed failure information', body)
        self.assertNotIn('sensitive credentials', body)
        self.assertIn('https://github.com/philstilwell/English-Ladder/actions/runs/12345', body)

    def test_diagnostic_notes_are_bounded(self):
        notes = [{'annotation_level': 'failure', 'message': str(i) + 'x' * 1000} for i in range(12)]
        payload = {'jobs': [{'name': 'Checks', 'conclusion': 'failure',
                            'check_run_url': alert.API_ROOT + '/repos/philstilwell/English-Ladder/check-runs/6'}]}
        details, _ = alert.collect_diagnostics(CONTEXT, lambda path, env: payload if '/jobs?' in path else notes)
        self.assertEqual(len(details[0]['annotations']), 3)
        self.assertTrue(all(len(text) <= 501 for text in details[0]['annotations']))

    def test_missing_mail_configuration_fails_without_contacting_github(self):
        with patch.object(alert, 'collect_diagnostics') as diagnostics, contextlib.redirect_stderr(io.StringIO()) as output:
            self.assertEqual(alert.main([], CONTEXT), 1)
        diagnostics.assert_not_called()
        self.assertIn('SMTP_PASSWORD', output.getvalue())
        self.assertIn('not configured', output.getvalue())

    def test_dry_run_requires_no_mail_account_and_does_not_send(self):
        with patch.object(alert, 'collect_diagnostics', return_value=([], [])), \
                patch.object(alert, 'send_report') as send, contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(alert.main(['--dry-run'], CONTEXT), 0)
        send.assert_not_called()
        self.assertIn('final daily attempt failed', output.getvalue())

    def test_test_mode_is_clearly_labeled_and_does_not_collect_failures(self):
        with patch.object(alert, 'collect_diagnostics') as diagnostics, \
                patch.object(alert, 'send_report') as send, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(alert.main(['--test'], {k: v for k, v in MAIL.items() if k not in ('ALERT_FROM', 'ALERT_TO')}), 0)
        diagnostics.assert_not_called()
        env, subject, body = send.call_args.args
        self.assertEqual(env['ALERT_TO'], 'philstilwell@gmail.com')
        self.assertEqual(env['ALERT_FROM'], 'philstilwell@gmail.com')
        self.assertIn('setup test', subject)
        self.assertIn('does not mean a lesson or website update failed', body)

    def test_starttls_happens_before_login_and_sends_expected_recipient(self):
        with patch.object(alert.smtplib, 'SMTP') as factory, patch.object(alert.smtplib, 'SMTP_SSL') as ssl_factory:
            smtp = factory.return_value.__enter__.return_value
            smtp.send_message.return_value = {}
            alert.send_report(MAIL, 'Test subject', 'Test body')
        ssl_factory.assert_not_called()
        self.assertEqual([c[0] for c in smtp.method_calls], ['ehlo', 'starttls', 'ehlo', 'login', 'send_message'])
        message = smtp.send_message.call_args.args[0]
        self.assertEqual(message['To'], 'philstilwell@gmail.com')
        self.assertEqual(message['Message-ID'], '<englishladder-failure-12345-2@englishladder.com>')
        self.assertTrue(smtp.starttls.call_args.kwargs['context'].check_hostname)

    def test_ssl_mail_uses_certificate_verification(self):
        with patch.object(alert.smtplib, 'SMTP_SSL') as factory, patch.object(alert.smtplib, 'SMTP') as clear_factory:
            smtp = factory.return_value.__enter__.return_value
            smtp.send_message.return_value = {}
            alert.send_report({**MAIL, 'SMTP_SECURITY': 'ssl'}, 'Test', 'Body')
        clear_factory.assert_not_called()
        self.assertEqual(factory.call_args.args, ('smtp.gmail.com', 465))
        self.assertTrue(factory.call_args.kwargs['context'].check_hostname)
        smtp.starttls.assert_not_called()

    def test_refused_delivery_is_an_error_without_a_duplicate_retry(self):
        with patch.object(alert.smtplib, 'SMTP') as factory:
            smtp = factory.return_value.__enter__.return_value
            smtp.send_message.return_value = {'philstilwell@gmail.com': (550, b'Rejected')}
            with self.assertRaises(smtplib.SMTPRecipientsRefused):
                alert.send_report(MAIL, 'Test', 'Body')
        self.assertEqual(factory.call_count, 1)
        self.assertEqual(smtp.send_message.call_count, 1)

    def test_plaintext_and_header_injections_rejected(self):
        for replacement in ({'SMTP_SECURITY': 'none'}, {'SMTP_PORT': 'bad'}, {'SMTP_PORT': '65536'},
                            {'SMTP_HOST': 'https://smtp.gmail.com'},
                            {'ALERT_FROM': 'sender@gmail.com\nBcc: stranger@example.com'},
                            {'ALERT_TO': 'philstilwell@gmail.com,stranger@example.com'}):
            with self.subTest(replacement=replacement), self.assertRaises(alert.ConfigurationError):
                alert.mail_settings({**MAIL, **replacement})

    def test_error_output_does_not_reveal_server_message_or_password(self):
        with patch.object(alert, 'send_report', side_effect=smtplib.SMTPAuthenticationError(535, b'test-only-password')), \
                contextlib.redirect_stderr(io.StringIO()) as output:
            self.assertEqual(alert.main(['--test'], MAIL), 1)
        self.assertIn('rejected its login', output.getvalue())
        self.assertNotIn('test-only-password', output.getvalue())

    def test_translation_failure_is_reported_even_when_english_job_succeeds(self):
        payload = {'jobs': [{'name': 'Generate and save checked lessons', 'conclusion': 'success',
                            'steps': [{'name': 'Checkout repository', 'conclusion': 'failure'},
                                      {'name': 'Refresh vocabulary translations', 'conclusion': 'failure'}]}]}
        env = {**CONTEXT, 'GENERATION_RESULT': 'success', 'PUBLISHING_RESULT': 'success',
               'TRANSLATIONS_RESULT': 'failure'}
        details, warnings = alert.collect_diagnostics(env, lambda *_: payload)
        _, body = alert.build_report(env, details, warnings)
        self.assertIn('Vocabulary translations: failure', body)
        self.assertIn('English lessons may already be live', body)
        self.assertIn('Refresh vocabulary translations', body)
        self.assertNotIn('Checkout repository', body)
        self.assertIn('Failed step within job', body)

    def test_image_failure_explains_that_saved_lessons_can_already_be_live(self):
        env = {**CONTEXT, 'PUBLISHING_RESULT': 'success', 'IMAGE_RESULT': 'failure'}
        _, body = alert.build_report(env, [], [])
        self.assertIn('Daily lesson illustration: failure', body)
        self.assertIn('saved English lesson may already be live', body)
        self.assertIn('illustration is still missing or could not be verified', body)

    def test_tls_failure_does_not_fall_back_to_unencrypted_login(self):
        with patch.object(alert.smtplib, 'SMTP') as factory:
            smtp = factory.return_value.__enter__.return_value
            smtp.starttls.side_effect = smtplib.SMTPNotSupportedError('No TLS')
            with self.assertRaises(smtplib.SMTPNotSupportedError):
                alert.send_report(MAIL, 'Test', 'Body')
        smtp.login.assert_not_called()
        smtp.send_message.assert_not_called()

    def test_invalid_run_context_rejected_before_network(self):
        for replacement in ({'GITHUB_REPOSITORY': 'bad\nrepo'}, {'GITHUB_RUN_ID': '../2'}, {'GITHUB_RUN_ATTEMPT': '0'}):
            with self.subTest(replacement=replacement), self.assertRaises(alert.ConfigurationError):
                alert.run_context({**CONTEXT, **replacement})


if __name__ == '__main__':
    unittest.main()
