import threading
from contextlib import contextmanager
from typing import Optional

_local = threading.local()


def set_warning_mode(enabled: bool, context: Optional[str] = None) -> None:
    _local.pattern_warning = enabled
    _local.pattern_context = context if enabled else None


def is_warning_mode() -> bool:
    return getattr(_local, "pattern_warning", False)


def get_context() -> Optional[str]:
    return getattr(_local, "pattern_context", None)


@contextmanager
def warning_mode(enabled: bool, context: Optional[str] = None):
    previous_enabled = is_warning_mode()
    previous_context = get_context()
    set_warning_mode(enabled, context)
    try:
        yield
    finally:
        set_warning_mode(previous_enabled, previous_context)
