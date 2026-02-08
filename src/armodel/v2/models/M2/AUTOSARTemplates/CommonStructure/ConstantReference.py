from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Constants import ValueSpecification


class ConstantReference(ValueSpecification):
    """
    Instead of defining this value inline, a constant is referenced.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::ConstantReference

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 440, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced constant.
        self._constant: Optional["ConstantSpecification"] = None

    @property
    def constant(self) -> Optional["ConstantSpecification"]:
        """Get constant (Pythonic accessor)."""
        return self._constant

    @constant.setter
    def constant(self, value: Optional["ConstantSpecification"]) -> None:
        """
        Set constant with validation.

        Args:
            value: The constant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._constant = None
            return

        if not isinstance(value, ConstantSpecification):
            raise TypeError(
                f"constant must be ConstantSpecification or None, got {type(value).__name__}"
            )
        self._constant = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConstant(self) -> "ConstantSpecification":
        """
        AUTOSAR-compliant getter for constant.

        Returns:
            The constant value

        Note:
            Delegates to constant property (CODING_RULE_V2_00017)
        """
        return self.constant  # Delegates to property

    def setConstant(self, value: "ConstantSpecification") -> "ConstantReference":
        """
        AUTOSAR-compliant setter for constant with method chaining.

        Args:
            value: The constant to set

        Returns:
            self for method chaining

        Note:
            Delegates to constant property setter (gets validation automatically)
        """
        self.constant = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_constant(self, value: Optional["ConstantSpecification"]) -> "ConstantReference":
        """
        Set constant and return self for chaining.

        Args:
            value: The constant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_constant("value")
        """
        self.constant = value  # Use property setter (gets validation)
        return self
