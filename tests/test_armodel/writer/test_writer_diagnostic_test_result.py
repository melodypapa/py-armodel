"""
Tests for writing DIAGNOSTIC-TEST-RESULT elements —
DiagnosticTestResult, Table 4.201 (p.204, R23-11).

The XSD group DIAGNOSTIC-TEST-RESULT (AUTOSAR_00052.xsd l.45943) fixes the
element order DIAGNOSTIC-EVENTS, MONITORED-IDENTIFIER-REF, TEST-IDENTIFIER,
UPDATE-KIND. diagnosticEvent (0..1 ref, atpSplitable; atpVariation) is modeled
as the optional diagnosticEventRef (PDF Mult column wins over the unbounded
splitable wrapper, EventHandler.eventMulticastAddressRef precedent): the
DIAGNOSTIC-EVENTS wrapper with its DIAGNOSTIC-EVENT-REF-CONDITIONAL item is
emitted only when the reference is set (sdClientTimerConfig single-shape
precedent). TEST-IDENTIFIER carries the nested DiagnosticTestIdentifier
children ID/UAS-ID. The dispatch entry is writeARPackageElement →
writeDiagnosticElement → writeDiagnosticTestResult.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_test_result.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticTestIdentifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticTestResult
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DiagnosticTestResultUpdateEnum,
    PositiveInteger,
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_identifier(id_value: int, uas_id_value: int) -> DiagnosticTestIdentifier:
    identifier = DiagnosticTestIdentifier()
    identifier_id = PositiveInteger()
    identifier_id.setValue(id_value)
    identifier.setId(identifier_id)
    uas_id = PositiveInteger()
    uas_id.setValue(uas_id_value)
    identifier.setUasId(uas_id)
    return identifier


def _populate(test_result: DiagnosticTestResult) -> DiagnosticTestResult:
    test_result.setDiagnosticEventRef(RefType().setDest("DIAGNOSTIC-EVENT").setValue("/AUTOSAR/DiagnosticEvents/Event1"))
    test_result.setMonitoredIdentifierRef(RefType().setDest("DIAGNOSTIC-MEASUREMENT-IDENTIFIER").setValue("/AUTOSAR/DiagnosticMeasurementIdentifiers/Mid1"))
    test_result.setTestIdentifier(_make_identifier(4, 300))
    update_kind = DiagnosticTestResultUpdateEnum()
    update_kind.setValue(DiagnosticTestResultUpdateEnum.STEADY)
    test_result.setUpdateKind(update_kind)
    return test_result


class TestWriteDiagnosticTestResult:
    """Tests for writeDiagnosticTestResult — own element field values (Table 4.201)."""

    def test_write_unset_fields_emit_identifiable_only(self):
        """Test that a DiagnosticTestResult without own fields emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTestResults")
        package.createDiagnosticTestResult("TestResult1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTestResult(parent, package.getReferrableElement("TestResult1", DiagnosticTestResult))

        child = parent.find("DIAGNOSTIC-TEST-RESULT")
        assert child is not None
        assert child.find("SHORT-NAME").text == "TestResult1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all fields are emitted in XSD order with the spec values and DEST attributes."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTestResults")
        test_result = _populate(package.createDiagnosticTestResult("TestResult1"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticTestResult(parent, test_result)

        child = parent.find("DIAGNOSTIC-TEST-RESULT")
        assert [c.tag for c in child] == ["SHORT-NAME", "DIAGNOSTIC-EVENTS", "MONITORED-IDENTIFIER-REF", "TEST-IDENTIFIER", "UPDATE-KIND"]
        events_tag = child.find("DIAGNOSTIC-EVENTS")
        conditional_tag = events_tag.find("DIAGNOSTIC-EVENT-REF-CONDITIONAL")
        assert conditional_tag is not None
        event_ref = conditional_tag.find("DIAGNOSTIC-EVENT-REF")
        assert event_ref.text == "/AUTOSAR/DiagnosticEvents/Event1"
        assert event_ref.get("DEST") == "DIAGNOSTIC-EVENT"
        monitored_ref = child.find("MONITORED-IDENTIFIER-REF")
        assert monitored_ref.text == "/AUTOSAR/DiagnosticMeasurementIdentifiers/Mid1"
        assert monitored_ref.get("DEST") == "DIAGNOSTIC-MEASUREMENT-IDENTIFIER"
        test_identifier = child.find("TEST-IDENTIFIER")
        assert [c.tag for c in test_identifier] == ["ID", "UAS-ID"]
        assert test_identifier.find("ID").text == "4"
        assert test_identifier.find("UAS-ID").text == "300"
        assert child.find("UPDATE-KIND").text == "STEADY"

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticTestResult to a DIAGNOSTIC-TEST-RESULT element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticTestResults")
        _populate(package.createDiagnosticTestResult("TestResult1"))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("TestResult1", DiagnosticTestResult))

        child = parent.find("DIAGNOSTIC-TEST-RESULT")
        assert child is not None
        assert child.find("SHORT-NAME").text == "TestResult1"
        assert child.find("MONITORED-IDENTIFIER-REF") is not None

    def test_round_trip_preserves_field_values(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticTestResults")
        _populate(package.createDiagnosticTestResult("TestResult1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            test_result_2 = package_2.getReferrableElement("TestResult1", DiagnosticTestResult)
            assert test_result_2 is not None
            assert test_result_2.getShortName() == "TestResult1"
            event_ref = test_result_2.getDiagnosticEventRef()
            assert event_ref is not None
            assert event_ref.getValue() == "/AUTOSAR/DiagnosticEvents/Event1"
            assert event_ref.getDest() == "DIAGNOSTIC-EVENT"
            monitored_ref = test_result_2.getMonitoredIdentifierRef()
            assert monitored_ref is not None
            assert monitored_ref.getValue() == "/AUTOSAR/DiagnosticMeasurementIdentifiers/Mid1"
            assert monitored_ref.getDest() == "DIAGNOSTIC-MEASUREMENT-IDENTIFIER"
            test_identifier = test_result_2.getTestIdentifier()
            assert test_identifier is not None
            assert test_identifier.getId() is not None
            assert test_identifier.getId().getValue() == 4
            assert test_identifier.getUasId() is not None
            assert test_identifier.getUasId().getValue() == 300
            update_kind = test_result_2.getUpdateKind()
            assert update_kind is not None
            assert update_kind.getValue() == DiagnosticTestResultUpdateEnum.STEADY
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticTestResult without own fields round-trips with all fields unset (no wrappers)."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticTestResults")
        package.createDiagnosticTestResult("TestResult1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            test_result_2 = package_2.getReferrableElement("TestResult1", DiagnosticTestResult)
            assert test_result_2 is not None
            assert test_result_2.getDiagnosticEventRef() is None
            assert test_result_2.getMonitoredIdentifierRef() is None
            assert test_result_2.getTestIdentifier() is None
            assert test_result_2.getUpdateKind() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
