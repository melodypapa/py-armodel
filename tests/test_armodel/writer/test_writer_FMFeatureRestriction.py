"""Writer tests for the FM-FEATURE-RESTRICTION element."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate import FMConditionByFeaturesAndAttributes
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureRestriction
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteFMFeatureRestriction:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_with_restriction(self):
        restriction = FMFeatureRestriction(self._parent(), "Restriction")
        condition = FMConditionByFeaturesAndAttributes()
        condition.setMixedString("feature == true")
        restriction.setRestriction(condition)

        container = ET.Element("RESTRICTIONS")
        ARXMLWriter().writeFMFeatureRestriction(container, restriction)
        element = container.find("FM-FEATURE-RESTRICTION")

        assert element.find("SHORT-NAME").text == "Restriction"
        assert element.find("RESTRICTION").text == "feature == true"

    def test_write_minimal(self):
        restriction = FMFeatureRestriction(self._parent(), "Restriction")

        container = ET.Element("RESTRICTIONS")
        ARXMLWriter().writeFMFeatureRestriction(container, restriction)
        element = container.find("FM-FEATURE-RESTRICTION")

        assert element.find("RESTRICTION") is None

    def test_round_trip(self):
        restriction = FMFeatureRestriction(self._parent(), "Restriction")
        condition = FMConditionByFeaturesAndAttributes()
        condition.setMixedString("feature == true")
        restriction.setRestriction(condition)

        container = ET.Element("RESTRICTIONS")
        ARXMLWriter().writeFMFeatureRestriction(container, restriction)
        element = container.find("FM-FEATURE-RESTRICTION")

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        parsed_element = ET.fromstring(xml_str)

        parsed = ARXMLParser().readFMFeatureRestriction(parsed_element, FMFeatureRestriction(self._parent(), "Restriction"))
        assert parsed.getRestriction() is not None
        assert parsed.getRestriction().getMixedString() == "feature == true"
