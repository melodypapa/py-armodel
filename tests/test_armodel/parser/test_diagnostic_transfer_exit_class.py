"""
Tests for reading the DIAGNOSTIC-TRANSFER-EXIT-CLASS element —
DiagnosticTransferExitClass, Table 4.118 (p.143, R23-11).

DiagnosticTransferExitClass (Base most-derived DiagnosticServiceClass,
concrete) defines no own attributes — the R23-11 table's attribute row is `-`
and XSD group DIAGNOSTIC-TRANSFER-EXIT-CLASS, AUTOSAR_00052.xsd l.46146, is an
empty sequence. Only the IDENTIFIABLE wrapper is read. The dispatch entry is
readARPackageElementsRest → readDiagnosticTransferExitClass via the ARPackage
create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_transfer_exit_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticTransferExitClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticTransferExitClass:
    """Tests for readDiagnosticTransferExitClass — own element field values (Table 4.118)."""

    def _read(self, parser, inner):
        transfer_exit_class = DiagnosticTransferExitClass(AUTOSAR.getInstance(), "Tea1")
        element = _snip(inner, root_tag="DIAGNOSTIC-TRANSFER-EXIT-CLASS")
        parser.readDiagnosticTransferExitClass(element, transfer_exit_class)
        return transfer_exit_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        transfer_exit_class = self._read(parser, "<SHORT-NAME>Tea1</SHORT-NAME>")
        assert transfer_exit_class.getShortName() == "Tea1"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        transfer_exit_class = self._read(parser, "")
        assert transfer_exit_class.getShortName() == "Tea1"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-TRANSFER-EXIT-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTransferExitClasses")
        element = _snip("<SHORT-NAME>Tea1</SHORT-NAME>", root_tag="DIAGNOSTIC-TRANSFER-EXIT-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-TRANSFER-EXIT-CLASS", element, package)
        assert package.getReferrableElement("Tea1", DiagnosticTransferExitClass) is not None
