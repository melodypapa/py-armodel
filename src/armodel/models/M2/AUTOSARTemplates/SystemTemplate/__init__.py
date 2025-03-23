from typing import List

from ....M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataMapping
from ....M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoServiceMapping
from ....M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import AppOsTaskProxyToEcuTaskProxyMapping
from ....M2.AUTOSARTemplates.SystemTemplate.EcuResourceMapping import ECUMapping
from ....M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from ....M2.AUTOSARTemplates.SystemTemplate.SWmapping import ApplicationPartitionToEcuPartitionMapping, SwcToImplMapping
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ByteOrderEnum, PositiveInteger, RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RevisionLabelString, TRefType


class SwcToEcuMapping(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.componentIRefs = []                    # type: List[ComponentInSystemInstanceRef]
        self.controlledHwElementRef = None          # type: RefType
        self.ecuInstanceRef = None                  # type: RefType
        self.processingUnitRef = None               # type: RefType

    def getComponentIRefs(self):
        return self.componentIRefs

    def addComponentIRef(self, value):
        self.componentIRefs.append(value)
        return self

    def getControlledHwElementRef(self):
        return self.controlledHwElementRef

    def setControlledHwElementRef(self, value):
        self.controlledHwElementRef = value
        return self

    def getEcuInstanceRef(self):
        return self.ecuInstanceRef

    def setEcuInstanceRef(self, value):
        self.ecuInstanceRef = value
        return self

    def getProcessingUnitRef(self):
        return self.processingUnitRef

    def setProcessingUnitRef(self, value):
        self.processingUnitRef = value
        return self


class ComManagementMapping(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.comManagementGroupRefs = []            # type: List[RefType]
        self.comManagementPortGroupRefs = []        # type: List[RefType]
        self.physicalChannelRef = None              # type: RefType

    def getComManagementGroupRefs(self):
        return self.comManagementGroupRefs

    def addComManagementGroupRef(self, value):
        if value is not None:
            self.comManagementGroupRefs.append(value)
        return self

    def getComManagementPortGroupRefs(self):
        return self.comManagementPortGroupRefs

    def addComManagementPortGroupRef(self, value):
        if value is not None:
            self.comManagementPortGroupRefs.append(value)
        return self

    def getPhysicalChannelRef(self):
        return self.physicalChannelRef

    def setPhysicalChannelRef(self, value):
        if value is not None:
            self.physicalChannelRef = value
        return self


class SystemMapping(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.applicationPartitionToEcuPartitionMappings = []                            # type: List[ApplicationPartitionToEcuPartitionMapping]
        self.appOsTaskProxyToEcuTaskProxyMappings = []                                  # type: List[AppOsTaskProxyToEcuTaskProxyMapping]
        self.comManagementMappings = []                                                 # type: List[ComManagementMapping]
        self.cryptoServiceMappings = []                                                 # type: List[CryptoServiceMapping]
        self.dataMappings = []                                                          # type: List[DataMapping]
        self.ddsISignalToTopicMappings = []                                             # type: List[DdsCpISignalToDdsTopicMapping]
        self.ecuResourceMappings = []                                                   # type: List[ECUMapping]
        self.j1939ControllerApplicationToJ1939NmNodeMappings = []                       # type: List[J1939ControllerApplicationToJ1939NmNodeMapping]
        self.mappingConstraints = []                                                    # type: List[MappingConstraint]
        self.pncMappings = []                                                           # type: List[PncMapping]
        self.portElementToComResourceMappings = []                                      # type: List[PortElementToCommunicationResourceMapping]
        self.resourceEstimations = []                                                   # type: List[EcuResourceEstimation]
        self.resourceToApplicationPartitionMappings = []                                # type: List[CpSoftwareClusterResourceToApplicationPartitionMapping]
        self.rteEventSeparations = []                                                   # type: List[RteEventInSystemSeparation]
        self.rteEventToOsTaskProxyMappings = []                                         # type: List[RteEventInSystemToOsTaskProxyMapping]
        self.signalPathConstraints = []                                                 # type: List[SignalPathConstraint]
        self.softwareClusterToApplicationPartitionMappings = []                         # type: List[CpSoftwareClusterToApplicationPartitionMapping]
        self.softwareClusterToResourceMappings = []                                     # type: List[CpSoftwareClusterToResourceMapping]
        self.swClusterMappings = []                                                     # type: List[CpSoftwareClusterToEcuInstanceMapping]
        self.swcToApplicationPartitionMappings = []                                     # type: List[SwcToApplicationPartitionMapping]
        self.swImplMappings = []                                                        # type: List[SwcToImplMapping]
        self.swMappings = []                                                            # type: List[SwcToEcuMapping]
        self.systemSignalGroupToComResourceMappings = []                                # type: List[SystemSignalGroupToCommunicationResourceMapping]
        self.systemSignalToComResourceMappings = []                                     # type: List[SystemSignalToCommunicationResourceMapping]

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

    def createECUMapping(self, short_name: str) -> ECUMapping:
        if short_name not in self.elements:
            mapping = ECUMapping(self, short_name)
            self.addElement(mapping)
            self.ecuResourceMappings.append(mapping)
        return self.getElement(short_name)

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

    def getSwImplMappings(self):
        return self.swImplMappings

    def createSwcToImplMapping(self, short_name: str) -> SwcToImplMapping:
        if short_name not in self.elements:
            mapping = SwcToImplMapping(self, short_name)
            self.addElement(mapping)
            self.swImplMappings.append(mapping)
        return self.getElement(short_name)

    def getSwMappings(self):
        return self.swMappings
    
    def getSwcToEcuMappings(self) -> List[SwcToEcuMapping]:
        return list(sorted(filter(lambda a: isinstance(a, SwcToEcuMapping), self.elements), key=lambda o: o.short_name))

    def createSwcToEcuMapping(self, short_name: str) -> SwcToEcuMapping:
        if short_name not in self.elements:
            mapping = SwcToEcuMapping(self, short_name)
            self.addElement(mapping)
            self.swMappings.append(mapping)
        return self.getElement(short_name)

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


class RootSwCompositionPrototype(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.calibrationParameterValueSetRef = None         # type: RefType
        self.flatMapRef = None                              # type: RefType
        self.softwareCompositionTRef = None                 # type: TRefType

    def getCalibrationParameterValueSetRef(self):
        return self.calibrationParameterValueSetRef

    def setCalibrationParameterValueSetRef(self, value):
        self.calibrationParameterValueSetRef = value
        return self

    def getFlatMapRef(self):
        return self.flatMapRef

    def setFlatMapRef(self, value):
        self.flatMapRef = value
        return self

    def getSoftwareCompositionTRef(self):
        return self.softwareCompositionTRef

    def setSoftwareCompositionTRef(self, value):
        self.softwareCompositionTRef = value
        return self


class J1939SharedAddressCluster(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.participatingJ1939ClusterRefs = []             # type: List[RefType]

    def getParticipatingJ1939ClusterRefs(self):
        return self.participatingJ1939ClusterRefs

    def addParticipatingJ1939ClusterRef(self, value):
        if value is not None:
            self.participatingJ1939ClusterRefs.append(value)
        return self


class System(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.clientIdDefinitionSetRefs = []                 # type: List[RefType]
        self.containerIPduHeaderByteOrder = None            # type: ByteOrderEnum
        self.ecuExtractVersion = None                       # type: RevisionLabelString
        self.fibexElements = []                             # type: List[RefType]
        self.interpolationRoutineMappingSetRefs = []        # type: List[RefType]
        self.j1939SharedAddressClusters = []                # type: List[J1939SharedAddressCluster]
        self.mappings = []                                  # type: List[SystemMapping]
        self.pncVectorLength = None                         # type: PositiveInteger
        self.pncVectorOffset = None                         # type: PositiveInteger
        self.rootSoftwareComposition = None                 # type: RootSwCompositionPrototype
        self.swClusterRefs = []                             # type: List[RefType]
        self.systemDocumentation = []                       # type: Chapter
        self.systemVersion = None                           # type: RevisionLabelString

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
        # return sorted(self.fibexElements, key= lambda i: i.getShortValue())
        return self.fibexElements

    def addFibexElementRef(self, value):
        if value is not None:
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
        return list(sorted(filter(lambda a: isinstance(a, SystemMapping), self.elements), key=lambda o: o.short_name))
    
    def getSystemMappings(self) -> List[SystemMapping]:
        return list(sorted(filter(lambda a: isinstance(a, SystemMapping), self.elements), key=lambda o: o.short_name))

    def createSystemMapping(self, short_name) -> SystemMapping:
        if not self.IsElementExists(short_name):
            mapping = SystemMapping(self, short_name)
            self.addElement(mapping)
        return self.getElement(short_name, SystemMapping)
    
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

    def createRootSoftwareComposition(self, short_name) -> RootSwCompositionPrototype:
        if short_name not in self.elements:
            prototype = RootSwCompositionPrototype(self, short_name)
            self.addElement(prototype)
            self.rootSoftwareComposition = prototype
        return self.getElement(short_name)

    def getSwClusterRefs(self):
        return self.swClusterRefs

    def addSwClusterRef(self, value):
        self.swClusterRefs.append(value)
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
