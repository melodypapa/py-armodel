"""Writer tests for the Xdoc inline text element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String, UriString
from armodel.models.M2.MSR.Documentation.BlockElements import Url
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Xdoc
from armodel.writer.arxml_writer import ARXMLWriter


class TestXdocWriter:
    def test_write_xdoc_emits_all_attributes(self):
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
        assert written.attrib == {
            "DATE": "2026-09-12",
            "NUMBER": "DOC-1",
            "POSITION": "section 1",
            "PUBLISHER": "Publisher",
            "STATE": "final",
        }
        assert written.find("URL").text == "https://example.com/doc"

    def test_write_xdoc_omits_none(self):
        parent = ET.Element("PARENT")

        ARXMLWriter().setXdoc(parent, "XDOC", None)

        assert parent.find("XDOC") is None
