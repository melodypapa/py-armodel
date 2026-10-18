"""Writer tests for the Xdoc inline text element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String, UriString
from armodel.models.M2.MSR.Documentation.BlockElements import Url
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Xdoc
from armodel.writer.arxml_writer import ARXMLWriter

XDOC_MEMBERS = ("NUMBER", "STATE", "DATE", "PUBLISHER", "URL", "POSITION")


class TestXdocWriter:
    def test_write_xdoc_emits_all_child_elements_in_sequence_order(self):
        xdoc = Xdoc(None, "XDOC")
        xdoc.setDate(DateTime().setValue("2026-09-12"))
        xdoc.setNumber(String().setValue("DOC-1"))
        xdoc.setPosition(String().setValue("section 1"))
        xdoc.setPublisher(String().setValue("Publisher"))
        xdoc.setState(String().setValue("final"))
        xdoc.setUrl(Url().setValue(UriString().setValue("https://example.com/doc")))
        parent = ET.Element("PARENT")

        ARXMLWriter().setXdoc(parent, "XDOC", xdoc)

        written = parent.find("XDOC")
        assert written is not None
        assert written.attrib == {}
        assert [child.tag for child in written if child.tag in XDOC_MEMBERS] == ["NUMBER", "STATE", "DATE", "PUBLISHER", "URL", "POSITION"]
        assert written.find("NUMBER").text == "DOC-1"
        assert written.find("STATE").text == "final"
        assert written.find("DATE").text == "2026-09-12"
        assert written.find("PUBLISHER").text == "Publisher"
        assert written.find("URL").text == "https://example.com/doc"
        assert written.find("POSITION").text == "section 1"

    def test_write_xdoc_omits_absent_members(self):
        xdoc = Xdoc(None, "XDOC")
        xdoc.setPublisher(String().setValue("Publisher"))
        parent = ET.Element("PARENT")

        ARXMLWriter().setXdoc(parent, "XDOC", xdoc)

        written = parent.find("XDOC")
        assert [child.tag for child in written if child.tag in XDOC_MEMBERS] == ["PUBLISHER"]

    def test_write_xdoc_omits_none(self):
        parent = ET.Element("PARENT")

        ARXMLWriter().setXdoc(parent, "XDOC", None)

        assert parent.find("XDOC") is None
