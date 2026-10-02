"""
Tests for writing DIAGNOSTIC-RESPONSE-ON-EVENT elements —
DiagnosticResponseOnEvent, Table 4.101 (p.132, R23-11).

DiagnosticResponseOnEvent (Base most-derived ARElement, aggregated by
ARPackage.element) owns three attributes in XSD group
DIAGNOSTIC-RESPONSE-ON-EVENT, AUTOSAR_00052.xsd l.42645: the 0..*
eventWindow aggregation (EVENT-WINDOWS wrapper of DIAGNOSTIC-EVENT-WINDOW
elements), the 0..1 responseOnEventAction attr (RESPONSE-ON-EVENT-ACTION)
and the 0..1 responseOnEventClass ref (RESPONSE-ON-EVENT-CLASS-REF, DEST
DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS--SUBTYPES-ENUM). The writer reads the
model via the get* getters in XSD element order. The dispatch entry is
writeARPackageElement → writeDiagnosticResponseOnEvent.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_response_on_event.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticEventWindow
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticResponseOnEvent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticEventWindowTimeEnum, DiagnosticResponseOnEventActionEnum, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestWriteDiagnosticResponseOnEvent:
    """Tests for writeDiagnosticResponseOnEvent — own element field values (Table 4.101)."""

    def _write(self, response_on_event: DiagnosticResponseOnEvent) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticResponseOnEvent(parent, response_on_event)
        return parent.find("DIAGNOSTIC-RESPONSE-ON-EVENT")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticResponseOnEvent without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        response_on_event = package.createDiagnosticResponseOnEvent("ResponseOnEvent1")

        child = self._write(response_on_event)
        assert child is not None
        assert child.find("SHORT-NAME").text == "ResponseOnEvent1"
        assert child.find("EVENT-WINDOWS") is None
        assert child.find("RESPONSE-ON-EVENT-ACTION") is None
        assert child.find("RESPONSE-ON-EVENT-CLASS-REF") is None

    def test_write_event_windows(self):
        """Test that the EVENT-WINDOWS wrapper is emitted from the aggregation list."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        response_on_event = package.createDiagnosticResponseOnEvent("ResponseOnEvent1")
        event_window = DiagnosticEventWindow()
        event_window.setEventWindowTime(DiagnosticEventWindowTimeEnum().setValue(DiagnosticEventWindowTimeEnum.INFINITE_TIME_TO_RESPONSE))
        response_on_event.addEventWindow(event_window)

        child = self._write(response_on_event)
        wrapper = child.find("EVENT-WINDOWS")
        assert wrapper is not None
        windows = wrapper.findall("DIAGNOSTIC-EVENT-WINDOW")
        assert len(windows) == 1
        assert windows[0].find("EVENT-WINDOW-TIME").text == "INFINITE-TIME-TO-RESPONSE"

    def test_write_response_on_event_action(self):
        """Test that the RESPONSE-ON-EVENT-ACTION is emitted as its enum XML token."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        response_on_event = package.createDiagnosticResponseOnEvent("ResponseOnEvent1")
        response_on_event.setResponseOnEventAction(DiagnosticResponseOnEventActionEnum().setValue(DiagnosticResponseOnEventActionEnum.START))

        child = self._write(response_on_event)
        action = child.find("RESPONSE-ON-EVENT-ACTION")
        assert action is not None
        assert action.text == "START"

    def test_write_response_on_event_class_ref(self):
        """Test that the RESPONSE-ON-EVENT-CLASS-REF is emitted with its DEST attribute."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        response_on_event = package.createDiagnosticResponseOnEvent("ResponseOnEvent1")
        response_on_event.setResponseOnEventClass(_ref("DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS", "/AUTOSAR/DiagnosticResponseOnEventClasses/ResponseOnEventClass"))

        child = self._write(response_on_event)
        ref = child.find("RESPONSE-ON-EVENT-CLASS-REF")
        assert ref is not None
        assert ref.text == "/AUTOSAR/DiagnosticResponseOnEventClasses/ResponseOnEventClass"
        assert ref.get("DEST") == "DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS"

    def test_write_element_order_matches_xsd_sequence(self):
        """Test that the emitted children follow the XSD element order (l.42645)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        response_on_event = package.createDiagnosticResponseOnEvent("ResponseOnEvent1")
        response_on_event.addEventWindow(DiagnosticEventWindow())
        response_on_event.setResponseOnEventAction(DiagnosticResponseOnEventActionEnum().setValue(DiagnosticResponseOnEventActionEnum.STOP))
        response_on_event.setResponseOnEventClass(_ref("DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS", "/AUTOSAR/DiagnosticResponseOnEventClasses/ResponseOnEventClass"))

        child = self._write(response_on_event)
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == [
            "EVENT-WINDOWS",
            "RESPONSE-ON-EVENT-ACTION",
            "RESPONSE-ON-EVENT-CLASS-REF",
        ]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticResponseOnEvent to a DIAGNOSTIC-RESPONSE-ON-EVENT element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        package.createDiagnosticResponseOnEvent("ResponseOnEvent1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getElement("ResponseOnEvent1", DiagnosticResponseOnEvent))

        child = parent.find("DIAGNOSTIC-RESPONSE-ON-EVENT")
        assert child is not None
        assert child.find("SHORT-NAME").text == "ResponseOnEvent1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticResponseOnEvents")
        response_on_event = package.createDiagnosticResponseOnEvent("ResponseOnEvent1")
        event_window = DiagnosticEventWindow()
        event_window.setEventWindowTime(DiagnosticEventWindowTimeEnum().setValue(DiagnosticEventWindowTimeEnum.POWER_WINDOW_TIME))
        response_on_event.addEventWindow(event_window)
        response_on_event.setResponseOnEventAction(DiagnosticResponseOnEventActionEnum().setValue(DiagnosticResponseOnEventActionEnum.ON_DTC_STATUS_CHANGE))
        response_on_event.setResponseOnEventClass(_ref("DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS", "/AUTOSAR/DiagnosticResponseOnEventClasses/ResponseOnEventClass"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            response_on_event_2 = package_2.getElement("ResponseOnEvent1", DiagnosticResponseOnEvent)
            assert response_on_event_2 is not None
            assert response_on_event_2.getShortName() == "ResponseOnEvent1"
            event_windows_2 = response_on_event_2.getEventWindows()
            assert len(event_windows_2) == 1
            assert event_windows_2[0].getEventWindowTime().getValue() == "powerWindowTime"
            assert response_on_event_2.getResponseOnEventAction().getValue() == "onDTCStatusChange"
            response_on_event_class = response_on_event_2.getResponseOnEventClass()
            assert response_on_event_class is not None
            assert response_on_event_class.getValue() == "/AUTOSAR/DiagnosticResponseOnEventClasses/ResponseOnEventClass"
            assert response_on_event_class.getDest() == "DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
