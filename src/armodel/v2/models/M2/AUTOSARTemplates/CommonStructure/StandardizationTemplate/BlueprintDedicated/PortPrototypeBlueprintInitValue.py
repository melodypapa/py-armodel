from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class PortPrototypeBlueprintInitValue(ARObject):
    """
    This meta-class represents the ability to express init values in
    PortPrototypeBlueprints. These init values act as a kind of blueprint from
    which for example proper ComSpecs can be derived.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintDedicated::Port

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 60, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the data prototype for which the init value applies.
        self._dataPrototype: RefType = None

    @property
    def data_prototype(self) -> RefType:
        """Get dataPrototype (Pythonic accessor)."""
        return self._dataPrototype

    @data_prototype.setter
    def data_prototype(self, value: RefType) -> None:
        """
        Set dataPrototype with validation.

        Args:
            value: The dataPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        self._dataPrototype = value
        # This is the init value for the particular data prototype.
        self._value: "ValueSpecification" = None

    @property
    def value(self) -> "ValueSpecification":
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: "ValueSpecification") -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"value must be ValueSpecification, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataPrototype(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataPrototype.

        Returns:
            The dataPrototype value

        Note:
            Delegates to data_prototype property (CODING_RULE_V2_00017)
        """
        return self.data_prototype  # Delegates to property

    def setDataPrototype(self, value: RefType) -> "PortPrototypeBlueprintInitValue":
        """
        AUTOSAR-compliant setter for dataPrototype with method chaining.

        Args:
            value: The dataPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_prototype property setter (gets validation automatically)
        """
        self.data_prototype = value  # Delegates to property setter
        return self

    def getValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "ValueSpecification") -> "PortPrototypeBlueprintInitValue":
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

    def with_data_prototype(self, value: RefType) -> "PortPrototypeBlueprintInitValue":
        """
        Set dataPrototype and return self for chaining.

        Args:
            value: The dataPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_prototype("value")
        """
        self.data_prototype = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: "ValueSpecification") -> "PortPrototypeBlueprintInitValue":
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
