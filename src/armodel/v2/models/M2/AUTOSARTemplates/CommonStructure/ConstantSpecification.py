from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import ValueSpecification
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


class ConstantSpecification(ARElement):
    """
    Specification of a constant that can be part of a package, i.e. it can be
    defined stand-alone.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ConstantSpecification

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 311, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 433, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specification of an expression leading to a value for this.
        self._valueSpec: Optional["ValueSpecification"] = None

    @property
    def value_spec(self) -> Optional["ValueSpecification"]:
        """Get valueSpec (Pythonic accessor)."""
        return self._valueSpec

    @value_spec.setter
    def value_spec(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set valueSpec with validation.

        Args:
            value: The valueSpec to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._valueSpec = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"valueSpec must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._valueSpec = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValueSpec(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for valueSpec.

        Returns:
            The valueSpec value

        Note:
            Delegates to value_spec property (CODING_RULE_V2_00017)
        """
        return self.value_spec  # Delegates to property

    def setValueSpec(self, value: "ValueSpecification") -> "ConstantSpecification":
        """
        AUTOSAR-compliant setter for valueSpec with method chaining.

        Args:
            value: The valueSpec to set

        Returns:
            self for method chaining

        Note:
            Delegates to value_spec property setter (gets validation automatically)
        """
        self.value_spec = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value_spec(self, value: Optional["ValueSpecification"]) -> "ConstantSpecification":
        """
        Set valueSpec and return self for chaining.

        Args:
            value: The valueSpec to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value_spec("value")
        """
        self.value_spec = value  # Use property setter (gets validation)
        return self
