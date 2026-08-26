"""
This module contains tests for the OffsetTimingConstraint class in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
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
