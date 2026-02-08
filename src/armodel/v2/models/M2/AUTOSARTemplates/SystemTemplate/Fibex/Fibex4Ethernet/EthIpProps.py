from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


class EthIpProps(ARElement):
    """
    This meta-class is used to configure the EcuInstance specific IP attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::EthIpProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 146, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configuration options for IPv4.
        self._ipv4Props: Optional["Ipv4Props"] = None

    @property
    def ipv4_props(self) -> Optional["Ipv4Props"]:
        """Get ipv4Props (Pythonic accessor)."""
        return self._ipv4Props

    @ipv4_props.setter
    def ipv4_props(self, value: Optional["Ipv4Props"]) -> None:
        """
        Set ipv4Props with validation.

        Args:
            value: The ipv4Props to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv4Props = None
            return

        if not isinstance(value, Ipv4Props):
            raise TypeError(
                f"ipv4Props must be Ipv4Props or None, got {type(value).__name__}"
            )
        self._ipv4Props = value
        # Configuration options for IPv6.
        self._ipv6Props: Optional["Ipv6Props"] = None

    @property
    def ipv6_props(self) -> Optional["Ipv6Props"]:
        """Get ipv6Props (Pythonic accessor)."""
        return self._ipv6Props

    @ipv6_props.setter
    def ipv6_props(self, value: Optional["Ipv6Props"]) -> None:
        """
        Set ipv6Props with validation.

        Args:
            value: The ipv6Props to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipv6Props = None
            return

        if not isinstance(value, Ipv6Props):
            raise TypeError(
                f"ipv6Props must be Ipv6Props or None, got {type(value).__name__}"
            )
        self._ipv6Props = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIpv4Props(self) -> "Ipv4Props":
        """
        AUTOSAR-compliant getter for ipv4Props.

        Returns:
            The ipv4Props value

        Note:
            Delegates to ipv4_props property (CODING_RULE_V2_00017)
        """
        return self.ipv4_props  # Delegates to property

    def setIpv4Props(self, value: "Ipv4Props") -> "EthIpProps":
        """
        AUTOSAR-compliant setter for ipv4Props with method chaining.

        Args:
            value: The ipv4Props to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv4_props property setter (gets validation automatically)
        """
        self.ipv4_props = value  # Delegates to property setter
        return self

    def getIpv6Props(self) -> "Ipv6Props":
        """
        AUTOSAR-compliant getter for ipv6Props.

        Returns:
            The ipv6Props value

        Note:
            Delegates to ipv6_props property (CODING_RULE_V2_00017)
        """
        return self.ipv6_props  # Delegates to property

    def setIpv6Props(self, value: "Ipv6Props") -> "EthIpProps":
        """
        AUTOSAR-compliant setter for ipv6Props with method chaining.

        Args:
            value: The ipv6Props to set

        Returns:
            self for method chaining

        Note:
            Delegates to ipv6_props property setter (gets validation automatically)
        """
        self.ipv6_props = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ipv4_props(self, value: Optional["Ipv4Props"]) -> "EthIpProps":
        """
        Set ipv4Props and return self for chaining.

        Args:
            value: The ipv4Props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv4_props("value")
        """
        self.ipv4_props = value  # Use property setter (gets validation)
        return self

    def with_ipv6_props(self, value: Optional["Ipv6Props"]) -> "EthIpProps":
        """
        Set ipv6Props and return self for chaining.

        Args:
            value: The ipv6Props to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ipv6_props("value")
        """
        self.ipv6_props = value  # Use property setter (gets validation)
        return self
