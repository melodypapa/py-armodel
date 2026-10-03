"""
Tests for writing DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS elements —
DiagnosticRequestOnBoardMonitoringTestResults, Table 4.139 (p.156, R23-11).

DiagnosticRequestOnBoardMonitoringTestResults (Base most-derived
DiagnosticServiceInstance) owns the * aggregation diagnosticTestResult
(DIAGNOSTIC-TEST-RESULT-REFS wrapper, unbounded DIAGNOSTIC-TEST-RESULT-REF items)
and the 0..1 reference requestOnBoardMonitoringTestResultsClass
(REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS-REF), AUTOSAR_00052.xsd group
DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS l.42191.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_on_board_monitoring_test_results.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestOnBoardMonitoringTestResults
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


def _make_full_mode06() -> DiagnosticRequestOnBoardMonitoringTestResults:
    package = AUTOSAR.getInstance().createARPackage("OBDMode06Services")
    mode06 = package.createDiagnosticRequestOnBoardMonitoringTestResults("Mode06")
    mode06.addDiagnosticTestResultRef(RefType().setDest("DIAGNOSTIC-TEST-RESULT").setValue("/AUTOSAR/DiagnosticTestResults/Test1"))
    mode06.setRequestOnBoardMonitoringTestResultsClassRef(
        RefType().setDest("DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS").setValue("/AUTOSAR/DiagnosticRequestOnBoardMonitoringTestResultsClasses/Class1")
    )
    return mode06


class TestWriteDiagnosticRequestOnBoardMonitoringTestResults:
    """Tests for writeDiagnosticRequestOnBoardMonitoringTestResults — own element field values (Table 4.139)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticRequestOnBoardMonitoringTestResults without fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode06Services")
        package.createDiagnosticRequestOnBoardMonitoringTestResults("Mode06")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestOnBoardMonitoringTestResults(parent, package.getReferrableElement("Mode06", DiagnosticRequestOnBoardMonitoringTestResults))

        child = parent.find("DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Mode06"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_empty_refs_emit_no_wrapper(self):
        """Test that an empty diagnosticTestResultRefs list emits no DIAGNOSTIC-TEST-RESULT-REFS wrapper element."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode06Services")
        mode06 = package.createDiagnosticRequestOnBoardMonitoringTestResults("Mode06")
        mode06.setRequestOnBoardMonitoringTestResultsClassRef(
            RefType().setDest("DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS").setValue("/AUTOSAR/DiagnosticRequestOnBoardMonitoringTestResultsClasses/Class1")
        )

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestOnBoardMonitoringTestResults(parent, mode06)

        child = parent.find("DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS")
        assert [c.tag for c in child] == ["SHORT-NAME", "REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS-REF"]
        assert child.find("DIAGNOSTIC-TEST-RESULT-REFS") is None

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values."""
        mode06 = _make_full_mode06()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestOnBoardMonitoringTestResults(parent, mode06)

        child = parent.find("DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS")
        assert [c.tag for c in child] == ["SHORT-NAME", "DIAGNOSTIC-TEST-RESULT-REFS", "REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS-REF"]
        test_result_refs = child.find("DIAGNOSTIC-TEST-RESULT-REFS")
        assert [c.tag for c in test_result_refs] == ["DIAGNOSTIC-TEST-RESULT-REF"]
        assert test_result_refs.find("DIAGNOSTIC-TEST-RESULT-REF").text == "/AUTOSAR/DiagnosticTestResults/Test1"
        assert test_result_refs.find("DIAGNOSTIC-TEST-RESULT-REF").get("DEST") == "DIAGNOSTIC-TEST-RESULT"
        assert child.find("REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS-REF").text == "/AUTOSAR/DiagnosticRequestOnBoardMonitoringTestResultsClasses/Class1"
        assert child.find("REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS-REF").get("DEST") == "DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS"

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the field values."""
        mode06 = _make_full_mode06()

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeDiagnosticRequestOnBoardMonitoringTestResults(parent, mode06)
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = DiagnosticRequestOnBoardMonitoringTestResults(AUTOSAR.getInstance(), "Mode06")
        element = ET.fromstring(xml_text).find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS")
        ARXMLParser().readDiagnosticRequestOnBoardMonitoringTestResults(element, reloaded)
        refs = reloaded.getDiagnosticTestResultRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/AUTOSAR/DiagnosticTestResults/Test1"
        assert refs[0].getDest() == "DIAGNOSTIC-TEST-RESULT"
        assert reloaded.getRequestOnBoardMonitoringTestResultsClassRef() is not None
        assert reloaded.getRequestOnBoardMonitoringTestResultsClassRef().getValue() == "/AUTOSAR/DiagnosticRequestOnBoardMonitoringTestResultsClasses/Class1"
        assert reloaded.getRequestOnBoardMonitoringTestResultsClassRef().getDest() == "DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS"
