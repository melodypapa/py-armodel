"""
This module contains tests for the TimingClock class in the
AUTOSAR CommonStructure.Timing.TimingClock module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.TimingClock import (
    TimingClock,
)


class TestTimingClock:
    """
    Test class for TimingClock functionality.
    """

    def test_initialization(self):
        obj = TimingClock()
        assert isinstance(obj, TimingClock)
