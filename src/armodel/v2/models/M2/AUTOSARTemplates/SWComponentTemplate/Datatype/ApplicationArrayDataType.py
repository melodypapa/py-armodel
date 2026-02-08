from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ApplicationArray,
    ApplicationCompositeDataType,
    String,
)


class ApplicationArrayDataType(ApplicationCompositeDataType):
    """
    An application data type which is an array, each element is of the same
    application data type.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes::ApplicationArrayDataType

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 252, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1995, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 35, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the profile which the array will follow if it is a size array.
        self._dynamicArray: Optional["String"] = None

    @property
    def dynamic_array(self) -> Optional["String"]:
        """Get dynamicArray (Pythonic accessor)."""
        return self._dynamicArray

    @dynamic_array.setter
    def dynamic_array(self, value: Optional["String"]) -> None:
        """
        Set dynamicArray with validation.

        Args:
            value: The dynamicArray to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamicArray = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"dynamicArray must be String or None, got {type(value).__name__}"
            )
        self._dynamicArray = value
        # This association implements the concept of an array That is, in some cases it
                # is necessary to be able single array elements, e.
        # g.
        # as input values for routine.
        self._element: Optional["ApplicationArray"] = None

    @property
    def element(self) -> Optional["ApplicationArray"]:
        """Get element (Pythonic accessor)."""
        return self._element

    @element.setter
    def element(self, value: Optional["ApplicationArray"]) -> None:
        """
        Set element with validation.

        Args:
            value: The element to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._element = None
            return

        if not isinstance(value, ApplicationArray):
            raise TypeError(
                f"element must be ApplicationArray or None, got {type(value).__name__}"
            )
        self._element = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDynamicArray(self) -> "String":
        """
        AUTOSAR-compliant getter for dynamicArray.

        Returns:
            The dynamicArray value

        Note:
            Delegates to dynamic_array property (CODING_RULE_V2_00017)
        """
        return self.dynamic_array  # Delegates to property

    def setDynamicArray(self, value: "String") -> "ApplicationArrayDataType":
        """
        AUTOSAR-compliant setter for dynamicArray with method chaining.

        Args:
            value: The dynamicArray to set

        Returns:
            self for method chaining

        Note:
            Delegates to dynamic_array property setter (gets validation automatically)
        """
        self.dynamic_array = value  # Delegates to property setter
        return self

    def getElement(self) -> "ApplicationArray":
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    def setElement(self, value: "ApplicationArray") -> "ApplicationArrayDataType":
        """
        AUTOSAR-compliant setter for element with method chaining.

        Args:
            value: The element to set

        Returns:
            self for method chaining

        Note:
            Delegates to element property setter (gets validation automatically)
        """
        self.element = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dynamic_array(self, value: Optional["String"]) -> "ApplicationArrayDataType":
        """
        Set dynamicArray and return self for chaining.

        Args:
            value: The dynamicArray to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dynamic_array("value")
        """
        self.dynamic_array = value  # Use property setter (gets validation)
        return self

    def with_element(self, value: Optional["ApplicationArray"]) -> "ApplicationArrayDataType":
        """
        Set element and return self for chaining.

        Args:
            value: The element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_element("value")
        """
        self.element = value  # Use property setter (gets validation)
        return self
