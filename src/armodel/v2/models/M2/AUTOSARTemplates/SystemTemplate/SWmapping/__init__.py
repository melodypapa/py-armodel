"""
V2 M2::AUTOSARTemplates::SystemTemplate::SWmapping package.
"""
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.ApplicationPartition import ApplicationPartition
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.ApplicationPartitionToEcuPartitionMapping import ApplicationPartitionToEcuPartitionMapping
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.ComponentClustering import ComponentClustering
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.ComponentSeparation import ComponentSeparation
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.EcuPartition import EcuPartition
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.EcuResourceEstimation import EcuResourceEstimation
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.J1939ControllerApplication import J1939ControllerApplication
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.J1939ControllerApplicationToJ1939NmNodeMapping import J1939ControllerApplicationToJ1939NmNodeMapping
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.MappingConstraint import MappingConstraint
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SwcToApplicationPartitionMapping import SwcToApplicationPartitionMapping
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SwcToEcuMapping import SwcToEcuMapping
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SwcToImplMapping import SwcToImplMapping

__all__ = [
    "ApplicationPartition",
    "ApplicationPartitionToEcuPartitionMapping",
    "ComponentClustering",
    "ComponentSeparation",
    "EcuPartition",
    "EcuResourceEstimation",
    "J1939ControllerApplication",
    "J1939ControllerApplicationToJ1939NmNodeMapping",
    "MappingConstraint",
    "MappingScopeEnum",
    "SwcToApplicationPartitionMapping",
    "SwcToEcuMapping",
    "SwcToImplMapping",
]
