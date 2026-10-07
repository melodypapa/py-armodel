"""Parser tests for DiagnosticTestResult (Table 4.201, p.204).

XSD group DIAGNOSTIC-TEST-RESULT (AUTOSAR_00052.xsd l.45943) element order:
DIAGNOSTIC-EVENTS (DIAGNOSTIC-EVENT-REF-CONDITIONAL/DIAGNOSTIC-EVENT-REF),
MONITORED-IDENTIFIER-REF, TEST-IDENTIFIER (ID, UAS-ID), UPDATE-KIND; the XSD
EVENT-REF element carries atp.Status="removed" and is not modeled (Rule 0015).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_test_result.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTestResult

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-TEST-RESULT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticTestResult:
    def test_read_sets_all_fields(self, parser):
        """Test that all four own fields are populated from the XSD element order."""
        test_result = DiagnosticTestResult(AUTOSAR.getInstance(), "TestResult1")
        element = _snip(
            "<SHORT-NAME>TestResult1</SHORT-NAME>"
            "<DIAGNOSTIC-EVENTS><DIAGNOSTIC-EVENT-REF-CONDITIONAL><DIAGNOSTIC-EVENT-REF DEST='DIAGNOSTIC-EVENT'>/AUTOSAR/DiagnosticEvents/Event1</DIAGNOSTIC-EVENT-REF></DIAGNOSTIC-EVENT-REF-CONDITIONAL></DIAGNOSTIC-EVENTS>"
            "<MONITORED-IDENTIFIER-REF DEST='DIAGNOSTIC-MEASUREMENT-IDENTIFIER'>/AUTOSAR/DiagnosticMeasurementIdentifiers/Mid1</MONITORED-IDENTIFIER-REF>"
            "<TEST-IDENTIFIER><ID>4</ID><UAS-ID>300</UAS-ID></TEST-IDENTIFIER>"
            "<UPDATE-KIND>STEADY</UPDATE-KIND>"
        )

        parser.readDiagnosticTestResult(element, test_result)

        assert test_result.getShortName() == "TestResult1"
        assert test_result.getDiagnosticEventRef() is not None
        assert test_result.getDiagnosticEventRef().getValue() == "/AUTOSAR/DiagnosticEvents/Event1"
        assert test_result.getDiagnosticEventRef().getDest() == "DIAGNOSTIC-EVENT"
        assert test_result.getMonitoredIdentifierRef() is not None
        assert test_result.getMonitoredIdentifierRef().getValue() == "/AUTOSAR/DiagnosticMeasurementIdentifiers/Mid1"
        assert test_result.getMonitoredIdentifierRef().getDest() == "DIAGNOSTIC-MEASUREMENT-IDENTIFIER"
        assert test_result.getTestIdentifier() is not None
        assert test_result.getTestIdentifier().getId() is not None
        assert test_result.getTestIdentifier().getId().getValue() == 4
        assert test_result.getTestIdentifier().getUasId() is not None
        assert test_result.getTestIdentifier().getUasId().getValue() == 300
        assert test_result.getUpdateKind() is not None
        assert test_result.getUpdateKind().getValue() == "STEADY"

    def test_read_empty(self, parser):
        """Test that a bare element leaves all own fields unset."""
        test_result = DiagnosticTestResult(AUTOSAR.getInstance(), "TestResult1")
        element = _snip("<SHORT-NAME>TestResult1</SHORT-NAME>")

        parser.readDiagnosticTestResult(element, test_result)

        assert test_result.getDiagnosticEventRef() is None
        assert test_result.getMonitoredIdentifierRef() is None
        assert test_result.getTestIdentifier() is None
        assert test_result.getUpdateKind() is None
