from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.ApplicationCompositeElementDataPrototype import (
    ApplicationCompositeElementDataPrototype,
)


class ApplicationArrayElement(ApplicationCompositeElementDataPrototype):
    """
    Describes the properties of the elements of an application array data type.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 252, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 43, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls how the information about the array size shall be
        # interpreted.
        self._arraySize: Optional["ArraySizeSemantics"] = None

    @property
    def array_size(self) -> Optional["ArraySizeSemantics"]:
        """Get arraySize (Pythonic accessor)."""
        return self._arraySize

    @array_size.setter
    def array_size(self, value: Optional["ArraySizeSemantics"]) -> None:
        """
        Set arraySize with validation.

        Args:
            value: The arraySize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arraySize = None
            return

        if not isinstance(value, ArraySizeSemantics):
            raise TypeError(
                f"arraySize must be ArraySizeSemantics or None, got {type(value).__name__}"
            )
        self._arraySize = value
        # This reference can be taken to assign a CompuMethod of TEXTTABLE to the
                # array.
        # The texttable entries textual value to an index number such that with that
                # index number is represented by a.
        self._indexDataType: Optional["ApplicationPrimitive"] = None

    @property
    def index_data_type(self) -> Optional["ApplicationPrimitive"]:
        """Get indexDataType (Pythonic accessor)."""
        return self._indexDataType

    @index_data_type.setter
    def index_data_type(self, value: Optional["ApplicationPrimitive"]) -> None:
        """
        Set indexDataType with validation.

        Args:
            value: The indexDataType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._indexDataType = None
            return

        if not isinstance(value, ApplicationPrimitive):
            raise TypeError(
                f"indexDataType must be ApplicationPrimitive or None, got {type(value).__name__}"
            )
        self._indexDataType = value
        # The maximum number of elements that the array can.
        self._maxNumberOf: Optional["PositiveInteger"] = None

    @property
    def max_number_of(self) -> Optional["PositiveInteger"]:
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNumberOf with validation.

        Args:
            value: The maxNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOf = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxNumberOf must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArraySize(self) -> "ArraySizeSemantics":
        """
        AUTOSAR-compliant getter for arraySize.

        Returns:
            The arraySize value

        Note:
            Delegates to array_size property (CODING_RULE_V2_00017)
        """
        return self.array_size  # Delegates to property

    def setArraySize(self, value: "ArraySizeSemantics") -> "ApplicationArrayElement":
        """
        AUTOSAR-compliant setter for arraySize with method chaining.

        Args:
            value: The arraySize to set

        Returns:
            self for method chaining

        Note:
            Delegates to array_size property setter (gets validation automatically)
        """
        self.array_size = value  # Delegates to property setter
        return self

    def getIndexDataType(self) -> "ApplicationPrimitive":
        """
        AUTOSAR-compliant getter for indexDataType.

        Returns:
            The indexDataType value

        Note:
            Delegates to index_data_type property (CODING_RULE_V2_00017)
        """
        return self.index_data_type  # Delegates to property

    def setIndexDataType(self, value: "ApplicationPrimitive") -> "ApplicationArrayElement":
        """
        AUTOSAR-compliant setter for indexDataType with method chaining.

        Args:
            value: The indexDataType to set

        Returns:
            self for method chaining

        Note:
            Delegates to index_data_type property setter (gets validation automatically)
        """
        self.index_data_type = value  # Delegates to property setter
        return self

    def getMaxNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "PositiveInteger") -> "ApplicationArrayElement":
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_array_size(self, value: Optional["ArraySizeSemantics"]) -> "ApplicationArrayElement":
        """
        Set arraySize and return self for chaining.

        Args:
            value: The arraySize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_array_size("value")
        """
        self.array_size = value  # Use property setter (gets validation)
        return self

    def with_index_data_type(self, value: Optional["ApplicationPrimitive"]) -> "ApplicationArrayElement":
        """
        Set indexDataType and return self for chaining.

        Args:
            value: The indexDataType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_index_data_type("value")
        """
        self.index_data_type = value  # Use property setter (gets validation)
        return self

    def with_max_number_of(self, value: Optional["PositiveInteger"]) -> "ApplicationArrayElement":
        """
        Set maxNumberOf and return self for chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self
