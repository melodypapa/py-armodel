"""
Tests for writing DIAGNOSTIC-J-1939-SW-MAPPING elements —
DiagnosticJ1939SwMapping, Table 5.42 (p.268, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_j1939_sw_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticJ1939SwMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticJ1939SwMapping:
    """Tests for writeDiagnosticJ1939SwMapping — own element field values (Table 5.42)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticJ1939SwMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticJ1939SwMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticJ1939SwMapping(parent, package.getElement("M1", DiagnosticJ1939SwMapping))

        child = parent.find("DIAGNOSTIC-J-1939-SW-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticJ1939SwMapping("M1")
        mapping.setNodeRef(RefType().setValue("/AUTOSAR/Node1"))
        mapping.setSwComponentPrototypeRef(RefType().setValue("/AUTOSAR/SwComponentPrototype1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticJ1939SwMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-J-1939-SW-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "NODE-REF", "SW-COMPONENT-PROTOTYPE-IREF"]
        assert child.find("NODE-REF").text == "/AUTOSAR/Node1"
        assert child.find("SW-COMPONENT-PROTOTYPE-IREF").text == "/AUTOSAR/SwComponentPrototype1"
