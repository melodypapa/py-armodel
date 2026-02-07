from typing import Optional


class GlobalTimeFrSlave(GlobalTimeSlave):
    """
    This represents the specialization of the GlobalTimeSlave for Flexray
    communication.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::FR::GlobalTimeFrSlave

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 878, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of whether or not validation of the CRC is.
        self._crcValidated: Optional["GlobalTimeCrc"] = None

    @property
    def crc_validated(self) -> Optional["GlobalTimeCrc"]:
        """Get crcValidated (Pythonic accessor)."""
        return self._crcValidated

    @crc_validated.setter
    def crc_validated(self, value: Optional["GlobalTimeCrc"]) -> None:
        """
        Set crcValidated with validation.

        Args:
            value: The crcValidated to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcValidated = None
            return

        if not isinstance(value, GlobalTimeCrc):
            raise TypeError(
                f"crcValidated must be GlobalTimeCrc or None, got {type(value).__name__}"
            )
        self._crcValidated = value
        # Specifies the maximum allowed gap of the sequence between two SYNC resp.
        # two OFS messages.
        self._sequence: Optional["PositiveInteger"] = None

    @property
    def sequence(self) -> Optional["PositiveInteger"]:
        """Get sequence (Pythonic accessor)."""
        return self._sequence

    @sequence.setter
    def sequence(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sequence with validation.

        Args:
            value: The sequence to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sequence = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sequence must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sequence = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCrcValidated(self) -> "GlobalTimeCrc":
        """
        AUTOSAR-compliant getter for crcValidated.

        Returns:
            The crcValidated value

        Note:
            Delegates to crc_validated property (CODING_RULE_V2_00017)
        """
        return self.crc_validated  # Delegates to property

    def setCrcValidated(self, value: "GlobalTimeCrc") -> "GlobalTimeFrSlave":
        """
        AUTOSAR-compliant setter for crcValidated with method chaining.

        Args:
            value: The crcValidated to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_validated property setter (gets validation automatically)
        """
        self.crc_validated = value  # Delegates to property setter
        return self

    def getSequence(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sequence.

        Returns:
            The sequence value

        Note:
            Delegates to sequence property (CODING_RULE_V2_00017)
        """
        return self.sequence  # Delegates to property

    def setSequence(self, value: "PositiveInteger") -> "GlobalTimeFrSlave":
        """
        AUTOSAR-compliant setter for sequence with method chaining.

        Args:
            value: The sequence to set

        Returns:
            self for method chaining

        Note:
            Delegates to sequence property setter (gets validation automatically)
        """
        self.sequence = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crc_validated(self, value: Optional["GlobalTimeCrc"]) -> "GlobalTimeFrSlave":
        """
        Set crcValidated and return self for chaining.

        Args:
            value: The crcValidated to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_validated("value")
        """
        self.crc_validated = value  # Use property setter (gets validation)
        return self

    def with_sequence(self, value: Optional["PositiveInteger"]) -> "GlobalTimeFrSlave":
        """
        Set sequence and return self for chaining.

        Args:
            value: The sequence to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sequence("value")
        """
        self.sequence = value  # Use property setter (gets validation)
        return self
