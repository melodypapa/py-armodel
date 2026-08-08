"""
This module contains tests for the TimingCondition class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingCondition import (
    TimingCondition,
)


class TestTimingCondition:
    """
    Test class for TimingCondition functionality.
    """

    def test_initialization(self):
        obj = TimingCondition()
        assert isinstance(obj, TimingCondition)
