"""
Tests for writing DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS elements —
DiagnosticResponseOnEventClass, Table 4.102 (p.133, R23-11).

DiagnosticResponseOnEventClass (Base most-derived DiagnosticServiceClass,
concrete) defines six 0..1 attributes in XSD group
DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS, AUTOSAR_00052.xsd l.42716:
maxNumChangeOfDataIdentfierEvents, maxNumComparisionOfValueEvents,
maxNumberOfStoredDTCStatusChangedEvents, maxSupportedDIDLength,
responseOnEventSchedulerRate and storeEventEnabled. The writer reads the
model via the get* getters in XSD element order. The dispatch entry is
writeARPackageElement → writeDiagnosticResponseOnEventClass.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_response_on_event_class.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticResponseOnEventClass
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, TimeValue
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _positive_integer(value: str) -> PositiveInteger:
    nrc_value = PositiveInteger()
    nrc_value.setValue(value)
    return nrc_value


class TestWriteDiagnosticResponseOnEventClass:
    """Tests for writeDiagnosticResponseOnEventClass — own element field values (Table 4.102)."""

    def _write(self, response_on_event_class: DiagnosticResponseOnEventClass) -> ET.Element:
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticResponseOnEventClass(parent, response_on_event_class)
        return parent.find("DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS")

    def test_write_empty_wrapper(self):
        """Test that a DiagnosticResponseOnEventClass without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        package.createDiagnosticResponseOnEventClass("Roec1")

        child = self._write(package.getReferrableElement("Roec1", DiagnosticResponseOnEventClass))
        assert child is not None
        assert child.find("SHORT-NAME").text == "Roec1"
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == []

    def test_write_max_number_of_stored_dtc_status_changed_events(self):
        """Test that the MAX-NUMBER-OF-STORED-DTC-STATUS-CHANGED-EVENTS is emitted."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        response_on_event_class = package.createDiagnosticResponseOnEventClass("Roec1")
        response_on_event_class.setMaxNumberOfStoredDTCStatusChangedEvents(_positive_integer("5"))

        child = self._write(response_on_event_class)
        element = child.find("MAX-NUMBER-OF-STORED-DTC-STATUS-CHANGED-EVENTS")
        assert element is not None
        assert element.text == "5"

    def test_write_max_num_change_of_data_identfier_events(self):
        """Test that the MAX-NUM-CHANGE-OF-DATA-IDENTFIER-EVENTS is emitted."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        response_on_event_class = package.createDiagnosticResponseOnEventClass("Roec1")
        response_on_event_class.setMaxNumChangeOfDataIdentfierEvents(_positive_integer("4"))

        child = self._write(response_on_event_class)
        element = child.find("MAX-NUM-CHANGE-OF-DATA-IDENTFIER-EVENTS")
        assert element is not None
        assert element.text == "4"

    def test_write_max_num_comparision_of_value_events(self):
        """Test that the MAX-NUM-COMPARISION-OF-VALUE-EVENTS is emitted."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        response_on_event_class = package.createDiagnosticResponseOnEventClass("Roec1")
        response_on_event_class.setMaxNumComparisionOfValueEvents(_positive_integer("3"))

        child = self._write(response_on_event_class)
        element = child.find("MAX-NUM-COMPARISION-OF-VALUE-EVENTS")
        assert element is not None
        assert element.text == "3"

    def test_write_max_supported_did_length(self):
        """Test that the MAX-SUPPORTED-DID-LENGTH is emitted."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        response_on_event_class = package.createDiagnosticResponseOnEventClass("Roec1")
        response_on_event_class.setMaxSupportedDIDLength(_positive_integer("6"))

        child = self._write(response_on_event_class)
        element = child.find("MAX-SUPPORTED-DID-LENGTH")
        assert element is not None
        assert element.text == "6"

    def test_write_response_on_event_scheduler_rate(self):
        """Test that the RESPONSE-ON-EVENT-SCHEDULER-RATE is emitted."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        response_on_event_class = package.createDiagnosticResponseOnEventClass("Roec1")
        scheduler_rate = TimeValue()
        scheduler_rate.setValue(0.5)
        response_on_event_class.setResponseOnEventSchedulerRate(scheduler_rate)

        child = self._write(response_on_event_class)
        element = child.find("RESPONSE-ON-EVENT-SCHEDULER-RATE")
        assert element is not None
        assert element.text == "0.5"

    def test_write_store_event_enabled(self):
        """Test that the STORE-EVENT-ENABLED boolean is emitted."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        response_on_event_class = package.createDiagnosticResponseOnEventClass("Roec1")
        store_event_enabled = Boolean()
        store_event_enabled.setValue("true")
        response_on_event_class.setStoreEventEnabled(store_event_enabled)

        child = self._write(response_on_event_class)
        element = child.find("STORE-EVENT-ENABLED")
        assert element is not None
        assert element.text == "true"

    def test_write_element_order_matches_xsd_sequence(self):
        """Test that the emitted children follow the XSD element order (l.42716)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        response_on_event_class = package.createDiagnosticResponseOnEventClass("Roec1")
        scheduler_rate = TimeValue()
        scheduler_rate.setValue(1.0)
        store_event_enabled = Boolean()
        store_event_enabled.setValue("false")
        response_on_event_class.setMaxNumberOfStoredDTCStatusChangedEvents(_positive_integer("5"))
        response_on_event_class.setMaxNumChangeOfDataIdentfierEvents(_positive_integer("4"))
        response_on_event_class.setMaxNumComparisionOfValueEvents(_positive_integer("3"))
        response_on_event_class.setMaxSupportedDIDLength(_positive_integer("6"))
        response_on_event_class.setResponseOnEventSchedulerRate(scheduler_rate)
        response_on_event_class.setStoreEventEnabled(store_event_enabled)

        child = self._write(response_on_event_class)
        assert [c.tag for c in child if c.tag != "SHORT-NAME"] == [
            "MAX-NUM-CHANGE-OF-DATA-IDENTFIER-EVENTS",
            "MAX-NUM-COMPARISION-OF-VALUE-EVENTS",
            "MAX-NUMBER-OF-STORED-DTC-STATUS-CHANGED-EVENTS",
            "MAX-SUPPORTED-DID-LENGTH",
            "RESPONSE-ON-EVENT-SCHEDULER-RATE",
            "STORE-EVENT-ENABLED",
        ]

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticResponseOnEventClass to a DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticResponseOnEvents")
        package.createDiagnosticResponseOnEventClass("Roec1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, package.getReferrableElement("Roec1", DiagnosticResponseOnEventClass))

        child = parent.find("DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Roec1"

    def test_round_trip_preserves_field_values(self):
        """Test the full create → save → reload → assert cycle preserving the field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticResponseOnEvents")
        response_on_event_class = package.createDiagnosticResponseOnEventClass("Roec1")
        scheduler_rate = TimeValue()
        scheduler_rate.setValue(0.5)
        store_event_enabled = Boolean()
        store_event_enabled.setValue("true")
        response_on_event_class.setMaxNumberOfStoredDTCStatusChangedEvents(_positive_integer("5"))
        response_on_event_class.setMaxNumChangeOfDataIdentfierEvents(_positive_integer("4"))
        response_on_event_class.setMaxNumComparisionOfValueEvents(_positive_integer("3"))
        response_on_event_class.setMaxSupportedDIDLength(_positive_integer("6"))
        response_on_event_class.setResponseOnEventSchedulerRate(scheduler_rate)
        response_on_event_class.setStoreEventEnabled(store_event_enabled)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            response_on_event_class_2 = package_2.getReferrableElement("Roec1", DiagnosticResponseOnEventClass)
            assert response_on_event_class_2 is not None
            assert response_on_event_class_2.getShortName() == "Roec1"
            assert response_on_event_class_2.getMaxNumberOfStoredDTCStatusChangedEvents().getValue() == 5
            assert response_on_event_class_2.getMaxNumChangeOfDataIdentfierEvents().getValue() == 4
            assert response_on_event_class_2.getMaxNumComparisionOfValueEvents().getValue() == 3
            assert response_on_event_class_2.getMaxSupportedDIDLength().getValue() == 6
            assert response_on_event_class_2.getResponseOnEventSchedulerRate().getValue() == 0.5
            assert response_on_event_class_2.getStoreEventEnabled().getValue() is True
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
