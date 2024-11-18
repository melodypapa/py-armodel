
from typing import List

from ..GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ..GenericStructure.GeneralTemplateClasses.Identifiable import ARElement

class SystemMapping(Identifiable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.applicationPartitionToEcuPartitionMappings = []
        self.appOsTaskProxyToEcuTaskProxyMappings = []
        self.comManagementMappings = []
        self.cryptoServiceMappings = []
        self.dataMappings = []
        self.ddsISignalToTopicMappings = []
        self.ecuResourceMappings = []
        self.j1939ControllerApplicationToJ1939NmNodeMappings = []
        self.mappingConstraints = []
        self.pncMappings = []
        self.portElementToComResourceMappings = []
        self.resourceEstimations = []
        self.resourceToApplicationPartitionMappings = []
        self.rteEventSeparations = []
        self.rteEventToOsTaskProxyMappings = []
        self.signalPathConstraints = []
        self.softwareClusterToApplicationPartitionMappings = []
        self.softwareClusterToResourceMappings = []
        self.swClusterMappings = []
        self.swcToApplicationPartitionMappings = []
        self.swImplMappings = []
        self.swMappings = []
        self.systemSignalGroupToComResourceMappings = []
        self.systemSignalToComResourceMappings = []

    def getApplicationPartitionToEcuPartitionMappings(self):
        return self.applicationPartitionToEcuPartitionMappings

    def addApplicationPartitionToEcuPartitionMapping(self, value):
        self.applicationPartitionToEcuPartitionMappings.append(value)
        return self

    def getAppOsTaskProxyToEcuTaskProxyMappings(self):
        return self.appOsTaskProxyToEcuTaskProxyMappings

    def addAppOsTaskProxyToEcuTaskProxyMapping(self, value):
        self.appOsTaskProxyToEcuTaskProxyMappings.append(value)
        return self

    def getComManagementMappings(self):
        return self.comManagementMappings

    def addComManagementMapping(self, value):
        self.comManagementMappings.append(value)
        return self

    def getCryptoServiceMappings(self):
        return self.cryptoServiceMappings

    def addCryptoServiceMapping(self, value):
        self.cryptoServiceMappings.append(value)
        return self

    def getDataMappings(self):
        return self.dataMappings

    def addDataMapping(self, value):
        self.dataMappings.append(value)
        return self

    def getDdsISignalToTopicMapping(self):
        return self.ddsISignalToTopicMappings

    def addDdsISignalToTopicMapping(self, value):
        self.ddsISignalToTopicMappings.append(value)
        return self

    def getEcuResourceMappings(self):
        return self.ecuResourceMappings

    def addEcuResourceMapping(self, value):
        self.ecuResourceMappings.append(value)
        return self

    def getJ1939ControllerApplicationToJ1939NmNodeMappings(self):
        return self.j1939ControllerApplicationToJ1939NmNodeMappings

    def addJ1939ControllerApplicationToJ1939NmNodeMapping(self, value):
        self.j1939ControllerApplicationToJ1939NmNodeMappings.append(value)
        return self

    def getMappingConstraints(self):
        return self.mappingConstraints

    def addMappingConstraint(self, value):
        self.mappingConstraints.append(value)
        return self

    def getPncMappings(self):
        return self.pncMappings

    def addPncMapping(self, value):
        self.pncMappings.append(value)
        return self

    def getPortElementToComResourceMappings(self):
        return self.portElementToComResourceMappings

    def addPortElementToComResourceMapping(self, value):
        self.portElementToComResourceMappings.append(value)
        return self

    def getResourceEstimations(self):
        return self.resourceEstimations

    def addResourceEstimation(self, value):
        self.resourceEstimations.append(value)
        return self

    def getResourceToApplicationPartitionMappings(self):
        return self.resourceToApplicationPartitionMappings

    def addResourceToApplicationPartitionMapping(self, value):
        self.resourceToApplicationPartitionMappings.append(value)
        return self

    def getRteEventSeparations(self):
        return self.rteEventSeparations

    def addRteEventSeparation(self, value):
        self.rteEventSeparations.append(value)
        return self

    def getRteEventToOsTaskProxyMappings(self):
        return self.rteEventToOsTaskProxyMappings

    def addRteEventToOsTaskProxyMapping(self, value):
        self.rteEventToOsTaskProxyMappings.append(value)
        return self

    def getSignalPathConstraints(self):
        return self.signalPathConstraints

    def addSignalPathConstraint(self, value):
        self.signalPathConstraints.append(value)
        return self

    def getSoftwareClusterToApplicationPartitionMappings(self):
        return self.softwareClusterToApplicationPartitionMappings

    def addSoftwareClusterToApplicationPartitionMapping(self, value):
        self.softwareClusterToApplicationPartitionMappings.append(value)
        return self

    def getSoftwareClusterToResourceMappings(self):
        return self.softwareClusterToResourceMappings

    def addSoftwareClusterToResourceMapping(self, value):
        self.softwareClusterToResourceMappings.append(value)
        return self

    def getSwClusterMappings(self):
        return self.swClusterMappings

    def addSwClusterMapping(self, value):
        self.swClusterMappings.append(value)
        return self

    def getSwcToApplicationPartitionMappings(self):
        return self.swcToApplicationPartitionMappings

    def addSwcToApplicationPartitionMappings(self, value):
        self.swcToApplicationPartitionMappings.append(value)
        return self

    def getSwImplMapping(self):
        return self.swImplMappings

    def addSwImplMappings(self, value):
        self.swImplMappings.append(value)
        return self

    def getSwMappings(self):
        return self.swMappings

    def addSwMapping(self, value):
        self.swMappings.append(value)
        return self

    def getSystemSignalGroupToComResourceMappings(self):
        return self.systemSignalGroupToComResourceMappings

    def addSystemSignalGroupToComResourceMapping(self, value):
        self.systemSignalGroupToComResourceMappings.append(value)
        return self

    def getSystemSignalToComResourceMappings(self):
        return self.systemSignalToComResourceMappings

    def addSystemSignalToComResourceMapping(self, value):
        self.systemSignalToComResourceMappings.append(value)
        return self


class System(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.clientIdDefinitionSetRefs = []                 # type: List[RefType]
        self.containerIPduHeaderByteOrder = None
        self.ecuExtractVersion = None
        self.fibexElements = []
        self.interpolationRoutineMappingSetRefs = []        # type: List[RefType]
        self.j1939SharedAddressClusters = []
        self.mappings = []                                  # type: List[SystemMapping]
        self.pncVectorLength = None
        self.pncVectorOffset = None
        self.rootSoftwareComposition = None
        self.swClusters = []
        self.systemDocumentation = []
        self.systemVersion = None

    def getClientIdDefinitionSetRefs(self):
        return self.clientIdDefinitionSetRefs

    def addClientIdDefinitionSetRefs(self, value):
        self.clientIdDefinitionSetRefs.append(value)
        return self

    def getContainerIPduHeaderByteOrder(self):
        return self.containerIPduHeaderByteOrder

    def setContainerIPduHeaderByteOrder(self, value):
        self.containerIPduHeaderByteOrder = value
        return self

    def getEcuExtractVersion(self):
        return self.ecuExtractVersion

    def setEcuExtractVersion(self, value):
        self.ecuExtractVersion = value
        return self

    def getFibexElementRefs(self):
        return self.fibexElements

    def addFibexElementRef(self, value):
        self.fibexElements.append(value)
        return self

    def getInterpolationRoutineMappingSetRefs(self):
        return self.interpolationRoutineMappingSetRefs

    def addInterpolationRoutineMappingSetRefs(self, value):
        self.interpolationRoutineMappingSetRefs.append(value)
        return self

    def getJ1939SharedAddressClusters(self):
        return self.j1939SharedAddressClusters

    def setJ1939SharedAddressClusters(self, value):
        self.j1939SharedAddressClusters.append(value)
        return self

    def getMappings(self) -> List[SystemMapping]:
        return list(sorted(filter(lambda a: isinstance(a, SystemMapping), self.elements.values()), key= lambda o:o.short_name))

    def createSystemMapping(self, short_name) -> SystemMapping:
        if (short_name not in self.elements):
            mapping = SystemMapping(self, short_name)
            self.elements[short_name] = mapping
        return self.elements[short_name]

    def getPncVectorLength(self):
        return self.pncVectorLength

    def setPncVectorLength(self, value):
        self.pncVectorLength = value
        return self

    def getPncVectorOffset(self):
        return self.pncVectorOffset

    def setPncVectorOffset(self, value):
        self.pncVectorOffset = value
        return self

    def getRootSoftwareComposition(self):
        return self.rootSoftwareComposition

    def setRootSoftwareComposition(self, value):
        self.rootSoftwareComposition = value
        return self

    def getSwClusters(self):
        return self.swClusters

    def addSwClusters(self, value):
        self.swClusters.append(value)
        return self

    def getSystemDocumentation(self):
        return self.systemDocumentation

    def setSystemDocumentation(self, value):
        self.systemDocumentation = value
        return self

    def getSystemVersion(self):
        return self.systemVersion

    def setSystemVersion(self, value):
        self.systemVersion = value
        return self




   


