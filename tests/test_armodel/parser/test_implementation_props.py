"""
Tests for parsing IMPLEMENTATION-PROPS elements — Table 5.20 (p.287, R23-11).

ImplementationProps is abstract (Base = ARObject, Referrable) and carries the
`symbol` attribute (CIdentifier, 0..1) serialized as the SYMBOL child element.
Exercised directly on a concrete subclass instance via readImplementationProps,
which owns the readReferrable call (Rule 0013.1).

Round-trip counterpart: tests/test_armodel/writer/test_implementation_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
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


class _ConcreteProps(ImplementationProps):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


def _props():
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return _ConcreteProps(ar_root, "props")


class TestReadImplementationProps:
    """
    Test readImplementationProps — SHORT-NAME via Referrable, SYMBOL field value (Table 5.20).
    """

    def test_read_symbol_field_value(self, parser):
        """
        Test that the SYMBOL value is populated into the symbol field.
        """
        props = _props()
        element = ET.fromstring(
            f"""<SYMBOL-PROPS xmlns='{NS}'>
                <SHORT-NAME>props</SHORT-NAME>
                <SYMBOL>TestSymbol_C</SYMBOL>
            </SYMBOL-PROPS>"""
        )

        parser.readImplementationProps(element, props)

        assert props.getSymbol() is not None
        assert props.getSymbol().getValue() == "TestSymbol_C"

    def test_read_without_symbol_leaves_field_none(self, parser):
        """
        Test that a props element without a SYMBOL child leaves the symbol field None.
        """
        props = _props()
        element = ET.fromstring(f"<SYMBOL-PROPS xmlns='{NS}'><SHORT-NAME>props</SHORT-NAME></SYMBOL-PROPS>")

        parser.readImplementationProps(element, props)

        assert props.getSymbol() is None
