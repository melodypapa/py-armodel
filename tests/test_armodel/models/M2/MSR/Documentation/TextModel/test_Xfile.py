"""Tests for the Xfile inline text element."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String, UriString
from armodel.models.M2.MSR.Documentation.BlockElements import Url
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Xfile


class TestXfile:
    def test_xfile_initialization(self):
        xfile = Xfile(None, "XFILE")

        assert xfile.getTool() is None
        assert xfile.getToolVersion() is None
        assert xfile.getUrl() is None
        assert xfile.getLongName1() is None

    def test_xfile_get_set_attributes(self):
        xfile = Xfile(None, "XFILE")
        tool = String().setValue("generator")
        tool_version = String().setValue("1.2")
        url = Url().setValue(UriString().setValue("https://example.com/file"))

        assert xfile.setTool(tool) is xfile
        assert xfile.setToolVersion(tool_version) is xfile
        assert xfile.setUrl(url) is xfile
        assert xfile.getTool() is tool
        assert xfile.getToolVersion() is tool_version
        assert xfile.getUrl() is url

        assert xfile.setTool(None) is xfile
        assert xfile.setToolVersion(None) is xfile
        assert xfile.setUrl(None) is xfile
        assert xfile.getTool() is tool
        assert xfile.getToolVersion() is tool_version
        assert xfile.getUrl() is url
