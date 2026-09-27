# This module contains AUTOSAR System Template Ethernet Communication classes for Fibex4Ethernet
# (M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Ethernet Communication).
# Source: AUTOSAR_TPS_SystemTemplate (R4.3.1), Tables 6.118 (SocketConnectionBundle), 6.120
# (SocketConnection), 6.121 (RuntimeAddressConfigurationEnum), 6.122 (SocketConnectionIpduIdentifier),
# 6.125 (SoAdRoutingGroup), 6.129 (IPv6ExtHeaderFilterList), 6.130 (TcpOptionFilterSet),
# 6.131 (TcpOptionFilterList).

from typing import List, Optional, TYPE_CHECKING

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, PositiveInteger, RefType, TimeValue

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel import SocketConnection
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import PduCollectionSemanticsEnum
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import PduCollectionTriggerEnum
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import UdpChecksumCalculationEnum


class RuntimeAddressConfigurationEnum(AREnum):
    """
    This enumeration defines the protocol to be used to obtain the address information.
    """

    # RuntimeAddressConfigurationEnum method parity checklist:
    # Spec: R4.3.1/AUTOSAR_TPS_SystemTemplate.pdf, Table 6.121, p.320 (R4.3.1)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on SocketConnection.runtimePortConfiguration
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1

    # Static configuration is used to obtain the address information. Tags: atp.EnumerationValue=0
    NONE = "none"

    # AUTOSAR Service Discovery is used to obtain the address information. Tags: atp.EnumerationValue=1
    SD = "sd"

    def __init__(self):
        super().__init__(
            [
                RuntimeAddressConfigurationEnum.NONE,
                RuntimeAddressConfigurationEnum.SD,
            ]
        )


class SocketConnectionIpduIdentifier(ARObject):
    """
    An Identifier is required in case of one port per ECU communication where multiple Pdus are transmitted over the same connection. If only one IPdu is transmitted over the connetion this attribute can be ignored.
    """

    # SocketConnectionIpduIdentifier method parity checklist:
    # Spec: R4.3.1/AUTOSAR_TPS_SystemTemplate.pdf, Table 6.122, p.321 (R4.3.1)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # [x] getHeaderId                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setHeaderId                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getPduCollectionPduTimeout  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setPduCollectionPduTimeout  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getPduCollectionSemantics   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setPduCollectionSemantics   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getPduCollectionTrigger     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setPduCollectionTrigger     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getPduTriggeringRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setPduTriggeringRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getRoutingGroupRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setRoutingGroupRefs         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1

    def __init__(self):
        super().__init__()

        # If multiple Pdus are transmitted over the same connection this headerId can be used to distinguish between the different Pdus.
        self.headerId: Optional[PositiveInteger] = None

        # Defines the timeout in seconds the PDU collection shall be transmitted at the latest after this PDU has been put into the buffer.
        self.pduCollectionPduTimeout: Optional[TimeValue] = None

        # Specifies if the referenced PduTriggering shall be collected using a queued (i.e. all PDU instances) or last-is-best (i.e. only the last PDU instance) semantics. If this attribute is not present the behavior of "queued" is assumed.
        self.pduCollectionSemantics: Optional["PduCollectionSemanticsEnum"] = None

        # Defines whether the referenced Pdu contributes to the triggering of the socket transmission if Pdu collection is enabled for this socket.
        self.pduCollectionTrigger: Optional["PduCollectionTriggerEnum"] = None

        # Reference to a Pdu that is mapped to a socket connection.
        self.pduTriggeringRef: Optional[RefType] = None

        # Reference to RoutingGroups that can be enabled or disabled.
        self.routingGroupRefs: List[RefType] = []

    def getHeaderId(self) -> Optional[PositiveInteger]:
        """
        If multiple Pdus are transmitted over the same connection this headerId can be used to distinguish between the different Pdus.
        """
        return self.headerId

    def setHeaderId(self, value: Optional[PositiveInteger]) -> "SocketConnectionIpduIdentifier":
        """
        If multiple Pdus are transmitted over the same connection this headerId can be used to distinguish between the different Pdus.
        A None value is a no-op and does not overwrite an existing headerId.
        """
        if value is not None:
            self.headerId = value
        return self

    def getPduCollectionPduTimeout(self) -> Optional[TimeValue]:
        """
        Defines the timeout in seconds the PDU collection shall be transmitted at the latest after this PDU has been put into the buffer.
        """
        return self.pduCollectionPduTimeout

    def setPduCollectionPduTimeout(self, value: Optional[TimeValue]) -> "SocketConnectionIpduIdentifier":
        """
        Defines the timeout in seconds the PDU collection shall be transmitted at the latest after this PDU has been put into the buffer.
        A None value is a no-op and does not overwrite an existing pduCollectionPduTimeout.
        """
        if value is not None:
            self.pduCollectionPduTimeout = value
        return self

    def getPduCollectionSemantics(self) -> Optional["PduCollectionSemanticsEnum"]:
        """
        Specifies if the referenced PduTriggering shall be collected using a queued (i.e. all PDU instances) or last-is-best (i.e. only the last PDU instance) semantics. If this attribute is not present the behavior of "queued" is assumed.
        """
        return self.pduCollectionSemantics

    def setPduCollectionSemantics(self, value: Optional["PduCollectionSemanticsEnum"]) -> "SocketConnectionIpduIdentifier":
        """
        Specifies if the referenced PduTriggering shall be collected using a queued (i.e. all PDU instances) or last-is-best (i.e. only the last PDU instance) semantics. If this attribute is not present the behavior of "queued" is assumed.
        A None value is a no-op and does not overwrite an existing pduCollectionSemantics.
        """
        if value is not None:
            self.pduCollectionSemantics = value
        return self

    def getPduCollectionTrigger(self) -> Optional["PduCollectionTriggerEnum"]:
        """
        Defines whether the referenced Pdu contributes to the triggering of the socket transmission if Pdu collection is enabled for this socket.
        """
        return self.pduCollectionTrigger

    def setPduCollectionTrigger(self, value: Optional["PduCollectionTriggerEnum"]) -> "SocketConnectionIpduIdentifier":
        """
        Defines whether the referenced Pdu contributes to the triggering of the socket transmission if Pdu collection is enabled for this socket.
        A None value is a no-op and does not overwrite an existing pduCollectionTrigger.
        """
        if value is not None:
            self.pduCollectionTrigger = value
        return self

    def getPduTriggeringRef(self) -> Optional[RefType]:
        """
        Reference to a Pdu that is mapped to a socket connection.
        """
        return self.pduTriggeringRef

    def setPduTriggeringRef(self, value: Optional[RefType]) -> "SocketConnectionIpduIdentifier":
        """
        Reference to a Pdu that is mapped to a socket connection.
        A None value is a no-op and does not overwrite an existing pduTriggeringRef.
        """
        if value is not None:
            self.pduTriggeringRef = value
        return self

    def getRoutingGroupRefs(self) -> List[RefType]:
        """
        Reference to RoutingGroups that can be enabled or disabled.
        """
        return self.routingGroupRefs

    def setRoutingGroupRefs(self, value: Optional[List[RefType]]) -> "SocketConnectionIpduIdentifier":
        """
        Reference to RoutingGroups that can be enabled or disabled.
        A None value is a no-op and leaves the existing routingGroupRefs unchanged.
        """
        if value is not None:
            self.routingGroupRefs = value
        return self


class SocketConnectionBundle(Referrable):
    """
    This elements groups SocketConnections, i.e. specifies socket connections belonging to the bundle and describes properties which are common for all socket connections in the bundle.
    """

    # SocketConnectionBundle method parity checklist:
    # Spec: R4.3.1/AUTOSAR_TPS_SystemTemplate.pdf, Table 6.118, p.316 (R4.3.1)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # [x] getBundledConnections          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] addBundledConnection           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getDifferentiatedServiceField [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setDifferentiatedServiceField [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getFlowLabel                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setFlowLabel                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getPathMtuDiscoveryEnabled     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setPathMtuDiscoveryEnabled     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getPdus                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] addPdu                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getServerPortRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setServerPortRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getUdpChecksumHandling         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setUdpChecksumHandling         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of SocketConnections in the connectionGroup.
        self.bundledConnections: List["SocketConnection"] = []

        # The 6-bit Differentiated Service Field in the IP headers may be used for classifying network traffic. If not set a value of zero is used to indicate packets that have not been classified.
        self.differentiatedServiceField: Optional[PositiveInteger] = None

        # The 20-bit Flow Label field in the IPv6 header may be used by a source to label sequences of packets for which it requests special handling by the IPv6 routers, such as non-default quality of service. If not set a Flow Label of zero is used to indicate packets that have not been labeled.
        self.flowLabel: Optional[PositiveInteger] = None

        # Defines whether the Path MTU Discovery shall be performed for the related socket.
        self.pathMtuDiscoveryEnabled: Optional[Boolean] = None

        # With this aggregation SocketConnectionIpduIdentifier elements are assigned to all SocketConnections that are available in this SocketConnetionBundle.
        self.pdus: List[SocketConnectionIpduIdentifier] = []

        # Server Port for TCP/UDP connection in an abstract communication sense. The server is the major provider of the communication. Please note that the server may also consume data.
        self.serverPortRef: Optional[RefType] = None

        # Specifies if UDP checksum handling shall be enabled (udpChecksumEnabled) or skipped (udpChecksumDisabled) on the related socket connection.
        self.udpChecksumHandling: Optional["UdpChecksumCalculationEnum"] = None

    def getBundledConnections(self) -> List["SocketConnection"]:
        """
        Collection of SocketConnections in the connectionGroup.
        """
        return self.bundledConnections

    def addBundledConnection(self, value: Optional["SocketConnection"]) -> "SocketConnectionBundle":
        """
        Collection of SocketConnections in the connectionGroup.
        A None value is a no-op and is not appended to bundledConnections.
        """
        if value is not None:
            self.bundledConnections.append(value)
        return self

    def getDifferentiatedServiceField(self) -> Optional[PositiveInteger]:
        """
        The 6-bit Differentiated Service Field in the IP headers may be used for classifying network traffic. If not set a value of zero is used to indicate packets that have not been classified.
        """
        return self.differentiatedServiceField

    def setDifferentiatedServiceField(self, value: Optional[PositiveInteger]) -> "SocketConnectionBundle":
        """
        The 6-bit Differentiated Service Field in the IP headers may be used for classifying network traffic. If not set a value of zero is used to indicate packets that have not been classified.
        A None value is a no-op and does not overwrite an existing differentiatedServiceField.
        """
        if value is not None:
            self.differentiatedServiceField = value
        return self

    def getFlowLabel(self) -> Optional[PositiveInteger]:
        """
        The 20-bit Flow Label field in the IPv6 header may be used by a source to label sequences of packets for which it requests special handling by the IPv6 routers, such as non-default quality of service. If not set a Flow Label of zero is used to indicate packets that have not been labeled.
        """
        return self.flowLabel

    def setFlowLabel(self, value: Optional[PositiveInteger]) -> "SocketConnectionBundle":
        """
        The 20-bit Flow Label field in the IPv6 header may be used by a source to label sequences of packets for which it requests special handling by the IPv6 routers, such as non-default quality of service. If not set a Flow Label of zero is used to indicate packets that have not been labeled.
        A None value is a no-op and does not overwrite an existing flowLabel.
        """
        if value is not None:
            self.flowLabel = value
        return self

    def getPathMtuDiscoveryEnabled(self) -> Optional[Boolean]:
        """
        Defines whether the Path MTU Discovery shall be performed for the related socket.
        """
        return self.pathMtuDiscoveryEnabled

    def setPathMtuDiscoveryEnabled(self, value: Optional[Boolean]) -> "SocketConnectionBundle":
        """
        Defines whether the Path MTU Discovery shall be performed for the related socket.
        A None value is a no-op and does not overwrite an existing pathMtuDiscoveryEnabled.
        """
        if value is not None:
            self.pathMtuDiscoveryEnabled = value
        return self

    def getPdus(self) -> List[SocketConnectionIpduIdentifier]:
        """
        With this aggregation SocketConnectionIpduIdentifier elements are assigned to all SocketConnections that are available in this SocketConnetionBundle.
        """
        return self.pdus

    def addPdu(self, value: Optional[SocketConnectionIpduIdentifier]) -> "SocketConnectionBundle":
        """
        With this aggregation SocketConnectionIpduIdentifier elements are assigned to all SocketConnections that are available in this SocketConnetionBundle.
        A None value is a no-op and is not appended to pdus.
        """
        if value is not None:
            self.pdus.append(value)
        return self

    def getServerPortRef(self) -> Optional[RefType]:
        """
        Server Port for TCP/UDP connection in an abstract communication sense. The server is the major provider of the communication. Please note that the server may also consume data.
        """
        return self.serverPortRef

    def setServerPortRef(self, value: Optional[RefType]) -> "SocketConnectionBundle":
        """
        Server Port for TCP/UDP connection in an abstract communication sense. The server is the major provider of the communication. Please note that the server may also consume data.
        A None value is a no-op and does not overwrite an existing serverPortRef.
        """
        if value is not None:
            self.serverPortRef = value
        return self

    def getUdpChecksumHandling(self) -> Optional["UdpChecksumCalculationEnum"]:
        """
        Specifies if UDP checksum handling shall be enabled (udpChecksumEnabled) or skipped (udpChecksumDisabled) on the related socket connection.
        """
        return self.udpChecksumHandling

    def setUdpChecksumHandling(self, value: Optional["UdpChecksumCalculationEnum"]) -> "SocketConnectionBundle":
        """
        Specifies if UDP checksum handling shall be enabled (udpChecksumEnabled) or skipped (udpChecksumDisabled) on the related socket connection.
        A None value is a no-op and does not overwrite an existing udpChecksumHandling.
        """
        if value is not None:
            self.udpChecksumHandling = value
        return self
