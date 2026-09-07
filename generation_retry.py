"""Retry temporary Gemini request failures without retrying invalid lesson content.

This wrapper only surrounds the provider request. Parsing, editorial review, and
curriculum validation remain the caller's responsibility and are never retried
here. Each call makes at most three provider requests, with two bounded waits.
"""
from __future__ import annotations

import logging
import socket
import time
from collections.abc import Callable
from typing import Any

try:
    import httpx
except ImportError:  # Offline checks do not need the optional provider runtime.
    httpx = None

LOGGER = logging.getLogger(__name__)
RETRY_DELAYS = (2, 4)
TRANSIENT_HTTP_STATUSES = frozenset({408, 429, 500, 502, 503, 504})


def _attribute(owner: Any, name: str) -> Any:
    try:
        return getattr(owner, name, None)
    except Exception:
        # A malformed third-party exception property must not hide the original
        # provider exception that the caller needs to diagnose the failure.
        return None


def _status_code(error: Exception) -> int | None:
    """Read status attributes only; never inspect or log a response body."""
    for owner, names in ((error, ("code", "status_code")),
                         (_attribute(error, "response"), ("status_code",))):
        if owner is None:
            continue
        for name in names:
            value = _attribute(owner, name)
            if isinstance(value, bool):
                continue
            if isinstance(value, int) and 100 <= value <= 599:
                return value
            if isinstance(value, str) and value.isascii() and value.isdecimal():
                code = int(value)
                if 100 <= code <= 599:
                    return code
    return None


def _is_transient(error: Exception, status: int | None) -> bool:
    if status is not None:
        return status in TRANSIENT_HTTP_STATUSES
    if isinstance(error, (TimeoutError, ConnectionError)):
        return True
    if isinstance(error, socket.gaierror):
        # Retry a temporary resolver outage, not an invalid/nonexistent hostname.
        return error.errno == socket.EAI_AGAIN
    if httpx is not None and isinstance(
        error, (httpx.TimeoutException, httpx.NetworkError, httpx.RemoteProtocolError)
    ):
        return True
    return False


def generate_with_retry(client: Any, *, _sleep: Callable[[float], None] | None = None,
                        **request: Any) -> Any:
    """Return the provider response unchanged, or raise its final exception.

    ``_sleep`` allows offline tests to exercise retry delays without waiting.
    The request itself is passed through without adding or changing fields.
    """
    sleep = time.sleep if _sleep is None else _sleep
    for attempt in range(len(RETRY_DELAYS) + 1):
        try:
            return client.models.generate_content(**request)
        except Exception as error:
            status = _status_code(error)
            if attempt == len(RETRY_DELAYS) or not _is_transient(error, status):
                raise
            delay = RETRY_DELAYS[attempt]
            # Provider exceptions may contain prompts, credentials, or response
            # bodies. Log only their class name and numerical HTTP status.
            LOGGER.warning(
                "Temporary generation request failure (%s, HTTP %s); "
                "retrying in %ss (request %s of %s).",
                type(error).__name__, status if status is not None else "unavailable",
                delay, attempt + 2, len(RETRY_DELAYS) + 1,
            )
            sleep(delay)
