"""
This module contains tests for the enumeration classes in the
AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import (
    AutoCollectEnum,
    BindingTimeEnum,
)


class TestAutoCollectEnum:
    """
    Test class for AutoCollectEnum functionality.
    """

    def test_members(self):
        assert AutoCollectEnum.AUTO_COLLECT_OFF.value == "OFF"
        assert AutoCollectEnum.AUTO_COLLECT_ON.value == "ON"
        assert AutoCollectEnum.AUTO_COLLECT_AUTO.value == "AUTO"


class TestBindingTimeEnum:
    """
    Test class for BindingTimeEnum functionality.
    """

    def test_enum_values(self):
        bt = BindingTimeEnum()
        assert set(bt.getEnumValues()) == {
            "codeGenerationTime",
            "linkTime",
            "preCompileTime",
            "systemDesignTime",
        }
