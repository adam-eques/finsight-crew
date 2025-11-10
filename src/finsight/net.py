"""Retry helper for network calls with exponential backoff."""

from __future__ import annotations

import functools
import time
from typing import Callable, Tuple, Type

from finsight.logging_utils import get_logger

log = get_logger(__name__)


def retry(times: int = 3, base_delay: float = 0.5,
          exceptions: Tuple[Type[Exception], ...] = (Exception,),
          sleep: Callable[[float], None] = time.sleep):
    """Retry the wrapped call up to ``times`` with exponential backoff."""
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            attempt = 0
            while True:
                try:
                    return fn(*args, **kwargs)
                except exceptions as exc:
                    attempt += 1
                    if attempt >= times:
                        raise
                    delay = base_delay * (2 ** (attempt - 1))
                    log.warning("%s failed (%s); retry %d in %.1fs",
                                fn.__name__, exc, attempt, delay)
                    sleep(delay)
        return wrapper
    return decorator
