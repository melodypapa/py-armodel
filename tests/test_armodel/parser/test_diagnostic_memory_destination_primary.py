"""
Tests for reading the DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY element —
DiagnosticMemoryDestinationPrimary, Table 4.173 (p.184, R23-11).

DiagnosticMemoryDestinationPrimary (Base most-derived DiagnosticMemoryDestination)
carries one own Attribute row — typeOfDtcSupported (0..1, attr) — while the nine
0..1 attributes of the XSD group DIAGNOSTIC-MEMORY-DESTINATION (AUTOSAR_00052.xsd
l.39458) come from the abstract base (Table 4.167, synced with the reusable helper
readDiagnosticMemoryDestination). The XSD complexType (l.39677) embeds the group
chain ... DIAGNOSTIC-MEMORY-DESTINATION → DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY,
so the reader is readDiagnosticMemoryDestinationPrimary = readIdentifiable +
readDiagnosticMemoryDestination (base helper, read ONCE) + the own
TYPE-OF-DTC-SUPPORTED child read through the synced
DiagnosticTypeOfDtcSupportedEnum token map.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_memory_destination_primary.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticMemoryDestinationPrimary:
    """Tests for readDiagnosticMemoryDestinationPrimary — own element field values (Table 4.173)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticMemoryDestinationPrimary

        primary = DiagnosticMemoryDestinationPrimary(AUTOSAR.getInstance(), "MemoryDestinationPrimary1")
        parser.readDiagnosticMemoryDestinationPrimary(_snip(inner, root_tag="DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY"), primary)
        return primary

    def test_read_sets_short_name(self, parser):
        """Test that the SHORT-NAME child is read into the Identifiable chain."""
        primary = self._read(parser, "<SHORT-NAME>MemoryDestinationPrimary1</SHORT-NAME>")
        assert primary.getShortName() == "MemoryDestinationPrimary1"

    def test_read_sets_type_of_dtc_supported(self, parser):
        """Test that TYPE-OF-DTC-SUPPORTED is read through the synced enum token map."""
        primary = self._read(parser, "<TYPE-OF-DTC-SUPPORTED>ISO-14229-1</TYPE-OF-DTC-SUPPORTED>")
        assert primary.getTypeOfDtcSupported() is not None
        assert primary.getTypeOfDtcSupported().getValue() == "iso14229_1"

    def test_read_sets_inherited_base_group_attribute(self, parser):
        """Test that a base group child (MAX-NUMBER-OF-EVENT-ENTRIES) is read via the base helper."""
        primary = self._read(parser, "<MAX-NUMBER-OF-EVENT-ENTRIES>10</MAX-NUMBER-OF-EVENT-ENTRIES>")
        assert primary.getMaxNumberOfEventEntries() is not None
        assert primary.getMaxNumberOfEventEntries().getValue() == 10

    def test_read_sets_inherited_base_group_enum_token(self, parser):
        """Test that CLEAR-DTC-LIMITATION is read through the base helper's enum token path."""
        primary = self._read(parser, "<CLEAR-DTC-LIMITATION>ALL-SUPPORTED-DTCS</CLEAR-DTC-LIMITATION>")
        assert primary.getClearDtcLimitation() is not None
        assert primary.getClearDtcLimitation().getValue() == "allSupportedDtcs"

    def test_read_sets_inherited_base_group_raw_literal(self, parser):
        """Test that MEMORY-ENTRY-STORAGE-TRIGGER is read as a raw literal while its enum is a stub."""
        primary = self._read(parser, "<MEMORY-ENTRY-STORAGE-TRIGGER>CONFIRMED</MEMORY-ENTRY-STORAGE-TRIGGER>")
        assert primary.getMemoryEntryStorageTrigger() is not None
        assert primary.getMemoryEntryStorageTrigger().getValue() == "CONFIRMED"

    def test_read_empty_leaves_fields_none(self, parser):
        """Test that an element without own or base group children leaves every field None (empty wrapper case)."""
        primary = self._read(parser, "<SHORT-NAME>MemoryDestinationPrimary1</SHORT-NAME>")
        assert primary.getTypeOfDtcSupported() is None
        assert primary.getAgingRequiresTestedCycle() is None
        assert primary.getClearDtcLimitation() is None
        assert primary.getDtcStatusAvailabilityMask() is None
        assert primary.getEventDisplacementStrategy() is None
        assert primary.getMaxNumberOfEventEntries() is None
        assert primary.getMemoryEntryStorageTrigger() is None
        assert primary.getStatusBitHandlingTestFailedSinceLastClear() is None
        assert primary.getStatusBitStorageTestFailed() is None
        assert primary.getTypeOfFreezeFrameRecordNumeration() is None

    def test_read_full_element_sets_all_fields(self, parser):
        """Test that SHORT-NAME + the nine base group children + the own child in XSD sequence order populate every field."""
        inner = (
            "<SHORT-NAME>MemoryDestinationPrimary1</SHORT-NAME>"
            "<AGING-REQUIRES-TESTED-CYCLE>true</AGING-REQUIRES-TESTED-CYCLE>"
            "<CLEAR-DTC-LIMITATION>CLEAR-ALL-DTCS</CLEAR-DTC-LIMITATION>"
            "<DTC-STATUS-AVAILABILITY-MASK>255</DTC-STATUS-AVAILABILITY-MASK>"
            "<EVENT-DISPLACEMENT-STRATEGY>FULL</EVENT-DISPLACEMENT-STRATEGY>"
            "<MAX-NUMBER-OF-EVENT-ENTRIES>10</MAX-NUMBER-OF-EVENT-ENTRIES>"
            "<MEMORY-ENTRY-STORAGE-TRIGGER>FDC-THRESHOLD</MEMORY-ENTRY-STORAGE-TRIGGER>"
            "<STATUS-BIT-HANDLING-TEST-FAILED-SINCE-LAST-CLEAR>STATUS-BIT-AGING-AND-DISPLACEMENT</STATUS-BIT-HANDLING-TEST-FAILED-SINCE-LAST-CLEAR>"
            "<STATUS-BIT-STORAGE-TEST-FAILED>true</STATUS-BIT-STORAGE-TEST-FAILED>"
            "<TYPE-OF-FREEZE-FRAME-RECORD-NUMERATION>CALCULATED</TYPE-OF-FREEZE-FRAME-RECORD-NUMERATION>"
            "<TYPE-OF-DTC-SUPPORTED>SAE-J-1939-73</TYPE-OF-DTC-SUPPORTED>"
        )
        primary = self._read(parser, inner)
        assert primary.getShortName() == "MemoryDestinationPrimary1"
        assert primary.getAgingRequiresTestedCycle().value is True
        assert primary.getClearDtcLimitation().getValue() == "clearAllDtcs"
        assert primary.getDtcStatusAvailabilityMask().getValue() == 255
        assert primary.getEventDisplacementStrategy().getValue() == "full"
        assert primary.getMaxNumberOfEventEntries().getValue() == 10
        assert primary.getMemoryEntryStorageTrigger().getValue() == "FDC-THRESHOLD"
        assert primary.getStatusBitHandlingTestFailedSinceLastClear().getValue() == "STATUS-BIT-AGING-AND-DISPLACEMENT"
        assert primary.getStatusBitStorageTestFailed().value is True
        assert primary.getTypeOfFreezeFrameRecordNumeration().getValue() == "CALCULATED"
        assert primary.getTypeOfDtcSupported().getValue() == "saeJ1939_73"
