from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf import (
    IEEE1722TpAcfBus,
)


class IEEE1722TpAcfLin(IEEE1722TpAcfBus):
    """
    ACF IEEE1722Tp bus used for LIN transport.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcf

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 666, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # CRF base frequency in Hz.
        self._baseFrequency: Optional["PositiveInteger"] = None

    @property
    def base_frequency(self) -> Optional["PositiveInteger"]:
        """Get baseFrequency (Pythonic accessor)."""
        return self._baseFrequency

    @base_frequency.setter
    def base_frequency(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set baseFrequency with validation.

        Args:
            value: The baseFrequency to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baseFrequency = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"baseFrequency must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._baseFrequency = value
        # Defines whether the "fs" (frame sync) shall be enabled.
        self._frameSync: Optional["Boolean"] = None

    @property
    def frame_sync(self) -> Optional["Boolean"]:
        """Get frameSync (Pythonic accessor)."""
        return self._frameSync

    @frame_sync.setter
    def frame_sync(self, value: Optional["Boolean"]) -> None:
        """
        Set frameSync with validation.

        Args:
            value: The frameSync to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frameSync = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"frameSync must be Boolean or None, got {type(value).__name__}"
            )
        self._frameSync = value
        # CRF timestamp interval as multiple of the baseFrequency.
        self._timestamp: Optional["PositiveInteger"] = None

    @property
    def timestamp(self) -> Optional["PositiveInteger"]:
        """Get timestamp (Pythonic accessor)."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set timestamp with validation.

        Args:
            value: The timestamp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timestamp = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"timestamp must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._timestamp = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaseFrequency(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for baseFrequency.

        Returns:
            The baseFrequency value

        Note:
            Delegates to base_frequency property (CODING_RULE_V2_00017)
        """
        return self.base_frequency  # Delegates to property

    def setBaseFrequency(self, value: "PositiveInteger") -> "IEEE1722TpAcfLin":
        """
        AUTOSAR-compliant setter for baseFrequency with method chaining.

        Args:
            value: The baseFrequency to set

        Returns:
            self for method chaining

        Note:
            Delegates to base_frequency property setter (gets validation automatically)
        """
        self.base_frequency = value  # Delegates to property setter
        return self

    def getFrameSync(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for frameSync.

        Returns:
            The frameSync value

        Note:
            Delegates to frame_sync property (CODING_RULE_V2_00017)
        """
        return self.frame_sync  # Delegates to property

    def setFrameSync(self, value: "Boolean") -> "IEEE1722TpAcfLin":
        """
        AUTOSAR-compliant setter for frameSync with method chaining.

        Args:
            value: The frameSync to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame_sync property setter (gets validation automatically)
        """
        self.frame_sync = value  # Delegates to property setter
        return self

    def getTimestamp(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for timestamp.

        Returns:
            The timestamp value

        Note:
            Delegates to timestamp property (CODING_RULE_V2_00017)
        """
        return self.timestamp  # Delegates to property

    def setTimestamp(self, value: "PositiveInteger") -> "IEEE1722TpAcfLin":
        """
        AUTOSAR-compliant setter for timestamp with method chaining.

        Args:
            value: The timestamp to set

        Returns:
            self for method chaining

        Note:
            Delegates to timestamp property setter (gets validation automatically)
        """
        self.timestamp = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base_frequency(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAcfLin":
        """
        Set baseFrequency and return self for chaining.

        Args:
            value: The baseFrequency to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base_frequency("value")
        """
        self.base_frequency = value  # Use property setter (gets validation)
        return self

    def with_frame_sync(self, value: Optional["Boolean"]) -> "IEEE1722TpAcfLin":
        """
        Set frameSync and return self for chaining.

        Args:
            value: The frameSync to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame_sync("value")
        """
        self.frame_sync = value  # Use property setter (gets validation)
        return self

    def with_timestamp(self, value: Optional["PositiveInteger"]) -> "IEEE1722TpAcfLin":
        """
        Set timestamp and return self for chaining.

        Args:
            value: The timestamp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timestamp("value")
        """
        self.timestamp = value  # Use property setter (gets validation)
        return self
