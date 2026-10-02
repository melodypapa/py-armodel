"""
Tests for writing DIAGNOSTIC-REQUEST-FILE-TRANSFER elements —
DiagnosticRequestFileTransfer, Table 4.125 (p.147, R23-11).

DiagnosticRequestFileTransfer (Base most-derived ARElement) owns one 0..1
reference requestFileTransferClass (REQUEST-FILE-TRANSFER-CLASS-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-REQUEST-FILE-TRANSFER l.42045: REQUEST-FILE-TRANSFER-CLASS-REF.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_file_transfer.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestFileTransfer
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


def _make_full_request_file_transfer() -> DiagnosticRequestFileTransfer:
    package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestFileTransferServices")
    request_file_transfer = package.createDiagnosticRequestFileTransfer("RequestFileTransfer1")
    request_file_transfer.setRequestFileTransferClassRef(RefType().setDest("DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS").setValue("/AUTOSAR/DiagnosticRequestFileTransferClasses/Class1"))
    return request_file_transfer


class TestWriteDiagnosticRequestFileTransfer:
    """Tests for writeDiagnosticRequestFileTransfer — own element field values (Table 4.125)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticRequestFileTransfer without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestFileTransferServices")
        package.createDiagnosticRequestFileTransfer("RequestFileTransfer1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestFileTransfer(parent, package.getReferrableElement("RequestFileTransfer1", DiagnosticRequestFileTransfer))

        child = parent.find("DIAGNOSTIC-REQUEST-FILE-TRANSFER")
        assert child is not None
        assert child.find("SHORT-NAME").text == "RequestFileTransfer1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        request_file_transfer = _make_full_request_file_transfer()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestFileTransfer(parent, request_file_transfer)

        child = parent.find("DIAGNOSTIC-REQUEST-FILE-TRANSFER")
        assert [c.tag for c in child] == ["SHORT-NAME", "REQUEST-FILE-TRANSFER-CLASS-REF"]
        assert child.find("REQUEST-FILE-TRANSFER-CLASS-REF").text == "/AUTOSAR/DiagnosticRequestFileTransferClasses/Class1"
        assert child.find("REQUEST-FILE-TRANSFER-CLASS-REF").get("DEST") == "DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        request_file_transfer = _make_full_request_file_transfer()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticRequestFileTransfer(parent, request_file_transfer)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticRequestFileTransfer(AUTOSAR.getInstance(), "RequestFileTransfer1")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-FILE-TRANSFER")
        ARXMLParser().readDiagnosticRequestFileTransfer(element, reloaded)
        assert reloaded.getRequestFileTransferClassRef() is not None
        assert reloaded.getRequestFileTransferClassRef().getValue() == "/AUTOSAR/DiagnosticRequestFileTransferClasses/Class1"
        assert reloaded.getRequestFileTransferClassRef().getDest() == "DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS"
