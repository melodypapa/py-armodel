from typing import Optional


class EcucFloatParamDef(EcucParameterDef):
    """
    Configuration parameter type for Float.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucFloatParamDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 61, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 186, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Default value of the float configuration parameter.
        self._defaultValue: Optional["Float"] = None

    @property
    def default_value(self) -> Optional["Float"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["Float"]) -> None:
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

        if not isinstance(value, Float):
            raise TypeError(
                f"defaultValue must be Float or None, got {type(value).__name__}"
            )
        self._defaultValue = value
        # Max value allowed for the parameter defined.
        # 318 Document ID 87: AUTOSAR_CP_TPS_ECUConfiguration ECU Configuration R23-11.
        self._max: Optional["Limit"] = None

    @property
    def max(self) -> Optional["Limit"]:
        """Get max (Pythonic accessor)."""
        return self._max

    @max.setter
    def max(self, value: Optional["Limit"]) -> None:
        """
        Set max with validation.

        Args:
            value: The max to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._max = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"max must be Limit or None, got {type(value).__name__}"
            )
        self._max = value
        # Min value allowed for the parameter defined.
        self._min: Optional["Limit"] = None

    @property
    def min(self) -> Optional["Limit"]:
        """Get min (Pythonic accessor)."""
        return self._min

    @min.setter
    def min(self, value: Optional["Limit"]) -> None:
        """
        Set min with validation.

        Args:
            value: The min to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._min = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"min must be Limit or None, got {type(value).__name__}"
            )
        self._min = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> "Float":
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "Float") -> "EcucFloatParamDef":
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

    def getMax(self) -> "Limit":
        """
        AUTOSAR-compliant getter for max.

        Returns:
            The max value

        Note:
            Delegates to max property (CODING_RULE_V2_00017)
        """
        return self.max  # Delegates to property

    def setMax(self, value: "Limit") -> "EcucFloatParamDef":
        """
        AUTOSAR-compliant setter for max with method chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Note:
            Delegates to max property setter (gets validation automatically)
        """
        self.max = value  # Delegates to property setter
        return self

    def getMin(self) -> "Limit":
        """
        AUTOSAR-compliant getter for min.

        Returns:
            The min value

        Note:
            Delegates to min property (CODING_RULE_V2_00017)
        """
        return self.min  # Delegates to property

    def setMin(self, value: "Limit") -> "EcucFloatParamDef":
        """
        AUTOSAR-compliant setter for min with method chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Note:
            Delegates to min property setter (gets validation automatically)
        """
        self.min = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional["Float"]) -> "EcucFloatParamDef":
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

    def with_max(self, value: Optional["Limit"]) -> "EcucFloatParamDef":
        """
        Set max and return self for chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max("value")
        """
        self.max = value  # Use property setter (gets validation)
        return self

    def with_min(self, value: Optional["Limit"]) -> "EcucFloatParamDef":
        """
        Set min and return self for chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min("value")
        """
        self.min = value  # Use property setter (gets validation)
        return self
