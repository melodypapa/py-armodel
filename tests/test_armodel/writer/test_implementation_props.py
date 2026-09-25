"""
Tests for writing IMPLEMENTATION-PROPS elements — Table 5.20 (p.287, R23-11).

ImplementationProps is abstract (Base = ARObject, Referrable) and carries the
`symbol` attribute (CIdentifier, 0..1) serialized as the SYMBOL child element.
Exercised directly on a concrete subclass instance via writeImplementationProps,
which owns the writeReferrable call (Rule 0013.1).

Round-trip counterpart: tests/test_armodel/parser/test_implementation_props.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


class _ConcreteProps(ImplementationProps):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


def _props_with_symbol(symbol_value=None):
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    props = _ConcreteProps(ar_root, "props")
    if symbol_value is not None:
        props.setSymbol(CIdentifier().setValue(symbol_value))
    return props


class TestWriteImplementationProps:
    """
    Test writeImplementationProps — SHORT-NAME via Referrable, SYMBOL field value (Table 5.20).
    """

    def test_write_short_name_and_symbol_field_value(self, writer):
        """
        Test that SHORT-NAME and the SYMBOL value are emitted.
        """
        props = _props_with_symbol("TestSymbol_C")
        parent = ET.Element("SYMBOL-PROPS")

        writer.writeImplementationProps(parent, props)

        assert parent.find("SHORT-NAME").text == "props"
        assert parent.find("SYMBOL") is not None
        assert parent.find("SYMBOL").text == "TestSymbol_C"

    def test_write_without_symbol_emits_no_symbol_element(self, writer):
        """
        Test that an unset symbol emits no SYMBOL element.
        """
        props = _props_with_symbol(None)
        parent = ET.Element("SYMBOL-PROPS")

        writer.writeImplementationProps(parent, props)

        assert parent.find("SHORT-NAME").text == "props"
        assert parent.find("SYMBOL") is None
