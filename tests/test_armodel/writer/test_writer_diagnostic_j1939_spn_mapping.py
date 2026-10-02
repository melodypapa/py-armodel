"""
Tests for writing DIAGNOSTIC-J-1939-SPN-MAPPING elements —
DiagnosticJ1939SpnMapping, Table 5.40 (p.267, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_j1939_spn_mapping.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticJ1939SpnMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticJ1939SpnMapping:
    """Tests for writeDiagnosticJ1939SpnMapping — own element field values (Table 5.40)."""

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticJ1939SpnMapping without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        package.createDiagnosticJ1939SpnMapping("M1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticJ1939SpnMapping(parent, package.getElement("M1", DiagnosticJ1939SpnMapping))

        child = parent.find("DIAGNOSTIC-J-1939-SPN-MAPPING")
        assert child is not None
        assert child.find("SHORT-NAME").text == "M1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMappings")
        mapping = package.createDiagnosticJ1939SpnMapping("M1")
        mapping.addSendingNodeRef(RefType().setValue("/AUTOSAR/SendingNode1"))
        mapping.setSpnRef(RefType().setValue("/AUTOSAR/Spn1"))
        mapping.setSystemSignalRef(RefType().setValue("/AUTOSAR/SystemSignal1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticJ1939SpnMapping(parent, mapping)

        child = parent.find("DIAGNOSTIC-J-1939-SPN-MAPPING")
        assert [c.tag for c in child] == ["SHORT-NAME", "SENDING-NODE-REFS", "SPN-REF", "SYSTEM-SIGNAL-REF"]
        assert child.find("SENDING-NODE-REFS/SENDING-NODE-REF").text == "/AUTOSAR/SendingNode1"
        assert child.find("SPN-REF").text == "/AUTOSAR/Spn1"
        assert child.find("SYSTEM-SIGNAL-REF").text == "/AUTOSAR/SystemSignal1"
