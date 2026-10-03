"""
Tests for writing DIAGNOSTIC-DATA-TRANSFER elements —
DiagnosticDataTransfer, Table 4.117 (p.143, R23-11).

DiagnosticDataTransfer (Base most-derived DiagnosticMemoryByAddress) owns one 0..1
reference transferExitClass (DATA-TRANSFER-CLASS-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-DATA-TRANSFER l.34573: DATA-TRANSFER-CLASS-REF.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_data_transfer.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataTransfer
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


def _make_full_data_transfer() -> DiagnosticDataTransfer:
    package = AUTOSAR.getInstance().createARPackage("DiagnosticDataTransferServices")
    data_transfer = package.createDiagnosticDataTransfer("DataTransfer1")
    data_transfer.setDataTransferClassRef(RefType().setDest("DIAGNOSTIC-DATA-TRANSFER-CLASS").setValue("/AUTOSAR/DiagnosticDataTransferClasses/Class1"))
    return data_transfer


class TestWriteDiagnosticDataTransfer:
    """Tests for writeDiagnosticDataTransfer — own element field values (Table 4.117)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticDataTransfer without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDataTransferServices")
        package.createDiagnosticDataTransfer("DataTransfer1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataTransfer(parent, package.getReferrableElement("DataTransfer1", DiagnosticDataTransfer))

        child = parent.find("DIAGNOSTIC-DATA-TRANSFER")
        assert child is not None
        assert child.find("SHORT-NAME").text == "DataTransfer1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        data_transfer = _make_full_data_transfer()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDataTransfer(parent, data_transfer)

        child = parent.find("DIAGNOSTIC-DATA-TRANSFER")
        assert [c.tag for c in child] == ["SHORT-NAME", "DATA-TRANSFER-CLASS-REF"]
        assert child.find("DATA-TRANSFER-CLASS-REF").text == "/AUTOSAR/DiagnosticDataTransferClasses/Class1"
        assert child.find("DATA-TRANSFER-CLASS-REF").get("DEST") == "DIAGNOSTIC-DATA-TRANSFER-CLASS"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        data_transfer = _make_full_data_transfer()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticDataTransfer(parent, data_transfer)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticDataTransfer(AUTOSAR.getInstance(), "DataTransfer1")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-DATA-TRANSFER")
        ARXMLParser().readDiagnosticDataTransfer(element, reloaded)
        assert reloaded.getDataTransferClassRef() is not None
        assert reloaded.getDataTransferClassRef().getValue() == "/AUTOSAR/DiagnosticDataTransferClasses/Class1"
        assert reloaded.getDataTransferClassRef().getDest() == "DIAGNOSTIC-DATA-TRANSFER-CLASS"
