"""Tests for the ShowResourceCategoryEnum inline attribute enumeration."""

from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import ShowResourceCategoryEnum


class TestShowResourceCategoryEnum:
    def test_show_resource_category_literals(self):
        enum = ShowResourceCategoryEnum()

        assert enum.validateEnumValue(ShowResourceCategoryEnum.NO_SHOW_CATEGORY)
        assert enum.validateEnumValue(ShowResourceCategoryEnum.SHOW_CATEGORY)
        assert ShowResourceCategoryEnum.NO_SHOW_CATEGORY == "NO-SHOW-CATEGORY"
        assert ShowResourceCategoryEnum.SHOW_CATEGORY == "SHOW-CATEGORY"

        enum.setValue(ShowResourceCategoryEnum.SHOW_CATEGORY)
        assert enum.getValue() == "SHOW-CATEGORY"
