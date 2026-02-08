"""
V2 M2::AUTOSARTemplates::CommonStructure::ResourceConsumption package.
"""

from .ExecutionTime import *
from .HeapUsage import *
from .MemorySectionUsage import *
from .StackUsage import *

# Classes:
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.HardwareConfiguration import HardwareConfiguration
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import ResourceConsumption
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.SoftwareContext import SoftwareContext

__all__ = [
    # .ExecutionTime.*,
    # .HeapUsage.*,
    # .MemorySectionUsage.*,
    # .StackUsage.*,
    "HardwareConfiguration",
    "ResourceConsumption",
    "SoftwareContext",
]
