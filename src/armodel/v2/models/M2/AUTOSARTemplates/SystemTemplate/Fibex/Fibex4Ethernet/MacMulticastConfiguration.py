from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import NetworkEndpointAddress
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class MacMulticastConfiguration(NetworkEndpointAddress):
    """
    References a per cluster globally defined MAC-Multicast-Group.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::MacMulticastConfiguration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 467, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a macMulticastGroup.
        self._macMulticastGroup: RefType = None

    @property
    def mac_multicast_group(self) -> RefType:
        """Get macMulticastGroup (Pythonic accessor)."""
        return self._macMulticastGroup

    @mac_multicast_group.setter
    def mac_multicast_group(self, value: RefType) -> None:
        """
        Set macMulticastGroup with validation.

        Args:
            value: The macMulticastGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._macMulticastGroup = None
            return

        self._macMulticastGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMacMulticastGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for macMulticastGroup.

        Returns:
            The macMulticastGroup value

        Note:
            Delegates to mac_multicast_group property (CODING_RULE_V2_00017)
        """
        return self.mac_multicast_group  # Delegates to property

    def setMacMulticastGroup(self, value: RefType) -> "MacMulticastConfiguration":
        """
        AUTOSAR-compliant setter for macMulticastGroup with method chaining.

        Args:
            value: The macMulticastGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to mac_multicast_group property setter (gets validation automatically)
        """
        self.mac_multicast_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mac_multicast_group(self, value: Optional[RefType]) -> "MacMulticastConfiguration":
        """
        Set macMulticastGroup and return self for chaining.

        Args:
            value: The macMulticastGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mac_multicast_group("value")
        """
        self.mac_multicast_group = value  # Use property setter (gets validation)
        return self
