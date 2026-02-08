from typing import Optional


class GlobalTimeCanMaster(GlobalTimeMaster):
    """
    This represents the specialization of the GlobalTimeMaster for the CAN
    communication.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::CAN::GlobalTimeCanMaster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 864, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of whether or not CRC is supported.
        # This is relevant for selected bus systems.
        self._crcSecured: Optional["GlobalTimeCrcSupport"] = None

    @property
    def crc_secured(self) -> Optional["GlobalTimeCrcSupport"]:
        """Get crcSecured (Pythonic accessor)."""
        return self._crcSecured

    @crc_secured.setter
    def crc_secured(self, value: Optional["GlobalTimeCrcSupport"]) -> None:
        """
        Set crcSecured with validation.

        Args:
            value: The crcSecured to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcSecured = None
            return

        if not isinstance(value, GlobalTimeCrcSupport):
            raise TypeError(
                f"crcSecured must be GlobalTimeCrcSupport or None, got {type(value).__name__}"
            )
        self._crcSecured = value
        # This represents the value for the confirmation timeout.
        # seconds.
        self._sync: Optional["TimeValue"] = None

    @property
    def sync(self) -> Optional["TimeValue"]:
        """Get sync (Pythonic accessor)."""
        return self._sync

    @sync.setter
    def sync(self, value: Optional["TimeValue"]) -> None:
        """
        Set sync with validation.

        Args:
            value: The sync to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sync = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"sync must be TimeValue or None, got {type(value).__name__}"
            )
        self._sync = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCrcSecured(self) -> "GlobalTimeCrcSupport":
        """
        AUTOSAR-compliant getter for crcSecured.

        Returns:
            The crcSecured value

        Note:
            Delegates to crc_secured property (CODING_RULE_V2_00017)
        """
        return self.crc_secured  # Delegates to property

    def setCrcSecured(self, value: "GlobalTimeCrcSupport") -> "GlobalTimeCanMaster":
        """
        AUTOSAR-compliant setter for crcSecured with method chaining.

        Args:
            value: The crcSecured to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_secured property setter (gets validation automatically)
        """
        self.crc_secured = value  # Delegates to property setter
        return self

    def getSync(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for sync.

        Returns:
            The sync value

        Note:
            Delegates to sync property (CODING_RULE_V2_00017)
        """
        return self.sync  # Delegates to property

    def setSync(self, value: "TimeValue") -> "GlobalTimeCanMaster":
        """
        AUTOSAR-compliant setter for sync with method chaining.

        Args:
            value: The sync to set

        Returns:
            self for method chaining

        Note:
            Delegates to sync property setter (gets validation automatically)
        """
        self.sync = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crc_secured(self, value: Optional["GlobalTimeCrcSupport"]) -> "GlobalTimeCanMaster":
        """
        Set crcSecured and return self for chaining.

        Args:
            value: The crcSecured to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_secured("value")
        """
        self.crc_secured = value  # Use property setter (gets validation)
        return self

    def with_sync(self, value: Optional["TimeValue"]) -> "GlobalTimeCanMaster":
        """
        Set sync and return self for chaining.

        Args:
            value: The sync to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sync("value")
        """
        self.sync = value  # Use property setter (gets validation)
        return self
