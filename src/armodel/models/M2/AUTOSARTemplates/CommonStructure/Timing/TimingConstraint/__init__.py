"""
This module contains timing constraint-related classes for AUTOSAR models.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import TimingConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import EOCExecutableEntityRefAbstract, EOCExecutableEntityRef, ExecutionOrderConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingExtensions import TimingExtension, SwcTiming
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.AgeConstraint import AgeConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionTimeConstraint import ExecutionTimeConstraint, ExecutionTimeTypeEnum
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint import LatencyTimingConstraint, LatencyConstraintTypeEnum
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.OffsetConstraint import OffsetTimingConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationPointConstraint import SynchronizationPointConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import SynchronizationTimingConstraint, SynchronizationTypeEnum, EventOccurrenceKindEnum
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import (
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