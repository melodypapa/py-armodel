from typing import List, Optional, cast
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype, AtpStructureElement
from armodel.models.M2.MSR.Documentation.Chapters import Chapter
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import DataMapping, TriggerToSignalMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import DdsCpISignalToDdsTopicMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import CryptoServiceMapping, SecOcCryptoServiceMapping, TlsCryptoServiceMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import (
    AppOsTaskProxyToEcuTaskProxyMapping,
    OsTaskPreemptabilityEnum,
    OsTaskProxy,
    RteEventInCompositionSeparation,
    RteEventInCompositionToOsTaskProxyMapping,
    RteEventInSystemSeparation,
    RteEventInSystemToOsTaskProxyMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import ECUMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
    ComponentInSystemInstanceRef,
    OperationInSystemInstanceRef,
    PortGroupInSystemInstanceRef,
    TriggerInSystemInstanceRef,
    VariableDataPrototypeInSystemInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping import PncMapping, PncMappingIdent
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import CommonSignalPath, SignalPathConstraint, SwcToSwcOperationArguments, SwcToSwcOperationArgumentsDirectionEnum, SwcToSwcSignal
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import (
    ApplicationPartition,
    ApplicationPartitionToEcuPartitionMapping,
    EcuResourceEstimation,
    MappingConstraint,
    SwcToApplicationPartitionMapping,
    SwcToEcuMapping,
    SwcToImplMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import (
    CpSoftwareCluster,
    CpSoftwareClusterMappingSet,
    CpSoftwareClusterResourceToApplicationPartitionMapping,
    CpSoftwareClusterToApplicationPartitionMapping,
    CpSoftwareClusterToEcuInstanceMapping,
    CpSoftwareClusterToResourceMapping,
    SwComponentPrototypeAssignment,
    SystemSignalGroupToCommunicationResourceMapping,
    SystemSignalToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    J1939ControllerApplicationToJ1939NmNodeMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    PortElementToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
    Numerical,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RevisionLabelString, TRefType


class ComManagementMapping(Identifiable, VariationPointCapable):
    """
    Describes a mapping between one or several Mode Management PortGroups and communication channels.
    """

    # ComManagementMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.46, p.282
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addComManagementGroupRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getComManagementGroupRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addComManagementPortGroupIRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getComManagementPortGroupIRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addPhysicalChannelRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPhysicalChannelRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # IPduGroup participating in a Mode Management PortGroup.
        self.comManagementGroupRefs: List[RefType] = []

        # Mode Management PortGroup to be mapped onto a communication channel. This reference is optional in case that the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy systems.
        self.comManagementPortGroupIRefs: List[PortGroupInSystemInstanceRef] = []

        # This reference maps the Mode Management PortGroup partial network to communication channels.
        self.physicalChannelRefs: List[RefType] = []

    def addComManagementGroupRef(self, value: Optional[RefType]) -> "ComManagementMapping":
        """
        IPduGroup participating in a Mode Management PortGroup.

        A None value is a no-op and does not add to comManagementGroupRefs.
        """
        if value is not None:
            self.comManagementGroupRefs.append(value)
        return self

    def getComManagementGroupRefs(self) -> List[RefType]:
        """
        IPduGroup participating in a Mode Management PortGroup.
        """
        return self.comManagementGroupRefs

    def addComManagementPortGroupIRef(self, value: Optional[PortGroupInSystemInstanceRef]) -> "ComManagementMapping":
        """
        Mode Management PortGroup to be mapped onto a communication channel. This reference is optional in case that the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy systems.

        A None value is a no-op and does not add to comManagementPortGroupIRefs.
        """
        if value is not None:
            self.comManagementPortGroupIRefs.append(value)
        return self

    def getComManagementPortGroupIRefs(self) -> List[PortGroupInSystemInstanceRef]:
        """
        Mode Management PortGroup to be mapped onto a communication channel. This reference is optional in case that the System Description doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy systems.
        """
        return self.comManagementPortGroupIRefs

    def addPhysicalChannelRef(self, value: Optional[RefType]) -> "ComManagementMapping":
        """
        This reference maps the Mode Management PortGroup partial network to communication channels.

        A None value is a no-op and does not add to physicalChannelRefs.
        """
        if value is not None:
            self.physicalChannelRefs.append(value)
        return self

    def getPhysicalChannelRefs(self) -> List[RefType]:
        """
        This reference maps the Mode Management PortGroup partial network to communication channels.
        """
        return self.physicalChannelRefs


class SystemMapping(Identifiable, VariationPointCapable):
    """
    The system mapping aggregates all mapping aspects (mapping of SW components to ECUs, mapping of data elements to signals, and mapping constraints).
    """

    # SystemMapping method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.1, p.193
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addApplicationPartitionToEcuPartitionMapping        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createApplicationPartitionToEcuPartitionMapping     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getApplicationPartitionToEcuPartitionMappings       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addAppOsTaskProxyToEcuTaskProxyMapping              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createAppOsTaskProxyToEcuTaskProxyMapping           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getAppOsTaskProxyToEcuTaskProxyMappings             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addComManagementMapping                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createComManagementMapping                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getComManagementMappings                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addCryptoServiceMapping                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createSecOcCryptoServiceMapping                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createTlsCryptoServiceMapping                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCryptoServiceMappings                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDataMapping                                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataMappings                                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDdsISignalToTopicMapping                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDdsISignalToTopicMappings                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createECUMapping                                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEcuResourceMappings                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addJ1939ControllerApplicationToJ1939NmNodeMapping   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getJ1939ControllerApplicationToJ1939NmNodeMappings  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addMappingConstraint                                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMappingConstraints                               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addPncMapping                                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPncMappings                                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addPortElementToComResourceMapping                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createPortElementToComResourceMapping               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPortElementToComResourceMappings                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addResourceEstimation                               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResourceEstimations                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addResourceToApplicationPartitionMapping            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getResourceToApplicationPartitionMappings           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addRteEventSeparation                               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRteEventSeparations                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addRteEventToOsTaskProxyMapping                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRteEventToOsTaskProxyMappings                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSignalPathConstraint                             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSignalPathConstraints                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSoftwareClusterToApplicationPartitionMapping     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSoftwareClusterToApplicationPartitionMappings    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSoftwareClusterToResourceMapping                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSoftwareClusterToResourceMappings                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSwClusterMapping                                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwClusterMappings                                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSwcToApplicationPartitionMapping                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createSwcToApplicationPartitionMapping              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwcToApplicationPartitionMappings                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSwcToImplMapping                              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwImplMappings                                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createSwcToEcuMapping                               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwMappings                                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSystemSignalGroupToComResourceMapping            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSystemSignalGroupToComResourceMappings           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSystemSignalToComResourceMapping                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSystemSignalToComResourceMappings                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Mapping of ApplicationPartitions to EcuPartitions Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=applicationPartitionToEcuPartitionMapping.shortName, applicationPartitionToEcuPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.applicationPartitionToEcuPartitionMappings: List[ApplicationPartitionToEcuPartitionMapping] = []

        # Mapping of an OsTaskProxy that was created in the context of a SwComponent to an OsTaskProxy that was created in the context of an Ecu.
        self.appOsTaskProxyToEcuTaskProxyMappings: List[AppOsTaskProxyToEcuTaskProxyMapping] = []

        # Mappings between Mode Management PortGroups and communication channels. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=comManagementMapping.shortName, comManagementMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        self.comManagementMappings: List[ComManagementMapping] = []

        # This aggregation represents the collection of crypto service mappings in the context of the enclosing System Mapping. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=cryptoServiceMapping.shortName, cryptoServiceMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.cryptoServiceMappings: List[CryptoServiceMapping] = []

        # The data mappings defined. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataMapping, dataMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.dataMappings: List[DataMapping] = []

        # Collection of DdsISignalToDdsTopicMappings. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ddsISignalToTopicMapping, ddsISignalToTopicMapping.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        self.ddsISignalToTopicMappings: List[DdsCpISignalToDdsTopicMapping] = []

        # Mapping of hardware related topology elements onto their counterpart definitions in the ECU Resource Template. atpVariation: The ECU Resource type might be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ecuResourceMapping.shortName, ecuResourceMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        self.ecuResourceMappings: List[ECUMapping] = []

        # Mapping of a J1939ControllerApplication to a J1939NmNode.
        self.j1939ControllerApplicationToJ1939NmNodeMappings: List[J1939ControllerApplicationToJ1939NmNodeMapping] = []

        # Constraints that limit the mapping freedom for the mapping of SW components to ECUs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=mappingConstraint, mappingConstraint.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        self.mappingConstraints: List[MappingConstraint] = []

        # Mappings between Virtual Function Clusters and Partial Network Clusters. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pncMapping, pncMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        self.pncMappings: List[PncMapping] = []

        # maps a communication resource to CP Software Clusters Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=portElementToComResourceMapping.shortName, portElementToComResourceMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.portElementToComResourceMappings: List[PortElementToCommunicationResourceMapping] = []

        # Resource estimations for this set of mappings, zero or one per ECU instance. atpVariation: Used ECUs are variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=resourceEstimation, resourceEstimation.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        self.resourceEstimations: List[EcuResourceEstimation] = []

        # Maps a Software Cluster resource to an Application Partition to restrict the usage. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=resourceToApplicationPartitionMapping.shortName, resourceToApplicationPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        self.resourceToApplicationPartitionMappings: List[CpSoftwareClusterResourceToApplicationPartitionMapping] = []

        # Separation constraint that limits the mapping freedom for the mapping of RteEvents to OsTasks in the System context.
        self.rteEventSeparations: List[RteEventInSystemSeparation] = []

        # Constraint that enforces a mapping of RteEvent to a particular OsTask in the System context.
        self.rteEventToOsTaskProxyMappings: List[RteEventInSystemToOsTaskProxyMapping] = []

        # Constraints that limit the mapping freedom for the mapping of data elements to signals. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=signalPathConstraint, signalPathConstraint.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        self.signalPathConstraints: List[SignalPathConstraint] = []

        # The mapping of ApplicationPartitions to a CpSoftwareCluster. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=softwareClusterToApplicationPartitionMapping.shortName, softwareClusterToApplicationPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        self.softwareClusterToApplicationPartitionMappings: List[CpSoftwareClusterToApplicationPartitionMapping] = []

        # maps a service resource to CP Software Clusters Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=softwareClusterToResourceMapping.shortName, softwareClusterToResourceMapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.softwareClusterToResourceMappings: List[CpSoftwareClusterToResourceMapping] = []

        # The mappings of SW cluster to ECUs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swClusterMapping.shortName, swClusterMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        self.swClusterMappings: List[CpSoftwareClusterToEcuInstanceMapping] = []

        # Allows to map a given SwComponentPrototype to a formally defined partition at a point in time when the corresponding EcuInstance is not yet known or defined. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swcToApplicationPartitionMapping.shortName, swcToApplicationPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.swcToApplicationPartitionMappings: List[SwcToApplicationPartitionMapping] = []

        # The mappings of AtomicSoftwareComponent Instances to Implementations. atpVariation: Derived, because SwcToEcuMapping is variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swImplMapping.shortName, swImplMapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.swImplMappings: List[SwcToImplMapping] = []

        # The mappings of SW components to ECUs. atpVariation: SWC shall be mapped to other ECUs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swMapping.shortName, swMapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        self.swMappings: List[SwcToEcuMapping] = []

        # Mapping of a communication resource to a SystemSignalGroup. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=systemSignalGroupToComResourceMapping.shortName, systemSignalGroupToComResourceMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        self.systemSignalGroupToComResourceMappings: List[SystemSignalGroupToCommunicationResourceMapping] = []

        # Mapping of a communication resource to a SystemSignal. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=systemSignalToComResourceMapping.shortName, systemSignalToComResourceMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        self.systemSignalToComResourceMappings: List[SystemSignalToCommunicationResourceMapping] = []

    def addApplicationPartitionToEcuPartitionMapping(self, value: Optional[ApplicationPartitionToEcuPartitionMapping]) -> "SystemMapping":
        """
        Mapping of ApplicationPartitions to EcuPartitions Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=applicationPartitionToEcuPartitionMapping.shortName, applicationPartitionToEcuPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild

        A None value is a no-op and does not add to applicationPartitionToEcuPartitionMappings.
        """
        if value is not None:
            self.applicationPartitionToEcuPartitionMappings.append(value)
        return self

    def createApplicationPartitionToEcuPartitionMapping(self, short_name: str) -> ApplicationPartitionToEcuPartitionMapping:
        """
        Mapping of ApplicationPartitions to EcuPartitions Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=applicationPartitionToEcuPartitionMapping.shortName, applicationPartitionToEcuPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, ApplicationPartitionToEcuPartitionMapping):
            mapping = ApplicationPartitionToEcuPartitionMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.applicationPartitionToEcuPartitionMappings.append(mapping)
        return cast(ApplicationPartitionToEcuPartitionMapping, self.getReferrableElement(short_name, ApplicationPartitionToEcuPartitionMapping))

    def getApplicationPartitionToEcuPartitionMappings(self) -> List[ApplicationPartitionToEcuPartitionMapping]:
        """
        Mapping of ApplicationPartitions to EcuPartitions Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=applicationPartitionToEcuPartitionMapping.shortName, applicationPartitionToEcuPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.applicationPartitionToEcuPartitionMappings

    def addAppOsTaskProxyToEcuTaskProxyMapping(self, value: Optional[AppOsTaskProxyToEcuTaskProxyMapping]) -> "SystemMapping":
        """
        Mapping of an OsTaskProxy that was created in the context of a SwComponent to an OsTaskProxy that was created in the context of an Ecu.

        A None value is a no-op and does not add to appOsTaskProxyToEcuTaskProxyMappings.
        """
        if value is not None:
            self.appOsTaskProxyToEcuTaskProxyMappings.append(value)
        return self

    def createAppOsTaskProxyToEcuTaskProxyMapping(self, short_name: str) -> AppOsTaskProxyToEcuTaskProxyMapping:
        """
        Mapping of an OsTaskProxy that was created in the context of a SwComponent to an OsTaskProxy that was created in the context of an Ecu.
        """
        if not self.IsReferrableElementExists(short_name, AppOsTaskProxyToEcuTaskProxyMapping):
            mapping = AppOsTaskProxyToEcuTaskProxyMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.appOsTaskProxyToEcuTaskProxyMappings.append(mapping)
        return cast(AppOsTaskProxyToEcuTaskProxyMapping, self.getReferrableElement(short_name, AppOsTaskProxyToEcuTaskProxyMapping))

    def getAppOsTaskProxyToEcuTaskProxyMappings(self) -> List[AppOsTaskProxyToEcuTaskProxyMapping]:
        """
        Mapping of an OsTaskProxy that was created in the context of a SwComponent to an OsTaskProxy that was created in the context of an Ecu.
        """
        return self.appOsTaskProxyToEcuTaskProxyMappings

    def addComManagementMapping(self, value: Optional[ComManagementMapping]) -> "SystemMapping":
        """
        Mappings between Mode Management PortGroups and communication channels. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=comManagementMapping.shortName, comManagementMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not add to comManagementMappings.
        """
        if value is not None:
            self.comManagementMappings.append(value)
        return self

    def createComManagementMapping(self, short_name: str) -> ComManagementMapping:
        """
        Mappings between Mode Management PortGroups and communication channels. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=comManagementMapping.shortName, comManagementMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        if not self.IsReferrableElementExists(short_name, ComManagementMapping):
            mapping = ComManagementMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.comManagementMappings.append(mapping)
        return cast(ComManagementMapping, self.getReferrableElement(short_name, ComManagementMapping))

    def getComManagementMappings(self) -> List[ComManagementMapping]:
        """
        Mappings between Mode Management PortGroups and communication channels. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=comManagementMapping.shortName, comManagementMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        return self.comManagementMappings

    def addCryptoServiceMapping(self, value: Optional[CryptoServiceMapping]) -> "SystemMapping":
        """
        This aggregation represents the collection of crypto service mappings in the context of the enclosing System Mapping. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=cryptoServiceMapping.shortName, cryptoServiceMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild

        A None value is a no-op and does not add to cryptoServiceMappings.
        """
        if value is not None:
            self.cryptoServiceMappings.append(value)
        return self

    def createSecOcCryptoServiceMapping(self, short_name: str) -> SecOcCryptoServiceMapping:
        """
        This aggregation represents the collection of crypto service mappings in the context of the enclosing System Mapping. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=cryptoServiceMapping.shortName, cryptoServiceMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, SecOcCryptoServiceMapping):
            mapping = SecOcCryptoServiceMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.cryptoServiceMappings.append(mapping)
        return cast(SecOcCryptoServiceMapping, self.getReferrableElement(short_name, SecOcCryptoServiceMapping))

    def createTlsCryptoServiceMapping(self, short_name: str) -> TlsCryptoServiceMapping:
        """
        This aggregation represents the collection of crypto service mappings in the context of the enclosing System Mapping. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=cryptoServiceMapping.shortName, cryptoServiceMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, TlsCryptoServiceMapping):
            mapping = TlsCryptoServiceMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.cryptoServiceMappings.append(mapping)
        return cast(TlsCryptoServiceMapping, self.getReferrableElement(short_name, TlsCryptoServiceMapping))

    def getCryptoServiceMappings(self) -> List[CryptoServiceMapping]:
        """
        This aggregation represents the collection of crypto service mappings in the context of the enclosing System Mapping. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=cryptoServiceMapping.shortName, cryptoServiceMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.cryptoServiceMappings

    def addDataMapping(self, value: Optional[DataMapping]) -> "SystemMapping":
        """
        The data mappings defined. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataMapping, dataMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild

        A None value is a no-op and does not add to dataMappings.
        """
        if value is not None:
            self.dataMappings.append(value)
        return self

    def getDataMappings(self) -> List[DataMapping]:
        """
        The data mappings defined. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=dataMapping, dataMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.dataMappings

    def addDdsISignalToTopicMapping(self, value: Optional[DdsCpISignalToDdsTopicMapping]) -> "SystemMapping":
        """
        Collection of DdsISignalToDdsTopicMappings. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ddsISignalToTopicMapping, ddsISignalToTopicMapping.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild

        A None value is a no-op and does not add to ddsISignalToTopicMappings.
        """
        if value is not None:
            self.ddsISignalToTopicMappings.append(value)
        return self

    def getDdsISignalToTopicMappings(self) -> List[DdsCpISignalToDdsTopicMapping]:
        """
        Collection of DdsISignalToDdsTopicMappings. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ddsISignalToTopicMapping, ddsISignalToTopicMapping.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=postBuild
        """
        return self.ddsISignalToTopicMappings

    def createECUMapping(self, short_name: str) -> ECUMapping:
        """
        Mapping of hardware related topology elements onto their counterpart definitions in the ECU Resource Template. atpVariation: The ECU Resource type might be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ecuResourceMapping.shortName, ecuResourceMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        if not self.IsReferrableElementExists(short_name, ECUMapping):
            mapping = ECUMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.ecuResourceMappings.append(mapping)
        return cast(ECUMapping, self.getReferrableElement(short_name, ECUMapping))

    def getEcuResourceMappings(self) -> List[ECUMapping]:
        """
        Mapping of hardware related topology elements onto their counterpart definitions in the ECU Resource Template. atpVariation: The ECU Resource type might be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=ecuResourceMapping.shortName, ecuResourceMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        return self.ecuResourceMappings

    def addJ1939ControllerApplicationToJ1939NmNodeMapping(self, value: Optional[J1939ControllerApplicationToJ1939NmNodeMapping]) -> "SystemMapping":
        """
        Mapping of a J1939ControllerApplication to a J1939NmNode.

        A None value is a no-op and does not add to j1939ControllerApplicationToJ1939NmNodeMappings.
        """
        if value is not None:
            self.j1939ControllerApplicationToJ1939NmNodeMappings.append(value)
        return self

    def getJ1939ControllerApplicationToJ1939NmNodeMappings(self) -> List[J1939ControllerApplicationToJ1939NmNodeMapping]:
        """
        Mapping of a J1939ControllerApplication to a J1939NmNode.
        """
        return self.j1939ControllerApplicationToJ1939NmNodeMappings

    def addMappingConstraint(self, value: Optional[MappingConstraint]) -> "SystemMapping":
        """
        Constraints that limit the mapping freedom for the mapping of SW components to ECUs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=mappingConstraint, mappingConstraint.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not add to mappingConstraints.
        """
        if value is not None:
            self.mappingConstraints.append(value)
        return self

    def getMappingConstraints(self) -> List[MappingConstraint]:
        """
        Constraints that limit the mapping freedom for the mapping of SW components to ECUs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=mappingConstraint, mappingConstraint.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        return self.mappingConstraints

    def addPncMapping(self, value: Optional[PncMapping]) -> "SystemMapping":
        """
        Mappings between Virtual Function Clusters and Partial Network Clusters. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pncMapping, pncMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not add to pncMappings.
        """
        if value is not None:
            self.pncMappings.append(value)
        return self

    def getPncMappings(self) -> List[PncMapping]:
        """
        Mappings between Virtual Function Clusters and Partial Network Clusters. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=pncMapping, pncMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        return self.pncMappings

    def addPortElementToComResourceMapping(self, value: Optional[PortElementToCommunicationResourceMapping]) -> "SystemMapping":
        """
        maps a communication resource to CP Software Clusters Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=portElementToComResourceMapping.shortName, portElementToComResourceMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild

        A None value is a no-op and does not add to portElementToComResourceMappings.
        """
        if value is not None:
            self.portElementToComResourceMappings.append(value)
        return self

    def createPortElementToComResourceMapping(self, short_name: str) -> PortElementToCommunicationResourceMapping:
        """
        maps a communication resource to CP Software Clusters Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=portElementToComResourceMapping.shortName, portElementToComResourceMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, PortElementToCommunicationResourceMapping):
            mapping = PortElementToCommunicationResourceMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.portElementToComResourceMappings.append(mapping)
        return cast(PortElementToCommunicationResourceMapping, self.getReferrableElement(short_name, PortElementToCommunicationResourceMapping))

    def getPortElementToComResourceMappings(self) -> List[PortElementToCommunicationResourceMapping]:
        """
        maps a communication resource to CP Software Clusters Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=portElementToComResourceMapping.shortName, portElementToComResourceMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.portElementToComResourceMappings

    def addResourceEstimation(self, value: Optional[EcuResourceEstimation]) -> "SystemMapping":
        """
        Resource estimations for this set of mappings, zero or one per ECU instance. atpVariation: Used ECUs are variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=resourceEstimation, resourceEstimation.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not add to resourceEstimations.
        """
        if value is not None:
            self.resourceEstimations.append(value)
        return self

    def getResourceEstimations(self) -> List[EcuResourceEstimation]:
        """
        Resource estimations for this set of mappings, zero or one per ECU instance. atpVariation: Used ECUs are variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=resourceEstimation, resourceEstimation.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        return self.resourceEstimations

    def addResourceToApplicationPartitionMapping(self, value: Optional[CpSoftwareClusterResourceToApplicationPartitionMapping]) -> "SystemMapping":
        """
        Maps a Software Cluster resource to an Application Partition to restrict the usage. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=resourceToApplicationPartitionMapping.shortName, resourceToApplicationPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not add to resourceToApplicationPartitionMappings.
        """
        if value is not None:
            self.resourceToApplicationPartitionMappings.append(value)
        return self

    def getResourceToApplicationPartitionMappings(self) -> List[CpSoftwareClusterResourceToApplicationPartitionMapping]:
        """
        Maps a Software Cluster resource to an Application Partition to restrict the usage. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=resourceToApplicationPartitionMapping.shortName, resourceToApplicationPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        return self.resourceToApplicationPartitionMappings

    def addRteEventSeparation(self, value: Optional[RteEventInSystemSeparation]) -> "SystemMapping":
        """
        Separation constraint that limits the mapping freedom for the mapping of RteEvents to OsTasks in the System context.

        A None value is a no-op and does not add to rteEventSeparations.
        """
        if value is not None:
            self.rteEventSeparations.append(value)
        return self

    def getRteEventSeparations(self) -> List[RteEventInSystemSeparation]:
        """
        Separation constraint that limits the mapping freedom for the mapping of RteEvents to OsTasks in the System context.
        """
        return self.rteEventSeparations

    def addRteEventToOsTaskProxyMapping(self, value: Optional[RteEventInSystemToOsTaskProxyMapping]) -> "SystemMapping":
        """
        Constraint that enforces a mapping of RteEvent to a particular OsTask in the System context.

        A None value is a no-op and does not add to rteEventToOsTaskProxyMappings.
        """
        if value is not None:
            self.rteEventToOsTaskProxyMappings.append(value)
        return self

    def getRteEventToOsTaskProxyMappings(self) -> List[RteEventInSystemToOsTaskProxyMapping]:
        """
        Constraint that enforces a mapping of RteEvent to a particular OsTask in the System context.
        """
        return self.rteEventToOsTaskProxyMappings

    def addSignalPathConstraint(self, value: Optional[SignalPathConstraint]) -> "SystemMapping":
        """
        Constraints that limit the mapping freedom for the mapping of data elements to signals. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=signalPathConstraint, signalPathConstraint.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not add to signalPathConstraints.
        """
        if value is not None:
            self.signalPathConstraints.append(value)
        return self

    def getSignalPathConstraints(self) -> List[SignalPathConstraint]:
        """
        Constraints that limit the mapping freedom for the mapping of data elements to signals. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=signalPathConstraint, signalPathConstraint.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        return self.signalPathConstraints

    def addSoftwareClusterToApplicationPartitionMapping(self, value: Optional[CpSoftwareClusterToApplicationPartitionMapping]) -> "SystemMapping":
        """
        The mapping of ApplicationPartitions to a CpSoftwareCluster. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=softwareClusterToApplicationPartitionMapping.shortName, softwareClusterToApplicationPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not add to softwareClusterToApplicationPartitionMappings.
        """
        if value is not None:
            self.softwareClusterToApplicationPartitionMappings.append(value)
        return self

    def getSoftwareClusterToApplicationPartitionMappings(self) -> List[CpSoftwareClusterToApplicationPartitionMapping]:
        """
        The mapping of ApplicationPartitions to a CpSoftwareCluster. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=softwareClusterToApplicationPartitionMapping.shortName, softwareClusterToApplicationPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        return self.softwareClusterToApplicationPartitionMappings

    def addSoftwareClusterToResourceMapping(self, value: Optional[CpSoftwareClusterToResourceMapping]) -> "SystemMapping":
        """
        maps a service resource to CP Software Clusters Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=softwareClusterToResourceMapping.shortName, softwareClusterToResourceMapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime

        A None value is a no-op and does not add to softwareClusterToResourceMappings.
        """
        if value is not None:
            self.softwareClusterToResourceMappings.append(value)
        return self

    def getSoftwareClusterToResourceMappings(self) -> List[CpSoftwareClusterToResourceMapping]:
        """
        maps a service resource to CP Software Clusters Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=softwareClusterToResourceMapping.shortName, softwareClusterToResourceMapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.softwareClusterToResourceMappings

    def addSwClusterMapping(self, value: Optional[CpSoftwareClusterToEcuInstanceMapping]) -> "SystemMapping":
        """
        The mappings of SW cluster to ECUs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swClusterMapping.shortName, swClusterMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not add to swClusterMappings.
        """
        if value is not None:
            self.swClusterMappings.append(value)
        return self

    def getSwClusterMappings(self) -> List[CpSoftwareClusterToEcuInstanceMapping]:
        """
        The mappings of SW cluster to ECUs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swClusterMapping.shortName, swClusterMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        return self.swClusterMappings

    def addSwcToApplicationPartitionMapping(self, value: Optional[SwcToApplicationPartitionMapping]) -> "SystemMapping":
        """
        Allows to map a given SwComponentPrototype to a formally defined partition at a point in time when the corresponding EcuInstance is not yet known or defined. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swcToApplicationPartitionMapping.shortName, swcToApplicationPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild

        A None value is a no-op and does not add to swcToApplicationPartitionMappings.
        """
        if value is not None:
            self.swcToApplicationPartitionMappings.append(value)
        return self

    def createSwcToApplicationPartitionMapping(self, short_name: str) -> SwcToApplicationPartitionMapping:
        """
        Allows to map a given SwComponentPrototype to a formally defined partition at a point in time when the corresponding EcuInstance is not yet known or defined. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swcToApplicationPartitionMapping.shortName, swcToApplicationPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, SwcToApplicationPartitionMapping):
            mapping = SwcToApplicationPartitionMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.swcToApplicationPartitionMappings.append(mapping)
        return cast(SwcToApplicationPartitionMapping, self.getReferrableElement(short_name, SwcToApplicationPartitionMapping))

    def getSwcToApplicationPartitionMappings(self) -> List[SwcToApplicationPartitionMapping]:
        """
        Allows to map a given SwComponentPrototype to a formally defined partition at a point in time when the corresponding EcuInstance is not yet known or defined. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swcToApplicationPartitionMapping.shortName, swcToApplicationPartitionMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.swcToApplicationPartitionMappings

    def createSwcToImplMapping(self, short_name: str) -> SwcToImplMapping:
        """
        The mappings of AtomicSoftwareComponent Instances to Implementations. atpVariation: Derived, because SwcToEcuMapping is variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swImplMapping.shortName, swImplMapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, SwcToImplMapping):
            mapping = SwcToImplMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.swImplMappings.append(mapping)
        return cast(SwcToImplMapping, self.getReferrableElement(short_name, SwcToImplMapping))

    def getSwImplMappings(self) -> List[SwcToImplMapping]:
        """
        The mappings of AtomicSoftwareComponent Instances to Implementations. atpVariation: Derived, because SwcToEcuMapping is variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swImplMapping.shortName, swImplMapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.swImplMappings

    def createSwcToEcuMapping(self, short_name: str) -> SwcToEcuMapping:
        """
        The mappings of SW components to ECUs. atpVariation: SWC shall be mapped to other ECUs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swMapping.shortName, swMapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        if not self.IsReferrableElementExists(short_name, SwcToEcuMapping):
            mapping = SwcToEcuMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.swMappings.append(mapping)
        return cast(SwcToEcuMapping, self.getReferrableElement(short_name, SwcToEcuMapping))

    def getSwMappings(self) -> List[SwcToEcuMapping]:
        """
        The mappings of SW components to ECUs. atpVariation: SWC shall be mapped to other ECUs. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=swMapping.shortName, swMapping.variationPoint.shortLabel vh.latestBindingTime=preCompileTime
        """
        return self.swMappings

    def addSystemSignalGroupToComResourceMapping(self, value: Optional[SystemSignalGroupToCommunicationResourceMapping]) -> "SystemMapping":
        """
        Mapping of a communication resource to a SystemSignalGroup. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=systemSignalGroupToComResourceMapping.shortName, systemSignalGroupToComResourceMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not add to systemSignalGroupToComResourceMappings.
        """
        if value is not None:
            self.systemSignalGroupToComResourceMappings.append(value)
        return self

    def getSystemSignalGroupToComResourceMappings(self) -> List[SystemSignalGroupToCommunicationResourceMapping]:
        """
        Mapping of a communication resource to a SystemSignalGroup. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=systemSignalGroupToComResourceMapping.shortName, systemSignalGroupToComResourceMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        return self.systemSignalGroupToComResourceMappings

    def addSystemSignalToComResourceMapping(self, value: Optional[SystemSignalToCommunicationResourceMapping]) -> "SystemMapping":
        """
        Mapping of a communication resource to a SystemSignal. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=systemSignalToComResourceMapping.shortName, systemSignalToComResourceMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not add to systemSignalToComResourceMappings.
        """
        if value is not None:
            self.systemSignalToComResourceMappings.append(value)
        return self

    def getSystemSignalToComResourceMappings(self) -> List[SystemSignalToCommunicationResourceMapping]:
        """
        Mapping of a communication resource to a SystemSignal. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=systemSignalToComResourceMapping.shortName, systemSignalToComResourceMapping.variationPoint.shortLabel vh.latestBindingTime=systemDesignTime
        """
        return self.systemSignalToComResourceMappings


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
    This meta-class represents the ability to identify several J1939Clusters that share a common address space for the routing of messages
    """

    # J1939SharedAddressCluster method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.324, p.694
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addParticipatingJ1939ClusterRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getParticipatingJ1939ClusterRefs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This identifies the J1939Clusters that share a common address space
        self.participatingJ1939ClusterRefs: List[RefType] = []

    def addParticipatingJ1939ClusterRef(self, value: Optional[RefType]) -> "J1939SharedAddressCluster":
        """
        This identifies the J1939Clusters that share a common address space

        A None value is a no-op and does not add to participatingJ1939ClusterRefs.
        """
        if value is not None:
            self.participatingJ1939ClusterRefs.append(value)
        return self

    def getParticipatingJ1939ClusterRefs(self) -> List[RefType]:
        """
        This identifies the J1939Clusters that share a common address space
        """
        return self.participatingJ1939ClusterRefs


class ClientIdDefinition(Identifiable, VariationPointCapable):
    """
    Several clients in one client-ECU can communicate via inter-ECU client-server communication with a server on a different ECU, if a client identifier is used to distinguish the different clients. The Client Identifier of the transaction handle that is used by the RTE can be defined by this element.
    """

    # ClientIdDefinition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 2.3, p.45 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getClientId                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setClientId                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getClientServerOperationIRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setClientServerOperationIRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The Client Identifier of the transaction handle used for an inter-ECU client server communication is defined by this attribute. If defined the RTE generator shall use this client Id.
        self.clientId: Optional[Numerical] = None

        # Reference to the ClientServerOperation that is called by the client. InstanceRef implemented by: OperationInSystemInstanceRef
        self.clientServerOperationIRef: Optional[OperationInSystemInstanceRef] = None

    def getClientId(self) -> Optional[Numerical]:
        """
        The Client Identifier of the transaction handle used for an inter-ECU client server communication is defined by this attribute. If defined the RTE generator shall use this client Id.
        """
        return self.clientId

    def setClientId(self, value: Optional[Numerical]) -> "ClientIdDefinition":
        """
        The Client Identifier of the transaction handle used for an inter-ECU client server communication is defined by this attribute. If defined the RTE generator shall use this client Id.

        A None value is a no-op and does not overwrite an existing clientId.
        """
        if value is not None:
            self.clientId = value
        return self

    def getClientServerOperationIRef(self) -> Optional[OperationInSystemInstanceRef]:
        """
        Reference to the ClientServerOperation that is called by the client. InstanceRef implemented by: OperationInSystemInstanceRef
        """
        return self.clientServerOperationIRef

    def setClientServerOperationIRef(self, value: Optional[OperationInSystemInstanceRef]) -> "ClientIdDefinition":
        """
        Reference to the ClientServerOperation that is called by the client. InstanceRef implemented by: OperationInSystemInstanceRef

        A None value is a no-op and does not overwrite an existing clientServerOperationIRef.
        """
        if value is not None:
            self.clientServerOperationIRef = value
        return self


class ClientIdDefinitionSet(ARElement):
    """
    Set of Client Identifiers that are used for inter-ECU client-server communication in the System. Tags: atp.recommendedPackage=ClientIdDefinitionSets
    """

    # ClientIdDefinitionSet method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 2.2, p.44 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getClientIdDefinitions     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addClientIdDefinition      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createClientIdDefinition   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Definition of a Client Identifier that will be used by the RTE in a inter-ECU client-server communication. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=clientIdDefinition.shortName, clientIdDefinition.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.clientIdDefinitions: List[ClientIdDefinition] = []

    def getClientIdDefinitions(self) -> List[ClientIdDefinition]:
        """
        Definition of a Client Identifier that will be used by the RTE in a inter-ECU client-server communication. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=clientIdDefinition.shortName, clientIdDefinition.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.clientIdDefinitions

    def addClientIdDefinition(self, value: ClientIdDefinition) -> "ClientIdDefinitionSet":
        """
        Definition of a Client Identifier that will be used by the RTE in a inter-ECU client-server communication. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=clientIdDefinition.shortName, clientIdDefinition.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        self.clientIdDefinitions.append(value)
        return self

    def createClientIdDefinition(self, short_name: str) -> ClientIdDefinition:
        """
        Definition of a Client Identifier that will be used by the RTE in a inter-ECU client-server communication. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=clientIdDefinition.shortName, clientIdDefinition.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if not self.IsReferrableElementExists(short_name, ClientIdDefinition):
            id_definition = ClientIdDefinition(self, short_name)
            self.addReferrableElement(id_definition)
            self.clientIdDefinitions.append(id_definition)
        return cast(ClientIdDefinition, self.getReferrableElement(short_name, ClientIdDefinition))


class System(AtpStructureElement):
    """
    The top level element of the System Description. The System description defines five major elements: Topology, Software, Communication, Mapping and Mapping Constraints. The System element directly aggregates the elements describing the Software, Mapping and Mapping Constraints; it contains a reference to an ASAM FIBEX description specifying Communication and Topology. Tags: atp.recommendedPackage=Systems

    [constr_3028] FibexElements: Each FibexElement that is used in the System Description shall be referenced by the System element in the role FibexElement.

    [constr_3027] Existence of ecuExtractVersion: In case the category of the System is SYSTEM_EXTRACT or ECU_EXTRACT the ecuExtractVersion attribute shall be defined.
    """

    # System method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 2.1, p.42
    # Spec verified: R23-11
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
        if not self.IsReferrableElementExists(short_name, J1939SharedAddressCluster):
            cluster = J1939SharedAddressCluster(self, short_name)
            self.addReferrableElement(cluster)
            self.j1939SharedAddressClusters.append(cluster)
        return cast(J1939SharedAddressCluster, self.getReferrableElement(short_name, J1939SharedAddressCluster))

    def getJ1939SharedAddressClusters(self) -> List[J1939SharedAddressCluster]:
        """
        Collection of J1939Clusters that share a common address space for the routing of messages.
        """
        return self.j1939SharedAddressClusters

    def createSystemMapping(self, short_name: str) -> SystemMapping:
        """
        Aggregation of all mapping aspects (mapping of SW components to ECUs, mapping of data elements to signals, and mapping constraints). In order to support OEM / Tier 1 interaction and shared development for one common System this aggregation is atpSplitable and atpVariation. The content of SystemMapping can be provided by several parties using different names for the SystemMapping. This element is not required when the System description is used for a network-only use-case.
        """
        if not self.IsReferrableElementExists(short_name, SystemMapping):
            mapping = SystemMapping(self, short_name)
            self.addReferrableElement(mapping)
            self.mappings.append(mapping)
        return cast(SystemMapping, self.getReferrableElement(short_name, SystemMapping))

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
        if not self.IsReferrableElementExists(short_name, RootSwCompositionPrototype):
            prototype = RootSwCompositionPrototype(self, short_name)
            self.addReferrableElement(prototype)
            self.rootSoftwareComposition = prototype
        return cast(RootSwCompositionPrototype, self.getReferrableElement(short_name, RootSwCompositionPrototype))

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
        if not self.IsReferrableElementExists(short_name, Chapter):
            chapter = Chapter(self, short_name)
            self.addReferrableElement(chapter)
            self.systemDocumentations.append(chapter)
        return cast(Chapter, self.getReferrableElement(short_name, Chapter))

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


__all__ = [
    "ApplicationPartition",
    "ApplicationPartitionToEcuPartitionMapping",
    "ARElement",
    "AppOsTaskProxyToEcuTaskProxyMapping",
    "RteEventInCompositionSeparation",
    "RteEventInCompositionToOsTaskProxyMapping",
    "RteEventInSystemSeparation",
    "RteEventInSystemToOsTaskProxyMapping",
    "ARObject",
    "AtpPrototype",
    "AtpStructureElement",
    "ByteOrderEnum",
    "Chapter",
    "ClientIdDefinition",
    "ClientIdDefinitionSet",
    "CommonSignalPath",
    "ComponentInSystemInstanceRef",
    "ComManagementMapping",
    "CryptoServiceMapping",
    "DataMapping",
    "ECUMapping",
    "Identifiable",
    "J1939SharedAddressCluster",
    "OperationInSystemInstanceRef",
    "OsTaskPreemptabilityEnum",
    "OsTaskProxy",
    "PncMapping",
    "PncMappingIdent",
    "PortGroupInSystemInstanceRef",
    "PositiveInteger",
    "RefType",
    "RevisionLabelString",
    "RootSwCompositionPrototype",
    "SignalPathConstraint",
    "SwComponentPrototypeAssignment",
    "SwcToSwcOperationArguments",
    "SwcToSwcOperationArgumentsDirectionEnum",
    "SwcToSwcSignal",
    "CpSoftwareClusterToEcuInstanceMapping",
    "CpSoftwareClusterResourceToApplicationPartitionMapping",
    "CpSoftwareClusterToApplicationPartitionMapping",
    "CpSoftwareClusterMappingSet",
    "SystemSignalGroupToCommunicationResourceMapping",
    "SystemSignalToCommunicationResourceMapping",
    "TriggerInSystemInstanceRef",
    "TriggerToSignalMapping",
    "CpSoftwareCluster",
    "SwcToEcuMapping",
    "SwcToImplMapping",
    "System",
    "SystemMapping",
    "TRefType",
    "VariableDataPrototypeInSystemInstanceRef",
    "VariationPointCapable",
]
