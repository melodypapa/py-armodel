"""
Tests for writing DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY elements —
DiagnosticMemoryDestinationPrimary, Table 4.173 (p.184, R23-11).

DiagnosticMemoryDestinationPrimary (Base most-derived DiagnosticMemoryDestination)
carries one own Attribute row — typeOfDtcSupported (0..1, attr) — while the nine
0..1 attributes of the XSD group DIAGNOSTIC-MEMORY-DESTINATION (AUTOSAR_00052.xsd
l.39458) come from the abstract base (Table 4.167, synced with the reusable helper
writeDiagnosticMemoryDestination). The XSD complexType (l.39677) embeds the group
chain ... DIAGNOSTIC-MEMORY-DESTINATION → DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY,
so the writer is writeDiagnosticMemoryDestinationPrimary =
DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY subelement + writeIdentifiable +
writeDiagnosticMemoryDestination (base helper) + the own TYPE-OF-DTC-SUPPORTED
child written through the synced DiagnosticTypeOfDtcSupportedEnum token map.
The dispatch entry is writeARPackageElement → writeDiagnosticMemoryDestinationPrimary.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_memory_destination_primary.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticMemoryDestinationPrimary
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    DiagnosticClearDtcLimitationEnum,
    DiagnosticEventDisplacementStrategyEnum,
    DiagnosticMemoryEntryStorageTriggerEnum,
    DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum,
    DiagnosticTypeOfDtcSupportedEnum,
    DiagnosticTypeOfFreezeFrameRecordNumerationEnum,
    PositiveInteger,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

BASE_GROUP_TAGS = [
    "AGING-REQUIRES-TESTED-CYCLE",
    "CLEAR-DTC-LIMITATION",
    "DTC-STATUS-AVAILABILITY-MASK",
    "EVENT-DISPLACEMENT-STRATEGY",
    "MAX-NUMBER-OF-EVENT-ENTRIES",
    "MEMORY-ENTRY-STORAGE-TRIGGER",
    "STATUS-BIT-HANDLING-TEST-FAILED-SINCE-LAST-CLEAR",
    "STATUS-BIT-STORAGE-TEST-FAILED",
    "TYPE-OF-FREEZE-FRAME-RECORD-NUMERATION",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_primary(package) -> DiagnosticMemoryDestinationPrimary:
    primary = package.createDiagnosticMemoryDestinationPrimary("MemoryDestinationPrimary1")
    primary.setAgingRequiresTestedCycle(Boolean().setValue(True))
    primary.setClearDtcLimitation(DiagnosticClearDtcLimitationEnum().setValue(DiagnosticClearDtcLimitationEnum.CLEAR_ALL_DTCS))
    primary.setDtcStatusAvailabilityMask(PositiveInteger().setValue(255))
    primary.setEventDisplacementStrategy(DiagnosticEventDisplacementStrategyEnum().setValue(DiagnosticEventDisplacementStrategyEnum.FULL))
    primary.setMaxNumberOfEventEntries(PositiveInteger().setValue(10))
    primary.setMemoryEntryStorageTrigger(DiagnosticMemoryEntryStorageTriggerEnum().setValue(DiagnosticMemoryEntryStorageTriggerEnum.CONFIRMED))
    primary.setStatusBitHandlingTestFailedSinceLastClear(DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum([]).setValue("STATUS-BIT-NORMAL"))
    primary.setStatusBitStorageTestFailed(Boolean().setValue(False))
    primary.setTypeOfFreezeFrameRecordNumeration(DiagnosticTypeOfFreezeFrameRecordNumerationEnum([]).setValue("CALCULATED"))
    primary.setTypeOfDtcSupported(DiagnosticTypeOfDtcSupportedEnum().setValue(DiagnosticTypeOfDtcSupportedEnum.ISO14229_1))
    return primary


class TestWriteDiagnosticMemoryDestinationPrimary:
    """Tests for writeDiagnosticMemoryDestinationPrimary — own element field values (Table 4.173)."""

    def test_write_all_fields_in_xsd_sequence_order(self):
        """Test that a fully set element emits SHORT-NAME + the nine base group children + the own child in XSD sequenceOffset order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMemoryDestinations")
        primary = _make_primary(package)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticMemoryDestinationPrimary(parent, primary)

        child = parent.find("DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY")
        assert child is not None
        assert [c.tag for c in child if c.tag in BASE_GROUP_TAGS + ["TYPE-OF-DTC-SUPPORTED"]] == BASE_GROUP_TAGS + ["TYPE-OF-DTC-SUPPORTED"]
        assert child.find("SHORT-NAME").text == "MemoryDestinationPrimary1"
        assert child.find("AGING-REQUIRES-TESTED-CYCLE").text == "true"
        assert child.find("CLEAR-DTC-LIMITATION").text == "CLEAR-ALL-DTCS"
        assert child.find("DTC-STATUS-AVAILABILITY-MASK").text == "255"
        assert child.find("EVENT-DISPLACEMENT-STRATEGY").text == "FULL"
        assert child.find("MAX-NUMBER-OF-EVENT-ENTRIES").text == "10"
        assert child.find("MEMORY-ENTRY-STORAGE-TRIGGER").text == "CONFIRMED"
        assert child.find("STATUS-BIT-HANDLING-TEST-FAILED-SINCE-LAST-CLEAR").text == "STATUS-BIT-NORMAL"
        assert child.find("STATUS-BIT-STORAGE-TEST-FAILED").text == "false"
        assert child.find("TYPE-OF-FREEZE-FRAME-RECORD-NUMERATION").text == "CALCULATED"
        assert child.find("TYPE-OF-DTC-SUPPORTED").text == "ISO-14229-1"

    def test_write_unset_fields_emit_no_children(self):
        """Test that an element without own or base group values emits no attribute children (empty wrapper case)."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMemoryDestinations")
        package.createDiagnosticMemoryDestinationPrimary("MemoryDestinationPrimary1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticMemoryDestinationPrimary(parent, package.getReferrableElement("MemoryDestinationPrimary1", DiagnosticMemoryDestinationPrimary))

        child = parent.find("DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY")
        assert child is not None
        assert child.find("TYPE-OF-DTC-SUPPORTED") is None
        assert child.find("AGING-REQUIRES-TESTED-CYCLE") is None
        assert child.find("MEMORY-ENTRY-STORAGE-TRIGGER") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticMemoryDestinationPrimary to a DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY element."""
        package = AUTOSAR.getInstance().createARPackage("DiagnosticMemoryDestinations")
        primary = package.createDiagnosticMemoryDestinationPrimary("MemoryDestinationPrimary1")
        primary.setTypeOfDtcSupported(DiagnosticTypeOfDtcSupportedEnum().setValue(DiagnosticTypeOfDtcSupportedEnum.ISO11992_4))

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, primary)

        child = parent.find("DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY")
        assert child is not None
        assert child.find("SHORT-NAME").text == "MemoryDestinationPrimary1"
        assert child.find("TYPE-OF-DTC-SUPPORTED").text == "ISO-11992-4"

    def test_round_trip_preserves_field_values(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with own and inherited base field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticMemoryDestinations")
        _make_primary(package)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            primary_2 = package_2.getReferrableElement("MemoryDestinationPrimary1", DiagnosticMemoryDestinationPrimary)
            assert primary_2 is not None
            assert primary_2.getShortName() == "MemoryDestinationPrimary1"
            assert primary_2.getTypeOfDtcSupported() is not None
            assert primary_2.getTypeOfDtcSupported().getValue() == "iso14229_1"
            assert primary_2.getAgingRequiresTestedCycle() is not None
            assert primary_2.getAgingRequiresTestedCycle().value is True
            assert primary_2.getClearDtcLimitation() is not None
            assert primary_2.getClearDtcLimitation().getValue() == "clearAllDtcs"
            assert primary_2.getDtcStatusAvailabilityMask() is not None
            assert primary_2.getDtcStatusAvailabilityMask().getValue() == 255
            assert primary_2.getEventDisplacementStrategy() is not None
            assert primary_2.getEventDisplacementStrategy().getValue() == "full"
            assert primary_2.getMaxNumberOfEventEntries() is not None
            assert primary_2.getMaxNumberOfEventEntries().getValue() == 10
            assert primary_2.getMemoryEntryStorageTrigger() is not None
            assert primary_2.getMemoryEntryStorageTrigger().getValue() == "confirmed"
            assert primary_2.getStatusBitHandlingTestFailedSinceLastClear() is not None
            assert primary_2.getStatusBitHandlingTestFailedSinceLastClear().getValue() == "STATUS-BIT-NORMAL"
            assert primary_2.getStatusBitStorageTestFailed() is not None
            assert primary_2.getStatusBitStorageTestFailed().value is False
            assert primary_2.getTypeOfFreezeFrameRecordNumeration() is not None
            assert primary_2.getTypeOfFreezeFrameRecordNumeration().getValue() == "CALCULATED"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticMemoryDestinationPrimary without any attribute value round-trips with None."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticMemoryDestinations")
        package.createDiagnosticMemoryDestinationPrimary("MemoryDestinationPrimary1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            primary_2 = package_2.getReferrableElement("MemoryDestinationPrimary1", DiagnosticMemoryDestinationPrimary)
            assert primary_2 is not None
            assert primary_2.getTypeOfDtcSupported() is None
            assert primary_2.getMaxNumberOfEventEntries() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
