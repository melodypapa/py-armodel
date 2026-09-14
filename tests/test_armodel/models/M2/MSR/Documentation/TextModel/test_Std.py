"""Tests for the Std inline text element."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String, UriString
from armodel.models.M2.MSR.Documentation.BlockElements import Url
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Std
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData import SingleLanguageLongName


class TestStd:
    def test_std_initialization(self):
        std = Std(None, "STD")

        assert std.getDate() is None
        assert std.getPosition() is None
        assert std.getState() is None
        assert std.getSubtitle() is None
        assert std.getUrl() is None
        assert std.getLongName1() is None

    def test_std_get_set_attributes(self):
        std = Std(None, "STD")
        date = DateTime().setValue("2026-09-12")
        position = String().setValue("section 1")
        state = String().setValue("final")
        subtitle = String().setValue("standard")
        url = Url().setValue(UriString().setValue("https://example.com/std"))

        assert std.setDate(date) is std
        assert std.setPosition(position) is std
        assert std.setState(state) is std
        assert std.setSubtitle(subtitle) is std
        assert std.setUrl(url) is std
        assert std.getDate() is date
        assert std.getPosition() is position
        assert std.getState() is state
        assert std.getSubtitle() is subtitle
        assert std.getUrl() is url

        assert std.setDate(None) is std
        assert std.setPosition(None) is std
        assert std.setState(None) is std
        assert std.setSubtitle(None) is std
        assert std.setUrl(None) is std
        assert std.getDate() is date
        assert std.getPosition() is position
        assert std.getState() is state
        assert std.getSubtitle() is subtitle
        assert std.getUrl() is url

    def test_std_inherited_long_name(self):
        std = Std(None, "STD")
        long_name = SingleLanguageLongName().setValue(String().setValue("Standard"))

        assert std.setLongName1(long_name) is std
        assert std.getLongName1() is long_name
        assert std.setLongName1(None) is std
        assert std.getLongName1() is long_name
