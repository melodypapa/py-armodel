
class PrimitiveAttributeCondition(AttributeCondition):
    """
    The PrimitiveAttributeCondition evaluates to true, if the referenced
    primitive attribute is accepted by all rules of this condition.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::PrimitiveAttributeCondition

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 104, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The primitive attribute that has to be accepted by the of this
        # PrimitiveAttributeCondition.
        self._attribute: "PrimitiveAttribute" = None

    @property
    def attribute(self) -> "PrimitiveAttribute":
        """Get attribute (Pythonic accessor)."""
        return self._attribute

    @attribute.setter
    def attribute(self, value: "PrimitiveAttribute") -> None:
        """
        Set attribute with validation.

        Args:
            value: The attribute to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PrimitiveAttribute):
            raise TypeError(
                f"attribute must be PrimitiveAttribute, got {type(value).__name__}"
            )
        self._attribute = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttribute(self) -> "PrimitiveAttribute":
        """
        AUTOSAR-compliant getter for attribute.

        Returns:
            The attribute value

        Note:
            Delegates to attribute property (CODING_RULE_V2_00017)
        """
        return self.attribute  # Delegates to property

    def setAttribute(self, value: "PrimitiveAttribute") -> "PrimitiveAttributeCondition":
        """
        AUTOSAR-compliant setter for attribute with method chaining.

        Args:
            value: The attribute to set

        Returns:
            self for method chaining

        Note:
            Delegates to attribute property setter (gets validation automatically)
        """
        self.attribute = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_attribute(self, value: "PrimitiveAttribute") -> "PrimitiveAttributeCondition":
        """
        Set attribute and return self for chaining.

        Args:
            value: The attribute to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_attribute("value")
        """
        self.attribute = value  # Use property setter (gets validation)
        return self
