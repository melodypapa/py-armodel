"""
AUTOSAR Package - ImplementationDataTypes

Package: M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    NameToken,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    AutosarDataType,
)


class AbstractImplementationDataType(AutosarDataType, ABC):
    """
    This meta-class represents an abstract base class for different flavors of
    ImplementationDataType.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes::AbstractImplementationDataType
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 267, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 42, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractImplementationDataType:
            raise TypeError("AbstractImplementationDataType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    def with_sub_element(self, value):
        """
        Set sub_element and return self for chaining.

        Args:
            value: The sub_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_element("value")
        """
        self.sub_element = value  # Use property setter (gets validation)
        return self

    def with_sub_element(self, value):
        """
        Set sub_element and return self for chaining.

        Args:
            value: The sub_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_element("value")
        """
        self.sub_element = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AbstractImplementationDataTypeElement(Identifiable, ABC):
    """
    This meta-class represents the ability to act as an abstract base class for
    specific derived meta-classes that support the modeling of
    ImplementationDataTypes for a particular language binding.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes::AbstractImplementationDataTypeElement
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 269, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractImplementationDataTypeElement:
            raise TypeError("AbstractImplementationDataTypeElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ImplementationDataType(AbstractImplementationDataType):
    """
    Describes a reusable data type on the implementation level. This will
    typically correspond to a typedef in C-code.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes::ImplementationDataType
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 320, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 230, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 299, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 268, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2031, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 47, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 451, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 193, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the profile which the array will follow in case this type is a
        # variable size array.
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"dynamicArray must be String or str or None, got {type(value).__name__}"
            )
        self._dynamicArray = value
        # of ImplementionDataTypeElement is variability with the purpose to support the
                # of elements inside a Implementation a structure.
        # atpVariation.
        self._subElement: List["ImplementationData"] = []

    @property
    def sub_element(self) -> List["ImplementationData"]:
        """Get subElement (Pythonic accessor)."""
        return self._subElement
        # This represents the SymbolProps for the Implementation.
        self._symbolProps: Optional["SymbolProps"] = None

    @property
    def symbol_props(self) -> Optional["SymbolProps"]:
        """Get symbolProps (Pythonic accessor)."""
        return self._symbolProps

    @symbol_props.setter
    def symbol_props(self, value: Optional["SymbolProps"]) -> None:
        """
        Set symbolProps with validation.
        
        Args:
            value: The symbolProps to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbolProps = None
            return

        if not isinstance(value, SymbolProps):
            raise TypeError(
                f"symbolProps must be SymbolProps or None, got {type(value).__name__}"
            )
        self._symbolProps = value
        # data type.
        self._typeEmitter: Optional["NameToken"] = None

    @property
    def type_emitter(self) -> Optional["NameToken"]:
        """Get typeEmitter (Pythonic accessor)."""
        return self._typeEmitter

    @type_emitter.setter
    def type_emitter(self, value: Optional["NameToken"]) -> None:
        """
        Set typeEmitter with validation.
        
        Args:
            value: The typeEmitter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._typeEmitter = None
            return

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"typeEmitter must be NameToken or str or None, got {type(value).__name__}"
            )
        self._typeEmitter = value

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

    def setDynamicArray(self, value: "String") -> "ImplementationDataType":
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

    def getSubElement(self) -> List["ImplementationData"]:
        """
        AUTOSAR-compliant getter for subElement.
        
        Returns:
            The subElement value
        
        Note:
            Delegates to sub_element property (CODING_RULE_V2_00017)
        """
        return self.sub_element  # Delegates to property

    def getSymbolProps(self) -> "SymbolProps":
        """
        AUTOSAR-compliant getter for symbolProps.
        
        Returns:
            The symbolProps value
        
        Note:
            Delegates to symbol_props property (CODING_RULE_V2_00017)
        """
        return self.symbol_props  # Delegates to property

    def setSymbolProps(self, value: "SymbolProps") -> "ImplementationDataType":
        """
        AUTOSAR-compliant setter for symbolProps with method chaining.
        
        Args:
            value: The symbolProps to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to symbol_props property setter (gets validation automatically)
        """
        self.symbol_props = value  # Delegates to property setter
        return self

    def getTypeEmitter(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for typeEmitter.
        
        Returns:
            The typeEmitter value
        
        Note:
            Delegates to type_emitter property (CODING_RULE_V2_00017)
        """
        return self.type_emitter  # Delegates to property

    def setTypeEmitter(self, value: "NameToken") -> "ImplementationDataType":
        """
        AUTOSAR-compliant setter for typeEmitter with method chaining.
        
        Args:
            value: The typeEmitter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to type_emitter property setter (gets validation automatically)
        """
        self.type_emitter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dynamic_array(self, value: Optional["String"]) -> "ImplementationDataType":
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

    def with_symbol_props(self, value: Optional["SymbolProps"]) -> "ImplementationDataType":
        """
        Set symbolProps and return self for chaining.
        
        Args:
            value: The symbolProps to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_symbol_props("value")
        """
        self.symbol_props = value  # Use property setter (gets validation)
        return self

    def with_type_emitter(self, value: Optional["NameToken"]) -> "ImplementationDataType":
        """
        Set typeEmitter and return self for chaining.
        
        Args:
            value: The typeEmitter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_type_emitter("value")
        """
        self.type_emitter = value  # Use property setter (gets validation)
        return self



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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isOptional must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isOptional = value
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


class ArraySizeSemanticsEnum(AREnum):
    """
    ArraySizeSemanticsEnum enumeration

This type controls how the information about the number of elements in an ApplicationArrayDataType is to be interpreted. Aggregated by ApplicationArrayElement.arraySizeSemantics, DiagnosticDataElement.arraySizeSemantics, ImplementationDataTypeElement.arraySizeSemantics, SwTextProps.arraySizeSemantics

Package: M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes
    """
    # Extract Template
    Diagnostic = "None"

    # CP R23-11
    AUTOSAR = "None"

    # This means that the ApplicationArrayDataType will always have a fixed number of elements.
    fixedSize = "0"

    # This implies that the actual number of elements in the ApplicationArrayDataType might vary at
    variableSize = "1"



class ArrayImplPolicyEnum(AREnum):
    """
    ArrayImplPolicyEnum enumeration

This meta-class provides values to configure the implementation of the payload part of an array. Aggregated by ImplementationDataTypeElement.arrayImplPolicy

Package: M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes
    """
    # This configuration demands the implementation of the payload as an array.
    payloadAsArray = "0"

    # This configuration demands the implementation of the payload as a pointer to an array.
    payloadAsPointerToArray = "1"
