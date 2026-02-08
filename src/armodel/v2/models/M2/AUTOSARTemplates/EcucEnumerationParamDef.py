from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    EcucEnumerationLiteral,
    EcucParameterDef,
    Identifier,
)


class EcucEnumerationParamDef(EcucParameterDef):
    """
    Configuration parameter type for Enumeration.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucEnumerationParamDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 66, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 186, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Default value of the enumeration configuration parameter.
        # needs to be one of the literals specified for this.
        self._defaultValue: Optional["Identifier"] = None

    @property
    def default_value(self) -> Optional["Identifier"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["Identifier"]) -> None:
        """
        Set defaultValue with validation.

        Args:
            value: The defaultValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultValue = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"defaultValue must be Identifier or None, got {type(value).__name__}"
            )
        self._defaultValue = value
        # Aggregation on the literals used to define this parameter.
        # This aggregation is optional if the has the category the of the EcucModuleDef
                # is set to this mandatory.
        self._literal: List["EcucEnumerationLiteral"] = []

    @property
    def literal(self) -> List["EcucEnumerationLiteral"]:
        """Get literal (Pythonic accessor)."""
        return self._literal

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "Identifier") -> "EcucEnumerationParamDef":
        """
        AUTOSAR-compliant setter for defaultValue with method chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_value property setter (gets validation automatically)
        """
        self.default_value = value  # Delegates to property setter
        return self

    def getLiteral(self) -> List["EcucEnumerationLiteral"]:
        """
        AUTOSAR-compliant getter for literal.

        Returns:
            The literal value

        Note:
            Delegates to literal property (CODING_RULE_V2_00017)
        """
        return self.literal  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional["Identifier"]) -> "EcucEnumerationParamDef":
        """
        Set defaultValue and return self for chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_value("value")
        """
        self.default_value = value  # Use property setter (gets validation)
        return self
