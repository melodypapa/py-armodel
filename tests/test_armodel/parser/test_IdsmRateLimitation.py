"""Parser tests for the IDSM-RATE-LIMITATION element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import IdsmRateLimitation
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


class TestReadIdsmRateLimitation:
    def test_read_all_members(self):
        parent = _parent()
        element = ET.Element("IDSM-RATE-LIMITATION")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "Limitation"
        max_events_in_interval_element = ET.SubElement(element, "MAX-EVENTS-IN-INTERVAL")
        max_events_in_interval_element.text = "5"
        time_interval_element = ET.SubElement(element, "TIME-INTERVAL")
        time_interval_element.text = "1.5"

        obj = ARXMLParser().readIdsmRateLimitation(_round_trip(element), IdsmRateLimitation(parent, "Limitation"))
        assert obj.getShortName() == "Limitation"
        assert obj.getMaxEventsInInterval() is not None
        assert obj.getMaxEventsInInterval().getValue() == 5
        assert obj.getTimeInterval() is not None
        assert obj.getTimeInterval().getValue() == 1.5

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("IDSM-RATE-LIMITATION")

        obj = ARXMLParser().readIdsmRateLimitation(_round_trip(element), IdsmRateLimitation(parent, "Limitation"))
        assert obj.getShortName() == "Limitation"
