"""
This module contains tests for the SynchronizationTiming related classes in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import (
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


class TestSynchronizationTimingConstraintSpecContract:
    """Table 3.54 (AUTOSAR_CP_TPS_TimingExtensions, p.92) spec contract
    for SynchronizationTimingConstraint."""

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 3.54 Note verbatim (the
        markdown's stray leading "Constraint " PDF label artifact dropped, its
        tail "interval are permitted." — cut by an inline image — restored from
        the XSD group documentation; the section-level [constr_] paragraphs are
        not part of the Note row).
        """
        assert SynchronizationTimingConstraint.__doc__.strip() == (
            "This constraint is used to restrict the timing behavior of different, but correlated events or event chains, with regard to synchronization. "
            "Two scenarios are supported: • If ( synchronizationConstraintType == responseSynchronization ) - TimingDescriptionEvent s: An arbitrary number of correlated events which play the role of responses shall occur synchronously with respect to a predefined tolerance. "
            "- TimingDescriptionEventChain s: An arbitrary number of correlated event chains with a common stimulus, but different responses, where the responses shall occur synchronously with respect to a predefined tolerance. "
            "• If ( synchronizationConstraintType == stimulusSynchronization ) - TimingDescriptionEvent s:An arbitrary number of correlated events which play the role of stimuli shall occur synchronously with respect to a predefined tolerance. "
            "- TimingDescriptionEventChain s: An arbitrary number of correlated event chains with a common response, but different stimuli, where the stimuli shall occur synchronously with respect to a predefined tolerance. "
            "In case the constraint is imposed on events the following two scenarios are supported: • If ( eventOccurrenceKind == singleOccurrence ): any of the events shall occur only once in the given time interval. "
            "• If ( eventOccurrenceKind == multipleOccurrences ): any of the events may occur more than once in the given time interval. "
            "In other words multiple occurrences of an event within the given time interval are permitted."
        )

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert SynchronizationTimingConstraint.__init__.__doc__ is None

    def test_base_is_timing_constraint(self):
        """
        Test that the Base per Table 3.54 is TimingConstraint (most-derived —
        the concrete constraint aggregates into TimingExtension.timingGuarantee/
        timingRequirement, not an ARElement).
        """
        from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import Traceable

        assert issubclass(SynchronizationTimingConstraint, TimingConstraint)
        assert issubclass(SynchronizationTimingConstraint, Traceable)

    def test_event_occurrence_kind_typed_optional_enum(self):
        """
        Test that eventOccurrenceKind (EventOccurrenceKindEnum, 0..1 attr) is an
        Optional[EventOccurrenceKindEnum] accessor pair.
        """
        getter_hints = typing.get_type_hints(SynchronizationTimingConstraint.getEventOccurrenceKind)
        assert getter_hints.get("return") == typing.Optional[EventOccurrenceKindEnum]

        setter_hints = typing.get_type_hints(SynchronizationTimingConstraint.setEventOccurrenceKind)
        assert setter_hints.get("value") == typing.Optional[EventOccurrenceKindEnum]
        assert setter_hints.get("return") is SynchronizationTimingConstraint

    def test_scope_scope_event_typed_ref_lists(self):
        """
        Test that scope/scopeEvent (TimingDescriptionEventChain/TimingDescriptionEvent,
        * ref) map to dedicated List[RefType] fields with add/get accessors
        (Kind `*` ref suffix per Rule 0001.5).
        """
        for adder, getter in (
            (SynchronizationTimingConstraint.addScope, SynchronizationTimingConstraint.getScopes),
            (SynchronizationTimingConstraint.addScopeEvent, SynchronizationTimingConstraint.getScopeEvents),
        ):
            adder_hints = typing.get_type_hints(adder)
            assert adder_hints.get("value") == typing.Optional[RefType]
            assert adder_hints.get("return") is SynchronizationTimingConstraint

            getter_hints = typing.get_type_hints(getter)
            assert getter_hints.get("return") == typing.List[RefType]

    def test_synchronization_constraint_type_typed_optional_enum(self):
        """
        Test that synchronizationConstraintType (SynchronizationTypeEnum, 0..1 attr)
        is an Optional[SynchronizationTypeEnum] accessor pair.
        """
        getter_hints = typing.get_type_hints(SynchronizationTimingConstraint.getSynchronizationConstraintType)
        assert getter_hints.get("return") == typing.Optional[SynchronizationTypeEnum]

        setter_hints = typing.get_type_hints(SynchronizationTimingConstraint.setSynchronizationConstraintType)
        assert setter_hints.get("value") == typing.Optional[SynchronizationTypeEnum]
        assert setter_hints.get("return") is SynchronizationTimingConstraint

    def test_tolerance_typed_optional_multidimensional_time(self):
        """
        Test that tolerance (MultidimensionalTime, 0..1 aggr) is an
        Optional[MultidimensionalTime] accessor pair.
        """
        getter_hints = typing.get_type_hints(SynchronizationTimingConstraint.getTolerance)
        assert getter_hints.get("return") == typing.Optional[MultidimensionalTime]

        setter_hints = typing.get_type_hints(SynchronizationTimingConstraint.setTolerance)
        assert setter_hints.get("value") == typing.Optional[MultidimensionalTime]
        assert setter_hints.get("return") is SynchronizationTimingConstraint

    def test_getter_docstrings_are_notes_verbatim(self):
        """
        Test that getter docstrings are the Table 3.54 Notes verbatim.
        """
        assert (
            SynchronizationTimingConstraint.getEventOccurrenceKind.__doc__.strip()
            == "Indicates whether the referenced events shall occur only once (single occurrence) or multiple times (multiple occurrences) in the given time interval."
        )
        assert SynchronizationTimingConstraint.getScopes.__doc__.strip() == "The event chains that are in the scope of the constraint. Mutually exclusive to scopeEvent , see ([constr_4522])."
        assert SynchronizationTimingConstraint.getScopeEvents.__doc__.strip() == "The events that are in the scope of the constraint. Mutually exclusive to scope , see ([constr_4522])"
        assert (
            SynchronizationTimingConstraint.getSynchronizationConstraintType.__doc__.strip()
            == "Indicates whether the associated events of the SynchronizationTimingConstraint have a common stimulus or response."
        )
        assert (
            SynchronizationTimingConstraint.getTolerance.__doc__.strip()
            == "The maximum time interval, within which the synchronized events shall occur. The events may occur in any order within this time interval. The time interval starts at the point-in-time when one of the referenced events occurs."
        )

    def test_setter_docstrings_are_notes_with_none_noop(self):
        """
        Test that setter/adder docstrings are the Table 3.54 Notes verbatim plus
        the None-no-op sentence.
        """
        assert (
            SynchronizationTimingConstraint.setEventOccurrenceKind.__doc__.strip()
            == "Indicates whether the referenced events shall occur only once (single occurrence) or multiple times (multiple occurrences) in the given time interval. A None value is a no-op and does not overwrite an existing eventOccurrenceKind."
        )
        assert (
            SynchronizationTimingConstraint.addScope.__doc__.strip()
            == "The event chains that are in the scope of the constraint. Mutually exclusive to scopeEvent , see ([constr_4522]). A None value is a no-op."
        )
        assert SynchronizationTimingConstraint.getScopes.__doc__.strip().endswith("see ([constr_4522]).")
        assert (
            SynchronizationTimingConstraint.addScopeEvent.__doc__.strip()
            == "The events that are in the scope of the constraint. Mutually exclusive to scope , see ([constr_4522]) A None value is a no-op."
        )
        assert (
            SynchronizationTimingConstraint.setSynchronizationConstraintType.__doc__.strip()
            == "Indicates whether the associated events of the SynchronizationTimingConstraint have a common stimulus or response. A None value is a no-op and does not overwrite an existing synchronizationConstraintType."
        )
        assert (
            SynchronizationTimingConstraint.setTolerance.__doc__.strip()
            == "The maximum time interval, within which the synchronized events shall occur. The events may occur in any order within this time interval. The time interval starts at the point-in-time when one of the referenced events occurs. A None value is a no-op and does not overwrite an existing tolerance."
        )
