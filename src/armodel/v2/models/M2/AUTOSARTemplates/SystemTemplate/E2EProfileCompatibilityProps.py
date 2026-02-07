from typing import Optional


class E2EProfileCompatibilityProps(ARElement):
    """
    This meta-class collects settings for configuration of the E2E state
    machine.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::E2EProfileCompatibilityProps

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 202, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 807, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # E2E State machine behavior concerning transition from to INVALID no direct
        # transition from NODATA to transition from INIT to INVALID due to (Autosar
        # R19-11 or former direct transition from NODATA to INVALID from INIT to
        # INVALID due to covered (state machine extended).
        self._transitToInvalid: Optional["Boolean"] = None

    @property
    def transit_to_invalid(self) -> Optional["Boolean"]:
        """Get transitToInvalid (Pythonic accessor)."""
        return self._transitToInvalid

    @transit_to_invalid.setter
    def transit_to_invalid(self, value: Optional["Boolean"]) -> None:
        """
        Set transitToInvalid with validation.

        Args:
            value: The transitToInvalid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transitToInvalid = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"transitToInvalid must be Boolean or None, got {type(value).__name__}"
            )
        self._transitToInvalid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTransitToInvalid(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for transitToInvalid.

        Returns:
            The transitToInvalid value

        Note:
            Delegates to transit_to_invalid property (CODING_RULE_V2_00017)
        """
        return self.transit_to_invalid  # Delegates to property

    def setTransitToInvalid(self, value: "Boolean") -> "E2EProfileCompatibilityProps":
        """
        AUTOSAR-compliant setter for transitToInvalid with method chaining.

        Args:
            value: The transitToInvalid to set

        Returns:
            self for method chaining

        Note:
            Delegates to transit_to_invalid property setter (gets validation automatically)
        """
        self.transit_to_invalid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_transit_to_invalid(self, value: Optional["Boolean"]) -> "E2EProfileCompatibilityProps":
        """
        Set transitToInvalid and return self for chaining.

        Args:
            value: The transitToInvalid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transit_to_invalid("value")
        """
        self.transit_to_invalid = value  # Use property setter (gets validation)
        return self
