"""
This module contains tests for the ExecutionTimeConstraint related classes in the
AUTOSAR CommonStructure.Timing.TimingConstraint module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionTimeConstraint import (
    ExecutionTimeConstraint,
    ExecutionTimeTypeEnum,
)


class TestExecutionTimeConstraint:
    """
    Test class for ExecutionTimeConstraint functionality.
    """

    def test_initialization(self):
        parent = AUTOSAR.getInstance().createARPackage("ExecTimePkg")
        obj = ExecutionTimeConstraint(parent, "ExecTime")
        assert obj.getShortName() == "ExecTime"


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
