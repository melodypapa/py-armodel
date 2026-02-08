from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class StreamFilterRuleIpTp(ARObject):
    """
    Configuration of filter rules for IP and TP.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::StreamFilterRuleIpTp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 137, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Filter to match packets with the destination IPv6 address range.
        self._destination: Optional["StreamFilterIpv6"] = None

    @property
    def destination(self) -> Optional["StreamFilterIpv6"]:
        """Get destination (Pythonic accessor)."""
        return self._destination

    @destination.setter
    def destination(self, value: Optional["StreamFilterIpv6"]) -> None:
        """
        Set destination with validation.

        Args:
            value: The destination to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destination = None
            return

        if not isinstance(value, StreamFilterIpv6):
            raise TypeError(
                f"destination must be StreamFilterIpv6 or None, got {type(value).__name__}"
            )
        self._destination = value
        # Filter to match packets with the set of destination UDP/ ranges.
        self._destinationPort: List["StreamFilterPortRange"] = []

    @property
    def destination_port(self) -> List["StreamFilterPortRange"]:
        """Get destinationPort (Pythonic accessor)."""
        return self._destinationPort
        # Filter to match packets with the source IPv6 address range.
        self._source: Optional["StreamFilterIpv6"] = None

    @property
    def source(self) -> Optional["StreamFilterIpv6"]:
        """Get source (Pythonic accessor)."""
        return self._source

    @source.setter
    def source(self, value: Optional["StreamFilterIpv6"]) -> None:
        """
        Set source with validation.

        Args:
            value: The source to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._source = None
            return

        if not isinstance(value, StreamFilterIpv6):
            raise TypeError(
                f"source must be StreamFilterIpv6 or None, got {type(value).__name__}"
            )
        self._source = value
        # Filter to match packets with the set of source UDP/TCP.
        self._sourcePort: List["StreamFilterPortRange"] = []

    @property
    def source_port(self) -> List["StreamFilterPortRange"]:
        """Get sourcePort (Pythonic accessor)."""
        return self._sourcePort

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestination(self) -> "StreamFilterIpv6":
        """
        AUTOSAR-compliant getter for destination.

        Returns:
            The destination value

        Note:
            Delegates to destination property (CODING_RULE_V2_00017)
        """
        return self.destination  # Delegates to property

    def setDestination(self, value: "StreamFilterIpv6") -> "StreamFilterRuleIpTp":
        """
        AUTOSAR-compliant setter for destination with method chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination property setter (gets validation automatically)
        """
        self.destination = value  # Delegates to property setter
        return self

    def getDestinationPort(self) -> List["StreamFilterPortRange"]:
        """
        AUTOSAR-compliant getter for destinationPort.

        Returns:
            The destinationPort value

        Note:
            Delegates to destination_port property (CODING_RULE_V2_00017)
        """
        return self.destination_port  # Delegates to property

    def getSource(self) -> "StreamFilterIpv6":
        """
        AUTOSAR-compliant getter for source.

        Returns:
            The source value

        Note:
            Delegates to source property (CODING_RULE_V2_00017)
        """
        return self.source  # Delegates to property

    def setSource(self, value: "StreamFilterIpv6") -> "StreamFilterRuleIpTp":
        """
        AUTOSAR-compliant setter for source with method chaining.

        Args:
            value: The source to set

        Returns:
            self for method chaining

        Note:
            Delegates to source property setter (gets validation automatically)
        """
        self.source = value  # Delegates to property setter
        return self

    def getSourcePort(self) -> List["StreamFilterPortRange"]:
        """
        AUTOSAR-compliant getter for sourcePort.

        Returns:
            The sourcePort value

        Note:
            Delegates to source_port property (CODING_RULE_V2_00017)
        """
        return self.source_port  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination(self, value: Optional["StreamFilterIpv6"]) -> "StreamFilterRuleIpTp":
        """
        Set destination and return self for chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination("value")
        """
        self.destination = value  # Use property setter (gets validation)
        return self

    def with_source(self, value: Optional["StreamFilterIpv6"]) -> "StreamFilterRuleIpTp":
        """
        Set source and return self for chaining.

        Args:
            value: The source to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source("value")
        """
        self.source = value  # Use property setter (gets validation)
        return self
