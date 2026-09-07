"""Offline request-failure tests; no API calls or paid generation."""
import copy
import json
import socket
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

import generation_retry as retry


class FakeAPIError(Exception):
    def __init__(self, code, message="private API body and credentials"):
        super().__init__(message)
        self.code = code


class GenerationRetryTests(unittest.TestCase):
    def test_client_timeout_and_sdk_retries_cannot_multiply_our_request_budget(self):
        import update_site
        client_factory = Mock()
        google = SimpleNamespace(genai=SimpleNamespace(Client=client_factory))
        with patch.dict("sys.modules", {"google": google}), \
                patch.dict("os.environ", {"GEMINI_API_KEY": "offline-test-key"}):
            result = update_site.configure_gemini()
        self.assertIs(result, client_factory.return_value)
        client_factory.assert_called_once_with(
            api_key="offline-test-key",
            http_options={"timeout": 180_000, "retry_options": {"attempts": 1}},
        )

    def client(self, *outcomes):
        generate = Mock(side_effect=outcomes)
        return SimpleNamespace(models=SimpleNamespace(generate_content=generate)), generate

    def test_success_preserves_response_and_request(self):
        response = object()
        client, generate = self.client(response)
        sleep = Mock()
        request = {"model": "test-model", "contents": ["lesson prompt"],
                   "config": {"response_mime_type": "application/json"}}
        original = copy.deepcopy(request)
        self.assertIs(response, retry.generate_with_retry(client, _sleep=sleep, **request))
        generate.assert_called_once_with(**original)
        self.assertEqual(original, request)
        sleep.assert_not_called()

    def test_all_selected_http_failures_are_retried_without_exposing_bodies(self):
        for status in (408, 429, 500, 502, 503, 504):
            for code in (status, str(status)):
                with self.subTest(code=code):
                    result = object()
                    client, generate = self.client(FakeAPIError(code), result)
                    sleep = Mock()
                    with self.assertLogs(retry.LOGGER, level="WARNING") as logs:
                        self.assertIs(result, retry.generate_with_retry(client, _sleep=sleep, model="test"))
                    self.assertEqual(2, generate.call_count)
                    sleep.assert_called_once_with(2)
                    self.assertIn(f"HTTP {status}", logs.output[0])
                    self.assertNotIn("private API body", logs.output[0])
                    self.assertNotIn("credentials", logs.output[0])

    def test_stdlib_temporary_connection_and_timeout_failures_recover(self):
        for error in (TimeoutError("private details"), ConnectionResetError("closed"),
                      ConnectionRefusedError("refused"), socket.gaierror(socket.EAI_AGAIN, "temporary")):
            with self.subTest(error=type(error).__name__):
                response = object()
                client, generate = self.client(error, response)
                with patch.object(retry.LOGGER, "warning"):
                    self.assertIs(response, retry.generate_with_retry(client, _sleep=Mock()))
                self.assertEqual(2, generate.call_count)

    def test_permanent_http_and_validation_errors_are_not_retried(self):
        for error in [FakeAPIError(code) for code in (400, 401, 403, 404, 422, 501)] + [
            ValueError("invalid schema"), json.JSONDecodeError("invalid JSON", "", 0),
            socket.gaierror(socket.EAI_NONAME, "unknown host"),
        ]:
            with self.subTest(error=error):
                client, generate = self.client(error, object())
                sleep = Mock()
                with self.assertRaises(type(error)) as caught:
                    retry.generate_with_retry(client, _sleep=sleep)
                self.assertIs(error, caught.exception)
                self.assertEqual(1, generate.call_count)
                sleep.assert_not_called()

    def test_exhaustion_raises_last_exception_after_three_calls_and_bounded_waits(self):
        errors = [TimeoutError("first"), FakeAPIError(503), ConnectionResetError("last")]
        client, generate = self.client(*errors)
        sleep = Mock()
        with patch.object(retry.LOGGER, "warning"), self.assertRaises(ConnectionResetError) as caught:
            retry.generate_with_retry(client, _sleep=sleep, contents="same request")
        self.assertIs(errors[-1], caught.exception)
        self.assertEqual(3, generate.call_count)
        self.assertEqual([2, 4], [call.args[0] for call in sleep.call_args_list])
        self.assertTrue(all(call.kwargs == {"contents": "same request"} for call in generate.call_args_list))

    def test_permanent_failure_after_transient_failure_stops_immediately(self):
        permanent = FakeAPIError(401)
        client, generate = self.client(FakeAPIError(429), permanent, object())
        sleep = Mock()
        with patch.object(retry.LOGGER, "warning"), self.assertRaises(FakeAPIError) as caught:
            retry.generate_with_retry(client, _sleep=sleep)
        self.assertIs(permanent, caught.exception)
        self.assertEqual(2, generate.call_count)
        sleep.assert_called_once_with(2)

    def test_status_code_property_is_recognized(self):
        class StatusError(Exception):
            @property
            def status_code(self):
                return 429
        client, generate = self.client(StatusError(), "okay")
        with patch.object(retry.LOGGER, "warning"):
            self.assertEqual("okay", retry.generate_with_retry(client, _sleep=Mock()))
        self.assertEqual(2, generate.call_count)

    def test_broken_exception_property_does_not_replace_original_failure(self):
        class BrokenStatusError(Exception):
            @property
            def code(self):
                raise ValueError("broken property")
        error = BrokenStatusError("original failure")
        client, generate = self.client(error)
        with self.assertRaises(BrokenStatusError) as caught:
            retry.generate_with_retry(client, _sleep=Mock())
        self.assertIs(error, caught.exception)
        self.assertEqual(1, generate.call_count)

    def test_http_status_on_response_is_recognized(self):
        error = RuntimeError("private response")
        error.response = SimpleNamespace(status_code=502)
        client, generate = self.client(error, "okay")
        with patch.object(retry.LOGGER, "warning"):
            self.assertEqual("okay", retry.generate_with_retry(client, _sleep=Mock()))
        self.assertEqual(2, generate.call_count)

    def test_httpx_network_failures_retry_but_local_configuration_failures_do_not(self):
        if retry.httpx is None:
            self.skipTest("httpx is not installed in this offline environment")
        for error, expected_calls in (
            (retry.httpx.ReadTimeout("timed out"), 2),
            (retry.httpx.ConnectError("could not connect"), 2),
            (retry.httpx.RemoteProtocolError("server disconnected"), 2),
            (retry.httpx.LocalProtocolError("invalid header"), 1),
            (retry.httpx.UnsupportedProtocol("invalid scheme"), 1),
        ):
            with self.subTest(error=type(error).__name__):
                client, generate = self.client(error, "okay")
                with patch.object(retry.LOGGER, "warning"):
                    if expected_calls == 2:
                        self.assertEqual("okay", retry.generate_with_retry(client, _sleep=Mock()))
                    else:
                        with self.assertRaises(type(error)) as caught:
                            retry.generate_with_retry(client, _sleep=Mock())
                        self.assertIs(error, caught.exception)
                self.assertEqual(expected_calls, generate.call_count)


if __name__ == "__main__":
    unittest.main()
