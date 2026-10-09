"""Writer tests for the IDSM-PROPERTIES element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import IdsmProperties
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import IdsmRateLimitation, IdsmTrafficLimitation
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteIdsmProperties:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _build_full(self):
        idsm_properties = IdsmProperties(self._parent(), "IdsmProperties")
        idsm_properties.addRateLimitationFilter(IdsmRateLimitation(idsm_properties, "Rate"))
        idsm_properties.addTrafficLimitationFilter(IdsmTrafficLimitation(idsm_properties, "Traffic"))
        return idsm_properties

    def test_write_all_members(self):
        idsm_properties = self._build_full()

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeIdsmProperties(container, idsm_properties)
        element = container.find("IDSM-PROPERTIES")

        assert element.find("SHORT-NAME").text == "IdsmProperties"
        assert element.find("RATE-LIMITATION-FILTERS/IDSM-RATE-LIMITATION/SHORT-NAME").text == "Rate"
        assert element.find("TRAFFIC-LIMITATION-FILTERS/IDSM-TRAFFIC-LIMITATION/SHORT-NAME").text == "Traffic"

    def test_write_minimal(self):
        idsm_properties = IdsmProperties(self._parent(), "IdsmProperties")

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeIdsmProperties(container, idsm_properties)
        element = container.find("IDSM-PROPERTIES")

        assert element.find("RATE-LIMITATION-FILTERS") is None
        assert element.find("TRAFFIC-LIMITATION-FILTERS") is None

    def test_round_trip(self):
        idsm_properties = self._build_full()

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeIdsmProperties(container, idsm_properties)
        element = container.find("IDSM-PROPERTIES")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed_parent = self._parent()
        parsed = ARXMLParser().readIdsmProperties(parsed_element, parsed_parent.createIdsmProperties("IdsmProperties"))
        assert len(parsed.getRateLimitationFilters()) == 1
        assert parsed.getRateLimitationFilters()[0].getShortName() == "Rate"
        assert len(parsed.getTrafficLimitationFilters()) == 1
        assert parsed.getTrafficLimitationFilters()[0].getShortName() == "Traffic"
