"""
Tests for writing the DIAGNOSTIC-MEMORY-DESTINATION group elements —
DiagnosticMemoryDestination, Table 4.167 (p.182, R23-11).

DiagnosticMemoryDestination (spec Class row marks it "(abstract)") carries the
nine 0..1 attribute elements of the XSD group DIAGNOSTIC-MEMORY-DESTINATION
(AUTOSAR_00052.xsd l.39458), embedded in each concrete subclass element
(DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY / -USER-DEFINED, aggregated by
ARPackage.element). There is no standalone DIAGNOSTIC-MEMORY-DESTINATION
element, so the writer is the named reusable helper
writeDiagnosticMemoryDestination that the concrete subclass writers call once
they are synced (Rule 0001.7 abstract-XML-bearing-base clause). Both concrete
subclasses are still unsynced stubs queued later in Group25, so the tests drive
the helper directly through a minimal concrete subclass instance and assert
field values / XSD sequenceOffset child order.

clearDtcLimitation, eventDisplacementStrategy, memoryEntryStorageTrigger,
statusBitHandlingTestFailedSinceLastClear and typeOfFreezeFrameRecordNumeration
are written through the _enumToken path against their synced enums.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_memory_destination.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticMemoryDestination
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    DiagnosticClearDtcLimitationEnum,
    DiagnosticEventDisplacementStrategyEnum,
    DiagnosticMemoryEntryStorageTriggerEnum,
    DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum,
    DiagnosticTypeOfFreezeFrameRecordNumerationEnum,
    PositiveInteger,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class _ConcreteDiagnosticMemoryDestination(DiagnosticMemoryDestination):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_destination() -> _ConcreteDiagnosticMemoryDestination:
    destination = _ConcreteDiagnosticMemoryDestination()
    destination.setAgingRequiresTestedCycle(Boolean().setValue(True))
    destination.setClearDtcLimitation(DiagnosticClearDtcLimitationEnum().setValue(DiagnosticClearDtcLimitationEnum.ALL_SUPPORTED_DTCS))
    destination.setDtcStatusAvailabilityMask(PositiveInteger().setValue(255))
    destination.setEventDisplacementStrategy(DiagnosticEventDisplacementStrategyEnum().setValue(DiagnosticEventDisplacementStrategyEnum.PRIO_OCC))
    destination.setMaxNumberOfEventEntries(PositiveInteger().setValue(10))
    destination.setMemoryEntryStorageTrigger(DiagnosticMemoryEntryStorageTriggerEnum().setValue(DiagnosticMemoryEntryStorageTriggerEnum.FDC_THRESHOLD))
    destination.setStatusBitHandlingTestFailedSinceLastClear(
        DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum().setValue(DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum.STATUS_BIT_NORMAL)
    )
    destination.setStatusBitStorageTestFailed(Boolean().setValue(False))
    destination.setTypeOfFreezeFrameRecordNumeration(DiagnosticTypeOfFreezeFrameRecordNumerationEnum().setValue(DiagnosticTypeOfFreezeFrameRecordNumerationEnum.CONFIGURED))
    return destination


class TestWriteDiagnosticMemoryDestination:
    """Tests for writeDiagnosticMemoryDestination — own group field values (Table 4.167)."""

    def test_write_all_fields_in_xsd_sequence_order(self):
        """Test that a fully set destination emits the nine children in XSD sequenceOffset order with the spec values."""
        parent = ET.Element("DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY")
        destination = _make_destination()

        ARXMLWriter().writeDiagnosticMemoryDestination(parent, destination)

        assert [c.tag for c in parent] == [
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
        assert parent.find("AGING-REQUIRES-TESTED-CYCLE").text == "true"
        assert parent.find("CLEAR-DTC-LIMITATION").text == "ALL-SUPPORTED-DTCS"
        assert parent.find("DTC-STATUS-AVAILABILITY-MASK").text == "255"
        assert parent.find("EVENT-DISPLACEMENT-STRATEGY").text == "PRIO-OCC"
        assert parent.find("MAX-NUMBER-OF-EVENT-ENTRIES").text == "10"
        assert parent.find("MEMORY-ENTRY-STORAGE-TRIGGER").text == "FDC-THRESHOLD"
        assert parent.find("STATUS-BIT-HANDLING-TEST-FAILED-SINCE-LAST-CLEAR").text == "STATUS-BIT-NORMAL"
        assert parent.find("STATUS-BIT-STORAGE-TEST-FAILED").text == "false"
        assert parent.find("TYPE-OF-FREEZE-FRAME-RECORD-NUMERATION").text == "CONFIGURED"

    def test_write_unset_field_emits_no_child(self):
        """Test that an unset destination emits no child element (empty wrapper case)."""
        parent = ET.Element("DIAGNOSTIC-MEMORY-DESTINATION-USER-DEFINED")
        destination = _ConcreteDiagnosticMemoryDestination()

        ARXMLWriter().writeDiagnosticMemoryDestination(parent, destination)

        assert [c.tag for c in parent] == []

    def test_round_trip_preserves_field_values(self):
        """Test the write → serialize → re-parse → read-back cycle preserving all nine field values."""
        parent = ET.Element("DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY", {"xmlns": NS})
        ARXMLWriter().writeDiagnosticMemoryDestination(parent, _make_destination())
        xml_text = ET.tostring(parent, encoding="unicode")

        reloaded = _ConcreteDiagnosticMemoryDestination()
        element = ET.fromstring(xml_text)
        ARXMLParser().readDiagnosticMemoryDestination(element, reloaded)

        assert reloaded.getAgingRequiresTestedCycle() is not None
        assert reloaded.getAgingRequiresTestedCycle().value is True
        assert reloaded.getClearDtcLimitation() is not None
        assert reloaded.getClearDtcLimitation().getValue() == DiagnosticClearDtcLimitationEnum.ALL_SUPPORTED_DTCS
        assert reloaded.getDtcStatusAvailabilityMask() is not None
        assert reloaded.getDtcStatusAvailabilityMask().getValue() == 255
        assert reloaded.getEventDisplacementStrategy() is not None
        assert reloaded.getEventDisplacementStrategy().getValue() == DiagnosticEventDisplacementStrategyEnum.PRIO_OCC
        assert reloaded.getMaxNumberOfEventEntries() is not None
        assert reloaded.getMaxNumberOfEventEntries().getValue() == 10
        assert reloaded.getMemoryEntryStorageTrigger() is not None
        assert isinstance(reloaded.getMemoryEntryStorageTrigger(), DiagnosticMemoryEntryStorageTriggerEnum)
        assert reloaded.getMemoryEntryStorageTrigger().getValue() == "FDC-THRESHOLD"
        assert reloaded.getStatusBitHandlingTestFailedSinceLastClear() is not None
        assert isinstance(reloaded.getStatusBitHandlingTestFailedSinceLastClear(), DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum)
        assert reloaded.getStatusBitHandlingTestFailedSinceLastClear().getValue() == DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum.STATUS_BIT_NORMAL
        assert reloaded.getStatusBitStorageTestFailed() is not None
        assert reloaded.getStatusBitStorageTestFailed().value is False
        assert reloaded.getTypeOfFreezeFrameRecordNumeration() is not None
        assert isinstance(reloaded.getTypeOfFreezeFrameRecordNumeration(), DiagnosticTypeOfFreezeFrameRecordNumerationEnum)
        assert reloaded.getTypeOfFreezeFrameRecordNumeration().getValue() == DiagnosticTypeOfFreezeFrameRecordNumerationEnum.CONFIGURED
