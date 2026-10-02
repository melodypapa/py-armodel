"""
Tests for writing DIAGNOSTIC-TRANSFER-EXIT elements —
DiagnosticTransferExit, Table 4.117 (p.143, R23-11).

DiagnosticTransferExit (Base most-derived DiagnosticMemoryByAddress) owns one 0..1
reference transferExitClass (TRANSFER-EXIT-CLASS-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-TRANSFER-EXIT l.46110: TRANSFER-EXIT-CLASS-REF.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_transfer_exit.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTransferExit
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_full_transfer_exit() -> DiagnosticTransferExit:
    package = AUTOSAR.getInstance().createARPackage("DiagnosticTransferExitServices")
    transfer_exit = package.createDiagnosticTransferExit("TransferExit1")
    transfer_exit.setTransferExitClassRef(RefType().setDest("DIAGNOSTIC-TRANSFER-EXIT-CLASS").setValue("/AUTOSAR/DiagnosticTransferExitClasses/Class1"))
    return transfer_exit


class TestWriteDiagnosticTransferExit:
    """Tests for writeDiagnosticTransferExit — own element field values (Table 4.117)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticTransferExit without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTransferExitServices")
        package.createDiagnosticTransferExit("TransferExit1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTransferExit(parent, package.getReferrableElement("TransferExit1", DiagnosticTransferExit))

        child = parent.find("DIAGNOSTIC-TRANSFER-EXIT")
        assert child is not None
        assert child.find("SHORT-NAME").text == "TransferExit1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        transfer_exit = _make_full_transfer_exit()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTransferExit(parent, transfer_exit)

        child = parent.find("DIAGNOSTIC-TRANSFER-EXIT")
        assert [c.tag for c in child] == ["SHORT-NAME", "TRANSFER-EXIT-CLASS-REF"]
        assert child.find("TRANSFER-EXIT-CLASS-REF").text == "/AUTOSAR/DiagnosticTransferExitClasses/Class1"
        assert child.find("TRANSFER-EXIT-CLASS-REF").get("DEST") == "DIAGNOSTIC-TRANSFER-EXIT-CLASS"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        transfer_exit = _make_full_transfer_exit()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticTransferExit(parent, transfer_exit)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticTransferExit(AUTOSAR.getInstance(), "TransferExit1")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-TRANSFER-EXIT")
        ARXMLParser().readDiagnosticTransferExit(element, reloaded)
        assert reloaded.getTransferExitClassRef() is not None
        assert reloaded.getTransferExitClassRef().getValue() == "/AUTOSAR/DiagnosticTransferExitClasses/Class1"
        assert reloaded.getTransferExitClassRef().getDest() == "DIAGNOSTIC-TRANSFER-EXIT-CLASS"
