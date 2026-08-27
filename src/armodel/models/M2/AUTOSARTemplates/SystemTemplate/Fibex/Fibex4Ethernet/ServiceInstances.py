# This module contains AUTOSAR System Template classes for service instances
# It defines consumed and provided service instances, application endpoints, and SOAD configurations

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AnyServiceInstanceId,
    AnyVersionString,
    AREnum,
    Boolean,
    PositiveInteger,
    RefType,
    String,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue import TagWithOptionalValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel import SocketConnection, SocketConnectionBundle
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import ApplicationEndpoint, RequestResponseDelay, SdClientConfig


class TransportProtocolConfiguration(ARObject, ABC):
    """
    Abstract base class for transport protocol configurations,
    defining the common properties and behavior for different
    transport protocols (TCP, UDP, etc.) used in service-oriented
    communication.
    """

    # TransportProtocolConfiguration method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is TransportProtocolConfiguration:
            raise TypeError("TransportProtocolConfiguration is an abstract class.")

        super().__init__()


class GenericTp(TransportProtocolConfiguration):
    """
    Defines generic transport protocol configuration properties,
    including address and technology specifications for custom
    transport protocol implementations.
    """

    # GenericTp method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getTpAddress                 [x] impl  [ ] docstring  [ ] test
    # [ ] setTpAddress                 [x] impl  [ ] docstring  [ ] test
    # [ ] getTpTechnology              [x] impl  [ ] docstring  [ ] test
    # [ ] setTpTechnology              [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.tpAddress: String = None
        self.tpTechnology: String = None

    def getTpAddress(self):
        return self.tpAddress

    def setTpAddress(self, value):
        self.tpAddress = value
        return self

    def getTpTechnology(self):
        return self.tpTechnology

    def setTpTechnology(self, value):
        self.tpTechnology = value
        return self


class TcpUdpConfig(TransportProtocolConfiguration, ABC):
    """
    Abstract base class for TCP and UDP transport protocol configurations,
    defining common properties for both connection-oriented and
    connectionless transport protocols.
    """

    # TcpUdpConfig method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is TcpUdpConfig:
            raise TypeError("TcpUdpConfig is an abstract class.")

        super().__init__()


class TpPort(ARObject):
    """
    Defines properties for a transport protocol port, including
    port number and dynamic assignment capabilities for network
    communication endpoints.
    """

    # TpPort method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDynamicallyAssigned       [x] impl  [ ] docstring  [ ] test
    # [ ] setDynamicallyAssigned       [x] impl  [ ] docstring  [ ] test
    # [ ] getPortNumber                [x] impl  [ ] docstring  [ ] test
    # [ ] setPortNumber                [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.dynamicallyAssigned: Boolean = None
        self.portNumber: PositiveInteger = None

    def getDynamicallyAssigned(self):
        return self.dynamicallyAssigned

    def setDynamicallyAssigned(self, value):
        self.dynamicallyAssigned = value
        return self

    def getPortNumber(self):
        return self.portNumber

    def setPortNumber(self, value):
        self.portNumber = value
        return self


class UdpTp(TcpUdpConfig):
    """
    Defines UDP (User Datagram Protocol) transport protocol configuration,
    specifying UDP-specific port configuration for unreliable but fast
    datagram-based communication services.
    """

    # UdpTp method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getUdpTpPort                 [x] impl  [ ] docstring  [ ] test
    # [ ] setUdpTpPort                 [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.udpTpPort: TpPort = None

    def getUdpTpPort(self):
        return self.udpTpPort

    def setUdpTpPort(self, value):
        self.udpTpPort = value
        return self


class TcpTp(TcpUdpConfig):
    """
    Defines TCP (Transmission Control Protocol) transport protocol configuration,
    specifying TCP-specific properties such as keep-alive settings, retransmission
    timeouts, and flow control parameters for reliable connection-oriented communication.
    """

    # TcpTp method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getKeepAliveInterval         [x] impl  [ ] docstring  [ ] test
    # [ ] setKeepAliveInterval         [x] impl  [ ] docstring  [ ] test
    # [ ] getKeepAliveProbesMax        [x] impl  [ ] docstring  [ ] test
    # [ ] setKeepAliveProbesMax        [x] impl  [ ] docstring  [ ] test
    # [ ] getKeepAlives                [x] impl  [ ] docstring  [ ] test
    # [ ] setKeepAlives                [x] impl  [ ] docstring  [ ] test
    # [ ] getKeepAliveTime             [x] impl  [ ] docstring  [ ] test
    # [ ] setKeepAliveTime             [x] impl  [ ] docstring  [ ] test
    # [ ] getNaglesAlgorithm           [x] impl  [ ] docstring  [ ] test
    # [ ] setNaglesAlgorithm           [x] impl  [ ] docstring  [ ] test
    # [ ] getReceiveWindowMin          [x] impl  [ ] docstring  [ ] test
    # [ ] setReceiveWindowMin          [x] impl  [ ] docstring  [ ] test
    # [ ] getTcpRetransmissionTimeout  [x] impl  [ ] docstring  [ ] test
    # [ ] setTcpRetransmissionTimeout  [x] impl  [ ] docstring  [ ] test
    # [ ] getTcpTpPort                 [x] impl  [ ] docstring  [ ] test
    # [ ] setTcpTpPort                 [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.keepAliveInterval: TimeValue = None
        self.keepAliveProbesMax: PositiveInteger = None
        self.keepAlives: Boolean = None
        self.keepAliveTime: TimeValue = None
        self.naglesAlgorithm: Boolean = None
        self.receiveWindowMin: PositiveInteger = None
        self.tcpRetransmissionTimeout: TimeValue = None
        self.tcpTpPort: TpPort = None

    def getKeepAliveInterval(self):
        return self.keepAliveInterval

    def setKeepAliveInterval(self, value):
        self.keepAliveInterval = value
        return self

    def getKeepAliveProbesMax(self):
        return self.keepAliveProbesMax

    def setKeepAliveProbesMax(self, value):
        self.keepAliveProbesMax = value
        return self

    def getKeepAlives(self):
        return self.keepAlives

    def setKeepAlives(self, value):
        self.keepAlives = value
        return self

    def getKeepAliveTime(self):
        return self.keepAliveTime

    def setKeepAliveTime(self, value):
        self.keepAliveTime = value
        return self

    def getNaglesAlgorithm(self):
        return self.naglesAlgorithm

    def setNaglesAlgorithm(self, value):
        self.naglesAlgorithm = value
        return self

    def getReceiveWindowMin(self):
        return self.receiveWindowMin

    def setReceiveWindowMin(self, value):
        self.receiveWindowMin = value
        return self

    def getTcpRetransmissionTimeout(self):
        return self.tcpRetransmissionTimeout

    def setTcpRetransmissionTimeout(self, value):
        self.tcpRetransmissionTimeout = value
        return self

    def getTcpTpPort(self):
        return self.tcpTpPort

    def setTcpTpPort(self, value):
        self.tcpTpPort = value
        return self


class AbstractServiceInstance(Identifiable, ABC):
    """It is possible to specify additional information about the AbstractServiceInstance with the Capability Record that allows to transport arbitrary configuration strings (key/value pairs). This allows to encode additional information like the name of a service or its configuration."""

    # AbstractServiceInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.158, p.477
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addCapabilityRecord             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCapabilityRecords            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getMajorVersion                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMajorVersion                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMethodActivationRoutingGroup [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMethodActivationRoutingGroup [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addRoutingGroupRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRoutingGroupRefs             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractServiceInstance:
            raise TypeError("AbstractServiceInstance is an abstract class.")

        super().__init__(parent, short_name)

        # A sequence of records to store arbitrary name/value pairs conveying additional information about the named service.
        self.capabilityRecords: List[TagWithOptionalValue] = []

        # Major Version of the ServiceInterface. Value can be set to a number that represents the Major Version of the service.
        self.majorVersion: Optional[PositiveInteger] = None

        # The ServiceDiscovery module is able to activate and deactivate the PDU routing for ClientServerOperations (SOME/IP methods).
        self.methodActivationRoutingGroup: Optional[PduActivationRoutingGroup] = None

        # The ServiceDiscovery module is able to activate and deactivate the PDU routing from and to TCP/IP-sockets.
        self.routingGroupRefs: List[RefType] = []

    def addCapabilityRecord(self, value: Optional[TagWithOptionalValue]) -> "AbstractServiceInstance":
        """
        A sequence of records to store arbitrary name/value pairs conveying additional information about the named service.
        A None value is a no-op and does not append to capabilityRecords.
        """
        if value is not None:
            self.capabilityRecords.append(value)
        return self

    def getCapabilityRecords(self) -> List[TagWithOptionalValue]:
        """A sequence of records to store arbitrary name/value pairs conveying additional information about the named service."""
        return self.capabilityRecords

    def getMajorVersion(self) -> Optional[PositiveInteger]:
        """Major Version of the ServiceInterface. Value can be set to a number that represents the Major Version of the service."""
        return self.majorVersion

    def setMajorVersion(self, value: Optional[PositiveInteger]) -> "AbstractServiceInstance":
        """
        Major Version of the ServiceInterface. Value can be set to a number that represents the Major Version of the service.
        A None value is a no-op and does not overwrite an existing majorVersion.
        """
        if value is not None:
            self.majorVersion = value
        return self

    def getMethodActivationRoutingGroup(self) -> Optional["PduActivationRoutingGroup"]:
        """The ServiceDiscovery module is able to activate and deactivate the PDU routing for ClientServerOperations (SOME/IP methods)."""
        return self.methodActivationRoutingGroup

    def setMethodActivationRoutingGroup(self, value: Optional["PduActivationRoutingGroup"]) -> "AbstractServiceInstance":
        """
        The ServiceDiscovery module is able to activate and deactivate the PDU routing for ClientServerOperations (SOME/IP methods).
        A None value is a no-op and does not overwrite an existing methodActivationRoutingGroup.
        """
        if value is not None:
            self.methodActivationRoutingGroup = value
        return self

    def addRoutingGroupRef(self, value: Optional[RefType]) -> "AbstractServiceInstance":
        """
        The ServiceDiscovery module is able to activate and deactivate the PDU routing from and to TCP/IP-sockets.
        A None value is a no-op and does not append to routingGroupRefs.
        """
        if value is not None:
            self.routingGroupRefs.append(value)
        return self

    def getRoutingGroupRefs(self) -> List[RefType]:
        """The ServiceDiscovery module is able to activate and deactivate the PDU routing from and to TCP/IP-sockets."""
        return self.routingGroupRefs


class ConsumedEventGroup(Identifiable):
    """This element represents an event-group to which the service consumer wants to subscribe."""

    # ConsumedEventGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.168, p.505
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getApplicationEndpointRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setApplicationEndpointRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAutoRequire                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAutoRequire                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEventGroupIdentifier        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEventGroupIdentifier        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addEventMulticastAddressRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEventMulticastAddressRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addPduActivationRoutingGroup   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPduActivationRoutingGroups  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getPriority                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPriority                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addRoutingGroupRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRoutingGroupRefs            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getSdClientConfig              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSdClientConfig              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSdClientTimerConfigRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSdClientTimerConfigRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Defines the application endpoint where the events of the event group are received in case of multicast reception.
        self.applicationEndpointRef: Optional[RefType] = None

        # Defines that this ConsumedEventGroup shall be requested (subscribed) as soon as the corresponding ConsumedServiceInstance is requested. This could be at ECU start, if ConsumedServiceInstance.autoRequire is set to TRUE or as soon as the ConsumedServiceInstance is requested by the application, if ConsumedService Instance.autoRequire is set to FALSE.
        self.autoRequire: Optional[Boolean] = None

        # EventGroup ID. Shall be unique within one system to allow service discovery.
        self.eventGroupIdentifier: Optional[PositiveInteger] = None

        # This reference defines the multicast address or a multicast address resource where the events of the event group are received. If the multicast address is determined via configuration and not at runtime via service discovery this reference points to the multicast address over which the events will be received. If the multicast address is determined at runtime via service discovery this reference shall be used to define the necessary local multicast address resources, i.e. RAM space in the TcpIp module in which the multicast address is stored at runtime. Please note that in this case the referenced address may be defined as ANY UDP port and ANY IP address since the multicast address will be received at runtime. If several multicast addresses are considered to be used the ConsumedEventGroup shall point to different ApplicationEndpoint objects to reserve the necessary resources in the configuration.
        self.eventMulticastAddressRefs: List[RefType] = []

        # The ServiceDiscovery module is able to activate and deactivate the PDU routing for receiving events.
        self.pduActivationRoutingGroups: List[PduActivationRoutingGroup] = []

        # Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed.
        self.priority: Optional[PositiveInteger] = None

        # The ServiceDiscovery module is able to activate and deactivate the PDU routing for receiving events.
        self.routingGroupRefs: List[RefType] = []

        # The readiness to receive events is defined by the Service Discovery of the ConsumedEventGroup. The Event Handler shall know about this announcement to decide about the submission of events. Therefore the Event Handler may be configured with Service-Discovery Client attributes.
        self.sdClientConfig: Optional[SdClientConfig] = None

        # Client Timing configuration settings that are EventGroup specific.
        self.sdClientTimerConfigRef: Optional[RefType] = None

    def getApplicationEndpointRef(self) -> Optional[RefType]:
        """Defines the application endpoint where the events of the event group are received in case of multicast reception."""
        return self.applicationEndpointRef

    def setApplicationEndpointRef(self, value: Optional[RefType]) -> "ConsumedEventGroup":
        """
        Defines the application endpoint where the events of the event group are received in case of multicast reception.
        A None value is a no-op and does not overwrite an existing applicationEndpointRef.
        """
        if value is not None:
            self.applicationEndpointRef = value
        return self

    def getAutoRequire(self) -> Optional[Boolean]:
        """Defines that this ConsumedEventGroup shall be requested (subscribed) as soon as the corresponding ConsumedServiceInstance is requested. This could be at ECU start, if ConsumedServiceInstance.autoRequire is set to TRUE or as soon as the ConsumedServiceInstance is requested by the application, if ConsumedService Instance.autoRequire is set to FALSE."""
        return self.autoRequire

    def setAutoRequire(self, value: Optional[Boolean]) -> "ConsumedEventGroup":
        """
        Defines that this ConsumedEventGroup shall be requested (subscribed) as soon as the corresponding ConsumedServiceInstance is requested. This could be at ECU start, if ConsumedServiceInstance.autoRequire is set to TRUE or as soon as the ConsumedServiceInstance is requested by the application, if ConsumedService Instance.autoRequire is set to FALSE.
        A None value is a no-op and does not overwrite an existing autoRequire.
        """
        if value is not None:
            self.autoRequire = value
        return self

    def getEventGroupIdentifier(self) -> Optional[PositiveInteger]:
        """EventGroup ID. Shall be unique within one system to allow service discovery."""
        return self.eventGroupIdentifier

    def setEventGroupIdentifier(self, value: Optional[PositiveInteger]) -> "ConsumedEventGroup":
        """
        EventGroup ID. Shall be unique within one system to allow service discovery.
        A None value is a no-op and does not overwrite an existing eventGroupIdentifier.
        """
        if value is not None:
            self.eventGroupIdentifier = value
        return self

    def addEventMulticastAddressRef(self, value: Optional[RefType]) -> "ConsumedEventGroup":
        """
        This reference defines the multicast address or a multicast address resource where the events of the event group are received. If the multicast address is determined via configuration and not at runtime via service discovery this reference points to the multicast address over which the events will be received. If the multicast address is determined at runtime via service discovery this reference shall be used to define the necessary local multicast address resources, i.e. RAM space in the TcpIp module in which the multicast address is stored at runtime. Please note that in this case the referenced address may be defined as ANY UDP port and ANY IP address since the multicast address will be received at runtime. If several multicast addresses are considered to be used the ConsumedEventGroup shall point to different ApplicationEndpoint objects to reserve the necessary resources in the configuration.
        A None value is a no-op and does not append to eventMulticastAddressRefs.
        """
        if value is not None:
            self.eventMulticastAddressRefs.append(value)
        return self

    def getEventMulticastAddressRefs(self) -> List[RefType]:
        """This reference defines the multicast address or a multicast address resource where the events of the event group are received. If the multicast address is determined via configuration and not at runtime via service discovery this reference points to the multicast address over which the events will be received. If the multicast address is determined at runtime via service discovery this reference shall be used to define the necessary local multicast address resources, i.e. RAM space in the TcpIp module in which the multicast address is stored at runtime. Please note that in this case the referenced address may be defined as ANY UDP port and ANY IP address since the multicast address will be received at runtime. If several multicast addresses are considered to be used the ConsumedEventGroup shall point to different ApplicationEndpoint objects to reserve the necessary resources in the configuration."""
        return self.eventMulticastAddressRefs

    def addPduActivationRoutingGroup(self, value: Optional["PduActivationRoutingGroup"]) -> "ConsumedEventGroup":
        """
        The ServiceDiscovery module is able to activate and deactivate the PDU routing for receiving events.
        A None value is a no-op and does not append to pduActivationRoutingGroups.
        """
        if value is not None:
            self.pduActivationRoutingGroups.append(value)
        return self

    def getPduActivationRoutingGroups(self) -> List["PduActivationRoutingGroup"]:
        """The ServiceDiscovery module is able to activate and deactivate the PDU routing for receiving events."""
        return self.pduActivationRoutingGroups

    def getPriority(self) -> Optional[PositiveInteger]:
        """Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed."""
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> "ConsumedEventGroup":
        """
        Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed.
        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self

    def addRoutingGroupRef(self, value: Optional[RefType]) -> "ConsumedEventGroup":
        """
        The ServiceDiscovery module is able to activate and deactivate the PDU routing for receiving events.
        A None value is a no-op and does not append to routingGroupRefs.
        """
        if value is not None:
            self.routingGroupRefs.append(value)
        return self

    def getRoutingGroupRefs(self) -> List[RefType]:
        """The ServiceDiscovery module is able to activate and deactivate the PDU routing for receiving events."""
        return self.routingGroupRefs

    def getSdClientConfig(self) -> Optional[SdClientConfig]:
        """The readiness to receive events is defined by the Service Discovery of the ConsumedEventGroup. The Event Handler shall know about this announcement to decide about the submission of events. Therefore the Event Handler may be configured with Service-Discovery Client attributes."""
        return self.sdClientConfig

    def setSdClientConfig(self, value: Optional[SdClientConfig]) -> "ConsumedEventGroup":
        """
        The readiness to receive events is defined by the Service Discovery of the ConsumedEventGroup. The Event Handler shall know about this announcement to decide about the submission of events. Therefore the Event Handler may be configured with Service-Discovery Client attributes.
        A None value is a no-op and does not overwrite an existing sdClientConfig.
        """
        if value is not None:
            self.sdClientConfig = value
        return self

    def getSdClientTimerConfigRef(self) -> Optional[RefType]:
        """Client Timing configuration settings that are EventGroup specific."""
        return self.sdClientTimerConfigRef

    def setSdClientTimerConfigRef(self, value: Optional[RefType]) -> "ConsumedEventGroup":
        """
        Client Timing configuration settings that are EventGroup specific.
        A None value is a no-op and does not overwrite an existing sdClientTimerConfigRef.
        """
        if value is not None:
            self.sdClientTimerConfigRef = value
        return self


class ServiceVersionAcceptanceKindEnum(AREnum):
    """
    Defined the possible acceptance kinds for required service instances.
    """

    # ServiceVersionAcceptanceKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.113, p.2057
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on ConsumedServiceInstance.versionDrivenFindBehavior

    # Search for ANY or specific minor version service instance and select either ALL returned service instances (in case of ANY) or exactly the specific minor version service instances defined in requiredMinorVersion. Tags: atp.EnumerationLiteralIndex=0
    EXACT_OR_ANY_MINOR_VERSION = "exactOrAnyMinorVersion"

    # Search for ANY minor version service instance and select only those service instances which have an equal or greater minor version than given in requiredMinorVersion. Tags: atp.EnumerationLiteralIndex=1
    MINIMUM_MINOR_VERSION = "minimumMinorVersion"

    def __init__(self):
        super().__init__(
            [
                ServiceVersionAcceptanceKindEnum.EXACT_OR_ANY_MINOR_VERSION,
                ServiceVersionAcceptanceKindEnum.MINIMUM_MINOR_VERSION,
            ]
        )


class UdpChecksumCalculationEnum(AREnum):
    """
    This enumeration defines the UDP checksum calculation.
    """

    # UdpChecksumCalculationEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.119, p.454
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on SocketAddress.udpChecksumHandling

    # Udp checksum handling shall be disabled Tags: atp.EnumerationLiteralIndex=1
    UDP_CHECKSUM_DISABLED = "udpChecksumDisabled"

    # Udp checksum handling shall be enabled Tags: atp.EnumerationLiteralIndex=0
    UDP_CHECKSUM_ENABLED = "udpChecksumEnabled"

    def __init__(self):
        super().__init__(
            [
                UdpChecksumCalculationEnum.UDP_CHECKSUM_ENABLED,
                UdpChecksumCalculationEnum.UDP_CHECKSUM_DISABLED,
            ]
        )


class EventGroupControlTypeEnum(AREnum):
    """
    Types of a RoutingGroups for the event communication.
    """

    # EventGroupControlTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.162, p.489
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on PduActivationRoutingGroup.eventGroupControlType

    # Activate the data path for unicast events and triggered unicast events that are sent out after a client got subscribed. Tags: atp.EnumerationLiteralIndex=0
    ACTIVATION_AND_TRIGGER_UNICAST = "activationAndTriggerUnicast"

    # Activate the data path for multicast events of an EventGroup. Tags: atp.EnumerationLiteralIndex=1
    ACTIVATION_MULTICAST = "activationMulticast"

    # Activate the data path for unicast events of an EventGroup. Tags: atp.EnumerationLiteralIndex=2
    ACTIVATION_UNICAST = "activationUnicast"

    # Activate the data path for triggered unicast events that are sent out after a client got subscribed. Tags: atp.EnumerationLiteralIndex=3
    TRIGGER_UNICAST = "triggerUnicast"

    def __init__(self):
        super().__init__(
            [
                EventGroupControlTypeEnum.ACTIVATION_AND_TRIGGER_UNICAST,
                EventGroupControlTypeEnum.ACTIVATION_MULTICAST,
                EventGroupControlTypeEnum.ACTIVATION_UNICAST,
                EventGroupControlTypeEnum.TRIGGER_UNICAST,
            ]
        )


class TcpRoleEnum(AREnum):
    """
    This enumeration defines whether a TCP node has the tcp server role or the client role.
    """

    # TcpRoleEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.135
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on StaticSocketConnection.tcpRole

    # Connects the client to a remote TCP host. Tags: atp.EnumerationLiteralIndex=0
    CONNECT = "connect"

    # Socket is put into the server mode (listen for connections). Tags: atp.EnumerationLiteralIndex=1
    LISTEN = "listen"

    def __init__(self):
        super().__init__(
            [
                TcpRoleEnum.CONNECT,
                TcpRoleEnum.LISTEN,
            ]
        )


class PduActivationRoutingGroup(Identifiable):
    """
    Group of Pdus that can be activated or deactivated for transmission over a socket connection.
    """

    # PduActivationRoutingGroup method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.161, p.489
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getEventGroupControlType        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setEventGroupControlType        [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getIPduIdentifierTcpRefs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addIPduIdentifierTcpRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIPduIdentifierUdpRefs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addIPduIdentifierUdpRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute defines the type of a RoutingGroup. There are RoutingGroups that activate the data path for unicast or multicast events of an event group. And there are RoutingGroups that activate the data path for initial events that are triggered, namely events that are sent out on the server side after a client got subscribed. Please note that this attribute is only valid for event communication (Sender Receiver communication) and shall be omitted in MethodActivationRoutingGroups.
        self.eventGroupControlType: Optional[EventGroupControlTypeEnum] = None

        # PduIdentifiers assigned for transmission over Tcp in case that the referencing PduActivationRoutingGroup is activated.
        self.iPduIdentifierTcpRefs: List[RefType] = []

        # PduIdentifiers assigned for transmission over Udp in case that the referencing PduActivationRoutingGroup is activated.
        self.iPduIdentifierUdpRefs: List[RefType] = []

    def getEventGroupControlType(self) -> Optional[EventGroupControlTypeEnum]:
        """This attribute defines the type of a RoutingGroup. There are RoutingGroups that activate the data path for unicast or multicast events of an event group. And there are RoutingGroups that activate the data path for initial events that are triggered, namely events that are sent out on the server side after a client got subscribed. Please note that this attribute is only valid for event communication (Sender Receiver communication) and shall be omitted in MethodActivationRoutingGroups."""
        return self.eventGroupControlType

    def setEventGroupControlType(self, value: Optional[EventGroupControlTypeEnum]) -> "PduActivationRoutingGroup":
        """
        This attribute defines the type of a RoutingGroup. There are RoutingGroups that activate the data path for unicast or multicast events of an event group. And there are RoutingGroups that activate the data path for initial events that are triggered, namely events that are sent out on the server side after a client got subscribed. Please note that this attribute is only valid for event communication (Sender Receiver communication) and shall be omitted in MethodActivationRoutingGroups.
        A None value is a no-op and does not overwrite an existing eventGroupControlType.
        """
        if value is not None:
            self.eventGroupControlType = value
        return self

    def getIPduIdentifierTcpRefs(self) -> List[RefType]:
        """PduIdentifiers assigned for transmission over Tcp in case that the referencing PduActivationRoutingGroup is activated."""
        return self.iPduIdentifierTcpRefs

    def addIPduIdentifierTcpRef(self, ref: Optional[RefType]) -> "PduActivationRoutingGroup":
        """
        PduIdentifiers assigned for transmission over Tcp in case that the referencing PduActivationRoutingGroup is activated.
        A None value is a no-op and does not append to iPduIdentifierTcpRefs.
        """
        if ref is not None:
            self.iPduIdentifierTcpRefs.append(ref)
        return self

    def getIPduIdentifierUdpRefs(self) -> List[RefType]:
        """PduIdentifiers assigned for transmission over Udp in case that the referencing PduActivationRoutingGroup is activated."""
        return self.iPduIdentifierUdpRefs

    def addIPduIdentifierUdpRef(self, ref: Optional[RefType]) -> "PduActivationRoutingGroup":
        """
        PduIdentifiers assigned for transmission over Udp in case that the referencing PduActivationRoutingGroup is activated.
        A None value is a no-op and does not append to iPduIdentifierUdpRefs.
        """
        if ref is not None:
            self.iPduIdentifierUdpRefs.append(ref)
        return self


class StaticSocketConnection(Identifiable):
    """
    Definition of static SocketConnection between the Socket that is defined by the aggregating Socket Address and the remoteAddress.
    """

    # StaticSocketConnection method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.201, p.544
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getIPduIdentifierRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addIPduIdentifierRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRemoteAddressRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRemoteAddressRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTcpConnectTimeout        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTcpConnectTimeout        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTcpRole                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setTcpRole                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Assignment of IPduIdentifiers that are transmitted over the static SocketConnection.
        self.iPduIdentifierRefs: List[RefType] = []

        # RemoteAddress of the static SocketConnection.
        self.remoteAddressRef: Optional[RefType] = None

        # Specifies the time in seconds how long TCP connect attempts are repeated to reach SOAD_SOCON_ONLINE. This attribute is restricted to socket connection groups which are initiating a TCP connection and are under control of SoAd.
        self.tcpConnectTimeout: Optional[TimeValue] = None

        # Defines whether the local Address (that is aggregating the StaticSocketConnection) does a listen or a connect.
        self.tcpRole: Optional[TcpRoleEnum] = None

    def getIPduIdentifierRefs(self) -> List[RefType]:
        """Assignment of IPduIdentifiers that are transmitted over the static SocketConnection."""
        return self.iPduIdentifierRefs

    def addIPduIdentifierRef(self, ref: Optional[RefType]) -> "StaticSocketConnection":
        """
        Assignment of IPduIdentifiers that are transmitted over the static SocketConnection.
        A None value is a no-op and does not append to iPduIdentifierRefs.
        """
        if ref is not None:
            self.iPduIdentifierRefs.append(ref)
        return self

    def getRemoteAddressRef(self) -> Optional[RefType]:
        """RemoteAddress of the static SocketConnection."""
        return self.remoteAddressRef

    def setRemoteAddressRef(self, ref: Optional[RefType]) -> "StaticSocketConnection":
        """
        RemoteAddress of the static SocketConnection.
        A None value is a no-op and does not overwrite an existing remoteAddressRef.
        """
        if ref is not None:
            self.remoteAddressRef = ref
        return self

    def getTcpConnectTimeout(self) -> Optional[TimeValue]:
        """Specifies the time in seconds how long TCP connect attempts are repeated to reach SOAD_SOCON_ONLINE. This attribute is restricted to socket connection groups which are initiating a TCP connection and are under control of SoAd."""
        return self.tcpConnectTimeout

    def setTcpConnectTimeout(self, value: Optional[TimeValue]) -> "StaticSocketConnection":
        """
        Specifies the time in seconds how long TCP connect attempts are repeated to reach SOAD_SOCON_ONLINE. This attribute is restricted to socket connection groups which are initiating a TCP connection and are under control of SoAd.
        A None value is a no-op and does not overwrite an existing tcpConnectTimeout.
        """
        if value is not None:
            self.tcpConnectTimeout = value
        return self

    def getTcpRole(self) -> Optional[TcpRoleEnum]:
        """Defines whether the local Address (that is aggregating the StaticSocketConnection) does a listen or a connect."""
        return self.tcpRole

    def setTcpRole(self, value: Optional[TcpRoleEnum]) -> "StaticSocketConnection":
        """
        Defines whether the local Address (that is aggregating the StaticSocketConnection) does a listen or a connect.
        A None value is a no-op and does not overwrite an existing tcpRole.
        """
        if value is not None:
            self.tcpRole = value
        return self


class ConsumedServiceInstance(AbstractServiceInstance):
    """Service instances that are consumed by the ECU that is connected via the ApplicationEndpoint to a CommunicationConnector."""

    # ConsumedServiceInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.167, p.501
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addAllowedServiceProviderRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAllowedServiceProviderRefs            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getAutoRequire                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAutoRequire                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addBlocklistedVersion                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getBlocklistedVersions                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createConsumedEventGroup                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConsumedEventGroups                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getEventMulticastSubscriptionAddressRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEventMulticastSubscriptionAddressRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInstanceIdentifier                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setInstanceIdentifier                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addLocalUnicastAddressRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLocalUnicastAddressRefs               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getMinorVersion                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinorVersion                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getProvidedServiceInstanceRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setProvidedServiceInstanceRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addRemoteUnicastAddressRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRemoteUnicastAddressRefs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getSdClientConfig                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSdClientConfig                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSdClientTimerConfigRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSdClientTimerConfigRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getServiceIdentifier                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setServiceIdentifier                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVersionDrivenFindBehavior             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVersionDrivenFindBehavior             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # NetworkEndpoint on which the ProvidedServiceInstance that is communicating with this ConsumedService Instance is allowed to be located so that the ACL check in the ServiceDiscovery is successful and the connection is allowed to be established.
        self.allowedServiceProviderRefs: List[RefType] = []

        # Defines that this ConsumedServiceInstance shall be required (searched for) by the service discovery at ECU start.
        self.autoRequire: Optional[Boolean] = None

        # Collection of blocklisted versions
        self.blocklistedVersions: List[SomeipServiceVersion] = []

        # Selection of event-groups the consumer wants to subscribe for.
        self.consumedEventGroups: List[ConsumedEventGroup] = []

        # Multicast Address that is used by the client to subscribe to the server: This enables the multicast subscription feature.
        self.eventMulticastSubscriptionAddressRef: Optional[RefType] = None

        # This attribute represents the ability to describe the required service instance ID.
        self.instanceIdentifier: Optional[AnyServiceInstanceId] = None

        # The local address over which the CSI is consumed (udp, tcp or both).
        self.localUnicastAddressRefs: List[RefType] = []

        # Minor Version of the ServiceInterface. Value can be set to a number that represents the Minor Version of the searched service or to ANY.
        self.minorVersion: Optional[AnyVersionString] = None

        # Reference to a providedServiceInstance to get the instanceIdentifier information from the ProvidedService Instance.
        self.providedServiceInstanceRef: Optional[RefType] = None

        # This reference defines the remote address where the service provider is located. This reference shall ONLY be used if the remote address is determined from the configuration and not at runtime from the Service Discovery.
        self.remoteUnicastAddressRefs: List[RefType] = []

        # Service Discovery Client configuration.
        self.sdClientConfig: Optional[SdClientConfig] = None

        # Client specific configuration settings relevant for the SOME/IP service discovery.
        self.sdClientTimerConfigRef: Optional[RefType] = None

        # This attribute represents the ability to describe the SOME/ IP service ID that is searched.
        self.serviceIdentifier: Optional[PositiveInteger] = None

        # Defines the service discovery find behavior.
        self.versionDrivenFindBehavior: Optional[ServiceVersionAcceptanceKindEnum] = None

    def addAllowedServiceProviderRef(self, value: Optional[RefType]) -> "ConsumedServiceInstance":
        """
        NetworkEndpoint on which the ProvidedServiceInstance that is communicating with this ConsumedService Instance is allowed to be located so that the ACL check in the ServiceDiscovery is successful and the connection is allowed to be established.
        A None value is a no-op and does not append to allowedServiceProviderRefs.
        """
        if value is not None:
            self.allowedServiceProviderRefs.append(value)
        return self

    def getAllowedServiceProviderRefs(self) -> List[RefType]:
        """NetworkEndpoint on which the ProvidedServiceInstance that is communicating with this ConsumedService Instance is allowed to be located so that the ACL check in the ServiceDiscovery is successful and the connection is allowed to be established."""
        return self.allowedServiceProviderRefs

    def getAutoRequire(self) -> Optional[Boolean]:
        """Defines that this ConsumedServiceInstance shall be required (searched for) by the service discovery at ECU start."""
        return self.autoRequire

    def setAutoRequire(self, value: Optional[Boolean]) -> "ConsumedServiceInstance":
        """
        Defines that this ConsumedServiceInstance shall be required (searched for) by the service discovery at ECU start.
        A None value is a no-op and does not overwrite an existing autoRequire.
        """
        if value is not None:
            self.autoRequire = value
        return self

    def addBlocklistedVersion(self, value: Optional["SomeipServiceVersion"]) -> "ConsumedServiceInstance":
        """
        Collection of blocklisted versions
        A None value is a no-op and does not append to blocklistedVersions.
        """
        if value is not None:
            self.blocklistedVersions.append(value)
        return self

    def getBlocklistedVersions(self) -> List["SomeipServiceVersion"]:
        """Collection of blocklisted versions"""
        return self.blocklistedVersions

    def createConsumedEventGroup(self, short_name: str) -> "ConsumedEventGroup":
        """Selection of event-groups the consumer wants to subscribe for."""
        if not self.IsElementExists(short_name, ConsumedEventGroup):
            group = ConsumedEventGroup(self, short_name)
            self.addElement(group)
            self.consumedEventGroups.append(group)
        return self.getElement(short_name, ConsumedEventGroup)

    def getConsumedEventGroups(self) -> List["ConsumedEventGroup"]:
        """Selection of event-groups the consumer wants to subscribe for."""
        return self.consumedEventGroups

    def getEventMulticastSubscriptionAddressRef(self) -> Optional[RefType]:
        """Multicast Address that is used by the client to subscribe to the server: This enables the multicast subscription feature."""
        return self.eventMulticastSubscriptionAddressRef

    def setEventMulticastSubscriptionAddressRef(self, value: Optional[RefType]) -> "ConsumedServiceInstance":
        """
        Multicast Address that is used by the client to subscribe to the server: This enables the multicast subscription feature.
        A None value is a no-op and does not overwrite an existing eventMulticastSubscriptionAddressRef.
        """
        if value is not None:
            self.eventMulticastSubscriptionAddressRef = value
        return self

    def getInstanceIdentifier(self) -> Optional[AnyServiceInstanceId]:
        """This attribute represents the ability to describe the required service instance ID."""
        return self.instanceIdentifier

    def setInstanceIdentifier(self, value: Optional[AnyServiceInstanceId]) -> "ConsumedServiceInstance":
        """
        This attribute represents the ability to describe the required service instance ID.
        A None value is a no-op and does not overwrite an existing instanceIdentifier.
        """
        if value is not None:
            self.instanceIdentifier = value
        return self

    def addLocalUnicastAddressRef(self, value: Optional[RefType]) -> "ConsumedServiceInstance":
        """
        The local address over which the CSI is consumed (udp, tcp or both).
        A None value is a no-op and does not append to localUnicastAddressRefs.
        """
        if value is not None:
            self.localUnicastAddressRefs.append(value)
        return self

    def getLocalUnicastAddressRefs(self) -> List[RefType]:
        """The local address over which the CSI is consumed (udp, tcp or both)."""
        return self.localUnicastAddressRefs

    def getMinorVersion(self) -> Optional[AnyVersionString]:
        """Minor Version of the ServiceInterface. Value can be set to a number that represents the Minor Version of the searched service or to ANY."""
        return self.minorVersion

    def setMinorVersion(self, value: Optional[AnyVersionString]) -> "ConsumedServiceInstance":
        """
        Minor Version of the ServiceInterface. Value can be set to a number that represents the Minor Version of the searched service or to ANY.
        A None value is a no-op and does not overwrite an existing minorVersion.
        """
        if value is not None:
            self.minorVersion = value
        return self

    def getProvidedServiceInstanceRef(self) -> Optional[RefType]:
        """Reference to a providedServiceInstance to get the instanceIdentifier information from the ProvidedService Instance."""
        return self.providedServiceInstanceRef

    def setProvidedServiceInstanceRef(self, value: Optional[RefType]) -> "ConsumedServiceInstance":
        """
        Reference to a providedServiceInstance to get the instanceIdentifier information from the ProvidedService Instance.
        A None value is a no-op and does not overwrite an existing providedServiceInstanceRef.
        """
        if value is not None:
            self.providedServiceInstanceRef = value
        return self

    def addRemoteUnicastAddressRef(self, value: Optional[RefType]) -> "ConsumedServiceInstance":
        """
        This reference defines the remote address where the service provider is located. This reference shall ONLY be used if the remote address is determined from the configuration and not at runtime from the Service Discovery.
        A None value is a no-op and does not append to remoteUnicastAddressRefs.
        """
        if value is not None:
            self.remoteUnicastAddressRefs.append(value)
        return self

    def getRemoteUnicastAddressRefs(self) -> List[RefType]:
        """This reference defines the remote address where the service provider is located. This reference shall ONLY be used if the remote address is determined from the configuration and not at runtime from the Service Discovery."""
        return self.remoteUnicastAddressRefs

    def getSdClientConfig(self) -> Optional[SdClientConfig]:
        """Service Discovery Client configuration."""
        return self.sdClientConfig

    def setSdClientConfig(self, value: Optional[SdClientConfig]) -> "ConsumedServiceInstance":
        """
        Service Discovery Client configuration.
        A None value is a no-op and does not overwrite an existing sdClientConfig.
        """
        if value is not None:
            self.sdClientConfig = value
        return self

    def getSdClientTimerConfigRef(self) -> Optional[RefType]:
        """Client specific configuration settings relevant for the SOME/IP service discovery."""
        return self.sdClientTimerConfigRef

    def setSdClientTimerConfigRef(self, value: Optional[RefType]) -> "ConsumedServiceInstance":
        """
        Client specific configuration settings relevant for the SOME/IP service discovery.
        A None value is a no-op and does not overwrite an existing sdClientTimerConfigRef.
        """
        if value is not None:
            self.sdClientTimerConfigRef = value
        return self

    def getServiceIdentifier(self) -> Optional[PositiveInteger]:
        """This attribute represents the ability to describe the SOME/ IP service ID that is searched."""
        return self.serviceIdentifier

    def setServiceIdentifier(self, value: Optional[PositiveInteger]) -> "ConsumedServiceInstance":
        """
        This attribute represents the ability to describe the SOME/ IP service ID that is searched.
        A None value is a no-op and does not overwrite an existing serviceIdentifier.
        """
        if value is not None:
            self.serviceIdentifier = value
        return self

    def getVersionDrivenFindBehavior(self) -> Optional[ServiceVersionAcceptanceKindEnum]:
        """Defines the service discovery find behavior."""
        return self.versionDrivenFindBehavior

    def setVersionDrivenFindBehavior(self, value: Optional[ServiceVersionAcceptanceKindEnum]) -> "ConsumedServiceInstance":
        """
        Defines the service discovery find behavior.
        A None value is a no-op and does not overwrite an existing versionDrivenFindBehavior.
        """
        if value is not None:
            self.versionDrivenFindBehavior = value
        return self


class InitialSdDelayConfig(ARObject):
    """
    Configures initial delay parameters for Service Discovery (SD)
    operations, defining the timing behavior for initial service
    discovery attempts and repetitions.
    """

    # InitialSdDelayConfig method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getInitialDelayMaxValue      [x] impl  [ ] docstring  [ ] test
    # [ ] setInitialDelayMaxValue      [x] impl  [ ] docstring  [ ] test
    # [ ] getInitialDelayMinValue      [x] impl  [ ] docstring  [ ] test
    # [ ] setInitialDelayMinValue      [x] impl  [ ] docstring  [ ] test
    # [ ] getInitialRepetitionsBaseDelay [x] impl  [ ] docstring  [ ] test
    # [ ] setInitialRepetitionsBaseDelay [x] impl  [ ] docstring  [ ] test
    # [ ] getInitialRepetitionsMax     [x] impl  [ ] docstring  [ ] test
    # [ ] setInitialRepetitionsMax     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.initialDelayMaxValue: TimeValue = None
        self.initialDelayMinValue: TimeValue = None
        self.initialRepetitionsBaseDelay: TimeValue = None
        self.initialRepetitionsMax: PositiveInteger = None

    def getInitialDelayMaxValue(self):
        return self.initialDelayMaxValue

    def setInitialDelayMaxValue(self, value):
        if value is not None:
            self.initialDelayMaxValue = value
        return self

    def getInitialDelayMinValue(self):
        return self.initialDelayMinValue

    def setInitialDelayMinValue(self, value):
        if value is not None:
            self.initialDelayMinValue = value
        return self

    def getInitialRepetitionsBaseDelay(self):
        return self.initialRepetitionsBaseDelay

    def setInitialRepetitionsBaseDelay(self, value):
        if value is not None:
            self.initialRepetitionsBaseDelay = value
        return self

    def getInitialRepetitionsMax(self):
        return self.initialRepetitionsMax

    def setInitialRepetitionsMax(self, value):
        if value is not None:
            self.initialRepetitionsMax = value
        return self


class SomeipSdClientServiceInstanceConfig(ARElement):
    """Client specific settings that are relevant for the configuration of SOME/IP Service-Discovery. Tags: atp.recommendedPackage=SomeipSdTimingConfigs"""

    # SomeipSdClientServiceInstanceConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.117, p.2059
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getInitialFindBehavior       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setInitialFindBehavior       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getPriority                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setPriority                  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] getServiceFindTimeToLive     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setServiceFindTimeToLive     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Controls initial find behavior of clients.
        self.initialFindBehavior: Optional[InitialSdDelayConfig] = None

        # This attribute defines the VLAN frame priority for Service Discovery messages that result from RequiredSomeipServiceInstances that are referncing this SomeipSdClientServiceInstanceConfig (Find, SubscribeEventGroup, Stop SubscribeEventgroup). Values from 0 (best effort) to 7 (highest) are allowed.
        self.priority: Optional[PositiveInteger] = None

        # This attribute represents the ability to define the time in seconds the service find is valid. Note! The TTL value for FindService entries is not used and shall be ignored by the server service. This configuration is only kept for backward compatibility. Default value if not specified shall be 0xFFFFFF.
        self.serviceFindTimeToLive: Optional[PositiveInteger] = None

    def getInitialFindBehavior(self) -> Optional[InitialSdDelayConfig]:
        """Controls initial find behavior of clients."""
        return self.initialFindBehavior

    def setInitialFindBehavior(self, value: Optional[InitialSdDelayConfig]) -> "SomeipSdClientServiceInstanceConfig":
        """
        Controls initial find behavior of clients.
        A None value is a no-op and does not overwrite an existing initialFindBehavior.
        """
        if value is not None:
            self.initialFindBehavior = value
        return self

    def getPriority(self) -> Optional[PositiveInteger]:
        """This attribute defines the VLAN frame priority for Service Discovery messages that result from RequiredSomeipServiceInstances that are referncing this SomeipSdClientServiceInstanceConfig (Find, SubscribeEventGroup, Stop SubscribeEventgroup). Values from 0 (best effort) to 7 (highest) are allowed."""
        return self.priority

    def setPriority(self, value: Optional[PositiveInteger]) -> "SomeipSdClientServiceInstanceConfig":
        """
        This attribute defines the VLAN frame priority for Service Discovery messages that result from RequiredSomeipServiceInstances that are referncing this SomeipSdClientServiceInstanceConfig (Find, SubscribeEventGroup, Stop SubscribeEventgroup). Values from 0 (best effort) to 7 (highest) are allowed.
        A None value is a no-op and does not overwrite an existing priority.
        """
        if value is not None:
            self.priority = value
        return self

    def getServiceFindTimeToLive(self) -> Optional[PositiveInteger]:
        """This attribute represents the ability to define the time in seconds the service find is valid. Note! The TTL value for FindService entries is not used and shall be ignored by the server service. This configuration is only kept for backward compatibility. Default value if not specified shall be 0xFFFFFF."""
        return self.serviceFindTimeToLive

    def setServiceFindTimeToLive(self, value: Optional[PositiveInteger]) -> "SomeipSdClientServiceInstanceConfig":
        """
        This attribute represents the ability to define the time in seconds the service find is valid. Note! The TTL value for FindService entries is not used and shall be ignored by the server service. This configuration is only kept for backward compatibility. Default value if not specified shall be 0xFFFFFF.
        A None value is a no-op and does not overwrite an existing serviceFindTimeToLive.
        """
        if value is not None:
            self.serviceFindTimeToLive = value
        return self


class SomeipServiceVersion(ARObject):
    """This meta-class represents the ability to describe a version of a SOME/IP Service."""

    # SomeipServiceVersion method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table F.118, p.2059
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMajorVersion        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMajorVersion        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinorVersion        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinorVersion        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Major Version of the ServiceInterface. Tags: xml.sequenceOffset=10
        self.majorVersion: Optional[PositiveInteger] = None

        # Minor Version of the ServiceInterface. Tags: xml.sequenceOffset=20
        self.minorVersion: Optional[PositiveInteger] = None

    def getMajorVersion(self) -> Optional[PositiveInteger]:
        """Major Version of the ServiceInterface. Tags: xml.sequenceOffset=10"""
        return self.majorVersion

    def setMajorVersion(self, value: Optional[PositiveInteger]) -> "SomeipServiceVersion":
        """
        Major Version of the ServiceInterface. Tags: xml.sequenceOffset=10
        A None value is a no-op and does not overwrite an existing majorVersion.
        """
        if value is not None:
            self.majorVersion = value
        return self

    def getMinorVersion(self) -> Optional[PositiveInteger]:
        """Minor Version of the ServiceInterface. Tags: xml.sequenceOffset=20"""
        return self.minorVersion

    def setMinorVersion(self, value: Optional[PositiveInteger]) -> "SomeipServiceVersion":
        """
        Minor Version of the ServiceInterface. Tags: xml.sequenceOffset=20
        A None value is a no-op and does not overwrite an existing minorVersion.
        """
        if value is not None:
            self.minorVersion = value
        return self


class SomeipSdClientEventGroupTimingConfig(ARElement):
    """This meta-class is used to specify configuration related to service discovery in the context of an event group on SOME/IP. Tags: atp.recommendedPackage=SomeipSdTimingConfigs"""

    # SomeipSdClientEventGroupTimingConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.173, p.521
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getRequestResponseDelay               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRequestResponseDelay               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSubscribeEventgroupRetryDelay      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSubscribeEventgroupRetryDelay      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSubscribeEventgroupRetryMax        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSubscribeEventgroupRetryMax        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeToLive                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeToLive                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The Service Discovery shall delay answers to unicast messages triggered by multicast messages (e.g. Subscribe Eventgroup after Offer Service).
        self.requestResponseDelay: Optional[RequestResponseDelay] = None

        # This attribute defines the interval in seconds to re-trigger a subscription to a Eventgroup, if a retry to subscribe to a Eventgroup is configured (subscribeEventgroupRetryMax > 0).
        self.subscribeEventgroupRetryDelay: Optional[TimeValue] = None

        # This attribute define the maximum counts of retries to subscribe to an Eventgroup. If the value is set to 0 no retry shall be done. If the value is set to 255 the retry shall be done as along as the Eventgroup is requested and no SubscribeEventGroupAck was received.
        self.subscribeEventgroupRetryMax: Optional[PositiveInteger] = None

        # Defines the time in seconds the subscription of this event is expected by the client. this value is sent from the client to the server in the SD-subscribeEvent message.
        self.timeToLive: Optional[PositiveInteger] = None

    def getRequestResponseDelay(self) -> Optional[RequestResponseDelay]:
        """The Service Discovery shall delay answers to unicast messages triggered by multicast messages (e.g. Subscribe Eventgroup after Offer Service)."""
        return self.requestResponseDelay

    def setRequestResponseDelay(self, value: Optional[RequestResponseDelay]) -> "SomeipSdClientEventGroupTimingConfig":
        """
        The Service Discovery shall delay answers to unicast messages triggered by multicast messages (e.g. Subscribe Eventgroup after Offer Service).
        A None value is a no-op and does not overwrite an existing requestResponseDelay.
        """
        if value is not None:
            self.requestResponseDelay = value
        return self

    def getSubscribeEventgroupRetryDelay(self) -> Optional[TimeValue]:
        """This attribute defines the interval in seconds to re-trigger a subscription to a Eventgroup, if a retry to subscribe to a Eventgroup is configured (subscribeEventgroupRetryMax > 0)."""
        return self.subscribeEventgroupRetryDelay

    def setSubscribeEventgroupRetryDelay(self, value: Optional[TimeValue]) -> "SomeipSdClientEventGroupTimingConfig":
        """
        This attribute defines the interval in seconds to re-trigger a subscription to a Eventgroup, if a retry to subscribe to a Eventgroup is configured (subscribeEventgroupRetryMax > 0).
        A None value is a no-op and does not overwrite an existing subscribeEventgroupRetryDelay.
        """
        if value is not None:
            self.subscribeEventgroupRetryDelay = value
        return self

    def getSubscribeEventgroupRetryMax(self) -> Optional[PositiveInteger]:
        """This attribute define the maximum counts of retries to subscribe to an Eventgroup. If the value is set to 0 no retry shall be done. If the value is set to 255 the retry shall be done as along as the Eventgroup is requested and no SubscribeEventGroupAck was received."""
        return self.subscribeEventgroupRetryMax

    def setSubscribeEventgroupRetryMax(self, value: Optional[PositiveInteger]) -> "SomeipSdClientEventGroupTimingConfig":
        """
        This attribute define the maximum counts of retries to subscribe to an Eventgroup. If the value is set to 0 no retry shall be done. If the value is set to 255 the retry shall be done as along as the Eventgroup is requested and no SubscribeEventGroupAck was received.
        A None value is a no-op and does not overwrite an existing subscribeEventgroupRetryMax.
        """
        if value is not None:
            self.subscribeEventgroupRetryMax = value
        return self

    def getTimeToLive(self) -> Optional[PositiveInteger]:
        """Defines the time in seconds the subscription of this event is expected by the client. this value is sent from the client to the server in the SD-subscribeEvent message."""
        return self.timeToLive

    def setTimeToLive(self, value: Optional[PositiveInteger]) -> "SomeipSdClientEventGroupTimingConfig":
        """
        Defines the time in seconds the subscription of this event is expected by the client. this value is sent from the client to the server in the SD-subscribeEvent message.
        A None value is a no-op and does not overwrite an existing timeToLive.
        """
        if value is not None:
            self.timeToLive = value
        return self


class SomeipSdServerEventGroupTimingConfig(ARElement):
    """EventGroup specific timing configuration settings. Tags: atp.recommendedPackage=SomeipSdTimingConfigs"""

    # SomeipSdServerEventGroupTimingConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.172, p.517
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getRequestResponseDelay    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRequestResponseDelay    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # The Service Discovery shall delay answers to unicast messages triggered by multicast messages (e.g. Subscribe Eventgroup after Offer Service).
        self.requestResponseDelay: Optional[RequestResponseDelay] = None

    def getRequestResponseDelay(self) -> Optional[RequestResponseDelay]:
        """The Service Discovery shall delay answers to unicast messages triggered by multicast messages (e.g. Subscribe Eventgroup after Offer Service)."""
        return self.requestResponseDelay

    def setRequestResponseDelay(self, value: Optional[RequestResponseDelay]) -> "SomeipSdServerEventGroupTimingConfig":
        """
        The Service Discovery shall delay answers to unicast messages triggered by multicast messages (e.g. Subscribe Eventgroup after Offer Service).
        A None value is a no-op and does not overwrite an existing requestResponseDelay.
        """
        if value is not None:
            self.requestResponseDelay = value
        return self


class SdServerConfig(ARObject):
    """
    Configures Service Discovery (SD) server properties, specifying
    service advertisement behavior, timing parameters, and version
    information for service providers in the network.
    """

    # SdServerConfig method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCapabilityRecords         [x] impl  [ ] docstring  [ ] test
    # [ ] setCapabilityRecords         [x] impl  [ ] docstring  [ ] test
    # [ ] getInitialOfferBehavior      [x] impl  [ ] docstring  [ ] test
    # [ ] setInitialOfferBehavior      [x] impl  [ ] docstring  [ ] test
    # [ ] getOfferCyclicDelay          [x] impl  [ ] docstring  [ ] test
    # [ ] setOfferCyclicDelay          [x] impl  [ ] docstring  [ ] test
    # [ ] getRequestResponseDelay      [x] impl  [ ] docstring  [ ] test
    # [ ] setRequestResponseDelay      [x] impl  [ ] docstring  [ ] test
    # [ ] getServerServiceMajorVersion [x] impl  [ ] docstring  [ ] test
    # [ ] setServerServiceMajorVersion [x] impl  [ ] docstring  [ ] test
    # [ ] getServerServiceMinorVersion [x] impl  [ ] docstring  [ ] test
    # [ ] setServerServiceMinorVersion [x] impl  [ ] docstring  [ ] test
    # [ ] getTtl                       [x] impl  [ ] docstring  [ ] test
    # [ ] setTtl                       [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.capabilityRecords = []  # type: List[TagWithOptionalValue]
        self.initialOfferBehavior = None  # type: InitialSdDelayConfig
        self.offerCyclicDelay = None  # type: TimeValue
        self.requestResponseDelay = None  # type: RequestResponseDelay
        self.serverServiceMajorVersion = None  # type: PositiveInteger
        self.serverServiceMinorVersion = None  # type: PositiveInteger
        self.ttl = None  # type: PositiveInteger

    def getCapabilityRecords(self):
        return self.capabilityRecords

    def setCapabilityRecords(self, value):
        if value is not None:
            self.capabilityRecords = value
        return self

    def getInitialOfferBehavior(self):
        return self.initialOfferBehavior

    def setInitialOfferBehavior(self, value):
        if value is not None:
            self.initialOfferBehavior = value
        return self

    def getOfferCyclicDelay(self):
        return self.offerCyclicDelay

    def setOfferCyclicDelay(self, value):
        if value is not None:
            self.offerCyclicDelay = value
        return self

    def getRequestResponseDelay(self):
        return self.requestResponseDelay

    def setRequestResponseDelay(self, value):
        if value is not None:
            self.requestResponseDelay = value
        return self

    def getServerServiceMajorVersion(self):
        return self.serverServiceMajorVersion

    def setServerServiceMajorVersion(self, value):
        if value is not None:
            self.serverServiceMajorVersion = value
        return self

    def getServerServiceMinorVersion(self):
        return self.serverServiceMinorVersion

    def setServerServiceMinorVersion(self, value):
        if value is not None:
            self.serverServiceMinorVersion = value
        return self

    def getTtl(self):
        return self.ttl

    def setTtl(self, value):
        if value is not None:
            self.ttl = value
        return self


class EventHandler(Identifiable):
    """
    This element represents an event group as part of the Provided Service Instance.
    """

    # EventHandler method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.166, p.492
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addConsumedEventGroupRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConsumedEventGroupRefs         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getEventGroupIdentifier           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEventGroupIdentifier           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEventMulticastAddressRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEventMulticastAddressRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMulticastThreshold             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMulticastThreshold             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addPduActivationRoutingGroup      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPduActivationRoutingGroups     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addRoutingGroupRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRoutingGroupRefs               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getSdServerConfig                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSdServerConfig                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSdServerEgTimingConfigRef      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSdServerEgTimingConfigRef      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # All consumers of the event are referenced here.
        self.consumedEventGroupRefs: List[RefType] = []

        # Unique Identifier that identifies the EventGroup in SOME/IP. This Identifier is sent as Eventgroup ID in SOME/IP Service Discovery messages.
        self.eventGroupIdentifier: Optional[PositiveInteger] = None

        # Multicast Address that is used for event communication in the IP-Multicast case. It is the destination address to which the server sends the multicast event messages if the mulicastThreshold is exceeded. This address is transmitted in the SD-SubscribeEventGroupAck Message to client (answer to SD-SubscribeEventGroup).
        self.eventMulticastAddressRef: Optional[RefType] = None

        # Specifies the number of subscribed clients that trigger the server to change the transmission of events to multicast. If configured to 0 only unicast will be used. If configured to 1 the first client will be already served by multicast. If configured to 2 the first client will be server with unicast and as soon as the second client arrives both will be served by multicast. This does not influence the handling of initial events, which are served using unicast only.
        self.multicastThreshold: Optional[PositiveInteger] = None

        # The ServiceDiscovery module is able to activate and deactivate the PDU routing for events.
        self.pduActivationRoutingGroups: List[PduActivationRoutingGroup] = []

        # The ServiceDiscovery module is able to activate and deactivate the PDU routing for events.
        self.routingGroupRefs: List[RefType] = []

        # Server configuration parameter for Service-Discovery.
        self.sdServerConfig: Optional[SdServerConfig] = None

        # Server Timing configuration settings that are EventGroup specific.
        self.sdServerEgTimingConfigRef: Optional[RefType] = None

    def addConsumedEventGroupRef(self, value: Optional[RefType]) -> "EventHandler":
        """
        All consumers of the event are referenced here.
        A None value is a no-op and does not append to consumedEventGroupRefs.
        """
        if value is not None:
            self.consumedEventGroupRefs.append(value)
        return self

    def getConsumedEventGroupRefs(self) -> List[RefType]:
        """All consumers of the event are referenced here."""
        return self.consumedEventGroupRefs

    def getEventGroupIdentifier(self) -> Optional[PositiveInteger]:
        """Unique Identifier that identifies the EventGroup in SOME/IP. This Identifier is sent as Eventgroup ID in SOME/IP Service Discovery messages."""
        return self.eventGroupIdentifier

    def setEventGroupIdentifier(self, value: Optional[PositiveInteger]) -> "EventHandler":
        """
        Unique Identifier that identifies the EventGroup in SOME/IP. This Identifier is sent as Eventgroup ID in SOME/IP Service Discovery messages.
        A None value is a no-op and does not overwrite an existing eventGroupIdentifier.
        """
        if value is not None:
            self.eventGroupIdentifier = value
        return self

    def getEventMulticastAddressRef(self) -> Optional[RefType]:
        """Multicast Address that is used for event communication in the IP-Multicast case. It is the destination address to which the server sends the multicast event messages if the mulicastThreshold is exceeded. This address is transmitted in the SD-SubscribeEventGroupAck Message to client (answer to SD-SubscribeEventGroup)."""
        return self.eventMulticastAddressRef

    def setEventMulticastAddressRef(self, value: Optional[RefType]) -> "EventHandler":
        """
        Multicast Address that is used for event communication in the IP-Multicast case. It is the destination address to which the server sends the multicast event messages if the mulicastThreshold is exceeded. This address is transmitted in the SD-SubscribeEventGroupAck Message to client (answer to SD-SubscribeEventGroup).
        A None value is a no-op and does not overwrite an existing eventMulticastAddressRef.
        """
        if value is not None:
            self.eventMulticastAddressRef = value
        return self

    def getMulticastThreshold(self) -> Optional[PositiveInteger]:
        """Specifies the number of subscribed clients that trigger the server to change the transmission of events to multicast. If configured to 0 only unicast will be used. If configured to 1 the first client will be already served by multicast. If configured to 2 the first client will be server with unicast and as soon as the second client arrives both will be served by multicast. This does not influence the handling of initial events, which are served using unicast only."""
        return self.multicastThreshold

    def setMulticastThreshold(self, value: Optional[PositiveInteger]) -> "EventHandler":
        """
        Specifies the number of subscribed clients that trigger the server to change the transmission of events to multicast. If configured to 0 only unicast will be used. If configured to 1 the first client will be already served by multicast. If configured to 2 the first client will be server with unicast and as soon as the second client arrives both will be served by multicast. This does not influence the handling of initial events, which are served using unicast only.
        A None value is a no-op and does not overwrite an existing multicastThreshold.
        """
        if value is not None:
            self.multicastThreshold = value
        return self

    def addPduActivationRoutingGroup(self, value: Optional[PduActivationRoutingGroup]) -> "EventHandler":
        """
        The ServiceDiscovery module is able to activate and deactivate the PDU routing for events.
        A None value is a no-op and does not append to pduActivationRoutingGroups.
        """
        if value is not None:
            self.pduActivationRoutingGroups.append(value)
        return self

    def getPduActivationRoutingGroups(self) -> List[PduActivationRoutingGroup]:
        """The ServiceDiscovery module is able to activate and deactivate the PDU routing for events."""
        return self.pduActivationRoutingGroups

    def addRoutingGroupRef(self, value: Optional[RefType]) -> "EventHandler":
        """
        The ServiceDiscovery module is able to activate and deactivate the PDU routing for events.
        A None value is a no-op and does not append to routingGroupRefs.
        """
        if value is not None:
            self.routingGroupRefs.append(value)
        return self

    def getRoutingGroupRefs(self) -> List[RefType]:
        """The ServiceDiscovery module is able to activate and deactivate the PDU routing for events."""
        return self.routingGroupRefs

    def getSdServerConfig(self) -> Optional[SdServerConfig]:
        """Server configuration parameter for Service-Discovery."""
        return self.sdServerConfig

    def setSdServerConfig(self, value: Optional[SdServerConfig]) -> "EventHandler":
        """
        Server configuration parameter for Service-Discovery.
        A None value is a no-op and does not overwrite an existing sdServerConfig.
        """
        if value is not None:
            self.sdServerConfig = value
        return self

    def getSdServerEgTimingConfigRef(self) -> Optional[RefType]:
        """Server Timing configuration settings that are EventGroup specific."""
        return self.sdServerEgTimingConfigRef

    def setSdServerEgTimingConfigRef(self, value: Optional[RefType]) -> "EventHandler":
        """
        Server Timing configuration settings that are EventGroup specific.
        A None value is a no-op and does not overwrite an existing sdServerEgTimingConfigRef.
        """
        if value is not None:
            self.sdServerEgTimingConfigRef = value
        return self


class ProvidedServiceInstance(AbstractServiceInstance):
    """
    Service instances that are provided by the ECU that is connected via the ApplicationEndpoint to a CommunicationConnector.
    """

    # ProvidedServiceInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table E.37, p.1002
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAllowedServiceConsumerRefs              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addAllowedServiceConsumerRef               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] setAllowedServiceConsumerRefs              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAutoAvailable                           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAutoAvailable                           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEventHandlers                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createEventHandler                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInstanceIdentifier                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setInstanceIdentifier                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLoadBalancingPriority                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLoadBalancingPriority                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLoadBalancingWeight                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLoadBalancingWeight                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLocalUnicastAddressRefs                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLocalUnicastAddressRefs                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addLocalUnicastAddressRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinorVersion                            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinorVersion                            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPriority                                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPriority                                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRemoteMulticastSubscriptionAddressRefs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRemoteMulticastSubscriptionAddressRefs [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addRemoteMulticastSubscriptionAddressRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getRemoteUnicastAddressRefs                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setRemoteUnicastAddressRefs                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addRemoteUnicastAddressRef                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSdServerConfig                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSdServerConfig                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSdServerTimerConfigRef                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSdServerTimerConfigRef                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getServiceIdentifier                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setServiceIdentifier                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # NetworkEndpoints on which the ConsumedService Instances that are communicating with this Provided ServiceInstance are allowed to be located so that the ACL check in the ServiceDiscovery is successful and the connection is allowed to be established. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=allowedServiceConsumer.networkEndpoint, allowedServiceConsumer.variationPoint.shortLabel atp.Status=draft vh.latestBindingTime=postBuild
        self.allowedServiceConsumerRefs: List[RefType] = []

        # Defines that this ProvidedServiceInstance shall be offered by the service discovery at ECU start.
        self.autoAvailable: Optional[Boolean] = None

        # Collection of event groups provided by the Provided ServiceInstance Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=eventHandler.shortName, event Handler.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.eventHandlers: List[EventHandler] = []

        # Instance identifier. Can be used for e.g. service discovery to identify the instance of the service.
        self.instanceIdentifier: Optional[PositiveInteger] = None

        # Defines the value to be used for load balancing priority in the service offer. Lower value means higher priority.
        self.loadBalancingPriority: Optional[PositiveInteger] = None

        # Defines the value to be used for load balancing weight in the service offer. Higher value means higher probability to be chosen.
        self.loadBalancingWeight: Optional[PositiveInteger] = None

        # The local address over which the PSI is provided (udp, tcp or both). Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=localUnicastAddress.applicationEndpoint, localUnicastAddress.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.localUnicastAddressRefs: List[RefType] = []

        # Minor Version of the Service that is provided by this ProvidedServiceInstance.
        self.minorVersion: Optional[PositiveInteger] = None

        # Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed.
        self.priority: Optional[PositiveInteger] = None

        # This reference defines the remote multicast subscribed addresses of service consumers. This reference shall ONLY be used if the remote address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=remoteMulticastSubscription Address.applicationEndpoint, remoteMulticast SubscriptionAddress.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.remoteMulticastSubscriptionAddressRefs: List[RefType] = []

        # This reference defines the remote addresses of service consumers. This reference shall ONLY be used if the remote address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=remoteUnicastAddress.applicationEndpoint, remoteUnicastAddress.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.remoteUnicastAddressRefs: List[RefType] = []

        # Service Discovery Server configuration. Tags: atp.Status=obsolete
        self.sdServerConfig: Optional[SdServerConfig] = None

        # Server specific configuration settings relevant for the SOME/IP service discovery. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=sdServerTimerConfig.someipSdServer ServiceInstanceConfig, sdServerTimer Config.variationPoint.shortLabel vh.latestBindingTime=postBuild
        self.sdServerTimerConfigRef: Optional[RefType] = None

        # This attribute represents the ability to describe the SOME/ IP service ID that is offered.
        self.serviceIdentifier: Optional[PositiveInteger] = None

    def getAllowedServiceConsumerRefs(self):
        """
        NetworkEndpoints on which the ConsumedService Instances that are communicating with this Provided ServiceInstance are allowed to be located so that the ACL check in the ServiceDiscovery is successful and the connection is allowed to be established. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=allowedServiceConsumer.networkEndpoint, allowedServiceConsumer.variationPoint.shortLabel atp.Status=draft vh.latestBindingTime=postBuild
        """
        return self.allowedServiceConsumerRefs

    def addAllowedServiceConsumerRef(self, allowed_service_consumer_ref: RefType) -> "ProvidedServiceInstance":
        """
        NetworkEndpoints on which the ConsumedService Instances that are communicating with this Provided ServiceInstance are allowed to be located so that the ACL check in the ServiceDiscovery is successful and the connection is allowed to be established. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=allowedServiceConsumer.networkEndpoint, allowedServiceConsumer.variationPoint.shortLabel atp.Status=draft vh.latestBindingTime=postBuild
        """
        if allowed_service_consumer_ref is not None:
            self.allowedServiceConsumerRefs.append(allowed_service_consumer_ref)
        return self

    def setAllowedServiceConsumerRefs(self, allowed_service_consumer_refs: List[RefType]) -> "ProvidedServiceInstance":
        """
        NetworkEndpoints on which the ConsumedService Instances that are communicating with this Provided ServiceInstance are allowed to be located so that the ACL check in the ServiceDiscovery is successful and the connection is allowed to be established. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=allowedServiceConsumer.networkEndpoint, allowedServiceConsumer.variationPoint.shortLabel atp.Status=draft vh.latestBindingTime=postBuild
        """
        if allowed_service_consumer_refs is not None:
            self.allowedServiceConsumerRefs = allowed_service_consumer_refs
        return self

    def getAutoAvailable(self):
        """
        Defines that this ProvidedServiceInstance shall be offered by the service discovery at ECU start.
        """
        return self.autoAvailable

    def setAutoAvailable(self, value):
        """
        Defines that this ProvidedServiceInstance shall be offered by the service discovery at ECU start.
        """
        if value is not None:
            self.autoAvailable = value
        return self

    def getEventHandlers(self):
        """
        Collection of event groups provided by the Provided ServiceInstance Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=eventHandler.shortName, event Handler.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.eventHandlers

    def createEventHandler(self, short_name: str) -> EventHandler:
        """
        Collection of event groups provided by the Provided ServiceInstance Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=eventHandler.shortName, event Handler.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if short_name not in self.elements:
            instance = EventHandler(self, short_name)
            self.addElement(instance)
            self.eventHandlers.append(instance)
        return self.getElement(short_name)

    def getInstanceIdentifier(self):
        """
        Instance identifier. Can be used for e.g. service discovery to identify the instance of the service.
        """
        return self.instanceIdentifier

    def setInstanceIdentifier(self, value):
        """
        Instance identifier. Can be used for e.g. service discovery to identify the instance of the service.
        """
        if value is not None:
            self.instanceIdentifier = value
        return self

    def getLoadBalancingPriority(self):
        """
        Defines the value to be used for load balancing priority in the service offer. Lower value means higher priority.
        """
        return self.loadBalancingPriority

    def setLoadBalancingPriority(self, value):
        """
        Defines the value to be used for load balancing priority in the service offer. Lower value means higher priority.
        """
        if value is not None:
            self.loadBalancingPriority = value
        return self

    def getLoadBalancingWeight(self):
        """
        Defines the value to be used for load balancing weight in the service offer. Higher value means higher probability to be chosen.
        """
        return self.loadBalancingWeight

    def setLoadBalancingWeight(self, value):
        """
        Defines the value to be used for load balancing weight in the service offer. Higher value means higher probability to be chosen.
        """
        if value is not None:
            self.loadBalancingWeight = value
        return self

    def getLocalUnicastAddressRefs(self):
        """
        The local address over which the PSI is provided (udp, tcp or both). Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=localUnicastAddress.applicationEndpoint, localUnicastAddress.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.localUnicastAddressRefs

    def setLocalUnicastAddressRefs(self, value):
        """
        The local address over which the PSI is provided (udp, tcp or both). Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=localUnicastAddress.applicationEndpoint, localUnicastAddress.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if value is not None:
            self.localUnicastAddressRefs = value
        return self

    def addLocalUnicastAddressRef(self, value):
        """
        The local address over which the PSI is provided (udp, tcp or both). Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=localUnicastAddress.applicationEndpoint, localUnicastAddress.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if value is not None:
            self.localUnicastAddressRefs.append(value)
        return self

    def getMinorVersion(self):
        """
        Minor Version of the Service that is provided by this ProvidedServiceInstance.
        """
        return self.minorVersion

    def setMinorVersion(self, value):
        """
        Minor Version of the Service that is provided by this ProvidedServiceInstance.
        """
        if value is not None:
            self.minorVersion = value
        return self

    def getPriority(self):
        """
        Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed.
        """
        return self.priority

    def setPriority(self, value):
        """
        Defines the frame priority where values from 0 (best effort) to 7 (highest) are allowed.
        """
        if value is not None:
            self.priority = value
        return self

    def getRemoteMulticastSubscriptionAddressRefs(self):
        """
        This reference defines the remote multicast subscribed addresses of service consumers. This reference shall ONLY be used if the remote address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=remoteMulticastSubscription Address.applicationEndpoint, remoteMulticast SubscriptionAddress.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.remoteMulticastSubscriptionAddressRefs

    def setRemoteMulticastSubscriptionAddressRefs(self, value):
        """
        This reference defines the remote multicast subscribed addresses of service consumers. This reference shall ONLY be used if the remote address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=remoteMulticastSubscription Address.applicationEndpoint, remoteMulticast SubscriptionAddress.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if value is not None:
            self.remoteMulticastSubscriptionAddressRefs = value
        return self

    def addRemoteMulticastSubscriptionAddressRef(self, value):
        """
        This reference defines the remote multicast subscribed addresses of service consumers. This reference shall ONLY be used if the remote address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=remoteMulticastSubscription Address.applicationEndpoint, remoteMulticast SubscriptionAddress.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if value is not None:
            self.remoteMulticastSubscriptionAddressRefs.append(value)
        return self

    def getRemoteUnicastAddressRefs(self):
        """
        This reference defines the remote addresses of service consumers. This reference shall ONLY be used if the remote address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=remoteUnicastAddress.applicationEndpoint, remoteUnicastAddress.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.remoteUnicastAddressRefs

    def setRemoteUnicastAddressRefs(self, value):
        """
        This reference defines the remote addresses of service consumers. This reference shall ONLY be used if the remote address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=remoteUnicastAddress.applicationEndpoint, remoteUnicastAddress.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if value is not None:
            self.remoteUnicastAddressRefs = value
        return self

    def addRemoteUnicastAddressRef(self, value):
        """
        This reference defines the remote addresses of service consumers. This reference shall ONLY be used if the remote address of the clients is determined from the configuration and not at runtime. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=remoteUnicastAddress.applicationEndpoint, remoteUnicastAddress.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if value is not None:
            self.remoteUnicastAddressRefs.append(value)
        return self

    def getSdServerConfig(self):
        """
        Service Discovery Server configuration. Tags: atp.Status=obsolete
        """
        return self.sdServerConfig

    def setSdServerConfig(self, value):
        """
        Service Discovery Server configuration. Tags: atp.Status=obsolete
        """
        if value is not None:
            self.sdServerConfig = value
        return self

    def getSdServerTimerConfigRef(self):
        """
        Server specific configuration settings relevant for the SOME/IP service discovery. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=sdServerTimerConfig.someipSdServer ServiceInstanceConfig, sdServerTimer Config.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        return self.sdServerTimerConfigRef

    def setSdServerTimerConfigRef(self, value):
        """
        Server specific configuration settings relevant for the SOME/IP service discovery. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=sdServerTimerConfig.someipSdServer ServiceInstanceConfig, sdServerTimer Config.variationPoint.shortLabel vh.latestBindingTime=postBuild
        """
        if value is not None:
            self.sdServerTimerConfigRef = value
        return self

    def getServiceIdentifier(self):
        """
        This attribute represents the ability to describe the SOME/ IP service ID that is offered.
        """
        return self.serviceIdentifier

    def setServiceIdentifier(self, value):
        """
        This attribute represents the ability to describe the SOME/ IP service ID that is offered.
        """
        if value is not None:
            self.serviceIdentifier = value
        return self


class SocketAddress(Identifiable):
    """This meta-class represents a socket address towards the rest of the meta-model. The actual semantics of the represented socket address, however, is contributed by aggregation of an ApplicationEndpoint."""

    # SocketAddress method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.118, p.453
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAllowedIPv6ExtHeadersRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAllowedIPv6ExtHeadersRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAllowedTcpOptionsRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAllowedTcpOptionsRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createApplicationEndpoint            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getApplicationEndpoint               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getConnectorRef                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setConnectorRef                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDifferentiatedServiceField        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDifferentiatedServiceField        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFlowLabel                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFlowLabel                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addMulticastConnectorRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMulticastConnectorRefs            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getPathMtuDiscoveryEnabled           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPathMtuDiscoveryEnabled           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPduCollectionMaxBufferSize        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPduCollectionMaxBufferSize        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPduCollectionTimeout              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPduCollectionTimeout              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addStaticSocketConnection            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getStaticSocketConnections           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getUdpChecksumHandling               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUdpChecksumHandling               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to a list of IPv6 Extension Headers allowed for this SocketConnection. If no list is referenced all IPv6 Extension Headers are allowed and processed.
        self.allowedIPv6ExtHeadersRef: Optional[RefType] = None

        # Reference to a list of TCP options allowed for this Socket Connection.
        self.allowedTcpOptionsRef: Optional[RefType] = None

        # Application addressing
        self.applicationEndpoint: Optional[ApplicationEndpoint] = None

        # Association to a CommunicationConnector in the topology description. This reference shall be used if the SocketAddress describes an IP unicast address for an ECU that is part of the model.
        self.connectorRef: Optional[RefType] = None

        # The 6-bit Differentiated Service Field in the IP headers may be used for classifying network traffic. If not set a value of zero is used to indicate packets that have not been classified.
        self.differentiatedServiceField: Optional[PositiveInteger] = None

        # The 20-bit Flow Label field in the IPv6 header may be used by a source to label sequences of packets for which it requests special handling by the IPv6 routers, such as non-default quality of service. If not set a Flow Label of zero is used to indicate packets that have not been labeled.
        self.flowLabel: Optional[PositiveInteger] = None

        # Association to a CommunicationConnector in the topology description. This reference shall be used if the SocketAddress describes an IP multicast address, i.e. if the aggregated ApplicationEndpoint references a NetworkEndpoint that describes an IP Address in the IP multicast range. Such a SocketAddress contains references to those Ecus (via the multicastConnector reference) in the model that will receive multicast messages via the SocketAddress that is defined by the aggregated ApplicationEndpoint and NetworkEndpoint, i.e. IP Address and UDP Port combination.
        self.multicastConnectorRefs: List[RefType] = []

        # Defines whether the Path MTU Discovery shall be performed for the related socket.
        self.pathMtuDiscoveryEnabled: Optional[Boolean] = None

        # Defines the maximum buffer size in Byte which shall be filled before a socket with Pdu collection enabled shall be transmitted to the lower layer.
        self.pduCollectionMaxBufferSize: Optional[PositiveInteger] = None

        # Defines the time in seconds which shall pass before a socket with Pdu collection enabled shall be transmitted to the lower layer after the first Pdu has been put into the socket buffer.
        self.pduCollectionTimeout: Optional[TimeValue] = None

        # Definition of a static SocketConnection.
        self.staticSocketConnections: List[StaticSocketConnection] = []

        # Specifies if UDP checksum handling shall be enabled (udpChecksumEnabled) or skipped (udpChecksum Disabled) on the related socket connection.
        self.udpChecksumHandling: Optional[UdpChecksumCalculationEnum] = None

    def getAllowedIPv6ExtHeadersRef(self) -> Optional[RefType]:
        """Reference to a list of IPv6 Extension Headers allowed for this SocketConnection. If no list is referenced all IPv6 Extension Headers are allowed and processed."""
        return self.allowedIPv6ExtHeadersRef

    def setAllowedIPv6ExtHeadersRef(self, value: Optional[RefType]) -> "SocketAddress":
        """
        Reference to a list of IPv6 Extension Headers allowed for this SocketConnection. If no list is referenced all IPv6 Extension Headers are allowed and processed.
        A None value is a no-op and does not overwrite an existing allowedIPv6ExtHeadersRef.
        """
        if value is not None:
            self.allowedIPv6ExtHeadersRef = value
        return self

    def getAllowedTcpOptionsRef(self) -> Optional[RefType]:
        """Reference to a list of TCP options allowed for this Socket Connection."""
        return self.allowedTcpOptionsRef

    def setAllowedTcpOptionsRef(self, value: Optional[RefType]) -> "SocketAddress":
        """
        Reference to a list of TCP options allowed for this Socket Connection.
        A None value is a no-op and does not overwrite an existing allowedTcpOptionsRef.
        """
        if value is not None:
            self.allowedTcpOptionsRef = value
        return self

    def createApplicationEndpoint(self, short_name: str) -> ApplicationEndpoint:
        """Application addressing"""
        if not self.IsElementExists(short_name, ApplicationEndpoint):
            end_point = ApplicationEndpoint(self, short_name)
            self.addElement(end_point)
            self.applicationEndpoint = end_point
        return self.getElement(short_name, ApplicationEndpoint)

    def getApplicationEndpoint(self) -> Optional[ApplicationEndpoint]:
        """Application addressing"""
        return self.applicationEndpoint

    def getConnectorRef(self) -> Optional[RefType]:
        """Association to a CommunicationConnector in the topology description. This reference shall be used if the SocketAddress describes an IP unicast address for an ECU that is part of the model."""
        return self.connectorRef

    def setConnectorRef(self, value: Optional[RefType]) -> "SocketAddress":
        """
        Association to a CommunicationConnector in the topology description. This reference shall be used if the SocketAddress describes an IP unicast address for an ECU that is part of the model.
        A None value is a no-op and does not overwrite an existing connectorRef.
        """
        if value is not None:
            self.connectorRef = value
        return self

    def getDifferentiatedServiceField(self) -> Optional[PositiveInteger]:
        """The 6-bit Differentiated Service Field in the IP headers may be used for classifying network traffic. If not set a value of zero is used to indicate packets that have not been classified."""
        return self.differentiatedServiceField

    def setDifferentiatedServiceField(self, value: Optional[PositiveInteger]) -> "SocketAddress":
        """
        The 6-bit Differentiated Service Field in the IP headers may be used for classifying network traffic. If not set a value of zero is used to indicate packets that have not been classified.
        A None value is a no-op and does not overwrite an existing differentiatedServiceField.
        """
        if value is not None:
            self.differentiatedServiceField = value
        return self

    def getFlowLabel(self) -> Optional[PositiveInteger]:
        """The 20-bit Flow Label field in the IPv6 header may be used by a source to label sequences of packets for which it requests special handling by the IPv6 routers, such as non-default quality of service. If not set a Flow Label of zero is used to indicate packets that have not been labeled."""
        return self.flowLabel

    def setFlowLabel(self, value: Optional[PositiveInteger]) -> "SocketAddress":
        """
        The 20-bit Flow Label field in the IPv6 header may be used by a source to label sequences of packets for which it requests special handling by the IPv6 routers, such as non-default quality of service. If not set a Flow Label of zero is used to indicate packets that have not been labeled.
        A None value is a no-op and does not overwrite an existing flowLabel.
        """
        if value is not None:
            self.flowLabel = value
        return self

    def addMulticastConnectorRef(self, value: Optional[RefType]) -> "SocketAddress":
        """
        Association to a CommunicationConnector in the topology description. This reference shall be used if the SocketAddress describes an IP multicast address, i.e. if the aggregated ApplicationEndpoint references a NetworkEndpoint that describes an IP Address in the IP multicast range. Such a SocketAddress contains references to those Ecus (via the multicastConnector reference) in the model that will receive multicast messages via the SocketAddress that is defined by the aggregated ApplicationEndpoint and NetworkEndpoint, i.e. IP Address and UDP Port combination.
        A None value is a no-op and does not append to multicastConnectorRefs.
        """
        if value is not None:
            self.multicastConnectorRefs.append(value)
        return self

    def getMulticastConnectorRefs(self) -> List[RefType]:
        """Association to a CommunicationConnector in the topology description. This reference shall be used if the SocketAddress describes an IP multicast address, i.e. if the aggregated ApplicationEndpoint references a NetworkEndpoint that describes an IP Address in the IP multicast range. Such a SocketAddress contains references to those Ecus (via the multicastConnector reference) in the model that will receive multicast messages via the SocketAddress that is defined by the aggregated ApplicationEndpoint and NetworkEndpoint, i.e. IP Address and UDP Port combination."""
        return self.multicastConnectorRefs

    def getPathMtuDiscoveryEnabled(self) -> Optional[Boolean]:
        """Defines whether the Path MTU Discovery shall be performed for the related socket."""
        return self.pathMtuDiscoveryEnabled

    def setPathMtuDiscoveryEnabled(self, value: Optional[Boolean]) -> "SocketAddress":
        """
        Defines whether the Path MTU Discovery shall be performed for the related socket.
        A None value is a no-op and does not overwrite an existing pathMtuDiscoveryEnabled.
        """
        if value is not None:
            self.pathMtuDiscoveryEnabled = value
        return self

    def getPduCollectionMaxBufferSize(self) -> Optional[PositiveInteger]:
        """Defines the maximum buffer size in Byte which shall be filled before a socket with Pdu collection enabled shall be transmitted to the lower layer."""
        return self.pduCollectionMaxBufferSize

    def setPduCollectionMaxBufferSize(self, value: Optional[PositiveInteger]) -> "SocketAddress":
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

    def setPduCollectionTimeout(self, value: Optional[TimeValue]) -> "SocketAddress":
        """
        Defines the time in seconds which shall pass before a socket with Pdu collection enabled shall be transmitted to the lower layer after the first Pdu has been put into the socket buffer.
        A None value is a no-op and does not overwrite an existing pduCollectionTimeout.
        """
        if value is not None:
            self.pduCollectionTimeout = value
        return self

    def addStaticSocketConnection(self, value: Optional[StaticSocketConnection]) -> "SocketAddress":
        """
        Definition of a static SocketConnection.
        A None value is a no-op and does not append to staticSocketConnections.
        """
        if value is not None:
            self.staticSocketConnections.append(value)
        return self

    def getStaticSocketConnections(self) -> List[StaticSocketConnection]:
        """Definition of a static SocketConnection."""
        return self.staticSocketConnections

    def getUdpChecksumHandling(self) -> Optional[UdpChecksumCalculationEnum]:
        """Specifies if UDP checksum handling shall be enabled (udpChecksumEnabled) or skipped (udpChecksum Disabled) on the related socket connection."""
        return self.udpChecksumHandling

    def setUdpChecksumHandling(self, value: Optional[UdpChecksumCalculationEnum]) -> "SocketAddress":
        """
        Specifies if UDP checksum handling shall be enabled (udpChecksumEnabled) or skipped (udpChecksum Disabled) on the related socket connection.
        A None value is a no-op and does not overwrite an existing udpChecksumHandling.
        """
        if value is not None:
            self.udpChecksumHandling = value
        return self


class SoAdConfig(ARObject):
    """
    SoAd Configuration for one specific Physical Channel.
    """

    # SoAdConfig method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.117, p.452
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addConnection                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConnections               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createSocketConnectionBundle [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getConnectionBundles         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createSocketAddress          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSocketAddresses           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This aggregation is obsolete and will be removed in the future. The connectionGroup aggregation with bundled Connections shall be used instead. Old description: Collection of socket connections.
        self.connections: List[SocketConnection] = []

        # Collection of SocketConnectionBundles.
        self.connectionBundles: List[SocketConnectionBundle] = []

        # Collection of SoAdAddresses.
        self.socketAddresses: List[SocketAddress] = []

    def addConnection(self, value: Optional[SocketConnection]) -> "SoAdConfig":
        """
        This aggregation is obsolete and will be removed in the future. The connectionGroup aggregation with bundled Connections shall be used instead. Old description: Collection of socket connections.
        A None value is a no-op and does not append to connections.
        """
        if value is not None:
            self.connections.append(value)
        return self

    def getConnections(self) -> List[SocketConnection]:
        """This aggregation is obsolete and will be removed in the future. The connectionGroup aggregation with bundled Connections shall be used instead. Old description: Collection of socket connections."""
        return self.connections

    def createSocketConnectionBundle(self, short_name: str) -> SocketConnectionBundle:
        """Collection of SocketConnectionBundles."""
        bundle = SocketConnectionBundle(self, short_name)
        self.connectionBundles.append(bundle)
        return bundle

    def getConnectionBundles(self) -> List[SocketConnectionBundle]:
        """Collection of SocketConnectionBundles."""
        return self.connectionBundles

    def createSocketAddress(self, short_name: str) -> SocketAddress:
        """Collection of SoAdAddresses."""
        address = SocketAddress(self, short_name)
        self.socketAddresses.append(address)
        return address

    def getSocketAddresses(self) -> List[SocketAddress]:
        """Collection of SoAdAddresses."""
        return self.socketAddresses
