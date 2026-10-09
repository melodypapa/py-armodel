"""Parser tests for the FM-FEATURE-MAP-ELEMENT element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureMapElement
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


class TestReadFMFeatureMapElement:
    def test_read_all_members(self):
        parent = _parent()
        element = ET.Element("FM-FEATURE-MAP-ELEMENT")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "MapElement"
        assertions_tag = ET.SubElement(element, "ASSERTIONS")
        assertion = ET.SubElement(assertions_tag, "FM-FEATURE-MAP-ASSERTION")
        assertion_short_name = ET.SubElement(assertion, "SHORT-NAME")
        assertion_short_name.text = "Assertion"
        conditions_tag = ET.SubElement(element, "CONDITIONS")
        condition = ET.SubElement(conditions_tag, "FM-FEATURE-MAP-CONDITION")
        condition_short_name = ET.SubElement(condition, "SHORT-NAME")
        condition_short_name.text = "Condition"
        pb_refs_tag = ET.SubElement(element, "POST-BUILD-VARIANT-CRITERION-VALUE-SET-REFS")
        pb_ref = ET.SubElement(pb_refs_tag, "POST-BUILD-VARIANT-CRITERION-VALUE-SET-REF")
        pb_ref.attrib["DEST"] = "POST-BUILD-VARIANT-CRITERION-VALUE-SET"
        pb_ref.text = "/Pkg/PostBuildValueSet"
        sw_refs_tag = ET.SubElement(element, "SW-SYSTEMCONSTANT-VALUE-SET-REFS")
        sw_ref = ET.SubElement(sw_refs_tag, "SW-SYSTEMCONSTANT-VALUE-SET-REF")
        sw_ref.attrib["DEST"] = "SW-SYSTEMCONSTANT-VALUE-SET"
        sw_ref.text = "/Pkg/SwSystemconstantValueSet"

        obj = ARXMLParser().readFMFeatureMapElement(_round_trip(element), FMFeatureMapElement(parent, "MapElement"))
        assert obj.getShortName() == "MapElement"
        assert len(obj.getAssertions()) == 1
        assert obj.getAssertions()[0].getShortName() == "Assertion"
        assert len(obj.getConditions()) == 1
        assert obj.getConditions()[0].getShortName() == "Condition"
        assert len(obj.getPostBuildVariantCriterionValueSetRefs()) == 1
        assert obj.getPostBuildVariantCriterionValueSetRefs()[0].getValue() == "/Pkg/PostBuildValueSet"
        assert len(obj.getSwSystemconstantValueSetRefs()) == 1
        assert obj.getSwSystemconstantValueSetRefs()[0].getValue() == "/Pkg/SwSystemconstantValueSet"

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("FM-FEATURE-MAP-ELEMENT")

        obj = ARXMLParser().readFMFeatureMapElement(_round_trip(element), FMFeatureMapElement(parent, "MapElement"))
        assert obj.getAssertions() == []
        assert obj.getConditions() == []
        assert obj.getPostBuildVariantCriterionValueSetRefs() == []
        assert obj.getSwSystemconstantValueSetRefs() == []
