"""Parser tests for the FM-FEATURE-RESTRICTION element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureRestriction
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


class TestReadFMFeatureRestriction:
    def test_read_with_restriction(self):
        parent = _parent()
        element = ET.Element("FM-FEATURE-RESTRICTION")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "Restriction"
        restriction = ET.SubElement(element, "RESTRICTION")
        restriction.text = "feature == true"

        obj = ARXMLParser().readFMFeatureRestriction(_round_trip(element), FMFeatureRestriction(parent, "Restriction"))
        assert obj.getRestriction() is not None
        assert obj.getRestriction().getMixedString() == "feature == true"

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("FM-FEATURE-RESTRICTION")

        obj = ARXMLParser().readFMFeatureRestriction(_round_trip(element), FMFeatureRestriction(parent, "Restriction"))
        assert obj.getRestriction() is None
