"""
This module contains tests for the TimingConditionFormula class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingConditionFormula import (
    TimingConditionFormula,
)


class TestTimingConditionFormula:
    """
    Test class for TimingConditionFormula functionality.
    """

    def test_initialization(self):
        obj = TimingConditionFormula()
        assert isinstance(obj, TimingConditionFormula)
