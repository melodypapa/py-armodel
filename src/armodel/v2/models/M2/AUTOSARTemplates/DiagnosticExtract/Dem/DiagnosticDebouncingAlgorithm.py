from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DiagnosticDebounceAlgorithmProps(Identifiable):
    """
    Defines properties for the debounce algorithm class.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticDebouncingAlgorithm

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 195, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 438, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Switch to store the debounce counter value non-volatile not.
        # counter value shall be stored non-volatile counter value is volatile that
                # this attribute is not relevant for the.
        self._debounce: Optional["Boolean"] = None

    @property
    def debounce(self) -> Optional["Boolean"]:
        """Get debounce (Pythonic accessor)."""
        return self._debounce

    @debounce.setter
    def debounce(self, value: Optional["Boolean"]) -> None:
        """
        Set debounce with validation.

        Args:
            value: The debounce to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._debounce = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"debounce must be Boolean or None, got {type(value).__name__}"
            )
        self._debounce = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDebounce(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for debounce.

        Returns:
            The debounce value

        Note:
            Delegates to debounce property (CODING_RULE_V2_00017)
        """
        return self.debounce  # Delegates to property

    def setDebounce(self, value: "Boolean") -> "DiagnosticDebounceAlgorithmProps":
        """
        AUTOSAR-compliant setter for debounce with method chaining.

        Args:
            value: The debounce to set

        Returns:
            self for method chaining

        Note:
            Delegates to debounce property setter (gets validation automatically)
        """
        self.debounce = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_debounce(self, value: Optional["Boolean"]) -> "DiagnosticDebounceAlgorithmProps":
        """
        Set debounce and return self for chaining.

        Args:
            value: The debounce to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_debounce("value")
        """
        self.debounce = value  # Use property setter (gets validation)
        return self
