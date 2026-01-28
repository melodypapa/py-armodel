"""
This module contains timing constraint-related classes for AUTOSAR models.
"""

from .TimingConstraint import TimingConstraint
from .ExecutionOrderConstraint import EOCExecutableEntityRefAbstract, EOCExecutableEntityRef, ExecutionOrderConstraint
from .TimingExtensions import TimingExtension, SwcTiming
from .AgeConstraint import AgeConstraint
from .ExecutionTimeConstraint import ExecutionTimeConstraint, ExecutionTimeTypeEnum
from .LatencyTimingConstraint import LatencyTimingConstraint, LatencyConstraintTypeEnum
from .OffsetConstraint import OffsetTimingConstraint
from .SynchronizationPointConstraint import SynchronizationPointConstraint
from .SynchronizationTiming import SynchronizationTimingConstraint, SynchronizationTypeEnum, EventOccurrenceKindEnum
from .EventTriggeringConstraint import (
    EventTriggeringConstraint,
    PeriodicEventTriggering,
    SporadicEventTriggering,
    ArbitraryEventTriggering,
    BurstPatternEventTriggering,
    ConcretePatternEventTriggering,
    ConfidenceInterval,
)

__all__ = [
    'TimingConstraint',
    'EOCExecutableEntityRefAbstract',
    'EOCExecutableEntityRef',
    'ExecutionOrderConstraint',
    'TimingExtension',
    'SwcTiming',
    'AgeConstraint',
    'ExecutionTimeConstraint',
    'ExecutionTimeTypeEnum',
    'LatencyTimingConstraint',
    'LatencyConstraintTypeEnum',
    'OffsetTimingConstraint',
    'SynchronizationPointConstraint',
    'SynchronizationTimingConstraint',
    'SynchronizationTypeEnum',
    'EventOccurrenceKindEnum',
    'EventTriggeringConstraint',
    'PeriodicEventTriggering',
    'SporadicEventTriggering',
    'ArbitraryEventTriggering',
    'BurstPatternEventTriggering',
    'ConcretePatternEventTriggering',
    'ConfidenceInterval',
]