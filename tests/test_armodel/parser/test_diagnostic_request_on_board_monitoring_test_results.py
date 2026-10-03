"""Parser tests for DiagnosticRequestOnBoardMonitoringTestResults (Table 4.139, p.156).

XSD group DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS (AUTOSAR_00052.xsd
l.42191) element order: DIAGNOSTIC-TEST-RESULT-REFS (wrapper, unbounded
DIAGNOSTIC-TEST-RESULT-REF items), REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS-REF.
(TEST-RESULT-REF carries atp.Status="removed" — not modeled.)

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_on_board_monitoring_test_results.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestOnBoardMonitoringTestResults

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticRequestOnBoardMonitoringTestResults:
    def test_read_sets_all_fields(self, parser):
        mode06 = DiagnosticRequestOnBoardMonitoringTestResults(AUTOSAR.getInstance(), "Mode06")
        element = _snip(
            "<SHORT-NAME>Mode06</SHORT-NAME>"
            "<DIAGNOSTIC-TEST-RESULT-REFS><DIAGNOSTIC-TEST-RESULT-REF DEST='DIAGNOSTIC-TEST-RESULT'>/AUTOSAR/DiagnosticTestResults/Test1</DIAGNOSTIC-TEST-RESULT-REF></DIAGNOSTIC-TEST-RESULT-REFS>"
            "<REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS-REF DEST='DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS'>/AUTOSAR/DiagnosticRequestOnBoardMonitoringTestResultsClasses/Class1</REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS-REF>"
        )
        parser.readDiagnosticRequestOnBoardMonitoringTestResults(element, mode06)
        assert mode06.getShortName() == "Mode06"
        refs = mode06.getDiagnosticTestResultRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/AUTOSAR/DiagnosticTestResults/Test1"
        assert refs[0].getDest() == "DIAGNOSTIC-TEST-RESULT"
        assert mode06.getRequestOnBoardMonitoringTestResultsClassRef() is not None
        assert mode06.getRequestOnBoardMonitoringTestResultsClassRef().getValue() == "/AUTOSAR/DiagnosticRequestOnBoardMonitoringTestResultsClasses/Class1"
        assert mode06.getRequestOnBoardMonitoringTestResultsClassRef().getDest() == "DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS"

    def test_read_empty(self, parser):
        mode06 = DiagnosticRequestOnBoardMonitoringTestResults(AUTOSAR.getInstance(), "Mode06")
        element = _snip("<SHORT-NAME>Mode06</SHORT-NAME>")
        parser.readDiagnosticRequestOnBoardMonitoringTestResults(element, mode06)
        assert mode06.getDiagnosticTestResultRefs() == []
        assert mode06.getRequestOnBoardMonitoringTestResultsClassRef() is None
