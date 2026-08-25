"""
This module contains tests for the SynchronizationTiming related classes in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import (
    EventOccurrenceKindEnum,
    SynchronizationTimingConstraint,
    SynchronizationTypeEnum,
)


class TestSynchronizationTiming:
    """
    Test class for SynchronizationTiming functionality.
    """

    def test_initialization(self):
        parent = AUTOSAR.getInstance().createARPackage("SyncPkg")
        obj = SynchronizationTimingConstraint(parent, "Sync")
        assert obj.getShortName() == "Sync"

    def test_synchronization_type_enum(self):
        obj = SynchronizationTypeEnum()
        assert isinstance(obj, SynchronizationTypeEnum)

    def test_event_occurrence_kind_enum(self):
        obj = EventOccurrenceKindEnum()
        assert isinstance(obj, EventOccurrenceKindEnum)


class TestSynchronizationTypeEnum:
    def test_initialization(self):
        """Test SynchronizationTypeEnum initialization"""
        enum = SynchronizationTypeEnum()
        assert isinstance(enum, SynchronizationTypeEnum)
        assert list(enum.getEnumValues()) == ["responseSynchronization", "stimulusSynchronization"]

    def test_enum_values(self):
        """Test SynchronizationTypeEnum literal values (Table 3.55)"""
        assert SynchronizationTypeEnum.RESPONSE_SYNCHRONIZATION == "responseSynchronization"
        assert SynchronizationTypeEnum.STIMULUS_SYNCHRONIZATION == "stimulusSynchronization"

    def test_valid_values(self):
        """Test SynchronizationTypeEnum setValue round-trip for all literals"""
        enum = SynchronizationTypeEnum()
        for member in [SynchronizationTypeEnum.RESPONSE_SYNCHRONIZATION, SynchronizationTypeEnum.STIMULUS_SYNCHRONIZATION]:
            assert enum.setValue(member).getValue() == member


class TestEventOccurrenceKindEnum:
    def test_initialization(self):
        """Test EventOccurrenceKindEnum initialization"""
        enum = EventOccurrenceKindEnum()
        assert isinstance(enum, EventOccurrenceKindEnum)
        assert list(enum.getEnumValues()) == ["multipleOccurrences", "singleOccurrence"]

    def test_enum_values(self):
        """Test EventOccurrenceKindEnum literal values (Table 3.56)"""
        assert EventOccurrenceKindEnum.MULTIPLE_OCCURRENCES == "multipleOccurrences"
        assert EventOccurrenceKindEnum.SINGLE_OCCURRENCE == "singleOccurrence"

    def test_valid_values(self):
        """Test EventOccurrenceKindEnum setValue round-trip for all literals"""
        enum = EventOccurrenceKindEnum()
        for member in [EventOccurrenceKindEnum.MULTIPLE_OCCURRENCES, EventOccurrenceKindEnum.SINGLE_OCCURRENCE]:
            assert enum.setValue(member).getValue() == member
