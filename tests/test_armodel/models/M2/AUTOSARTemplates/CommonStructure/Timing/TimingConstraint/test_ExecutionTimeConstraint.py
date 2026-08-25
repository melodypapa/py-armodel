"""
This module contains tests for the ExecutionTimeConstraint related classes in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingCondition import ComponentInCompositionInstanceRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionTimeConstraint import (
    ExecutionTimeConstraint,
    ExecutionTimeTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Integer,
    RefType,
)


class TestExecutionTimeConstraint:
    """
    Test class for ExecutionTimeConstraint functionality.
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
        constraint = ExecutionTimeConstraint(self._parent(), "ExecTime1")
        assert isinstance(constraint, ExecutionTimeConstraint)
        assert constraint.getShortName() == "ExecTime1"
        assert constraint.getTimingConditionRef() is None
        assert constraint.getComponentIRef() is None
        assert constraint.getExecutableRef() is None
        assert constraint.getExecutionTimeType() is None
        assert constraint.getMaximum() is None
        assert constraint.getMinimum() is None

    def test_get_set_component_iref(self):
        constraint = ExecutionTimeConstraint(self._parent(), "ExecTime1")
        iref = ComponentInCompositionInstanceRef()
        iref.setTargetComponentRef(RefType().setValue("/AUTOSAR/Comp/SwcProto").setDest("SW-COMPONENT-PROTOTYPE"))
        assert constraint.setComponentIRef(iref) is constraint
        assert constraint.getComponentIRef() is iref
        assert constraint.getComponentIRef().getTargetComponentRef().getValue() == "/AUTOSAR/Comp/SwcProto"
        assert constraint.getComponentIRef().getTargetComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"

    def test_set_component_iref_none_is_no_op(self):
        constraint = ExecutionTimeConstraint(self._parent(), "ExecTime1")
        iref = ComponentInCompositionInstanceRef()
        iref.setTargetComponentRef(RefType().setValue("/AUTOSAR/Comp/SwcProto").setDest("SW-COMPONENT-PROTOTYPE"))
        constraint.setComponentIRef(iref)
        constraint.setComponentIRef(None)
        assert constraint.getComponentIRef() is iref

    def test_get_set_executable_ref(self):
        constraint = ExecutionTimeConstraint(self._parent(), "ExecTime1")
        ref = RefType().setValue("/AUTOSAR/Runnable").setDest("RUNNABLE-ENTITY")
        assert constraint.setExecutableRef(ref) is constraint
        assert constraint.getExecutableRef() is ref
        assert constraint.getExecutableRef().getValue() == "/AUTOSAR/Runnable"
        assert constraint.getExecutableRef().getDest() == "RUNNABLE-ENTITY"

    def test_set_executable_ref_none_is_no_op(self):
        constraint = ExecutionTimeConstraint(self._parent(), "ExecTime1")
        ref = RefType().setValue("/AUTOSAR/Runnable").setDest("RUNNABLE-ENTITY")
        constraint.setExecutableRef(ref)
        constraint.setExecutableRef(None)
        assert constraint.getExecutableRef() is ref

    def test_get_set_execution_time_type(self):
        constraint = ExecutionTimeConstraint(self._parent(), "ExecTime1")
        exec_type = ExecutionTimeTypeEnum().setValue(ExecutionTimeTypeEnum.NET)
        assert constraint.setExecutionTimeType(exec_type) is constraint
        assert constraint.getExecutionTimeType() is exec_type
        assert constraint.getExecutionTimeType().getValue() == "net"

    def test_set_execution_time_type_none_is_no_op(self):
        constraint = ExecutionTimeConstraint(self._parent(), "ExecTime1")
        exec_type = ExecutionTimeTypeEnum().setValue(ExecutionTimeTypeEnum.GROSS)
        constraint.setExecutionTimeType(exec_type)
        constraint.setExecutionTimeType(None)
        assert constraint.getExecutionTimeType() is exec_type

    def test_get_set_maximum(self):
        constraint = ExecutionTimeConstraint(self._parent(), "ExecTime1")
        maximum = self._mdt()
        assert constraint.setMaximum(maximum) is constraint
        assert constraint.getMaximum() is maximum
        assert constraint.getMaximum().getCseCodeFactor().getValue() == 50

    def test_set_maximum_none_is_no_op(self):
        constraint = ExecutionTimeConstraint(self._parent(), "ExecTime1")
        maximum = self._mdt()
        constraint.setMaximum(maximum)
        constraint.setMaximum(None)
        assert constraint.getMaximum() is maximum

    def test_get_set_minimum(self):
        constraint = ExecutionTimeConstraint(self._parent(), "ExecTime1")
        minimum = self._mdt()
        assert constraint.setMinimum(minimum) is constraint
        assert constraint.getMinimum() is minimum

    def test_set_minimum_none_is_no_op(self):
        constraint = ExecutionTimeConstraint(self._parent(), "ExecTime1")
        minimum = self._mdt()
        constraint.setMinimum(minimum)
        constraint.setMinimum(None)
        assert constraint.getMinimum() is minimum


class TestExecutionTimeTypeEnum:
    def test_initialization(self):
        """Test ExecutionTimeTypeEnum initialization"""
        enum = ExecutionTimeTypeEnum()
        assert isinstance(enum, ExecutionTimeTypeEnum)
        assert list(enum.getEnumValues()) == ["gross", "net"]

    def test_enum_values(self):
        """Test ExecutionTimeTypeEnum literal values (Table 3.76)"""
        assert ExecutionTimeTypeEnum.GROSS == "gross"
        assert ExecutionTimeTypeEnum.NET == "net"

    def test_valid_values(self):
        """Test ExecutionTimeTypeEnum setValue round-trip for all literals"""
        enum = ExecutionTimeTypeEnum()
        for member in [ExecutionTimeTypeEnum.GROSS, ExecutionTimeTypeEnum.NET]:
            assert enum.setValue(member).getValue() == member
