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

    def test_execution_type_enum_members(self):
        assert ExecutionTimeTypeEnum.BEST_CASE == "best-case"
        assert ExecutionTimeTypeEnum.WORST_CASE == "worst-case"
        assert ExecutionTimeTypeEnum.AVERAGE_CASE == "average-case"
