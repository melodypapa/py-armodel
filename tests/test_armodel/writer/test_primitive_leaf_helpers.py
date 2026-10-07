"""
Writer tests: ARLiteral primitives are emitted through the typed leaf helpers
setChildElementOptional<Cls> (Rule 0013.2), carrying the inherited T timestamp.

Reader counterpart: tests/test_armodel/parser/test_primitive_leaf_helpers.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    DiagRequirementIdString,
    Ip4AddressString,
    Ip6AddressString,
    McdIdentifier,
    SymbolString,
)
from armodel.writer.arxml_writer import ARXMLWriter


class TestCategoryStringLeaf:
    def test_writes_concrete_type_and_t(self):
        value = CategoryString()
        value.setValue("SW-COMPONENT-TYPE")
        value.timestamp = "2023-05-05T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalCategoryString(element, "CATEGORY", value)

        written = element.find("CATEGORY")
        assert written is not None
        assert written.text == "SW-COMPONENT-TYPE"
        assert written.attrib["T"] == "2023-05-05T00:00:00Z"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalCategoryString(element, "CATEGORY", None)

        assert element.find("CATEGORY") is None


class TestMcdIdentifierLeaf:
    def test_writes_concrete_type_and_t(self):
        value = McdIdentifier()
        value.setValue("DISP-1")
        value.timestamp = "2023-06-06T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalMcdIdentifier(element, "DISPLAY-IDENTIFIER", value)

        written = element.find("DISPLAY-IDENTIFIER")
        assert written is not None
        assert written.text == "DISP-1"
        assert written.attrib["T"] == "2023-06-06T00:00:00Z"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalMcdIdentifier(element, "DISPLAY-IDENTIFIER", None)

        assert element.find("DISPLAY-IDENTIFIER") is None


class TestSymbolStringLeaf:
    def test_writes_concrete_type_name_pattern_and_t(self):
        value = SymbolString()
        value.setValue("Sym")
        value.setNamePattern("[A-Z]+")
        value.timestamp = "2023-07-07T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalSymbolString(element, "SYMBOL", value)

        written = element.find("SYMBOL")
        assert written is not None
        assert written.text == "Sym"
        assert written.attrib["NAME-PATTERN"] == "[A-Z]+"
        assert written.attrib["T"] == "2023-07-07T00:00:00Z"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalSymbolString(element, "SYMBOL", None)

        assert element.find("SYMBOL") is None


class TestDiagRequirementIdStringLeaf:
    def test_writes_concrete_type_and_t(self):
        value = DiagRequirementIdString()
        value.setValue("REQ-1")
        value.timestamp = "2023-08-08T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalDiagRequirementIdString(element, "DIAG-REQUIREMENT", value)

        written = element.find("DIAG-REQUIREMENT")
        assert written is not None
        assert written.text == "REQ-1"
        assert written.attrib["T"] == "2023-08-08T00:00:00Z"

    def test_none_emits_nothing(self):
        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalDiagRequirementIdString(element, "DIAG-REQUIREMENT", None)

        assert element.find("DIAG-REQUIREMENT") is None


class TestIpAddressStringLeaf:
    def test_writes_concrete_ip4_type_and_t(self):
        value = Ip4AddressString()
        value.setValue("192.168.0.1")
        value.timestamp = "2023-10-10T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalIp4AddressString(element, "IPV-4-ADDRESS", value)

        written = element.find("IPV-4-ADDRESS")
        assert written is not None
        assert written.text == "192.168.0.1"
        assert written.attrib["T"] == "2023-10-10T00:00:00Z"

    def test_writes_concrete_ip6_type_and_t(self):
        value = Ip6AddressString()
        value.setValue("fe80::1")
        value.timestamp = "2023-10-10T00:00:00Z"

        element = ET.Element("ROOT")
        ARXMLWriter().setChildElementOptionalIp6AddressString(element, "IPV-6-ADDRESS", value)

        written = element.find("IPV-6-ADDRESS")
        assert written is not None
        assert written.text == "fe80::1"
        assert written.attrib["T"] == "2023-10-10T00:00:00Z"
