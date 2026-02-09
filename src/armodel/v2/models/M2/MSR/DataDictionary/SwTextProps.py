from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SwTextProps(ARObject):
    """
    This meta-class expresses particular properties applicable to strings in
    variables or calibration parameters.

    Package: M2::MSR::DataDictionary::DataDefProperties

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 343, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 313, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 249, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 216, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls the semantics of the arraysize for the array
                # representing the string in an Implementation there to support a safe
                # conversion between ImplementationDatatype, even length strings as required e.
        # g.
        # for Support of.
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
        # In baseType denotes the intended encoding of in the string on level of
                # ApplicationData.
        self._baseType: Optional["SwBaseType"] = None

    @property
    def base_type(self) -> Optional["SwBaseType"]:
        """Get baseType (Pythonic accessor)."""
        return self._baseType

    @base_type.setter
    def base_type(self, value: Optional["SwBaseType"]) -> None:
        """
        Set baseType with validation.

        Args:
            value: The baseType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baseType = None
            return

        if not isinstance(value, SwBaseType):
            raise TypeError(
                f"baseType must be SwBaseType or None, got {type(value).__name__}"
            )
        self._baseType = value
        # will be interpreted according to the encoding the associated base type of the
                # data object, (hex) represents the ASCII character zero as and 0 (dec)
                # represents an end of string as of the fill character depends on the
                # arraySize.
        self._swFillCharacter: Optional["Integer"] = None

    @property
    def sw_fill_character(self) -> Optional["Integer"]:
        """Get swFillCharacter (Pythonic accessor)."""
        return self._swFillCharacter

    @sw_fill_character.setter
    def sw_fill_character(self, value: Optional["Integer"]) -> None:
        """
        Set swFillCharacter with validation.

        Args:
            value: The swFillCharacter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swFillCharacter = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"swFillCharacter must be Integer or None, got {type(value).__name__}"
            )
        self._swFillCharacter = value
        # Note the bytes depends on the encoding in the.
        self._swMaxTextSize: Optional["Integer"] = None

    @property
    def sw_max_text_size(self) -> Optional["Integer"]:
        """Get swMaxTextSize (Pythonic accessor)."""
        return self._swMaxTextSize

    @sw_max_text_size.setter
    def sw_max_text_size(self, value: Optional["Integer"]) -> None:
        """
        Set swMaxTextSize with validation.

        Args:
            value: The swMaxTextSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swMaxTextSize = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"swMaxTextSize must be Integer or None, got {type(value).__name__}"
            )
        self._swMaxTextSize = value

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

    def setArraySize(self, value: "ArraySizeSemantics") -> "SwTextProps":
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

    def getBaseType(self) -> "SwBaseType":
        """
        AUTOSAR-compliant getter for baseType.

        Returns:
            The baseType value

        Note:
            Delegates to base_type property (CODING_RULE_V2_00017)
        """
        return self.base_type  # Delegates to property

    def setBaseType(self, value: "SwBaseType") -> "SwTextProps":
        """
        AUTOSAR-compliant setter for baseType with method chaining.

        Args:
            value: The baseType to set

        Returns:
            self for method chaining

        Note:
            Delegates to base_type property setter (gets validation automatically)
        """
        self.base_type = value  # Delegates to property setter
        return self

    def getSwFillCharacter(self) -> "Integer":
        """
        AUTOSAR-compliant getter for swFillCharacter.

        Returns:
            The swFillCharacter value

        Note:
            Delegates to sw_fill_character property (CODING_RULE_V2_00017)
        """
        return self.sw_fill_character  # Delegates to property

    def setSwFillCharacter(self, value: "Integer") -> "SwTextProps":
        """
        AUTOSAR-compliant setter for swFillCharacter with method chaining.

        Args:
            value: The swFillCharacter to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_fill_character property setter (gets validation automatically)
        """
        self.sw_fill_character = value  # Delegates to property setter
        return self

    def getSwMaxTextSize(self) -> "Integer":
        """
        AUTOSAR-compliant getter for swMaxTextSize.

        Returns:
            The swMaxTextSize value

        Note:
            Delegates to sw_max_text_size property (CODING_RULE_V2_00017)
        """
        return self.sw_max_text_size  # Delegates to property

    def setSwMaxTextSize(self, value: "Integer") -> "SwTextProps":
        """
        AUTOSAR-compliant setter for swMaxTextSize with method chaining.

        Args:
            value: The swMaxTextSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_max_text_size property setter (gets validation automatically)
        """
        self.sw_max_text_size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_array_size(self, value: Optional["ArraySizeSemantics"]) -> "SwTextProps":
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

    def with_base_type(self, value: Optional["SwBaseType"]) -> "SwTextProps":
        """
        Set baseType and return self for chaining.

        Args:
            value: The baseType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_base_type("value")
        """
        self.base_type = value  # Use property setter (gets validation)
        return self

    def with_sw_fill_character(self, value: Optional["Integer"]) -> "SwTextProps":
        """
        Set swFillCharacter and return self for chaining.

        Args:
            value: The swFillCharacter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_fill_character("value")
        """
        self.sw_fill_character = value  # Use property setter (gets validation)
        return self

    def with_sw_max_text_size(self, value: Optional["Integer"]) -> "SwTextProps":
        """
        Set swMaxTextSize and return self for chaining.

        Args:
            value: The swMaxTextSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_max_text_size("value")
        """
        self.sw_max_text_size = value  # Use property setter (gets validation)
        return self
