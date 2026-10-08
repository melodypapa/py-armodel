"""Parser tests for the FM-ATTRIBUTE-DEF element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMAttributeDef
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


class TestReadFMAttributeDef:
    def test_read_all_members(self):
        parent = _parent()
        element = ET.Element("FM-ATTRIBUTE-DEF")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "AttrDef"
        default_value = ET.SubElement(element, "DEFAULT-VALUE")
        default_value.text = "1.5"
        max_element = ET.SubElement(element, "MAX")
        max_element.text = "10"
        min_element = ET.SubElement(element, "MIN")
        min_element.text = "1"

        obj = ARXMLParser().readFMAttributeDef(_round_trip(element), FMAttributeDef(parent, "AttrDef"))
        assert obj.getShortName() == "AttrDef"
        assert obj.getDefaultValue() is not None
        assert obj.getDefaultValue().getValue() == 1.5
        assert obj.getMax() is not None
        assert obj.getMax().getValue() == "10"
        assert obj.getMin() is not None
        assert obj.getMin().getValue() == "1"

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("FM-ATTRIBUTE-DEF")

        obj = ARXMLParser().readFMAttributeDef(_round_trip(element), FMAttributeDef(parent, "AttrDef"))
        assert obj.getDefaultValue() is None
        assert obj.getMax() is None
        assert obj.getMin() is None


class TestFMAttributeDefSTAttributes:
    def test_round_trip_preserves_s_t_attributes(self):
        """The reader/writer must call the base helpers (Rule 0025) so the AR-OBJECT
        attributeGroup S/T checksum/timestamp attributes survive a write→parse round-trip."""
        parent = _parent()
        element = ET.Element("FM-ATTRIBUTE-DEF")
        element.attrib["S"] = "CHECKSUM-1"
        element.attrib["T"] = "2026-10-09T12:00:00+01:00"

        from armodel.writer.arxml_writer import ARXMLWriter

        parsed = ARXMLParser().readFMAttributeDef(_round_trip(element), FMAttributeDef(parent, "AttrDef"))
        assert parsed.getChecksum() is not None
        assert parsed.getChecksum().getValue() == "CHECKSUM-1"
        assert parsed.getTimestamp() is not None

        container = ET.Element("ATTRIBUTE-DEFS")
        ARXMLWriter().writeFMAttributeDef(container, parsed)
        child = container.find("FM-ATTRIBUTE-DEF")
        assert child.attrib["S"] == "CHECKSUM-1"
        assert child.attrib["T"] == "2026-10-09T12:00:00+01:00"
