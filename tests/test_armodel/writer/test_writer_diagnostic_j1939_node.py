"""
Tests for writing DIAGNOSTIC-J-1939-NODE elements —
DiagnosticJ1939Node, Table 5.41 (p.267, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_j1939_node.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticJ1939Node
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticJ1939Node:
    """Tests for writeDiagnosticJ1939Node — own element field values (Table 5.41)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticJ1939Node without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticJ1939Node("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticJ1939Node(parent, package.getReferrableElement("M1", DiagnosticJ1939Node))

        child = parent.find("DIAGNOSTIC-J-1939-NODE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticJ1939Node("M1")
        mapping.setNmNodeRef(RefType().setValue("/AUTOSAR/NmNode1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticJ1939Node(parent, mapping)

        child = parent.find("DIAGNOSTIC-J-1939-NODE")
        assert [c.tag for c in child] == ["SHORT-NAME", "NM-NODE-REF"]
        assert child.find("NM-NODE-REF").text == "/AUTOSAR/NmNode1"
