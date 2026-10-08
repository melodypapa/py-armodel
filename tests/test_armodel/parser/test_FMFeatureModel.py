"""Parser tests for the FM-FEATURE-MODEL element."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import FMFeatureModel
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


class TestReadFMFeatureModel:
    def test_read_all_members(self):
        element = ET.Element("FM-FEATURE-MODEL")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "FeatureModel"
        refs_tag = ET.SubElement(element, "FEATURE-REFS")
        feature_ref = ET.SubElement(refs_tag, "FEATURE-REF")
        feature_ref.attrib["DEST"] = "FM-FEATURE"
        feature_ref.text = "/Pkg/Feature"
        root_ref = ET.SubElement(element, "ROOT-REF")
        root_ref.attrib["DEST"] = "FM-FEATURE"
        root_ref.text = "/Pkg/Root"

        parent = _parent()
        obj = ARXMLParser().readFMFeatureModel(_round_trip(element), parent.createFMFeatureModel("FeatureModel"))
        assert obj.getShortName() == "FeatureModel"
        assert len(obj.getFeatureRefs()) == 1
        assert obj.getFeatureRefs()[0].getValue() == "/Pkg/Feature"
        assert obj.getFeatureRefs()[0].getDest() == "FM-FEATURE"
        assert obj.getRootRef() is not None
        assert obj.getRootRef().getValue() == "/Pkg/Root"

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("FM-FEATURE-MODEL")

        obj = ARXMLParser().readFMFeatureModel(_round_trip(element), parent.createFMFeatureModel("FeatureModel"))
        assert obj.getFeatureRefs() == []
        assert obj.getRootRef() is None
