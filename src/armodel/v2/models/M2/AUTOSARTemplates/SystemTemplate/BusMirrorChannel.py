from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class BusMirrorChannel(ARObject):
    """
    This element assigns a busMirrorNetworkId to the referenced channel.

    Package: M2::AUTOSARTemplates::SystemTemplate::BusMirror::BusMirrorChannel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 698, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the networkId of the communication.
        self._busMirror: Optional["PositiveInteger"] = None

    @property
    def bus_mirror(self) -> Optional["PositiveInteger"]:
        """Get busMirror (Pythonic accessor)."""
        return self._busMirror

    @bus_mirror.setter
    def bus_mirror(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set busMirror with validation.

        Args:
            value: The busMirror to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._busMirror = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"busMirror must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._busMirror = value
        # Reference to PhysicalChannel that is used in the bus sourceChannel or
                # targetChannel.
        # atpVariation.
        self._channel: Optional["PhysicalChannel"] = None

    @property
    def channel(self) -> Optional["PhysicalChannel"]:
        """Get channel (Pythonic accessor)."""
        return self._channel

    @channel.setter
    def channel(self, value: Optional["PhysicalChannel"]) -> None:
        """
        Set channel with validation.

        Args:
            value: The channel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._channel = None
            return

        if not isinstance(value, PhysicalChannel):
            raise TypeError(
                f"channel must be PhysicalChannel or None, got {type(value).__name__}"
            )
        self._channel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBusMirror(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for busMirror.

        Returns:
            The busMirror value

        Note:
            Delegates to bus_mirror property (CODING_RULE_V2_00017)
        """
        return self.bus_mirror  # Delegates to property

    def setBusMirror(self, value: "PositiveInteger") -> "BusMirrorChannel":
        """
        AUTOSAR-compliant setter for busMirror with method chaining.

        Args:
            value: The busMirror to set

        Returns:
            self for method chaining

        Note:
            Delegates to bus_mirror property setter (gets validation automatically)
        """
        self.bus_mirror = value  # Delegates to property setter
        return self

    def getChannel(self) -> "PhysicalChannel":
        """
        AUTOSAR-compliant getter for channel.

        Returns:
            The channel value

        Note:
            Delegates to channel property (CODING_RULE_V2_00017)
        """
        return self.channel  # Delegates to property

    def setChannel(self, value: "PhysicalChannel") -> "BusMirrorChannel":
        """
        AUTOSAR-compliant setter for channel with method chaining.

        Args:
            value: The channel to set

        Returns:
            self for method chaining

        Note:
            Delegates to channel property setter (gets validation automatically)
        """
        self.channel = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bus_mirror(self, value: Optional["PositiveInteger"]) -> "BusMirrorChannel":
        """
        Set busMirror and return self for chaining.

        Args:
            value: The busMirror to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bus_mirror("value")
        """
        self.bus_mirror = value  # Use property setter (gets validation)
        return self

    def with_channel(self, value: Optional["PhysicalChannel"]) -> "BusMirrorChannel":
        """
        Set channel and return self for chaining.

        Args:
            value: The channel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_channel("value")
        """
        self.channel = value  # Use property setter (gets validation)
        return self
