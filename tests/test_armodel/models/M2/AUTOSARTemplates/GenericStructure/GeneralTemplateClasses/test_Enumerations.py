"""
This module contains tests for the enumeration classes in the
AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import (
    BindingTimeEnum,
    XmlSpaceEnum,
)


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


class TestXmlSpaceEnum:
    """
    Test class for XmlSpaceEnum functionality.
    """

    def test_members(self):
        assert XmlSpaceEnum.DEFAULT == "default"
        assert XmlSpaceEnum.PRESERVE == "preserve"

    def test_enum_values(self):
        enum = XmlSpaceEnum()
        assert set(enum.getEnumValues()) == {"default", "preserve"}

    def test_set_value(self):
        enum = XmlSpaceEnum().setValue(XmlSpaceEnum.PRESERVE)
        assert enum.getValue() == "preserve"
