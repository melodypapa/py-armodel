from typing import Optional


class DiagnosticEcuReset(DiagnosticServiceInstance):
    """
    This represents an instance of the "ECU Reset" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::EcuReset::DiagnosticEcuReset

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 102, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute shall be used to define a custom number if none of the
        # standardized values of shall be used.
        self._customSub: Optional["PositiveInteger"] = None

    @property
    def custom_sub(self) -> Optional["PositiveInteger"]:
        """Get customSub (Pythonic accessor)."""
        return self._customSub

    @custom_sub.setter
    def custom_sub(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set customSub with validation.

        Args:
            value: The customSub to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._customSub = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"customSub must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._customSub = value
        # This reference substantiates that abstract reference in the reference
        # represents the ability to access among all DiagnosticEcuReset in the.
        self._ecuResetClass: Optional["DiagnosticEcuReset"] = None

    @property
    def ecu_reset_class(self) -> Optional["DiagnosticEcuReset"]:
        """Get ecuResetClass (Pythonic accessor)."""
        return self._ecuResetClass

    @ecu_reset_class.setter
    def ecu_reset_class(self, value: Optional["DiagnosticEcuReset"]) -> None:
        """
        Set ecuResetClass with validation.

        Args:
            value: The ecuResetClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuResetClass = None
            return

        if not isinstance(value, DiagnosticEcuReset):
            raise TypeError(
                f"ecuResetClass must be DiagnosticEcuReset or None, got {type(value).__name__}"
            )
        self._ecuResetClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCustomSub(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for customSub.

        Returns:
            The customSub value

        Note:
            Delegates to custom_sub property (CODING_RULE_V2_00017)
        """
        return self.custom_sub  # Delegates to property

    def setCustomSub(self, value: "PositiveInteger") -> "DiagnosticEcuReset":
        """
        AUTOSAR-compliant setter for customSub with method chaining.

        Args:
            value: The customSub to set

        Returns:
            self for method chaining

        Note:
            Delegates to custom_sub property setter (gets validation automatically)
        """
        self.custom_sub = value  # Delegates to property setter
        return self

    def getEcuResetClass(self) -> "DiagnosticEcuReset":
        """
        AUTOSAR-compliant getter for ecuResetClass.

        Returns:
            The ecuResetClass value

        Note:
            Delegates to ecu_reset_class property (CODING_RULE_V2_00017)
        """
        return self.ecu_reset_class  # Delegates to property

    def setEcuResetClass(self, value: "DiagnosticEcuReset") -> "DiagnosticEcuReset":
        """
        AUTOSAR-compliant setter for ecuResetClass with method chaining.

        Args:
            value: The ecuResetClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_reset_class property setter (gets validation automatically)
        """
        self.ecu_reset_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_custom_sub(self, value: Optional["PositiveInteger"]) -> "DiagnosticEcuReset":
        """
        Set customSub and return self for chaining.

        Args:
            value: The customSub to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_custom_sub("value")
        """
        self.custom_sub = value  # Use property setter (gets validation)
        return self

    def with_ecu_reset_class(self, value: Optional["DiagnosticEcuReset"]) -> "DiagnosticEcuReset":
        """
        Set ecuResetClass and return self for chaining.

        Args:
            value: The ecuResetClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_reset_class("value")
        """
        self.ecu_reset_class = value  # Use property setter (gets validation)
        return self
