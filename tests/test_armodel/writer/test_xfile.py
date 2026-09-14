"""Writer tests for the Xfile inline text element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String, UriString
from armodel.models.M2.MSR.Documentation.BlockElements import Url
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Xfile
from armodel.writer.arxml_writer import ARXMLWriter


class TestXfileWriter:
    def test_write_xfile_emits_children_in_xsd_order(self):
        xfile = Xfile(None, "XFILE")
        xfile.setTool(String().setValue("generator"))
        xfile.setToolVersion(String().setValue("1.2"))
        xfile.setUrl(Url().setValue(UriString().setValue("https://example.com/file")))
        parent = ET.Element("PARENT")

        ARXMLWriter().setXfile(parent, "XFILE", xfile)

        written = parent.find("XFILE")
        assert written is not None
        assert [child.tag for child in written][-3:] == ["URL", "TOOL", "TOOL-VERSION"]
        assert written.find("URL").text == "https://example.com/file"
        assert written.find("TOOL").text == "generator"
        assert written.find("TOOL-VERSION").text == "1.2"

    def test_write_xfile_omits_none(self):
        parent = ET.Element("PARENT")

        ARXMLWriter().setXfile(parent, "XFILE", None)

        assert parent.find("XFILE") is None
