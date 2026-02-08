"""
V2 M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock package.
"""
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock import (
    TimingClock,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClockSyncAccuracy import (
    TimingClockSyncAccuracy,
)

from .TDLETZoneClock import TDLETZoneClock

__all__ = [
    "TDLETZoneClock",
    "TimingClock",
    "TimingClockSyncAccuracy",
]
