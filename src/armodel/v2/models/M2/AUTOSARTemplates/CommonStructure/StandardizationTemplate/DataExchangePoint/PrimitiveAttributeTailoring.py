from typing import List, Optional


class PrimitiveAttributeTailoring(AttributeTailoring):
    """
    Tailoring of primitive attributes. Primitive attributes are attributes that
    have a type which is marked by the stereotype <<primitive>> or
    <<enumeration>>

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::PrimitiveAttributeTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 111, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specification of how to handle AUTOSAR defined default values.
        self._defaultValue: Optional["DefaultValueApplication"] = None

    @property
    def default_value(self) -> Optional["DefaultValueApplication"]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional["DefaultValueApplication"]) -> None:
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

        if not isinstance(value, DefaultValueApplication):
            raise TypeError(
                f"defaultValue must be DefaultValueApplication or None, got {type(value).__name__}"
            )
        self._defaultValue = value
        # Tailors the attribute of a <<primitive>> data type.
        self._subAttribute: List["PrimitiveAttribute"] = []

    @property
    def sub_attribute(self) -> List["PrimitiveAttribute"]:
        """Get subAttribute (Pythonic accessor)."""
        return self._subAttribute
        # The restriction of the attribute value.
        self._valueRestrictionSeverity: Optional["ValueRestrictionWith"] = None

    @property
    def value_restriction_severity(self) -> Optional["ValueRestrictionWith"]:
        """Get valueRestrictionSeverity (Pythonic accessor)."""
        return self._valueRestrictionSeverity

    @value_restriction_severity.setter
    def value_restriction_severity(self, value: Optional["ValueRestrictionWith"]) -> None:
        """
        Set valueRestrictionSeverity with validation.

        Args:
            value: The valueRestrictionSeverity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._valueRestrictionSeverity = None
            return

        if not isinstance(value, ValueRestrictionWith):
            raise TypeError(
                f"valueRestrictionSeverity must be ValueRestrictionWith or None, got {type(value).__name__}"
            )
        self._valueRestrictionSeverity = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> "DefaultValueApplication":
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: "DefaultValueApplication") -> "PrimitiveAttributeTailoring":
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

    def getSubAttribute(self) -> List["PrimitiveAttribute"]:
        """
        AUTOSAR-compliant getter for subAttribute.

        Returns:
            The subAttribute value

        Note:
            Delegates to sub_attribute property (CODING_RULE_V2_00017)
        """
        return self.sub_attribute  # Delegates to property

    def getValueRestrictionSeverity(self) -> "ValueRestrictionWith":
        """
        AUTOSAR-compliant getter for valueRestrictionSeverity.

        Returns:
            The valueRestrictionSeverity value

        Note:
            Delegates to value_restriction_severity property (CODING_RULE_V2_00017)
        """
        return self.value_restriction_severity  # Delegates to property

    def setValueRestrictionSeverity(self, value: "ValueRestrictionWith") -> "PrimitiveAttributeTailoring":
        """
        AUTOSAR-compliant setter for valueRestrictionSeverity with method chaining.

        Args:
            value: The valueRestrictionSeverity to set

        Returns:
            self for method chaining

        Note:
            Delegates to value_restriction_severity property setter (gets validation automatically)
        """
        self.value_restriction_severity = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional["DefaultValueApplication"]) -> "PrimitiveAttributeTailoring":
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

    def with_value_restriction_severity(self, value: Optional["ValueRestrictionWith"]) -> "PrimitiveAttributeTailoring":
        """
        Set valueRestrictionSeverity and return self for chaining.

        Args:
            value: The valueRestrictionSeverity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value_restriction_severity("value")
        """
        self.value_restriction_severity = value  # Use property setter (gets validation)
        return self
