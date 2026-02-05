from typing import Any, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    Ip6AddressString,
)


class PlatformModuleEthernetEndpointConfiguration(ARElement):
    """
    This meta-class defines the attributes for the configuration of a port,
    protocol type and IP address of the communication on a VLAN. Tags:
    atp.recommendedPackage=PlatformModuleEndpointConfigurations

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 65, Foundation R23-11)
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Type: EthernetCommunication.
        # Reference to the CommunicationConnector (VLAN) for which the network
        # configuration is defined.
        self.communications: Optional[Any] = None
        # Multicast IPv4 Address to which the message will be.
        self.ipv4MulticastIps: Optional[Ip4AddressString] = None
        # Multicast IPv6 Address to which the message will be.
        self.ipv6MulticastIps: Optional[Ip6AddressString] = None

    def getCommunications(self) -> Any:
        return self.communications

    def setCommunications(
        self, value: Any
    ) -> "PlatformModuleEthernetEndpointConfiguration":
        self.communications = value
        return self

    def getIpv4MulticastIps(self) -> Ip4AddressString:
        return self.ipv4MulticastIps

    def setIpv4MulticastIps(
        self, value: Ip4AddressString
    ) -> "PlatformModuleEthernetEndpointConfiguration":
        self.ipv4MulticastIps = value
        return self

    def getIpv6MulticastIps(self) -> Ip6AddressString:
        return self.ipv6MulticastIps

    def setIpv6MulticastIps(
        self, value: Ip6AddressString
    ) -> "PlatformModuleEthernetEndpointConfiguration":
        self.ipv6MulticastIps = value
        return self
