"""Writer tests for the FM-COND element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndAttributes
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureMapCondition
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMFeatureMapCondition:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_with_formula(self):
        obj = FMFeatureMapCondition(self._parent(), "MapElement")
        formula = FMConditionByFeaturesAndAttributes()
        formula.setMixedString("feature == true")
        obj.setFmCond(formula)

        container = ET.Element("CONDITIONS")
        ARXMLWriter().writeFMFeatureMapCondition(container, obj)
        element = container.find("FM-FEATURE-MAP-CONDITION")

        assert element.find("SHORT-NAME").text == "MapElement"
        assert element.find("FM-COND").text == "feature == true"

    def test_write_minimal(self):
        obj = FMFeatureMapCondition(self._parent(), "MapElement")

        container = ET.Element("CONDITIONS")
        ARXMLWriter().writeFMFeatureMapCondition(container, obj)
        element = container.find("FM-FEATURE-MAP-CONDITION")

        assert element.find("FM-COND") is None

    def test_round_trip(self):
        obj = FMFeatureMapCondition(self._parent(), "MapElement")
        formula = FMConditionByFeaturesAndAttributes()
        formula.setMixedString("feature == true")
        obj.setFmCond(formula)

        container = ET.Element("CONDITIONS")
        ARXMLWriter().writeFMFeatureMapCondition(container, obj)
        element = container.find("FM-FEATURE-MAP-CONDITION")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed = ARXMLParser().readFMFeatureMapCondition(parsed_element, FMFeatureMapCondition(self._parent(), "MapElement"))
        assert parsed.getFmCond() is not None
        assert parsed.getFmCond().getMixedString() == "feature == true"
