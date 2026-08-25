# This module contains AUTOSAR System Template classes for Ethernet communication
# It defines socket connections, connection bundles, and service instances for Ethernet networking

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Boolean, Identifier, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import TpConnectionIdent
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Describable, Referrable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerFdConfiguration,
    CanControllerXlConfiguration,
    CanControllerXlConfigurationRequirements,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement


class SocketConnection(Describable):
    """
    The SoAd serves as a (De)Multiplexer between different PDU sources and the TCP/IP stack.
    """

    # SocketConnection method parity checklist (XSD-only class — obsolete, no R23-11 PDF table; Rule 0002:
    # attributes derived from the AUTOSAR_00052.xsd SOCKET-CONNECTION group; no # Spec line, no marker):
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAllowedIPv6ExtHeadersRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAllowedIPv6ExtHeadersRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAllowedTcpOptionsRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAllowedTcpOptionsRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAutosarConnector                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAutosarConnector                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getClientIpAddrFromConnectionRequest  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setClientIpAddrFromConnectionRequest  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getClientPortFromConnectionRequest    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setClientPortFromConnectionRequest    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getClientPortRef                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setClientPortRef                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDoIpSourceAddressRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDoIpSourceAddressRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDoIpTargetAddressRef               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDoIpTargetAddressRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIdent                              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIdent                              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLocalPortRef                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLocalPortRef                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNPduRef                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNPduRef                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPdus                               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addPdu                                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPduCollectionMaxBufferSize         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPduCollectionMaxBufferSize         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPduCollectionTimeout               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPduCollectionTimeout               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRemotePortRef                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRemotePortRef                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRuntimeIpAddressConfiguration      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRuntimeIpAddressConfiguration      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRuntimePortConfiguration           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRuntimePortConfiguration           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getShortLabel                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setShortLabel                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Reference to a list of IPv6 Extension Headers allowed for this SocketConnection. If no list is referenced all IPv6 Extension Headers are allowed and processed.
        self.allowedIPv6ExtHeadersRef: Optional[RefType] = None

        # Reference to a list of TCP options allowed for this SocketConnection.
        self.allowedTcpOptionsRef: Optional[RefType] = None

        # This attribute is deprecated and will be removed in future.
        self.autosarConnector: Optional[ARLiteral] = None

        # If set to true the Server "learns" the client IP address on connection request. This means that the statically configured IP Address of the related client shall be ignored. If set to false the Server only accepts statically configured IP address, e.g. 192.168.1.2. This means that the statically configured IP Address of the Client shall be used.
        self.clientIpAddrFromConnectionRequest: Optional[Boolean] = None

        # If set to true the Server "learns" the client Port on connection request. This means that the statically configured Port of the related client shall be ignored. If set to false the Server only accepts statically configured Port. This means that the statically configured Port of the Client shall be used.
        self.clientPortFromConnectionRequest: Optional[Boolean] = None

        # Client Port for TCP/UDP connection in an abstract communication sense. The client is the major requester of the communication. Please note that the client may also produce data.
        self.clientPortRef: Optional[RefType] = None

        # The logical DoIP address of the source entity. This optional reference shall only be used for DoIP (Diagnosis over IP).
        self.doIpSourceAddressRef: Optional[RefType] = None

        # The logical DoIP address of the target entity. This optional reference shall only be used for DoIP (Diagnosis over IP).
        self.doIpTargetAddressRef: Optional[RefType] = None

        # This adds the ability to become referrable to SocketConnection.
        self.ident: Optional[TpConnectionIdent] = None

        # This reference is obsolete and will be removed in the future. The serverPort reference in SocketConnectionBundle shall be used instead. Old description: Local Port for TCP/UDP connection.
        self.localPortRef: Optional[RefType] = None

        # Reference to data packets that are transmitted over Ethernet. Each data packet can contain multiple IPdus.
        self.nPduRef: Optional[RefType] = None

        # PDUs handed over by the PDU Router (Transmission over the Ethernet) or PDUs handed over by SoAd (Reception over Ethernet). Multiple IPdus can be transmitted over one socket connection.
        self.pdus: List[SocketConnectionIpduIdentifier] = []

        # Defines the maximum buffer size in Byte which shall be filled before a socket with Pdu collection enabled shall be transmitted to the lower layer.
        self.pduCollectionMaxBufferSize: Optional[PositiveInteger] = None

        # Defines the time in seconds which shall pass before a socket with Pdu collection enabled shall be transmitted to the lower layer after the first Pdu has been put into the socket buffer.
        self.pduCollectionTimeout: Optional[TimeValue] = None

        # This reference is obsolete and will be removed in the future. The clientPort reference shall be used instead. Old description: Remote Port for TCP/UDP connection. May be different for each Frame or use the same remote port. In second case headerId attribute needs to be considered.
        self.remotePortRef: Optional[RefType] = None

        # This attribute determines which protocol is used by the client to obtain the IP Address information. If this attribute is not set to none the value determines the service used by the client to obtain the IP Address information for the SocketConnection. If this attribute is set to none the client used the statically configured IP Address information.
        self.runtimeIpAddressConfiguration: Optional[ARLiteral] = None

        # This attribute determines which protocol is used by the client to obtain the Port information. If this attribute is not set to none the value determines the service used by the client to obtain the Port information for the SocketConnection. If this attribute is set to none the client uses the statically configured Port information.
        self.runtimePortConfiguration: Optional[ARLiteral] = None

        # This attribute specifies an identifying shortName for the SocketConnection. It shall be unique within its context.
        self.shortLabel: Optional[Identifier] = None

        # This attribute is deprecated and will be removed in future.
        self.socketProtocol: Optional[ARLiteral] = None

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

    def getAutosarConnector(self) -> Optional[ARLiteral]:
        """This attribute is deprecated and will be removed in future."""
        return self.autosarConnector

    def setAutosarConnector(self, value: Optional[ARLiteral]) -> "SocketConnection":
        """
        This attribute is deprecated and will be removed in future.
        A None value is a no-op and does not overwrite an existing autosarConnector.
        """
        if value is not None:
            self.autosarConnector = value
        return self

    def getClientIpAddrFromConnectionRequest(self) -> Optional[Boolean]:
        """If set to true the Server \"learns\" the client IP address on connection request. This means that the statically configured IP Address of the related client shall be ignored. If set to false the Server only accepts statically configured IP address, e.g. 192.168.1.2. This means that the statically configured IP Address of the Client shall be used."""
        return self.clientIpAddrFromConnectionRequest

    def setClientIpAddrFromConnectionRequest(self, value: Optional[Boolean]) -> "SocketConnection":
        """
        If set to true the Server \"learns\" the client IP address on connection request. This means that the statically configured IP Address of the related client shall be ignored. If set to false the Server only accepts statically configured IP address, e.g. 192.168.1.2. This means that the statically configured IP Address of the Client shall be used.
        A None value is a no-op and does not overwrite an existing clientIpAddrFromConnectionRequest.
        """
        if value is not None:
            self.clientIpAddrFromConnectionRequest = value
        return self

    def getClientPortFromConnectionRequest(self) -> Optional[Boolean]:
        """If set to true the Server \"learns\" the client Port on connection request. This means that the statically configured Port of the related client shall be ignored. If set to false the Server only accepts statically configured Port. This means that the statically configured Port of the Client shall be used."""
        return self.clientPortFromConnectionRequest

    def setClientPortFromConnectionRequest(self, value: Optional[Boolean]) -> "SocketConnection":
        """
        If set to true the Server \"learns\" the client Port on connection request. This means that the statically configured Port of the related client shall be ignored. If set to false the Server only accepts statically configured Port. This means that the statically configured Port of the Client shall be used.
        A None value is a no-op and does not overwrite an existing clientPortFromConnectionRequest.
        """
        if value is not None:
            self.clientPortFromConnectionRequest = value
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

    def getDoIpSourceAddressRef(self) -> Optional[RefType]:
        """The logical DoIP address of the source entity. This optional reference shall only be used for DoIP (Diagnosis over IP)."""
        return self.doIpSourceAddressRef

    def setDoIpSourceAddressRef(self, value: Optional[RefType]) -> "SocketConnection":
        """
        The logical DoIP address of the source entity. This optional reference shall only be used for DoIP (Diagnosis over IP).
        A None value is a no-op and does not overwrite an existing doIpSourceAddressRef.
        """
        if value is not None:
            self.doIpSourceAddressRef = value
        return self

    def getDoIpTargetAddressRef(self) -> Optional[RefType]:
        """The logical DoIP address of the target entity. This optional reference shall only be used for DoIP (Diagnosis over IP)."""
        return self.doIpTargetAddressRef

    def setDoIpTargetAddressRef(self, value: Optional[RefType]) -> "SocketConnection":
        """
        The logical DoIP address of the target entity. This optional reference shall only be used for DoIP (Diagnosis over IP).
        A None value is a no-op and does not overwrite an existing doIpTargetAddressRef.
        """
        if value is not None:
            self.doIpTargetAddressRef = value
        return self

    def getIdent(self) -> Optional[TpConnectionIdent]:
        """This adds the ability to become referrable to SocketConnection."""
        return self.ident

    def setIdent(self, value: Optional[TpConnectionIdent]) -> "SocketConnection":
        """
        This adds the ability to become referrable to SocketConnection.
        A None value is a no-op and does not overwrite an existing ident.
        """
        if value is not None:
            self.ident = value
        return self

    def getLocalPortRef(self) -> Optional[RefType]:
        """This reference is obsolete and will be removed in the future. The serverPort reference in SocketConnectionBundle shall be used instead. Old description: Local Port for TCP/UDP connection."""
        return self.localPortRef

    def setLocalPortRef(self, value: Optional[RefType]) -> "SocketConnection":
        """
        This reference is obsolete and will be removed in the future. The serverPort reference in SocketConnectionBundle shall be used instead. Old description: Local Port for TCP/UDP connection.
        A None value is a no-op and does not overwrite an existing localPortRef.
        """
        if value is not None:
            self.localPortRef = value
        return self

    def getNPduRef(self) -> Optional[RefType]:
        """Reference to data packets that are transmitted over Ethernet. Each data packet can contain multiple IPdus."""
        return self.nPduRef

    def setNPduRef(self, value: Optional[RefType]) -> "SocketConnection":
        """
        Reference to data packets that are transmitted over Ethernet. Each data packet can contain multiple IPdus.
        A None value is a no-op and does not overwrite an existing nPduRef.
        """
        if value is not None:
            self.nPduRef = value
        return self

    def getPdus(self) -> List["SocketConnectionIpduIdentifier"]:
        """PDUs handed over by the PDU Router (Transmission over the Ethernet) or PDUs handed over by SoAd (Reception over Ethernet). Multiple IPdus can be transmitted over one socket connection."""
        return self.pdus

    def addPdu(self, value: Optional["SocketConnectionIpduIdentifier"]) -> "SocketConnection":
        """
        PDUs handed over by the PDU Router (Transmission over the Ethernet) or PDUs handed over by SoAd (Reception over Ethernet). Multiple IPdus can be transmitted over one socket connection.
        A None value is a no-op and does not append to pdus.
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

    def getRemotePortRef(self) -> Optional[RefType]:
        """This reference is obsolete and will be removed in the future. The clientPort reference shall be used instead. Old description: Remote Port for TCP/UDP connection. May be different for each Frame or use the same remote port. In second case headerId attribute needs to be considered."""
        return self.remotePortRef

    def setRemotePortRef(self, value: Optional[RefType]) -> "SocketConnection":
        """
        This reference is obsolete and will be removed in the future. The clientPort reference shall be used instead. Old description: Remote Port for TCP/UDP connection. May be different for each Frame or use the same remote port. In second case headerId attribute needs to be considered.
        A None value is a no-op and does not overwrite an existing remotePortRef.
        """
        if value is not None:
            self.remotePortRef = value
        return self

    def getRuntimeIpAddressConfiguration(self) -> Optional[ARLiteral]:
        """This attribute determines which protocol is used by the client to obtain the IP Address information. If this attribute is not set to none the value determines the service used by the client to obtain the IP Address information for the SocketConnection. If this attribute is set to none the client used the statically configured IP Address information."""
        return self.runtimeIpAddressConfiguration

    def setRuntimeIpAddressConfiguration(self, value: Optional[ARLiteral]) -> "SocketConnection":
        """
        This attribute determines which protocol is used by the client to obtain the IP Address information. If this attribute is not set to none the value determines the service used by the client to obtain the IP Address information for the SocketConnection. If this attribute is set to none the client used the statically configured IP Address information.
        A None value is a no-op and does not overwrite an existing runtimeIpAddressConfiguration.
        """
        if value is not None:
            self.runtimeIpAddressConfiguration = value
        return self

    def getRuntimePortConfiguration(self) -> Optional[ARLiteral]:
        """This attribute determines which protocol is used by the client to obtain the Port information. If this attribute is not set to none the value determines the service used by the client to obtain the Port information for the SocketConnection. If this attribute is set to none the client uses the statically configured Port information."""
        return self.runtimePortConfiguration

    def setRuntimePortConfiguration(self, value: Optional[ARLiteral]) -> "SocketConnection":
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

    def getSocketProtocol(self) -> Optional[ARLiteral]:
        """This attribute is deprecated and will be removed in future."""
        return self.socketProtocol

    def setSocketProtocol(self, value: Optional[ARLiteral]) -> "SocketConnection":
        """
        This attribute is deprecated and will be removed in future.
        A None value is a no-op and does not overwrite an existing socketProtocol.
        """
        if value is not None:
            self.socketProtocol = value
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


class CanControllerConfiguration(ARObject):
    """
    CAN 2.0 configuration parameters for the CAN XL controller.

    Placeholder for the AUTOSAR CAN-CONTROLLER-CONFIGURATION meta-class
    (AUTOSAR_CP_TPS_SystemTemplate, Table 3.14). The inner attributes
    (propSeg, syncJumpWidth, timeSeg1, timeSeg2) are not yet modeled; this
    class is provided so CanXlProps.canConfig can be referenced. To be fully
    synced in a later pass.
    """

    def __init__(self):
        super().__init__()


class CanXlProps(ARElement):
    """
    This meta-class is used to configure Machine specific CAN XL attributes.
    """

    # CanXlProps method parity checklist:
    # Spec: AUTOSAR_AP_TPS_SystemDesign (AdaptivePlatform), class CAN-XL-PROPS, p.n/a (source: AUTOSAR_00052.xsd)
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCanBaudrate                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanBaudrate                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanConfig                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanConfig                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanFdBaudrate               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanFdBaudrate               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanFdConfig                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanFdConfig                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanXlBaudrate               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanXlBaudrate               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanXlConfig                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanXlConfig                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCanXlConfigReqs             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setCanXlConfigReqs             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies the data segment CAN 2.0 baud rate of the CAN XL controller in bits/s.
        self.canBaudrate: Optional[PositiveInteger] = None

        # CAN 2.0 configuration parameters for the CAN XL controller.
        self.canConfig: Optional[CanControllerConfiguration] = None

        # Specifies the data segment CAN FD baud rate of the CAN XL controller in bits/s.
        self.canFdBaudrate: Optional[PositiveInteger] = None

        # CAN FD configuration parameters for the CAN XL controller.
        self.canFdConfig: Optional[CanControllerFdConfiguration] = None

        # Specifies the data segment CAN XL baud rate of the CAN XL controller in bits/s.
        self.canXlBaudrate: Optional[PositiveInteger] = None

        # CAN XL configuration parameters for the CAN XL controller.
        self.canXlConfig: Optional[CanControllerXlConfiguration] = None

        # CAN XL configuration parameter requirements for the CAN XL controller.
        self.canXlConfigReqs: Optional[CanControllerXlConfigurationRequirements] = None

    def getCanBaudrate(self) -> Optional[PositiveInteger]:
        """
        Specifies the data segment CAN 2.0 baud rate of the CAN XL controller in bits/s.
        """
        return self.canBaudrate

    def setCanBaudrate(self, value: Optional[PositiveInteger]) -> "CanXlProps":
        """
        Specifies the data segment CAN 2.0 baud rate of the CAN XL controller in bits/s.
        A None value is a no-op and does not overwrite an existing canBaudrate.
        """
        if value is not None:
            self.canBaudrate = value
        return self

    def getCanConfig(self) -> Optional[CanControllerConfiguration]:
        """
        CAN 2.0 configuration parameters for the CAN XL controller.
        """
        return self.canConfig

    def setCanConfig(self, value: Optional[CanControllerConfiguration]) -> "CanXlProps":
        """
        CAN 2.0 configuration parameters for the CAN XL controller.
        A None value is a no-op and does not overwrite an existing canConfig.
        """
        if value is not None:
            self.canConfig = value
        return self

    def getCanFdBaudrate(self) -> Optional[PositiveInteger]:
        """
        Specifies the data segment CAN FD baud rate of the CAN XL controller in bits/s.
        """
        return self.canFdBaudrate

    def setCanFdBaudrate(self, value: Optional[PositiveInteger]) -> "CanXlProps":
        """
        Specifies the data segment CAN FD baud rate of the CAN XL controller in bits/s.
        A None value is a no-op and does not overwrite an existing canFdBaudrate.
        """
        if value is not None:
            self.canFdBaudrate = value
        return self

    def getCanFdConfig(self) -> Optional[CanControllerFdConfiguration]:
        """
        CAN FD configuration parameters for the CAN XL controller.
        """
        return self.canFdConfig

    def setCanFdConfig(self, value: Optional[CanControllerFdConfiguration]) -> "CanXlProps":
        """
        CAN FD configuration parameters for the CAN XL controller.
        A None value is a no-op and does not overwrite an existing canFdConfig.
        """
        if value is not None:
            self.canFdConfig = value
        return self

    def getCanXlBaudrate(self) -> Optional[PositiveInteger]:
        """
        Specifies the data segment CAN XL baud rate of the CAN XL controller in bits/s.
        """
        return self.canXlBaudrate

    def setCanXlBaudrate(self, value: Optional[PositiveInteger]) -> "CanXlProps":
        """
        Specifies the data segment CAN XL baud rate of the CAN XL controller in bits/s.
        A None value is a no-op and does not overwrite an existing canXlBaudrate.
        """
        if value is not None:
            self.canXlBaudrate = value
        return self

    def getCanXlConfig(self) -> Optional[CanControllerXlConfiguration]:
        """
        CAN XL configuration parameters for the CAN XL controller.
        """
        return self.canXlConfig

    def setCanXlConfig(self, value: Optional[CanControllerXlConfiguration]) -> "CanXlProps":
        """
        CAN XL configuration parameters for the CAN XL controller.
        A None value is a no-op and does not overwrite an existing canXlConfig.
        """
        if value is not None:
            self.canXlConfig = value
        return self

    def getCanXlConfigReqs(self) -> Optional[CanControllerXlConfigurationRequirements]:
        """
        CAN XL configuration parameter requirements for the CAN XL controller.
        """
        return self.canXlConfigReqs

    def setCanXlConfigReqs(self, value: Optional[CanControllerXlConfigurationRequirements]) -> "CanXlProps":
        """
        CAN XL configuration parameter requirements for the CAN XL controller.
        A None value is a no-op and does not overwrite an existing canXlConfigReqs.
        """
        if value is not None:
            self.canXlConfigReqs = value
        return self
