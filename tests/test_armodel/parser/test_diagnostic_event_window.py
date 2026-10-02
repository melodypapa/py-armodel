"""
Tests for reading the DIAGNOSTIC-EVENT-WINDOW element —
DiagnosticEventWindow, Table 4.103 (p.133, R23-11).

DiagnosticEventWindow (concrete ARObject, Aggregated by
DiagnosticResponseOnEvent.eventWindow) defines one 0..1 attribute:
eventWindowTime (DiagnosticEventWindowTimeEnum, EVENT-WINDOW-TIME) —
AUTOSAR_00052.xsd group DIAGNOSTIC-EVENT-WINDOW l.37131. The reusable
readDiagnosticEventWindow helper is verified directly; the aggregator
dispatch is wired with the DiagnosticResponseOnEvent pass.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_event_window.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticEventWindow:
    """Tests for readDiagnosticEventWindow — own element field values (Table 4.103)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticEventWindow

        event_window = DiagnosticEventWindow()
        element = _snip(inner, root_tag="DIAGNOSTIC-EVENT-WINDOW")
        parser.readDiagnosticEventWindow(element, event_window)
        return event_window

    def test_read_event_window_time(self, parser):
        """Test that the EVENT-WINDOW-TIME enum token is read into eventWindowTime."""
        event_window = self._read(parser, "<EVENT-WINDOW-TIME>INFINITE-TIME-TO-RESPONSE</EVENT-WINDOW-TIME>")
        assert event_window.getEventWindowTime() is not None
        assert event_window.getEventWindowTime().getValue() == "infiniteTimeToResponse"

    def test_read_power_window_time_token(self, parser):
        """Test that the POWER-WINDOW-TIME enum token is read into eventWindowTime."""
        event_window = self._read(parser, "<EVENT-WINDOW-TIME>POWER-WINDOW-TIME</EVENT-WINDOW-TIME>")
        assert event_window.getEventWindowTime() is not None
        assert event_window.getEventWindowTime().getValue() == "powerWindowTime"

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving all fields unset."""
        event_window = self._read(parser, "")
        assert event_window.getEventWindowTime() is None
