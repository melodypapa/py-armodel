"""
Tests for reading the DIAGNOSTIC-REQUEST-UPLOAD-CLASS element —
DiagnosticRequestUploadClass, Table 4.124 (p.146, R23-11).

DiagnosticRequestUploadClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — the R23-11 table's attribute row is `-`
and XSD group DIAGNOSTIC-REQUEST-UPLOAD-CLASS, AUTOSAR_00052.xsd l.42508, is an
empty sequence. Only the IDENTIFIABLE wrapper is read. The dispatch entry is
readARPackageElementsRest → readDiagnosticRequestUploadClass via the ARPackage
create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_upload_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestUploadClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRequestUploadClass:
    """Tests for readDiagnosticRequestUploadClass — own element field values (Table 4.124)."""

    def _read(self, parser, inner):
        request_upload_class = DiagnosticRequestUploadClass(AUTOSAR.getInstance(), "Rqu1")
        element = _snip(inner, root_tag="DIAGNOSTIC-REQUEST-UPLOAD-CLASS")
        parser.readDiagnosticRequestUploadClass(element, request_upload_class)
        return request_upload_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        request_upload_class = self._read(parser, "<SHORT-NAME>Rqu1</SHORT-NAME>")
        assert request_upload_class.getShortName() == "Rqu1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        request_upload_class = self._read(parser, "")
        assert request_upload_class.getShortName() == "Rqu1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-REQUEST-UPLOAD-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticRequestUploadClasses")
        element = _snip("<SHORT-NAME>Rqu1</SHORT-NAME>", root_tag="DIAGNOSTIC-REQUEST-UPLOAD-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-REQUEST-UPLOAD-CLASS", element, package)
        assert package.getReferrableElement("Rqu1", DiagnosticRequestUploadClass) is not None
