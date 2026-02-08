from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class EthTSynCrcFlags(ARObject):
    """
    Defines the fields of the message which shall be taken into account for CRC
    calculation and verification.

    Package: M2::AUTOSARTemplates::SystemTemplate::GlobalTime::ETH

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 868, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # CorrectionField from the Follow_Up Message Header be included in CRC
        # calculation.
        self._crcCorrection: Optional["Boolean"] = None

    @property
    def crc_correction(self) -> Optional["Boolean"]:
        """Get crcCorrection (Pythonic accessor)."""
        return self._crcCorrection

    @crc_correction.setter
    def crc_correction(self, value: Optional["Boolean"]) -> None:
        """
        Set crcCorrection with validation.

        Args:
            value: The crcCorrection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcCorrection = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"crcCorrection must be Boolean or None, got {type(value).__name__}"
            )
        self._crcCorrection = value
        # DomainNumber from the Follow_Up Message Header be included in CRC
        # calculation.
        self._crcDomain: Optional["Boolean"] = None

    @property
    def crc_domain(self) -> Optional["Boolean"]:
        """Get crcDomain (Pythonic accessor)."""
        return self._crcDomain

    @crc_domain.setter
    def crc_domain(self, value: Optional["Boolean"]) -> None:
        """
        Set crcDomain with validation.

        Args:
            value: The crcDomain to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcDomain = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"crcDomain must be Boolean or None, got {type(value).__name__}"
            )
        self._crcDomain = value
        # MessageLength from the Follow_Up Message Header be included in CRC
        # calculation.
        self._crcMessage: Optional["Boolean"] = None

    @property
    def crc_message(self) -> Optional["Boolean"]:
        """Get crcMessage (Pythonic accessor)."""
        return self._crcMessage

    @crc_message.setter
    def crc_message(self, value: Optional["Boolean"]) -> None:
        """
        Set crcMessage with validation.

        Args:
            value: The crcMessage to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcMessage = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"crcMessage must be Boolean or None, got {type(value).__name__}"
            )
        self._crcMessage = value
        # PreciseOriginTimestamp from the Follow_Up Message shall be included in CRC
        # calculation.
        self._crcPrecise: Optional["Boolean"] = None

    @property
    def crc_precise(self) -> Optional["Boolean"]:
        """Get crcPrecise (Pythonic accessor)."""
        return self._crcPrecise

    @crc_precise.setter
    def crc_precise(self, value: Optional["Boolean"]) -> None:
        """
        Set crcPrecise with validation.

        Args:
            value: The crcPrecise to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcPrecise = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"crcPrecise must be Boolean or None, got {type(value).__name__}"
            )
        self._crcPrecise = value
        # SequenceId from the Follow_Up Message Header shall in CRC calculation.
        self._crcSequenceId: Optional["Boolean"] = None

    @property
    def crc_sequence_id(self) -> Optional["Boolean"]:
        """Get crcSequenceId (Pythonic accessor)."""
        return self._crcSequenceId

    @crc_sequence_id.setter
    def crc_sequence_id(self, value: Optional["Boolean"]) -> None:
        """
        Set crcSequenceId with validation.

        Args:
            value: The crcSequenceId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcSequenceId = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"crcSequenceId must be Boolean or None, got {type(value).__name__}"
            )
        self._crcSequenceId = value
        # SourcePortIdentity from the Follow_Up Message Header be included in CRC
        # calculation.
        self._crcSourcePort: Optional["Boolean"] = None

    @property
    def crc_source_port(self) -> Optional["Boolean"]:
        """Get crcSourcePort (Pythonic accessor)."""
        return self._crcSourcePort

    @crc_source_port.setter
    def crc_source_port(self, value: Optional["Boolean"]) -> None:
        """
        Set crcSourcePort with validation.

        Args:
            value: The crcSourcePort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcSourcePort = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"crcSourcePort must be Boolean or None, got {type(value).__name__}"
            )
        self._crcSourcePort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCrcCorrection(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for crcCorrection.

        Returns:
            The crcCorrection value

        Note:
            Delegates to crc_correction property (CODING_RULE_V2_00017)
        """
        return self.crc_correction  # Delegates to property

    def setCrcCorrection(self, value: "Boolean") -> "EthTSynCrcFlags":
        """
        AUTOSAR-compliant setter for crcCorrection with method chaining.

        Args:
            value: The crcCorrection to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_correction property setter (gets validation automatically)
        """
        self.crc_correction = value  # Delegates to property setter
        return self

    def getCrcDomain(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for crcDomain.

        Returns:
            The crcDomain value

        Note:
            Delegates to crc_domain property (CODING_RULE_V2_00017)
        """
        return self.crc_domain  # Delegates to property

    def setCrcDomain(self, value: "Boolean") -> "EthTSynCrcFlags":
        """
        AUTOSAR-compliant setter for crcDomain with method chaining.

        Args:
            value: The crcDomain to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_domain property setter (gets validation automatically)
        """
        self.crc_domain = value  # Delegates to property setter
        return self

    def getCrcMessage(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for crcMessage.

        Returns:
            The crcMessage value

        Note:
            Delegates to crc_message property (CODING_RULE_V2_00017)
        """
        return self.crc_message  # Delegates to property

    def setCrcMessage(self, value: "Boolean") -> "EthTSynCrcFlags":
        """
        AUTOSAR-compliant setter for crcMessage with method chaining.

        Args:
            value: The crcMessage to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_message property setter (gets validation automatically)
        """
        self.crc_message = value  # Delegates to property setter
        return self

    def getCrcPrecise(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for crcPrecise.

        Returns:
            The crcPrecise value

        Note:
            Delegates to crc_precise property (CODING_RULE_V2_00017)
        """
        return self.crc_precise  # Delegates to property

    def setCrcPrecise(self, value: "Boolean") -> "EthTSynCrcFlags":
        """
        AUTOSAR-compliant setter for crcPrecise with method chaining.

        Args:
            value: The crcPrecise to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_precise property setter (gets validation automatically)
        """
        self.crc_precise = value  # Delegates to property setter
        return self

    def getCrcSequenceId(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for crcSequenceId.

        Returns:
            The crcSequenceId value

        Note:
            Delegates to crc_sequence_id property (CODING_RULE_V2_00017)
        """
        return self.crc_sequence_id  # Delegates to property

    def setCrcSequenceId(self, value: "Boolean") -> "EthTSynCrcFlags":
        """
        AUTOSAR-compliant setter for crcSequenceId with method chaining.

        Args:
            value: The crcSequenceId to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_sequence_id property setter (gets validation automatically)
        """
        self.crc_sequence_id = value  # Delegates to property setter
        return self

    def getCrcSourcePort(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for crcSourcePort.

        Returns:
            The crcSourcePort value

        Note:
            Delegates to crc_source_port property (CODING_RULE_V2_00017)
        """
        return self.crc_source_port  # Delegates to property

    def setCrcSourcePort(self, value: "Boolean") -> "EthTSynCrcFlags":
        """
        AUTOSAR-compliant setter for crcSourcePort with method chaining.

        Args:
            value: The crcSourcePort to set

        Returns:
            self for method chaining

        Note:
            Delegates to crc_source_port property setter (gets validation automatically)
        """
        self.crc_source_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crc_correction(self, value: Optional["Boolean"]) -> "EthTSynCrcFlags":
        """
        Set crcCorrection and return self for chaining.

        Args:
            value: The crcCorrection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_correction("value")
        """
        self.crc_correction = value  # Use property setter (gets validation)
        return self

    def with_crc_domain(self, value: Optional["Boolean"]) -> "EthTSynCrcFlags":
        """
        Set crcDomain and return self for chaining.

        Args:
            value: The crcDomain to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_domain("value")
        """
        self.crc_domain = value  # Use property setter (gets validation)
        return self

    def with_crc_message(self, value: Optional["Boolean"]) -> "EthTSynCrcFlags":
        """
        Set crcMessage and return self for chaining.

        Args:
            value: The crcMessage to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_message("value")
        """
        self.crc_message = value  # Use property setter (gets validation)
        return self

    def with_crc_precise(self, value: Optional["Boolean"]) -> "EthTSynCrcFlags":
        """
        Set crcPrecise and return self for chaining.

        Args:
            value: The crcPrecise to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_precise("value")
        """
        self.crc_precise = value  # Use property setter (gets validation)
        return self

    def with_crc_sequence_id(self, value: Optional["Boolean"]) -> "EthTSynCrcFlags":
        """
        Set crcSequenceId and return self for chaining.

        Args:
            value: The crcSequenceId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_sequence_id("value")
        """
        self.crc_sequence_id = value  # Use property setter (gets validation)
        return self

    def with_crc_source_port(self, value: Optional["Boolean"]) -> "EthTSynCrcFlags":
        """
        Set crcSourcePort and return self for chaining.

        Args:
            value: The crcSourcePort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crc_source_port("value")
        """
        self.crc_source_port = value  # Use property setter (gets validation)
        return self
