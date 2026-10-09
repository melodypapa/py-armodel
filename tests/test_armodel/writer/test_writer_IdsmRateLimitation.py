"""Writer tests for the IDSM-RATE-LIMITATION element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import IdsmRateLimitation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Float, PositiveInteger
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteIdsmRateLimitation:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self):
        obj = IdsmRateLimitation(self._parent(), "Limitation")
        value = PositiveInteger()
        value.setValue(5)
        obj.setMaxEventsInInterval(value)
        value = Float()
        value.setValue(1.5)
        obj.setTimeInterval(value)
        return obj

    def test_write_all_members(self):
        obj = self._build_full()

        container = ET.Element("FILTERS")
        ARXMLWriter().writeIdsmRateLimitation(container, obj)
        element = container.find("IDSM-RATE-LIMITATION")

        assert element.find("SHORT-NAME").text == "Limitation"
        assert element.find("MAX-EVENTS-IN-INTERVAL").text == "5"
        assert element.find("TIME-INTERVAL").text == "1.5"

    def test_write_minimal(self):
        obj = IdsmRateLimitation(self._parent(), "Limitation")

        container = ET.Element("FILTERS")
        ARXMLWriter().writeIdsmRateLimitation(container, obj)
        element = container.find("IDSM-RATE-LIMITATION")
        assert element.find("MAX-EVENTS-IN-INTERVAL") is None
        assert element.find("TIME-INTERVAL") is None

    def test_round_trip(self):
        obj = self._build_full()

        container = ET.Element("FILTERS")
        ARXMLWriter().writeIdsmRateLimitation(container, obj)
        element = container.find("IDSM-RATE-LIMITATION")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed = ARXMLParser().readIdsmRateLimitation(parsed_element, IdsmRateLimitation(self._parent(), "Limitation"))
        assert parsed.getShortName() == "Limitation"
        assert parsed.getMaxEventsInInterval().getValue() == 5
        assert parsed.getTimeInterval().getValue() == 1.5
