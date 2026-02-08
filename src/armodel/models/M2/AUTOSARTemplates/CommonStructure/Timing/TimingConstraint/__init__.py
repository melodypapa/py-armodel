"""
This module contains timing constraint-related classes for AUTOSAR models.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.AgeConstraint import (
    AgeConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import (
    ArbitraryEventTriggering,
    BurstPatternEventTriggering,
    ConcretePatternEventTriggering,
    ConfidenceInterval,
    EventTriggeringConstraint,
    PeriodicEventTriggering,
    SporadicEventTriggering,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCExecutableEntityRef,
    EOCExecutableEntityRefAbstract,
    ExecutionOrderConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionTimeConstraint import (
    ExecutionTimeConstraint,
    ExecutionTimeTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.LatencyTimingConstraint import (
    LatencyConstraintTypeEnum,
    LatencyTimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.OffsetConstraint import (
    OffsetTimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationPointConstraint import (
    SynchronizationPointConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import (
    EventOccurrenceKindEnum,
    SynchronizationTimingConstraint,
    SynchronizationTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import (
    SwcTiming,
    TimingExtension,
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
