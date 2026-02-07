from typing import Optional


class DiagnosticEnvModeCondition(DiagnosticEnvCompareCondition):
    """
    DiagnosticEnvModeCondition are atomic condition based on the comparison of
    the active Mode Declaration in a ModeDeclarationGroupProtoype with the
    constant value of a ModeDeclaration. The formulation of this condition uses
    only one DiagnosticEnvElement, which contains enough information to deduce
    the variable part (i.e. the part that changes at runtime) as well as the
    constant part of the comparison. Only DiagnosticCompareTypeEnum.isEqual or
    DiagnosticCompareTypeEnum.isNotEqual are eligible values for
    DiagnosticAtomicCondition.compareType.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvModeCondition

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 88, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference represents both the ModeDeclaration and the ModeDeclaration
        # relevant for the.
        self._modeElement: Optional["DiagnosticEnvMode"] = None

    @property
    def mode_element(self) -> Optional["DiagnosticEnvMode"]:
        """Get modeElement (Pythonic accessor)."""
        return self._modeElement

    @mode_element.setter
    def mode_element(self, value: Optional["DiagnosticEnvMode"]) -> None:
        """
        Set modeElement with validation.

        Args:
            value: The modeElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeElement = None
            return

        if not isinstance(value, DiagnosticEnvMode):
            raise TypeError(
                f"modeElement must be DiagnosticEnvMode or None, got {type(value).__name__}"
            )
        self._modeElement = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeElement(self) -> "DiagnosticEnvMode":
        """
        AUTOSAR-compliant getter for modeElement.

        Returns:
            The modeElement value

        Note:
            Delegates to mode_element property (CODING_RULE_V2_00017)
        """
        return self.mode_element  # Delegates to property

    def setModeElement(self, value: "DiagnosticEnvMode") -> "DiagnosticEnvModeCondition":
        """
        AUTOSAR-compliant setter for modeElement with method chaining.

        Args:
            value: The modeElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_element property setter (gets validation automatically)
        """
        self.mode_element = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_element(self, value: Optional["DiagnosticEnvMode"]) -> "DiagnosticEnvModeCondition":
        """
        Set modeElement and return self for chaining.

        Args:
            value: The modeElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_element("value")
        """
        self.mode_element = value  # Use property setter (gets validation)
        return self
