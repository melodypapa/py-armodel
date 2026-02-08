from typing import Optional


class ConcreteClassTailoring(DataFormatElementScope):
    """
    Tailoring of concrete meta classes.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::ConcreteClassTailoring

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 103, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specification if this concrete Meta-Class is a root element I.
        # e.
        # : The validation starts at an object of this and continues by following all
                # references that are in scope of this Point.
        self._validationRoot: Optional["Boolean"] = None

    @property
    def validation_root(self) -> Optional["Boolean"]:
        """Get validationRoot (Pythonic accessor)."""
        return self._validationRoot

    @validation_root.setter
    def validation_root(self, value: Optional["Boolean"]) -> None:
        """
        Set validationRoot with validation.

        Args:
            value: The validationRoot to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._validationRoot = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"validationRoot must be Boolean or None, got {type(value).__name__}"
            )
        self._validationRoot = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValidationRoot(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for validationRoot.

        Returns:
            The validationRoot value

        Note:
            Delegates to validation_root property (CODING_RULE_V2_00017)
        """
        return self.validation_root  # Delegates to property

    def setValidationRoot(self, value: "Boolean") -> "ConcreteClassTailoring":
        """
        AUTOSAR-compliant setter for validationRoot with method chaining.

        Args:
            value: The validationRoot to set

        Returns:
            self for method chaining

        Note:
            Delegates to validation_root property setter (gets validation automatically)
        """
        self.validation_root = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_validation_root(self, value: Optional["Boolean"]) -> "ConcreteClassTailoring":
        """
        Set validationRoot and return self for chaining.

        Args:
            value: The validationRoot to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_validation_root("value")
        """
        self.validation_root = value  # Use property setter (gets validation)
        return self
