from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype, AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoServiceMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import AppOsTaskProxyToEcuTaskProxyMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import ECUMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import ApplicationPartitionToEcuPartitionMapping, SwcToImplMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement as ARElement,
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum as ByteOrderEnum,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RevisionLabelString, TRefType


class SwcToEcuMapping(Identifiable):
    """
    Represents the mapping between software components and ECU instances
    in the system, defining how components are assigned to specific
    ECUs including hardware element and processing unit references.
    """
    # SwcToEcuMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getComponentIRefs            [x] impl  [ ] docstring  [ ] test
    # [ ] addComponentIRef             [x] impl  [ ] docstring  [ ] test
    # [ ] getControlledHwElementRef    [x] impl  [ ] docstring  [ ] test
    # [ ] setControlledHwElementRef    [x] impl  [ ] docstring  [ ] test
    # [ ] getEcuInstanceRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setEcuInstanceRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getProcessingUnitRef         [x] impl  [ ] docstring  [ ] test
    # [ ] setProcessingUnitRef         [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.componentIRefs: List[ComponentInSystemInstanceRef] = []
        self.controlledHwElementRef: RefType = None
        self.ecuInstanceRef: RefType = None
        self.processingUnitRef: RefType = None

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
    """
    Represents communication management mapping in the system,
    defining how communication management groups and port groups
    are mapped to physical communication channels.
    """
    # ComManagementMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getComManagementGroupRefs    [x] impl  [ ] docstring  [ ] test
    # [ ] addComManagementGroupRef     [x] impl  [ ] docstring  [ ] test
    # [ ] getComManagementPortGroupRefs [x] impl  [ ] docstring  [ ] test
    # [ ] addComManagementPortGroupRef [x] impl  [ ] docstring  [ ] test
    # [ ] getPhysicalChannelRef        [x] impl  [ ] docstring  [ ] test
    # [ ] setPhysicalChannelRef        [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.comManagementGroupRefs: List[RefType] = []
        self.comManagementPortGroupRefs: List[RefType] = []
        self.physicalChannelRef: RefType = None

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
    """
    Represents system mapping in the AUTOSAR system, organizing
    various types of mappings including application partition mappings,
    ECU resource mappings, data mappings, and software component mappings
    for comprehensive system configuration.
    """
    # SystemMapping method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getApplicationPartitionToEcuPartitionMappings [x] impl  [ ] docstring  [ ] test
    # [ ] addApplicationPartitionToEcuPartitionMapping [x] impl  [ ] docstring  [ ] test
    # [ ] getAppOsTaskProxyToEcuTaskProxyMappings [x] impl  [ ] docstring  [ ] test
    # [ ] addAppOsTaskProxyToEcuTaskProxyMapping [x] impl  [ ] docstring  [ ] test
    # [ ] getComManagementMappings     [x] impl  [ ] docstring  [ ] test
    # [ ] addComManagementMapping      [x] impl  [ ] docstring  [ ] test
    # [ ] getCryptoServiceMappings     [x] impl  [ ] docstring  [ ] test
    # [ ] addCryptoServiceMapping      [x] impl  [ ] docstring  [ ] test
    # [ ] getDataMappings              [x] impl  [ ] docstring  [ ] test
    # [ ] addDataMapping               [x] impl  [ ] docstring  [ ] test
    # [ ] getDdsISignalToTopicMapping  [x] impl  [ ] docstring  [ ] test
    # [ ] addDdsISignalToTopicMapping  [x] impl  [ ] docstring  [ ] test
    # [ ] getEcuResourceMappings       [x] impl  [ ] docstring  [ ] test
    # [ ] createECUMapping             [x] impl  [ ] docstring  [ ] test
    # [ ] getJ1939ControllerApplicationToJ1939NmNodeMappings [x] impl  [ ] docstring  [ ] test
    # [ ] addJ1939ControllerApplicationToJ1939NmNodeMapping [x] impl  [ ] docstring  [ ] test
    # [ ] getMappingConstraints        [x] impl  [ ] docstring  [ ] test
    # [ ] addMappingConstraint         [x] impl  [ ] docstring  [ ] test
    # [ ] getPncMappings               [x] impl  [ ] docstring  [ ] test
    # [ ] addPncMapping                [x] impl  [ ] docstring  [ ] test
    # [ ] getPortElementToComResourceMappings [x] impl  [ ] docstring  [ ] test
    # [ ] addPortElementToComResourceMapping [x] impl  [ ] docstring  [ ] test
    # [ ] getResourceEstimations       [x] impl  [ ] docstring  [ ] test
    # [ ] addResourceEstimation        [x] impl  [ ] docstring  [ ] test
    # [ ] getResourceToApplicationPartitionMappings [x] impl  [ ] docstring  [ ] test
    # [ ] addResourceToApplicationPartitionMapping [x] impl  [ ] docstring  [ ] test
    # [ ] getRteEventSeparations       [x] impl  [ ] docstring  [ ] test
    # [ ] addRteEventSeparation        [x] impl  [ ] docstring  [ ] test
    # [ ] getRteEventToOsTaskProxyMappings [x] impl  [ ] docstring  [ ] test
    # [ ] addRteEventToOsTaskProxyMapping [x] impl  [ ] docstring  [ ] test
    # [ ] getSignalPathConstraints     [x] impl  [ ] docstring  [ ] test
    # [ ] addSignalPathConstraint      [x] impl  [ ] docstring  [ ] test
    # [ ] getSoftwareClusterToApplicationPartitionMappings [x] impl  [ ] docstring  [ ] test
    # [ ] addSoftwareClusterToApplicationPartitionMapping [x] impl  [ ] docstring  [ ] test
    # [ ] getSoftwareClusterToResourceMappings [x] impl  [ ] docstring  [ ] test
    # [ ] addSoftwareClusterToResourceMapping [x] impl  [ ] docstring  [ ] test
    # [ ] getSwClusterMappings         [x] impl  [ ] docstring  [ ] test
    # [ ] addSwClusterMapping          [x] impl  [ ] docstring  [ ] test
    # [ ] getSwcToApplicationPartitionMappings [x] impl  [ ] docstring  [ ] test
    # [ ] addSwcToApplicationPartitionMappings [x] impl  [ ] docstring  [ ] test
    # [ ] getSwImplMappings            [x] impl  [ ] docstring  [ ] test
    # [ ] createSwcToImplMapping       [x] impl  [ ] docstring  [ ] test
    # [ ] getSwMappings                [x] impl  [ ] docstring  [ ] test
    # [ ] getSwcToEcuMappings          [x] impl  [ ] docstring  [ ] test
    # [ ] createSwcToEcuMapping        [x] impl  [ ] docstring  [ ] test
    # [ ] getSystemSignalGroupToComResourceMappings [x] impl  [ ] docstring  [ ] test
    # [ ] addSystemSignalGroupToComResourceMapping [x] impl  [ ] docstring  [ ] test
    # [ ] getSystemSignalToComResourceMappings [x] impl  [ ] docstring  [ ] test
    # [ ] addSystemSignalToComResourceMapping [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.applicationPartitionToEcuPartitionMappings: List[ApplicationPartitionToEcuPartitionMapping] = []
        self.appOsTaskProxyToEcuTaskProxyMappings: List[AppOsTaskProxyToEcuTaskProxyMapping] = []
        self.comManagementMappings: List[ComManagementMapping] = []
        self.cryptoServiceMappings: List[CryptoServiceMapping] = []
        self.dataMappings: List[DataMapping] = []
        self.ddsISignalToTopicMappings: List = []
        self.ecuResourceMappings: List[ECUMapping] = []
        self.j1939ControllerApplicationToJ1939NmNodeMappings: List = []
        self.mappingConstraints: List = []
        self.pncMappings: List = []
        self.portElementToComResourceMappings: List = []
        self.resourceEstimations: List = []
        self.resourceToApplicationPartitionMappings: List = []
        self.rteEventSeparations: List = []
        self.rteEventToOsTaskProxyMappings: List = []
        self.signalPathConstraints: List = []
        self.softwareClusterToApplicationPartitionMappings: List = []
        self.softwareClusterToResourceMappings: List = []
        self.swClusterMappings: List = []
        self.swcToApplicationPartitionMappings: List = []
        self.swImplMappings: List[SwcToImplMapping] = []
        self.swMappings: List[SwcToEcuMapping] = []
        self.systemSignalGroupToComResourceMappings: List = []
        self.systemSignalToComResourceMappings: List = []

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


class RootSwCompositionPrototype(AtpPrototype):
    """
    Represents the root software composition prototype in the system,
    defining references to calibration parameter value sets, flat maps,
    and software composition templates for the top-level composition.
    """
    # RootSwCompositionPrototype method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCalibrationParameterValueSetRef [x] impl  [ ] docstring  [ ] test
    # [ ] setCalibrationParameterValueSetRef [x] impl  [ ] docstring  [ ] test
    # [ ] getFlatMapRef                [x] impl  [ ] docstring  [ ] test
    # [ ] setFlatMapRef                [x] impl  [ ] docstring  [ ] test
    # [ ] getSoftwareCompositionTRef   [x] impl  [ ] docstring  [ ] test
    # [ ] setSoftwareCompositionTRef   [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.calibrationParameterValueSetRef: RefType = None
        self.flatMapRef: RefType = None
        self.softwareCompositionTRef: TRefType = None

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
    """
    Represents a J1939 shared address cluster in the system,
    defining references to participating J1939 clusters for
    shared address management in J1939 communication.
    """
    # J1939SharedAddressCluster method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getParticipatingJ1939ClusterRefs [x] impl  [ ] docstring  [ ] test
    # [ ] addParticipatingJ1939ClusterRef [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.participatingJ1939ClusterRefs: List[RefType] = []

    def getParticipatingJ1939ClusterRefs(self):
        return self.participatingJ1939ClusterRefs

    def addParticipatingJ1939ClusterRef(self, value):
        if value is not None:
            self.participatingJ1939ClusterRefs.append(value)
        return self


class System(AtpStructureElement):
    """
    Represents the top-level system in the AUTOSAR system template,
    organizing all system-level elements including ECU extractions,
    mappings, and system configurations for complete system definition.
    """
    # System method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getClientIdDefinitionSetRefs [x] impl  [ ] docstring  [ ] test
    # [ ] addClientIdDefinitionSetRefs [x] impl  [ ] docstring  [ ] test
    # [ ] getContainerIPduHeaderByteOrder [x] impl  [ ] docstring  [ ] test
    # [ ] setContainerIPduHeaderByteOrder [x] impl  [ ] docstring  [ ] test
    # [ ] getEcuExtractVersion         [x] impl  [ ] docstring  [ ] test
    # [ ] setEcuExtractVersion         [x] impl  [ ] docstring  [ ] test
    # [ ] getFibexElementRefs          [x] impl  [ ] docstring  [ ] test
    # [ ] addFibexElementRef           [x] impl  [ ] docstring  [ ] test
    # [ ] getInterpolationRoutineMappingSetRefs [x] impl  [ ] docstring  [ ] test
    # [ ] addInterpolationRoutineMappingSetRefs [x] impl  [ ] docstring  [ ] test
    # [ ] getJ1939SharedAddressClusters [x] impl  [ ] docstring  [ ] test
    # [ ] setJ1939SharedAddressClusters [x] impl  [ ] docstring  [ ] test
    # [ ] getMappings                  [x] impl  [ ] docstring  [ ] test
    # [ ] getSystemMappings            [x] impl  [ ] docstring  [ ] test
    # [ ] createSystemMapping          [x] impl  [ ] docstring  [ ] test
    # [ ] getPncVectorLength           [x] impl  [ ] docstring  [ ] test
    # [ ] setPncVectorLength           [x] impl  [ ] docstring  [ ] test
    # [ ] getPncVectorOffset           [x] impl  [ ] docstring  [ ] test
    # [ ] setPncVectorOffset           [x] impl  [ ] docstring  [ ] test
    # [ ] getRootSoftwareComposition   [x] impl  [ ] docstring  [ ] test
    # [ ] createRootSoftwareComposition [x] impl  [ ] docstring  [ ] test
    # [ ] getSwClusterRefs             [x] impl  [ ] docstring  [ ] test
    # [ ] addSwClusterRef              [x] impl  [ ] docstring  [ ] test
    # [ ] getSystemDocumentation       [x] impl  [ ] docstring  [ ] test
    # [ ] setSystemDocumentation       [x] impl  [ ] docstring  [ ] test
    # [ ] getSystemVersion             [x] impl  [ ] docstring  [ ] test
    # [ ] setSystemVersion             [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.clientIdDefinitionSetRefs: List[RefType] = []
        self.containerIPduHeaderByteOrder = None
        self.ecuExtractVersion: RevisionLabelString = None
        self.fibexElements: List[RefType] = []
        self.interpolationRoutineMappingSetRefs: List[RefType] = []
        self.j1939SharedAddressClusters: List[J1939SharedAddressCluster] = []
        self.mappings: List[SystemMapping] = []
        self.pncVectorLength: PositiveInteger = None
        self.pncVectorOffset: PositiveInteger = None
        self.rootSoftwareComposition: RootSwCompositionPrototype = None
        self.swClusterRefs: List[RefType] = []
        self.systemDocumentation = []
        self.systemVersion: RevisionLabelString = None

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
