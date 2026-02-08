from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import StreamFilterMAC
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class StreamFilterRuleDataLinkLayer(ARObject):
    """
    Configuration of filter rules on the DataLink layer

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::StreamFilterRuleDataLinkLayer

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 137, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match packets with the destination MAC address/ mask.
        self._destinationMac: Optional["StreamFilterMAC"] = None

    @property
    def destination_mac(self) -> Optional["StreamFilterMAC"]:
        """Get destinationMac (Pythonic accessor)."""
        return self._destinationMac

    @destination_mac.setter
    def destination_mac(self, value: Optional["StreamFilterMAC"]) -> None:
        """
        Set destinationMac with validation.

        Args:
            value: The destinationMac to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationMac = None
            return

        if not isinstance(value, StreamFilterMAC):
            raise TypeError(
                f"destinationMac must be StreamFilterMAC or None, got {type(value).__name__}"
            )
        self._destinationMac = value
        # Filter to match packets based on the EtherType field in frame.
        self._etherType: Optional["PositiveInteger"] = None

    @property
    def ether_type(self) -> Optional["PositiveInteger"]:
        """Get etherType (Pythonic accessor)."""
        return self._etherType

    @ether_type.setter
    def ether_type(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set etherType with validation.

        Args:
            value: The etherType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._etherType = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"etherType must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._etherType = value
        # Filter to match packets with the source MAC address/ mask.
        self._sourceMac: Optional["StreamFilterMAC"] = None

    @property
    def source_mac(self) -> Optional["StreamFilterMAC"]:
        """Get sourceMac (Pythonic accessor)."""
        return self._sourceMac

    @source_mac.setter
    def source_mac(self, value: Optional["StreamFilterMAC"]) -> None:
        """
        Set sourceMac with validation.

        Args:
            value: The sourceMac to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceMac = None
            return

        if not isinstance(value, StreamFilterMAC):
            raise TypeError(
                f"sourceMac must be StreamFilterMAC or None, got {type(value).__name__}"
            )
        self._sourceMac = value
        # Filter of packets with a VlanId.
        self._vlanId: Optional["PositiveInteger"] = None

    @property
    def vlan_id(self) -> Optional["PositiveInteger"]:
        """Get vlanId (Pythonic accessor)."""
        return self._vlanId

    @vlan_id.setter
    def vlan_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set vlanId with validation.

        Args:
            value: The vlanId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlanId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"vlanId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._vlanId = value
        # Filter of packets with a Vlan priority.
        self._vlanPriority: Optional["PositiveInteger"] = None

    @property
    def vlan_priority(self) -> Optional["PositiveInteger"]:
        """Get vlanPriority (Pythonic accessor)."""
        return self._vlanPriority

    @vlan_priority.setter
    def vlan_priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set vlanPriority with validation.

        Args:
            value: The vlanPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vlanPriority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"vlanPriority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._vlanPriority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationMac(self) -> "StreamFilterMAC":
        """
        AUTOSAR-compliant getter for destinationMac.

        Returns:
            The destinationMac value

        Note:
            Delegates to destination_mac property (CODING_RULE_V2_00017)
        """
        return self.destination_mac  # Delegates to property

    def setDestinationMac(self, value: "StreamFilterMAC") -> "StreamFilterRuleDataLinkLayer":
        """
        AUTOSAR-compliant setter for destinationMac with method chaining.

        Args:
            value: The destinationMac to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_mac property setter (gets validation automatically)
        """
        self.destination_mac = value  # Delegates to property setter
        return self

    def getEtherType(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for etherType.

        Returns:
            The etherType value

        Note:
            Delegates to ether_type property (CODING_RULE_V2_00017)
        """
        return self.ether_type  # Delegates to property

    def setEtherType(self, value: "PositiveInteger") -> "StreamFilterRuleDataLinkLayer":
        """
        AUTOSAR-compliant setter for etherType with method chaining.

        Args:
            value: The etherType to set

        Returns:
            self for method chaining

        Note:
            Delegates to ether_type property setter (gets validation automatically)
        """
        self.ether_type = value  # Delegates to property setter
        return self

    def getSourceMac(self) -> "StreamFilterMAC":
        """
        AUTOSAR-compliant getter for sourceMac.

        Returns:
            The sourceMac value

        Note:
            Delegates to source_mac property (CODING_RULE_V2_00017)
        """
        return self.source_mac  # Delegates to property

    def setSourceMac(self, value: "StreamFilterMAC") -> "StreamFilterRuleDataLinkLayer":
        """
        AUTOSAR-compliant setter for sourceMac with method chaining.

        Args:
            value: The sourceMac to set

        Returns:
            self for method chaining

        Note:
            Delegates to source_mac property setter (gets validation automatically)
        """
        self.source_mac = value  # Delegates to property setter
        return self

    def getVlanId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for vlanId.

        Returns:
            The vlanId value

        Note:
            Delegates to vlan_id property (CODING_RULE_V2_00017)
        """
        return self.vlan_id  # Delegates to property

    def setVlanId(self, value: "PositiveInteger") -> "StreamFilterRuleDataLinkLayer":
        """
        AUTOSAR-compliant setter for vlanId with method chaining.

        Args:
            value: The vlanId to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan_id property setter (gets validation automatically)
        """
        self.vlan_id = value  # Delegates to property setter
        return self

    def getVlanPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for vlanPriority.

        Returns:
            The vlanPriority value

        Note:
            Delegates to vlan_priority property (CODING_RULE_V2_00017)
        """
        return self.vlan_priority  # Delegates to property

    def setVlanPriority(self, value: "PositiveInteger") -> "StreamFilterRuleDataLinkLayer":
        """
        AUTOSAR-compliant setter for vlanPriority with method chaining.

        Args:
            value: The vlanPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to vlan_priority property setter (gets validation automatically)
        """
        self.vlan_priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_mac(self, value: Optional["StreamFilterMAC"]) -> "StreamFilterRuleDataLinkLayer":
        """
        Set destinationMac and return self for chaining.

        Args:
            value: The destinationMac to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_mac("value")
        """
        self.destination_mac = value  # Use property setter (gets validation)
        return self

    def with_ether_type(self, value: Optional["PositiveInteger"]) -> "StreamFilterRuleDataLinkLayer":
        """
        Set etherType and return self for chaining.

        Args:
            value: The etherType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ether_type("value")
        """
        self.ether_type = value  # Use property setter (gets validation)
        return self

    def with_source_mac(self, value: Optional["StreamFilterMAC"]) -> "StreamFilterRuleDataLinkLayer":
        """
        Set sourceMac and return self for chaining.

        Args:
            value: The sourceMac to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source_mac("value")
        """
        self.source_mac = value  # Use property setter (gets validation)
        return self

    def with_vlan_id(self, value: Optional["PositiveInteger"]) -> "StreamFilterRuleDataLinkLayer":
        """
        Set vlanId and return self for chaining.

        Args:
            value: The vlanId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan_id("value")
        """
        self.vlan_id = value  # Use property setter (gets validation)
        return self

    def with_vlan_priority(self, value: Optional["PositiveInteger"]) -> "StreamFilterRuleDataLinkLayer":
        """
        Set vlanPriority and return self for chaining.

        Args:
            value: The vlanPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vlan_priority("value")
        """
        self.vlan_priority = value  # Use property setter (gets validation)
        return self
