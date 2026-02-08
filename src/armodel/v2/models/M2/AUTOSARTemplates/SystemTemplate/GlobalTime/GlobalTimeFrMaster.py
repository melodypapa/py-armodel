from typing import Optional


class GlobalTimeFrMaster(GlobalTimeMaster):
    """
    This represents the specialization of the GlobalTimeMaster for Flexray
    communication.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::FR::GlobalTimeFrMaster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 877, Classic Platform R23-11)
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

    def setCrcSecured(self, value: "GlobalTimeCrcSupport") -> "GlobalTimeFrMaster":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crc_secured(self, value: Optional["GlobalTimeCrcSupport"]) -> "GlobalTimeFrMaster":
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
