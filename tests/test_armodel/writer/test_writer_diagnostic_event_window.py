"""
Tests for writing DIAGNOSTIC-EVENT-WINDOW elements —
DiagnosticEventWindow, Table 4.103 (p.133, R23-11).

DiagnosticEventWindow (concrete ARObject, Aggregated by
DiagnosticResponseOnEvent.eventWindow) defines one 0..1 attribute:
eventWindowTime (EVENT-WINDOW-TIME) — AUTOSAR_00052.xsd group
DIAGNOSTIC-EVENT-WINDOW l.37131 / complexType l.37153. The reusable
writeDiagnosticEventWindow helper is verified directly; the aggregator
dispatch is wired with the DiagnosticResponseOnEvent pass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_event_window.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticEventWindow
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticEventWindowTimeEnum
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestWriteDiagnosticEventWindow:
    """Tests for writeDiagnosticEventWindow — own element field values (Table 4.103)."""

    def _write(self, event_window: DiagnosticEventWindow) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEventWindow(parent, event_window)
        return parent.find("DIAGNOSTIC-EVENT-WINDOW")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticEventWindow without attributes emits an empty DIAGNOSTIC-EVENT-WINDOW element."""
        event_window = DiagnosticEventWindow()

        child = self._write(event_window)
        assert child is not None
        assert len(child) == 0

    def test_write_event_window_time(self):
        """Test that the EVENT-WINDOW-TIME is emitted as its enum XML token."""
        event_window = DiagnosticEventWindow()
        event_window.setEventWindowTime(DiagnosticEventWindowTimeEnum().setValue(DiagnosticEventWindowTimeEnum.INFINITE_TIME_TO_RESPONSE))

        child = self._write(event_window)
        assert child is not None
        element = child.find("EVENT-WINDOW-TIME")
        assert element is not None
        assert element.text == "INFINITE-TIME-TO-RESPONSE"

    def test_round_trip_preserves_field_values(self):
        """Test the full write → re-read cycle preserving the field values (nested ARObject — no document dispatch)."""
        event_window = DiagnosticEventWindow()
        event_window.setEventWindowTime(DiagnosticEventWindowTimeEnum().setValue(DiagnosticEventWindowTimeEnum.POWER_WINDOW_TIME))

        root = self._write(event_window)
        wrapped = ET.fromstring("<PARENT xmlns='http://autosar.org/schema/r4.0'>%s</PARENT>" % ET.tostring(root, encoding="unicode"))

        parser = ARXMLParser()
        parser.detectNamespace(wrapped)
        event_window_2 = DiagnosticEventWindow()
        parser.readDiagnosticEventWindow(wrapped.find("{http://autosar.org/schema/r4.0}DIAGNOSTIC-EVENT-WINDOW"), event_window_2)
        assert event_window_2.getEventWindowTime() is not None
        assert event_window_2.getEventWindowTime().getValue() == "powerWindowTime"
