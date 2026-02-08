from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    AbstractImplementationDataTypeElement,
    ArrayImplPolicyEnum,
    ArraySizeSemantics,
    ImplementationData,
    SwDataDefProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
    """
    Declares a data object which is locally aggregated. Such an element can only
    be used within the scope where it is aggregated. This element either
    consists of further subElements or it is further defined via its
    swDataDefProps. There are several use cases within the system of
    ImplementationDataTypes fur such a local declaration: • It can represent the
    elements of an array, defining the element type and array size • It can
    represent an element of a struct, defining its type • It can be the local
    declaration of a debug element.

    Package: M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes::ImplementationDataTypeElement

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 321, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 269, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2032, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 452, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls the implementation of the payload array.
        # It shall only be used if the enclosing an array.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._arrayImplPolicy: Optional["ArrayImplPolicyEnum"] = None

    @property
    def array_impl_policy(self) -> Optional["ArrayImplPolicyEnum"]:
        """Get arrayImplPolicy (Pythonic accessor)."""
        return self._arrayImplPolicy

    @array_impl_policy.setter
    def array_impl_policy(self, value: Optional["ArrayImplPolicyEnum"]) -> None:
        """
        Set arrayImplPolicy with validation.

        Args:
            value: The arrayImplPolicy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arrayImplPolicy = None
            return

        if not isinstance(value, ArrayImplPolicyEnum):
            raise TypeError(
                f"arrayImplPolicy must be ArrayImplPolicyEnum or None, got {type(value).__name__}"
            )
        self._arrayImplPolicy = value
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
        # This attribute represents the ability to declare the as optional.
        # that, at runtime, the ImplementationDataType or may not have a valid value
                # and shall ignored.
        # runtime software provides means to set as not valid at end of a communication
                # and determine its the receiving end.
        self._isOptional: Optional["Boolean"] = None

    @property
    def is_optional(self) -> Optional["Boolean"]:
        """Get isOptional (Pythonic accessor)."""
        return self._isOptional

    @is_optional.setter
    def is_optional(self, value: Optional["Boolean"]) -> None:
        """
        Set isOptional with validation.

        Args:
            value: The isOptional to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isOptional = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isOptional must be Boolean or None, got {type(value).__name__}"
            )
        self._isOptional = value
        # Element of an array, struct, or union in case of a nested declaration (i.
        # e.
        # without using "typedefs").
        # of ImplementionDataTypeElement is variability with the purpose to support the
                # of elements inside a Implementation a structure.
        # atpVariation.
        self._subElement: List["ImplementationData"] = []

    @property
    def sub_element(self) -> List["ImplementationData"]:
        """Get subElement (Pythonic accessor)."""
        return self._subElement
        # The properties of this ImplementationDataTypeElement.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArrayImplPolicy(self) -> "ArrayImplPolicyEnum":
        """
        AUTOSAR-compliant getter for arrayImplPolicy.

        Returns:
            The arrayImplPolicy value

        Note:
            Delegates to array_impl_policy property (CODING_RULE_V2_00017)
        """
        return self.array_impl_policy  # Delegates to property

    def setArrayImplPolicy(self, value: "ArrayImplPolicyEnum") -> "ImplementationDataTypeElement":
        """
        AUTOSAR-compliant setter for arrayImplPolicy with method chaining.

        Args:
            value: The arrayImplPolicy to set

        Returns:
            self for method chaining

        Note:
            Delegates to array_impl_policy property setter (gets validation automatically)
        """
        self.array_impl_policy = value  # Delegates to property setter
        return self

    def getArraySize(self) -> "ArraySizeSemantics":
        """
        AUTOSAR-compliant getter for arraySize.

        Returns:
            The arraySize value

        Note:
            Delegates to array_size property (CODING_RULE_V2_00017)
        """
        return self.array_size  # Delegates to property

    def setArraySize(self, value: "ArraySizeSemantics") -> "ImplementationDataTypeElement":
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

    def getIsOptional(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isOptional.

        Returns:
            The isOptional value

        Note:
            Delegates to is_optional property (CODING_RULE_V2_00017)
        """
        return self.is_optional  # Delegates to property

    def setIsOptional(self, value: "Boolean") -> "ImplementationDataTypeElement":
        """
        AUTOSAR-compliant setter for isOptional with method chaining.

        Args:
            value: The isOptional to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_optional property setter (gets validation automatically)
        """
        self.is_optional = value  # Delegates to property setter
        return self

    def getSubElement(self) -> List["ImplementationData"]:
        """
        AUTOSAR-compliant getter for subElement.

        Returns:
            The subElement value

        Note:
            Delegates to sub_element property (CODING_RULE_V2_00017)
        """
        return self.sub_element  # Delegates to property

    def getSwDataDef(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for swDataDef.

        Returns:
            The swDataDef value

        Note:
            Delegates to sw_data_def property (CODING_RULE_V2_00017)
        """
        return self.sw_data_def  # Delegates to property

    def setSwDataDef(self, value: "SwDataDefProps") -> "ImplementationDataTypeElement":
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

    def with_array_impl_policy(self, value: Optional["ArrayImplPolicyEnum"]) -> "ImplementationDataTypeElement":
        """
        Set arrayImplPolicy and return self for chaining.

        Args:
            value: The arrayImplPolicy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_array_impl_policy("value")
        """
        self.array_impl_policy = value  # Use property setter (gets validation)
        return self

    def with_array_size(self, value: Optional["ArraySizeSemantics"]) -> "ImplementationDataTypeElement":
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

    def with_is_optional(self, value: Optional["Boolean"]) -> "ImplementationDataTypeElement":
        """
        Set isOptional and return self for chaining.

        Args:
            value: The isOptional to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_optional("value")
        """
        self.is_optional = value  # Use property setter (gets validation)
        return self

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> "ImplementationDataTypeElement":
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
