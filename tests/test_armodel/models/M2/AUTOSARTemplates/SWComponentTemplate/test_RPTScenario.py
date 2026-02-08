"""
This module contains comprehensive tests for the RPTScenario module in SWComponentTemplate.
Tests cover all classes and methods in the RPTScenario.py file to achieve 100% test coverage.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import (
    IdentCaption,
    ModeAccessPointIdent,
)


class TestIdentCaption:
    """Test class for IdentCaption abstract class."""

    def test_ident_caption_abstract(self):
        """Test that IdentCaption is an abstract class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            IdentCaption(ar_root, "TestIdentCaption")


class TestModeAccessPointIdent:
    """Test class for ModeAccessPointIdent class."""

    def test_mode_access_point_ident_initialization(self):
        """Test ModeAccessPointIdent initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        mode_access_point_ident = ModeAccessPointIdent(ar_root, "TestModeAccessPointIdent")

        assert mode_access_point_ident.parent == ar_root
        assert mode_access_point_ident.short_name == "TestModeAccessPointIdent"
