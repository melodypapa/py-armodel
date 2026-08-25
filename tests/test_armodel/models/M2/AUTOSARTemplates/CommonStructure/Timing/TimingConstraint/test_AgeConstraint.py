"""
This module contains tests for the AgeConstraint class in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.AgeConstraint import (
    AgeConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Integer,
    RefType,
)


class TestAgeConstraint:
    """
    Test class for AgeConstraint functionality.
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
        constraint = AgeConstraint(self._parent(), "Age1")
        assert isinstance(constraint, AgeConstraint)
        assert constraint.getShortName() == "Age1"
        assert constraint.getTimingConditionRef() is None
        assert constraint.getMaximum() is None
        assert constraint.getMinimum() is None
        assert constraint.getScopeRef() is None

    def test_get_set_maximum(self):
        constraint = AgeConstraint(self._parent(), "Age1")
        maximum = self._mdt()
        assert constraint.setMaximum(maximum) is constraint
        assert constraint.getMaximum() is maximum
        assert constraint.getMaximum().getCseCodeFactor().getValue() == 50

    def test_set_maximum_none_is_no_op(self):
        constraint = AgeConstraint(self._parent(), "Age1")
        maximum = self._mdt()
        constraint.setMaximum(maximum)
        constraint.setMaximum(None)
        assert constraint.getMaximum() is maximum

    def test_get_set_minimum(self):
        constraint = AgeConstraint(self._parent(), "Age1")
        minimum = self._mdt()
        assert constraint.setMinimum(minimum) is constraint
        assert constraint.getMinimum() is minimum

    def test_set_minimum_none_is_no_op(self):
        constraint = AgeConstraint(self._parent(), "Age1")
        minimum = self._mdt()
        constraint.setMinimum(minimum)
        constraint.setMinimum(None)
        assert constraint.getMinimum() is minimum

    def test_get_set_scope_ref(self):
        constraint = AgeConstraint(self._parent(), "Age1")
        ref = RefType().setValue("/Pkg/TdEvent").setDest("TIMING-DESCRIPTION-EVENT")
        assert constraint.setScopeRef(ref) is constraint
        assert constraint.getScopeRef() is ref
        assert constraint.getScopeRef().getValue() == "/Pkg/TdEvent"
        assert constraint.getScopeRef().getDest() == "TIMING-DESCRIPTION-EVENT"

    def test_set_scope_ref_none_is_no_op(self):
        constraint = AgeConstraint(self._parent(), "Age1")
        ref = RefType().setValue("/Pkg/TdEvent").setDest("TIMING-DESCRIPTION-EVENT")
        constraint.setScopeRef(ref)
        constraint.setScopeRef(None)
        assert constraint.getScopeRef() is ref
