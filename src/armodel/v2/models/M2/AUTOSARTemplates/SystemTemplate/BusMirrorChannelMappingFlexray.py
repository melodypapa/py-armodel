from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror import (
    BusMirrorChannelMapping,
)


class BusMirrorChannelMappingFlexray(BusMirrorChannelMapping):
    """
    This element defines the bus mirroring between a CAN, LIN or FlexRay
    sourceChannel and a FlexRay targetChannel.

    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 704, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Time in seconds after which the collection of source into the destination
                # frame is stopped and the sent at the latest.
        # destination frames are only sent when full or time stamp overflows.
        self._transmission: Optional["TimeValue"] = None

    @property
    def transmission(self) -> Optional["TimeValue"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["TimeValue"]) -> None:
        """
        Set transmission with validation.

        Args:
            value: The transmission to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"transmission must be TimeValue or None, got {type(value).__name__}"
            )
        self._transmission = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTransmission(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "TimeValue") -> "BusMirrorChannelMappingFlexray":
        """
        AUTOSAR-compliant setter for transmission with method chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_transmission(self, value: Optional["TimeValue"]) -> "BusMirrorChannelMappingFlexray":
        """
        Set transmission and return self for chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self
