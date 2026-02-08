from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class StreamFilterIpv6Address(ARObject):
    """
    IPv6 address range definition.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 138, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match packets with the IPv6 address range.
        # atp.
        # Status=candidate.
        self._ipv6Address: Optional["Ip6AddressString"] = None

    @property
    def ipv6_address(self) -> Optional["Ip6AddressString"]:
        """Get ipv6Address (Pythonic accessor)."""
        return self._ipv6Address

    @ipv6_address.setter
    def ipv6_address(self, value: Optional["Ip6AddressString"]) -> None:
        """
        Set ipv6Address with validation.

        Args:
            value: The ipv6Address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv6Address = None
            return

        if not isinstance(value, Ip6AddressString):
            raise TypeError(
                f"ipv6Address must be Ip6AddressString or None, got {type(value).__name__}"
            )
        self._ipv6Address = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIpv6Address(self) -> "Ip6AddressString":
        """
        AUTOSAR-compliant getter for ipv6Address.

        Returns:
            The ipv6Address value

        Note:
            Delegates to ipv6_address property (CODING_RULE_V2_00017)
        """
        return self.ipv6_address  # Delegates to property

    def setIpv6Address(self, value: "Ip6AddressString") -> "StreamFilterIpv6Address":
        """
        AUTOSAR-compliant setter for ipv6Address with method chaining.

        Args:
            value: The ipv6Address to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv6_address property setter (gets validation automatically)
        """
        self.ipv6_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ipv6_address(self, value: Optional["Ip6AddressString"]) -> "StreamFilterIpv6Address":
        """
        Set ipv6Address and return self for chaining.

        Args:
            value: The ipv6Address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv6_address("value")
        """
        self.ipv6_address = value  # Use property setter (gets validation)
        return self
