from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SwPointerTargetProps(ARObject):
    """
    This element defines, that the data object (which is specified by the
    aggregating element) contains a reference to another data object or to a
    function in the CPU code. This corresponds to a pointer in the C-language.
    The attributes of this element describe the category and the detailed
    properties of the target which is either a data description or a function
    signature.

    Package: M2::MSR::DataDictionary::DataDefProperties

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 39, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 311, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 286, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 471, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced BswModuleEntry serves as the signature a function pointer
                # definition.
        # Primary use case: function as argument to other function.
        self._functionPointer: Optional["BswModuleEntry"] = None

    @property
    def function_pointer(self) -> Optional["BswModuleEntry"]:
        """Get functionPointer (Pythonic accessor)."""
        return self._functionPointer

    @function_pointer.setter
    def function_pointer(self, value: Optional["BswModuleEntry"]) -> None:
        """
        Set functionPointer with validation.

        Args:
            value: The functionPointer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._functionPointer = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"functionPointer must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._functionPointer = value
        # atpSplitable.
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
                # specify the category of data.
        # case of a function pointer, it could be used to denote of the referenced
                # BswModuleEntry.
        self._targetCategory: Optional["Identifier"] = None

    @property
    def target_category(self) -> Optional["Identifier"]:
        """Get targetCategory (Pythonic accessor)."""
        return self._targetCategory

    @target_category.setter
    def target_category(self, value: Optional["Identifier"]) -> None:
        """
        Set targetCategory with validation.

        Args:
            value: The targetCategory to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetCategory = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"targetCategory must be Identifier or None, got {type(value).__name__}"
            )
        self._targetCategory = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFunctionPointer(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for functionPointer.

        Returns:
            The functionPointer value

        Note:
            Delegates to function_pointer property (CODING_RULE_V2_00017)
        """
        return self.function_pointer  # Delegates to property

    def setFunctionPointer(self, value: "BswModuleEntry") -> "SwPointerTargetProps":
        """
        AUTOSAR-compliant setter for functionPointer with method chaining.

        Args:
            value: The functionPointer to set

        Returns:
            self for method chaining

        Note:
            Delegates to function_pointer property setter (gets validation automatically)
        """
        self.function_pointer = value  # Delegates to property setter
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

    def setSwDataDef(self, value: "SwDataDefProps") -> "SwPointerTargetProps":
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

    def getTargetCategory(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for targetCategory.

        Returns:
            The targetCategory value

        Note:
            Delegates to target_category property (CODING_RULE_V2_00017)
        """
        return self.target_category  # Delegates to property

    def setTargetCategory(self, value: "Identifier") -> "SwPointerTargetProps":
        """
        AUTOSAR-compliant setter for targetCategory with method chaining.

        Args:
            value: The targetCategory to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_category property setter (gets validation automatically)
        """
        self.target_category = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_function_pointer(self, value: Optional["BswModuleEntry"]) -> "SwPointerTargetProps":
        """
        Set functionPointer and return self for chaining.

        Args:
            value: The functionPointer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function_pointer("value")
        """
        self.function_pointer = value  # Use property setter (gets validation)
        return self

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "SwPointerTargetProps":
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

    def with_target_category(self, value: Optional["Identifier"]) -> "SwPointerTargetProps":
        """
        Set targetCategory and return self for chaining.

        Args:
            value: The targetCategory to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_category("value")
        """
        self.target_category = value  # Use property setter (gets validation)
        return self
