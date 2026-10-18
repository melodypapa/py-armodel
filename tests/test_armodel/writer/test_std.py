"""Writer tests for the Std inline text element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String, UriString
from armodel.models.M2.MSR.Documentation.BlockElements import Url
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Std
from armodel.writer.arxml_writer import ARXMLWriter

STD_MEMBERS = ("SUBTITLE", "STATE", "DATE", "URL", "POSITION")


class TestStdWriter:
    def test_write_std_emits_all_child_elements_in_sequence_order(self):
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
        assert written.attrib == {}
        assert [child.tag for child in written if child.tag in STD_MEMBERS] == ["SUBTITLE", "STATE", "DATE", "URL", "POSITION"]
        assert written.find("SUBTITLE").text == "standard"
        assert written.find("STATE").text == "final"
        assert written.find("DATE").text == "2026-09-12"
        assert written.find("URL").text == "https://example.com/std"
        assert written.find("POSITION").text == "section 1"

    def test_write_std_omits_absent_members(self):
        std = Std(None, "STD")
        std.setState(String().setValue("final"))
        parent = ET.Element("PARENT")

        ARXMLWriter().setStd(parent, "STD", std)

        written = parent.find("STD")
        assert [child.tag for child in written if child.tag in STD_MEMBERS] == ["STATE"]

    def test_write_std_omits_none(self):
        parent = ET.Element("PARENT")

        ARXMLWriter().setStd(parent, "STD", None)

        assert parent.find("STD") is None
