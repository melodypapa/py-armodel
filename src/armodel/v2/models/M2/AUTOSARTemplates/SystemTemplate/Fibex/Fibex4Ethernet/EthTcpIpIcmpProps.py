from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class EthTcpIpIcmpProps(ARElement):
    """
    This meta-class is used to configure the EcuInstance specific ICMP (Internet
    Control Message Protocol) attributes

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 156, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ICMPv4 configuration properties.
        self._icmpV4Props: Optional["TcpIpIcmpv4Props"] = None

    @property
    def icmp_v4_props(self) -> Optional["TcpIpIcmpv4Props"]:
        """Get icmpV4Props (Pythonic accessor)."""
        return self._icmpV4Props

    @icmp_v4_props.setter
    def icmp_v4_props(self, value: Optional["TcpIpIcmpv4Props"]) -> None:
        """
        Set icmpV4Props with validation.

        Args:
            value: The icmpV4Props to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._icmpV4Props = None
            return

        if not isinstance(value, TcpIpIcmpv4Props):
            raise TypeError(
                f"icmpV4Props must be TcpIpIcmpv4Props or None, got {type(value).__name__}"
            )
        self._icmpV4Props = value
        # ICMPv6 configuration properties.
        self._icmpV6Props: Optional["TcpIpIcmpv6Props"] = None

    @property
    def icmp_v6_props(self) -> Optional["TcpIpIcmpv6Props"]:
        """Get icmpV6Props (Pythonic accessor)."""
        return self._icmpV6Props

    @icmp_v6_props.setter
    def icmp_v6_props(self, value: Optional["TcpIpIcmpv6Props"]) -> None:
        """
        Set icmpV6Props with validation.

        Args:
            value: The icmpV6Props to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._icmpV6Props = None
            return

        if not isinstance(value, TcpIpIcmpv6Props):
            raise TypeError(
                f"icmpV6Props must be TcpIpIcmpv6Props or None, got {type(value).__name__}"
            )
        self._icmpV6Props = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIcmpV4Props(self) -> "TcpIpIcmpv4Props":
        """
        AUTOSAR-compliant getter for icmpV4Props.

        Returns:
            The icmpV4Props value

        Note:
            Delegates to icmp_v4_props property (CODING_RULE_V2_00017)
        """
        return self.icmp_v4_props  # Delegates to property

    def setIcmpV4Props(self, value: "TcpIpIcmpv4Props") -> "EthTcpIpIcmpProps":
        """
        AUTOSAR-compliant setter for icmpV4Props with method chaining.

        Args:
            value: The icmpV4Props to set

        Returns:
            self for method chaining

        Note:
            Delegates to icmp_v4_props property setter (gets validation automatically)
        """
        self.icmp_v4_props = value  # Delegates to property setter
        return self

    def getIcmpV6Props(self) -> "TcpIpIcmpv6Props":
        """
        AUTOSAR-compliant getter for icmpV6Props.

        Returns:
            The icmpV6Props value

        Note:
            Delegates to icmp_v6_props property (CODING_RULE_V2_00017)
        """
        return self.icmp_v6_props  # Delegates to property

    def setIcmpV6Props(self, value: "TcpIpIcmpv6Props") -> "EthTcpIpIcmpProps":
        """
        AUTOSAR-compliant setter for icmpV6Props with method chaining.

        Args:
            value: The icmpV6Props to set

        Returns:
            self for method chaining

        Note:
            Delegates to icmp_v6_props property setter (gets validation automatically)
        """
        self.icmp_v6_props = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_icmp_v4_props(self, value: Optional["TcpIpIcmpv4Props"]) -> "EthTcpIpIcmpProps":
        """
        Set icmpV4Props and return self for chaining.

        Args:
            value: The icmpV4Props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_icmp_v4_props("value")
        """
        self.icmp_v4_props = value  # Use property setter (gets validation)
        return self

    def with_icmp_v6_props(self, value: Optional["TcpIpIcmpv6Props"]) -> "EthTcpIpIcmpProps":
        """
        Set icmpV6Props and return self for chaining.

        Args:
            value: The icmpV6Props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_icmp_v6_props("value")
        """
        self.icmp_v6_props = value  # Use property setter (gets validation)
        return self
