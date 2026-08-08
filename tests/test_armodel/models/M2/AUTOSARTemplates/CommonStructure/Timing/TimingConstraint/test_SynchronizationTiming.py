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
