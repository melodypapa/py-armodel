"""
Tests for reading the DIAGNOSTIC-EVENT element —
DiagnosticEvent, Table 4.149 (p.165, R23-11).

DiagnosticEvent (Base most-derived ARElement) carries nine own Attribute rows;
the XSD group DIAGNOSTIC-EVENT (AUTOSAR_00052.xsd l.36166) fixes the element
order ASSOCIATED-EVENT-IDENTIFICATION → CLEAR-EVENT-ALLOWED-BEHAVIOR →
CONFIRMATION-THRESHOLD (POSITIVE-INTEGER-VALUE-VARIATION-POINT wrapper) →
CONNECTED-INDICATORS (wrapper of DIAGNOSTIC-CONNECTED-INDICATOR) →
EVENT-CLEAR-ALLOWED → EVENT-KIND → PRESTORAGE-FREEZE-FRAME →
PRESTORED-FREEZEFRAME-STORED-IN-NVM → RECOVERABLE-IN-SAME-OPERATION-CYCLE.

EVENT-CLEAR-ALLOWED round-trips as the typed DiagnosticEventClearAllowedEnum
(Table 4.153) literal; EVENT-KIND round-trips as the typed DiagnosticEventKindEnum
(Table 4.154) literal.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_event.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticEventClearAllowedEnum, DiagnosticEventKindEnum
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticEvent:
    """Tests for readDiagnosticEvent — own element field values (Table 4.149)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEvent

        event = DiagnosticEvent(AUTOSAR.getInstance(), "Event1")
        parser.readDiagnosticEvent(_snip(inner, root_tag="DIAGNOSTIC-EVENT"), event)
        return event

    def test_read_sets_associated_event_identification(self, parser):
        """Test that ASSOCIATED-EVENT-IDENTIFICATION is read into associatedEventIdentification."""
        event = self._read(parser, "<SHORT-NAME>Event1</SHORT-NAME><ASSOCIATED-EVENT-IDENTIFICATION>3</ASSOCIATED-EVENT-IDENTIFICATION>")
        assert event.getShortName() == "Event1"
        assert event.getAssociatedEventIdentification() is not None
        assert event.getAssociatedEventIdentification().value == 3

    def test_read_sets_clear_event_allowed_behavior(self, parser):
        """Test that the CLEAR-EVENT-ALLOWED-BEHAVIOR token is read as the typed enum literal."""
        event = self._read(parser, "<CLEAR-EVENT-ALLOWED-BEHAVIOR>NO-STATUS-BYTE-CHANGE</CLEAR-EVENT-ALLOWED-BEHAVIOR>")
        assert event.getClearEventAllowedBehavior() is not None
        assert event.getClearEventAllowedBehavior().getValue() == "NO-STATUS-BYTE-CHANGE"

    def test_read_sets_confirmation_threshold_variation_point(self, parser):
        """Test that the CONFIRMATION-THRESHOLD value inside the POSITIVE-INTEGER-VALUE-VARIATION-POINT wrapper is read."""
        event = self._read(parser, "<CONFIRMATION-THRESHOLD><POSITIVE-INTEGER-VALUE-VARIATION-POINT>2</POSITIVE-INTEGER-VALUE-VARIATION-POINT></CONFIRMATION-THRESHOLD>")
        assert event.getConfirmationThreshold() is not None
        assert event.getConfirmationThreshold().value == 2

    def test_read_sets_connected_indicators(self, parser):
        """Test that the CONNECTED-INDICATORS wrapper items are read into the connectedIndicators list."""
        event = self._read(
            parser,
            "<CONNECTED-INDICATORS>"
            '<DIAGNOSTIC-CONNECTED-INDICATOR><INDICATOR-REF DEST="DIAGNOSTIC-INDICATOR-REF">/DiagnosticExtract/Indicator1</INDICATOR-REF></DIAGNOSTIC-CONNECTED-INDICATOR>'
            '<DIAGNOSTIC-CONNECTED-INDICATOR><INDICATOR-REF DEST="DIAGNOSTIC-INDICATOR-REF">/DiagnosticExtract/Indicator2</INDICATOR-REF></DIAGNOSTIC-CONNECTED-INDICATOR>'
            "</CONNECTED-INDICATORS>",
        )
        indicators = event.getConnectedIndicators()
        assert len(indicators) == 2
        assert indicators[0].getIndicatorRef().getValue() == "/DiagnosticExtract/Indicator1"
        assert indicators[1].getIndicatorRef().getValue() == "/DiagnosticExtract/Indicator2"

    def test_read_sets_event_clear_allowed(self, parser):
        """Test that the EVENT-CLEAR-ALLOWED token is read as the typed enum literal."""
        event = self._read(parser, "<EVENT-CLEAR-ALLOWED>ALWAYS</EVENT-CLEAR-ALLOWED>")
        assert event.getEventClearAllowed() is not None
        assert isinstance(event.getEventClearAllowed(), DiagnosticEventClearAllowedEnum)
        assert event.getEventClearAllowed().getValue() == "ALWAYS"

    def test_read_sets_event_kind(self, parser):
        """Test that the EVENT-KIND token is read as the typed enum literal."""
        event = self._read(parser, "<EVENT-KIND>BSW</EVENT-KIND>")
        assert event.getEventKind() is not None
        assert isinstance(event.getEventKind(), DiagnosticEventKindEnum)
        assert event.getEventKind().getValue() == DiagnosticEventKindEnum.BSW

    def test_read_sets_boolean_attributes(self, parser):
        """Test that the three BOOLEAN attributes are read into their fields."""
        event = self._read(
            parser,
            "<PRESTORAGE-FREEZE-FRAME>true</PRESTORAGE-FREEZE-FRAME>"
            "<PRESTORED-FREEZEFRAME-STORED-IN-NVM>false</PRESTORED-FREEZEFRAME-STORED-IN-NVM>"
            "<RECOVERABLE-IN-SAME-OPERATION-CYCLE>true</RECOVERABLE-IN-SAME-OPERATION-CYCLE>",
        )
        assert event.getPrestorageFreezeFrame() is not None
        assert event.getPrestorageFreezeFrame().value is True
        assert event.getPrestoredFreezeframeStoredInNvm() is not None
        assert event.getPrestoredFreezeframeStoredInNvm().value is False
        assert event.getRecoverableInSameOperationCycle() is not None
        assert event.getRecoverableInSameOperationCycle().value is True

    def test_read_empty_leaves_fields_unset(self, parser):
        """Test that an element without own children leaves every field unset and the list empty (empty wrapper case)."""
        event = self._read(parser, "<SHORT-NAME>Event1</SHORT-NAME>")
        assert event.getAssociatedEventIdentification() is None
        assert event.getClearEventAllowedBehavior() is None
        assert event.getConfirmationThreshold() is None
        assert event.getConnectedIndicators() == []
        assert event.getEventClearAllowed() is None
        assert event.getEventKind() is None
        assert event.getPrestorageFreezeFrame() is None
        assert event.getPrestoredFreezeframeStoredInNvm() is None
        assert event.getRecoverableInSameOperationCycle() is None
