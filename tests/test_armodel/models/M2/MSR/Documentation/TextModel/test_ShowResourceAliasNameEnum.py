"""Tests for the ShowResourceAliasNameEnum inline attribute enumeration."""

from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import ShowResourceAliasNameEnum


class TestShowResourceAliasNameEnum:
    def test_show_resource_alias_name_literals(self):
        enum = ShowResourceAliasNameEnum()

        assert enum.validateEnumValue(ShowResourceAliasNameEnum.NO_SHOW_ALIAS_NAME)
        assert enum.validateEnumValue(ShowResourceAliasNameEnum.SHOW_ALIAS_NAME)
        assert ShowResourceAliasNameEnum.NO_SHOW_ALIAS_NAME == "NO-SHOW-ALIAS-NAME"
        assert ShowResourceAliasNameEnum.SHOW_ALIAS_NAME == "SHOW-ALIAS-NAME"

        enum.setValue(ShowResourceAliasNameEnum.SHOW_ALIAS_NAME)
        assert enum.getValue() == "SHOW-ALIAS-NAME"
