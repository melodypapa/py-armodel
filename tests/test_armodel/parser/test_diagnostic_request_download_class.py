"""
Tests for reading the DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS element —
DiagnosticRequestDownloadClass, Table 4.122 (p.145, R23-11).

DiagnosticRequestDownloadClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — the R23-11 table's attribute row is `-`
and XSD group DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS, AUTOSAR_00052.xsd l.41843, is an
empty sequence. Only the IDENTIFIABLE wrapper is read. The dispatch entry is
readARPackageElementsRest → readDiagnosticRequestDownloadClass via the ARPackage
create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_download_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestDownloadClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRequestDownloadClass:
    """Tests for readDiagnosticRequestDownloadClass — own element field values (Table 4.122)."""

    def _read(self, parser, inner):
        request_download_class = DiagnosticRequestDownloadClass(AUTOSAR.getInstance(), "Rqd1")
        element = _snip(inner, root_tag="DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS")
        parser.readDiagnosticRequestDownloadClass(element, request_download_class)
        return request_download_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        request_download_class = self._read(parser, "<SHORT-NAME>Rqd1</SHORT-NAME>")
        assert request_download_class.getShortName() == "Rqd1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        request_download_class = self._read(parser, "")
        assert request_download_class.getShortName() == "Rqd1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestDownloadClasses")
        element = _snip("<SHORT-NAME>Rqd1</SHORT-NAME>", root_tag="DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS", element, package)
        assert package.getReferrableElement("Rqd1", DiagnosticRequestDownloadClass) is not None
