"""Parser tests for the POST-BUILD-VARIANT-CRITERION-VALUE-SET element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
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


class TestReadPostBuildVariantCriterionValueSet:
    def test_read_with_items(self):
        element = ET.Element("POST-BUILD-VARIANT-CRITERION-VALUE-SET")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "ValueSet"
        wrapper_tag = ET.SubElement(element, "POST-BUILD-VARIANT-CRITERION-VALUES")
        ET.SubElement(wrapper_tag, "POST-BUILD-VARIANT-CRITERION-VALUE")

        parent = _parent()
        obj = ARXMLParser().readPostBuildVariantCriterionValueSet(_round_trip(element), parent.createPostBuildVariantCriterionValueSet("ValueSet"))
        assert obj.getShortName() == "ValueSet"
        assert len(obj.getPostBuildVariantCriterionValues()) == 1

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("POST-BUILD-VARIANT-CRITERION-VALUE-SET")

        obj = ARXMLParser().readPostBuildVariantCriterionValueSet(_round_trip(element), parent.createPostBuildVariantCriterionValueSet("ValueSet"))
        assert obj.getPostBuildVariantCriterionValues() == []
