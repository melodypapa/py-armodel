"""Tests for inline attribute enumerations."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum
from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import (
    ResolutionPolicyEnum,
    ShowContentEnum,
    ShowResourceAliasNameEnum,
    ShowResourceCategoryEnum,
    ShowResourceLongNameEnum,
    ShowResourceNumberEnum,
)


class TestResolutionPolicyEnum:
    def test_initialization_and_values(self):
        enum = ResolutionPolicyEnum()

        assert isinstance(enum, AREnum)
        assert set(enum.getEnumValues()) == {ResolutionPolicyEnum.NO_SLOPPY, ResolutionPolicyEnum.SLOPPY}

    def test_resolution_policy_literals(self):
        enum = ResolutionPolicyEnum()

        assert enum.validateEnumValue(ResolutionPolicyEnum.NO_SLOPPY)
        assert enum.validateEnumValue(ResolutionPolicyEnum.SLOPPY)
        assert ResolutionPolicyEnum.NO_SLOPPY == "NO-SLOPPY"
        assert ResolutionPolicyEnum.SLOPPY == "SLOPPY"

        enum.setValue(ResolutionPolicyEnum.SLOPPY)
        assert enum.getValue() == "SLOPPY"
        assert enum.validateEnumValue("INVALID") is False


class TestShowContentEnum:
    def test_initialization_and_values(self):
        enum = ShowContentEnum()

        assert isinstance(enum, AREnum)
        assert set(enum.getEnumValues()) == {ShowContentEnum.NO_SHOW_CONTENT, ShowContentEnum.SHOW_CONTENT}

    def test_show_content_literals(self):
        enum = ShowContentEnum()

        assert enum.validateEnumValue(ShowContentEnum.NO_SHOW_CONTENT)
        assert enum.validateEnumValue(ShowContentEnum.SHOW_CONTENT)
        assert ShowContentEnum.NO_SHOW_CONTENT == "NO-SHOW-CONTENT"
        assert ShowContentEnum.SHOW_CONTENT == "SHOW-CONTENT"

        assert enum.setValue(ShowContentEnum.SHOW_CONTENT) is enum
        assert enum.getValue() == "SHOW-CONTENT"
        assert enum.validateEnumValue("INVALID") is False


class TestShowResourceAliasNameEnum:
    def test_initialization_and_values(self):
        enum = ShowResourceAliasNameEnum()

        assert isinstance(enum, AREnum)
        assert set(enum.getEnumValues()) == {
            ShowResourceAliasNameEnum.NO_SHOW_ALIAS_NAME,
            ShowResourceAliasNameEnum.SHOW_ALIAS_NAME,
        }

    def test_show_resource_alias_name_literals(self):
        enum = ShowResourceAliasNameEnum()

        assert enum.validateEnumValue(ShowResourceAliasNameEnum.NO_SHOW_ALIAS_NAME)
        assert enum.validateEnumValue(ShowResourceAliasNameEnum.SHOW_ALIAS_NAME)
        assert ShowResourceAliasNameEnum.NO_SHOW_ALIAS_NAME == "NO-SHOW-ALIAS-NAME"
        assert ShowResourceAliasNameEnum.SHOW_ALIAS_NAME == "SHOW-ALIAS-NAME"

        assert enum.setValue(ShowResourceAliasNameEnum.SHOW_ALIAS_NAME) is enum
        assert enum.getValue() == "SHOW-ALIAS-NAME"
        assert enum.validateEnumValue("INVALID") is False


class TestShowResourceCategoryEnum:
    def test_initialization_and_values(self):
        enum = ShowResourceCategoryEnum()

        assert isinstance(enum, AREnum)
        assert set(enum.getEnumValues()) == {ShowResourceCategoryEnum.NO_SHOW_CATEGORY, ShowResourceCategoryEnum.SHOW_CATEGORY}

    def test_show_resource_category_literals(self):
        enum = ShowResourceCategoryEnum()

        assert enum.validateEnumValue(ShowResourceCategoryEnum.NO_SHOW_CATEGORY)
        assert enum.validateEnumValue(ShowResourceCategoryEnum.SHOW_CATEGORY)
        assert ShowResourceCategoryEnum.NO_SHOW_CATEGORY == "NO-SHOW-CATEGORY"
        assert ShowResourceCategoryEnum.SHOW_CATEGORY == "SHOW-CATEGORY"

        assert enum.setValue(ShowResourceCategoryEnum.SHOW_CATEGORY) is enum
        assert enum.getValue() == "SHOW-CATEGORY"
        assert enum.validateEnumValue("INVALID") is False


class TestShowResourceLongNameEnum:
    def test_initialization_and_values(self):
        enum = ShowResourceLongNameEnum()

        assert isinstance(enum, AREnum)
        assert set(enum.getEnumValues()) == {ShowResourceLongNameEnum.NO_SHOW_LONG_NAME, ShowResourceLongNameEnum.SHOW_LONG_NAME}

    def test_show_resource_long_name_literals(self):
        enum = ShowResourceLongNameEnum()

        assert enum.validateEnumValue(ShowResourceLongNameEnum.NO_SHOW_LONG_NAME)
        assert enum.validateEnumValue(ShowResourceLongNameEnum.SHOW_LONG_NAME)
        assert ShowResourceLongNameEnum.NO_SHOW_LONG_NAME == "NO-SHOW-LONG-NAME"
        assert ShowResourceLongNameEnum.SHOW_LONG_NAME == "SHOW-LONG-NAME"

        assert enum.setValue(ShowResourceLongNameEnum.SHOW_LONG_NAME) is enum
        assert enum.getValue() == "SHOW-LONG-NAME"
        assert enum.validateEnumValue("INVALID") is False


class TestShowResourceNumberEnum:
    def test_initialization_and_values(self):
        enum = ShowResourceNumberEnum()

        assert isinstance(enum, AREnum)
        assert set(enum.getEnumValues()) == {ShowResourceNumberEnum.NO_SHOW_NUMBER, ShowResourceNumberEnum.SHOW_NUMBER}

    def test_show_resource_number_literals(self):
        enum = ShowResourceNumberEnum()

        assert enum.validateEnumValue(ShowResourceNumberEnum.NO_SHOW_NUMBER)
        assert enum.validateEnumValue(ShowResourceNumberEnum.SHOW_NUMBER)
        assert ShowResourceNumberEnum.NO_SHOW_NUMBER == "NO-SHOW-NUMBER"
        assert ShowResourceNumberEnum.SHOW_NUMBER == "SHOW-NUMBER"

        assert enum.setValue(ShowResourceNumberEnum.SHOW_NUMBER) is enum
        assert enum.getValue() == "SHOW-NUMBER"
        assert enum.validateEnumValue("INVALID") is False
