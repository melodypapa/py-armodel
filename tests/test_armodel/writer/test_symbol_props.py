"""
Tests for writing SYMBOL-PROPS elements — Table 5.21 (p.288, R23-11).

SymbolProps has no own attributes (Table 5.21 Attribute row is "-"); the `symbol`
attribute is inherited from ImplementationProps (Table 5.20) and serialized as the
SYMBOL child element. Exercised via the ImplementationDataType.symbolProps aggregation.

Round-trip counterpart: tests/test_armodel/parser/test_symbol_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _data_type_with_props(symbol_value=None):
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    from armodel.models import ImplementationDataType

    data_type = ImplementationDataType(parent=ar_root, short_name="dt")
    props = data_type.createSymbolProps("sym")
    if symbol_value is not None:
        symbol = CIdentifier()
        symbol.setValue(symbol_value)
        props.setSymbol(symbol)
    return data_type


class TestWriteSymbolProps:
    """
    Test writeImplementationDataTypeSymbolProps → writeSymbolProps (Table 5.21).
    """

    def test_write_field_values(self, writer):
        """
        Test that the SYMBOL-PROPS element carries SHORT-NAME and the inherited
        SYMBOL value.
        """
        data_type = _data_type_with_props("TestSymbol_C")

        element = ET.Element("PARENT")
        writer.writeImplementationDataTypeSymbolProps(element, data_type)

        props_tag = element.find("SYMBOL-PROPS")
        assert props_tag is not None
        assert props_tag.find("SHORT-NAME").text == "sym"
        assert props_tag.find("SYMBOL").text == "TestSymbol_C"

    def test_write_without_symbol_props(self, writer):
        """
        Test that a data type without symbolProps writes no element.
        """
        ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        from armodel.models import ImplementationDataType

        data_type = ImplementationDataType(parent=ar_root, short_name="dt")

        element = ET.Element("PARENT")
        writer.writeImplementationDataTypeSymbolProps(element, data_type)

        assert element.find("SYMBOL-PROPS") is None

    def test_write_symbol_props_without_symbol(self, writer):
        """
        Test that a SYMBOL-PROPS without a symbol writes the wrapper without a
        SYMBOL child.
        """
        data_type = _data_type_with_props(None)

        element = ET.Element("PARENT")
        writer.writeImplementationDataTypeSymbolProps(element, data_type)

        props_tag = element.find("SYMBOL-PROPS")
        assert props_tag is not None
        assert props_tag.find("SHORT-NAME").text == "sym"
        assert props_tag.find("SYMBOL") is None
