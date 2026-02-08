from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    EcucParameterValue,
    VerbatimString,
)


class EcucTextualParamValue(EcucParameterValue):
    """
    Holding a value which is not subject to variation.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucTextualParamValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 127, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 443, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 190, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Value of the parameter, not subject to variant handling.
        self._value: Optional["VerbatimString"] = None

    @property
    def value(self) -> Optional["VerbatimString"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["VerbatimString"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"value must be VerbatimString or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "VerbatimString") -> "EcucTextualParamValue":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional["VerbatimString"]) -> "EcucTextualParamValue":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self
