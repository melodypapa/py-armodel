from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DiagnosticDataElement(Identifiable):
    """
    This meta-class represents the ability to describe a concrete piece of data
    to be taken into account for diagnostic purposes.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 41, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 982, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls the meaning of the value of the array size.
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
        # The existence of this attribute turns the data instance into array of data.
        # The attribute determines the size of the terms of how many elements the array
                # can take.
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
        # Size in bytes of scaling information for the DiagnosticData used with
        # DiagnosticReadScalingDataBy.
        self._scalingInfoSize: Optional["PositiveInteger"] = None

    @property
    def scaling_info_size(self) -> Optional["PositiveInteger"]:
        """Get scalingInfoSize (Pythonic accessor)."""
        return self._scalingInfoSize

    @scaling_info_size.setter
    def scaling_info_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set scalingInfoSize with validation.

        Args:
            value: The scalingInfoSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._scalingInfoSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"scalingInfoSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._scalingInfoSize = value
        # This property allows to specify data definition properties order to support
                # the definition of e.
        # g.
        # computation data constraints.
        self._swDataDef: Optional["SwDataDefProps"] = None

    @property
    def sw_data_def(self) -> Optional["SwDataDefProps"]:
        """Get swDataDef (Pythonic accessor)."""
        return self._swDataDef

    @sw_data_def.setter
    def sw_data_def(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set swDataDef with validation.

        Args:
            value: The swDataDef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swDataDef = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"swDataDef must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._swDataDef = value

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

    def setArraySize(self, value: "ArraySizeSemantics") -> "DiagnosticDataElement":
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

    def getMaxNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "PositiveInteger") -> "DiagnosticDataElement":
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

    def getScalingInfoSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for scalingInfoSize.

        Returns:
            The scalingInfoSize value

        Note:
            Delegates to scaling_info_size property (CODING_RULE_V2_00017)
        """
        return self.scaling_info_size  # Delegates to property

    def setScalingInfoSize(self, value: "PositiveInteger") -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant setter for scalingInfoSize with method chaining.

        Args:
            value: The scalingInfoSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to scaling_info_size property setter (gets validation automatically)
        """
        self.scaling_info_size = value  # Delegates to property setter
        return self

    def getSwDataDef(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for swDataDef.

        Returns:
            The swDataDef value

        Note:
            Delegates to sw_data_def property (CODING_RULE_V2_00017)
        """
        return self.sw_data_def  # Delegates to property

    def setSwDataDef(self, value: "SwDataDefProps") -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant setter for swDataDef with method chaining.

        Args:
            value: The swDataDef to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_data_def property setter (gets validation automatically)
        """
        self.sw_data_def = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_array_size(self, value: Optional["ArraySizeSemantics"]) -> "DiagnosticDataElement":
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

    def with_max_number_of(self, value: Optional["PositiveInteger"]) -> "DiagnosticDataElement":
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

    def with_scaling_info_size(self, value: Optional["PositiveInteger"]) -> "DiagnosticDataElement":
        """
        Set scalingInfoSize and return self for chaining.

        Args:
            value: The scalingInfoSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scaling_info_size("value")
        """
        self.scaling_info_size = value  # Use property setter (gets validation)
        return self

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "DiagnosticDataElement":
        """
        Set swDataDef and return self for chaining.

        Args:
            value: The swDataDef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_data_def("value")
        """
        self.sw_data_def = value  # Use property setter (gets validation)
        return self
