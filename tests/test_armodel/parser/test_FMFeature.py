"""Parser tests for the FM-FEATURE element (AR-PACKAGE element round-trip)."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import FMFeature
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


class TestReadFMFeature:
    def test_read_all_members(self):
        element = ET.Element("FM-FEATURE")
        short_name = ET.SubElement(element, "SHORT-NAME")
        short_name.text = "Feature"
        defs_tag = ET.SubElement(element, "ATTRIBUTE-DEFS")
        attribute_def = ET.SubElement(defs_tag, "FM-ATTRIBUTE-DEF")
        ET.SubElement(attribute_def, "SHORT-NAME").text = "AttrDef"
        decompositions_tag = ET.SubElement(element, "DECOMPOSITIONS")
        decomposition = ET.SubElement(decompositions_tag, "FM-FEATURE-DECOMPOSITION")
        category = ET.SubElement(decomposition, "CATEGORY")
        category.text = "MANDATORYFEATURE"
        maximum = ET.SubElement(element, "MAXIMUM-INTENDED-BINDING-TIME")
        maximum.text = "SYSTEM-DESIGN-TIME"
        minimum = ET.SubElement(element, "MINIMUM-INTENDED-BINDING-TIME")
        minimum.text = "PRE-COMPILE-TIME"
        relations_tag = ET.SubElement(element, "RELATIONS")
        relation = ET.SubElement(relations_tag, "FM-FEATURE-RELATION")
        ET.SubElement(relation, "SHORT-NAME").text = "Relation"
        restrictions_tag = ET.SubElement(element, "RESTRICTIONS")
        restriction = ET.SubElement(restrictions_tag, "FM-FEATURE-RESTRICTION")
        ET.SubElement(restriction, "SHORT-NAME").text = "Restriction"

        parent = _parent()
        feature = parent.createFMFeature("Feature")
        obj = ARXMLParser().readFMFeature(_round_trip(element), feature)
        assert obj.getShortName() == "Feature"
        assert len(obj.getAttributeDefs()) == 1
        assert obj.getAttributeDefs()[0].getShortName() == "AttrDef"
        assert len(obj.getDecompositions()) == 1
        assert obj.getDecompositions()[0].getCategory().getValue() == "MANDATORYFEATURE"
        assert obj.getMaximumIntendedBindingTime().getValue() == "SYSTEM-DESIGN-TIME"
        assert obj.getMinimumIntendedBindingTime().getValue() == "PRE-COMPILE-TIME"
        assert len(obj.getRelations()) == 1
        assert obj.getRelations()[0].getShortName() == "Relation"
        assert len(obj.getRestrictions()) == 1
        assert obj.getRestrictions()[0].getShortName() == "Restriction"

    def test_read_minimal(self):
        parent = _parent()
        element = ET.Element("FM-FEATURE")

        feature = parent.createFMFeature("Feature")
        obj = ARXMLParser().readFMFeature(_round_trip(element), feature)
        assert obj.getAttributeDefs() == []
        assert obj.getDecompositions() == []
        assert obj.getMaximumIntendedBindingTime() is None
        assert obj.getRelations() == []
        assert obj.getRestrictions() == []
