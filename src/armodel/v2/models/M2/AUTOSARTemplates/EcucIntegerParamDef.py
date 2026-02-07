from typing import Optional


class EcucIntegerParamDef(EcucParameterDef):
    """
    Configuration parameter type for Integer.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucIntegerParamDef

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 60, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 187, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Default value of the integer configuration parameter.
        self._defaultValue: Optional["UnlimitedInteger"] = None

    @property
    def default_value(self) -> Optional["UnlimitedInteger"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["UnlimitedInteger"]) -> None:
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

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"defaultValue must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._defaultValue = value
        # Max value allowed for the parameter defined.
        self._max: Optional["UnlimitedInteger"] = None

    @property
    def max(self) -> Optional["UnlimitedInteger"]:
        """Get max (Pythonic accessor)."""
        return self._max

    @max.setter
    def max(self, value: Optional["UnlimitedInteger"]) -> None:
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

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"max must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._max = value
        # Min value allowed for the parameter defined.
        self._min: Optional["UnlimitedInteger"] = None

    @property
    def min(self) -> Optional["UnlimitedInteger"]:
        """Get min (Pythonic accessor)."""
        return self._min

    @min.setter
    def min(self, value: Optional["UnlimitedInteger"]) -> None:
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

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"min must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._min = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "UnlimitedInteger") -> "EcucIntegerParamDef":
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

    def getMax(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for max.

        Returns:
            The max value

        Note:
            Delegates to max property (CODING_RULE_V2_00017)
        """
        return self.max  # Delegates to property

    def setMax(self, value: "UnlimitedInteger") -> "EcucIntegerParamDef":
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

    def getMin(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for min.

        Returns:
            The min value

        Note:
            Delegates to min property (CODING_RULE_V2_00017)
        """
        return self.min  # Delegates to property

    def setMin(self, value: "UnlimitedInteger") -> "EcucIntegerParamDef":
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

    def with_default_value(self, value: Optional["UnlimitedInteger"]) -> "EcucIntegerParamDef":
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

    def with_max(self, value: Optional["UnlimitedInteger"]) -> "EcucIntegerParamDef":
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

    def with_min(self, value: Optional["UnlimitedInteger"]) -> "EcucIntegerParamDef":
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
