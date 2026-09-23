"""
This module contains tests for the enumeration classes in the
AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import (
    BindingTimeEnum,
    XmlSpaceEnum,
)


class TestBindingTimeEnum:
    """Test cases for BindingTimeEnum (Table E.8, p.972)."""

    def test_class_note_docstring_verbatim(self):
        """Spec Note per Table E.8, verbatim."""
        assert BindingTimeEnum.__doc__.strip() == ("This enumerator specifies the applicable binding times for the pre build variation points.")

    def test_init_has_no_docstring(self):
        assert BindingTimeEnum.__init__.__doc__ is None

    def test_enum_members(self):
        """Spec literals per Table E.8 (idx0-3); member values are the camelCase mmt.qualifiedName literals."""
        assert BindingTimeEnum.CODE_GENERATION_TIME == "codeGenerationTime"
        assert BindingTimeEnum.LINK_TIME == "linkTime"
        assert BindingTimeEnum.PRE_COMPILE_TIME == "preCompileTime"
        assert BindingTimeEnum.SYSTEM_DESIGN_TIME == "systemDesignTime"

    def test_enum_values_displayed_order(self):
        e = BindingTimeEnum()
        assert list(e.getEnumValues()) == [
            "codeGenerationTime",
            "linkTime",
            "preCompileTime",
            "systemDesignTime",
        ]

    def test_instantiability(self):
        e = BindingTimeEnum()
        e.setValue(BindingTimeEnum.CODE_GENERATION_TIME)
        assert e.getValue() == "codeGenerationTime"
        assert e.getText() == "codeGenerationTime"
        e2 = BindingTimeEnum().setValue(BindingTimeEnum.SYSTEM_DESIGN_TIME)
        assert e2.getValue() == "systemDesignTime"
        assert e2.getText() == "systemDesignTime"

    def test_validate_enum_value(self):
        e = BindingTimeEnum()
        assert e.validateEnumValue("codeGenerationTime") is True
        assert e.validateEnumValue("systemDesignTime") is True
        assert e.validateEnumValue("CODE-GENERATION-TIME") is False
        assert e.validateEnumValue("bogus") is False


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
