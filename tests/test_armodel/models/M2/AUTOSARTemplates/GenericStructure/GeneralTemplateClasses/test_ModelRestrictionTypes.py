"""
Tests for the ModelRestrictionTypes module (FullBindingTimeEnum).
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import (
    FullBindingTimeEnum,
)


class TestFullBindingTimeEnum:
    """
    Test class for FullBindingTimeEnum functionality (Table 4.39).
    """

    def test_initialization(self):
        enum = FullBindingTimeEnum()
        assert enum is not None
        assert enum._value is None

    def test_literal_members(self):
        assert FullBindingTimeEnum.BLUEPRINT_DERIVATION_TIME == "BLUEPRINT-DERIVATION-TIME"
        assert FullBindingTimeEnum.SYSTEM_DESIGN_TIME == "SYSTEM-DESIGN-TIME"
        assert FullBindingTimeEnum.CODE_GENERATION_TIME == "CODE-GENERATION-TIME"
        assert FullBindingTimeEnum.PRE_COMPILE_TIME == "PRE-COMPILE-TIME"
        assert FullBindingTimeEnum.LINK_TIME == "LINK-TIME"
        assert FullBindingTimeEnum.POST_BUILD == "POST-BUILD"

    def test_enum_values(self):
        enum = FullBindingTimeEnum()
        assert list(enum.getEnumValues()) == [
            "BLUEPRINT-DERIVATION-TIME",
            "SYSTEM-DESIGN-TIME",
            "CODE-GENERATION-TIME",
            "PRE-COMPILE-TIME",
            "LINK-TIME",
            "POST-BUILD",
        ]

    def test_set_value(self):
        enum = FullBindingTimeEnum().setValue(FullBindingTimeEnum.POST_BUILD)
        assert enum.getValue() == "POST-BUILD"
