"""
Reader tests: ARLiteral primitives are materialised as their concrete type via
the typed leaf helpers getChildElementOptional<Cls> (Rule 0013.2), and the
inherited T timestamp survives.

Writer counterpart: tests/test_armodel/writer/test_primitive_leaf_helpers.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    McdIdentifier,
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
