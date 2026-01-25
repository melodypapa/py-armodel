"""
Parser for AUTOSAR network management elements.

Handles:
- NM-CONFIG
- NM-NODE
- NM-CLUSTER
- CAN-NM-MODE
- UDP-NM-CLUSTER
- EndToEndProtection (EndToEndProtectionSet, EndToEndProtection)
- Transport Protocols (GenericTP, TCP-TP, UDP-TP, CAN-TP, LIN-TP, DO-IP-TP)
"""
import xml.etree.ElementTree as ET

from ..base_arxml_parser import BaseARXMLParser
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import (
    EndToEndDescription,
    EndToEndProtection,
    EndToEndProtectionISignalIPdu,
    EndToEndProtectionSet,
    EndToEndProtectionVariablePrototype,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ISignalToIPduMapping,
    NmPdu,
    Pdu,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    RxIdentifierRange,
)
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
from ...models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
    VariableDataPrototypeInSystemInstanceRef,
)
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
from ...models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    GenericTp,
    TcpTp,
    TransportProtocolConfiguration,
    UdpTp,
)
from ...models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    EndToEndTransformationDescription,
    EndToEndTransformationISignalProps,
)


class NetworkManagementParser(BaseARXMLParser):
    """
    Parser for AUTOSAR network management elements.

    Handles network management configuration, node clustering,
    transport protocols, and end-to-end protection.
    """

    def __init__(self, options=None):
        """Initialize NetworkManagementParser."""
        super().__init__(options)

    # ========================================================================
    # End-to-End Protection
    # ========================================================================

    def readEndToEndDescriptionDataIds(
        self, element: ET.Element, parent: EndToEndDescription
    ):
        child_element = self.find(element, "DATA-IDS")
        if child_element is not None:
            for value in self.getChildElementNumericalValueList(
                child_element, "DATA-ID"
            ):
                parent.addDataId(value)

    def getEndToEndDescription(
        self, element: ET.Element, key: str
    ) -> EndToEndDescription:
        child_element = self.find(element, key)
        desc = None
        if child_element is not None:
            desc = EndToEndDescription()
            self.readARObjectAttributes(child_element, desc)
            desc.setCategory(self.getChildElementOptionalLiteral(child_element, "CATEGORY"))
            self.readEndToEndDescriptionDataIds(child_element, desc)
            desc.setDataIdMode(
                self.getChildElementOptionalPositiveInteger(child_element, "DATA-ID-MODE")
            ).setDataLength(
                self.getChildElementOptionalPositiveInteger(child_element, "DATA-LENGTH")
            ).setMaxDeltaCounterInit(
                self.getChildElementOptionalPositiveInteger(
                    child_element, "MAX-DELTA-COUNTER-INIT"
                )
            ).setCrcOffset(
                self.getChildElementOptionalPositiveInteger(child_element, "CRC-OFFSET")
            ).setCounterOffset(
                self.getChildElementOptionalPositiveInteger(child_element, "COUNTER-OFFSET")
            )
        return desc

    def getVariableDataPrototypeInSystemInstanceRef(
        self, element: ET.Element,
    ) -> VariableDataPrototypeInSystemInstanceRef:
        instance_ref = None
        if element is not None:
            instance_ref = VariableDataPrototypeInSystemInstanceRef()
            for ref in self.getChildElementRefTypeList(
                element, "CONTEXT-COMPONENT-REF"
            ):
                instance_ref.addContextComponentRef(ref)
            instance_ref.setContextCompositionRef(
                self.getChildElementOptionalRefType(element, "CONTEXT-COMPOSITION-REF")
            ).setContextPortRef(
                self.getChildElementOptionalRefType(element, "CONTEXT-PORT-REF")
            ).setTargetDataPrototypeRef(
                self.getChildElementOptionalRefType(element, "TARGET-DATA-PROTOTYPE-REF")
            )
        return instance_ref

    def readEndToEndProtectionVariablePrototype(
        self, element: ET.Element, prototype: EndToEndProtectionVariablePrototype
    ):
        self.readARObjectAttributes(element, prototype)
        for child_element in self.findall(element, "RECEIVER-IREFS/RECEIVER-IREF"):
            prototype.addReceiverIref(
                self.getVariableDataPrototypeInSystemInstanceRef(child_element)
            )
        child_element = self.find(element, "SENDER-IREF")
        if child_element is not None:
            prototype.senderIRef = self.getVariableDataPrototypeInSystemInstanceRef(
                child_element
            )
        return prototype

    def readEndToEndProtectionEndToEndProtectionVariablePrototypes(
        self, element: ET.Element, protection: EndToEndProtection
    ):
        for child_element in self.findall(
            element, "END-TO-END-PROTECTION-VARIABLE-PROTOTYPES/*"
        ):
            tag_name = self.getTagName(child_element)
            if tag_name == "END-TO-END-PROTECTION-VARIABLE-PROTOTYPE":
                prototype = EndToEndProtectionVariablePrototype()
                self.readEndToEndProtectionVariablePrototype(child_element, prototype)
                protection.addEndToEndProtectionVariablePrototype(prototype)
            else:
                self.raiseError(
                    "Unsupported End To End Protection Variable Prototype <%s>"
                    % tag_name
                )

    def readEndToEndProtectionISignalIPdu(
        self, element: ET.Element, ipdu: EndToEndProtectionISignalIPdu
    ):
        ipdu.setDataOffset(self.getChildElementOptionalIntegerValue(element, "DATA-OFFSET")) \
            .setISignalGroupRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-GROUP-REF")) \
            .setISignalIPduRef(self.getChildElementOptionalRefType(element, "I-SIGNAL-I-PDU-REF"))

    def readEndToEndProtectionEndToEndProtectionISignalIPdus(
        self, element: ET.Element, protection: EndToEndProtection
    ):
        for child_element in self.findall(
            element, "END-TO-END-PROTECTION-I-SIGNAL-I-PDUS/*"
        ):
            tag_name = self.getTagName(child_element)
            if tag_name == "END-TO-END-PROTECTION-I-SIGNAL-I-PDU":
                ipdu = EndToEndProtectionISignalIPdu()
                self.readEndToEndProtectionISignalIPdu(child_element, ipdu)
                protection.addEndToEndProtectionISignalIPdu(ipdu)
            else:
                self.notImplemented(
                    "Unsupported EndToEndProtectionISignalIPdu <%s>" % tag_name
                )

    def readEndToEndProtection(
        self, element: ET.Element, parent: EndToEndProtectionSet
    ):
        short_name = self.getShortName(element)
        self.logger.debug("readEndToEndProtection %s" % short_name)
        protection = parent.createEndToEndProtection(short_name)
        self.readIdentifiable(element, protection)
        protection.setEndToEndProfile(self.getEndToEndDescription(element, "END-TO-END-PROFILE"))
        self.readEndToEndProtectionEndToEndProtectionISignalIPdus(element, protection)
        self.readEndToEndProtectionEndToEndProtectionVariablePrototypes(
            element, protection
        )

    def readEndToEndProtections(
        self, element: ET.Element, parent: EndToEndProtectionSet
    ):
        for child_element in self.findall(element, "END-TO-END-PROTECTIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "END-TO-END-PROTECTION":
                self.readEndToEndProtection(child_element, parent)
            else:
                self.notImplemented("Unsupported EndToEndProtectionSet <%s>" % tag_name)

    def readEndToEndProtectionSet(
        self, element: ET.Element, protection_set: EndToEndProtectionSet
    ):
        self.logger.debug("Read EndToEndProtectionSet <%s>" % protection_set.getShortName())
        self.readIdentifiable(element, protection_set)
        self.readEndToEndProtections(element, protection_set)

    def readEndToEndTransformationDescription(
        self, element: ET.Element, desc: EndToEndTransformationDescription
    ):
        self.readARObjectAttributes(element, desc)
        desc.setCategory(self.getChildElementOptionalLiteral(element, "CATEGORY"))
        self.readEndToEndDescriptionDataIds(element, desc)
        desc.setDataIdMode(self.getChildElementOptionalPositiveInteger(element, "DATA-ID-MODE")) \
           .setDataLength(self.getChildElementOptionalPositiveInteger(element, "DATA-LENGTH"))

    def readEndToEndTransformationISignalPropsDataIds(
        self, element: ET.Element, props: EndToEndTransformationISignalProps
    ):
        child_element = self.find(element, "DATA-IDS")
        if child_element is not None:
            props.addDataId(
                self.getChildElementOptionalPositiveInteger(child_element, "DATA-ID")
            )

    def readEndToEndTransformationISignalProps(
        self, element: ET.Element, props: EndToEndTransformationISignalProps
    ):
        child_element = self.find(
            element,
            "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS/END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL",
        )
        if child_element is not None:
            self.readTransformationISignalProps(child_element, props)
            self.readEndToEndTransformationISignalPropsDataIds(child_element, props)

    # ========================================================================
    # Network Management - NM PDU
    # ========================================================================

    def readNmPduISignalToIPduMappings(self, element: ET.Element, pdu: NmPdu):
        for child_element in self.findall(element, "I-SIGNAL-TO-I-PDU-MAPPINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "I-SIGNAL-TO-I-PDU-MAPPING":
                mapping = pdu.createISignalToIPduMapping(self.getShortName(child_element))
                self.readISignalToIPduMapping(child_element, mapping)
            else:
                self.notImplemented("Unsupported ISignalToIPduMapping <%s>" % tag_name)

    def readNmPdu(self, element: ET.Element, pdu: NmPdu):
        self.logger.debug("Read NmPdu <%s>" % pdu.getShortName())
        self.readPdu(element, pdu)
        self.readNmPduISignalToIPduMappings(element, pdu)
        pdu.setUnusedBitPattern(
            self.getChildElementOptionalIntegerValue(element, "UNUSED-BIT-PATTERN")
        )

    # ========================================================================
    # Network Management - NM Node
    # ========================================================================

    def readNmNode(self, element: ET.Element, nm_node: NmNode):
        self.readIdentifiable(element, nm_node)

        nm_node.setControllerRef(
            self.getChildElementOptionalRefType(element, "CONTROLLER-REF")
        ).setNmIfEcuRef(
            self.getChildElementOptionalRefType(element, "NM-IF-ECU-REF")
        ).setNmPassiveModeEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-PASSIVE-MODE-ENABLED")
        ).setNmNodeId(
            self.getChildElementOptionalNumericalValue(element, "NM-NODE-ID")
        )
        for ref in self.getChildElementRefTypeList(element, "RX-NM-PDU-REFS/RX-NM-PDU-REF"):
            nm_node.addRxNmPduRef(ref)
        for ref in self.getChildElementRefTypeList(element, "TX-NM-PDU-REFS/TX-NM-PDU-REF"):
            nm_node.addTxNmPduRefs(ref)

    def readCanNmNode(self, element: ET.Element, nm_node: CanNmNode):
        self.logger.debug("Read CanNmNode <%s>" % nm_node.getShortName())
        self.readNmNode(element, nm_node)
        nm_node.setNmCarWakeUpRxEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-CAR-WAKE-UP-RX-ENABLED")
        ).setNmMsgCycleOffset(
            self.getChildElementOptionalFloatValue(element, "NM-MSG-CYCLE-OFFSET")
        ).setNmMsgReducedTime(
            self.getChildElementOptionalFloatValue(element, "NM-MSG-REDUCED-TIME")
        ).setNmRangeConfig(
            self.getChildElementRxIdentifierRange(element, "NM-RANGE-CONFIG")
        )

    def readUdpNmNode(self, element: ET.Element, nm_node: UdpNmNode):
        self.logger.debug("Read UdpNmNode <%s>" % nm_node.getShortName())
        self.readNmNode(element, nm_node)
        nm_node.setNmMsgCycleOffset(
            self.getChildElementOptionalTimeValue(element, "NM-MSG-CYCLE-OFFSET")
        )

    # ========================================================================
    # Network Management - NM Cluster
    # ========================================================================

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

    def getCanNmClusterCoupling(
        self, element: ET.Element,
    ) -> CanNmClusterCoupling:
        coupling = CanNmClusterCoupling()
        for ref in self.getChildElementRefTypeList(
            element, "COUPLED-CLUSTER-REFS/COUPLED-CLUSTER-REF"
        ):
            coupling.addCoupledClusterRef(ref)
        coupling.setNmBusloadReductionEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-BUSLOAD-REDUCTION-ENABLED")
        ).setNmImmediateRestartEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-IMMEDIATE-RESTART-ENABLED")
        )
        return coupling

    def getUdpNmClusterCoupling(self, element: ET.Element) -> UdpNmClusterCoupling:
        coupling = UdpNmClusterCoupling()
        for ref in self.getChildElementRefTypeList(
            element, "COUPLED-CLUSTER-REFS/COUPLED-CLUSTER-REF"
        ):
            coupling.addCoupledClusterRef(ref)
        coupling.setNmImmediateRestartEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-IMMEDIATE-RESTART-ENABLED")
        )
        return coupling

    def readNmConfigNmClusterCouplings(
        self, element: ET.Element, nm_config: NmConfig
    ):
        for child_element in self.findall(element, "NM-CLUSTER-COUPLINGS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-NM-CLUSTER-COUPLING":
                nm_config.addNmClusterCouplings(
                    self.getCanNmClusterCoupling(child_element)
                )
            elif tag_name == "UDP-NM-CLUSTER-COUPLING":
                nm_config.addNmClusterCouplings(self.getUdpNmClusterCoupling(child_element))
            else:
                self.notImplemented("Unsupported Nm Node <%s>" % tag_name)

    def readNmCluster(self, element: ET.Element, cluster: NmCluster):
        self.logger.debug("read NmCluster %s" % cluster.getShortName())
        self.readIdentifiable(element, cluster)
        cluster.setCommunicationClusterRef(
            self.getChildElementOptionalRefType(element, "COMMUNICATION-CLUSTER-REF")
        ).setNmChannelId(
            self.getChildElementOptionalNumericalValue(element, "NM-CHANNEL-ID")
        ).setNmChannelSleepMaster(
            self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-SLEEP-MASTER")
        )
        self.readNmClusterNmNodes(element, cluster)
        cluster.setNmSynchronizingNetwork(
            self.getChildElementOptionalBooleanValue(element, "NM-SYNCHRONIZING-NETWORK")
        )

    def readCanNmCluster(self, element: ET.Element, cluster: CanNmCluster):
        self.logger.debug("Read CanNmCluster <%s>" % cluster.getShortName())
        self.readNmCluster(element, cluster)
        cluster.setNmBusloadReductionActive(
            self.getChildElementOptionalBooleanValue(element, "NM-BUSLOAD-REDUCTION-ACTIVE")
        ).setNmCarWakeUpRxEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-CAR-WAKE-UP-RX-ENABLED")
        ).setNmCbvPosition(
            self.getChildElementOptionalNumericalValue(element, "NM-CBV-POSITION")
        ).setNmChannelActive(
            self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-ACTIVE")
        ).setNmImmediateNmCycleTime(
            self.getChildElementOptionalFloatValue(element, "NM-IMMEDIATE-NM-CYCLE-TIME")
        ).setNmImmediateNmTransmissions(
            self.getChildElementOptionalNumericalValue(element, "NM-IMMEDIATE-NM-TRANSMISSIONS")
        ).setNmMessageTimeoutTime(
            self.getChildElementOptionalFloatValue(element, "NM-MESSAGE-TIMEOUT-TIME")
        ).setNmMsgCycleTime(
            self.getChildElementOptionalFloatValue(element, "NM-MSG-CYCLE-TIME")
        ).setNmNetworkTimeout(
            self.getChildElementOptionalFloatValue(element, "NM-NETWORK-TIMEOUT")
        ).setNmNidPosition(
            self.getChildElementOptionalNumericalValue(element, "NM-NID-POSITION")
        ).setNmRemoteSleepIndicationTime(
            self.getChildElementOptionalFloatValue(element, "NM-REMOTE-SLEEP-INDICATION-TIME")
        ).setNmRepeatMessageTime(
            self.getChildElementOptionalFloatValue(element, "NM-REPEAT-MESSAGE-TIME")
        ).setNmUserDataLength(
            self.getChildElementOptionalNumericalValue(element, "NM-USER-DATA-LENGTH")
        ).setNmWaitBusSleepTime(
            self.getChildElementOptionalFloatValue(element, "NM-WAIT-BUS-SLEEP-TIME")
        )

    def readUdpNmCluster(self, element: ET.Element, cluster: UdpNmCluster):
        self.logger.debug("Read UdpNmCluster <%s>" % cluster.getShortName())
        self.readNmCluster(element, cluster)
        cluster.setNmCbvPosition(
            self.getChildElementOptionalIntegerValue(element, "NM-CBV-POSITION")
        ).setNmChannelActive(
            self.getChildElementOptionalBooleanValue(element, "NM-CHANNEL-ACTIVE")
        ).setNmImmediateNmCycleTime(
            self.getChildElementOptionalTimeValue(element, "NM-IMMEDIATE-NM-CYCLE-TIME")
        ).setNmImmediateNmTransmissions(
            self.getChildElementOptionalPositiveInteger(element, "NM-IMMEDIATE-NM-TRANSMISSIONS")
        ).setNmMessageTimeoutTime(
            self.getChildElementOptionalTimeValue(element, "NM-MESSAGE-TIMEOUT-TIME")
        ).setNmMsgCycleTime(
            self.getChildElementOptionalTimeValue(element, "NM-MSG-CYCLE-TIME")
        ).setNmNetworkTimeout(
            self.getChildElementOptionalTimeValue(element, "NM-NETWORK-TIMEOUT")
        ).setNmNidPosition(
            self.getChildElementOptionalIntegerValue(element, "NM-NID-POSITION")
        ).setNmRemoteSleepIndicationTime(
            self.getChildElementOptionalTimeValue(element, "NM-REMOTE-SLEEP-INDICATION-TIME")
        ).setNmRepeatMessageTime(
            self.getChildElementOptionalTimeValue(element, "NM-REPEAT-MESSAGE-TIME")
        ).setNmWaitBusSleepTime(
            self.getChildElementOptionalTimeValue(element, "NM-WAIT-BUS-SLEEP-TIME")
        ).setVlanRef(self.getChildElementOptionalRefType(element, "VLAN-REF"))

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

    # ========================================================================
    # Network Management - NM ECU
    # ========================================================================

    def readUdpNmEcu(self, element: ET.Element, ecu: UdpNmEcu):
        ecu.setNmSynchronizationPointEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-SYNCHRONIZATION-POINT-ENABLED")
        )

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
        nm_ecu.setEcuInstanceRef(
            self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF")
        ).setNmBusSynchronizationEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-BUS-SYNCHRONIZATION-ENABLED")
        ).setNmComControlEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-COM-CONTROL-ENABLED")
        ).setNmNodeDetectionEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-NODE-DETECTION-ENABLED")
        ).setNmNodeIdEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-NODE-ID-ENABLED")
        ).setNmPduRxIndicationEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-PDU-RX-INDICATION-ENABLED")
        ).setNmRemoteSleepIndEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-REMOTE-SLEEP-IND-ENABLED")
        ).setNmRepeatMsgIndEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-REPEAT-MSG-IND-ENABLED")
        ).setNmStateChangeIndEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-STATE-CHANGE-IND-ENABLED")
        ).setNmUserDataEnabled(
            self.getChildElementOptionalBooleanValue(element, "NM-USER-DATA-ENABLED")
        )

    def readNmConfigNmIfEcus(self, element: ET.Element, nm_config: NmConfig):
        for child_element in self.findall(element, "NM-IF-ECUS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "NM-ECU":
                ecu = nm_config.createNmEcu(self.getShortName(child_element))
                self.readNmEcu(child_element, ecu)
            else:
                self.notImplemented("Unsupported NmIfEcus <%s>" % tag_name)

    # ========================================================================
    # Network Management - NM Config
    # ========================================================================

    def readNmConfig(self, element: ET.Element, config: NmConfig):
        self.logger.debug("Read NmConfig <%s>" % config.getShortName())
        self.readIdentifiable(element, config)
        self.readNmConfigNmClusters(element, config)
        self.readNmConfigNmClusterCouplings(element, config)
        self.readNmConfigNmIfEcus(element, config)

    # ========================================================================
    # Transport Protocols - Generic TP
    # ========================================================================

    def readGenericTp(self, element: ET.Element, tp: GenericTp):
        self.logger.debug("Read GenericTp")

    def readTcpTp(self, element: ET.Element, tp: TcpTp):
        self.logger.debug("Read TcpTp")

    def readUdpTp(self, element: ET.Element, tp: UdpTp):
        self.logger.debug("Read UdpTp")

    # ========================================================================
    # Transport Protocols - Common TP Config
    # ========================================================================

    def readTpConfig(self, element: ET.Element, config: TpConfig):
        self.readIdentifiable(element, config)
        config.setCommunicationClusterRef(
            self.getChildElementOptionalRefType(element, "COMMUNICATION-CLUSTER-REF")
        )

    # ========================================================================
    # Transport Protocols - CAN TP
    # ========================================================================

    def readCanTpAddress(self, element: ET.Element, address: CanTpAddress):
        self.readIdentifiable(element, address)
        address.setTpAddress(
            self.getChildElementOptionalIntegerValue(element, "TP-ADDRESS")
        ).setTpAddressExtensionValue(
            self.getChildElementOptionalIntegerValue(element, "TP-ADDRESS-EXTENSION-VALUE")
        )

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
        channel.setChannelId(
            self.getChildElementOptionalPositiveInteger(element, "CHANNEL-ID")
        ).setChannelMode(self.getChildElementOptionalLiteral(element, "CHANNEL-MODE"))

    def readCanTpConfigTpChannels(self, element: ET.Element, config: CanTpConfig):
        for child_element in self.findall(element, "TP-CHANNELS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-TP-CHANNEL":
                channel = config.createCanTpChannel(self.getShortName(child_element))
                self.readCanTpChannel(child_element, channel)
            else:
                self.notImplemented("Unsupported TpChannel <%s>" % tag_name)

    def readTpConnection(self, element: ET.Element, connection: TpConnection):
        self.readARObjectAttributes(element, connection)
        child_element = self.find(element, "IDENT")
        if child_element is not None:
            ident = connection.createTpConnectionIdent(self.getShortName(child_element))
            self.readReferrable(child_element, ident)

    def readTpConnectionReceiverRefs(
        self, element: ET.Element, connection: CanTpConnection
    ):
        for ref in self.getChildElementRefTypeList(element, "RECEIVER-REFS/RECEIVER-REF"):
            connection.addReceiverRef(ref)

    def readCanTpConnection(self, element: ET.Element, connection: CanTpConnection):
        self.readTpConnection(element, connection)
        connection.setAddressingFormat(
            self.getChildElementOptionalLiteral(element, "ADDRESSING-FORMAT")
        ).setCanTpChannelRef(
            self.getChildElementOptionalRefType(element, "CAN-TP-CHANNEL-REF")
        ).setCancellation(
            self.getChildElementOptionalBooleanValue(element, "CANCELLATION")
        ).setDataPduRef(self.getChildElementOptionalRefType(element, "DATA-PDU-REF")).setFlowControlPduRef(
            self.getChildElementOptionalRefType(element, "FLOW-CONTROL-PDU-REF")
        ).setMaxBlockSize(
            self.getChildElementOptionalIntegerValue(element, "MAX-BLOCK-SIZE")
        ).setMulticastRef(
            self.getChildElementOptionalRefType(element, "MULTICAST-REF")
        ).setPaddingActivation(
            self.getChildElementOptionalBooleanValue(element, "PADDING-ACTIVATION")
        )
        self.readTpConnectionReceiverRefs(element, connection)
        connection.setTaType(self.getChildElementOptionalLiteral(element, "TA-TYPE")).setTimeoutBr(
            self.getChildElementOptionalTimeValue(element, "TIMEOUT-BR")
        ).setTimeoutBs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-BS")).setTimeoutCr(
            self.getChildElementOptionalTimeValue(element, "TIMEOUT-CR")
        ).setTimeoutCs(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CS")).setTpSduRef(
            self.getChildElementOptionalRefType(element, "TP-SDU-REF")
        ).setTransmitterRef(
            self.getChildElementOptionalRefType(element, "TRANSMITTER-REF")
        )

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
        tp_ecu.setCycleTimeMainFunction(
            self.getChildElementOptionalTimeValue(element, "CYCLE-TIME-MAIN-FUNCTION")
        ).setEcuInstanceRef(
            self.getChildElementOptionalRefType(element, "ECU-INSTANCE-REF")
        )

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
        tp_node.setConnectorRef(
            self.getChildElementOptionalRefType(element, "CONNECTOR-REF")
        ).setMaxFcWait(self.getChildElementOptionalIntegerValue(element, "MAX-FC-WAIT")).setStMin(
            self.getChildElementOptionalTimeValue(element, "ST-MIN")
        ).setTimeoutAr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-AR")).setTimeoutAs(
            self.getChildElementOptionalTimeValue(element, "TIMEOUT-AS")
        ).setTpAddressRef(self.getChildElementOptionalRefType(element, "TP-ADDRESS-REF"))

    def readCanTpConfigTpNodes(self, element: ET.Element, config: CanTpConfig):
        for child_element in self.findall(element, "TP-NODES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "CAN-TP-NODE":
                tp_node = config.createCanTpNode(self.getShortName(child_element))
                self.readCanTpNode(child_element, tp_node)
            else:
                self.notImplemented("Unsupported TpNode <%s>" % tag_name)

    def readCanTpConfig(self, element: ET.Element, config: CanTpConfig):
        self.logger.debug("Read CanTpConfig <%s>" % config.getShortName())
        self.readTpConfig(element, config)
        self.readCanTpConfigTpAddresses(element, config)
        self.readCanTpConfigTpChannels(element, config)
        self.readCanTpConfigTpConnections(element, config)
        self.readCanTpConfigTpEcus(element, config)
        self.readCanTpConfigTpNodes(element, config)

    # ========================================================================
    # Transport Protocols - LIN TP
    # ========================================================================

    def readTpAddress(self, element: ET.Element, address: TpAddress):
        self.readIdentifiable(element, address)
        address.setTpAddress(self.getChildElementOptionalIntegerValue(element, "TP-ADDRESS"))

    def readLinTpConfigTpAddresses(self, element: ET.Element, config: LinTpConfig):
        for child_element in self.findall(element, "TP-ADDRESSS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "TP-ADDRESS":
                address = config.createTpAddress(self.getShortName(child_element))
                self.readTpAddress(child_element, address)
            else:
                self.notImplemented("Unsupported TpAddress <%s>" % tag_name)

    def readLinTpConnection(self, element: ET.Element, connection: LinTpConnection):
        self.readTpConnection(element, connection)
        connection.setDataPduRef(
            self.getChildElementOptionalRefType(element, "DATA-PDU-REF")
        ).setFlowControlRef(
            self.getChildElementOptionalRefType(element, "FLOW-CONTROL-REF")
        ).setLinTpNSduRef(
            self.getChildElementOptionalRefType(element, "LIN-TP-N-SDU-REF")
        )
        self.readTpConnectionReceiverRefs(element, connection)
        connection.setTimeoutAs(
            self.getChildElementOptionalTimeValue(element, "TIMEOUT-AS")
        ).setTimeoutCr(self.getChildElementOptionalTimeValue(element, "TIMEOUT-CR")).setTimeoutCs(
            self.getChildElementOptionalTimeValue(element, "TIMEOUT-CS")
        ).setTransmitterRef(
            self.getChildElementOptionalRefType(element, "TRANSMITTER-REF")
        )

    def readLinTpConfigTpConnections(self, element: ET.Element, config: LinTpConfig):
        for child_element in self.findall(element, "TP-CONNECTIONS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "LIN-TP-CONNECTION":
                connection = LinTpConnection()
                self.readLinTpConnection(child_element, connection)
                config.addTpConnection(connection)
            else:
                self.notImplemented("Unsupported TpConnection <%s>" % tag_name)

    def readLinTpNode(self, element: ET.Element, tp_node: LinTpNode):
        self.readIdentifiable(element, tp_node)
        tp_node.setConnectorRef(
            self.getChildElementOptionalRefType(element, "CONNECTOR-REF")
        ).setDropNotRequestedNad(
            self.getChildElementOptionalBooleanValue(element, "DROP-NOT-REQUESTED-NAD")
        ).setP2Max(self.getChildElementOptionalTimeValue(element, "P-2-MAX")).setP2Timing(
            self.getChildElementOptionalTimeValue(element, "P-2-TIMING")
        ).setTpAddressRef(self.getChildElementOptionalRefType(element, "TP-ADDRESS-REF"))

    def readLinTpConfigTpNodes(self, element: ET.Element, config: LinTpConfig):
        for child_element in self.findall(element, "TP-NODES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "LIN-TP-NODE":
                tp_node = config.createLinTpNode(self.getShortName(child_element))
                self.readLinTpNode(child_element, tp_node)
            else:
                self.notImplemented("Unsupported TpNode <%s>" % tag_name)

    def readLinTpConfig(self, element: ET.Element, config: LinTpConfig):
        self.logger.debug("Read LinTpConfig <%s>" % config.getShortName())
        self.readTpConfig(element, config)
        self.readLinTpConfigTpAddresses(element, config)
        self.readLinTpConfigTpConnections(element, config)
        self.readLinTpConfigTpNodes(element, config)

    # ========================================================================
    # Transport Protocols - DO-IP TP
    # ========================================================================

    def readDoIpLogicAddress(self, element: ET.Element, address: DoIpLogicAddress):
        self.readIdentifiable(element, address)
        address.setRoutingActivationDelay(
            self.getChildElementOptionalTimeValue(element, "ROUTING-ACTIVATION-DELAY")
        )

    def readDoIpTpConnection(self, element: ET.Element, connection: DoIpTpConnection):
        self.readTpConnection(element, connection)
        connection.setDoIpLogicAddressRef(
            self.getChildElementOptionalRefType(element, "DO-IP-LOGIC-ADDRESS-REF")
        )

    def readDoIpTpConfig(self, element: ET.Element, config: DoIpTpConfig):
        self.logger.debug("Read DoIpTpConfig <%s>" % config.getShortName())
        self.readTpConfig(element, config)
