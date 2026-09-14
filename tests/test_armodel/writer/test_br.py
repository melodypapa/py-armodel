"""Writer tests for the Br inline text element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Br
from armodel.writer.arxml_writer import ARXMLWriter


class TestBrWriter:
    def test_write_br_emits_element_and_ar_object_attributes(self):
        br = Br()
        br.setChecksum(String().setValue("checksum"))
        br.setTimestamp(DateTime().setValue("timestamp"))
        element = ET.Element("PARENT")

        ARXMLWriter().setBr(element, "BR", br)

        written = element.find("BR")
        assert written is not None
        assert written.attrib == {"S": "checksum", "T": "timestamp"}

    def test_write_br_omits_none(self):
        element = ET.Element("PARENT")

        ARXMLWriter().setBr(element, "BR", None)

        assert element.find("BR") is None
