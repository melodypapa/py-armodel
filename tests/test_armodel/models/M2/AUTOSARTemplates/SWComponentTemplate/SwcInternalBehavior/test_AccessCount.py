"""
This module contains comprehensive tests for the AccessCount module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the AccessCount.py file to achieve 100% test coverage.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import (
    AbstractAccessPoint,
)


class TestAbstractAccessPoint:
    """Test class for AbstractAccessPoint abstract class."""

    def test_abstract_access_point_initialization(self):
        """Test AbstractAccessPoint initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            AbstractAccessPoint(ar_root, "TestAbstractAccessPoint")
