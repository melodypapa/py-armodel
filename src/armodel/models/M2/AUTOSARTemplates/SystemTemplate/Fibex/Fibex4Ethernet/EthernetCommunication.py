# This module contains AUTOSAR System Template classes for Ethernet communication
# It defines socket connections, connection bundles, and service instances for Ethernet networking

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, Describable, Referrable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerFdConfiguration,
    CanControllerXlConfiguration,
    CanControllerXlConfigurationRequirements,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import FibexElement


class SocketConnection(Describable):
    """
    Represents a socket connection in the Ethernet communication system,
    defining properties for TCP/IP communication including IP addresses,
    ports, PDU handling, and timeout configurations for network connections.
    """

    # SocketConnection method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getAllowedIPv6ExtHeadersRef  [x] impl  [ ] docstring  [ ] test
    # [ ] setAllowedIPv6ExtHeadersRef  [x] impl  [ ] docstring  [ ] test
    # [ ] getAllowedTcpOptionsRef      [x] impl  [ ] docstring  [ ] test
    # [ ] setAllowedTcpOptionsRef      [x] impl  [ ] docstring  [ ] test
    # [ ] getClientIpAddrFromConnectionRequest [x] impl  [ ] docstring  [ ] test
    # [ ] setClientIpAddrFromConnectionRequest [x] impl  [ ] docstring  [ ] test
    # [ ] getClientPortRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setClientPortRef             [x] impl  [ ] docstring  [ ] test
    # [ ] getClientPortFromConnectionRequest [x] impl  [ ] docstring  [ ] test
    # [ ] setClientPortFromConnectionRequest [x] impl  [ ] docstring  [ ] test
    # [ ] getPdus                      [x] impl  [ ] docstring  [ ] test
    # [ ] addPdu                       [x] impl  [ ] docstring  [ ] test
    # [ ] getPduSocketConnectionIpdus  [x] impl  [ ] docstring  [ ] test
    # [ ] addPduSocketConnectionIpdu   [x] impl  [ ] docstring  [ ] test
    # [ ] getPduCollectionMaxBufferSize [x] impl  [ ] docstring  [ ] test
    # [ ] setPduCollectionMaxBufferSize [x] impl  [ ] docstring  [ ] test
    # [ ] getPduCollectionTimeout      [x] impl  [ ] docstring  [ ] test
    # [ ] setPduCollectionTimeout      [x] impl  [ ] docstring  [ ] test
    # [ ] getRuntimeIpAddressConfiguration [x] impl  [ ] docstring  [ ] test
    # [ ] setRuntimeIpAddressConfiguration [x] impl  [ ] docstring  [ ] test
    # [ ] getRuntimePortConfiguration  [x] impl  [ ] docstring  [ ] test
    # [ ] setRuntimePortConfiguration  [x] impl  [ ] docstring  [ ] test
    # [ ] getShortLabel                [x] impl  [ ] docstring  [ ] test
    # [ ] setShortLabel                [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.allowedIPv6ExtHeadersRef: RefType = None
        self.allowedTcpOptionsRef: RefType = None
        self.clientIpAddrFromConnectionRequest: Boolean = None
        self.clientPortRef: RefType = None
        self.clientPortFromConnectionRequest: Boolean = None
        self.pdus: List[SocketConnectionIpduIdentifier] = []
        self.pduSocketConnectionIpdus: List[Identifier] = []
        self.pduCollectionMaxBufferSize: PositiveInteger = None
        self.pduCollectionTimeout: TimeValue = None
        self.runtimeIpAddressConfiguration = None
        self.runtimePortConfiguration = None
        self.shortLabel: Identifier = None

    def getAllowedIPv6ExtHeadersRef(self):
        return self.allowedIPv6ExtHeadersRef

    def setAllowedIPv6ExtHeadersRef(self, value):
        self.allowedIPv6ExtHeadersRef = value
        return self

    def getAllowedTcpOptionsRef(self):
        return self.allowedTcpOptionsRef

    def setAllowedTcpOptionsRef(self, value):
        self.allowedTcpOptionsRef = value
        return self

    def getClientIpAddrFromConnectionRequest(self):
        return self.clientIpAddrFromConnectionRequest

    def setClientIpAddrFromConnectionRequest(self, value):
        self.clientIpAddrFromConnectionRequest = value
        return self

    def getClientPortRef(self):
        return self.clientPortRef

    def setClientPortRef(self, value):
        self.clientPortRef = value
        return self

    def getClientPortFromConnectionRequest(self):
        return self.clientPortFromConnectionRequest

    def setClientPortFromConnectionRequest(self, value):
        self.clientPortFromConnectionRequest = value
        return self

    def getPdus(self):
        return self.pdus

    def addPdu(self, value):
        self.pdus.append(value)
        return self

    def getPduSocketConnectionIpdus(self):
        return self.pduSocketConnectionIpdus

    def addPduSocketConnectionIpdu(self, value):
        self.pduSocketConnectionIpdus.append(value)
        return self

    def getPduCollectionMaxBufferSize(self):
        return self.pduCollectionMaxBufferSize

    def setPduCollectionMaxBufferSize(self, value):
        self.pduCollectionMaxBufferSize = value
        return self

    def getPduCollectionTimeout(self):
        return self.pduCollectionTimeout

    def setPduCollectionTimeout(self, value):
        self.pduCollectionTimeout = value
        return self

    def getRuntimeIpAddressConfiguration(self):
        return self.runtimeIpAddressConfiguration

    def setRuntimeIpAddressConfiguration(self, value):
        self.runtimeIpAddressConfiguration = value
        return self

    def getRuntimePortConfiguration(self):
        return self.runtimePortConfiguration

    def setRuntimePortConfiguration(self, value):
        self.runtimePortConfiguration = value
        return self

    def getShortLabel(self):
        return self.shortLabel

    def setShortLabel(self, value):
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
