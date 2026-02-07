from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class MacMulticastGroup(Identifiable):
    """
    Per EthernetCluster globally defined MacMulticastGroup. One sender can
    handle many receivers simultaneously if the receivers have all the same
    macMulticastAddress. The addresses need to be unique for the particular
    EthernetCluster.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::MacMulticastGroup

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 103, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A multicast MAC address (Media Access Control is a identifier for a group of
        # hosts in a network.
        self._macMulticast: Optional["MacAddressString"] = None

    @property
    def mac_multicast(self) -> Optional["MacAddressString"]:
        """Get macMulticast (Pythonic accessor)."""
        return self._macMulticast

    @mac_multicast.setter
    def mac_multicast(self, value: Optional["MacAddressString"]) -> None:
        """
        Set macMulticast with validation.

        Args:
            value: The macMulticast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macMulticast = None
            return

        if not isinstance(value, MacAddressString):
            raise TypeError(
                f"macMulticast must be MacAddressString or None, got {type(value).__name__}"
            )
        self._macMulticast = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMacMulticast(self) -> "MacAddressString":
        """
        AUTOSAR-compliant getter for macMulticast.

        Returns:
            The macMulticast value

        Note:
            Delegates to mac_multicast property (CODING_RULE_V2_00017)
        """
        return self.mac_multicast  # Delegates to property

    def setMacMulticast(self, value: "MacAddressString") -> "MacMulticastGroup":
        """
        AUTOSAR-compliant setter for macMulticast with method chaining.

        Args:
            value: The macMulticast to set

        Returns:
            self for method chaining

        Note:
            Delegates to mac_multicast property setter (gets validation automatically)
        """
        self.mac_multicast = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mac_multicast(self, value: Optional["MacAddressString"]) -> "MacMulticastGroup":
        """
        Set macMulticast and return self for chaining.

        Args:
            value: The macMulticast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mac_multicast("value")
        """
        self.mac_multicast = value  # Use property setter (gets validation)
        return self
