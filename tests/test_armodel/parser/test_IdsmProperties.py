"""Parser tests for the IDSM-PROPERTIES element."""

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


class TestReadIdsmProperties:
    def test_read_all_members(self):
        element = ET.Element("IDSM-PROPERTIES")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "IdsmProperties"
        rate_tag = ET.SubElement(element, "RATE-LIMITATION-FILTERS")
        rate = ET.SubElement(rate_tag, "IDSM-RATE-LIMITATION")
        ET.SubElement(rate, "SHORT-NAME").text = "Rate"
        traffic_tag = ET.SubElement(element, "TRAFFIC-LIMITATION-FILTERS")
        traffic = ET.SubElement(traffic_tag, "IDSM-TRAFFIC-LIMITATION")
        ET.SubElement(traffic, "SHORT-NAME").text = "Traffic"

        parent = _parent()
        obj = ARXMLParser().readIdsmProperties(_round_trip(element), parent.createIdsmProperties("IdsmProperties"))
        assert obj.getShortName() == "IdsmProperties"
        assert len(obj.getRateLimitationFilters()) == 1
        assert obj.getRateLimitationFilters()[0].getShortName() == "Rate"
        assert len(obj.getTrafficLimitationFilters()) == 1
        assert obj.getTrafficLimitationFilters()[0].getShortName() == "Traffic"

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("IDSM-PROPERTIES")

        obj = ARXMLParser().readIdsmProperties(_round_trip(element), parent.createIdsmProperties("IdsmProperties"))
        assert obj.getRateLimitationFilters() == []
        assert obj.getTrafficLimitationFilters() == []
