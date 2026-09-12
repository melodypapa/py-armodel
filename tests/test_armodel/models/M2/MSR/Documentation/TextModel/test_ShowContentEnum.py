"""Tests for the ShowContentEnum inline attribute enumeration."""

from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import ShowContentEnum


class TestShowContentEnum:
    def test_show_content_literals(self):
        enum = ShowContentEnum()

        assert enum.validateEnumValue(ShowContentEnum.NO_SHOW_CONTENT)
        assert enum.validateEnumValue(ShowContentEnum.SHOW_CONTENT)
        assert ShowContentEnum.NO_SHOW_CONTENT == "NO-SHOW-CONTENT"
        assert ShowContentEnum.SHOW_CONTENT == "SHOW-CONTENT"

        enum.setValue(ShowContentEnum.SHOW_CONTENT)
        assert enum.getValue() == "SHOW-CONTENT"
