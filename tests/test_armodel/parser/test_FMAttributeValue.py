"""Parser tests for the FM-ATTRIBUTE-VALUE element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import FMAttributeValue
from armodel.parser.arxml_parser import ARXMLParser


def _parent():
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document.createARPackage("AUTOSAR")


def _round_trip(element: ET.Element) -> ET.Element:
    xml_str = ET.tostring(element).decode()
    xml_str = re.sub(r"^(<[A-Za-z][\w.-]*)", r'\1 xmlns="http://autosar.org/schema/r4.0"', xml_str)
    return ET.fromstring(xml_str)


class TestReadFMAttributeValue:
    def test_read_all_members(self):
        element = ET.Element("FM-ATTRIBUTE-VALUE")
        definition_ref = ET.SubElement(element, "DEFINITION-REF")
        definition_ref.attrib["DEST"] = "FM-ATTRIBUTE-DEF"
        definition_ref.text = "/Pkg/AttrDef"
        value_element = ET.SubElement(element, "VALUE")
        value_element.text = "1.5"

        obj = ARXMLParser().readFMAttributeValue(_round_trip(element), FMAttributeValue())
        assert obj.getDefinitionRef() is not None
        assert obj.getDefinitionRef().getValue() == "/Pkg/AttrDef"
        assert obj.getDefinitionRef().getDest() == "FM-ATTRIBUTE-DEF"
        assert obj.getValue() is not None
        assert obj.getValue().getValue() == 1.5

    def test_read_minimal(self):
        element = ET.Element("FM-ATTRIBUTE-VALUE")

        obj = ARXMLParser().readFMAttributeValue(_round_trip(element), FMAttributeValue())
        assert obj.getDefinitionRef() is None
        assert obj.getValue() is None


class TestFMAttributeValueSTAttributes:
    def test_round_trip_preserves_s_t_attributes(self):
        """The reader/writer must call readARObject/writeARObject (Rule 0025) so the AR-OBJECT
        attributeGroup S/T checksum/timestamp attributes survive a write→parse round-trip."""
        element = ET.Element("FM-ATTRIBUTE-VALUE")
        element.attrib["S"] = "CHECKSUM-1"
        element.attrib["T"] = "2026-10-09T12:00:00+01:00"

        from armodel.writer.arxml_writer import ARXMLWriter

        parsed = ARXMLParser().readFMAttributeValue(_round_trip(element), FMAttributeValue())
        assert parsed.getChecksum() is not None
        assert parsed.getChecksum().getValue() == "CHECKSUM-1"
        assert parsed.getTimestamp() is not None

        out = ET.Element("ATTRIBUTE-VALUES")
        ARXMLWriter().writeFMAttributeValue(out, parsed)
        child = out.find("FM-ATTRIBUTE-VALUE")
        assert child.attrib["S"] == "CHECKSUM-1"
        assert child.attrib["T"] == "2026-10-09T12:00:00+01:00"
