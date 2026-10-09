"""Parser tests for the IDSM-TRAFFIC-LIMITATION element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import IdsmTrafficLimitation
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


class TestReadIdsmTrafficLimitation:
    def test_read_all_members(self):
        parent = _parent()
        element = ET.Element("IDSM-TRAFFIC-LIMITATION")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "Limitation"
        max_bytes_in_interval_element = ET.SubElement(element, "MAX-BYTES-IN-INTERVAL")
        max_bytes_in_interval_element.text = "1024"
        time_interval_element = ET.SubElement(element, "TIME-INTERVAL")
        time_interval_element.text = "2.5"

        obj = ARXMLParser().readIdsmTrafficLimitation(_round_trip(element), IdsmTrafficLimitation(parent, "Limitation"))
        assert obj.getShortName() == "Limitation"
        assert obj.getMaxBytesInInterval() is not None
        assert obj.getMaxBytesInInterval().getValue() == 1024
        assert obj.getTimeInterval() is not None
        assert obj.getTimeInterval().getValue() == 2.5

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("IDSM-TRAFFIC-LIMITATION")

        obj = ARXMLParser().readIdsmTrafficLimitation(_round_trip(element), IdsmTrafficLimitation(parent, "Limitation"))
        assert obj.getShortName() == "Limitation"
