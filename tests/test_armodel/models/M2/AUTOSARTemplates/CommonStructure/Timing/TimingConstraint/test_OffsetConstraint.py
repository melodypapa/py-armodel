"""
This module contains tests for the OffsetTimingConstraint class in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.OffsetConstraint import (
    OffsetTimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Integer,
    RefType,
)


class TestOffsetTimingConstraint:
    """
    Test class for OffsetTimingConstraint functionality.
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
        constraint = OffsetTimingConstraint(self._parent(), "Offset1")
        assert isinstance(constraint, OffsetTimingConstraint)
        assert constraint.getShortName() == "Offset1"
        assert constraint.getTimingConditionRef() is None
        assert constraint.getMaximum() is None
        assert constraint.getMinimum() is None
        assert constraint.getSourceRef() is None
        assert constraint.getTargetRef() is None

    def test_get_set_maximum(self):
        constraint = OffsetTimingConstraint(self._parent(), "Offset1")
        maximum = self._mdt()
        assert constraint.setMaximum(maximum) is constraint
        assert constraint.getMaximum() is maximum
        assert constraint.getMaximum().getCseCodeFactor().getValue() == 50

    def test_set_maximum_none_is_no_op(self):
        constraint = OffsetTimingConstraint(self._parent(), "Offset1")
        maximum = self._mdt()
        constraint.setMaximum(maximum)
        constraint.setMaximum(None)
        assert constraint.getMaximum() is maximum

    def test_get_set_minimum(self):
        constraint = OffsetTimingConstraint(self._parent(), "Offset1")
        minimum = self._mdt()
        assert constraint.setMinimum(minimum) is constraint
        assert constraint.getMinimum() is minimum

    def test_set_minimum_none_is_no_op(self):
        constraint = OffsetTimingConstraint(self._parent(), "Offset1")
        minimum = self._mdt()
        constraint.setMinimum(minimum)
        constraint.setMinimum(None)
        assert constraint.getMinimum() is minimum

    def test_get_set_source_ref(self):
        constraint = OffsetTimingConstraint(self._parent(), "Offset1")
        ref = RefType().setValue("/Pkg/SourceEvent").setDest("TIMING-DESCRIPTION-EVENT")
        assert constraint.setSourceRef(ref) is constraint
        assert constraint.getSourceRef() is ref
        assert constraint.getSourceRef().getValue() == "/Pkg/SourceEvent"
        assert constraint.getSourceRef().getDest() == "TIMING-DESCRIPTION-EVENT"

    def test_set_source_ref_none_is_no_op(self):
        constraint = OffsetTimingConstraint(self._parent(), "Offset1")
        ref = RefType().setValue("/Pkg/SourceEvent").setDest("TIMING-DESCRIPTION-EVENT")
        constraint.setSourceRef(ref)
        constraint.setSourceRef(None)
        assert constraint.getSourceRef() is ref

    def test_get_set_target_ref(self):
        constraint = OffsetTimingConstraint(self._parent(), "Offset1")
        ref = RefType().setValue("/Pkg/TargetEvent").setDest("TIMING-DESCRIPTION-EVENT")
        assert constraint.setTargetRef(ref) is constraint
        assert constraint.getTargetRef() is ref
        assert constraint.getTargetRef().getValue() == "/Pkg/TargetEvent"
        assert constraint.getTargetRef().getDest() == "TIMING-DESCRIPTION-EVENT"

    def test_set_target_ref_none_is_no_op(self):
        constraint = OffsetTimingConstraint(self._parent(), "Offset1")
        ref = RefType().setValue("/Pkg/TargetEvent").setDest("TIMING-DESCRIPTION-EVENT")
        constraint.setTargetRef(ref)
        constraint.setTargetRef(None)
        assert constraint.getTargetRef() is ref


class TestOffsetTimingConstraintSpecContract:
    """Table 3.66 (AUTOSAR_CP_TPS_TimingExtensions, p.114) spec contract
    for OffsetTimingConstraint."""

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 3.66 Note verbatim.
        """
        assert OffsetTimingConstraint.__doc__.strip() == (
            "Bounds the time offset between the occurrence of two timing events, without requiring a direct functional dependency "
            "between the source and the target . If the target event occurs, it is expected to occur earliest with the minimum , "
            "and latest with the maximum offset relatively after the occurrence of the source event. Note: not every source event "
            "occurrence shall be followed by a target event occurrence. In contrast to LatencyTimingConstraint , there shall not "
            "necessarily be a causal dependency between the source and target event."
        )

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert OffsetTimingConstraint.__init__.__doc__ is None

    def test_base_is_timing_constraint(self):
        """
        Test that the Base per Table 3.66 is TimingConstraint (most-derived —
        the concrete constraint aggregates into TimingExtension.timingGuarantee/
        timingRequirement, not an ARElement).
        """
        from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import Traceable

        assert issubclass(OffsetTimingConstraint, TimingConstraint)
        assert issubclass(OffsetTimingConstraint, Traceable)
        assert not issubclass(OffsetTimingConstraint, MultidimensionalTime)

    def test_maximum_minimum_typed_optional_multidimensional_time(self):
        """
        Test that maximum/minimum (MultidimensionalTime, 0..1 aggr) are typed
        Optional[MultidimensionalTime] accessor pairs.
        """
        for getter, setter in ((OffsetTimingConstraint.getMaximum, OffsetTimingConstraint.setMaximum), (OffsetTimingConstraint.getMinimum, OffsetTimingConstraint.setMinimum)):
            getter_hints = typing.get_type_hints(getter)
            assert getter_hints.get("return") == typing.Optional[MultidimensionalTime]

            setter_hints = typing.get_type_hints(setter)
            assert setter_hints.get("value") == typing.Optional[MultidimensionalTime]
            assert setter_hints.get("return") is OffsetTimingConstraint

    def test_source_target_typed_optional_ref_type(self):
        """
        Test that source/target (TimingDescriptionEvent, 0..1 ref) map to
        Optional[RefType] accessor pairs (Kind ref suffix per Rule 0001.5).
        """
        for getter, setter in ((OffsetTimingConstraint.getSourceRef, OffsetTimingConstraint.setSourceRef), (OffsetTimingConstraint.getTargetRef, OffsetTimingConstraint.setTargetRef)):
            getter_hints = typing.get_type_hints(getter)
            assert getter_hints.get("return") == typing.Optional[RefType]

            setter_hints = typing.get_type_hints(setter)
            assert setter_hints.get("value") == typing.Optional[RefType]
            assert setter_hints.get("return") is OffsetTimingConstraint

    def test_getter_docstrings_are_notes_verbatim(self):
        """
        Test that getter docstrings are the Table 3.66 Notes verbatim without the Tags suffix.
        """
        assert OffsetTimingConstraint.getMaximum.__doc__.strip() == "The maximum offset the target event occurs relatively after the occurrence of the source event."
        assert OffsetTimingConstraint.getMinimum.__doc__.strip() == "The mimum offset the target event occurs relatively after the occurrence of the source event."
        assert OffsetTimingConstraint.getSourceRef.__doc__.strip() == "The timing event that the target event is to be synchronized with."
        assert OffsetTimingConstraint.getTargetRef.__doc__.strip() == "The timing event which is expected to occur timely after the source event."

    def test_setter_docstrings_are_notes_with_none_noop(self):
        """
        Test that setter docstrings are the Table 3.66 Notes verbatim plus the None-no-op sentence.
        """
        assert OffsetTimingConstraint.setMaximum.__doc__.strip() == (
            "The maximum offset the target event occurs relatively after the occurrence of the source event. " "A None value is a no-op and does not overwrite an existing maximum."
        )
        assert OffsetTimingConstraint.setMinimum.__doc__.strip() == (
            "The mimum offset the target event occurs relatively after the occurrence of the source event. " "A None value is a no-op and does not overwrite an existing minimum."
        )
        assert OffsetTimingConstraint.setSourceRef.__doc__.strip() == (
            "The timing event that the target event is to be synchronized with. " "A None value is a no-op and does not overwrite an existing source."
        )
        assert OffsetTimingConstraint.setTargetRef.__doc__.strip() == (
            "The timing event which is expected to occur timely after the source event. " "A None value is a no-op and does not overwrite an existing target."
        )
