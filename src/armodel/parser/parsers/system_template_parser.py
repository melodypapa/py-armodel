"""
Parser for AUTOSAR SystemTemplate elements.

Handles:
- System
- SystemSignal
- SystemSignalGroup
- EcuInstance
- SwcToEcuMapping
- SwMappings
- RootSoftwareCompositions
- DataMapping
- Fibex (CAN, Ethernet, FlexRay, LIN)
- Network Management
- Transport Protocols
- Data Transformations
"""
import xml.etree.ElementTree as ET
from typing import List

from ..base_arxml_parser import BaseARXMLParser

# Core System imports
from ...models.M2.AUTOSARTemplates.SystemTemplate import (
    SwcToEcuMapping,
    System,
    SystemMapping,
)

# DataMapping imports
from ...models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    SenderReceiverToSignalGroupMapping,
    SenderReceiverToSignalMapping,
    SenderRecCompositeTypeMapping,
    SenderRecRecordElementMapping,
    SenderRecRecordTypeMapping,
)

# DiagnosticConnection
from ...models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import (
    DiagnosticConnection,
)

# ECUResourceMapping
from ...models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping import (
    ECUMapping,
)

# Fibex - CAN
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanFrame,
    CanFrameTriggering,
    RxIdentifierRange,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    AbstractCanCommunicationController,
    AbstractCanCommunicationControllerAttributes,
    CanCommunicationConnector,
    CanCommunicationController,
    CanControllerConfigurationRequirements,
    CanControllerFdConfiguration,
    CanControllerFdConfigurationRequirements,
)

# Fibex - Ethernet
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetCommunication import (
    SoAdRoutingGroup,
    SocketConnection,
    SocketConnectionBundle,
    SocketConnectionIpduIdentifier,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPort,
    CouplingPortDetails,
    CouplingPortFifo,
    CouplingPortScheduler,
    CouplingPortStructuralElement,
    EthernetCluster,
    EthernetCommunicationConnector,
    EthernetCommunicationController,
    EthernetPriorityRegeneration,
    InitialSdDelayConfig,
    MacMulticastGroup,
    RequestResponseDelay,
    SdClientConfig,
    VlanMembership,
)

# Fibex - Ethernet NetworkEndpoint and ServiceInstances
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.NetworkEndpoint import (
    DoIpEntity,
    InfrastructureServices,
    Ipv6Configuration,
    NetworkEndpoint,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    ApplicationEndpoint,
    ConsumedEventGroup,
    ConsumedServiceInstance,
    EventHandler,
    GenericTp,
    ProvidedServiceInstance,
    SdServerConfig,
    SoAdConfig,
    SocketAddress,
    TcpTp,
    TpPort,
    TransportProtocolConfiguration,
    UdpTp,
)

# Fibex - Ethernet Frame
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import (
    GenericEthernetFrame,
)

# Fibex - FlexRay
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import (
    FlexrayAbsolutelyScheduledTiming,
    FlexrayFrame,
    FlexrayFrameTriggering,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayCluster,
    FlexrayCommunicationConnector,
    FlexrayCommunicationController,
)

# Fibex - LIN
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    ApplicationEntry,
    LinFrameTriggering,
    LinScheduleTable,
    LinUnconditionalFrame,
    ScheduleTableEntry,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import (
    LinCommunicationConnector,
    LinCommunicationController,
    LinMaster,
)

# Fibex - Multiplatform
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform import (
    FrameMapping,
    Gateway,
    IPduMapping,
    ISignalMapping,
    TargetIPduRef,
)

# Fibex - Core Communication
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    DcmIPdu,
    DynamicPart,
    DynamicPartAlternative,
    Frame,
    FrameTriggering,
    GeneralPurposeIPdu,
    GeneralPurposePdu,
    IPdu,
    IPduTiming,
    ISignal,
    ISignalGroup,
    ISignalIPdu,
    ISignalIPduGroup,
    ISignalToIPduMapping,
    ISignalTriggering,
    MultiplexedIPdu,
    MultiplexedPart,
    NPdu,
    NmPdu,
    Pdu,
    PduTriggering,
    SecureCommunicationAuthenticationProps,
    SecureCommunicationFreshnessProps,
    SecureCommunicationProps,
    SecureCommunicationPropsSet,
    SecuredIPdu,
    SegmentPosition,
    StaticPart,
    SystemSignal,
    SystemSignalGroup,
    UserDefinedIPdu,
    UserDefinedPdu,
)

# Fibex - Core Topology
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    AbstractCanCluster,
    CanCluster,
    CanClusterBusOffRecovery,
    CanPhysicalChannel,
    CommConnectorPort,
    CommunicationCluster,
    CommunicationConnector,
    CommunicationController,
    CommunicationCycle,
    CycleRepetition,
    EthernetPhysicalChannel,
    FlexrayPhysicalChannel,
    FramePort,
    IPduPort,
    ISignalPort,
    LinCluster,
    LinPhysicalChannel,
    PhysicalChannel,
)

# Fibex - ECU Instance
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.EcuInstance import (
    EcuInstance,
)

# Fibex - Timing
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.Timing import (
    CyclicTiming,
    EventControlledTiming,
    TimeRangeType,
    TransmissionModeCondition,
    TransmissionModeDeclaration,
    TransmissionModeTiming,
)

# InstanceRefs
from ...models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
    ComponentInSystemInstanceRef,
    VariableDataPrototypeInSystemInstanceRef,
)

# Network Management
from ...models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    CanNmCluster,
    CanNmClusterCoupling,
    CanNmNode,
    NmCluster,
    NmConfig,
    NmEcu,
    NmNode,
    UdpNmCluster,
    UdpNmClusterCoupling,
    UdpNmEcu,
    UdpNmNode,
)

# SWmapping
from ...models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import (
    SwcToImplMapping,
)

# Transformer
from ...models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    BufferProperties,
    DataTransformation,
    DataTransformationSet,
    EndToEndTransformationDescription,
    EndToEndTransformationISignalProps,
    TransformationDescription,
    TransformationISignalProps,
    TransformationTechnology,
)

# Transport Protocols
from ...models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    CanTpAddress,
    CanTpChannel,
    CanTpConfig,
    CanTpConnection,
    CanTpEcu,
    CanTpNode,
    DoIpLogicAddress,
    DoIpTpConfig,
    DoIpTpConnection,
    LinTpConfig,
    LinTpConnection,
    LinTpNode,
    TpAddress,
    TpConfig,
    TpConnection,
)

# PortInterface mappings (for transformation)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    DataPrototypeMapping,
)

# EcuResourceTemplate
from ...models.M2.AUTOSARTemplates.EcuResourceTemplate import (
    HwDescriptionEntity,
    HwElement,
    HwPinGroup,
)
from ...models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import (
    HwAttributeDef,
    HwCategory,
    HwType,
)

# DiagnosticExtract
from ...models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import (
    DiagnosticServiceTable,
)

# CommonStructure
from ...models.M2.AUTOSARTemplates.CommonStructure import (
    ValueSpecification,
)

# AutosarTopLevelStructure
from ...models.M2.AUTOSARTemplates.AutosarTopLevelStructure import (
    AUTOSAR,
)


class SystemTemplateParser(BaseARXMLParser):
    """
    Parser for AUTOSAR SystemTemplate elements.

    This parser handles:
    - System configuration and mappings
    - System signals and signal groups
    - ECU instances
    - Fibex elements (CAN, LIN, Ethernet, FlexRay)
    - Network management
    - Transport protocols
    - Data transformations
    - Communication connectors and controllers
    """

    def __init__(self, options=None, main_parser=None):
        """Initialize SystemTemplateParser."""
        super().__init__(options)
        self._main_parser = main_parser

    # System Elements


    def readSystem(self, element: ET.Element, system: System):
        self.logger.debug("Read System <%s>" % system.getShortName())
        self.readIdentifiable(element, system)
        system.setEcuExtractVersion(self.getChildElementOptionalLiteral(element, "ECU-EXTRACT-VERSION"))
        self.readSystemFibexElementRefs(element, system)
        self.readSystemMappings(element, system)
        self.readRootSwCompositionPrototype(element, system)
        system.setSystemVersion(self.getChildElementOptionalRevisionLabelString(element, "SYSTEM-VERSION"))
        AUTOSAR.getInstance().addSystem(system)


    def readSystemSignal(self, element: ET.Element, signal: SystemSignal):
        self.logger.debug("Read SystemSignal <%s>" % signal.getShortName())
        self.readIdentifiable(element, signal)
        signal.setDynamicLength(self.getChildElementOptionalBooleanValue(element, "DYNAMIC-LENGTH")) \
              .setPhysicalProps(self.getSwDataDefProps(element, "PHYSICAL-PROPS"))


    def readSystemSignalGroup(self, element: ET.Element, group: SystemSignalGroup):
        self.logger.debug("Read SystemSignalGroup <%s>" % group.getShortName())
        self.readIdentifiable(element, group)
        for ref_type in self.getChildElementRefTypeList(element, "SYSTEM-SIGNAL-REFS/SYSTEM-SIGNAL-REF"):
            group.addSystemSignalRefs(ref_type)


    def readSystemFibexElementRefs(self, element: ET.Element, system: System):
        for ref in self.getChildElementRefTypeList(element, "FIBEX-ELEMENTS/FIBEX-ELEMENT-REF-CONDITIONAL/FIBEX-ELEMENT-REF"):
            system.addFibexElementRef(ref)


    def readSystemMappings(self, element: ET.Element, system: System):
        for child_element in self.findall(element, "MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SYSTEM-MAPPING":
                mapping = system.createSystemMapping(self.getShortName(child_element))
                self.readSystemMapping(child_element, mapping)
            else:
                self.notImplemented("Unsupported Mapping %s" % tag_name)


    def readSystemMapping(self, element: ET.Element, mapping: SystemMapping):
        # self.logger.debug("Read SystemMapping <%s>" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        self.readSystemMappingDataMappings(element, mapping)
        self.readSystemMappingEcuResourceMappings(element, mapping)
        self.readSystemMappingSwImplMappings(element, mapping)
        self.readSystemMappingSwMappings(element, mapping)


    def readSwcToEcuMapping(self, element: ET.Element, mapping: SwcToEcuMapping):
        # self.logger.debug("SwcToEcuMapping %s" % mapping.getShortName())
        self.readIdentifiable(element, mapping)
        for child_element in self.findall(element, "COMPONENT-IREFS/COMPONENT-IREF"):
            mapping.addComponentIRef(self.getComponentInSystemInstanceRef(child_element))
        mapping.setEcuInstanceRef(self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF"))


    def readSwcToImplMapping(self, element: ET.Element, mapping: SwcToImplMapping):
        self.readIdentifiable(element, mapping)
        mapping.setComponentImplementationRef(self.getChildElementOptionalRefType(element, "COMPONENT-IMPLEMENTATION-REF"))
        for child_element in self.findall(element, "COMPONENT-IREFS/COMPONENT-IREF"):
            mapping.addComponentIRef(self.getComponentInSystemInstanceRef(child_element))


    def readEcuInstance(self, element: ET.Element, instance: EcuInstance):
        self.logger.debug("Read EcuInstance <%s>" % instance.getShortName())
        self.readIdentifiable(element, instance)
        self.readEcuInstanceAssociatedComIPduGroupRefs(element, instance)
        instance.setComConfigurationGwTimeBase(self.getChildElementOptionalTimeValue(element, "COM-CONFIGURATION-GW-TIME-BASE")) \
                .setComConfigurationRxTimeBase(self.getChildElementOptionalTimeValue(element, "COM-CONFIGURATION-RX-TIME-BASE")) \
                .setComConfigurationTxTimeBase(self.getChildElementOptionalTimeValue(element, "COM-CONFIGURATION-TX-TIME-BASE")) \
                .setComEnableMDTForCyclicTransmission(self.getChildElementOptionalBooleanValue(element, "COM-ENABLE-MDT-FOR-CYCLIC-TRANSMISSION"))
        self.readEcuInstanceCommControllers(element, instance)
        self.readEcuInstanceConnectors(element, instance)
        instance.setDiagnosticAddress(self.getChildElementOptionalIntegerValue(element, "DIAGNOSTIC-ADDRESS")) \
                .setSleepModeSupported(self.getChildElementOptionalBooleanValue(element, "SLEEP-MODE-SUPPORTED")) \
                .setWakeUpOverBusSupported(self.getChildElementOptionalBooleanValue(element, "WAKE-UP-OVER-BUS-SUPPORTED"))



    def readEcuInstanceCommControllers(self, element: ET.Element, instance: EcuInstance):
        self.logger.debug("readEcuInstanceCommControllers %s" % instance.getShortName())
        for child_element in self.findall(element, "COMM-CONTROLLERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-COMMUNICATION-CONTROLLER":
                controller = instance.createCanCommunicationController(self.getShortName(child_element))
                self.readCanCommunicationController(child_element, controller)
            elif tag_name == "ETHERNET-COMMUNICATION-CONTROLLER":
                controller = instance.createEthernetCommunicationController(self.getShortName(child_element))
                self.readEthernetCommunicationController(child_element, controller)
            elif tag_name == "LIN-MASTER":
                controller = instance.createLinMaster(self.getShortName(child_element))
                self.readLinMaster(child_element, controller)
            elif tag_name == "FLEXRAY-COMMUNICATION-CONTROLLER":
                controller = instance.createFlexrayCommunicationController(self.getShortName(child_element))
                self.readFlexrayCommunicationController(child_element, controller)
            else:
                self.raiseError("Unsupported Communication Controller <%s>" % tag_name)


    def readEcuInstanceConnectors(self, element: ET.Element, instance: EcuInstance):
        self.logger.debug("readEcuInstanceCommControllers %s" % instance.getShortName())
        for child_element in self.findall(element, "CONNECTORS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-COMMUNICATION-CONNECTOR":
                connector = instance.createCanCommunicationConnector(self.getShortName(child_element))
                self.readCanCommunicationConnector(child_element, connector)
            elif tag_name == "ETHERNET-COMMUNICATION-CONNECTOR":
                connector = instance.createEthernetCommunicationConnector(self.getShortName(child_element))
                self.readEthernetCommunicationConnector(child_element, connector)
            elif tag_name == "LIN-COMMUNICATION-CONNECTOR":
                connector = instance.createLinCommunicationConnector(self.getShortName(child_element))
                self.readLinCommunicationConnector(child_element, connector)
            elif tag_name == "FLEXRAY-COMMUNICATION-CONNECTOR":
                connector = instance.createFlexrayCommunicationConnector(self.getShortName(child_element))
                self.readFlexrayCommunicationConnector(child_element, connector)
            else:
                self.notImplemented("Unsupported Communication Connector <%s>" % tag_name)


    def readEcuInstanceAssociatedComIPduGroupRefs(self, element: ET.Element, instance: EcuInstance):
        for ref in self.getChildElementRefTypeList(element, "ASSOCIATED-COM-I-PDU-GROUP-REFS/ASSOCIATED-COM-I-PDU-GROUP-REF"):
            instance.addAssociatedComIPduGroupRef(ref)


    def readGateway(self, element: ET.Element, gateway: Gateway):
        self.logger.debug("Read Gateway <%s>" % gateway.getShortName())
        self.readIdentifiable(element, gateway)
        gateway.setEcuRef(self.getChildElementOptionalRefType(element, "ECU-REF"))
        for mapping in self.getIPduMappings(element):
            gateway.addIPduMapping(mapping)
        for mapping in self.getISignalMappings(element):
            gateway.addSignalMapping(mapping)


    def readCommunicationCluster(self, element: ET.Element, cluster: CommunicationCluster):
        cluster.setBaudrate(self.getChildElementOptionalNumericalValue(element, "BAUDRATE"))
        self.readCommunicationClusterPhysicalChannels(element, cluster)
        cluster.setProtocolName(self.getChildElementOptionalLiteral(element, "PROTOCOL-NAME")) \
               .setProtocolVersion(self.getChildElementOptionalLiteral(element, "PROTOCOL-VERSION"))
        


    def readCommunicationClusterPhysicalChannels(self, element: ET.Element, cluster: CommunicationCluster):
        for child_element in self.findall(element, "PHYSICAL-CHANNELS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-PHYSICAL-CHANNEL":
                channel = cluster.createCanPhysicalChannel(self.getShortName(child_element))
                self.readCanPhysicalChannel(child_element, channel)
            elif tag_name == "LIN-PHYSICAL-CHANNEL":
                channel = cluster.createLinPhysicalChannel(self.getShortName(child_element))
                self.readLinPhysicalChannel(child_element, channel)
            elif tag_name == "ETHERNET-PHYSICAL-CHANNEL":
                channel = cluster.createEthernetPhysicalChannel(self.getShortName(child_element))
                self.readEthernetPhysicalChannel(child_element, channel)
            elif tag_name == "FLEXRAY-PHYSICAL-CHANNEL":
                channel = cluster.createFlexrayPhysicalChannel(self.getShortName(child_element))
                self.readFlexrayPhysicalChannel(child_element, channel)
            else:
                self.notImplemented("Unsupported Physical Channel <%s>" % tag_name)


    def readCommunicationConnector(self, element: ET.Element, connector: CommunicationConnector):
        self.readIdentifiable(element, connector)
        connector.setCommControllerRef(self.getChildElementOptionalRefType(element, "COMM-CONTROLLER-REF"))
        self.readCommunicationConnectorEcuCommPortInstances(element, connector)
        connector.setPncGatewayType(self.getChildElementOptionalLiteral(element, "PNC-GATEWAY-TYPE"))


    def readCommunicationConnectorEcuCommPortInstances(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCommunicationConnectorEcuCommPortInstances(*args, **kwargs)


    def readCommunicationController(self, element: ET.Element, controller: CommunicationController):
        controller.setWakeUpByControllerSupported(self.getChildElementOptionalBooleanValue(element, "WAKE-UP-BY-CONTROLLER-SUPPORTED"))


    def readFramePort(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readFramePort(*args, **kwargs)


    def readIPduPort(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readIPduPort(*args, **kwargs)


    def readISignalPort(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readISignalPort(*args, **kwargs)


    def readAbstractCanCluster(self, element: ET.Element, cluster: AbstractCanCluster):
        self.readCommunicationCluster(element, cluster)
        cluster.setBusOffRecovery(self.getCanClusterBusOffRecovery(element, "BUS-OFF-RECOVERY")) \
               .setCanFdBaudrate(self.getChildElementOptionalNumericalValue(element, "CAN-FD-BAUDRATE")) \
               .setSpeed(self.getChildElementOptionalNumericalValue(element, "SPEED"))


    def readCanCluster(self, element: ET.Element, cluster: CanCluster):
        self.logger.debug("Read CanCluster <%s>" % cluster.getShortName())
        self.readIdentifiable(element, cluster)
        child_element = self.find(element, "CAN-CLUSTER-VARIANTS/CAN-CLUSTER-CONDITIONAL")
        if child_element is not None:
            self.readAbstractCanCluster(child_element, cluster)


    def readCanPhysicalChannel(self, element: ET.Element, channel: CanPhysicalChannel):
        self.readPhysicalChannel(element, channel)


    def readCanFrame(self, element: ET.Element, frame: CanFrame):
        self.logger.debug("Read CanFrame <%s>" % frame.getShortName())
        self.readFrame(element, frame)


    def readCanFrameTriggering(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCanFrameTriggering(*args, **kwargs)


    def readCanCommunicationController(self, element: ET.Element, controller: CanCommunicationController):
        self.logger.debug("Read CanCommunicationController %s" % controller.getShortName())
        self.readIdentifiable(element, controller)
        child_element = self.find(element, "CAN-COMMUNICATION-CONTROLLER-VARIANTS/CAN-COMMUNICATION-CONTROLLER-CONDITIONAL")
        if child_element is not None:
            self.readAbstractCanCommunicationController(child_element, controller)


    def readCanCommunicationConnector(self, element: ET.Element, connector: CanCommunicationConnector):
        self.readCommunicationConnector(element, connector)


    def readCanControllerConfigurationRequirements(self, element: ET.Element, requirements: CanControllerConfigurationRequirements):
        self.readAbstractCanCommunicationControllerAttributes(element, requirements)
        requirements.setMaxNumberOfTimeQuantaPerBit(self.getChildElementOptionalIntegerValue(element, "MAX-NUMBER-OF-TIME-QUANTA-PER-BIT")) \
                    .setMaxSamplePoint(self.getChildElementOptionalFloatValue(element, "MAX-SAMPLE-POINT")) \
                    .setMaxSyncJumpWidth(self.getChildElementOptionalFloatValue(element, "MAX-SYNC-JUMP-WIDTH")) \
                    .setMinNumberOfTimeQuantaPerBit(self.getChildElementOptionalIntegerValue(element, "MIN-NUMBER-OF-TIME-QUANTA-PER-BIT")) \
                    .setMinSamplePoint(self.getChildElementOptionalFloatValue(element, "MIN-SAMPLE-POINT")) \
                    .setMinSyncJumpWidth(self.getChildElementOptionalFloatValue(element, "MIN-SYNC-JUMP-WIDTH"))


    def readLinCluster(self, element: ET.Element, cluster: LinCluster):
        self.logger.debug("Read LinCluster <%s>" % cluster.getShortName())
        self.readIdentifiable(element, cluster)
        child_element = self.find(element, "LIN-CLUSTER-VARIANTS/LIN-CLUSTER-CONDITIONAL")
        if child_element is not None:
            self.readCommunicationCluster(child_element, cluster)


    def readLinPhysicalChannel(self, element: ET.Element, channel: LinPhysicalChannel):
        self.readPhysicalChannel(element, channel)
        self.readLinPhysicalChannelScheduleTables(element, channel)


    def readLinUnconditionalFrame(self, element: ET.Element, frame: LinUnconditionalFrame):
        self.logger.debug("Read LinUnconditionalFrame <%s>" % frame.getShortName())
        self.readFrame(element, frame)


    def readLinScheduleTable(self, element: ET.Element, table: LinScheduleTable):
        self.readIdentifiable(element, table)
        table.setResumePosition(self.getChildElementOptionalLiteral(element, "RESUME-POSITION")) \
             .setRunMode(self.getChildElementOptionalLiteral(element, "RUN-MODE"))
        self.readLinScheduleTableTableEntries(element, table)


    def readLinFrameTriggering(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readLinFrameTriggering(*args, **kwargs)


    def readLinCommunicationController(self, element: ET.Element, controller: LinCommunicationController):
        self.readCommunicationController(element, controller)
        controller.setProtocolVersion(self.getChildElementOptionalLiteral(element, "PROTOCOL-VERSION"))


    def readLinCommunicationConnector(self, element: ET.Element, connector: LinCommunicationConnector):
        self.readCommunicationConnector(element, connector)


    def readLinMaster(self, element: ET.Element, controller: LinMaster):
        self.logger.debug("Read LinMaster %s" % controller.getShortName())
        self.readIdentifiable(element, controller)
        child_element = self.find(element, "LIN-MASTER-VARIANTS/LIN-MASTER-CONDITIONAL")
        if child_element is not None:
            self.readLinCommunicationController(child_element, controller)
            controller.setTimeBase(self.getChildElementOptionalTimeValue(child_element, "TIME-BASE")) \
                      .setTimeBaseJitter(self.getChildElementOptionalTimeValue(child_element, "TIME-BASE-JITTER"))


    def readEthernetCluster(self, element: ET.Element, cluster: EthernetCluster):
        self.logger.debug("Read EthernetCluster <%s>" % cluster.getShortName())
        self.readIdentifiable(element, cluster)
        child_element = self.find(element, "ETHERNET-CLUSTER-VARIANTS/ETHERNET-CLUSTER-CONDITIONAL")
        if child_element is not None:
            self.readCommunicationCluster(child_element, cluster)
            self.readEthernetClusterMacMulticastGroups(child_element, cluster)


    def readEthernetClusterMacMulticastGroups(self, element: ET.Element, cluster: EthernetCluster):
        for child_element in self.findall(element, "MAC-MULTICAST-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if (tag_name == "MAC-MULTICAST-GROUP"):
                group = cluster.createMacMulticastGroup(self.getShortName(child_element))
                self.readMacMulticastGroup(child_element, group)
            else:
                self.notImplemented("Unsupported assigned data type <%s>" % tag_name)


    def readEthernetPhysicalChannel(self, element: ET.Element, channel: EthernetPhysicalChannel):
        self.readPhysicalChannel(element, channel)
        self.readEthernetPhysicalChannelNetworkEndPoints(element, channel)
        channel.setSoAdConfig(self.getSoAdConfig(element, "SO-AD-CONFIG"))
        self.readEthernetPhysicalChannelVlan(element, channel)


    def readEthernetPhysicalChannelNetworkEndPoints(self, element: ET.Element, channel: EthernetPhysicalChannel):
        for child_element in self.findall(element, "NETWORK-ENDPOINTS/NETWORK-ENDPOINT"):
            end_point = channel.createNetworkEndPoint(self.getShortName(child_element))
            self.readNetworkEndPoint(child_element, end_point)


    def readEthernetPhysicalChannelVlan(self, element: ET.Element, channel: EthernetPhysicalChannel):
        child_element = self.find(element, "VLAN")
        if child_element is not None:
            vlan = channel.createVlanConfig(self.getShortName(child_element))
            vlan.setVlanIdentifier(self.getChildElementOptionalPositiveInteger(child_element, "VLAN-IDENTIFIER"))


    def readGenericEthernetFrame(self, element: ET.Element, frame: GenericEthernetFrame):
        self.logger.debug("Read GenericEthernetFrame <%s>" % frame.getShortName())
        self.readFrame(element, frame)


    def readEthernetCommunicationController(self, element: ET.Element, controller: EthernetCommunicationController):
        self.logger.debug("Read EthernetCommunicationController %s" % controller.getShortName())
        self.readIdentifiable(element, controller)
        child_element = self.find(element, "ETHERNET-COMMUNICATION-CONTROLLER-VARIANTS/ETHERNET-COMMUNICATION-CONTROLLER-CONDITIONAL")
        if child_element is not None:
            self.readCommunicationController(child_element, controller)
            self.readEthernetCommunicationControllerCouplingPorts(child_element, controller)


    def readEthernetCommunicationControllerCouplingPorts(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readEthernetCommunicationControllerCouplingPorts(*args, **kwargs)


    def readEthernetCommunicationConnector(self, element: ET.Element, connector: EthernetCommunicationConnector):
        self.readCommunicationConnector(element, connector)
        connector.setMaximumTransmissionUnit(self.getChildElementOptionalPositiveInteger(element, "MAXIMUM-TRANSMISSION-UNIT"))
        self.readEthernetCommunicationConnectorNetworkEndpointRefs(element, connector)


    def readEthernetCommunicationConnectorNetworkEndpointRefs(self, element: ET.Element, connector: EthernetCommunicationConnector):
        for ref in self.getChildElementRefTypeList(element, "NETWORK-ENDPOINT-REFS/NETWORK-ENDPOINT-REF"):
            connector.addNetworkEndpointRef(ref)


    def readCouplingPort(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPort(*args, **kwargs)


    def readCouplingPortFifo(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPortFifo(*args, **kwargs)


    def readCouplingPortScheduler(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPortScheduler(*args, **kwargs)


    def readCouplingPortVlanMemberships(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPortVlanMemberships(*args, **kwargs)


    def readCouplingPortDetailsEthernetPriorityRegenerations(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPortDetailsEthernetPriorityRegenerations(*args, **kwargs)


    def readCouplingPortDetailsCouplingPortStructuralElements(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPortDetailsCouplingPortStructuralElements(*args, **kwargs)


    def readCouplingPortSchedulerCouplingPortStructuralElement(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readCouplingPortSchedulerCouplingPortStructuralElement(*args, **kwargs)


    def readVlanMembership(self, element: ET.Element, membership: VlanMembership):
        membership.setSendActivity(self.getChildElementOptionalLiteral(element, "SEND-ACTIVITY")) \
                  .setVlanRef(self.getChildElementOptionalRefType(element, "VLAN-REF"))
    


    def readEthernetPriorityRegeneration(self, element: ET.Element, regeneration: EthernetPriorityRegeneration):
        regeneration.setIngressPriority(self.getChildElementOptionalPositiveInteger(element, "INGRESS-PRIORITY")) \
                    .setRegeneratedPriority(self.getChildElementOptionalPositiveInteger(element, "REGENERATED-PRIORITY"))


    def readFlexrayCluster(self, element: ET.Element, cluster: FlexrayCluster):
        self.logger.debug("Read FlexrayCluster <%s>" % cluster.getShortName())
        self.readIdentifiable(element, cluster)
        child_element = self.find(element, "FLEXRAY-CLUSTER-VARIANTS/FLEXRAY-CLUSTER-CONDITIONAL")
        if child_element is not None:
            self.readCommunicationCluster(child_element, cluster)
            cluster.setActionPointOffset(self.getChildElementOptionalIntegerValue(child_element, "ACTION-POINT-OFFSET")) \
                   .setBit(self.getChildElementOptionalTimeValue(child_element, "BIT")) \
                   .setCasRxLowMax(self.getChildElementOptionalIntegerValue(child_element, "CAS-RX-LOW-MAX")) \
                   .setColdStartAttempts(self.getChildElementOptionalIntegerValue(child_element, "COLD-START-ATTEMPTS")) \
                   .setCycle(self.getChildElementOptionalTimeValue(child_element, "CYCLE")) \
                   .setCycleCountMax(self.getChildElementOptionalIntegerValue(child_element, "CYCLE-COUNT-MAX")) \
                   .setDetectNitError(self.getChildElementOptionalBooleanValue(child_element, "DETECT-NIT-ERROR")) \
                   .setDynamicSlotIdlePhase(self.getChildElementOptionalIntegerValue(child_element, "DYNAMIC-SLOT-IDLE-PHASE")) \
                   .setIgnoreAfterTx(self.getChildElementOptionalIntegerValue(child_element, "IGNORE-AFTER-TX")) \
                   .setListenNoise(self.getChildElementOptionalIntegerValue(child_element, "LISTEN-NOISE")) \
                   .setMacroPerCycle(self.getChildElementOptionalIntegerValue(child_element, "MACRO-PER-CYCLE")) \
                   .setMacrotickDuration(self.getChildElementOptionalTimeValue(child_element, "MACROTICK-DURATION")) \
                   .setMaxWithoutClockCorrectionFatal(self.getChildElementOptionalIntegerValue(child_element, "MAX-WITHOUT-CLOCK-CORRECTION-FATAL")) \
                   .setMaxWithoutClockCorrectionPassive(self.getChildElementOptionalIntegerValue(child_element, "MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE")) \
                   .setMinislotActionPointOffset(self.getChildElementOptionalIntegerValue(child_element, "MINISLOT-ACTION-POINT-OFFSET")) \
                   .setMinislotDuration(self.getChildElementOptionalIntegerValue(child_element, "MINISLOT-DURATION")) \
                   .setNetworkIdleTime(self.getChildElementOptionalIntegerValue(child_element, "NETWORK-IDLE-TIME")) \
                   .setNetworkManagementVectorLength(self.getChildElementOptionalIntegerValue(child_element, "NETWORK-MANAGEMENT-VECTOR-LENGTH")) \
                   .setNumberOfMinislots(self.getChildElementOptionalIntegerValue(child_element, "NUMBER-OF-MINISLOTS")) \
                   .setNumberOfStaticSlots(self.getChildElementOptionalIntegerValue(child_element, "NUMBER-OF-STATIC-SLOTS")) \
                   .setOffsetCorrectionStart(self.getChildElementOptionalIntegerValue(child_element, "OFFSET-CORRECTION-START")) \
                   .setPayloadLengthStatic(self.getChildElementOptionalIntegerValue(child_element, "PAYLOAD-LENGTH-STATIC")) \
                   .setSafetyMargin(self.getChildElementOptionalIntegerValue(child_element, "SAFETY-MARGIN")) \
                   .setSampleClockPeriod(self.getChildElementOptionalTimeValue(child_element, "SAMPLE-CLOCK-PERIOD")) \
                   .setStaticSlotDuration(self.getChildElementOptionalIntegerValue(child_element, "STATIC-SLOT-DURATION")) \
                   .setSyncFrameIdCountMax(self.getChildElementOptionalIntegerValue(child_element, "SYNC-FRAME-ID-COUNT-MAX")) \
                   .setTransmissionStartSequenceDuration(self.getChildElementOptionalIntegerValue(child_element, "TRANSMISSION-START-SEQUENCE-DURATION")) \
                   .setWakeupRxIdle(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-IDLE")) \
                   .setWakeupRxLow(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-LOW")) \
                   .setWakeupRxWindow(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-RX-WINDOW")) \
                   .setWakeupTxActive(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-TX-ACTIVE")) \
                   .setWakeupTxIdle(self.getChildElementOptionalIntegerValue(child_element, "WAKEUP-TX-IDLE"))            # noqa E501


    def readFlexrayPhysicalChannel(self, element: ET.Element, channel: FlexrayPhysicalChannel):
        self.readPhysicalChannel(element, channel)
        channel.setChannelName(self.getChildElementOptionalLiteral(element, "CHANNEL-NAME"))


    def readFlexrayFrame(self, element: ET.Element, frame: FlexrayFrame):
        self.logger.debug("Read FlexrayFrame <%s>" % frame.getShortName())
        self.readFrame(element, frame)
   


    def readFlexrayFrameTriggering(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readFlexrayFrameTriggering(*args, **kwargs)


    def readFlexrayFrameTriggeringAbsolutelyScheduledTimings(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readFlexrayFrameTriggeringAbsolutelyScheduledTimings(*args, **kwargs)


    def readFlexrayCommunicationController(self, element: ET.Element, controller: FlexrayCommunicationController):
        self.logger.debug("Read CommunicationController <%s>" % controller.getShortName())
        self.readIdentifiable(element, controller)
        child_element = self.find(element, "FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS/FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL")
        if child_element is not None:
            self.readCommunicationController(element, controller)
            controller.setAcceptedStartupRange(self.getChildElementOptionalIntegerValue(child_element, "ACCEPTED-STARTUP-RANGE")) \
                      .setAllowHaltDueToClock(self.getChildElementOptionalBooleanValue(child_element, "ALLOW-HALT-DUE-TO-CLOCK")) \
                      .setAllowPassiveToActive(self.getChildElementOptionalIntegerValue(child_element, "ALLOW-PASSIVE-TO-ACTIVE")) \
                      .setClusterDriftDamping(self.getChildElementOptionalIntegerValue(child_element, "CLUSTER-DRIFT-DAMPING")) \
                      .setDecodingCorrection(self.getChildElementOptionalIntegerValue(child_element, "DECODING-CORRECTION")) \
                      .setDelayCompensationA(self.getChildElementOptionalIntegerValue(child_element, "DELAY-COMPENSATION-A")) \
                      .setDelayCompensationB(self.getChildElementOptionalIntegerValue(child_element, "DELAY-COMPENSATION-B")) \
                      .setKeySlotOnlyEnabled(self.getChildElementOptionalBooleanValue(child_element, "KEY-SLOT-ONLY-ENABLED")) \
                      .setKeySlotUsedForStartUp(self.getChildElementOptionalBooleanValue(child_element, "KEY-SLOT-USED-FOR-START-UP")) \
                      .setKeySlotUsedForSync(self.getChildElementOptionalBooleanValue(child_element, "KEY-SLOT-USED-FOR-SYNC")) \
                      .setLatestTX(self.getChildElementOptionalIntegerValue(child_element, "LATEST-TX")) \
                      .setListenTimeout(self.getChildElementOptionalIntegerValue(child_element, "LISTEN-TIMEOUT")) \
                      .setMacroInitialOffsetA(self.getChildElementOptionalIntegerValue(child_element, "MACRO-INITIAL-OFFSET-A")) \
                      .setMacroInitialOffsetB(self.getChildElementOptionalIntegerValue(child_element, "MACRO-INITIAL-OFFSET-B")) \
                      .setMaximumDynamicPayloadLength(self.getChildElementOptionalIntegerValue(child_element, "MAXIMUM-DYNAMIC-PAYLOAD-LENGTH")) \
                      .setMicroInitialOffsetA(self.getChildElementOptionalIntegerValue(child_element, "MICRO-INITIAL-OFFSET-A")) \
                      .setMicroInitialOffsetB(self.getChildElementOptionalIntegerValue(child_element, "MICRO-INITIAL-OFFSET-B")) \
                      .setMicroPerCycle(self.getChildElementOptionalIntegerValue(child_element, "MICRO-PER-CYCLE")) \
                      .setMicrotickDuration(self.getChildElementOptionalTimeValue(child_element, "MICROTICK-DURATION")) \
                      .setOffsetCorrectionOut(self.getChildElementOptionalIntegerValue(child_element, "OFFSET-CORRECTION-OUT")) \
                      .setRateCorrectionOut(self.getChildElementOptionalIntegerValue(child_element, "RATE-CORRECTION-OUT")) \
                      .setSamplesPerMicrotick(self.getChildElementOptionalIntegerValue(child_element, "SAMPLES-PER-MICROTICK")) \
                      .setWakeUpPattern(self.getChildElementOptionalIntegerValue(child_element, "WAKE-UP-PATTERN"))


    def readFlexrayCommunicationConnector(self, element: ET.Element, connector: FlexrayCommunicationConnector):
        self.readCommunicationConnector(element, connector)


    def readFlexrayAbsolutelyScheduledTiming(self, element: ET.Element, timing: FlexrayAbsolutelyScheduledTiming):
        self.readARObjectAttributes(element, timing)
        self.readFlexrayAbsolutelyScheduledTimingCommunicationCycle(element, timing)
        timing.setSlotID(self.getChildElementOptionalPositiveInteger(element, "SLOT-ID"))
        


    def readFlexrayAbsolutelyScheduledTimingCommunicationCycle(self, element: ET.Element, timing: FlexrayAbsolutelyScheduledTiming):
        for child_element in self.findall(element, "COMMUNICATION-CYCLE/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CYCLE-REPETITION":
                repetition = CycleRepetition()
                self.readCycleRepetition(child_element, repetition)
                timing.setCommunicationCycle(repetition)
            else:
                self.notImplemented("Unsupported CommunicationCycle <%s>" % tag_name)
        


    def readSystemSignal(self, element: ET.Element, signal: SystemSignal):
        self.logger.debug("Read SystemSignal <%s>" % signal.getShortName())
        self.readIdentifiable(element, signal)
        signal.setDynamicLength(self.getChildElementOptionalBooleanValue(element, "DYNAMIC-LENGTH")) \
              .setPhysicalProps(self.getSwDataDefProps(element, "PHYSICAL-PROPS"))


    def readSystemSignalGroup(self, element: ET.Element, group: SystemSignalGroup):
        self.logger.debug("Read SystemSignalGroup <%s>" % group.getShortName())
        self.readIdentifiable(element, group)
        for ref_type in self.getChildElementRefTypeList(element, "SYSTEM-SIGNAL-REFS/SYSTEM-SIGNAL-REF"):
            group.addSystemSignalRefs(ref_type)


    def readISignal(self, element: ET.Element, signal: ISignal):
        self.logger.debug("Read ISignal <%s>" % signal.getShortName())
        self.readIdentifiable(element, signal)
        signal.setDataTypePolicy(self.getChildElementOptionalLiteral(element, "DATA-TYPE-POLICY")) \
              .setISignalType(self.getChildElementOptionalLiteral(element, "I-SIGNAL-TYPE")) \
              .setInitValue(self.getInitValue(element)) \
              .setLength(self.getChildElementOptionalNumericalValue(element, "LENGTH")) \
              .setNetworkRepresentationProps(self.getSwDataDefProps(element, "NETWORK-REPRESENTATION-PROPS")) \
              .setSystemSignalRef(self.getChildElementOptionalRefType(element, "SYSTEM-SIGNAL-REF"))


    def readISignalGroup(self, element: ET.Element, group: ISignalGroup):
        self.logger.debug("Read ISignalGroup <%s>" % group.getShortName())
        self.readIdentifiable(element, group)
        self.readISignalGroupComBasedSignalGroupTransformation(element, group)
        self.readISignalGroupISignalRef(element, group)
        group.setSystemSignalGroupRef(self.getChildElementOptionalRefType(element, "SYSTEM-SIGNAL-GROUP-REF"))
        self.readISignalGroupTransformationISignalProps(element, group)


    def readISignalGroupISignalRef(self, element: ET.Element, group: ISignalGroup):
        for ref_type in self.getChildElementRefTypeList(element, "I-SIGNAL-REFS/I-SIGNAL-REF"):
            group.addISignalRef(ref_type)


    def readISignalGroupComBasedSignalGroupTransformation(self, element: ET.Element, group: ISignalGroup):
        for ref in self.getChildElementRefTypeList(element, "COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS/DATA-TRANSFORMATION-REF-CONDITIONAL/DATA-TRANSFORMATION-REF"):      # noqa E501
            group.addComBasedSignalGroupTransformationRef(ref)


    def readISignalGroupTransformationISignalProps(self, element: ET.Element, group: ISignalGroup):
        for child_element in self.findall(element, "TRANSFORMATION-I-SIGNAL-PROPSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS":
                props = EndToEndTransformationISignalProps()
                self.readEndToEndTransformationISignalProps(child_element, props)
                group.setTransformationISignalProps(props)
            else:
                self.notImplemented("Unsupported TransformationISignalProps %s" % tag_name)


    def readISignalTriggering(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readISignalTriggering(*args, **kwargs)


    def readPhysicalChannelFrameTriggerings(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPhysicalChannelFrameTriggerings(*args, **kwargs)


    def readPhysicalChannelISignalTriggerings(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readPhysicalChannelISignalTriggerings(*args, **kwargs)


    def readFrame(self, element: ET.Element, frame: Frame):
        self.readIdentifiable(element, frame)
        frame.frameLength = self.getChildElementOptionalNumericalValue(element, "FRAME-LENGTH")
        self.readPduToFrameMappings(element, frame)


    def readFrameTriggering(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readFrameTriggering(*args, **kwargs)


    def readPduToFrameMappings(self, element: ET.Element, parent: Frame):
        for child_element in self.findall(element, "PDU-TO-FRAME-MAPPINGS/PDU-TO-FRAME-MAPPING"):
            short_name = self.getShortName(child_element)
            self.logger.debug("readPduToFrameMapping %s" % short_name)
            mapping = parent.createPduToFrameMapping(short_name)
            self.readIdentifiable(child_element, mapping)
            mapping.packingByteOrder = self.getChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER")
            mapping.pduRef = self.getChildElementOptionalRefType(child_element, "PDU-REF")
            mapping.startPosition = self.getChildElementOptionalNumericalValue(child_element, "START-POSITION")


    def readIPdu(self, element: ET.Element, pdu: IPdu):
        self.readPdu(element, pdu)


    def readIPduPort(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readIPduPort(*args, **kwargs)


    def readISignalIPdu(self, element: ET.Element, ipdu: ISignalIPdu):
        self.logger.debug("Read ISignalIPdu <%s>" % ipdu.getShortName())
        self.readIdentifiable(element, ipdu)
        ipdu.setLength(self.getChildElementOptionalNumericalValue(element, "LENGTH")) \
            .setIPduTimingSpecification(self.getISignalIPduIPduTimingSpecification(element))
        self.readISignalToPduMappings(element, ipdu)
        ipdu.setUnusedBitPattern(self.getChildElementOptionalIntegerValue(element, "UNUSED-BIT-PATTERN"))


    def readISignalIPduGroup(self, element: ET.Element, group: ISignalIPduGroup):
        self.logger.debug("Read ISignalIPduGroup <%s>" % group.getShortName())
        self.readIdentifiable(element, group)
        group.setCommunicationDirection(self.getChildElementOptionalLiteral(element, "COMMUNICATION-DIRECTION")) \
             .setCommunicationMode(self.getChildElementOptionalLiteral(element, "COMMUNICATION-MODE"))
        for ref_type in self.getChildElementRefTypeList(element, "CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS/CONTAINED-I-SIGNAL-I-PDU-GROUP-REF"):
            group.addContainedISignalIPduGroupRef(ref_type)
        for ref_type in self.getISignalIPduRefs(element):
            group.addISignalIPduRef(ref_type)


    def readISignalToIPduMapping(self, element: ET.Element, mapping: ISignalToIPduMapping):
        self.readIdentifiable(element, mapping)
        mapping.setISignalRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-REF")) \
               .setPackingByteOrder(self.getChildElementOptionalLiteral(element, "PACKING-BYTE-ORDER")) \
               .setStartPosition(self.getChildElementOptionalIntegerValue(element, "START-POSITION")) \
               .setTransferProperty(self.getChildElementOptionalLiteral(element, "TRANSFER-PROPERTY"))
        


    def readISignalToPduMappings(self, element: ET.Element, parent: ISignalIPdu):
        for child_element in self.findall(element, "I-SIGNAL-TO-PDU-MAPPINGS/I-SIGNAL-TO-I-PDU-MAPPING"):
            short_name = self.getShortName(child_element)
            mapping = parent.createISignalToPduMappings(short_name)
            self.readIdentifiable(child_element, mapping)
            mapping.setISignalRef(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-REF")) \
                   .setISignalGroupRef(self.getChildElementOptionalRefType(child_element, "I-SIGNAL-GROUP-REF")) \
                   .setPackingByteOrder(self.getChildElementOptionalLiteral(child_element, "PACKING-BYTE-ORDER")) \
                   .setStartPosition(self.getChildElementOptionalNumericalValue(child_element, "START-POSITION")) \
                   .setTransferProperty(self.getChildElementOptionalLiteral(child_element, "TRANSFER-PROPERTY")) \
                   .setUpdateIndicationBitPosition(self.getChildElementOptionalNumericalValue(child_element, "UPDATE-INDICATION-BIT-POSITION"))
    


    def readGeneralPurposeIPdu(self, element: ET.Element, i_pdu: GeneralPurposeIPdu):
        self.logger.debug("Read GeneralPurposeIPdu <%s>" % i_pdu.getShortName())
        self.readIPdu(element, i_pdu)


    def readGeneralPurposePdu(self, element: ET.Element, pdu: GeneralPurposePdu):
        self.logger.debug("Read GeneralPurposePdu <%s>" % pdu.getShortName())
        self.readPdu(element, pdu)


    def readMultiplexedIPdu(self, element: ET.Element, ipdu: MultiplexedIPdu):
        self.logger.debug("Read MultiplexedIPdu <%s>" % ipdu.getShortName())
        self.readIPdu(element, ipdu)
        self.readMultiplexedIPduDynamicParts(element, ipdu)
        ipdu.setSelectorFieldByteOrder(self.getChildElementOptionalLiteral(element, "SELECTOR-FIELD-BYTE-ORDER")) \
            .setSelectorFieldLength(self.getChildElementOptionalIntegerValue(element, "SELECTOR-FIELD-LENGTH")) \
            .setSelectorFieldStartPosition(self.getChildElementOptionalIntegerValue(element, "SELECTOR-FIELD-START-POSITION"))
        self.readMultiplexedIPduStaticParts(element, ipdu)
        ipdu.setTriggerMode(self.getChildElementOptionalLiteral(element, "TRIGGER-MODE")) \
            .setUnusedBitPattern(self.getChildElementOptionalIntegerValue(element, "UNUSED-BIT-PATTERN"))


    def readMultiplexedIPduStaticParts(self, element: ET.Element, ipdu: MultiplexedIPdu):
        for child_element in self.findall(element, "STATIC-PARTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "STATIC-PART":
                part = StaticPart()
                self.readStaticPart(child_element, part)
                ipdu.setStaticPart(part)
            else:
                self.notImplemented("Unsupported StaticPart <%s>" % tag_name)


    def readMultiplexedIPduDynamicParts(self, element: ET.Element, ipdu: MultiplexedIPdu):
        for child_element in self.findall(element, "DYNAMIC-PARTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DYNAMIC-PART":
                part = DynamicPart()
                self.readDynamicPart(child_element, part)
                ipdu.setDynamicPart(part)
            else:
                self.notImplemented("Unsupported DynamicPart <%s>" % tag_name)


    def readMultiplexedPart(self, element: ET.Element, part: MultiplexedPart):
        self.readMultiplexedPartSegmentPositions(element, part)


    def readMultiplexedPartSegmentPositions(self, element: ET.Element, part: MultiplexedPart):
        for child_element in self.findall(element, "SEGMENT-POSITIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SEGMENT-POSITION":
                position = SegmentPosition()
                self.readSegmentPosition(child_element, position)
                part.addSegmentPosition(position)
            else:
                self.notImplemented("Unsupported DynamicPart <%s>" % tag_name)


    def readUserDefinedIPdu(self, element: ET.Element, ipdu: UserDefinedIPdu):
        self.logger.debug("Read UserDefinedIPdu <%s>" % ipdu.getShortName())
        self.readIPdu(element, ipdu)
        ipdu.setCddType(self.getChildElementOptionalLiteral(element, "CDD-TYPE"))


    def readUserDefinedPdu(self, element: ET.Element, pdu: UserDefinedPdu):
        self.logger.debug("Read UserDefinedPdu <%s>" % pdu.getShortName())
        self.readPdu(element, pdu)
        pdu.setCddType(self.getChildElementOptionalLiteral(element, "CDD-TYPE"))


    def readNmPdu(self, element: ET.Element, pdu: NmPdu):
        self.logger.debug("Read NmPdu <%s>" % pdu.getShortName())
        self.readPdu(element, pdu)
        self.readNmPduISignalToIPduMappings(element, pdu)
        pdu.setUnusedBitPattern(self.getChildElementOptionalIntegerValue(element, "UNUSED-BIT-PATTERN"))


    def readDcmIPdu(self, element: ET.Element, i_pdu: DcmIPdu):
        self.logger.debug("Read DcmIPdu <%s>" % i_pdu.getShortName())
        self.readIPdu(element, i_pdu)
        i_pdu.setDiagPduType(self.getChildElementOptionalLiteral(element, "DIAG-PDU-TYPE"))


    def readSecuredIPdu(self, element: ET.Element, i_pdu: SecuredIPdu):
        self.logger.debug("Read SecuredIPdu <%s>" % i_pdu.getShortName())
        self.readIPdu(element, i_pdu)
        i_pdu.setAuthenticationPropsRef(self.getChildElementOptionalRefType(element, "AUTHENTICATION-PROPS-REF")) \
             .setFreshnessPropsRef(self.getChildElementOptionalRefType(element, "FRESHNESS-PROPS-REF")) \
             .setPayloadRef(self.getChildElementOptionalRefType(element, "PAYLOAD-REF")) \
             .setSecureCommunicationProps(self.getSecureCommunicationProps(element, "SECURE-COMMUNICATION-PROPS")) \
             .setUseAsCryptographicIPdu(self.getChildElementOptionalBooleanValue(element, "USE-AS-CRYPTOGRAPHIC-I-PDU"))


    def readSegmentPosition(self, element: ET.Element, position: SegmentPosition):
        position.setSegmentByteOrder(self.getChildElementOptionalLiteral(element, "SEGMENT-BYTE-ORDER")) \
                .setSegmentLength(self.getChildElementOptionalIntegerValue(element, "SEGMENT-LENGTH")) \
                .setSegmentPosition(self.getChildElementOptionalIntegerValue(element, "SEGMENT-POSITION"))


    def readStaticPart(self, element: ET.Element, part: StaticPart):
        self.readMultiplexedPart(element, part)
        part.setIPduRef(self.getChildElementOptionalRefType(element, "I-PDU-REF"))


    def readDynamicPart(self, element: ET.Element, part: DynamicPart):
        self.readMultiplexedPart(element, part)
        self.readDynamicPartDynamicPartAlternatives(element, part)


    def readDynamicPartAlternative(self, element: ET.Element, alternative: DynamicPartAlternative):
        alternative.setIPduRef(self.getChildElementOptionalRefType(element, "I-PDU-REF")) \
                   .setInitialDynamicPart(self.getChildElementOptionalBooleanValue(element, "INITIAL-DYNAMIC-PART")) \
                   .setSelectorFieldCode(self.getChildElementOptionalIntegerValue(element, "SELECTOR-FIELD-CODE"))


    def readNmCluster(self, element: ET.Element, cluster: NmCluster):
        self.logger.debug("read NmCluster %s" % cluster.getShortName())
        self.readIdentifiable(element, cluster)
        cluster.setCommunicationClusterRef(self.getChildElementOptionalRefType(element, "COMMUNICATION-CLUSTER-REF")) \
               .setNmChannelId(self.getChildElementOptionalNumericalValue(element, "NM-CHANNEL-ID")) \
               .setNmChannelSleepMaster(self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-SLEEP-MASTER"))
        self.readNmClusterNmNodes(element, cluster)
        cluster.setNmSynchronizingNetwork(self.getChildElementOptionalBooleanValue(element, "NM-SYNCHRONIZING-NETWORK"))


    def readNmClusterNmNodes(self, element: ET.Element, cluster: NmCluster):
        self.logger.debug("readNmConfigNmNodes %s" % cluster.getShortName())
        for child_element in self.findall(element, "NM-NODES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-NM-NODE":
                nm_node = cluster.createCanNmNode(self.getShortName(child_element))
                self.readCanNmNode(child_element, nm_node)
            elif tag_name == "UDP-NM-NODE":
                nm_node = cluster.readUdpNmNode(self.getShortName(child_element))
                self.readUdpNmNode(child_element, nm_node)
            else:
                self.notImplemented("Unsupported Nm Node <%s>" % tag_name)


    def readCanNmCluster(self, element: ET.Element, cluster: CanNmCluster):
        self.logger.debug("Read CanNmCluster <%s>" % cluster.getShortName())
        self.readNmCluster(element, cluster)
        cluster.setNmBusloadReductionActive(self.getChildElementOptionalBooleanValue(element, "NM-BUSLOAD-REDUCTION-ACTIVE")) \
               .setNmCarWakeUpRxEnabled(self.getChildElementOptionalBooleanValue(element, "NM-CAR-WAKE-UP-RX-ENABLED")) \
               .setNmCbvPosition(self.getChildElementOptionalNumericalValue(element, "NM-CBV-POSITION")) \
               .setNmChannelActive(self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-ACTIVE")) \
               .setNmImmediateNmCycleTime(self.getChildElementOptionalFloatValue(element, "NM-IMMEDIATE-NM-CYCLE-TIME")) \
               .setNmImmediateNmTransmissions(self. getChildElementOptionalNumericalValue(element, "NM-IMMEDIATE-NM-TRANSMISSIONS")) \
               .setNmMessageTimeoutTime(self.getChildElementOptionalFloatValue(element, "NM-MESSAGE-TIMEOUT-TIME")) \
               .setNmMsgCycleTime(self.getChildElementOptionalFloatValue(element, "NM-MSG-CYCLE-TIME")) \
               .setNmNetworkTimeout(self.getChildElementOptionalFloatValue(element, "NM-NETWORK-TIMEOUT")) \
               .setNmNidPosition(self. getChildElementOptionalNumericalValue(element, "NM-NID-POSITION")) \
               .setNmRemoteSleepIndicationTime(self.getChildElementOptionalFloatValue(element, "NM-REMOTE-SLEEP-INDICATION-TIME")) \
               .setNmRepeatMessageTime(self.getChildElementOptionalFloatValue(element, "NM-REPEAT-MESSAGE-TIME")) \
               .setNmUserDataLength(self. getChildElementOptionalNumericalValue(element, "NM-USER-DATA-LENGTH")) \
               .setNmWaitBusSleepTime(self.getChildElementOptionalFloatValue(element, "NM-WAIT-BUS-SLEEP-TIME"))
        


    def readUdpNmCluster(self, element: ET.Element, cluster: UdpNmCluster):
        self.logger.debug("Read UdpNmCluster %s" % cluster.getShortName())
        self.readNmCluster(element, cluster)
        cluster.setNmCbvPosition(self.getChildElementOptionalIntegerValue(element, "NM-CBV-POSITION")) \
               .setNmChannelActive(self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-ACTIVE")) \
               .setNmImmediateNmCycleTime(self.getChildElementOptionalTimeValue(element, "NM-IMMEDIATE-NM-CYCLE-TIME")) \
               .setNmImmediateNmTransmissions(self.getChildElementOptionalPositiveInteger(element, "NM-IMMEDIATE-NM-TRANSMISSIONS")) \
               .setNmMessageTimeoutTime(self.getChildElementOptionalTimeValue(element, "NM-MESSAGE-TIMEOUT-TIME")) \
               .setNmMsgCycleTime(self.getChildElementOptionalTimeValue(element, "NM-MSG-CYCLE-TIME")) \
               .setNmNetworkTimeout(self.getChildElementOptionalTimeValue(element, "NM-NETWORK-TIMEOUT")) \
               .setNmNidPosition(self.getChildElementOptionalIntegerValue(element, "NM-NID-POSITION")) \
               .setNmRemoteSleepIndicationTime(self.getChildElementOptionalTimeValue(element, "NM-REMOTE-SLEEP-INDICATION-TIME")) \
               .setNmRepeatMessageTime(self.getChildElementOptionalTimeValue(element, "NM-REPEAT-MESSAGE-TIME")) \
               .setNmWaitBusSleepTime(self.getChildElementOptionalTimeValue(element, "NM-WAIT-BUS-SLEEP-TIME")) \
               .setVlanRef(self.getChildElementOptionalRefType(element, "VLAN-REF"))
        


    def readNmConfigNmClusterCouplings(self, element: ET.Element, nm_config: NmConfig):
        for child_element in self.findall(element, "NM-CLUSTER-COUPLINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-NM-CLUSTER-COUPLING":
                nm_config.addNmClusterCouplings(self.getCanNmClusterCoupling(child_element))
            elif tag_name == "UDP-NM-CLUSTER-COUPLING":
                nm_config.addNmClusterCouplings(self.getUdpNmClusterCoupling(child_element))
            else:
                self.notImplemented("Unsupported Nm Node <%s>" % tag_name)


    def readNmConfig(self, element: ET.Element, config: NmConfig):
        self.logger.debug("Read NmConfig <%s>" % config.getShortName())
        self.readIdentifiable(element, config)
        self.readNmConfigNmClusters(element, config)
        self.readNmConfigNmClusterCouplings(element, config)
        self.readNmConfigNmIfEcus(element, config)


    def readNmConfigNmClusters(self, element: ET.Element, nm_config: NmConfig):
        for child_element in self.findall(element, "NM-CLUSTERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-NM-CLUSTER":
                cluster = nm_config.createCanNmCluster(self.getShortName(child_element))
                self.readCanNmCluster(child_element, cluster)
            elif tag_name == "UDP-NM-CLUSTER":
                cluster = nm_config.createUdpNmCluster(self.getShortName(child_element))
                self.readUdpNmCluster(child_element, cluster)
            else:
                self.raiseError("Unsupported Nm Cluster <%s>" % tag_name)


    def readNmConfigNmIfEcus(self, element: ET.Element, nm_config: NmConfig):
        for child_element in self.findall(element, "NM-IF-ECUS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "NM-ECU":
                ecu = nm_config.createNmEcu(self.getShortName(child_element))
                self.readNmEcu(child_element, ecu)
            else:
                self.notImplemented("Unsupported NmIfEcus <%s>" % tag_name)
    


    def readBusDependentNmEcus(self, element: ET.Element, nm_ecu: NmEcu):
        for child_element in self.findall(element, "BUS-DEPENDENT-NM-ECUS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "UDP-NM-ECU":
                udp_nm_ecu = UdpNmEcu()
                self.readUdpNmEcu(child_element, udp_nm_ecu)
                nm_ecu.addBusDependentNmEcu(udp_nm_ecu)
            else:
                self.notImplemented("Unsupported BusDependentNmEcu <%s>" % tag_name)


    def readNmEcu(self, element: ET.Element, nm_ecu: NmEcu):
        self.readIdentifiable(element, nm_ecu)
        self.readBusDependentNmEcus(element, nm_ecu)
        nm_ecu.setEcuInstanceRef(self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF")) \
              .setNmBusSynchronizationEnabled(self.getChildElementOptionalBooleanValue(element, "NM-BUS-SYNCHRONIZATION-ENABLED")) \
              .setNmComControlEnabled(self.getChildElementOptionalBooleanValue(element, "NM-COM-CONTROL-ENABLED")) \
              .setNmNodeDetectionEnabled(self.getChildElementOptionalBooleanValue(element, "NM-NODE-DETECTION-ENABLED")) \
              .setNmNodeIdEnabled(self.getChildElementOptionalBooleanValue(element, "NM-NODE-ID-ENABLED")) \
              .setNmPduRxIndicationEnabled(self.getChildElementOptionalBooleanValue(element, "NM-PDU-RX-INDICATION-ENABLED")) \
              .setNmRemoteSleepIndEnabled(self.getChildElementOptionalBooleanValue(element, "NM-REMOTE-SLEEP-IND-ENABLED")) \
              .setNmRepeatMsgIndEnabled(self.getChildElementOptionalBooleanValue(element, "NM-REPEAT-MSG-IND-ENABLED")) \
              .setNmStateChangeIndEnabled(self.getChildElementOptionalBooleanValue(element, "NM-STATE-CHANGE-IND-ENABLED")) \
              .setNmUserDataEnabled(self.getChildElementOptionalBooleanValue(element, "NM-USER-DATA-ENABLED"))


    def readCanNmNode(self, element: ET.Element, nm_node: CanNmNode):
        self.logger.debug("Read CanNmNode <%s>" % nm_node.getShortName())
        self.readNmNode(element, nm_node)
        nm_node.setNmCarWakeUpRxEnabled(self.getChildElementOptionalBooleanValue(element, "NM-CAR-WAKE-UP-RX-ENABLED")) \
               .setNmMsgCycleOffset(self.getChildElementOptionalFloatValue(element, "NM-MSG-CYCLE-OFFSET")) \
               .setNmMsgReducedTime(self.getChildElementOptionalFloatValue(element, "NM-MSG-REDUCED-TIME")) \
               .setNmRangeConfig(self.getChildElementRxIdentifierRange(element, "NM-RANGE-CONFIG"))
        


    def readUdpNmEcu(self, element: ET.Element, ecu: UdpNmEcu):
        ecu.setNmSynchronizationPointEnabled(self.getChildElementOptionalBooleanValue(element, "NM-SYNCHRONIZATION-POINT-ENABLED"))


    def readNmNode(self, element: ET.Element, nm_node: NmNode):
        self.readIdentifiable(element, nm_node)

        nm_node.setControllerRef(self.getChildElementOptionalRefType(element, "CONTROLLER-REF")) \
               .setNmIfEcuRef(self.getChildElementOptionalRefType(element, "NM-IF-ECU-REF")) \
               .setNmPassiveModeEnabled(self.getChildElementOptionalBooleanValue(element, "NM-PASSIVE-MODE-ENABLED")) \
               .setNmNodeId(self.getChildElementOptionalNumericalValue(element, "NM-NODE-ID"))
        for ref in self.getChildElementRefTypeList(element, "RX-NM-PDU-REFS/RX-NM-PDU-REF"):
            nm_node.addRxNmPduRef(ref)
        for ref in self.getChildElementRefTypeList(element, "TX-NM-PDU-REFS/TX-NM-PDU-REF"):
            nm_node.addTxNmPduRefs(ref)


    def readUdpNmNode(self, element: ET.Element, nm_node: UdpNmNode):
        self.logger.debug("Read UdpNmNode <%s>" % nm_node.getShortName())
        self.readNmNode(element, nm_node)
        nm_node.setNmMsgCycleOffset(self.getChildElementOptionalTimeValue(element, "NM-MSG-CYCLE-OFFSET"))


    def readTpConfig(self, element: ET.Element, config: TpConfig):
        self.readIdentifiable(element, config)
        config.setCommunicationClusterRef(self.getChildElementOptionalRefType(element, "COMMUNICATION-CLUSTER-REF"))


    def readTpConnection(self, element: ET.Element, connection: TpConnection):
        self.readARObjectAttributes(element, connection)
        child_element = self.find(element, "IDENT")
        if child_element is not None:
            ident = connection.createTpConnectionIdent(self.getShortName(child_element))
            self.readReferrable(child_element, ident)


    def readCanTpConfig(self, element: ET.Element, config: CanTpConfig):
        self.logger.debug("Read CanTpConfig <%s>" % config.getShortName())
        self.readTpConfig(element, config)
        self.readCanTpConfigTpAddresses(element, config)
        self.readCanTpConfigTpChannels(element, config)
        self.readCanTpConfigTpConnections(element, config)
        self.readCanTpConfigTpEcus(element, config)
        self.readCanTpConfigTpNodes(element, config)


    def readCanTpAddress(self, element: ET.Element, address: CanTpAddress):
        self.readIdentifiable(element, address)
        address.setTpAddress(self.getChildElementOptionalIntegerValue(element, "TP-ADDRESS")) \
               .setTpAddressExtensionValue(self.getChildElementOptionalIntegerValue(element, "TP-ADDRESS-EXTENSION-VALUE"))


    def readCanTpConfigTpAddresses(self, element: ET.Element, config: CanTpConfig):
        for child_element in self.findall(element, "TP-ADDRESSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-TP-ADDRESS":
                address = config.createCanTpAddress(self.getShortName(child_element))
                self.readCanTpAddress(child_element, address)
            else:
                self.notImplemented("Unsupported TpAddress <%s>" % tag_name)


    def readCanTpChannel(self, element: ET.Element, channel: CanTpChannel):
        self.readIdentifiable(element, channel)
        channel.setChannelId(self.getChildElementOptionalPositiveInteger(element, "CHANNEL-ID")) \
               .setChannelMode(self.getChildElementOptionalLiteral(element, "CHANNEL-MODE"))


    def readCanTpConfigTpChannels(self, element: ET.Element, config: CanTpConfig):
        for child_element in self.findall(element, "TP-CHANNELS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-TP-CHANNEL":
                channel = config.createCanTpChannel(self.getShortName(child_element))
                self.readCanTpChannel(child_element, channel)
            else:
                self.notImplemented("Unsupported TpChannel <%s>" % tag_name)


    def readCanTpConnection(self, element: ET.Element, connection: CanTpConnection):
        self.readTpConnection(element, connection)
        connection.setAddressingFormat(self.getChildElementOptionalLiteral(element, "ADDRESSING-FORMAT")) \
                  .setCanTpChannelRef(self.getChildElementOptionalRefType(element, "CAN-TP-CHANNEL-REF")) \
                  .setCancellation(self.getChildElementOptionalBooleanValue(element, "CANCELLATION")) \
                  .setDataPduRef(self.getChildElementOptionalRefType(element, "DATA-PDU-REF")) \
                  .setFlowControlPduRef(self.getChildElementOptionalRefType(element, "FLOW-CONTROL-PDU-REF")) \
                  .setMaxBlockSize(self.getChildElementOptionalIntegerValue(element, "MAX-BLOCK-SIZE")) \
                  .setMulticastRef(self.getChildElementOptionalRefType(element, "MULTICAST-REF")) \
                  .setPaddingActivation(self.getChildElementOptionalBooleanValue(element, "PADDING-ACTIVATION"))
        self.readTpConnectionReceiverRefs(element, connection)
        connection.setTaType(self.getChildElementOptionalLiteral(element, "TA-TYPE")) \
                  .setTimeoutBr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-BR")) \
                  .setTimeoutBs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-BS")) \
                  .setTimeoutCr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CR")) \
                  .setTimeoutCs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CS")) \
                  .setTpSduRef(self.getChildElementOptionalRefType(element, "TP-SDU-REF")) \
                  .setTransmitterRef(self.getChildElementOptionalRefType(element, "TRANSMITTER-REF"))


    def readTpConnectionReceiverRefs(self, element: ET.Element, connection: CanTpConnection):
        for ref in self.getChildElementRefTypeList(element, "RECEIVER-REFS/RECEIVER-REF"):
            connection.addReceiverRef(ref)


    def readCanTpConfigTpConnections(self, element: ET.Element, config: CanTpConfig):
        for child_element in self.findall(element, "TP-CONNECTIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-TP-CONNECTION":
                connection = CanTpConnection()
                self.readCanTpConnection(child_element, connection)
                config.addTpConnection(connection)
            else:
                self.notImplemented("Unsupported TpConnection <%s>" % tag_name)


    def readCanTpEcu(self, element: ET.Element, tp_ecu: CanTpEcu):
        tp_ecu.setCycleTimeMainFunction(self.getChildElementOptionalTimeValue(element, "CYCLE-TIME-MAIN-FUNCTION")) \
              .setEcuInstanceRef(self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF"))


    def readCanTpConfigTpEcus(self, element: ET.Element, config: CanTpConfig):
        for child_element in self.findall(element, "TP-ECUS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-TP-ECU":
                tp_ecu = CanTpEcu()
                self.readCanTpEcu(child_element, tp_ecu)
                config.addTpEcu(tp_ecu)
            else:
                self.notImplemented("Unsupported TpEcu <%s>" % tag_name)


    def readCanTpNode(self, element: ET.Element, tp_node: CanTpNode):
        self.readIdentifiable(element, tp_node)
        tp_node.setConnectorRef(self.getChildElementOptionalRefType(element, "CONNECTOR-REF")) \
               .setMaxFcWait(self.getChildElementOptionalIntegerValue(element, "MAX-FC-WAIT")) \
               .setStMin(self.getChildElementOptionalTimeValue(element, "ST-MIN")) \
               .setTimeoutAr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-AR")) \
               .setTimeoutAs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-AS")) \
               .setTpAddressRef(self.getChildElementOptionalRefType(element, "TP-ADDRESS-REF"))


    def readLinTpConfig(self, element: ET.Element, config: LinTpConfig):
        self.logger.debug("Read LinTpConfig <%s>" % config.getShortName())
        self.readTpConfig(element, config)
        self.readLinTpConfigTpAddresses(element, config)
        self.readLinTpConfigTpConnections(element, config)
        self.readLinTpConfigTpNodes(element, config)


    def readLinTpConnection(self, element: ET.Element, connection: LinTpConnection):
        self.readTpConnection(element, connection)
        connection.setDataPduRef(self.getChildElementOptionalRefType(element, "DATA-PDU-REF")) \
                  .setFlowControlRef(self.getChildElementOptionalRefType(element, "FLOW-CONTROL-REF")) \
                  .setLinTpNSduRef(self.getChildElementOptionalRefType(element, "LIN-TP-N-SDU-REF"))
        self.readTpConnectionReceiverRefs(element, connection)
        connection.setTimeoutAs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-AS")) \
                  .setTimeoutCr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CR")) \
                  .setTimeoutCs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CS")) \
                  .setTransmitterRef(self.getChildElementOptionalRefType(element, "TRANSMITTER-REF"))


    def readLinTpNode(self, element: ET.Element, tp_node: LinTpNode):
        self.readIdentifiable(element, tp_node)
        tp_node.setConnectorRef(self.getChildElementOptionalRefType(element, "CONNECTOR-REF")) \
               .setDropNotRequestedNad(self.getChildElementOptionalBooleanValue(element, "DROP-NOT-REQUESTED-NAD")) \
               .setP2Max(self.getChildElementOptionalTimeValue(element, "P-2-MAX")) \
               .setP2Timing(self.getChildElementOptionalTimeValue(element, "P-2-TIMING")) \
               .setTpAddressRef(self.getChildElementOptionalRefType(element, "TP-ADDRESS-REF"))


    def readDoIpTpConfig(self, element: ET.Element, config: DoIpTpConfig):
        self.logger.debug("Read DoIpTpConfig <%s>" % config.getShortName())
        self.readTpConfig(element, config)
        self.readDoIpTpConfigDoIpLogicAddresses(element, config)
        self.readDoIpTpConfigTpConnections(element, config)


    def readDoIpLogicAddress(self, element: ET.Element, address: DoIpLogicAddress):
        self.readIdentifiable(element, address)
        address.setAddress(self.getChildElementOptionalIntegerValue(element, "ADDRESS"))


    def readDoIpTpConfigDoIpLogicAddresses(self, element: ET.Element, config: DoIpTpConfig):
        for child_element in self.findall(element, "DO-IP-LOGIC-ADDRESSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DO-IP-LOGIC-ADDRESS":
                address = config.createDoIpLogicAddress(self.getShortName(child_element))
                self.readDoIpLogicAddress(child_element, address)
            else:
                self.notImplemented("Unsupported DoIpLogicAddress <%s>" % tag_name)


    def readDoIpTpConnection(self, element: ET.Element, connection: DoIpTpConnection):
        self.readTpConnection(element, connection)
        connection.setDoIpSourceAddressRef(self.getChildElementOptionalRefType(element, "DO-IP-SOURCE-ADDRESS-REF")) \
                  .setDoIpTargetAddressRef(self.getChildElementOptionalRefType(element, "DO-IP-TARGET-ADDRESS-REF")) \
                  .setTpSduRef(self.getChildElementOptionalRefType(element, "TP-SDU-REF"))


    def readDoIpTpConfigTpConnections(self, element: ET.Element, config: DoIpTpConfig):
        for child_element in self.findall(element, "TP-CONNECTIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DO-IP-TP-CONNECTION":
                connection = DoIpTpConnection()
                self.readDoIpTpConnection(child_element, connection)
                config.addTpConnection(connection)
            else:
                self.notImplemented("Unsupported TpConnection <%s>" % tag_name)


    def readSecureCommunicationPropsSet(self, element: ET.Element, props_set: SecureCommunicationPropsSet):
        self.logger.debug("Read SecureCommunicationPropsSet <%s>" % props_set.getShortName())
        self.readIdentifiable(element, props_set)
        self.readSecureCommunicationPropsSetAuthenticationProps(element, props_set)
        self.readSecureCommunicationPropsSetFreshnessProps(element, props_set)
    


    def readSecureCommunicationPropsSetAuthenticationProps(self, element: ET.Element, props_set: SecureCommunicationPropsSet):
        for child_element in self.findall(element, "AUTHENTICATION-PROPSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SECURE-COMMUNICATION-AUTHENTICATION-PROPS":
                props = props_set.createSecureCommunicationAuthenticationProps(self.getShortName(child_element))
                self.readSecureCommunicationAuthenticationProps(child_element, props)
            else:
                self.notImplemented("Unsupported AuthenticationProps <%s>" % tag_name)


    def readSecureCommunicationAuthenticationProps(self, element: ET.Element, props: SecureCommunicationAuthenticationProps):
        self.readIdentifiable(element, props)
        props.setAuthAlgorithm(self.getChildElementOptionalLiteral(element, "AUTH-ALGORITHM")) \
             .setAuthInfoTxLength(self.getChildElementOptionalPositiveInteger(element, "AUTH-INFO-TX-LENGTH"))


    def readSecureCommunicationPropsSetFreshnessProps(self, element: ET.Element, props_set: SecureCommunicationPropsSet):
        for child_element in self.findall(element, "FRESHNESS-PROPSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SECURE-COMMUNICATION-FRESHNESS-PROPS":
                props = props_set.createSecureCommunicationFreshnessProps(self.getShortName(child_element))
                self.readSecureCommunicationFreshnessProps(child_element, props)
            else:
                self.notImplemented("Unsupported FreshnessProps <%s>" % tag_name)


    def readSecureCommunicationFreshnessProps(self, element: ET.Element, props: SecureCommunicationFreshnessProps):
        self.readIdentifiable(element, props)
        props.setFreshnessValueLength(self.getChildElementOptionalLiteral(element, "FRESHNESS-VALUE-LENGTH")) \
             .setFreshnessValueTxLength(self.getChildElementOptionalPositiveInteger(element, "FRESHNESS-VALUE-TX-LENGTH"))


    def readDataTransformationSet(self, element: ET.Element, dtf_set: DataTransformationSet):
        self.logger.debug("Read DataTransformationSet <%s>" % dtf_set.getShortName())
        self.readARElement(element, dtf_set)
        self.readDataTransformationSetDataTransformations(element, dtf_set)
        self.readDataTransformationSetTransformationTechnologies(element, dtf_set)


    def readDataTransformationSetDataTransformations(self, element: ET.Element, dtf_set: DataTransformationSet):
        for child_element in self.findall(element, "DATA-TRANSFORMATIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "DATA-TRANSFORMATION":
                dtf = dtf_set.createDataTransformation(self.getShortName(child_element))
                self.readDataTransformation(child_element, dtf)
            else:
                self.notImplemented("Unsupported DataTransformation <%s>" % tag_name)


    def readDataTransformationSetTransformationTechnologies(self, element: ET.Element, dtf_set: DataTransformationSet):
        for child_element in self.findall(element, "TRANSFORMATION-TECHNOLOGYS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "TRANSFORMATION-TECHNOLOGY":
                tech = dtf_set.createTransformationTechnology(self.getShortName(child_element))
                self.readTransformationTechnology(child_element, tech)
            else:
                self.notImplemented("Unsupported TransformationTechnology <%s>" % tag_name)


    def readDataTransformation(self, element: ET.Element, dtf: DataTransformation):
        self.readIdentifiable(element, dtf)
        dtf.setExecuteDespiteDataUnavailability(self.getChildElementOptionalBooleanValue(element, "EXECUTE-DESPITE-DATA-UNAVAILABILITY"))
        self.readDataTransformationTransformerChainRefs(element, dtf)


    def readTransformationISignalProps(self, element: ET.Element, props: TransformationISignalProps):
        self.readDescribable(element, props)


    def readEndToEndTransformationISignalProps(self, element: ET.Element, props: EndToEndTransformationISignalProps):
        child_element = self.find(element, "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS/END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL")
        if child_element is not None:
            self.readTransformationISignalProps(child_element, props)
            props.setTransformerRef(self.getChildElementOptionalRefType(child_element, "TRANSFORMER-REF"))
            self.readEndToEndTransformationISignalPropsDataIds(child_element, props)
            props.setDataLength(self.getChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH"))


    def readTransformationDescription(self, element: ET.Element, desc: TransformationDescription):
        self.readDescribable(element, desc)
    


    def readEndToEndTransformationDescription(self, element: ET.Element, desc: EndToEndTransformationDescription):
        self.readTransformationDescription(element, desc)
        desc.setDataIdMode(self.getChildElementOptionalLiteral(element, "DATA-ID-MODE")) \
            .setMaxDeltaCounter(self.getChildElementOptionalPositiveInteger(element, "MAX-DELTA-COUNTER")) \
            .setMaxErrorStateInit(self.getChildElementOptionalPositiveInteger(element, "MAX-ERROR-STATE-INIT")) \
            .setMaxErrorStateInvalid(self.getChildElementOptionalPositiveInteger(element, "MAX-ERROR-STATE-INVALID")) \
            .setMaxErrorStateValid(self.getChildElementOptionalPositiveInteger(element, "MAX-ERROR-STATE-VALID")) \
            .setMaxNoNewOrRepeatedData(self.getChildElementOptionalPositiveInteger(element, "MAX-NO-NEW-OR-REPEATED-DATA")) \
            .setMinOkStateInit(self.getChildElementOptionalPositiveInteger(element, "MIN-OK-STATE-INIT")) \
            .setMinOkStateInvalid(self.getChildElementOptionalPositiveInteger(element, "MIN-OK-STATE-INVALID")) \
            .setMinOkStateValid(self.getChildElementOptionalPositiveInteger(element, "MIN-OK-STATE-VALID")) \
            .setProfileBehavior(self.getChildElementOptionalLiteral(element, "PROFILE-BEHAVIOR")) \
            .setProfileName(self.getChildElementOptionalLiteral(element, "PROFILE-NAME")) \
            .setSyncCounterInit(self.getChildElementOptionalPositiveInteger(element, "SYNC-COUNTER-INIT")) \
            .setUpperHeaderBitsToShift(self.getChildElementOptionalPositiveInteger(element, "UPPER-HEADER-BITS-TO-SHIFT")) \
            .setWindowSizeInit(self.getChildElementOptionalPositiveInteger(element, "WINDOW-SIZE-INIT")) \
            .setWindowSizeInvalid(self.getChildElementOptionalPositiveInteger(element, "WINDOW-SIZE-INVALID")) \
            .setWindowSizeValid(self.getChildElementOptionalPositiveInteger(element, "WINDOW-SIZE-VALID"))


    def readTransformationTechnology(self, element: ET.Element, tech: TransformationTechnology):
        self.readIdentifiable(element, tech)
        tech.setBufferProperties(self.getBufferProperties(element, "BUFFER-PROPERTIES")) \
            .setNeedsOriginalData(self.getChildElementOptionalBooleanValue(element, "NEEDS-ORIGINAL-DATA")) \
            .setProtocol(self.getChildElementOptionalLiteral(element, "PROTOCOL"))
        self.readTransformationTechnologyTransformationDescriptions(element, tech)
        tech.setTransformerClass(self.getChildElementOptionalLiteral(element, "TRANSFORMER-CLASS")) \
            .setVersion(self.getChildElementOptionalLiteral(element, "VERSION"))


    def readSenderReceiverToSignalMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSenderReceiverToSignalMapping(*args, **kwargs)


    def readSenderReceiverToSignalGroupMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSenderReceiverToSignalGroupMapping(*args, **kwargs)


    def readSenderReceiverToSignalGroupMappingTypeMapping(self, *args, **kwargs):
        """Delegate to PortInterfaceParser."""
        return self._port_interface_parser.readSenderReceiverToSignalGroupMappingTypeMapping(*args, **kwargs)


    def readNetworkEndPoint(self, element: ET.Element, end_point: NetworkEndpoint):
        self.readIdentifiable(element, end_point)
        end_point.setInfrastructureServices(self.getInfrastructureServices(element, "INFRASTRUCTURE-SERVICES"))
        self.readNetworkEndPointNetworkEndPointAddress(element, end_point)
        end_point.setPriority(self.getChildElementOptionalPositiveInteger(element, "PRIORITY"))


    def readNetworkEndPointNetworkEndPointAddress(self, element: ET.Element, end_point: NetworkEndpoint):
        for child_element in self.findall(element, "NETWORK-ENDPOINT-ADDRESSES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "IPV-6-CONFIGURATION":
                end_point.addNetworkEndpointAddress(self.getIpv6Configuration(child_element))
            else:
                self.notImplemented("Unsupported Network EndPoint Address <%s>" % tag_name)


    def readSocketAddress(self, element: ET.Element, address: SocketAddress):
        self.readIdentifiable(element, address)
        self.readSocketAddressApplicationEndpoint(element, address)
        self.readSocketAddressMulticastConnectorRefs(element, address)
        address.setConnectorRef(self.getChildElementOptionalRefType(element, "CONNECTOR-REF")) \
               .setPortAddress(self.getChildElementOptionalPositiveInteger(element, "PORT-ADDRESS"))


    def readSocketAddressApplicationEndpoint(self, element: ET.Element, address: SocketAddress):
        child_element = self.find(element, "APPLICATION-ENDPOINT")
        if child_element is not None:
            end_point = address.createApplicationEndpoint(self.getShortName(child_element))
            self.readSocketAddressApplicationEndpointConsumedServiceInstances(child_element, end_point)
            end_point.setNetworkEndpointRef(self.getChildElementOptionalRefType(child_element, "NETWORK-ENDPOINT-REF")) \
                     .setPriority(self.getChildElementOptionalPositiveInteger(child_element, "PRIORITY"))
            self.readSocketAddressApplicationEndpointProvidedServiceInstance(child_element, end_point)
            end_point.setTpConfiguration(self.getTransportProtocolConfiguration(child_element, "TP-CONFIGURATION"))
            


    def readSocketAddressApplicationEndpointProvidedServiceInstance(self, element: ET.Element, end_point: ApplicationEndpoint):
        for child_element in self.findall(element, "PROVIDED-SERVICE-INSTANCES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "PROVIDED-SERVICE-INSTANCE":
                instance = end_point.createProvidedServiceInstance(self.getShortName(child_element))
                self.readProvidedServiceInstance(child_element, instance)
            else:
                self.notImplemented("Unsupported ConsumedServiceInstances <%s>" % tag_name)


    def readSocketAddressApplicationEndpointConsumedServiceInstances(self, element: ET.Element, end_point: ApplicationEndpoint):
        for child_element in self.findall(element, "CONSUMED-SERVICE-INSTANCES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CONSUMED-SERVICE-INSTANCE":
                instance = end_point.createConsumedServiceInstance(self.getShortName(child_element))
                self.readConsumedServiceInstance(child_element, instance)
            else:
                self.notImplemented("Unsupported ConsumedServiceInstances <%s>" % tag_name)


    def readProvidedServiceInstance(self, element: ET.Element, instance: ProvidedServiceInstance):
        self.readIdentifiable(element, instance)
        self.readProvidedServiceInstanceEventHandlers(element, instance)
        instance.setInstanceIdentifier(self.getChildElementOptionalPositiveInteger(element, "INSTANCE-IDENTIFIER")) \
                .setSdServerConfig(self.getSdServerConfig(element, "SD-SERVER-CONFIG")) \
                .setServiceIdentifier(self.getChildElementOptionalPositiveInteger(element, "SERVICE-IDENTIFIER"))


    def readProvidedServiceInstanceEventHandlers(self, element: ET.Element, instance: ProvidedServiceInstance):
        for child_element in self.findall(element, "EVENT-HANDLERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "EVENT-HANDLER":
                handler = instance.createEventHandler(self.getShortName(child_element))
                self.readEventHandler(child_element, handler)
            else:
                self.notImplemented("Unsupported Event Handler <%s>" % tag_name)


    def readConsumedServiceInstance(self, element: ET.Element, instance: ConsumedServiceInstance):
        self.readIdentifiable(element, instance)
        self.readConsumedServiceInstanceConsumedEventGroups(element, instance)
        instance.setProvidedServiceInstanceRef(self.getChildElementOptionalRefType(element, "PROVIDED-SERVICE-INSTANCE-REF"))
        instance.setSdClientConfig(self.getSdClientConfig(element, "SD-CLIENT-CONFIG"))
    


    def readConsumedServiceInstanceConsumedEventGroups(self, element: ET.Element, instance: ConsumedServiceInstance):
        for child_element in self.findall(element, "CONSUMED-EVENT-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CONSUMED-EVENT-GROUP":
                group = instance.createConsumedEventGroup(self.getShortName(child_element))
                self.readConsumedEventGroup(child_element, group)
            else:
                self.notImplemented("Unsupported ConsumedEventGroups <%s>" % tag_name)


    def readEventHandler(self, element: ET.Element, handler: EventHandler):
        self.readIdentifiable(element, handler)
        handler.setApplicationEndpointRef(self.getChildElementOptionalRefType(element, "APPLICATION-ENDPOINT-REF"))
        for ref in self.getChildElementRefTypeList(element, "CONSUMED-EVENT-GROUP-REFS/CONSUMED-EVENT-GROUP-REF"):
            handler.addConsumedEventGroupRef(ref)
        handler.setMulticastThreshold(self.getChildElementOptionalPositiveInteger(element, "MULTICAST-THRESHOLD"))
        for ref in self.getChildElementRefTypeList(element, "ROUTING-GROUP-REFS/ROUTING-GROUP-REF"):
            handler.addRoutingGroupRef(ref)
        handler.setSdServerConfig(self.getSdServerConfig(element, "SD-SERVER-CONFIG"))


    def readSoAdConfigSocketAddresses(self, element: ET.Element, config: SoAdConfig):
        for child_element in self.findall(element, "SOCKET-ADDRESSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SOCKET-ADDRESS":
                address = config.createSocketAddress(self.getShortName(child_element))
                self.readSocketAddress(child_element, address)
            else:
                self.notImplemented("Unsupported Socket Address <%s>" % tag_name)


    def readSoAdConfigConnectionBundles(self, element: ET.Element, config: SoAdConfig):
        for child_element in self.findall(element, "CONNECTION-BUNDLES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SOCKET-CONNECTION-BUNDLE":
                bundle = config.createSocketConnectionBundle(self.getShortName(child_element))
                self.readSocketConnectionBundle(child_element, bundle)
            else:
                self.notImplemented("Unsupported Connection Bundle <%s>" % tag_name)


    def readSocketConnectionBundle(self, element: ET.Element, bundle: SocketConnectionBundle):
        self.readSocketConnectionBundleConnections(element, bundle)
        bundle.setServerPortRef(self.getChildElementOptionalRefType(element, "SERVER-PORT-REF"))


    def readSocketConnectionBundleConnections(self, element: ET.Element, bundle: SocketConnectionBundle):
        for child_element in self.findall(element, "BUNDLED-CONNECTIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "SOCKET-CONNECTION":
                bundle.addBundledConnection(self.getSocketConnection(child_element))
            else:
                self.notImplemented("Unsupported Bundled Connection <%s>" % tag_name)


    def readSoAdRoutingGroup(self, element: ET.Element, group: SoAdRoutingGroup):
        self.logger.debug("Read SoAdRoutingGroup <%s>" % group.getShortName())
        self.readIdentifiable(element, group)
        group.setEventGroupControlType(self.getChildElementOptionalLiteral(element, "EVENT-GROUP-CONTROL-TYPE"))


    def readHwElement(self, element: ET.Element, hw_element: HwElement):
        self.logger.debug("Read HwElement <%s>" % hw_element.getShortName())
        self.readHwDescriptionEntity(element, hw_element)
        self.readHwElementHwPinGroups(element, hw_element)


    def readHwElementHwPinGroups(self, element: ET.Element, hw_element: HwElement):
        for child_element in self.findall(element, "HW-PIN-GROUPS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "HW-PIN-GROUP":
                pin_group = hw_element.createHwPinGroup(self.getShortName(child_element))
                self.readHwPinGroup(child_element, pin_group)
            else:
                self.notImplemented("Unsupported Hw Pin Group <%s>" % tag_name)


    def readHwPinGroup(self, element: ET.SubElement, pin_group: HwPinGroup):
        self.readHwDescriptionEntity(element, pin_group)


    def readHwCategory(self, element: ET.Element, hw_category: HwCategory):
        self.logger.debug("Read HwCategory <%s>" % hw_category.getShortName())
        self.readARElement(element, hw_category)
        self.readHwCategoryHwAttributeDef(element, hw_category)


    def readHwCategoryHwAttributeDef(self, element: ET.Element, hw_category: HwCategory):
        for child_element in self.findall(element, "HW-ATTRIBUTE-DEFS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "HW-ATTRIBUTE-DEF":
                pin_group = hw_category.createHwAttributeDef(self.getShortName(child_element))
                self.readHwAttributeDef(child_element, pin_group)
            else:
                self.notImplemented("Unsupported Hw Attribute Defs <%s>" % tag_name)


    def readHwAttributeDef(self, element: ET.Element, attribute_def: HwAttributeDef):
        self.readIdentifiable(element, attribute_def)
        attribute_def.setUnitRef(self.getChildElementOptionalRefType(element, "UNIT-REF"))


    def readHwType(self, element: ET.Element, type: HwType):
        self.logger.debug("Read HwType <%s>" % type.getShortName())
        self.readARElement(element, type)


    def readHwDescriptionEntity(self, element: ET.Element, entity: HwDescriptionEntity):
        self.readARElement(element, entity)
        self.readHwDescriptionEntityHwCategoryRefs(element, entity)


    def readHwDescriptionEntityHwCategoryRefs(self, element: ET.Element, entity: HwDescriptionEntity):
        for ref in self.getChildElementRefTypeList(element, "HW-CATEGORY-REFS/HW-CATEGORY-REF"):
            entity.addHwCategoryRef(ref)


    def readDiagnosticConnection(self, element: ET.Element, connection: DiagnosticConnection):
        self.logger.debug("Read DiagnosticConnection <%s>" % connection.getShortName())
        self.readIdentifiable(element, connection)
        self.readDiagnosticConnectionFunctionalRequestRefs(element, connection)
        connection.setPhysicalRequestRef(self.getChildElementOptionalRefType(element, "PHYSICAL-REQUEST-REF")) \
                  .setResponseOnEventRef(self.getChildElementOptionalRefType(element, "RESPONSE-REF"))
        


    def readDiagnosticConnectionFunctionalRequestRefs(self, element: ET.Element, connection: DiagnosticConnection):
        for ref in self.getChildElementRefTypeList(element, "FUNCTIONAL-REQUEST-REFS/FUNCTIONAL-REQUEST-REF"):
            connection.addFunctionalRequestRef(ref)


    def readDiagnosticServiceTable(self, element: ET.Element, table: DiagnosticServiceTable):
        self.logger.debug("Read DiagnosticServiceTable <%s>" % table.getShortName())
        self.readIdentifiable(element, table)
        self.readDiagnosticServiceTableDiagnosticConnectionRefs(element, table)
        table.setEcuInstanceRef(self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF"))


    def readDiagnosticServiceTableDiagnosticConnectionRefs(self, element: ET.Element, table: DiagnosticServiceTable):
        for ref in self.getChildElementRefTypeList(element, "DIAGNOSTIC-CONNECTIONS/DIAGNOSTIC-CONNECTION-REF-CONDITIONAL/DIAGNOSTIC-CONNECTION-REF"):
            table.addDiagnosticConnectionRef(ref)
        


    def readCommunicationCycle(self, element: ET.Element, cycle: CommunicationCycle):
        self.readARObjectAttributes(element, cycle)
        


    def readCycleRepetition(self, element: ET.Element, cycle: CycleRepetition):
        self.readCommunicationCycle(element, cycle)
        cycle.setBaseCycle(self.getChildElementOptionalIntegerValue(element, "BASE-CYCLE")) \
             .setCycleRepetition(self.getChildElementOptionalLiteral(element, "CYCLE-REPETITION"))
        


    def readGateway(self, element: ET.Element, gateway: Gateway):
        self.logger.debug("Read Gateway <%s>" % gateway.getShortName())
        self.readIdentifiable(element, gateway)
        gateway.setEcuRef(self.getChildElementOptionalRefType(element, "ECU-REF"))
        for mapping in self.getIPduMappings(element):
            gateway.addIPduMapping(mapping)
        for mapping in self.getISignalMappings(element):
            gateway.addSignalMapping(mapping)


    def getFrameMappings(self, element: ET.Element) -> List[FrameMapping]:
        mappings = []
        for child_element in self.findall(element, 'FRAME-MAPPINGS/'):
            mapping = FrameMapping()
            mapping.sourceFrameRef = self.getChildElementOptionalRefType(child_element, "SOURCE-FRAME-REF")
            mapping.targetFrameRef = self.getChildElementOptionalRefType(child_element, "TARGET-FRAME-REF")
            mappings.append(mapping)
        return mappings


    def getISignalMappings(self, element: ET.Element) -> List[ISignalMapping]:
        mappings = []
        for child_element in self.findall(element, "SIGNAL-MAPPINGS/I-SIGNAL-MAPPING"):
            mapping = ISignalMapping()
            mapping.sourceSignalRef = self.getChildElementOptionalRefType(child_element, "SOURCE-SIGNAL-REF")
            mapping.targetSignalRef = self.getChildElementOptionalRefType(child_element, "TARGET-SIGNAL-REF")
            mappings.append(mapping)
        return mappings
    


    def getTargetIPduRef(self, element, key: str) -> TargetIPduRef:
        i_pdu_ref = None
        child_element = self.find(element, key)
        if child_element is not None:
            i_pdu_ref = TargetIPduRef()
            i_pdu_ref.setTargetIPdu(self.getChildElementOptionalRefType(child_element, "TARGET-I-PDU-REF"))
        return i_pdu_ref
    


