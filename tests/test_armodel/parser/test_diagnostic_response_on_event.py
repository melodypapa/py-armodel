"""
Tests for reading the DIAGNOSTIC-RESPONSE-ON-EVENT element —
DiagnosticResponseOnEvent, Table 4.101 (p.132, R23-11).

DiagnosticResponseOnEvent (Base most-derived ARElement, aggregated by
ARPackage.element) owns three attributes in XSD group
DIAGNOSTIC-RESPONSE-ON-EVENT, AUTOSAR_00052.xsd l.42645: the 0..*
eventWindow aggregation (EVENT-WINDOWS wrapper of DIAGNOSTIC-EVENT-WINDOW
elements), the 0..1 responseOnEventAction attr (RESPONSE-ON-EVENT-ACTION,
DIAGNOSTIC-RESPONSE-ON-EVENT-ACTION-ENUM--SIMPLE tokens) and the 0..1
responseOnEventClass ref (RESPONSE-ON-EVENT-CLASS-REF, DEST
DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS--SUBTYPES-ENUM). The removed EVENTS and
STORE-EVENT-SUPPORT elements (atp.Status="removed") are not modeled.
The reader populates the fields via the model mutators in XSD element order.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_response_on_event.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticResponseOnEvent:
    """Tests for readDiagnosticResponseOnEvent — own element field values (Table 4.101)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticResponseOnEvent

        response_on_event = DiagnosticResponseOnEvent(parent=MagicMock(), short_name="ResponseOnEvent")
        element = _snip(inner, root_tag="DIAGNOSTIC-RESPONSE-ON-EVENT")
        parser.readDiagnosticResponseOnEvent(element, response_on_event)
        return response_on_event

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        response_on_event = self._read(parser, "<SHORT-NAME>ResponseOnEvent</SHORT-NAME>")
        assert response_on_event.getShortName() == "ResponseOnEvent"

    def test_read_event_windows(self, parser):
        """Test that the EVENT-WINDOWS wrapper is read into the aggregation list."""
        inner = (
            "<EVENT-WINDOWS>"
            "<DIAGNOSTIC-EVENT-WINDOW>"
            "<EVENT-WINDOW-TIME>INFINITE-TIME-TO-RESPONSE</EVENT-WINDOW-TIME>"
            "</DIAGNOSTIC-EVENT-WINDOW>"
            "<DIAGNOSTIC-EVENT-WINDOW>"
            "<EVENT-WINDOW-TIME>POWER-WINDOW-TIME</EVENT-WINDOW-TIME>"
            "</DIAGNOSTIC-EVENT-WINDOW>"
            "</EVENT-WINDOWS>"
        )
        response_on_event = self._read(parser, inner)
        event_windows = response_on_event.getEventWindows()
        assert len(event_windows) == 2
        assert event_windows[0].getEventWindowTime().getValue() == "INFINITE-TIME-TO-RESPONSE"
        assert event_windows[1].getEventWindowTime().getValue() == "POWER-WINDOW-TIME"

    def test_read_response_on_event_action(self, parser):
        """Test that the RESPONSE-ON-EVENT-ACTION enum token is read."""
        response_on_event = self._read(parser, "<RESPONSE-ON-EVENT-ACTION>ON-CHANGE-OF-DATA-IDENTIFIER</RESPONSE-ON-EVENT-ACTION>")
        assert response_on_event.getResponseOnEventAction() is not None
        assert response_on_event.getResponseOnEventAction().getValue() == "ON-CHANGE-OF-DATA-IDENTIFIER"

    def test_read_response_on_event_class_ref(self, parser):
        """Test that the RESPONSE-ON-EVENT-CLASS-REF is read with its DEST attribute."""
        inner = '<RESPONSE-ON-EVENT-CLASS-REF DEST="DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS">/AUTOSAR/DiagnosticResponseOnEventClasses/ResponseOnEventClass</RESPONSE-ON-EVENT-CLASS-REF>'
        response_on_event = self._read(parser, inner)
        ref = response_on_event.getResponseOnEventClass()
        assert ref is not None
        assert ref.getValue() == "/AUTOSAR/DiagnosticResponseOnEventClasses/ResponseOnEventClass"
        assert ref.getDest() == "DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving all attributes unset."""
        response_on_event = self._read(parser, "<SHORT-NAME>ResponseOnEvent</SHORT-NAME>")
        assert response_on_event.getEventWindows() == []
        assert response_on_event.getResponseOnEventAction() is None
        assert response_on_event.getResponseOnEventClass() is None
