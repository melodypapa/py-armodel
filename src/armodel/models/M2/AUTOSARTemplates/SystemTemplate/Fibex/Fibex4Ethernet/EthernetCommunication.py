# This module contains AUTOSAR System Template Ethernet Communication classes for Fibex4Ethernet
# (M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Ethernet Communication).
# Source: AUTOSAR_TPS_SystemTemplate (R4.3.1), Tables 6.118 (SocketConnectionBundle), 6.120
# (SocketConnection), 6.121 (RuntimeAddressConfigurationEnum), 6.122 (SocketConnectionIpduIdentifier),
# 6.125 (SoAdRoutingGroup), 6.129 (IPv6ExtHeaderFilterList), 6.130 (TcpOptionFilterSet),
# 6.131 (TcpOptionFilterList).

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Describable, Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Identifier, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement


class RuntimeAddressConfigurationEnum(AREnum):
    """
    This enumeration defines the protocol to be used to obtain the address information.
    """

    # RuntimeAddressConfigurationEnum method parity checklist:
    # Spec: AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.121, p.320
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on SocketConnection.runtimePortConfiguration

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


class SocketConnection(Describable):
    """
    The SoAd serves as a (De)Multiplexer between different PDU sources and the TCP/IP stack.
    """

    # SocketConnection method parity checklist:
    # Spec: AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.120, p.318-319 (full 11-row table, spans the page break; element names and removed-member exclusion per the R4.3.1 AUTOSAR_00044.xsd SOCKET-CONNECTION group, atp.Status="removed" members excluded; member order = PDF table order in model, checklist, reader and writer)
    # Spec verified: R4.3.1
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # [x] getAllowedIPv6ExtHeadersRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setAllowedIPv6ExtHeadersRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getAllowedTcpOptionsRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setAllowedTcpOptionsRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getClientIpAddrFromConnectionRequest  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setClientIpAddrFromConnectionRequest  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getClientPortRef                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setClientPortRef                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getClientPortFromConnectionRequest    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setClientPortFromConnectionRequest    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getPdus                               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] addPdu                                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getPduCollectionMaxBufferSize         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setPduCollectionMaxBufferSize         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getPduCollectionTimeout               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setPduCollectionTimeout               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getRuntimeIpAddressConfiguration      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setRuntimeIpAddressConfiguration      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getRuntimePortConfiguration           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setRuntimePortConfiguration           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getShortLabel                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] setShortLabel                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1

    def __init__(self):
        super().__init__()

        # Reference to a list of IPv6 Extension Headers allowed for this SocketConnection. If no list is referenced all IPv6 Extension Headers are allowed and processed.
        self.allowedIPv6ExtHeadersRef: Optional[RefType] = None

        # Reference to a list of TCP options allowed for this SocketConnection.
        self.allowedTcpOptionsRef: Optional[RefType] = None

        # If set to true the Server "learns" the client IP address on connection request. This means that the statically configured IP Address of the related client shall be ignored. If set to false the Server only accepts statically configured IP address, e.g. 192.168.1.2. This means that the statically configured IP Address of the Client shall be used.
        self.clientIpAddrFromConnectionRequest: Optional[Boolean] = None

        # Client Port for TCP/UDP connection in an abstract communication sense. The client is the major requester of the communication. Please note that the client may also produce data.
        self.clientPortRef: Optional[RefType] = None

        # If set to true the Server "learns" the client Port on connection request. This means that the statically configured Port of the related client shall be ignored. If set to false the Server only accepts statically configured Port. This means that the statically configured Port of the Client shall be used.
        self.clientPortFromConnectionRequest: Optional[Boolean] = None

        # PDUs handed over by the PDU Router (Transmission over the Ethernet) or PDUs handed over by SoAd (Reception over Ethernet). Multiple IPdus can be transmitted over one socket connection.
        self.pdus: List["SocketConnectionIpduIdentifier"] = []

        # Defines the maximum buffer size in Byte which shall be filled before a socket with Pdu collection enabled shall be transmitted to the lower layer.
        self.pduCollectionMaxBufferSize: Optional[PositiveInteger] = None

        # Defines the time in seconds which shall pass before a socket with Pdu collection enabled shall be transmitted to the lower layer after the first Pdu has been put into the socket buffer.
        self.pduCollectionTimeout: Optional[TimeValue] = None

        # This attribute determines which protocol is used by the client to obtain the IP Address information. If this attribute is not set to none the value determines the service used by the client to obtain the IP Address information for the SocketConnection. If this attribute is set to none the client used the statically configured IP Address information.
        self.runtimeIpAddressConfiguration: Optional[RuntimeAddressConfigurationEnum] = None

        # This attribute determines which protocol is used by the client to obtain the Port information. If this attribute is not set to none the value determines the service used by the client to obtain the Port information for the SocketConnection. If this attribute is set to none the client uses the statically configured Port information.
        self.runtimePortConfiguration: Optional[RuntimeAddressConfigurationEnum] = None

        # This attribute specifies an identifying shortName for the SocketConnection. It shall be unique within its context.
        self.shortLabel: Optional[Identifier] = None

    def getAllowedIPv6ExtHeadersRef(self) -> Optional[RefType]:
        """Reference to a list of IPv6 Extension Headers allowed for this SocketConnection. If no list is referenced all IPv6 Extension Headers are allowed and processed."""
        return self.allowedIPv6ExtHeadersRef

    def setAllowedIPv6ExtHeadersRef(self, value: Optional[RefType]) -> "SocketConnection":
        """
        Reference to a list of IPv6 Extension Headers allowed for this SocketConnection. If no list is referenced all IPv6 Extension Headers are allowed and processed.
        A None value is a no-op and does not overwrite an existing allowedIPv6ExtHeadersRef.
        """
        if value is not None:
            self.allowedIPv6ExtHeadersRef = value
        return self

    def getAllowedTcpOptionsRef(self) -> Optional[RefType]:
        """Reference to a list of TCP options allowed for this SocketConnection."""
        return self.allowedTcpOptionsRef

    def setAllowedTcpOptionsRef(self, value: Optional[RefType]) -> "SocketConnection":
        """
        Reference to a list of TCP options allowed for this SocketConnection.
        A None value is a no-op and does not overwrite an existing allowedTcpOptionsRef.
        """
        if value is not None:
            self.allowedTcpOptionsRef = value
        return self

    def getClientIpAddrFromConnectionRequest(self) -> Optional[Boolean]:
        """If set to true the Server "learns" the client IP address on connection request. This means that the statically configured IP Address of the related client shall be ignored. If set to false the Server only accepts statically configured IP address, e.g. 192.168.1.2. This means that the statically configured IP Address of the Client shall be used."""
        return self.clientIpAddrFromConnectionRequest

    def setClientIpAddrFromConnectionRequest(self, value: Optional[Boolean]) -> "SocketConnection":
        """
        If set to true the Server "learns" the client IP address on connection request. This means that the statically configured IP Address of the related client shall be ignored. If set to false the Server only accepts statically configured IP address, e.g. 192.168.1.2. This means that the statically configured IP Address of the Client shall be used.
        A None value is a no-op and does not overwrite an existing clientIpAddrFromConnectionRequest.
        """
        if value is not None:
            self.clientIpAddrFromConnectionRequest = value
        return self

    def getClientPortRef(self) -> Optional[RefType]:
        """Client Port for TCP/UDP connection in an abstract communication sense. The client is the major requester of the communication. Please note that the client may also produce data."""
        return self.clientPortRef

    def setClientPortRef(self, value: Optional[RefType]) -> "SocketConnection":
        """
        Client Port for TCP/UDP connection in an abstract communication sense. The client is the major requester of the communication. Please note that the client may also produce data.
        A None value is a no-op and does not overwrite an existing clientPortRef.
        """
        if value is not None:
            self.clientPortRef = value
        return self

    def getClientPortFromConnectionRequest(self) -> Optional[Boolean]:
        """If set to true the Server "learns" the client Port on connection request. This means that the statically configured Port of the related client shall be ignored. If set to false the Server only accepts statically configured Port. This means that the statically configured Port of the Client shall be used."""
        return self.clientPortFromConnectionRequest

    def setClientPortFromConnectionRequest(self, value: Optional[Boolean]) -> "SocketConnection":
        """
        If set to true the Server "learns" the client Port on connection request. This means that the statically configured Port of the related client shall be ignored. If set to false the Server only accepts statically configured Port. This means that the statically configured Port of the Client shall be used.
        A None value is a no-op and does not overwrite an existing clientPortFromConnectionRequest.
        """
        if value is not None:
            self.clientPortFromConnectionRequest = value
        return self

    def getPdus(self) -> List["SocketConnectionIpduIdentifier"]:
        """PDUs handed over by the PDU Router (Transmission over the Ethernet) or PDUs handed over by SoAd (Reception over Ethernet). Multiple IPdus can be transmitted over one socket connection."""
        return self.pdus

    def addPdu(self, value: Optional["SocketConnectionIpduIdentifier"]) -> "SocketConnection":
        """
        PDUs handed over by the PDU Router (Transmission over the Ethernet) or PDUs handed over by SoAd (Reception over Ethernet). Multiple IPdus can be transmitted over one socket connection.
        A None value is a no-op and does not extend pdus.
        """
        if value is not None:
            self.pdus.append(value)
        return self

    def getPduCollectionMaxBufferSize(self) -> Optional[PositiveInteger]:
        """Defines the maximum buffer size in Byte which shall be filled before a socket with Pdu collection enabled shall be transmitted to the lower layer."""
        return self.pduCollectionMaxBufferSize

    def setPduCollectionMaxBufferSize(self, value: Optional[PositiveInteger]) -> "SocketConnection":
        """
        Defines the maximum buffer size in Byte which shall be filled before a socket with Pdu collection enabled shall be transmitted to the lower layer.
        A None value is a no-op and does not overwrite an existing pduCollectionMaxBufferSize.
        """
        if value is not None:
            self.pduCollectionMaxBufferSize = value
        return self

    def getPduCollectionTimeout(self) -> Optional[TimeValue]:
        """Defines the time in seconds which shall pass before a socket with Pdu collection enabled shall be transmitted to the lower layer after the first Pdu has been put into the socket buffer."""
        return self.pduCollectionTimeout

    def setPduCollectionTimeout(self, value: Optional[TimeValue]) -> "SocketConnection":
        """
        Defines the time in seconds which shall pass before a socket with Pdu collection enabled shall be transmitted to the lower layer after the first Pdu has been put into the socket buffer.
        A None value is a no-op and does not overwrite an existing pduCollectionTimeout.
        """
        if value is not None:
            self.pduCollectionTimeout = value
        return self

    def getRuntimeIpAddressConfiguration(self) -> Optional[RuntimeAddressConfigurationEnum]:
        """This attribute determines which protocol is used by the client to obtain the IP Address information. If this attribute is not set to none the value determines the service used by the client to obtain the IP Address information for the SocketConnection. If this attribute is set to none the client used the statically configured IP Address information."""
        return self.runtimeIpAddressConfiguration

    def setRuntimeIpAddressConfiguration(self, value: Optional[RuntimeAddressConfigurationEnum]) -> "SocketConnection":
        """
        This attribute determines which protocol is used by the client to obtain the IP Address information. If this attribute is not set to none the value determines the service used by the client to obtain the IP Address information for the SocketConnection. If this attribute is set to none the client used the statically configured IP Address information.
        A None value is a no-op and does not overwrite an existing runtimeIpAddressConfiguration.
        """
        if value is not None:
            self.runtimeIpAddressConfiguration = value
        return self

    def getRuntimePortConfiguration(self) -> Optional[RuntimeAddressConfigurationEnum]:
        """This attribute determines which protocol is used by the client to obtain the Port information. If this attribute is not set to none the value determines the service used by the client to obtain the Port information for the SocketConnection. If this attribute is set to none the client uses the statically configured Port information."""
        return self.runtimePortConfiguration

    def setRuntimePortConfiguration(self, value: Optional[RuntimeAddressConfigurationEnum]) -> "SocketConnection":
        """
        This attribute determines which protocol is used by the client to obtain the Port information. If this attribute is not set to none the value determines the service used by the client to obtain the Port information for the SocketConnection. If this attribute is set to none the client uses the statically configured Port information.
        A None value is a no-op and does not overwrite an existing runtimePortConfiguration.
        """
        if value is not None:
            self.runtimePortConfiguration = value
        return self

    def getShortLabel(self) -> Optional[Identifier]:
        """This attribute specifies an identifying shortName for the SocketConnection. It shall be unique within its context."""
        return self.shortLabel

    def setShortLabel(self, value: Optional[Identifier]) -> "SocketConnection":
        """
        This attribute specifies an identifying shortName for the SocketConnection. It shall be unique within its context.
        A None value is a no-op and does not overwrite an existing shortLabel.
        """
        if value is not None:
            self.shortLabel = value
        return self


class SocketConnectionIpduIdentifier(ARObject):
    """
    Identifies an IPDU (Interaction Protocol Data Unit) within a socket connection,
    defining header IDs, timeout values, collection semantics, and references
    to PDUs and triggering mechanisms for Ethernet communication.
    """

    # SocketConnectionIpduIdentifier method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getHeaderId                  [x] impl  [ ] docstring  [ ] test
    # [ ] setHeaderId                  [x] impl  [ ] docstring  [ ] test
    # [ ] getPduCollectionPduTimeout   [x] impl  [ ] docstring  [ ] test
    # [ ] setPduCollectionPduTimeout   [x] impl  [ ] docstring  [ ] test
    # [ ] getPduCollectionSemantics    [x] impl  [ ] docstring  [ ] test
    # [ ] setPduCollectionSemantics    [x] impl  [ ] docstring  [ ] test
    # [ ] getPduCollectionTrigger      [x] impl  [ ] docstring  [ ] test
    # [ ] setPduCollectionTrigger      [x] impl  [ ] docstring  [ ] test
    # [ ] getPduRef                    [x] impl  [ ] docstring  [ ] test
    # [ ] setPduRef                    [x] impl  [ ] docstring  [ ] test
    # [ ] getPduTriggeringRef          [x] impl  [ ] docstring  [ ] test
    # [ ] setPduTriggeringRef          [x] impl  [ ] docstring  [ ] test
    # [ ] getRoutingGroupRefs          [x] impl  [ ] docstring  [ ] test
    # [ ] setRoutingGroupRefs          [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.headerId: PositiveInteger = None
        self.pduCollectionPduTimeout: TimeValue = None
        self.pduCollectionSemantics = None
        self.pduCollectionTrigger = None
        self.PduRef: RefType = None
        self.pduTriggeringRef: RefType = None
        self.routingGroupRefs: List[RefType] = []

    def getHeaderId(self):
        return self.headerId

    def setHeaderId(self, value):
        self.headerId = value
        return self

    def getPduCollectionPduTimeout(self):
        return self.pduCollectionPduTimeout

    def setPduCollectionPduTimeout(self, value):
        self.pduCollectionPduTimeout = value
        return self

    def getPduCollectionSemantics(self):
        return self.pduCollectionSemantics

    def setPduCollectionSemantics(self, value):
        self.pduCollectionSemantics = value
        return self

    def getPduCollectionTrigger(self):
        return self.pduCollectionTrigger

    def setPduCollectionTrigger(self, value):
        self.pduCollectionTrigger = value
        return self

    def getPduRef(self):
        return self.PduRef

    def setPduRef(self, value):
        self.PduRef = value
        return self

    def getPduTriggeringRef(self):
        return self.pduTriggeringRef

    def setPduTriggeringRef(self, value):
        self.pduTriggeringRef = value
        return self

    def getRoutingGroupRefs(self):
        return self.routingGroupRefs

    def setRoutingGroupRefs(self, value):
        self.routingGroupRefs = value
        return self


class SocketConnectionBundle(Referrable):
    """
    Groups multiple socket connections into a bundle for managing related
    Ethernet communications, including differentiated services, flow labels,
    and UDP checksum handling configurations.
    """

    # SocketConnectionBundle method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getBundledConnections        [x] impl  [ ] docstring  [ ] test
    # [ ] addBundledConnection         [x] impl  [ ] docstring  [ ] test
    # [ ] getDifferentiatedServiceField [x] impl  [ ] docstring  [ ] test
    # [ ] setDifferentiatedServiceField [x] impl  [ ] docstring  [ ] test
    # [ ] getFlowLabel                 [x] impl  [ ] docstring  [ ] test
    # [ ] setFlowLabel                 [x] impl  [ ] docstring  [ ] test
    # [ ] getPathMtuDiscoveryEnabled   [x] impl  [ ] docstring  [ ] test
    # [ ] setPathMtuDiscoveryEnabled   [x] impl  [ ] docstring  [ ] test
    # [ ] getPdus                      [x] impl  [ ] docstring  [ ] test
    # [ ] setPdus                      [x] impl  [ ] docstring  [ ] test
    # [ ] getServerPortRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setServerPortRef             [x] impl  [ ] docstring  [ ] test
    # [ ] getUdpChecksumHandling       [x] impl  [ ] docstring  [ ] test
    # [ ] setUdpChecksumHandling       [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.bundledConnections: List[SocketConnection] = []
        self.differentiatedServiceField: PositiveInteger = None
        self.flowLabel: PositiveInteger = None
        self.pathMtuDiscoveryEnabled: Boolean = None
        self.pdus: List[SocketConnectionIpduIdentifier] = []
        self.serverPortRef: RefType = None
        self.udpChecksumHandling = None  # type: UdpChecksumCalculationEnum

    def getBundledConnections(self):
        return self.bundledConnections

    def addBundledConnection(self, value):
        self.bundledConnections.append(value)
        return self

    def getDifferentiatedServiceField(self):
        return self.differentiatedServiceField

    def setDifferentiatedServiceField(self, value):
        self.differentiatedServiceField = value
        return self

    def getFlowLabel(self):
        return self.flowLabel

    def setFlowLabel(self, value):
        self.flowLabel = value
        return self

    def getPathMtuDiscoveryEnabled(self):
        return self.pathMtuDiscoveryEnabled

    def setPathMtuDiscoveryEnabled(self, value):
        self.pathMtuDiscoveryEnabled = value
        return self

    def getPdus(self):
        return self.pdus

    def setPdus(self, value):
        self.pdus = value
        return self

    def getServerPortRef(self):
        return self.serverPortRef

    def setServerPortRef(self, value):
        self.serverPortRef = value
        return self

    def getUdpChecksumHandling(self):
        return self.udpChecksumHandling

    def setUdpChecksumHandling(self, value):
        self.udpChecksumHandling = value
        return self


class SoAdRoutingGroup(FibexElement):
    """
    Defines a routing group for the Socket Adaptor (SoAd) module,
    specifying how Ethernet communication is organized and controlled
    within the AUTOSAR communication system.
    """

    # SoAdRoutingGroup method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEventGroupControlType     [x] impl  [ ] docstring  [ ] test
    # [ ] setEventGroupControlType     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.eventGroupControlType = None  # type: EventGroupControlTypeEnum

    def getEventGroupControlType(self):
        return self.eventGroupControlType

    def setEventGroupControlType(self, value):
        if value is not None:
            self.eventGroupControlType = value
        return self


class IPv6ExtHeaderFilterList(Identifiable):
    """
    White list for the filtering of IPv6 extension headers.
    """

    # IPv6ExtHeaderFilterList method parity checklist:
    # Spec: AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.129, p.325
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # [x] getAllowedIPv6ExtHeaders  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # [x] addAllowedIPv6ExtHeader   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # (reader/writer N/A: consumed as ref target on SocketConnection.allowedIPv6ExtHeaders)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # IPv6 Extension Header type allowed by this filter.
        self.allowedIPv6ExtHeaders: List[PositiveInteger] = []

    def getAllowedIPv6ExtHeaders(self) -> List[PositiveInteger]:
        """IPv6 Extension Header type allowed by this filter."""
        return self.allowedIPv6ExtHeaders

    def addAllowedIPv6ExtHeader(self, value: PositiveInteger) -> "IPv6ExtHeaderFilterList":
        """
        IPv6 Extension Header type allowed by this filter.
        A None value is a no-op and does not extend allowedIPv6ExtHeaders.
        """
        if value is not None:
            self.allowedIPv6ExtHeaders.append(value)
        return self


class TcpOptionFilterList(Identifiable):
    """
    White list for the filtering of TCP options.
    """

    # TcpOptionFilterList method parity checklist:
    # Spec: AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.131, p.326
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # [x] getAllowedTcpOptions   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1
    # [x] addAllowedTcpOption    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # (serialized as TCP-OPTION-FILTER-LIST within TcpOptionFilterSet, R4.3.1 AUTOSAR_00044.xsd)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # TCP option kind allowed by this filter.
        self.allowedTcpOptions: List[PositiveInteger] = []

    def getAllowedTcpOptions(self) -> List[PositiveInteger]:
        """TCP option kind allowed by this filter."""
        return self.allowedTcpOptions

    def addAllowedTcpOption(self, value: PositiveInteger) -> "TcpOptionFilterList":
        """
        TCP option kind allowed by this filter.
        A None value is a no-op and does not extend allowedTcpOptions.
        """
        if value is not None:
            self.allowedTcpOptions.append(value)
        return self


class TcpOptionFilterSet(ARElement):
    """
    Set of TcpOptionFilterLists. Tags: atp.recommendedPackage=TcpOptionFilterSets
    """

    # TcpOptionFilterSet method parity checklist:
    # Spec: AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.130, p.326
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R4.3.1
    # [x] createTcpOptionFilterList  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R4.3.1
    # [x] getTcpOptionFilterLists    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R4.3.1

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Collection of white lists for the filtering of TCP options.
        self.tcpOptionFilterLists: List[TcpOptionFilterList] = []

    def createTcpOptionFilterList(self, short_name: str) -> TcpOptionFilterList:
        """
        Collection of white lists for the filtering of TCP options.
        Creates and appends a new TcpOptionFilterList; an existing list with the same
        short name is returned unchanged.
        """
        if not self.IsElementExists(short_name, TcpOptionFilterList):
            tcp_filter_list = TcpOptionFilterList(self, short_name)
            self.addElement(tcp_filter_list)
            self.tcpOptionFilterLists.append(tcp_filter_list)
        return self.getElement(short_name, TcpOptionFilterList)

    def getTcpOptionFilterLists(self) -> List[TcpOptionFilterList]:
        """Collection of white lists for the filtering of TCP options."""
        return self.tcpOptionFilterLists
