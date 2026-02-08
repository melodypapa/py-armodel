"""
V2 M2::AUTOSARTemplates::CommonStructure::ResourceConsumption package.
"""

# Classes:
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.HardwareConfiguration import (
    HardwareConfiguration,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import (
    ResourceConsumption,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime import (
    AnalyzedExecutionTime,
    ExecutionTime,
    MeasuredExecutionTime,
    MemorySectionLocation,
    RoughEstimateOfExecutionTime,
    SimulatedExecutionTime,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import (
    HeapUsage,
    MeasuredHeapUsage,
    RoughEstimateHeapUsage,
    WorstCaseHeapUsage,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import (
    MemorySection,
    SectionNamePrefix,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import (
    MeasuredStackUsage,
    RoughEstimateStackUsage,
    StackUsage,
    WorstCaseStackUsage,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SoftwareContext import (
    SoftwareContext,
)

__all__ = [
    # .ExecutionTime.*,
    # .HeapUsage.*,
    # .MemorySectionUsage.*,
    # .StackUsage.*,
    "HardwareConfiguration",
    "ResourceConsumption",
    "SoftwareContext",
]
