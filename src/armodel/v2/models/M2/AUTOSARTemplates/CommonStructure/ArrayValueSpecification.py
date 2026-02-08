from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    CompositeValueSpecification,
)


class ArrayValueSpecification(CompositeValueSpecification):
    """
    Specifies the values for an array.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 303, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 434, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1999, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The value for a single array element.
        # All Value aggregated by ArrayValueSpecification the same structure.
        # atpVariation.
        self._element: List["ValueSpecification"] = []

    @property
    def element(self) -> List["ValueSpecification"]:
        """Get element (Pythonic accessor)."""
        return self._element
        # This attribute shall only have a meaning for dynamic and shall be taken as a
        # sanity check: the number in the attribute shall be identical to the number of
        # attribute does not exist it means that no partial intended.
        self._intendedPartial: Optional["PositiveInteger"] = None

    @property
    def intended_partial(self) -> Optional["PositiveInteger"]:
        """Get intendedPartial (Pythonic accessor)."""
        return self._intendedPartial

    @intended_partial.setter
    def intended_partial(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set intendedPartial with validation.

        Args:
            value: The intendedPartial to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._intendedPartial = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"intendedPartial must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._intendedPartial = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElement(self) -> List["ValueSpecification"]:
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    def getIntendedPartial(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for intendedPartial.

        Returns:
            The intendedPartial value

        Note:
            Delegates to intended_partial property (CODING_RULE_V2_00017)
        """
        return self.intended_partial  # Delegates to property

    def setIntendedPartial(self, value: "PositiveInteger") -> "ArrayValueSpecification":
        """
        AUTOSAR-compliant setter for intendedPartial with method chaining.

        Args:
            value: The intendedPartial to set

        Returns:
            self for method chaining

        Note:
            Delegates to intended_partial property setter (gets validation automatically)
        """
        self.intended_partial = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_intended_partial(self, value: Optional["PositiveInteger"]) -> "ArrayValueSpecification":
        """
        Set intendedPartial and return self for chaining.

        Args:
            value: The intendedPartial to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_intended_partial("value")
        """
        self.intended_partial = value  # Use property setter (gets validation)
        return self
