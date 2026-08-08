"""
This module contains tests for the TDLETZoneClock class in the
AUTOSAR CommonStructure.Timing.TimingClock module.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.TDLETZoneClock import (
    TDLETZoneClock,
)


class TestTDLETZoneClock:
    """
    Test class for TDLETZoneClock functionality.
    """

    def test_initialization(self):
        obj = TDLETZoneClock()
        assert isinstance(obj, TDLETZoneClock)
