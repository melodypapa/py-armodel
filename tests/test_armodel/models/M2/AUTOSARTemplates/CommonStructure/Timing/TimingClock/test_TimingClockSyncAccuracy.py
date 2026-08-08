"""
This module contains tests for the TimingClockSyncAccuracy class in the
AUTOSAR CommonStructure.Timing.TimingClock module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.TimingClockSyncAccuracy import (
    TimingClockSyncAccuracy,
)


class TestTimingClockSyncAccuracy:
    """
    Test class for TimingClockSyncAccuracy functionality.
    """

    def test_initialization(self):
        obj = TimingClockSyncAccuracy()
        assert isinstance(obj, TimingClockSyncAccuracy)
