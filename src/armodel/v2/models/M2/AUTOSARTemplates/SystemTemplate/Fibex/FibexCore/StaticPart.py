from typing import Optional


class StaticPart(MultiplexedPart):
    """
    Some parts/signals of the I-PDU may be the same regardless of the selector
    field. Such a part is called static part. The static part is optional.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::StaticPart

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 410, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a Com IPdu which is routed to the IPduM is combined to a
        # multiplexedPdu.
        self._iPdu: Optional["ISignalIPdu"] = None

    @property
    def i_pdu(self) -> Optional["ISignalIPdu"]:
        """Get iPdu (Pythonic accessor)."""
        return self._iPdu

    @i_pdu.setter
    def i_pdu(self, value: Optional["ISignalIPdu"]) -> None:
        """
        Set iPdu with validation.

        Args:
            value: The iPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iPdu = None
            return

        if not isinstance(value, ISignalIPdu):
            raise TypeError(
                f"iPdu must be ISignalIPdu or None, got {type(value).__name__}"
            )
        self._iPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPdu(self) -> "ISignalIPdu":
        """
        AUTOSAR-compliant getter for iPdu.

        Returns:
            The iPdu value

        Note:
            Delegates to i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_pdu  # Delegates to property

    def setIPdu(self, value: "ISignalIPdu") -> "StaticPart":
        """
        AUTOSAR-compliant setter for iPdu with method chaining.

        Args:
            value: The iPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to i_pdu property setter (gets validation automatically)
        """
        self.i_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_pdu(self, value: Optional["ISignalIPdu"]) -> "StaticPart":
        """
        Set iPdu and return self for chaining.

        Args:
            value: The iPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_pdu("value")
        """
        self.i_pdu = value  # Use property setter (gets validation)
        return self
