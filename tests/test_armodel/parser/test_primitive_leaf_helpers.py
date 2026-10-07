"""
Reader tests: ARLiteral primitives are materialised as their concrete type via
the typed leaf helpers getChildElementOptional<Cls> (Rule 0013.2), and the
inherited T timestamp survives.

Writer counterpart: tests/test_armodel/writer/test_primitive_leaf_helpers.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    DiagRequirementIdString,
    McdIdentifier,
    SymbolString,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestCategoryStringLeaf:
    def test_reads_concrete_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><CATEGORY T='2023-05-05T00:00:00Z'>SW-COMPONENT-TYPE</CATEGORY></ROOT>")

        value = ARXMLParser().getChildElementOptionalCategoryString(element, "CATEGORY")

        assert isinstance(value, CategoryString)
        assert value.getValue() == "SW-COMPONENT-TYPE"
        assert value.timestamp == "2023-05-05T00:00:00Z"

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalCategoryString(element, "CATEGORY") is None


class TestMcdIdentifierLeaf:
    def test_reads_concrete_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><DISPLAY-IDENTIFIER T='2023-06-06T00:00:00Z'>DISP-1</DISPLAY-IDENTIFIER></ROOT>")

        value = ARXMLParser().getChildElementOptionalMcdIdentifier(element, "DISPLAY-IDENTIFIER")

        assert isinstance(value, McdIdentifier)
        assert value.getValue() == "DISP-1"
        assert value.timestamp == "2023-06-06T00:00:00Z"

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalMcdIdentifier(element, "DISPLAY-IDENTIFIER") is None


class TestSymbolStringLeaf:
    def test_reads_concrete_type_name_pattern_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><SYMBOL NAME-PATTERN='[A-Z]+' T='2023-07-07T00:00:00Z'>Sym</SYMBOL></ROOT>")

        value = ARXMLParser().getChildElementOptionalSymbolString(element, "SYMBOL")

        assert isinstance(value, SymbolString)
        assert value.getValue() == "Sym"
        assert value.getNamePattern() == "[A-Z]+"
        assert value.timestamp == "2023-07-07T00:00:00Z"

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalSymbolString(element, "SYMBOL") is None


class TestDiagRequirementIdStringLeaf:
    def test_reads_concrete_type_and_t(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><DIAG-REQUIREMENT T='2023-08-08T00:00:00Z'>REQ-1</DIAG-REQUIREMENT></ROOT>")

        value = ARXMLParser().getChildElementOptionalDiagRequirementIdString(element, "DIAG-REQUIREMENT")

        assert isinstance(value, DiagRequirementIdString)
        assert value.getValue() == "REQ-1"
        assert value.timestamp == "2023-08-08T00:00:00Z"

    def test_missing_returns_none(self):
        element = ET.fromstring(f"<ROOT xmlns='{NS}'/>")

        assert ARXMLParser().getChildElementOptionalDiagRequirementIdString(element, "DIAG-REQUIREMENT") is None
