"""
V2 M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster package.
"""

from .BinaryManifest import *

# Classes:
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.ClientServerOperationComProps import ClientServerOperationComProps
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.CpSoftwareCluster import CpSoftwareCluster
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.CpSoftwareClusterCommunicationResource import CpSoftwareClusterCommunicationResource
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.CpSoftwareClusterCommunicationResourceProps import CpSoftwareClusterCommunicationResourceProps
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.CpSoftwareClusterMappingSet import CpSoftwareClusterMappingSet
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.CpSoftwareClusterResource import CpSoftwareClusterResource
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.CpSoftwareClusterResourcePool import CpSoftwareClusterResourcePool
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.CpSoftwareClusterResourceToApplicationPartitionMapping import CpSoftwareClusterResourceToApplicationPartitionMapping
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.CpSoftwareClusterServiceResource import CpSoftwareClusterServiceResource
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.CpSoftwareClusterToApplicationPartitionMapping import CpSoftwareClusterToApplicationPartitionMapping
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.CpSoftwareClusterToEcuInstanceMapping import CpSoftwareClusterToEcuInstanceMapping
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.CpSoftwareClusterToResourceMapping import CpSoftwareClusterToResourceMapping
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DataComProps import DataComProps
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.RoleBasedResourceDependency import RoleBasedResourceDependency
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SwComponentPrototypeAssignment import SwComponentPrototypeAssignment
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SystemSignalGroupToCommunicationResourceMapping import SystemSignalGroupToCommunicationResourceMapping
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SystemSignalToCommunicationResourceMapping import SystemSignalToCommunicationResourceMapping

__all__ = [
    # .BinaryManifest.*,
    "ClientServerOperationComProps",
    "CpSoftwareCluster",
    "CpSoftwareClusterCommunicationResource",
    "CpSoftwareClusterCommunicationResourceProps",
    "CpSoftwareClusterMappingSet",
    "CpSoftwareClusterResource",
    "CpSoftwareClusterResourcePool",
    "CpSoftwareClusterResourceToApplicationPartitionMapping",
    "CpSoftwareClusterServiceResource",
    "CpSoftwareClusterToApplicationPartitionMapping",
    "CpSoftwareClusterToEcuInstanceMapping",
    "CpSoftwareClusterToResourceMapping",
    "DataComProps",
    "DataConsistencyPolicyEnum",
    "RoleBasedResourceDependency",
    "SendIndicationEnum",
    "SwComponentPrototypeAssignment",
    "SystemSignalGroupToCommunicationResourceMapping",
    "SystemSignalToCommunicationResourceMapping",
]
