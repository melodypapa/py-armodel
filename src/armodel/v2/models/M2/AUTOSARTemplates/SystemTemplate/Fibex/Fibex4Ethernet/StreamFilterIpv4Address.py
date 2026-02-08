from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class StreamFilterIpv4Address(ARObject):
    """
    IPv4 address range definition.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::StreamFilterIpv4Address

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 138, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match packets with the IPv4 address range.
        # atp.
        # Status=candidate.
        self._ipv4Address: Optional["Ip4AddressString"] = None

    @property
    def ipv4_address(self) -> Optional["Ip4AddressString"]:
        """Get ipv4Address (Pythonic accessor)."""
        return self._ipv4Address

    @ipv4_address.setter
    def ipv4_address(self, value: Optional["Ip4AddressString"]) -> None:
        """
        Set ipv4Address with validation.

        Args:
            value: The ipv4Address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv4Address = None
            return

        if not isinstance(value, Ip4AddressString):
            raise TypeError(
                f"ipv4Address must be Ip4AddressString or None, got {type(value).__name__}"
            )
        self._ipv4Address = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIpv4Address(self) -> "Ip4AddressString":
        """
        AUTOSAR-compliant getter for ipv4Address.

        Returns:
            The ipv4Address value

        Note:
            Delegates to ipv4_address property (CODING_RULE_V2_00017)
        """
        return self.ipv4_address  # Delegates to property

    def setIpv4Address(self, value: "Ip4AddressString") -> "StreamFilterIpv4Address":
        """
        AUTOSAR-compliant setter for ipv4Address with method chaining.

        Args:
            value: The ipv4Address to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv4_address property setter (gets validation automatically)
        """
        self.ipv4_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ipv4_address(self, value: Optional["Ip4AddressString"]) -> "StreamFilterIpv4Address":
        """
        Set ipv4Address and return self for chaining.

        Args:
            value: The ipv4Address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv4_address("value")
        """
        self.ipv4_address = value  # Use property setter (gets validation)
        return self
