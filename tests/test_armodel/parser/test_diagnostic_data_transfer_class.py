"""
Tests for reading the DIAGNOSTIC-DATA-TRANSFER-CLASS element —
DiagnosticDataTransferClass, Table 4.120 (p.143, R23-11).

DiagnosticDataTransferClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — the R23-11 table's attribute row is `-`
and XSD group DIAGNOSTIC-DATA-TRANSFER-CLASS, AUTOSAR_00052.xsd l.34595, is an
empty sequence. Only the IDENTIFIABLE wrapper is read. The dispatch entry is
readARPackageElementsRest → readDiagnosticDataTransferClass via the ARPackage
create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_data_transfer_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticDataTransferClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticDataTransferClass:
    """Tests for readDiagnosticDataTransferClass — own element field values (Table 4.118)."""

    def _read(self, parser, inner):
        data_transfer_class = DiagnosticDataTransferClass(AUTOSAR.getInstance(), "Tea1")
        element = _snip(inner, root_tag="DIAGNOSTIC-DATA-TRANSFER-CLASS")
        parser.readDiagnosticDataTransferClass(element, data_transfer_class)
        return data_transfer_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        data_transfer_class = self._read(parser, "<SHORT-NAME>Tea1</SHORT-NAME>")
        assert data_transfer_class.getShortName() == "Tea1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        data_transfer_class = self._read(parser, "")
        assert data_transfer_class.getShortName() == "Tea1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-DATA-TRANSFER-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticDataTransferClasses")
        element = _snip("<SHORT-NAME>Tea1</SHORT-NAME>", root_tag="DIAGNOSTIC-DATA-TRANSFER-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-DATA-TRANSFER-CLASS", element, package)
        assert package.getReferrableElement("Tea1", DiagnosticDataTransferClass) is not None
