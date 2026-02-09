"""
Common fixtures for V2 model tests.

This file provides reusable fixtures for V2 model testing including:
- AUTOSAR singleton reset
- Temporary file paths
- Common primitive type instances
"""
from pathlib import Path
from typing import Generator

import pytest

from armodel.v2.models import AUTOSAR


@pytest.fixture
def autosar_reset() -> Generator[None, None, None]:
    """
    Reset AUTOSAR singleton before and after each test.

    This ensures tests don't interfere with each other by clearing
    the singleton state.

    Yields:
        None
    """
    AUTOSAR.resetInstance()
    yield
    AUTOSAR.resetInstance()


@pytest.fixture
def temp_file(tmp_path: Path) -> Path:
    """
    Create a temporary file path for ARXML testing.

    Args:
        tmp_path: Pytest's temporary directory fixture

    Returns:
        Path to a temporary file
    """
    return tmp_path / "temp.arxml"


@pytest.fixture
def temp_arxml_file(tmp_path: Path) -> Generator[Path, None, None]:
    """
    Create a temporary ARXML file for testing.

    Args:
        tmp_path: Pytest's temporary directory fixture

    Yields:
        Path to a temporary ARXML file
    """
    arxml_file = tmp_path / "test.arxml"
    yield arxml_file
    # Cleanup happens automatically with tmp_path