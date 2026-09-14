"""Writer tests for the Std inline text element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String, UriString
from armodel.models.M2.MSR.Documentation.BlockElements import Url
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Std
from armodel.writer.arxml_writer import ARXMLWriter


class TestStdWriter:
    def test_write_std_emits_all_attributes(self):
        std = Std(None, "STD")
        std.setDate(DateTime().setValue("2026-09-12"))
        std.setPosition(String().setValue("section 1"))
        std.setState(String().setValue("final"))
        std.setSubtitle(String().setValue("standard"))
        std.setUrl(Url().setValue(UriString().setValue("https://example.com/std")))
        parent = ET.Element("PARENT")

        ARXMLWriter().setStd(parent, "STD", std)

        written = parent.find("STD")
        assert written is not None
        assert written.attrib == {
            "DATE": "2026-09-12",
            "POSITION": "section 1",
            "STATE": "final",
            "SUBTITLE": "standard",
        }
        assert written.find("URL").text == "https://example.com/std"

    def test_write_std_omits_none(self):
        parent = ET.Element("PARENT")

        ARXMLWriter().setStd(parent, "STD", None)

        assert parent.find("STD") is None
