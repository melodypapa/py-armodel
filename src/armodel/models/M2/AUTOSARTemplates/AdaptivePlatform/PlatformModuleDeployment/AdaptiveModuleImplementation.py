from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    Ip6AddressString,
    RefType,
)


class PlatformModuleEndpointConfiguration(ARElement, ABC):
    """
    This meta-class defines the abstract attributes for the configuration of a network for a specific CommunicationConnector.
    """

    # PlatformModuleEndpointConfiguration method parity checklist:
    # Spec: PlatformModuleEndpointConfiguration derived from AUTOSAR_00052.xsd (XSD-only; no own table in repo corpus), line 91412
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is PlatformModuleEndpointConfiguration:
            raise TypeError("PlatformModuleEndpointConfiguration is an abstract class.")
        super().__init__(parent, short_name)


class PlatformModuleEthernetEndpointConfiguration(PlatformModuleEndpointConfiguration):
    """
    This meta-class defines the attributes for the configuration of a port, protocol type and IP address of the communication on a VLAN. Tags: atp.recommendedPackage=PlatformModuleEndpointConfigurations
    """

    # PlatformModuleEthernetEndpointConfiguration method parity checklist:
    # Spec: AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf, Table B.19, p.65
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCommunicationConnectorRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommunicationConnectorRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIpv4MulticastIpAddress     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpv4MulticastIpAddress     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIpv6MulticastIpAddress     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIpv6MulticastIpAddress     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Reference to the CommunicationConnector (VLAN) for which the network configuration is defined.
        self.communicationConnectorRef: Optional[RefType] = None

        # Multicast IPv4 Address to which the message will be transmitted.
        self.ipv4MulticastIpAddress: Optional[Ip4AddressString] = None

        # Multicast IPv6 Address to which the message will be transmitted.
        self.ipv6MulticastIpAddress: Optional[Ip6AddressString] = None

    def getCommunicationConnectorRef(self) -> Optional[RefType]:
        """
        Reference to the CommunicationConnector (VLAN) for which the network configuration is defined.
        """
        return self.communicationConnectorRef

    def setCommunicationConnectorRef(self, value: Optional[RefType]) -> "PlatformModuleEthernetEndpointConfiguration":
        """
        Reference to the CommunicationConnector (VLAN) for which the network configuration is defined.

        A None value is a no-op and does not overwrite an existing communicationConnectorRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.communicationConnectorRef = value
        return self

    def getIpv4MulticastIpAddress(self) -> Optional[Ip4AddressString]:
        """
        Multicast IPv4 Address to which the message will be transmitted.
        """
        return self.ipv4MulticastIpAddress

    def setIpv4MulticastIpAddress(self, value: Optional[Ip4AddressString]) -> "PlatformModuleEthernetEndpointConfiguration":
        """
        Multicast IPv4 Address to which the message will be transmitted.

        A None value is a no-op and does not overwrite an existing ipv4MulticastIpAddress.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ipv4MulticastIpAddress = value
        return self

    def getIpv6MulticastIpAddress(self) -> Optional[Ip6AddressString]:
        """
        Multicast IPv6 Address to which the message will be transmitted.
        """
        return self.ipv6MulticastIpAddress

    def setIpv6MulticastIpAddress(self, value: Optional[Ip6AddressString]) -> "PlatformModuleEthernetEndpointConfiguration":
        """
        Multicast IPv6 Address to which the message will be transmitted.

        A None value is a no-op and does not overwrite an existing ipv6MulticastIpAddress.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ipv6MulticastIpAddress = value
        return self
