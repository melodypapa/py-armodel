from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    Ipv4ArpProps,
    Ipv4AutoIpProps,
    Ipv4Fragmentation,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class Ipv4Props(ARObject):
    """
    This meta-class specifies the configuration options for IPv4.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::Ipv4Props

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 146, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configuration properties for the ARP (Address Resolution.
        self._arpProps: Optional["Ipv4ArpProps"] = None

    @property
    def arp_props(self) -> Optional["Ipv4ArpProps"]:
        """Get arpProps (Pythonic accessor)."""
        return self._arpProps

    @arp_props.setter
    def arp_props(self, value: Optional["Ipv4ArpProps"]) -> None:
        """
        Set arpProps with validation.

        Args:
            value: The arpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arpProps = None
            return

        if not isinstance(value, Ipv4ArpProps):
            raise TypeError(
                f"arpProps must be Ipv4ArpProps or None, got {type(value).__name__}"
            )
        self._arpProps = value
        # Configuration options for Auto-IP (automatic private IP.
        self._autoIpProps: Optional["Ipv4AutoIpProps"] = None

    @property
    def auto_ip_props(self) -> Optional["Ipv4AutoIpProps"]:
        """Get autoIpProps (Pythonic accessor)."""
        return self._autoIpProps

    @auto_ip_props.setter
    def auto_ip_props(self, value: Optional["Ipv4AutoIpProps"]) -> None:
        """
        Set autoIpProps with validation.

        Args:
            value: The autoIpProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._autoIpProps = None
            return

        if not isinstance(value, Ipv4AutoIpProps):
            raise TypeError(
                f"autoIpProps must be Ipv4AutoIpProps or None, got {type(value).__name__}"
            )
        self._autoIpProps = value
        # Configuration options for IPv4 packet fragmentation/ reassembly.
        self._fragmentation: Optional["Ipv4Fragmentation"] = None

    @property
    def fragmentation(self) -> Optional["Ipv4Fragmentation"]:
        """Get fragmentation (Pythonic accessor)."""
        return self._fragmentation

    @fragmentation.setter
    def fragmentation(self, value: Optional["Ipv4Fragmentation"]) -> None:
        """
        Set fragmentation with validation.

        Args:
            value: The fragmentation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fragmentation = None
            return

        if not isinstance(value, Ipv4Fragmentation):
            raise TypeError(
                f"fragmentation must be Ipv4Fragmentation or None, got {type(value).__name__}"
            )
        self._fragmentation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArpProps(self) -> "Ipv4ArpProps":
        """
        AUTOSAR-compliant getter for arpProps.

        Returns:
            The arpProps value

        Note:
            Delegates to arp_props property (CODING_RULE_V2_00017)
        """
        return self.arp_props  # Delegates to property

    def setArpProps(self, value: "Ipv4ArpProps") -> "Ipv4Props":
        """
        AUTOSAR-compliant setter for arpProps with method chaining.

        Args:
            value: The arpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to arp_props property setter (gets validation automatically)
        """
        self.arp_props = value  # Delegates to property setter
        return self

    def getAutoIpProps(self) -> "Ipv4AutoIpProps":
        """
        AUTOSAR-compliant getter for autoIpProps.

        Returns:
            The autoIpProps value

        Note:
            Delegates to auto_ip_props property (CODING_RULE_V2_00017)
        """
        return self.auto_ip_props  # Delegates to property

    def setAutoIpProps(self, value: "Ipv4AutoIpProps") -> "Ipv4Props":
        """
        AUTOSAR-compliant setter for autoIpProps with method chaining.

        Args:
            value: The autoIpProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to auto_ip_props property setter (gets validation automatically)
        """
        self.auto_ip_props = value  # Delegates to property setter
        return self

    def getFragmentation(self) -> "Ipv4Fragmentation":
        """
        AUTOSAR-compliant getter for fragmentation.

        Returns:
            The fragmentation value

        Note:
            Delegates to fragmentation property (CODING_RULE_V2_00017)
        """
        return self.fragmentation  # Delegates to property

    def setFragmentation(self, value: "Ipv4Fragmentation") -> "Ipv4Props":
        """
        AUTOSAR-compliant setter for fragmentation with method chaining.

        Args:
            value: The fragmentation to set

        Returns:
            self for method chaining

        Note:
            Delegates to fragmentation property setter (gets validation automatically)
        """
        self.fragmentation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_arp_props(self, value: Optional["Ipv4ArpProps"]) -> "Ipv4Props":
        """
        Set arpProps and return self for chaining.

        Args:
            value: The arpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_arp_props("value")
        """
        self.arp_props = value  # Use property setter (gets validation)
        return self

    def with_auto_ip_props(self, value: Optional["Ipv4AutoIpProps"]) -> "Ipv4Props":
        """
        Set autoIpProps and return self for chaining.

        Args:
            value: The autoIpProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_auto_ip_props("value")
        """
        self.auto_ip_props = value  # Use property setter (gets validation)
        return self

    def with_fragmentation(self, value: Optional["Ipv4Fragmentation"]) -> "Ipv4Props":
        """
        Set fragmentation and return self for chaining.

        Args:
            value: The fragmentation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fragmentation("value")
        """
        self.fragmentation = value  # Use property setter (gets validation)
        return self
