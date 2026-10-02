"""
Tests for writing DIAGNOSTIC-J-1939-SPN elements —
DiagnosticJ1939Spn, Table 4.219 (p.219, R23-11).

DiagnosticJ1939Spn (Base most-derived DiagnosticCommonElement) owns the 0..1
spn attribute (SPN, POSITIVE-INTEGER), AUTOSAR_00052.xsd group
DIAGNOSTIC-J-1939-SPN l.39071.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_j1939_spn.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticJ1939Spn
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticJ1939Spn:
    """Tests for writeDiagnosticJ1939Spn — own element field values (Table 4.219)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticJ1939Spn without spn emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticJ1939Spns")
        package.createDiagnosticJ1939Spn("Spn1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticJ1939Spn(parent, package.getElement("Spn1", DiagnosticJ1939Spn))

        child = parent.find("DIAGNOSTIC-J-1939-SPN")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Spn1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_spn(self):
        """Test that the spn attribute is emitted with the spec value."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticJ1939Spns")
        spn = package.createDiagnosticJ1939Spn("Spn1")
        value = PositiveInteger()
        value.setValue("19000")
        spn.setSpn(value)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticJ1939Spn(parent, spn)

        child = parent.find("DIAGNOSTIC-J-1939-SPN")
        spn_element = child.find("SPN")
        assert spn_element is not None
        assert spn_element.text == "19000"
