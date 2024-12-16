from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, String

from typing import List

class InfrastructureServices(ARObject):
    def __init__(self):
        super().__init__()

        self.doIpEntity = None                                      # type: DoIpEntity
        self.timeSynchronization = None                             # type: TimeSynchronization

    def getDoIpEntity(self):
        return self.doIpEntity

    def setDoIpEntity(self, value):
        self.doIpEntity = value
        return self

    def getTimeSynchronization(self):
        return self.timeSynchronization

    def setTimeSynchronization(self, value):
        self.timeSynchronization = value
        return self

class NetworkEndpoint(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.fullyQualifiedDomainName = None                        # type: String
        self.infrastructureServices = None                          # type: InfrastructureServices
        self.ipSecConfig = None                                     # type: IPSecConfig
        self.networkEndpointAddresses = []                          # type: List[NetworkEndpointAddress]
        self.priority = None                                        # type: PositiveInteger

    def getFullyQualifiedDomainName(self):
        return self.fullyQualifiedDomainName

    def setFullyQualifiedDomainName(self, value):
        self.fullyQualifiedDomainName = value
        return self

    def getInfrastructureServices(self):
        return self.infrastructureServices

    def setInfrastructureServices(self, value):
        self.infrastructureServices = value
        return self

    def getIpSecConfig(self):
        return self.ipSecConfig

    def setIpSecConfig(self, value):
        self.ipSecConfig = value
        return self

    def getNetworkEndpointAddresses(self):
        return self.networkEndpointAddresses

    def setNetworkEndpointAddresses(self, value):
        self.networkEndpointAddresses = value
        return self

    def getPriority(self):
        return self.priority

    def setPriority(self, value):
        self.priority = value
        return self