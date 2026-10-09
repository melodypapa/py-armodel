"""Writer tests for the FM-SYSCOND element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndSwSystemconsts
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureMapAssertion
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMFeatureMapAssertion:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_with_formula(self):
        obj = FMFeatureMapAssertion(self._parent(), "MapElement")
        formula = FMConditionByFeaturesAndSwSystemconsts()
        formula.setMixedString("feature == true")
        obj.setFmSyscond(formula)

        container = ET.Element("CONDITIONS")
        ARXMLWriter().writeFMFeatureMapAssertion(container, obj)
        element = container.find("FM-FEATURE-MAP-ASSERTION")

        assert element.find("SHORT-NAME").text == "MapElement"
        assert element.find("FM-SYSCOND").text == "feature == true"

    def test_write_minimal(self):
        obj = FMFeatureMapAssertion(self._parent(), "MapElement")

        container = ET.Element("CONDITIONS")
        ARXMLWriter().writeFMFeatureMapAssertion(container, obj)
        element = container.find("FM-FEATURE-MAP-ASSERTION")

        assert element.find("FM-SYSCOND") is None

    def test_round_trip(self):
        obj = FMFeatureMapAssertion(self._parent(), "MapElement")
        formula = FMConditionByFeaturesAndSwSystemconsts()
        formula.setMixedString("feature == true")
        obj.setFmSyscond(formula)

        container = ET.Element("CONDITIONS")
        ARXMLWriter().writeFMFeatureMapAssertion(container, obj)
        element = container.find("FM-FEATURE-MAP-ASSERTION")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed = ARXMLParser().readFMFeatureMapAssertion(parsed_element, FMFeatureMapAssertion(self._parent(), "MapElement"))
        assert parsed.getFmSyscond() is not None
        assert parsed.getFmSyscond().getMixedString() == "feature == true"
