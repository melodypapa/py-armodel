"""Parser round-trip tests for the SecurityExtractTemplate ARElements."""

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


class TestReadSecurityExtractElements:
    def test_read_security_event_definition(self):
        element = ET.Element("SECURITY-EVENT-DEFINITION")
        ET.SubElement(element, "SHORT-NAME").text = "Definition"
        id_element = ET.SubElement(element, "ID")
        id_element.text = "42"

        parent = _parent()
        obj = ARXMLParser().readSecurityEventDefinition(_round_trip(element), parent.createSecurityEventDefinition("Definition"))
        assert obj.getShortName() == "Definition"
        assert obj.getId().getValue() == 42

    def test_read_security_event_filter_chain(self):
        element = ET.Element("SECURITY-EVENT-FILTER-CHAIN")
        ET.SubElement(element, "SHORT-NAME").text = "Chain"
        aggregation = ET.SubElement(element, "AGGREGATION")
        ET.SubElement(aggregation, "SHORT-NAME").text = "Aggregation"
        one_every_n = ET.SubElement(element, "ONE-EVERY-N")
        ET.SubElement(one_every_n, "SHORT-NAME").text = "OneEveryN"
        n_element = ET.SubElement(one_every_n, "N")
        n_element.text = "3"
        state = ET.SubElement(element, "STATE")
        ET.SubElement(state, "SHORT-NAME").text = "State"
        threshold = ET.SubElement(element, "THRESHOLD")
        ET.SubElement(threshold, "SHORT-NAME").text = "Threshold"

        parent = _parent()
        obj = ARXMLParser().readSecurityEventFilterChain(_round_trip(element), parent.createSecurityEventFilterChain("Chain"))
        assert obj.getShortName() == "Chain"
        assert obj.getAggregation() is not None
        assert obj.getAggregation().getShortName() == "Aggregation"
        assert obj.getOneEveryN() is not None
        assert obj.getOneEveryN().getN().getValue() == 3
        assert obj.getState() is not None
        assert obj.getThreshold() is not None

    def test_read_ids_design(self):
        element = ET.Element("IDS-DESIGN")
        ET.SubElement(element, "SHORT-NAME").text = "Design"
        elements_tag = ET.SubElement(element, "ELEMENTS")
        conditional = ET.SubElement(elements_tag, "IDS-COMMON-ELEMENT-REF-CONDITIONAL")
        ref = ET.SubElement(conditional, "IDS-COMMON-ELEMENT-REF")
        ref.attrib["DEST"] = "SECURITY-EVENT-DEFINITION"
        ref.text = "/Pkg/Definition"

        parent = _parent()
        obj = ARXMLParser().readIdsDesign(_round_trip(element), parent.createIdsDesign("Design"))
        assert obj.getShortName() == "Design"
        assert len(obj.getElementRefs()) == 1
        assert obj.getElementRefs()[0].getValue() == "/Pkg/Definition"
        assert obj.getElementRefs()[0].getDest() == "SECURITY-EVENT-DEFINITION"

    def test_read_security_event_context_mapping_bsw_module(self):
        element = ET.Element("SECURITY-EVENT-CONTEXT-MAPPING-BSW-MODULE")
        ET.SubElement(element, "SHORT-NAME").text = "Mapping"
        filter_chains_tag = ET.SubElement(element, "FILTER-CHAINS")
        conditional = ET.SubElement(filter_chains_tag, "SECURITY-EVENT-FILTER-CHAIN-REF-CONDITIONAL")
        ref = ET.SubElement(conditional, "SECURITY-EVENT-FILTER-CHAIN-REF")
        ref.attrib["DEST"] = "SECURITY-EVENT-FILTER-CHAIN"
        ref.text = "/Pkg/Chain"
        ET.SubElement(element, "AFFECTED-BSW-MODULE").text = "Crypto"

        parent = _parent()
        obj = ARXMLParser().readSecurityEventContextMappingBswModule(_round_trip(element), parent.createSecurityEventContextMappingBswModule("Mapping"))
        assert obj.getShortName() == "Mapping"
        assert obj.getFilterChainRef().getValue() == "/Pkg/Chain"
        assert obj.getAffectedBswModule().getValue() == "Crypto"

    def test_read_idsm_instance(self):
        element = ET.Element("IDSM-INSTANCE")
        ET.SubElement(element, "SHORT-NAME").text = "Instance"
        states_tag = ET.SubElement(element, "BLOCK-STATES")
        block_state = ET.SubElement(states_tag, "BLOCK-STATE")
        ET.SubElement(block_state, "SHORT-NAME").text = "BlockState"
        id_element = ET.SubElement(element, "IDSM-INSTANCE-ID")
        id_element.text = "5"
        ET.SubElement(element, "TIMESTAMP-FORMAT").text = "UTC"

        parent = _parent()
        obj = ARXMLParser().readIdsmInstance(_round_trip(element), parent.createIdsmInstance("Instance"))
        assert obj.getShortName() == "Instance"
        assert len(obj.getBlockStates()) == 1
        assert obj.getBlockStates()[0].getShortName() == "BlockState"
        assert obj.getIdsmInstanceId().getValue() == 5
        assert obj.getTimestampFormat().getValue() == "UTC"
