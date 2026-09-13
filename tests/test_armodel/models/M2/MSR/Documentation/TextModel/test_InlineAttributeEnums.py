"""Tests for inline attribute enumerations."""

from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import (
    ResolutionPolicyEnum,
    ShowContentEnum,
    ShowResourceAliasNameEnum,
    ShowResourceCategoryEnum,
    ShowResourceLongNameEnum,
)


class TestResolutionPolicyEnum:
    def test_resolution_policy_literals(self):
        enum = ResolutionPolicyEnum()

        assert enum.validateEnumValue(ResolutionPolicyEnum.NO_SLOPPY)
        assert enum.validateEnumValue(ResolutionPolicyEnum.SLOPPY)
        assert ResolutionPolicyEnum.NO_SLOPPY == "NO-SLOPPY"
        assert ResolutionPolicyEnum.SLOPPY == "SLOPPY"

        enum.setValue(ResolutionPolicyEnum.SLOPPY)
        assert enum.getValue() == "SLOPPY"


class TestShowContentEnum:
    def test_show_content_literals(self):
        enum = ShowContentEnum()

        assert enum.validateEnumValue(ShowContentEnum.NO_SHOW_CONTENT)
        assert enum.validateEnumValue(ShowContentEnum.SHOW_CONTENT)
        assert ShowContentEnum.NO_SHOW_CONTENT == "NO-SHOW-CONTENT"
        assert ShowContentEnum.SHOW_CONTENT == "SHOW-CONTENT"

        enum.setValue(ShowContentEnum.SHOW_CONTENT)
        assert enum.getValue() == "SHOW-CONTENT"


class TestShowResourceAliasNameEnum:
    def test_show_resource_alias_name_literals(self):
        enum = ShowResourceAliasNameEnum()

        assert enum.validateEnumValue(ShowResourceAliasNameEnum.NO_SHOW_ALIAS_NAME)
        assert enum.validateEnumValue(ShowResourceAliasNameEnum.SHOW_ALIAS_NAME)
        assert ShowResourceAliasNameEnum.NO_SHOW_ALIAS_NAME == "NO-SHOW-ALIAS-NAME"
        assert ShowResourceAliasNameEnum.SHOW_ALIAS_NAME == "SHOW-ALIAS-NAME"

        enum.setValue(ShowResourceAliasNameEnum.SHOW_ALIAS_NAME)
        assert enum.getValue() == "SHOW-ALIAS-NAME"


class TestShowResourceCategoryEnum:
    def test_show_resource_category_literals(self):
        enum = ShowResourceCategoryEnum()

        assert enum.validateEnumValue(ShowResourceCategoryEnum.NO_SHOW_CATEGORY)
        assert enum.validateEnumValue(ShowResourceCategoryEnum.SHOW_CATEGORY)
        assert ShowResourceCategoryEnum.NO_SHOW_CATEGORY == "NO-SHOW-CATEGORY"
        assert ShowResourceCategoryEnum.SHOW_CATEGORY == "SHOW-CATEGORY"

        enum.setValue(ShowResourceCategoryEnum.SHOW_CATEGORY)
        assert enum.getValue() == "SHOW-CATEGORY"


class TestShowResourceLongNameEnum:
    def test_show_resource_long_name_literals(self):
        enum = ShowResourceLongNameEnum()

        assert enum.validateEnumValue(ShowResourceLongNameEnum.NO_SHOW_LONG_NAME)
        assert enum.validateEnumValue(ShowResourceLongNameEnum.SHOW_LONG_NAME)
        assert ShowResourceLongNameEnum.NO_SHOW_LONG_NAME == "NO-SHOW-LONG-NAME"
        assert ShowResourceLongNameEnum.SHOW_LONG_NAME == "SHOW-LONG-NAME"

        enum.setValue(ShowResourceLongNameEnum.SHOW_LONG_NAME)
        assert enum.getValue() == "SHOW-LONG-NAME"
