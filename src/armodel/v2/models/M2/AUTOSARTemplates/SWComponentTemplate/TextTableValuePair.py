from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import Numerical
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TextTableValuePair(ARObject):
    """
    Defines a pair of text values which are translated into each other.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::TextTableValuePair

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 146, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Value of first DataPrototype provided similar to a which is intended to be a
                # Primitive data element.
        # Note that the is a variant, it can be computed by a.
        self._firstValue: Optional["Numerical"] = None

    @property
    def first_value(self) -> Optional["Numerical"]:
        """Get firstValue (Pythonic accessor)."""
        return self._firstValue

    @first_value.setter
    def first_value(self, value: Optional["Numerical"]) -> None:
        """
        Set firstValue with validation.

        Args:
            value: The firstValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstValue = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"firstValue must be Numerical or None, got {type(value).__name__}"
            )
        self._firstValue = value
        # Value of second DataPrototype provided similar to a which is intended to be a
                # Primitive data element.
        # Note that the is a variant, it can be computed by a.
        self._secondValue: Optional["Numerical"] = None

    @property
    def second_value(self) -> Optional["Numerical"]:
        """Get secondValue (Pythonic accessor)."""
        return self._secondValue

    @second_value.setter
    def second_value(self, value: Optional["Numerical"]) -> None:
        """
        Set secondValue with validation.

        Args:
            value: The secondValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondValue = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"secondValue must be Numerical or None, got {type(value).__name__}"
            )
        self._secondValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstValue(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for firstValue.

        Returns:
            The firstValue value

        Note:
            Delegates to first_value property (CODING_RULE_V2_00017)
        """
        return self.first_value  # Delegates to property

    def setFirstValue(self, value: "Numerical") -> "TextTableValuePair":
        """
        AUTOSAR-compliant setter for firstValue with method chaining.

        Args:
            value: The firstValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to first_value property setter (gets validation automatically)
        """
        self.first_value = value  # Delegates to property setter
        return self

    def getSecondValue(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for secondValue.

        Returns:
            The secondValue value

        Note:
            Delegates to second_value property (CODING_RULE_V2_00017)
        """
        return self.second_value  # Delegates to property

    def setSecondValue(self, value: "Numerical") -> "TextTableValuePair":
        """
        AUTOSAR-compliant setter for secondValue with method chaining.

        Args:
            value: The secondValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to second_value property setter (gets validation automatically)
        """
        self.second_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_first_value(self, value: Optional["Numerical"]) -> "TextTableValuePair":
        """
        Set firstValue and return self for chaining.

        Args:
            value: The firstValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_value("value")
        """
        self.first_value = value  # Use property setter (gets validation)
        return self

    def with_second_value(self, value: Optional["Numerical"]) -> "TextTableValuePair":
        """
        Set secondValue and return self for chaining.

        Args:
            value: The secondValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_value("value")
        """
        self.second_value = value  # Use property setter (gets validation)
        return self
