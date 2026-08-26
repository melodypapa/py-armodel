"""
This module contains tests for the SynchronizationTiming related classes in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTimingConstraint import (
    EventOccurrenceKindEnum,
    SynchronizationTimingConstraint,
    SynchronizationTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Integer,
    RefType,
)


class TestSynchronizationTiming:
    """
    Test class for SynchronizationTimingConstraint functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def _mdt(self) -> MultidimensionalTime:
        mdt = MultidimensionalTime()
        mdt.setCseCode(CseCodeType().setValue("0"))
        mdt.setCseCodeFactor(Integer().setValue("50"))
        return mdt

    def test_initialization(self):
        constraint = SynchronizationTimingConstraint(self._parent(), "Sync1")
        assert isinstance(constraint, SynchronizationTimingConstraint)
        assert constraint.getShortName() == "Sync1"
        assert constraint.getTimingConditionRef() is None
        assert constraint.getEventOccurrenceKind() is None
        assert constraint.getScopes() == []
        assert constraint.getScopeEvents() == []
        assert constraint.getSynchronizationConstraintType() is None
        assert constraint.getTolerance() is None

    def test_get_set_event_occurrence_kind(self):
        constraint = SynchronizationTimingConstraint(self._parent(), "Sync1")
        kind = EventOccurrenceKindEnum().setValue(EventOccurrenceKindEnum.SINGLE_OCCURRENCE)
        assert constraint.setEventOccurrenceKind(kind) is constraint
        assert constraint.getEventOccurrenceKind() is kind
        assert constraint.getEventOccurrenceKind().getValue() == "singleOccurrence"

    def test_set_event_occurrence_kind_none_is_no_op(self):
        constraint = SynchronizationTimingConstraint(self._parent(), "Sync1")
        kind = EventOccurrenceKindEnum().setValue(EventOccurrenceKindEnum.MULTIPLE_OCCURRENCES)
        constraint.setEventOccurrenceKind(kind)
        constraint.setEventOccurrenceKind(None)
        assert constraint.getEventOccurrenceKind() is kind

    def test_add_scope(self):
        constraint = SynchronizationTimingConstraint(self._parent(), "Sync1")
        ref1 = RefType().setValue("/Pkg/Chain1").setDest("TIMING-DESCRIPTION-EVENT-CHAIN")
        ref2 = RefType().setValue("/Pkg/Chain2").setDest("TIMING-DESCRIPTION-EVENT-CHAIN")
        assert constraint.addScope(ref1) is constraint
        assert constraint.addScope(ref2) is constraint
        scopes = constraint.getScopes()
        assert len(scopes) == 2
        assert scopes[0] is ref1
        assert scopes[1] is ref2

    def test_add_scope_none_is_no_op(self):
        constraint = SynchronizationTimingConstraint(self._parent(), "Sync1")
        assert constraint.addScope(None) is constraint
        assert constraint.getScopes() == []

    def test_add_scope_event(self):
        constraint = SynchronizationTimingConstraint(self._parent(), "Sync1")
        ref1 = RefType().setValue("/Pkg/Event1").setDest("TIMING-DESCRIPTION-EVENT")
        ref2 = RefType().setValue("/Pkg/Event2").setDest("TIMING-DESCRIPTION-EVENT")
        assert constraint.addScopeEvent(ref1) is constraint
        assert constraint.addScopeEvent(ref2) is constraint
        events = constraint.getScopeEvents()
        assert len(events) == 2
        assert events[0] is ref1
        assert events[1] is ref2

    def test_add_scope_event_none_is_no_op(self):
        constraint = SynchronizationTimingConstraint(self._parent(), "Sync1")
        assert constraint.addScopeEvent(None) is constraint
        assert constraint.getScopeEvents() == []

    def test_get_set_synchronization_constraint_type(self):
        constraint = SynchronizationTimingConstraint(self._parent(), "Sync1")
        sync_type = SynchronizationTypeEnum().setValue(SynchronizationTypeEnum.STIMULUS_SYNCHRONIZATION)
        assert constraint.setSynchronizationConstraintType(sync_type) is constraint
        assert constraint.getSynchronizationConstraintType() is sync_type
        assert constraint.getSynchronizationConstraintType().getValue() == "stimulusSynchronization"

    def test_set_synchronization_constraint_type_none_is_no_op(self):
        constraint = SynchronizationTimingConstraint(self._parent(), "Sync1")
        sync_type = SynchronizationTypeEnum().setValue(SynchronizationTypeEnum.RESPONSE_SYNCHRONIZATION)
        constraint.setSynchronizationConstraintType(sync_type)
        constraint.setSynchronizationConstraintType(None)
        assert constraint.getSynchronizationConstraintType() is sync_type

    def test_get_set_tolerance(self):
        constraint = SynchronizationTimingConstraint(self._parent(), "Sync1")
        tolerance = self._mdt()
        assert constraint.setTolerance(tolerance) is constraint
        assert constraint.getTolerance() is tolerance
        assert constraint.getTolerance().getCseCode().getValue() == "0"
        assert constraint.getTolerance().getCseCodeFactor().getValue() == 50

    def test_set_tolerance_none_is_no_op(self):
        constraint = SynchronizationTimingConstraint(self._parent(), "Sync1")
        tolerance = self._mdt()
        constraint.setTolerance(tolerance)
        constraint.setTolerance(None)
        assert constraint.getTolerance() is tolerance


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
