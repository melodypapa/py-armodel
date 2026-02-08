from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    FrameTriggering,
)


class LinFrameTriggering(FrameTriggering):
    """
    LIN specific attributes to the FrameTriggering

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 428, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # To describe a frames identifier on the communication with a fixed
                # identifierValue.
        # For Lin attribute shall be ignored.
        self._identifier: Optional["Integer"] = None

    @property
    def identifier(self) -> Optional["Integer"]:
        """Get identifier (Pythonic accessor)."""
        return self._identifier

    @identifier.setter
    def identifier(self, value: Optional["Integer"]) -> None:
        """
        Set identifier with validation.

        Args:
            value: The identifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._identifier = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"identifier must be Integer or None, got {type(value).__name__}"
            )
        self._identifier = value
        # Type of checksum that the frame is using.
        # This attribute is in case of sporadic frames it should not.
        self._linChecksum: Optional["LinChecksumType"] = None

    @property
    def lin_checksum(self) -> Optional["LinChecksumType"]:
        """Get linChecksum (Pythonic accessor)."""
        return self._linChecksum

    @lin_checksum.setter
    def lin_checksum(self, value: Optional["LinChecksumType"]) -> None:
        """
        Set linChecksum with validation.

        Args:
            value: The linChecksum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._linChecksum = None
            return

        if not isinstance(value, LinChecksumType):
            raise TypeError(
                f"linChecksum must be LinChecksumType or None, got {type(value).__name__}"
            )
        self._linChecksum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIdentifier(self) -> "Integer":
        """
        AUTOSAR-compliant getter for identifier.

        Returns:
            The identifier value

        Note:
            Delegates to identifier property (CODING_RULE_V2_00017)
        """
        return self.identifier  # Delegates to property

    def setIdentifier(self, value: "Integer") -> "LinFrameTriggering":
        """
        AUTOSAR-compliant setter for identifier with method chaining.

        Args:
            value: The identifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to identifier property setter (gets validation automatically)
        """
        self.identifier = value  # Delegates to property setter
        return self

    def getLinChecksum(self) -> "LinChecksumType":
        """
        AUTOSAR-compliant getter for linChecksum.

        Returns:
            The linChecksum value

        Note:
            Delegates to lin_checksum property (CODING_RULE_V2_00017)
        """
        return self.lin_checksum  # Delegates to property

    def setLinChecksum(self, value: "LinChecksumType") -> "LinFrameTriggering":
        """
        AUTOSAR-compliant setter for linChecksum with method chaining.

        Args:
            value: The linChecksum to set

        Returns:
            self for method chaining

        Note:
            Delegates to lin_checksum property setter (gets validation automatically)
        """
        self.lin_checksum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_identifier(self, value: Optional["Integer"]) -> "LinFrameTriggering":
        """
        Set identifier and return self for chaining.

        Args:
            value: The identifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_identifier("value")
        """
        self.identifier = value  # Use property setter (gets validation)
        return self

    def with_lin_checksum(self, value: Optional["LinChecksumType"]) -> "LinFrameTriggering":
        """
        Set linChecksum and return self for chaining.

        Args:
            value: The linChecksum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lin_checksum("value")
        """
        self.lin_checksum = value  # Use property setter (gets validation)
        return self
