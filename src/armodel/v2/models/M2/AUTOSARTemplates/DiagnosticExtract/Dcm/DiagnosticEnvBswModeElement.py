from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticEnvModeElement,
    ModeDeclaration,
)


class DiagnosticEnvBswModeElement(DiagnosticEnvModeElement):
    """
    This meta-class represents the ability to refer to a specific
    ModeDeclaration in the scope of a BswModule Description.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvBswModeElement

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 90, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # the ModeDeclaration for the specific mode by: ModeInBswModule.
        self._mode: Optional["ModeDeclaration"] = None

    @property
    def mode(self) -> Optional["ModeDeclaration"]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set mode with validation.

        Args:
            value: The mode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"mode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._mode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: "ModeDeclaration") -> "DiagnosticEnvBswModeElement":
        """
        AUTOSAR-compliant setter for mode with method chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode(self, value: Optional["ModeDeclaration"]) -> "DiagnosticEnvBswModeElement":
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self
