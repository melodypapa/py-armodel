from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype, AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoServiceMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import AppOsTaskProxyToEcuTaskProxyMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import ECUMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import ApplicationPartitionToEcuPartitionMapping, SwcToImplMapping
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement as ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum as ByteOrderEnum,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RevisionLabelString, TRefType
from armodel.models.M2.MSR.Documentation.Chapters import Chapter


class SwcToEcuMapping(Identifiable, VariationPointCapable):
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


class ComManagementMapping(Identifiable, VariationPointCapable):
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


class SystemMapping(Identifiable, VariationPointCapable):
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
        if not self.IsElementExists(short_name, ECUMapping):
            mapping = ECUMapping(self, short_name)
            self.addElement(mapping)
            self.ecuResourceMappings.append(mapping)
        return self.getElement(short_name, ECUMapping)

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
        if not self.IsElementExists(short_name, SwcToImplMapping):
            mapping = SwcToImplMapping(self, short_name)
            self.addElement(mapping)
            self.swImplMappings.append(mapping)
        return self.getElement(short_name, SwcToImplMapping)

    def getSwMappings(self):
        return self.swMappings

    def getSwcToEcuMappings(self) -> List[SwcToEcuMapping]:
        return list(sorted(filter(lambda a: isinstance(a, SwcToEcuMapping), self.elements), key=lambda o: o.short_name))

    def createSwcToEcuMapping(self, short_name: str) -> SwcToEcuMapping:
        if not self.IsElementExists(short_name, SwcToEcuMapping):
            mapping = SwcToEcuMapping(self, short_name)
            self.addElement(mapping)
            self.swMappings.append(mapping)
        return self.getElement(short_name, SwcToEcuMapping)

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


class RootSwCompositionPrototype(AtpPrototype, VariationPointCapable):
    """
    The RootSwCompositionPrototype represents the top-level-composition of software components within a given System. According to the use case of the System, this may for example be a more or less complete VFB description, the software of a System Extract or the software of a flat ECU Extract with only atomic SWCs. Therefore the RootSwComposition will only occasionally contain all atomic software components that are used in a complete VFB System. The OEM is primarily interested in the required functionality and the interfaces defining the integration of the Software Component into the System. The internal structure of such a component contains often substantial intellectual property of a supplier. Therefore a top-level software composition will often contain empty compositions which represent subsystems. The contained SwComponentPrototypes are fully specified by their SwComponentTypes (including Port Prototypes, PortInterfaces, VariableDataPrototypes, SwcInternalBehavior etc.), and their ports are interconnected using SwConnectorPrototypes.
    """

    # RootSwCompositionPrototype method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 4.1, p.186
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCalibrationParameterValueSetRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addCalibrationParameterValueSetRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFlatMapRef                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFlatMapRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSoftwareCompositionTRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSoftwareCompositionTRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Used CalibrationParameterValueSet for instance specific initialization of calibration parameters.
        self.calibrationParameterValueSetRefs: List[RefType] = []

        # The FlatMap used in the scope of this RootSw CompositionPrototype.
        self.flatMapRef: Optional[RefType] = None

        # We assume that there is exactly one top-level composition that includes all Component instances of the system.
        self.softwareCompositionTRef: Optional[TRefType] = None

    def getCalibrationParameterValueSetRefs(self) -> List[RefType]:
        """
        Used CalibrationParameterValueSet for instance specific initialization of calibration parameters.
        """
        return self.calibrationParameterValueSetRefs

    def addCalibrationParameterValueSetRef(self, value: Optional[RefType]) -> "RootSwCompositionPrototype":
        """
        Used CalibrationParameterValueSet for instance specific initialization of calibration parameters.
        A None value is a no-op and does not add to calibrationParameterValueSetRefs.
        """
        if value is not None:
            self.calibrationParameterValueSetRefs.append(value)
        return self

    def getFlatMapRef(self) -> Optional[RefType]:
        """
        The FlatMap used in the scope of this RootSw CompositionPrototype.
        """
        return self.flatMapRef

    def setFlatMapRef(self, value: Optional[RefType]) -> "RootSwCompositionPrototype":
        """
        The FlatMap used in the scope of this RootSw CompositionPrototype.
        A None value is a no-op and does not overwrite an existing flatMapRef.
        """
        if value is not None:
            self.flatMapRef = value
        return self

    def getSoftwareCompositionTRef(self) -> Optional[TRefType]:
        """
        We assume that there is exactly one top-level composition that includes all Component instances of the system.
        """
        return self.softwareCompositionTRef

    def setSoftwareCompositionTRef(self, value: Optional[TRefType]) -> "RootSwCompositionPrototype":
        """
        We assume that there is exactly one top-level composition that includes all Component instances of the system.
        A None value is a no-op and does not overwrite an existing softwareCompositionTRef.
        """
        if value is not None:
            self.softwareCompositionTRef = value
        return self


class J1939SharedAddressCluster(Identifiable, VariationPointCapable):
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
    The top level element of the System Description. The System description defines five major elements: Topology, Software, Communication, Mapping and Mapping Constraints. The System element directly aggregates the elements describing the Software, Mapping and Mapping Constraints; it contains a reference to an ASAM FIBEX description specifying Communication and Topology. Tags: atp.recommendedPackage=Systems

    [constr_3028] FibexElements: Each FibexElement that is used in the System Description shall be referenced by the System element in the role FibexElement.

    [constr_3027] Existence of ecuExtractVersion: In case the category of the System is SYSTEM_EXTRACT or ECU_EXTRACT the ecuExtractVersion attribute shall be defined.
    """

    # System method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 2.1, p.42
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addClientIdDefinitionSetRef                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getClientIdDefinitionSetRefs                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getContainerIPduHeaderByteOrder                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setContainerIPduHeaderByteOrder                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEcuExtractVersion                                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcuExtractVersion                                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addFibexElementRef                                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFibexElementRefs                                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addInterpolationRoutineMappingSetRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInterpolationRoutineMappingSetRefs                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createJ1939SharedAddressCluster                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getJ1939SharedAddressClusters                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSystemMapping                                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMappings                                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getPncVectorLength                                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPncVectorLength                                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPncVectorOffset                                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPncVectorOffset                                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createRootSoftwareComposition                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRootSoftwareComposition                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSwClusterRef                                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwClusterRefs                                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSystemDocumentation                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSystemDocumentations                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getSystemVersion                                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSystemVersion                                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Set of Client Identifiers that are used for inter-ECU client-server communication in the System.
        self.clientIdDefinitionSetRefs: List[RefType] = []

        # Defines the byteOrder of the header in ContainerIPdus.
        self.containerIPduHeaderByteOrder: Optional[ByteOrderEnum] = None

        # Version number of the Ecu Extract.
        self.ecuExtractVersion: Optional[RevisionLabelString] = None

        # Reference to ASAM FIBEX elements specifying Communication and Topology. All Fibex Elements used within a System Description shall be referenced from the System Element. atpVariation: In order to describe a product-line, all Fibex Elements can be optional.
        self.fibexElementRefs: List[RefType] = []

        # This reference identifies the InterpolationRoutineMappingSets that are relevant in the context of the enclosing System.
        self.interpolationRoutineMappingSetRefs: List[RefType] = []

        # Collection of J1939Clusters that share a common address space for the routing of messages.
        self.j1939SharedAddressClusters: List[J1939SharedAddressCluster] = []

        # Aggregation of all mapping aspects (mapping of SW components to ECUs, mapping of data elements to signals, and mapping constraints). In order to support OEM / Tier 1 interaction and shared development for one common System this aggregation is atpSplitable and atpVariation. The content of SystemMapping can be provided by several parties using different names for the SystemMapping. This element is not required when the System description is used for a network-only use-case.
        self.mappings: List[SystemMapping] = []

        # Length of the partial networking request release information vector (in bytes).
        self.pncVectorLength: Optional[PositiveInteger] = None

        # Absolute offset (with respect to the NM-PDU) of the partial networking request release information vector that is defined in bytes as an index starting with 0.
        self.pncVectorOffset: Optional[PositiveInteger] = None

        # Aggregation of the root software composition, containing all software components in the System in a hierarchical structure. This element is not required when the System description is used for a network-only use-case. atpVariation: The RootSwCompositionPrototype can vary.
        self.rootSoftwareComposition: Optional[RootSwCompositionPrototype] = None

        # CP Software Clusters of this System
        self.swClusterRefs: List[RefType] = []

        # Possibility to provide additional documentation while defining the System. The System documentation can be composed of several chapters.
        self.systemDocumentations: List[Chapter] = []

        # Version number of the System Description.
        self.systemVersion: Optional[RevisionLabelString] = None

    def addClientIdDefinitionSetRef(self, value: Optional[RefType]) -> "System":
        """
        Set of Client Identifiers that are used for inter-ECU client-server communication in the System.

        A None value is a no-op and does not add to clientIdDefinitionSetRefs.
        """
        if value is not None:
            self.clientIdDefinitionSetRefs.append(value)
        return self

    def getClientIdDefinitionSetRefs(self) -> List[RefType]:
        """
        Set of Client Identifiers that are used for inter-ECU client-server communication in the System.
        """
        return self.clientIdDefinitionSetRefs

    def getContainerIPduHeaderByteOrder(self) -> Optional[ByteOrderEnum]:
        """
        Defines the byteOrder of the header in ContainerIPdus.
        """
        return self.containerIPduHeaderByteOrder

    def setContainerIPduHeaderByteOrder(self, value: Optional[ByteOrderEnum]) -> "System":
        """
        Defines the byteOrder of the header in ContainerIPdus.

        A None value is a no-op and does not overwrite an existing containerIPduHeaderByteOrder.
        """
        if value is not None:
            self.containerIPduHeaderByteOrder = value
        return self

    def getEcuExtractVersion(self) -> Optional[RevisionLabelString]:
        """
        Version number of the Ecu Extract.
        """
        return self.ecuExtractVersion

    def setEcuExtractVersion(self, value: Optional[RevisionLabelString]) -> "System":
        """
        Version number of the Ecu Extract.

        A None value is a no-op and does not overwrite an existing ecuExtractVersion.
        """
        if value is not None:
            self.ecuExtractVersion = value
        return self

    def addFibexElementRef(self, value: Optional[RefType]) -> "System":
        """
        Reference to ASAM FIBEX elements specifying Communication and Topology. All Fibex Elements used within a System Description shall be referenced from the System Element. atpVariation: In order to describe a product-line, all Fibex Elements can be optional.

        A None value is a no-op and does not add to fibexElementRefs.
        """
        if value is not None:
            self.fibexElementRefs.append(value)
        return self

    def getFibexElementRefs(self) -> List[RefType]:
        """
        Reference to ASAM FIBEX elements specifying Communication and Topology. All Fibex Elements used within a System Description shall be referenced from the System Element. atpVariation: In order to describe a product-line, all Fibex Elements can be optional.
        """
        return self.fibexElementRefs

    def addInterpolationRoutineMappingSetRef(self, value: Optional[RefType]) -> "System":
        """
        This reference identifies the InterpolationRoutineMappingSets that are relevant in the context of the enclosing System.

        A None value is a no-op and does not add to interpolationRoutineMappingSetRefs.
        """
        if value is not None:
            self.interpolationRoutineMappingSetRefs.append(value)
        return self

    def getInterpolationRoutineMappingSetRefs(self) -> List[RefType]:
        """
        This reference identifies the InterpolationRoutineMappingSets that are relevant in the context of the enclosing System.
        """
        return self.interpolationRoutineMappingSetRefs

    def createJ1939SharedAddressCluster(self, short_name: str) -> J1939SharedAddressCluster:
        """
        Collection of J1939Clusters that share a common address space for the routing of messages.
        """
        if not self.IsElementExists(short_name, J1939SharedAddressCluster):
            cluster = J1939SharedAddressCluster(self, short_name)
            self.addElement(cluster)
            self.j1939SharedAddressClusters.append(cluster)
        return self.getElement(short_name, J1939SharedAddressCluster)

    def getJ1939SharedAddressClusters(self) -> List[J1939SharedAddressCluster]:
        """
        Collection of J1939Clusters that share a common address space for the routing of messages.
        """
        return self.j1939SharedAddressClusters

    def createSystemMapping(self, short_name: str) -> SystemMapping:
        """
        Aggregation of all mapping aspects (mapping of SW components to ECUs, mapping of data elements to signals, and mapping constraints). In order to support OEM / Tier 1 interaction and shared development for one common System this aggregation is atpSplitable and atpVariation. The content of SystemMapping can be provided by several parties using different names for the SystemMapping. This element is not required when the System description is used for a network-only use-case.
        """
        if not self.IsElementExists(short_name, SystemMapping):
            mapping = SystemMapping(self, short_name)
            self.addElement(mapping)
            self.mappings.append(mapping)
        return self.getElement(short_name, SystemMapping)

    def getMappings(self) -> List[SystemMapping]:
        """
        Aggregation of all mapping aspects (mapping of SW components to ECUs, mapping of data elements to signals, and mapping constraints). In order to support OEM / Tier 1 interaction and shared development for one common System this aggregation is atpSplitable and atpVariation. The content of SystemMapping can be provided by several parties using different names for the SystemMapping. This element is not required when the System description is used for a network-only use-case.
        """
        return self.mappings

    def getPncVectorLength(self) -> Optional[PositiveInteger]:
        """
        Length of the partial networking request release information vector (in bytes).
        """
        return self.pncVectorLength

    def setPncVectorLength(self, value: Optional[PositiveInteger]) -> "System":
        """
        Length of the partial networking request release information vector (in bytes).

        A None value is a no-op and does not overwrite an existing pncVectorLength.
        """
        if value is not None:
            self.pncVectorLength = value
        return self

    def getPncVectorOffset(self) -> Optional[PositiveInteger]:
        """
        Absolute offset (with respect to the NM-PDU) of the partial networking request release information vector that is defined in bytes as an index starting with 0.
        """
        return self.pncVectorOffset

    def setPncVectorOffset(self, value: Optional[PositiveInteger]) -> "System":
        """
        Absolute offset (with respect to the NM-PDU) of the partial networking request release information vector that is defined in bytes as an index starting with 0.

        A None value is a no-op and does not overwrite an existing pncVectorOffset.
        """
        if value is not None:
            self.pncVectorOffset = value
        return self

    def createRootSoftwareComposition(self, short_name: str) -> RootSwCompositionPrototype:
        """
        Aggregation of the root software composition, containing all software components in the System in a hierarchical structure. This element is not required when the System description is used for a network-only use-case. atpVariation: The RootSwCompositionPrototype can vary.
        """
        if not self.IsElementExists(short_name, RootSwCompositionPrototype):
            prototype = RootSwCompositionPrototype(self, short_name)
            self.addElement(prototype)
            self.rootSoftwareComposition = prototype
        return self.getElement(short_name, RootSwCompositionPrototype)

    def getRootSoftwareComposition(self) -> Optional[RootSwCompositionPrototype]:
        """
        Aggregation of the root software composition, containing all software components in the System in a hierarchical structure. This element is not required when the System description is used for a network-only use-case. atpVariation: The RootSwCompositionPrototype can vary.
        """
        return self.rootSoftwareComposition

    def addSwClusterRef(self, value: Optional[RefType]) -> "System":
        """
        CP Software Clusters of this System

        A None value is a no-op and does not add to swClusterRefs.
        """
        if value is not None:
            self.swClusterRefs.append(value)
        return self

    def getSwClusterRefs(self) -> List[RefType]:
        """
        CP Software Clusters of this System
        """
        return self.swClusterRefs

    def createSystemDocumentation(self, short_name: str) -> Chapter:
        """
        Possibility to provide additional documentation while defining the System. The System documentation can be composed of several chapters.
        """
        if not self.IsElementExists(short_name, Chapter):
            chapter = Chapter(self, short_name)
            self.addElement(chapter)
            self.systemDocumentations.append(chapter)
        return self.getElement(short_name, Chapter)

    def getSystemDocumentations(self) -> List[Chapter]:
        """
        Possibility to provide additional documentation while defining the System. The System documentation can be composed of several chapters.
        """
        return self.systemDocumentations

    def getSystemVersion(self) -> Optional[RevisionLabelString]:
        """
        Version number of the System Description.
        """
        return self.systemVersion

    def setSystemVersion(self, value: Optional[RevisionLabelString]) -> "System":
        """
        Version number of the System Description.

        A None value is a no-op and does not overwrite an existing systemVersion.
        """
        if value is not None:
            self.systemVersion = value
        return self
