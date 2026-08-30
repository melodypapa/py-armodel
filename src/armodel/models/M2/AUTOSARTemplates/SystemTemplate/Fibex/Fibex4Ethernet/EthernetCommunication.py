# This module contains AUTOSAR System Template Ethernet Communication classes for Fibex4Ethernet
# (M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Ethernet Communication).
# Source: AUTOSAR_TPS_SystemTemplate (R4.3.1), Tables 6.118 (SocketConnectionBundle), 6.120
# (SocketConnection), 6.121 (RuntimeAddressConfigurationEnum), 6.122 (SocketConnectionIpduIdentifier),
# 6.125 (SoAdRoutingGroup), 6.129 (IPv6ExtHeaderFilterList), 6.130 (TcpOptionFilterSet),
# 6.131 (TcpOptionFilterList).

from typing import List, TYPE_CHECKING

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, PositiveInteger, RefType, TimeValue

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel import SocketConnection


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


class SocketConnectionIpduIdentifier(ARObject):
    """
    Identifies an IPDU (Interaction Protocol Data Unit) within a socket connection,
    defining header IDs, timeout values, collection semantics, and references
    to PDUs and triggering mechanisms for Ethernet communication.
    """

    # SocketConnectionIpduIdentifier method parity checklist:
    # Spec: AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.122
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
    # Spec: AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.118
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
