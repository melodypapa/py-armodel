"""Shared fixtures for parser tests.

These were previously duplicated across the `*_gaps.py` test files and several
of the per-topic handler test modules. They are centralised here so that every
parser test benefits from a consistent AUTOSAR singleton lifecycle.

Note: ``setARRelease("R23-11")`` is part of the reset fixture because CLAUDE.md
mandates calling ``setARRelease`` before parsing/writing, and several gap test
files already depended on the R23-11 schema being active.

Helper functions (``_snip``, ``_autosar_root``) live in ``_helpers.py``.
"""
import pytest

from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test and pin the R23-11 release."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Fresh ARXMLParser instance running in strict mode."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


@pytest.fixture
def warning_parser():
    """ARXMLParser configured in warning mode (logs instead of raising)."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser(options={"warning": True})
