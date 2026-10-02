"""
Tests for reading the DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS element —
DiagnosticResponseOnEventClass, Table 4.102 (p.133, R23-11).

DiagnosticResponseOnEventClass (Base most-derived DiagnosticServiceClass,
concrete) defines six 0..1 attributes in XSD group
DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS, AUTOSAR_00052.xsd l.42716:
maxNumChangeOfDataIdentfierEvents and maxNumComparisionOfValueEvents /
maxNumberOfStoredDTCStatusChangedEvents / maxSupportedDIDLength
(POSITIVE-INTEGER), responseOnEventSchedulerRate (TIME-VALUE) and
storeEventEnabled (BOOLEAN). The removed INTER-MESSAGE-TIME element
(atp.Status="removed") is not modeled. The reader populates the fields via
the model mutators in XSD element order. The dispatch entry is
readARPackageElements → readDiagnosticResponseOnEventClass via the ARPackage
create factory.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_response_on_event_class.py
"""

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticResponseOnEventClass:
    """Tests for readDiagnosticResponseOnEventClass — own element field values (Table 4.102)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticResponseOnEventClass

        response_on_event_class = DiagnosticResponseOnEventClass(parent=parser, short_name="Roec")
        element = _snip(inner, root_tag="DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS")
        parser.readDiagnosticResponseOnEventClass(element, response_on_event_class)
        return response_on_event_class

    def test_read_short_name(self, parser):
        """Test that the IDENTIFIABLE wrapper is read (short name)."""
        response_on_event_class = self._read(parser, "<SHORT-NAME>Roec</SHORT-NAME>")
        assert response_on_event_class.getShortName() == "Roec"

    def test_read_max_number_of_stored_dtc_status_changed_events(self, parser):
        """Test that the MAX-NUMBER-OF-STORED-DTC-STATUS-CHANGED-EVENTS positive integer is read."""
        response_on_event_class = self._read(parser, "<MAX-NUMBER-OF-STORED-DTC-STATUS-CHANGED-EVENTS>5</MAX-NUMBER-OF-STORED-DTC-STATUS-CHANGED-EVENTS>")
        assert response_on_event_class.getMaxNumberOfStoredDTCStatusChangedEvents() is not None
        assert response_on_event_class.getMaxNumberOfStoredDTCStatusChangedEvents().getValue() == 5

    def test_read_max_num_change_of_data_identfier_events(self, parser):
        """Test that the MAX-NUM-CHANGE-OF-DATA-IDENTFIER-EVENTS positive integer is read."""
        response_on_event_class = self._read(parser, "<MAX-NUM-CHANGE-OF-DATA-IDENTFIER-EVENTS>4</MAX-NUM-CHANGE-OF-DATA-IDENTFIER-EVENTS>")
        assert response_on_event_class.getMaxNumChangeOfDataIdentfierEvents() is not None
        assert response_on_event_class.getMaxNumChangeOfDataIdentfierEvents().getValue() == 4

    def test_read_max_num_comparision_of_value_events(self, parser):
        """Test that the MAX-NUM-COMPARISION-OF-VALUE-EVENTS positive integer is read."""
        response_on_event_class = self._read(parser, "<MAX-NUM-COMPARISION-OF-VALUE-EVENTS>3</MAX-NUM-COMPARISION-OF-VALUE-EVENTS>")
        assert response_on_event_class.getMaxNumComparisionOfValueEvents() is not None
        assert response_on_event_class.getMaxNumComparisionOfValueEvents().getValue() == 3

    def test_read_max_supported_did_length(self, parser):
        """Test that the MAX-SUPPORTED-DID-LENGTH positive integer is read."""
        response_on_event_class = self._read(parser, "<MAX-SUPPORTED-DID-LENGTH>6</MAX-SUPPORTED-DID-LENGTH>")
        assert response_on_event_class.getMaxSupportedDIDLength() is not None
        assert response_on_event_class.getMaxSupportedDIDLength().getValue() == 6

    def test_read_response_on_event_scheduler_rate(self, parser):
        """Test that the RESPONSE-ON-EVENT-SCHEDULER-RATE time value is read."""
        response_on_event_class = self._read(parser, "<RESPONSE-ON-EVENT-SCHEDULER-RATE>0.5</RESPONSE-ON-EVENT-SCHEDULER-RATE>")
        assert response_on_event_class.getResponseOnEventSchedulerRate() is not None
        assert response_on_event_class.getResponseOnEventSchedulerRate().getValue() == 0.5

    def test_read_store_event_enabled(self, parser):
        """Test that the STORE-EVENT-ENABLED boolean is read."""
        response_on_event_class = self._read(parser, "<STORE-EVENT-ENABLED>true</STORE-EVENT-ENABLED>")
        assert response_on_event_class.getStoreEventEnabled() is not None
        assert response_on_event_class.getStoreEventEnabled().getValue() is True

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving all attributes unset."""
        response_on_event_class = self._read(parser, "<SHORT-NAME>Roec</SHORT-NAME>")
        assert response_on_event_class.getMaxNumberOfStoredDTCStatusChangedEvents() is None
        assert response_on_event_class.getMaxNumChangeOfDataIdentfierEvents() is None
        assert response_on_event_class.getMaxNumComparisionOfValueEvents() is None
        assert response_on_event_class.getMaxSupportedDIDLength() is None
        assert response_on_event_class.getResponseOnEventSchedulerRate() is None
        assert response_on_event_class.getStoreEventEnabled() is None
