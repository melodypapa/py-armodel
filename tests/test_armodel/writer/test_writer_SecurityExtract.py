"""Writer round-trip tests for the SecurityExtractTemplate ARElements."""

import re
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    SecurityEventContextMappingBswModule,
    SecurityEventDefinition,
    SecurityEventFilterChain,
    IdsDesign,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    SecurityEventAggregationFilter,
    SecurityEventOneEveryNFilter,
    SecurityEventStateFilter,
    SecurityEventThresholdFilter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteSecurityExtractElements:
    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_write_and_round_trip_filter_chain(self):
        filter_chain = SecurityEventFilterChain(self._parent(), "Chain")
        aggregation = SecurityEventAggregationFilter(filter_chain, "Aggregation")
        filter_chain.setAggregation(aggregation)
        one_every_n = SecurityEventOneEveryNFilter(filter_chain, "OneEveryN")
        n = PositiveInteger()
        n.setValue(3)
        one_every_n.setN(n)
        filter_chain.setOneEveryN(one_every_n)
        state = SecurityEventStateFilter(filter_chain, "State")
        state.addBlockIfStateActiveCpRef(RefType().setValue("/Pkg/BlockState").setDest("BLOCK-STATE"))
        filter_chain.setState(state)
        threshold = SecurityEventThresholdFilter(filter_chain, "Threshold")
        filter_chain.setThreshold(threshold)

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeSecurityEventFilterChain(container, filter_chain)
        element = container.find("SECURITY-EVENT-FILTER-CHAIN")

        assert element.find("SHORT-NAME").text == "Chain"
        assert element.find("AGGREGATION/SHORT-NAME").text == "Aggregation"
        assert element.find("ONE-EVERY-N/N").text == "3"
        assert element.find("STATE/BLOCK-IF-STATE-ACTIVE-CP-REFS/BLOCK-IF-STATE-ACTIVE-CP-REF").text == "/Pkg/BlockState"
        assert element.find("THRESHOLD") is not None

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]

        parsed_parent = self._parent()
        parsed = ARXMLParser().readSecurityEventFilterChain(ET.fromstring(xml_str), parsed_parent.createSecurityEventFilterChain("Chain"))
        assert parsed.getAggregation() is not None
        assert parsed.getOneEveryN().getN().getValue() == 3
        assert parsed.getState().getBlockIfStateActiveCpRefs()[0].getValue() == "/Pkg/BlockState"
        assert parsed.getThreshold() is not None

    def test_write_and_round_trip_context_mapping_bsw_module(self):
        mapping = SecurityEventContextMappingBswModule(self._parent(), "Mapping")
        mapping.setFilterChainRef(RefType().setValue("/Pkg/Chain").setDest("SECURITY-EVENT-FILTER-CHAIN"))

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeSecurityEventContextMappingBswModule(container, mapping)
        element = container.find("SECURITY-EVENT-CONTEXT-MAPPING-BSW-MODULE")

        assert element.find("FILTER-CHAINS/SECURITY-EVENT-FILTER-CHAIN-REF-CONDITIONAL/SECURITY-EVENT-FILTER-CHAIN-REF").text == "/Pkg/Chain"

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]

        parsed_parent = self._parent()
        parsed = ARXMLParser().readSecurityEventContextMappingBswModule(ET.fromstring(xml_str), parsed_parent.createSecurityEventContextMappingBswModule("Mapping"))
        assert parsed.getFilterChainRef().getValue() == "/Pkg/Chain"

    def test_write_and_round_trip_ids_design(self):
        ids_design = IdsDesign(self._parent(), "Design")
        ids_design.addElementRef(RefType().setValue("/Pkg/Definition").setDest("SECURITY-EVENT-DEFINITION"))

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeIdsDesign(container, ids_design)
        element = container.find("IDS-DESIGN")

        assert element.find("ELEMENTS/IDS-COMMON-ELEMENT-REF-CONDITIONAL/IDS-COMMON-ELEMENT-REF").text == "/Pkg/Definition"

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]

        parsed_parent = self._parent()
        parsed = ARXMLParser().readIdsDesign(ET.fromstring(xml_str), parsed_parent.createIdsDesign("Design"))
        assert parsed.getElementRefs()[0].getValue() == "/Pkg/Definition"

    def test_write_and_round_trip_security_event_definition(self):
        definition = SecurityEventDefinition(self._parent(), "Definition")
        security_event_id = PositiveInteger()
        security_event_id.setValue(42)
        definition.setId(security_event_id)

        container = ET.Element("ELEMENTS")
        ARXMLWriter().writeSecurityEventDefinition(container, definition)
        element = container.find("SECURITY-EVENT-DEFINITION")

        assert element.find("ID").text == "42"

        xml_str = ET.tostring(element).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]

        parsed_parent = self._parent()
        parsed = ARXMLParser().readSecurityEventDefinition(ET.fromstring(xml_str), parsed_parent.createSecurityEventDefinition("Definition"))
        assert parsed.getId().getValue() == 42
