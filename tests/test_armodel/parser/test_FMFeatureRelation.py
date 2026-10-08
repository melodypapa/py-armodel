"""Parser tests for the FM-FEATURE-RELATION element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureRelation
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


class TestReadFMFeatureRelation:
    def test_read_all_members(self):
        parent = _parent()
        element = ET.Element("FM-FEATURE-RELATION")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "Relation"
        refs_tag = ET.SubElement(element, "FEATURE-REFS")
        feature_ref = ET.SubElement(refs_tag, "FEATURE-REF")
        feature_ref.attrib["DEST"] = "FM-FEATURE"
        feature_ref.text = "/Pkg/Feature"
        restriction = ET.SubElement(element, "RESTRICTION")
        restriction.text = "feature == true"

        obj = ARXMLParser().readFMFeatureRelation(_round_trip(element), FMFeatureRelation(parent, "Relation"))
        assert obj.getShortName() == "Relation"
        assert len(obj.getFeatureRefs()) == 1
        assert obj.getFeatureRefs()[0].getValue() == "/Pkg/Feature"
        assert obj.getFeatureRefs()[0].getDest() == "FM-FEATURE"
        assert obj.getRestriction() is not None
        assert obj.getRestriction().getMixedString() == "feature == true"

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("FM-FEATURE-RELATION")

        obj = ARXMLParser().readFMFeatureRelation(_round_trip(element), FMFeatureRelation(parent, "Relation"))
        assert obj.getFeatureRefs() == []
        assert obj.getRestriction() is None
