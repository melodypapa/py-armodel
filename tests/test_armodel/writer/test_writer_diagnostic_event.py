"""
Tests for writing DIAGNOSTIC-EVENT elements —
DiagnosticEvent, Table 4.149 (p.165, R23-11).

The XSD group DIAGNOSTIC-EVENT (AUTOSAR_00052.xsd l.36166) fixes the element
order ASSOCIATED-EVENT-IDENTIFICATION → CLEAR-EVENT-ALLOWED-BEHAVIOR →
CONFIRMATION-THRESHOLD (POSITIVE-INTEGER-VALUE-VARIATION-POINT wrapper) →
CONNECTED-INDICATORS (wrapper of DIAGNOSTIC-CONNECTED-INDICATOR) →
EVENT-CLEAR-ALLOWED → EVENT-KIND → PRESTORAGE-FREEZE-FRAME →
PRESTORED-FREEZEFRAME-STORED-IN-NVM → RECOVERABLE-IN-SAME-OPERATION-CYCLE.
The dispatch entry is writeARPackageElement → writeDiagnosticEvent.

EVENT-CLEAR-ALLOWED round-trips as the typed DiagnosticEventClearAllowedEnum
(Table 4.153) literal; EVENT-KIND still round-trips as a raw literal until
DiagnosticEventKindEnum (Table 4.154) gains its literals (queued in Group25).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_event.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticConnectedIndicator
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEvent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    DiagnosticClearEventAllowedBehaviorEnum,
    DiagnosticEventClearAllowedEnum,
    DiagnosticEventKindEnum,
    PositiveInteger,
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticEvent:
    """Tests for writeDiagnosticEvent — own element field values (Table 4.149)."""

    def _make_event(self, short_name: str = "Event1") -> DiagnosticEvent:
        package = AUTOSAR.getInstance().createARPackage("DiagnosticEvents")
        return package.createDiagnosticEvent(short_name)

    def _populate(self, event: DiagnosticEvent) -> DiagnosticEvent:
        event.setAssociatedEventIdentification(PositiveInteger().setValue(3))
        event.setClearEventAllowedBehavior(DiagnosticClearEventAllowedBehaviorEnum().setValue("noStatusByteChange"))
        event.setConfirmationThreshold(PositiveInteger().setValue(2))
        indicator = DiagnosticConnectedIndicator()
        indicator.setIndicatorRef(RefType().setValue("/DiagnosticExtract/Indicator1"))
        event.addConnectedIndicator(indicator)
        event.setEventClearAllowed(DiagnosticEventClearAllowedEnum().setValue(DiagnosticEventClearAllowedEnum.ALWAYS))
        event.setEventKind(DiagnosticEventKindEnum([]).setValue("BSW"))
        event.setPrestorageFreezeFrame(Boolean().setValue(True))
        event.setPrestoredFreezeframeStoredInNvm(Boolean().setValue(False))
        event.setRecoverableInSameOperationCycle(Boolean().setValue(True))
        return event

    def test_write_all_fields_in_xsd_order(self):
        """Test that the populated fields are emitted in the XSD group element order with the spec values."""
        event = self._populate(self._make_event())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEvent(parent, event)

        child = parent.find("DIAGNOSTIC-EVENT")
        assert child is not None
        assert [c.tag for c in child] == [
            "SHORT-NAME",
            "ASSOCIATED-EVENT-IDENTIFICATION",
            "CLEAR-EVENT-ALLOWED-BEHAVIOR",
            "CONFIRMATION-THRESHOLD",
            "CONNECTED-INDICATORS",
            "EVENT-CLEAR-ALLOWED",
            "EVENT-KIND",
            "PRESTORAGE-FREEZE-FRAME",
            "PRESTORED-FREEZEFRAME-STORED-IN-NVM",
            "RECOVERABLE-IN-SAME-OPERATION-CYCLE",
        ]
        assert child.find("SHORT-NAME").text == "Event1"
        assert child.find("ASSOCIATED-EVENT-IDENTIFICATION").text == "3"
        assert child.find("CLEAR-EVENT-ALLOWED-BEHAVIOR").text == "NO-STATUS-BYTE-CHANGE"
        assert child.find("CONFIRMATION-THRESHOLD/POSITIVE-INTEGER-VALUE-VARIATION-POINT").text == "2"
        indicators = child.find("CONNECTED-INDICATORS")
        assert indicators is not None
        assert indicators[0].tag == "DIAGNOSTIC-CONNECTED-INDICATOR"
        assert indicators[0].find("INDICATOR-REF").text == "/DiagnosticExtract/Indicator1"
        assert child.find("EVENT-CLEAR-ALLOWED").text == "ALWAYS"
        assert child.find("EVENT-KIND").text == "BSW"
        assert child.find("PRESTORAGE-FREEZE-FRAME").text == "true"
        assert child.find("PRESTORED-FREEZEFRAME-STORED-IN-NVM").text == "false"
        assert child.find("RECOVERABLE-IN-SAME-OPERATION-CYCLE").text == "true"

    def test_write_unset_fields_emit_no_children(self):
        """Test that an unpopulated DiagnosticEvent emits no own children (empty wrapper case)."""
        self._make_event()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEvent(parent, AUTOSAR.getInstance().getARPackages()[0].getReferrableElement("Event1", DiagnosticEvent))

        child = parent.find("DIAGNOSTIC-EVENT")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME"]
        assert child.find("CONNECTED-INDICATORS") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticEvent to a DIAGNOSTIC-EVENT element."""
        event = self._populate(self._make_event())

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, event)

        child = parent.find("DIAGNOSTIC-EVENT")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Event1"
        assert child.find("ASSOCIATED-EVENT-IDENTIFICATION").text == "3"

    def test_round_trip_preserves_field_values(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticEvents")
        self._populate(package.createDiagnosticEvent("Event1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            event_2 = package_2.getReferrableElement("Event1", DiagnosticEvent)
            assert event_2 is not None
            assert event_2.getShortName() == "Event1"
            assert event_2.getAssociatedEventIdentification().value == 3
            assert event_2.getClearEventAllowedBehavior().getValue() == "noStatusByteChange"
            assert event_2.getConfirmationThreshold().value == 2
            indicators = event_2.getConnectedIndicators()
            assert len(indicators) == 1
            assert indicators[0].getIndicatorRef().getValue() == "/DiagnosticExtract/Indicator1"
            assert event_2.getEventClearAllowed() is not None
            assert isinstance(event_2.getEventClearAllowed(), DiagnosticEventClearAllowedEnum)
            assert event_2.getEventClearAllowed().getValue() == "always"
            assert event_2.getEventKind().getValue() == "BSW"
            assert event_2.getPrestorageFreezeFrame().value is True
            assert event_2.getPrestoredFreezeframeStoredInNvm().value is False
            assert event_2.getRecoverableInSameOperationCycle().value is True
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticEvent without own fields round-trips with unset fields and an empty list."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticEvents")
        package.createDiagnosticEvent("Event1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            event_2 = package_2.getReferrableElement("Event1", DiagnosticEvent)
            assert event_2 is not None
            assert event_2.getAssociatedEventIdentification() is None
            assert event_2.getClearEventAllowedBehavior() is None
            assert event_2.getConfirmationThreshold() is None
            assert event_2.getConnectedIndicators() == []
            assert event_2.getEventClearAllowed() is None
            assert event_2.getEventKind() is None
            assert event_2.getPrestorageFreezeFrame() is None
            assert event_2.getPrestoredFreezeframeStoredInNvm() is None
            assert event_2.getRecoverableInSameOperationCycle() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
