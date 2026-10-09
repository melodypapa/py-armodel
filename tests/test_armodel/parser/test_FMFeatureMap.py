"""Parser tests for the FM-FEATURE-MAP element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
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


class TestReadFMFeatureMap:
    def test_read_with_mapping(self):
        element = ET.Element("FM-FEATURE-MAP")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "FeatureMap"
        mappings_tag = ET.SubElement(element, "MAPPINGS")
        map_element = ET.SubElement(mappings_tag, "FM-FEATURE-MAP-ELEMENT")
        ET.SubElement(map_element, "SHORT-NAME").text = "Mapping"

        parent = _parent()
        obj = ARXMLParser().readFMFeatureMap(_round_trip(element), parent.createFMFeatureMap("FeatureMap"))
        assert obj.getShortName() == "FeatureMap"
        assert len(obj.getMappings()) == 1
        assert obj.getMappings()[0].getShortName() == "Mapping"

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("FM-FEATURE-MAP")

        obj = ARXMLParser().readFMFeatureMap(_round_trip(element), parent.createFMFeatureMap("FeatureMap"))
        assert obj.getMappings() == []
