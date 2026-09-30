"""
This module contains timing-related classes for AUTOSAR models.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    EOCEventRef,
    EOCExecutableEntityRefAbstract,
    EOCExecutableEntityRef,
    EOCExecutableEntityRefGroup,
    ExecutionOrderConstraint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions import (
    TimingExtension,
    SwcTiming,
    BswCompositionTiming,
    BswModuleTiming,
    EcuTiming,
    SystemTiming,
    TDCpSoftwareClusterMappingSet,
    VfbTiming,
)

__all__ = [
    "VfbTiming",
    "TDCpSoftwareClusterMappingSet",
    "SystemTiming",
    "EcuTiming",
    "BswModuleTiming",
    "BswCompositionTiming",
    "TimingConstraint",
    "EOCEventRef",
    "EOCExecutableEntityRefAbstract",
    "EOCExecutableEntityRef",
    "EOCExecutableEntityRefGroup",
    "ExecutionOrderConstraint",
    "TimingExtension",
    "SwcTiming",
]
