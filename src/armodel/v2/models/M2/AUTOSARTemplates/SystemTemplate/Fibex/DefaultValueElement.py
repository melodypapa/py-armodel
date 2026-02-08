from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DefaultValueElement(ARObject):
    """
    The default value consists of a number of elements. Each element is one byte
    long and the number of elements is specified by SduLength.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 841, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The integer value of a freely defined data byte.
        self._elementByteValue: Optional["Integer"] = None

    @property
    def element_byte_value(self) -> Optional["Integer"]:
        """Get elementByteValue (Pythonic accessor)."""
        return self._elementByteValue

    @element_byte_value.setter
    def element_byte_value(self, value: Optional["Integer"]) -> None:
        """
        Set elementByteValue with validation.

        Args:
            value: The elementByteValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._elementByteValue = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"elementByteValue must be Integer or None, got {type(value).__name__}"
            )
        self._elementByteValue = value
        # This attribute specifies the byte position of the element default value.
        self._elementPosition: Optional["Integer"] = None

    @property
    def element_position(self) -> Optional["Integer"]:
        """Get elementPosition (Pythonic accessor)."""
        return self._elementPosition

    @element_position.setter
    def element_position(self, value: Optional["Integer"]) -> None:
        """
        Set elementPosition with validation.

        Args:
            value: The elementPosition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._elementPosition = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"elementPosition must be Integer or None, got {type(value).__name__}"
            )
        self._elementPosition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElementByteValue(self) -> "Integer":
        """
        AUTOSAR-compliant getter for elementByteValue.

        Returns:
            The elementByteValue value

        Note:
            Delegates to element_byte_value property (CODING_RULE_V2_00017)
        """
        return self.element_byte_value  # Delegates to property

    def setElementByteValue(self, value: "Integer") -> "DefaultValueElement":
        """
        AUTOSAR-compliant setter for elementByteValue with method chaining.

        Args:
            value: The elementByteValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to element_byte_value property setter (gets validation automatically)
        """
        self.element_byte_value = value  # Delegates to property setter
        return self

    def getElementPosition(self) -> "Integer":
        """
        AUTOSAR-compliant getter for elementPosition.

        Returns:
            The elementPosition value

        Note:
            Delegates to element_position property (CODING_RULE_V2_00017)
        """
        return self.element_position  # Delegates to property

    def setElementPosition(self, value: "Integer") -> "DefaultValueElement":
        """
        AUTOSAR-compliant setter for elementPosition with method chaining.

        Args:
            value: The elementPosition to set

        Returns:
            self for method chaining

        Note:
            Delegates to element_position property setter (gets validation automatically)
        """
        self.element_position = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_element_byte_value(self, value: Optional["Integer"]) -> "DefaultValueElement":
        """
        Set elementByteValue and return self for chaining.

        Args:
            value: The elementByteValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_element_byte_value("value")
        """
        self.element_byte_value = value  # Use property setter (gets validation)
        return self

    def with_element_position(self, value: Optional["Integer"]) -> "DefaultValueElement":
        """
        Set elementPosition and return self for chaining.

        Args:
            value: The elementPosition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_element_position("value")
        """
        self.element_position = value  # Use property setter (gets validation)
        return self
