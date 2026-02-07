from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class IndexedArrayElement(ARObject):
    """
    This element represents exactly one indexed element in the array. Either the
    applicationArrayElement or implementationArrayElement reference shall be
    used.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::IndexedArrayElement

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 237, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to an ApplicationArrayElement in an array.
        self._applicationArray: Optional["ApplicationArray"] = None

    @property
    def application_array(self) -> Optional["ApplicationArray"]:
        """Get applicationArray (Pythonic accessor)."""
        return self._applicationArray

    @application_array.setter
    def application_array(self, value: Optional["ApplicationArray"]) -> None:
        """
        Set applicationArray with validation.

        Args:
            value: The applicationArray to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._applicationArray = None
            return

        if not isinstance(value, ApplicationArray):
            raise TypeError(
                f"applicationArray must be ApplicationArray or None, got {type(value).__name__}"
            )
        self._applicationArray = value
        # Reference to an ImplementationDataTypeElement in an array.
        self._implementation: Optional["ImplementationData"] = None

    @property
    def implementation(self) -> Optional["ImplementationData"]:
        """Get implementation (Pythonic accessor)."""
        return self._implementation

    @implementation.setter
    def implementation(self, value: Optional["ImplementationData"]) -> None:
        """
        Set implementation with validation.

        Args:
            value: The implementation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implementation = None
            return

        if not isinstance(value, ImplementationData):
            raise TypeError(
                f"implementation must be ImplementationData or None, got {type(value).__name__}"
            )
        self._implementation = value
        # Position of an element in an array.
        # Starting position is 0.
        self._index: Optional["Integer"] = None

    @property
    def index(self) -> Optional["Integer"]:
        """Get index (Pythonic accessor)."""
        return self._index

    @index.setter
    def index(self, value: Optional["Integer"]) -> None:
        """
        Set index with validation.

        Args:
            value: The index to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._index = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"index must be Integer or None, got {type(value).__name__}"
            )
        self._index = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplicationArray(self) -> "ApplicationArray":
        """
        AUTOSAR-compliant getter for applicationArray.

        Returns:
            The applicationArray value

        Note:
            Delegates to application_array property (CODING_RULE_V2_00017)
        """
        return self.application_array  # Delegates to property

    def setApplicationArray(self, value: "ApplicationArray") -> "IndexedArrayElement":
        """
        AUTOSAR-compliant setter for applicationArray with method chaining.

        Args:
            value: The applicationArray to set

        Returns:
            self for method chaining

        Note:
            Delegates to application_array property setter (gets validation automatically)
        """
        self.application_array = value  # Delegates to property setter
        return self

    def getImplementation(self) -> "ImplementationData":
        """
        AUTOSAR-compliant getter for implementation.

        Returns:
            The implementation value

        Note:
            Delegates to implementation property (CODING_RULE_V2_00017)
        """
        return self.implementation  # Delegates to property

    def setImplementation(self, value: "ImplementationData") -> "IndexedArrayElement":
        """
        AUTOSAR-compliant setter for implementation with method chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Note:
            Delegates to implementation property setter (gets validation automatically)
        """
        self.implementation = value  # Delegates to property setter
        return self

    def getIndex(self) -> "Integer":
        """
        AUTOSAR-compliant getter for index.

        Returns:
            The index value

        Note:
            Delegates to index property (CODING_RULE_V2_00017)
        """
        return self.index  # Delegates to property

    def setIndex(self, value: "Integer") -> "IndexedArrayElement":
        """
        AUTOSAR-compliant setter for index with method chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Note:
            Delegates to index property setter (gets validation automatically)
        """
        self.index = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application_array(self, value: Optional["ApplicationArray"]) -> "IndexedArrayElement":
        """
        Set applicationArray and return self for chaining.

        Args:
            value: The applicationArray to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application_array("value")
        """
        self.application_array = value  # Use property setter (gets validation)
        return self

    def with_implementation(self, value: Optional["ImplementationData"]) -> "IndexedArrayElement":
        """
        Set implementation and return self for chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implementation("value")
        """
        self.implementation = value  # Use property setter (gets validation)
        return self

    def with_index(self, value: Optional["Integer"]) -> "IndexedArrayElement":
        """
        Set index and return self for chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_index("value")
        """
        self.index = value  # Use property setter (gets validation)
        return self
