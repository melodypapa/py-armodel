"""Parser tests for the FM-FEATURE-SELECTION-SET element."""

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


class TestReadFMFeatureSelectionSet:
    def test_read_all_members(self):
        element = ET.Element("FM-FEATURE-SELECTION-SET")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "SelectionSet"
        fm_refs_tag = ET.SubElement(element, "FEATURE-MODEL-REFS")
        fm_ref = ET.SubElement(fm_refs_tag, "FEATURE-MODEL-REF")
        fm_ref.attrib["DEST"] = "FM-FEATURE-MODEL"
        fm_ref.text = "/Pkg/FeatureModel"
        inc_refs_tag = ET.SubElement(element, "INCLUDE-REFS")
        inc_ref = ET.SubElement(inc_refs_tag, "INCLUDE-REF")
        inc_ref.attrib["DEST"] = "FM-FEATURE-SELECTION-SET"
        inc_ref.text = "/Pkg/OtherSet"
        selections_tag = ET.SubElement(element, "SELECTIONS")
        selection = ET.SubElement(selections_tag, "FM-FEATURE-SELECTION")
        ET.SubElement(selection, "SHORT-NAME").text = "Selection"

        parent = _parent()
        obj = ARXMLParser().readFMFeatureSelectionSet(_round_trip(element), parent.createFMFeatureSelectionSet("SelectionSet"))
        assert obj.getShortName() == "SelectionSet"
        assert len(obj.getFeatureModelRefs()) == 1
        assert obj.getFeatureModelRefs()[0].getValue() == "/Pkg/FeatureModel"
        assert len(obj.getIncludeRefs()) == 1
        assert obj.getIncludeRefs()[0].getValue() == "/Pkg/OtherSet"
        assert len(obj.getSelections()) == 1
        assert obj.getSelections()[0].getShortName() == "Selection"

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("FM-FEATURE-SELECTION-SET")

        obj = ARXMLParser().readFMFeatureSelectionSet(_round_trip(element), parent.createFMFeatureSelectionSet("SelectionSet"))
        assert obj.getFeatureModelRefs() == []
        assert obj.getIncludeRefs() == []
        assert obj.getSelections() == []
