"""
Tests for reading the DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS element —
DiagnosticRequestFileTransferClass, Table 4.126 (p.147, R23-11).

DiagnosticRequestFileTransferClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — the R23-11 table's attribute row is `-`
and XSD group DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS, AUTOSAR_00052.xsd l.42092,
is an empty sequence. Only the IDENTIFIABLE wrapper is read. The dispatch entry
is readARPackageElementsRest → readDiagnosticRequestFileTransferClass via the
ARPackage create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_file_transfer_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestFileTransferClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRequestFileTransferClass:
    """Tests for readDiagnosticRequestFileTransferClass — own element field values (Table 4.126)."""

    def _read(self, parser, inner):
        request_file_transfer_class = DiagnosticRequestFileTransferClass(AUTOSAR.getInstance(), "Rqf1")
        element = _snip(inner, root_tag="DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS")
        parser.readDiagnosticRequestFileTransferClass(element, request_file_transfer_class)
        return request_file_transfer_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        request_file_transfer_class = self._read(parser, "<SHORT-NAME>Rqf1</SHORT-NAME>")
        assert request_file_transfer_class.getShortName() == "Rqf1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        request_file_transfer_class = self._read(parser, "")
        assert request_file_transfer_class.getShortName() == "Rqf1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestFileTransferClasses")
        element = _snip("<SHORT-NAME>Rqf1</SHORT-NAME>", root_tag="DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS", element, package)
        assert package.getReferrableElement("Rqf1", DiagnosticRequestFileTransferClass) is not None
