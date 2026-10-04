"""
Tests for reading the DIAGNOSTIC-MEMORY-DESTINATION group elements —
DiagnosticMemoryDestination, Table 4.167 (p.182, R23-11).

DiagnosticMemoryDestination (spec Class row marks it "(abstract)") carries the
nine 0..1 attribute elements of the XSD group DIAGNOSTIC-MEMORY-DESTINATION
(AUTOSAR_00052.xsd l.39458), embedded in each concrete subclass element
(DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY / -USER-DEFINED, aggregated by
ARPackage.element). There is no standalone DIAGNOSTIC-MEMORY-DESTINATION
element, so the reader is the named reusable helper
readDiagnosticMemoryDestination that the concrete subclass readers call once
they are synced (Rule 0001.7 abstract-XML-bearing-base clause). Both concrete
subclasses are still unsynced stubs queued later in Group25, so the tests drive
the helper directly through a minimal concrete subclass instance.

clearDtcLimitation, eventDisplacementStrategy, memoryEntryStorageTrigger and
statusBitHandlingTestFailedSinceLastClear are read through the _enumToken path
against their synced enums; typeOfFreezeFrameRecordNumeration is round-tripped
as a raw literal until its enum (Table 4.172, Group25) gains its literals.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_memory_destination.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticMemoryDestination
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DiagnosticMemoryEntryStorageTriggerEnum,
    DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum,
)

NS = "http://autosar.org/schema/r4.0"


class _ConcreteDiagnosticMemoryDestination(DiagnosticMemoryDestination):
    pass


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticMemoryDestination:
    """Tests for readDiagnosticMemoryDestination — own group field values (Table 4.167)."""

    def _read(self, parser, inner):
        destination = _ConcreteDiagnosticMemoryDestination()
        parser.readDiagnosticMemoryDestination(_snip(inner), destination)
        return destination

    def test_read_sets_aging_requires_tested_cycle(self, parser):
        """Test that AGING-REQUIRES-TESTED-CYCLE true is read into agingRequiresTestedCycle."""
        destination = self._read(parser, "<AGING-REQUIRES-TESTED-CYCLE>true</AGING-REQUIRES-TESTED-CYCLE>")
        assert destination.getAgingRequiresTestedCycle() is not None
        assert destination.getAgingRequiresTestedCycle().value is True

    def test_read_sets_clear_dtc_limitation(self, parser):
        """Test that CLEAR-DTC-LIMITATION is read through the synced enum token map."""
        destination = self._read(parser, "<CLEAR-DTC-LIMITATION>ALL-SUPPORTED-DTCS</CLEAR-DTC-LIMITATION>")
        assert destination.getClearDtcLimitation() is not None
        assert destination.getClearDtcLimitation().getValue() == "allSupportedDtcs"

    def test_read_sets_dtc_status_availability_mask(self, parser):
        """Test that DTC-STATUS-AVAILABILITY-MASK is read into dtcStatusAvailabilityMask."""
        destination = self._read(parser, "<DTC-STATUS-AVAILABILITY-MASK>255</DTC-STATUS-AVAILABILITY-MASK>")
        assert destination.getDtcStatusAvailabilityMask() is not None
        assert destination.getDtcStatusAvailabilityMask().getValue() == 255

    def test_read_sets_event_displacement_strategy(self, parser):
        """Test that EVENT-DISPLACEMENT-STRATEGY is read through the synced enum token map."""
        destination = self._read(parser, "<EVENT-DISPLACEMENT-STRATEGY>PRIO-OCC</EVENT-DISPLACEMENT-STRATEGY>")
        assert destination.getEventDisplacementStrategy() is not None
        assert destination.getEventDisplacementStrategy().getValue() == "prioOcc"

    def test_read_sets_max_number_of_event_entries(self, parser):
        """Test that MAX-NUMBER-OF-EVENT-ENTRIES is read into maxNumberOfEventEntries."""
        destination = self._read(parser, "<MAX-NUMBER-OF-EVENT-ENTRIES>10</MAX-NUMBER-OF-EVENT-ENTRIES>")
        assert destination.getMaxNumberOfEventEntries() is not None
        assert destination.getMaxNumberOfEventEntries().getValue() == 10

    def test_read_sets_memory_entry_storage_trigger(self, parser):
        """Test that the MEMORY-ENTRY-STORAGE-TRIGGER token is read as the typed enum literal."""
        destination = self._read(parser, "<MEMORY-ENTRY-STORAGE-TRIGGER>CONFIRMED</MEMORY-ENTRY-STORAGE-TRIGGER>")
        assert destination.getMemoryEntryStorageTrigger() is not None
        assert isinstance(destination.getMemoryEntryStorageTrigger(), DiagnosticMemoryEntryStorageTriggerEnum)
        assert destination.getMemoryEntryStorageTrigger().getValue() == "confirmed"

    def test_read_sets_status_bit_handling_test_failed_since_last_clear(self, parser):
        """Test that the STATUS-BIT-HANDLING-TEST-FAILED-SINCE-LAST-CLEAR token is read as the typed enum literal."""
        destination = self._read(parser, "<STATUS-BIT-HANDLING-TEST-FAILED-SINCE-LAST-CLEAR>STATUS-BIT-NORMAL</STATUS-BIT-HANDLING-TEST-FAILED-SINCE-LAST-CLEAR>")
        assert destination.getStatusBitHandlingTestFailedSinceLastClear() is not None
        assert isinstance(destination.getStatusBitHandlingTestFailedSinceLastClear(), DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum)
        assert destination.getStatusBitHandlingTestFailedSinceLastClear().getValue() == "statusBitNormal"

    def test_read_sets_status_bit_storage_test_failed(self, parser):
        """Test that STATUS-BIT-STORAGE-TEST-FAILED false is read into statusBitStorageTestFailed."""
        destination = self._read(parser, "<STATUS-BIT-STORAGE-TEST-FAILED>false</STATUS-BIT-STORAGE-TEST-FAILED>")
        assert destination.getStatusBitStorageTestFailed() is not None
        assert destination.getStatusBitStorageTestFailed().value is False

    def test_read_sets_type_of_freeze_frame_record_numeration_as_raw_literal(self, parser):
        """Test that TYPE-OF-FREEZE-FRAME-RECORD-NUMERATION is round-tripped as a raw literal while its enum is a stub."""
        destination = self._read(parser, "<TYPE-OF-FREEZE-FRAME-RECORD-NUMERATION>CONFIGURED</TYPE-OF-FREEZE-FRAME-RECORD-NUMERATION>")
        assert destination.getTypeOfFreezeFrameRecordNumeration() is not None
        assert destination.getTypeOfFreezeFrameRecordNumeration().getValue() == "CONFIGURED"

    def test_read_empty_leaves_all_fields_none(self, parser):
        """Test that an element without group children leaves every field None."""
        destination = self._read(parser, "")
        assert destination.getAgingRequiresTestedCycle() is None
        assert destination.getClearDtcLimitation() is None
        assert destination.getDtcStatusAvailabilityMask() is None
        assert destination.getEventDisplacementStrategy() is None
        assert destination.getMaxNumberOfEventEntries() is None
        assert destination.getMemoryEntryStorageTrigger() is None
        assert destination.getStatusBitHandlingTestFailedSinceLastClear() is None
        assert destination.getStatusBitStorageTestFailed() is None
        assert destination.getTypeOfFreezeFrameRecordNumeration() is None

    def test_read_full_element_sets_all_fields(self, parser):
        """Test that all nine group children in XSD sequence order populate every field."""
        inner = (
            "<AGING-REQUIRES-TESTED-CYCLE>true</AGING-REQUIRES-TESTED-CYCLE>"
            "<CLEAR-DTC-LIMITATION>CLEAR-ALL-DTCS</CLEAR-DTC-LIMITATION>"
            "<DTC-STATUS-AVAILABILITY-MASK>255</DTC-STATUS-AVAILABILITY-MASK>"
            "<EVENT-DISPLACEMENT-STRATEGY>FULL</EVENT-DISPLACEMENT-STRATEGY>"
            "<MAX-NUMBER-OF-EVENT-ENTRIES>10</MAX-NUMBER-OF-EVENT-ENTRIES>"
            "<MEMORY-ENTRY-STORAGE-TRIGGER>FDC-THRESHOLD</MEMORY-ENTRY-STORAGE-TRIGGER>"
            "<STATUS-BIT-HANDLING-TEST-FAILED-SINCE-LAST-CLEAR>STATUS-BIT-AGING-AND-DISPLACEMENT</STATUS-BIT-HANDLING-TEST-FAILED-SINCE-LAST-CLEAR>"
            "<STATUS-BIT-STORAGE-TEST-FAILED>true</STATUS-BIT-STORAGE-TEST-FAILED>"
            "<TYPE-OF-FREEZE-FRAME-RECORD-NUMERATION>CALCULATED</TYPE-OF-FREEZE-FRAME-RECORD-NUMERATION>"
        )
        destination = self._read(parser, inner)
        assert destination.getAgingRequiresTestedCycle().value is True
        assert destination.getClearDtcLimitation().getValue() == "clearAllDtcs"
        assert destination.getDtcStatusAvailabilityMask().getValue() == 255
        assert destination.getEventDisplacementStrategy().getValue() == "full"
        assert destination.getMaxNumberOfEventEntries().getValue() == 10
        assert destination.getMemoryEntryStorageTrigger() is not None
        assert isinstance(destination.getMemoryEntryStorageTrigger(), DiagnosticMemoryEntryStorageTriggerEnum)
        assert destination.getMemoryEntryStorageTrigger().getValue() == "fdcThreshold"
        assert destination.getStatusBitHandlingTestFailedSinceLastClear() is not None
        assert isinstance(destination.getStatusBitHandlingTestFailedSinceLastClear(), DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum)
        assert destination.getStatusBitHandlingTestFailedSinceLastClear().getValue() == "statusBitAgingAndDisplacement"
        assert destination.getStatusBitStorageTestFailed().value is True
        assert destination.getTypeOfFreezeFrameRecordNumeration().getValue() == "CALCULATED"
