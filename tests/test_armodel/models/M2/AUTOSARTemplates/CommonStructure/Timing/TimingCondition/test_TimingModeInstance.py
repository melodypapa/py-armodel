"""
This module contains tests for the TimingModeInstance class in the
AUTOSAR CommonStructure.Timing.TimingCondition module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingModeInstance import (
    TimingModeInstance,
)


class TestTimingModeInstance:
    """
    Test class for TimingModeInstance functionality.
    """

    def test_initialization(self):
        obj = TimingModeInstance()
        assert isinstance(obj, TimingModeInstance)
