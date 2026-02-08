from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    Ipv4DhcpServer,
    Ipv6DhcpServer,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class DhcpServerConfiguration(ARObject):
    """
    Defines the configuration of DHCP servers that are running on the network
    endpoint. It is possible that an Ipv4DhcpServer and an Ipv6DhcpServer run on
    the same Ecu.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::DhcpServerConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 131, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configuration of a IPv4 DHCP server that runs on the network endpoint.
        self._ipv4DhcpServer: Optional["Ipv4DhcpServer"] = None

    @property
    def ipv4_dhcp_server(self) -> Optional["Ipv4DhcpServer"]:
        """Get ipv4DhcpServer (Pythonic accessor)."""
        return self._ipv4DhcpServer

    @ipv4_dhcp_server.setter
    def ipv4_dhcp_server(self, value: Optional["Ipv4DhcpServer"]) -> None:
        """
        Set ipv4DhcpServer with validation.

        Args:
            value: The ipv4DhcpServer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv4DhcpServer = None
            return

        if not isinstance(value, Ipv4DhcpServer):
            raise TypeError(
                f"ipv4DhcpServer must be Ipv4DhcpServer or None, got {type(value).__name__}"
            )
        self._ipv4DhcpServer = value
        # Configuration of a IPv6 DHCP server that runs on the network endpoint.
        self._ipv6DhcpServer: Optional["Ipv6DhcpServer"] = None

    @property
    def ipv6_dhcp_server(self) -> Optional["Ipv6DhcpServer"]:
        """Get ipv6DhcpServer (Pythonic accessor)."""
        return self._ipv6DhcpServer

    @ipv6_dhcp_server.setter
    def ipv6_dhcp_server(self, value: Optional["Ipv6DhcpServer"]) -> None:
        """
        Set ipv6DhcpServer with validation.

        Args:
            value: The ipv6DhcpServer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv6DhcpServer = None
            return

        if not isinstance(value, Ipv6DhcpServer):
            raise TypeError(
                f"ipv6DhcpServer must be Ipv6DhcpServer or None, got {type(value).__name__}"
            )
        self._ipv6DhcpServer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIpv4DhcpServer(self) -> "Ipv4DhcpServer":
        """
        AUTOSAR-compliant getter for ipv4DhcpServer.

        Returns:
            The ipv4DhcpServer value

        Note:
            Delegates to ipv4_dhcp_server property (CODING_RULE_V2_00017)
        """
        return self.ipv4_dhcp_server  # Delegates to property

    def setIpv4DhcpServer(self, value: "Ipv4DhcpServer") -> "DhcpServerConfiguration":
        """
        AUTOSAR-compliant setter for ipv4DhcpServer with method chaining.

        Args:
            value: The ipv4DhcpServer to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv4_dhcp_server property setter (gets validation automatically)
        """
        self.ipv4_dhcp_server = value  # Delegates to property setter
        return self

    def getIpv6DhcpServer(self) -> "Ipv6DhcpServer":
        """
        AUTOSAR-compliant getter for ipv6DhcpServer.

        Returns:
            The ipv6DhcpServer value

        Note:
            Delegates to ipv6_dhcp_server property (CODING_RULE_V2_00017)
        """
        return self.ipv6_dhcp_server  # Delegates to property

    def setIpv6DhcpServer(self, value: "Ipv6DhcpServer") -> "DhcpServerConfiguration":
        """
        AUTOSAR-compliant setter for ipv6DhcpServer with method chaining.

        Args:
            value: The ipv6DhcpServer to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv6_dhcp_server property setter (gets validation automatically)
        """
        self.ipv6_dhcp_server = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ipv4_dhcp_server(self, value: Optional["Ipv4DhcpServer"]) -> "DhcpServerConfiguration":
        """
        Set ipv4DhcpServer and return self for chaining.

        Args:
            value: The ipv4DhcpServer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv4_dhcp_server("value")
        """
        self.ipv4_dhcp_server = value  # Use property setter (gets validation)
        return self

    def with_ipv6_dhcp_server(self, value: Optional["Ipv6DhcpServer"]) -> "DhcpServerConfiguration":
        """
        Set ipv6DhcpServer and return self for chaining.

        Args:
            value: The ipv6DhcpServer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv6_dhcp_server("value")
        """
        self.ipv6_dhcp_server = value  # Use property setter (gets validation)
        return self
