"""Parser tests for the FM-COND element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureMapCondition
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


class TestReadFMFeatureMapCondition:
    def test_read_with_formula(self):
        parent = _parent()
        element = ET.Element("FM-COND")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "MapElement"
        formula = ET.SubElement(element, "FM-COND")
        formula.text = "feature == true"

        obj = ARXMLParser().readFMFeatureMapCondition(_round_trip(element), FMFeatureMapCondition(parent, "MapElement"))
        assert obj.getShortName() == "MapElement"
        assert obj.getFmCond() is not None
        assert obj.getFmCond().getMixedString() == "feature == true"

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("FM-COND")

        obj = ARXMLParser().readFMFeatureMapCondition(_round_trip(element), FMFeatureMapCondition(parent, "MapElement"))
        assert obj.getFmCond() is None
