"""
This module contains tests for the LatencyTimingConstraint related classes in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint import (
    LatencyConstraintTypeEnum,
    LatencyTimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Integer,
    RefType,
)


class TestLatencyTimingConstraint:
    """
    Test class for LatencyTimingConstraint functionality.
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
        constraint = LatencyTimingConstraint(self._parent(), "Latency1")
        assert isinstance(constraint, LatencyTimingConstraint)
        assert constraint.getShortName() == "Latency1"
        assert constraint.getTimingConditionRef() is None
        assert constraint.getLatencyConstraintType() is None
        assert constraint.getMaximum() is None
        assert constraint.getMinimum() is None
        assert constraint.getNominal() is None
        assert constraint.getScopeRef() is None

    def test_get_set_latency_constraint_type(self):
        constraint = LatencyTimingConstraint(self._parent(), "Latency1")
        latency_type = LatencyConstraintTypeEnum().setValue(LatencyConstraintTypeEnum.REACTION)
        assert constraint.setLatencyConstraintType(latency_type) is constraint
        assert constraint.getLatencyConstraintType() is latency_type
        assert constraint.getLatencyConstraintType().getValue() == "reaction"

    def test_set_latency_constraint_type_none_is_no_op(self):
        constraint = LatencyTimingConstraint(self._parent(), "Latency1")
        latency_type = LatencyConstraintTypeEnum().setValue(LatencyConstraintTypeEnum.AGE)
        constraint.setLatencyConstraintType(latency_type)
        constraint.setLatencyConstraintType(None)
        assert constraint.getLatencyConstraintType() is latency_type

    def test_get_set_maximum(self):
        constraint = LatencyTimingConstraint(self._parent(), "Latency1")
        maximum = self._mdt()
        assert constraint.setMaximum(maximum) is constraint
        assert constraint.getMaximum() is maximum
        assert constraint.getMaximum().getCseCodeFactor().getValue() == 50

    def test_set_maximum_none_is_no_op(self):
        constraint = LatencyTimingConstraint(self._parent(), "Latency1")
        maximum = self._mdt()
        constraint.setMaximum(maximum)
        constraint.setMaximum(None)
        assert constraint.getMaximum() is maximum

    def test_get_set_minimum(self):
        constraint = LatencyTimingConstraint(self._parent(), "Latency1")
        minimum = self._mdt()
        assert constraint.setMinimum(minimum) is constraint
        assert constraint.getMinimum() is minimum

    def test_set_minimum_none_is_no_op(self):
        constraint = LatencyTimingConstraint(self._parent(), "Latency1")
        minimum = self._mdt()
        constraint.setMinimum(minimum)
        constraint.setMinimum(None)
        assert constraint.getMinimum() is minimum

    def test_get_set_nominal(self):
        constraint = LatencyTimingConstraint(self._parent(), "Latency1")
        nominal = self._mdt()
        assert constraint.setNominal(nominal) is constraint
        assert constraint.getNominal() is nominal

    def test_set_nominal_none_is_no_op(self):
        constraint = LatencyTimingConstraint(self._parent(), "Latency1")
        nominal = self._mdt()
        constraint.setNominal(nominal)
        constraint.setNominal(None)
        assert constraint.getNominal() is nominal

    def test_get_set_scope_ref(self):
        constraint = LatencyTimingConstraint(self._parent(), "Latency1")
        ref = RefType().setValue("/Pkg/Chain").setDest("TIMING-DESCRIPTION-EVENT-CHAIN")
        assert constraint.setScopeRef(ref) is constraint
        assert constraint.getScopeRef() is ref
        assert constraint.getScopeRef().getValue() == "/Pkg/Chain"
        assert constraint.getScopeRef().getDest() == "TIMING-DESCRIPTION-EVENT-CHAIN"

    def test_set_scope_ref_none_is_no_op(self):
        constraint = LatencyTimingConstraint(self._parent(), "Latency1")
        ref = RefType().setValue("/Pkg/Chain").setDest("TIMING-DESCRIPTION-EVENT-CHAIN")
        constraint.setScopeRef(ref)
        constraint.setScopeRef(None)
        assert constraint.getScopeRef() is ref


class TestLatencyConstraintTypeEnum:
    def test_initialization(self):
        """Test LatencyConstraintTypeEnum initialization"""
        enum = LatencyConstraintTypeEnum()
        assert isinstance(enum, LatencyConstraintTypeEnum)
        assert list(enum.getEnumValues()) == ["age", "reaction"]

    def test_enum_values(self):
        """Test LatencyConstraintTypeEnum literal values (Table 3.58)"""
        assert LatencyConstraintTypeEnum.AGE == "age"
        assert LatencyConstraintTypeEnum.REACTION == "reaction"

    def test_valid_values(self):
        """Test LatencyConstraintTypeEnum setValue round-trip for all literals"""
        enum = LatencyConstraintTypeEnum()
        for member in [LatencyConstraintTypeEnum.AGE, LatencyConstraintTypeEnum.REACTION]:
            assert enum.setValue(member).getValue() == member
