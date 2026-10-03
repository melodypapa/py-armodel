"""
Tests for reading the DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS
element — DiagnosticRequestOnBoardMonitoringTestResultsClass, Table 4.140 (p.157,
R23-11).

DiagnosticRequestOnBoardMonitoringTestResultsClass (Base most-derived
DiagnosticServiceClass, concrete) defines no own attributes — the R23-11 table's
attribute row is `-` and XSD group
DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS, AUTOSAR_00052.xsd
l.42270, is an empty sequence. Only the IDENTIFIABLE wrapper is read. The
dispatch entry is readARPackageElementsRest →
readDiagnosticRequestOnBoardMonitoringTestResultsClass via the ARPackage create
factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_on_board_monitoring_test_results_class.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestOnBoardMonitoringTestResultsClass
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticRequestOnBoardMonitoringTestResultsClass:
    """Tests for readDiagnosticRequestOnBoardMonitoringTestResultsClass — own element field values (Table 4.140)."""

    def _read(self, parser, inner):
        request_on_board_monitoring_test_results_class = DiagnosticRequestOnBoardMonitoringTestResultsClass(AUTOSAR.getInstance(), "Obd061")
        element = _snip(inner, root_tag="DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS")
        parser.readDiagnosticRequestOnBoardMonitoringTestResultsClass(element, request_on_board_monitoring_test_results_class)
        return request_on_board_monitoring_test_results_class

    def test_read_identifiable_wrapper(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name comes from the dispatch constructor)."""
        request_on_board_monitoring_test_results_class = self._read(parser, "<SHORT-NAME>Obd061</SHORT-NAME>")
        assert request_on_board_monitoring_test_results_class.getShortName() == "Obd061"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the element valid."""
        request_on_board_monitoring_test_results_class = self._read(parser, "")
        assert request_on_board_monitoring_test_results_class.getShortName() == "Obd061"

    def test_arpackage_dispatch_reads_element(self, parser):
        """Test that readARPackageElementsRest dispatches DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS through the ARPackage create factory."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode06Classes")
        element = _snip("<SHORT-NAME>Obd061</SHORT-NAME>", root_tag="DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS")
        parser.readARPackageElementsRest("DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS", element, package)
        assert package.getReferrableElement("Obd061", DiagnosticRequestOnBoardMonitoringTestResultsClass) is not None
