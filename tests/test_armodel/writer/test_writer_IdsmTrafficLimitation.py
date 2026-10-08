"""Writer tests for the IDSM-TRAFFIC-LIMITATION element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import IdsmTrafficLimitation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, Float
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteIdsmTrafficLimitation:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self):
        obj = IdsmTrafficLimitation(self._parent(), "Limitation")
        value = PositiveInteger()
        value.setValue(1024)
        obj.setMaxBytesInInterval(value)
        value = Float()
        value.setValue(2.5)
        obj.setTimeInterval(value)
        return obj

    def test_write_all_members(self):
        obj = self._build_full()

        container = ET.Element("FILTERS")
        ARXMLWriter().writeIdsmTrafficLimitation(container, obj)
        element = container.find("IDSM-TRAFFIC-LIMITATION")

        assert element.find("SHORT-NAME").text == "Limitation"
        assert element.find("MAX-BYTES-IN-INTERVAL").text == "1024"
        assert element.find("TIME-INTERVAL").text == "2.5"

    def test_write_minimal(self):
        obj = IdsmTrafficLimitation(self._parent(), "Limitation")

        container = ET.Element("FILTERS")
        ARXMLWriter().writeIdsmTrafficLimitation(container, obj)
        element = container.find("IDSM-TRAFFIC-LIMITATION")
        assert element.find("MAX-BYTES-IN-INTERVAL") is None
        assert element.find("TIME-INTERVAL") is None

    def test_round_trip(self):
        obj = self._build_full()

        container = ET.Element("FILTERS")
        ARXMLWriter().writeIdsmTrafficLimitation(container, obj)
        element = container.find("IDSM-TRAFFIC-LIMITATION")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed = ARXMLParser().readIdsmTrafficLimitation(parsed_element, IdsmTrafficLimitation(self._parent(), "Limitation"))
        assert parsed.getShortName() == "Limitation"
        assert parsed.getMaxBytesInInterval().getValue() == 1024
        assert parsed.getTimeInterval().getValue() == 2.5
