"""Parser tests for the FM-FEATURE-SELECTION element (XSD element order per xml.sequenceOffset)."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import FMFeatureSelection
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


class TestReadFMFeatureSelection:
    def test_read_all_members(self):
        parent = _parent()
        element = ET.Element("FM-FEATURE-SELECTION")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "Selection"
        feature_ref = ET.SubElement(element, "FEATURE-REF")
        feature_ref.attrib["DEST"] = "FM-FEATURE"
        feature_ref.text = "/Pkg/Feature"
        state = ET.SubElement(element, "STATE")
        state.text = "SELECTED"
        minimum = ET.SubElement(element, "MINIMUM-SELECTED-BINDING-TIME")
        minimum.text = "PRE-COMPILE-TIME"
        maximum = ET.SubElement(element, "MAXIMUM-SELECTED-BINDING-TIME")
        maximum.text = "SYSTEM-DESIGN-TIME"
        values_tag = ET.SubElement(element, "ATTRIBUTE-VALUES")
        ET.SubElement(values_tag, "FM-ATTRIBUTE-VALUE")

        obj = ARXMLParser().readFMFeatureSelection(_round_trip(element), FMFeatureSelection(parent, "Selection"))
        assert obj.getShortName() == "Selection"
        assert obj.getFeatureRef() is not None
        assert obj.getFeatureRef().getValue() == "/Pkg/Feature"
        assert obj.getFeatureRef().getDest() == "FM-FEATURE"
        assert obj.getState() is not None
        assert obj.getState().getValue() == "SELECTED"
        assert obj.getMinimumSelectedBindingTime().getValue() == "PRE-COMPILE-TIME"
        assert obj.getMaximumSelectedBindingTime().getValue() == "SYSTEM-DESIGN-TIME"
        assert len(obj.getAttributeValues()) == 1

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("FM-FEATURE-SELECTION")

        obj = ARXMLParser().readFMFeatureSelection(_round_trip(element), FMFeatureSelection(parent, "Selection"))
        assert obj.getFeatureRef() is None
        assert obj.getState() is None
        assert obj.getMinimumSelectedBindingTime() is None
        assert obj.getMaximumSelectedBindingTime() is None
        assert obj.getAttributeValues() == []
