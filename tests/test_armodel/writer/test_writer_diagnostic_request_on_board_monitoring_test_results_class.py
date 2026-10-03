"""
Tests for writing the DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS
element — DiagnosticRequestOnBoardMonitoringTestResultsClass, Table 4.140 (p.157,
R23-11).

DiagnosticRequestOnBoardMonitoringTestResultsClass (Base most-derived
DiagnosticServiceClass) defines no own attributes; the writer emits the
IDENTIFIABLE wrapper only, and the dispatch entry is writeARPackageElementRest →
writeDiagnosticRequestOnBoardMonitoringTestResultsClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_request_on_board_monitoring_test_results_class.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticRequestOnBoardMonitoringTestResultsClass
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticRequestOnBoardMonitoringTestResultsClass:
    """Tests for writeDiagnosticRequestOnBoardMonitoringTestResultsClass — own element field values (Table 4.140)."""

    def test_write_emits_identifiable_wrapper(self):
        """Test that writing emits the DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS wrapper with the SHORT-NAME."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode06Classes")
        package.createDiagnosticRequestOnBoardMonitoringTestResultsClass("Obd061")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticRequestOnBoardMonitoringTestResultsClass(parent, package.getReferrableElement("Obd061", DiagnosticRequestOnBoardMonitoringTestResultsClass))

        child = parent.find("DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Obd061"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_round_trip_preserves_element(self):
        """Test the write → serialize → re-parse → read-back cycle preserving the element."""
        package = AUTOSAR.getInstance().createARPackage("OBDMode06Classes")
        package.createDiagnosticRequestOnBoardMonitoringTestResultsClass("Obd061")

        parent = ET.Element("PARENT", {"xmlns": "http://autosar.org/schema/r4.0"})
        ARXMLWriter().writeARPackageElementRest(parent, package.getReferrableElement("Obd061", DiagnosticRequestOnBoardMonitoringTestResultsClass))
        xml_text = ET.tostring(parent, encoding="unicode")

        parser = ARXMLParser()
        reloaded_package = AUTOSAR.getInstance().createARPackage("Reloaded")
        element = ET.fromstring(xml_text)
        parser.readARPackageElementsRest(
            "DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS", element.find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS"), reloaded_package
        )
        reloaded = reloaded_package.getReferrableElement("Obd061", DiagnosticRequestOnBoardMonitoringTestResultsClass)
        assert reloaded is not None
        assert reloaded.getShortName() == "Obd061"
