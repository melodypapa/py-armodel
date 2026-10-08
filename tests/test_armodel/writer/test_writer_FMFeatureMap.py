"""Writer tests for the FM-FEATURE-MAP element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import FMFeatureMap
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureMapElement
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMFeatureMap:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_with_mapping(self):
        feature_map = FMFeatureMap(self._parent(), "FeatureMap")
        feature_map.addMapping(FMFeatureMapElement(feature_map, "Mapping"))

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeFMFeatureMap(container, feature_map)
        element = container.find("FM-FEATURE-MAP")

        assert element.find("SHORT-NAME").text == "FeatureMap"
        assert element.find("MAPPINGS/FM-FEATURE-MAP-ELEMENT/SHORT-NAME").text == "Mapping"

    def test_write_minimal(self):
        feature_map = FMFeatureMap(self._parent(), "FeatureMap")

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeFMFeatureMap(container, feature_map)
        element = container.find("FM-FEATURE-MAP")

        assert element.find("MAPPINGS") is None

    def test_round_trip(self):
        feature_map = FMFeatureMap(self._parent(), "FeatureMap")
        feature_map.addMapping(FMFeatureMapElement(feature_map, "Mapping"))

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeFMFeatureMap(container, feature_map)
        element = container.find("FM-FEATURE-MAP")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed_parent = self._parent()
        parsed = ARXMLParser().readFMFeatureMap(parsed_element, parsed_parent.createFMFeatureMap("FeatureMap"))
        assert len(parsed.getMappings()) == 1
        assert parsed.getMappings()[0].getShortName() == "Mapping"
