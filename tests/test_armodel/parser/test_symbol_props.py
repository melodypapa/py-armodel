"""
Tests for parsing SYMBOL-PROPS elements — Table 5.21 (p.288, R23-11).

SymbolProps has no own attributes (Table 5.21 Attribute row is "-"); the `symbol`
attribute is inherited from ImplementationProps (Table 5.20) and serialized as the
SYMBOL child element. Exercised via the ImplementationDataType.symbolProps aggregation.

Round-trip counterpart: tests/test_armodel/writer/test_symbol_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _data_type():
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    from armodel.models import ImplementationDataType

    return ImplementationDataType(parent=ar_root, short_name="dt")


class TestReadSymbolProps:
    """
    Test readImplementationDataTypeSymbolProps → readSymbolProps (Table 5.21).
    """

    def test_read_field_values(self, parser):
        """
        Test that SHORT-NAME and the inherited SYMBOL value are populated.
        """
        data_type = _data_type()
        element = ET.fromstring(
            f"""<IMPLEMENTATION-DATA-TYPE xmlns='{NS}'>
                <SYMBOL-PROPS>
                    <SHORT-NAME>sym</SHORT-NAME>
                    <SYMBOL>TestSymbol_C</SYMBOL>
                </SYMBOL-PROPS>
            </IMPLEMENTATION-DATA-TYPE>"""
        )

        parser.readImplementationDataTypeSymbolProps(element, data_type)

        props = data_type.getSymbolProps()
        assert props is not None
        assert props.getShortName() == "sym"
        assert props.getSymbol().getValue() == "TestSymbol_C"

    def test_read_without_symbol_props(self, parser):
        """
        Test that an IMPLEMENTATION-DATA-TYPE without SYMBOL-PROPS leaves symbolProps None.
        """
        data_type = _data_type()
        element = ET.fromstring(f"<IMPLEMENTATION-DATA-TYPE xmlns='{NS}'></IMPLEMENTATION-DATA-TYPE>")

        parser.readImplementationDataTypeSymbolProps(element, data_type)

        assert data_type.getSymbolProps() is None

    def test_read_symbol_props_without_symbol(self, parser):
        """
        Test that a SYMBOL-PROPS without a SYMBOL child leaves the symbol None.
        """
        data_type = _data_type()
        element = ET.fromstring(
            f"""<IMPLEMENTATION-DATA-TYPE xmlns='{NS}'>
                <SYMBOL-PROPS>
                    <SHORT-NAME>sym</SHORT-NAME>
                </SYMBOL-PROPS>
            </IMPLEMENTATION-DATA-TYPE>"""
        )

        parser.readImplementationDataTypeSymbolProps(element, data_type)

        props = data_type.getSymbolProps()
        assert props is not None
        assert props.getShortName() == "sym"
        assert props.getSymbol() is None
