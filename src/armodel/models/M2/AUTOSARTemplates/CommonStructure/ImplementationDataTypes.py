from __future__ import annotations

from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, AREnum, NameToken, PositiveInteger, String
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import ArraySizeHandlingEnum, AutosarDataType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import SymbolProps


class AbstractImplementationDataTypeElement(AtpStructureElement, ABC):
    """
    This meta-class represents the ability to act as an abstract base class for specific derived meta-classes that support the modeling of ImplementationDataTypes for a particular language binding.
    """

    # AbstractImplementationDataTypeElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.16, p.269
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent, short_name: str):
        if type(self) is AbstractImplementationDataTypeElement:
            raise TypeError("AbstractImplementationDataTypeElement is an abstract class.")
        super().__init__(parent, short_name)


class ImplementationDataTypeElement(AbstractImplementationDataTypeElement, VariationPointCapable):
    """
    Declares a data object which is locally aggregated. Such an element can only be used within the scope where it is aggregated. This element either consists of further subElements or it is further defined via its swDataDefProps. There are several use cases within the system of ImplementationDataTypes fur such a local declaration: • It can represent the elements of an array, defining the element type and array size • It can represent an element of a struct, defining its type • It can be the local declaration of a debug element.
    """

    # ImplementationDataTypeElement method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.17, p.270
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getArrayImplPolicy                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setArrayImplPolicy                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getArraySize                          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setArraySize                          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getArraySizeHandling                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setArraySizeHandling                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getArraySizeSemantics                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setArraySizeSemantics                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIsOptional                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIsOptional                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwDataDefProps                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwDataDefProps                     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createImplementationDataTypeElement   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSubElements                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This attribute controls the implementation of the payload of an array. It shall only be used if the enclosing ImplementationDataType constitutes an array.
        self.arrayImplPolicy: Optional[ArrayImplPolicyEnum] = None

        # The existence of this attributes (if bigger than 0) defines the size of an array and declares that this ImplementationDataTypeElement represents the type of each single array element.
        self.arraySize: Optional[PositiveInteger] = None

        # The way how the size of the array is handled in case of a variable size array.
        self.arraySizeHandling: Optional[ArraySizeHandlingEnum] = None

        # This attribute controls the meaning of the value of the array size.
        self.arraySizeSemantics: Optional[ArraySizeSemanticsEnum] = None

        # This attribute represents the ability to declare the enclosing ImplementationDataTypeElement as optional. This means that, at runtime, the ImplementationDataTypeElement may or may not have a valid value and shall therefore be ignored. The underlying runtime software provides means to set the CppImplementationDataTypeElement as not valid at the sending end of a communication and determine its validity at the receiving end.
        self.isOptional: Optional[Boolean] = None

        # Element of an array, struct, or union in case of a nested declaration (i.e. without using "typedefs"). The aggregation of ImplementionDataTypeElement is subject to variability with the purpose to support the conditional existence of elements inside a ImplementationDataType representing a structure.
        self.subElements: List[ImplementationDataTypeElement] = []

        # The properties of this ImplementationDataTypeElement.
        self.swDataDefProps: Optional[SwDataDefProps] = None

    def getArrayImplPolicy(self) -> Optional[ArrayImplPolicyEnum]:
        """
        This attribute controls the implementation of the payload of an array. It shall only be used if the enclosing ImplementationDataType constitutes an array.
        """
        return self.arrayImplPolicy

    def setArrayImplPolicy(self, value: Optional[ArrayImplPolicyEnum]) -> ImplementationDataTypeElement:
        """
        This attribute controls the implementation of the payload of an array. It shall only be used if the enclosing ImplementationDataType constitutes an array. A None value is a no-op and does not overwrite an existing arrayImplPolicy.
        """
        if value is not None:
            self.arrayImplPolicy = value
        return self

    def getArraySize(self) -> Optional[PositiveInteger]:
        """
        The existence of this attributes (if bigger than 0) defines the size of an array and declares that this ImplementationDataTypeElement represents the type of each single array element.
        """
        return self.arraySize

    def setArraySize(self, value: Optional[PositiveInteger]) -> ImplementationDataTypeElement:
        """
        The existence of this attributes (if bigger than 0) defines the size of an array and declares that this ImplementationDataTypeElement represents the type of each single array element. A None value is a no-op and does not overwrite an existing arraySize.
        """
        if value is not None:
            self.arraySize = value
        return self

    def getArraySizeHandling(self) -> Optional[ArraySizeHandlingEnum]:
        """
        The way how the size of the array is handled in case of a variable size array.
        """
        return self.arraySizeHandling

    def setArraySizeHandling(self, value: Optional[ArraySizeHandlingEnum]) -> ImplementationDataTypeElement:
        """
        The way how the size of the array is handled in case of a variable size array. A None value is a no-op and does not overwrite an existing arraySizeHandling.
        """
        if value is not None:
            self.arraySizeHandling = value
        return self

    def getArraySizeSemantics(self) -> Optional[ArraySizeSemanticsEnum]:
        """
        This attribute controls the meaning of the value of the array size.
        """
        return self.arraySizeSemantics

    def setArraySizeSemantics(self, value: Optional[ArraySizeSemanticsEnum]) -> ImplementationDataTypeElement:
        """
        This attribute controls the meaning of the value of the array size. A None value is a no-op and does not overwrite an existing arraySizeSemantics.
        """
        if value is not None:
            self.arraySizeSemantics = value
        return self

    def getIsOptional(self) -> Optional[Boolean]:
        """
        This attribute represents the ability to declare the enclosing ImplementationDataTypeElement as optional. This means that, at runtime, the ImplementationDataTypeElement may or may not have a valid value and shall therefore be ignored. The underlying runtime software provides means to set the CppImplementationDataTypeElement as not valid at the sending end of a communication and determine its validity at the receiving end.
        """
        return self.isOptional

    def setIsOptional(self, value: Optional[Boolean]) -> ImplementationDataTypeElement:
        """
        This attribute represents the ability to declare the enclosing ImplementationDataTypeElement as optional. This means that, at runtime, the ImplementationDataTypeElement may or may not have a valid value and shall therefore be ignored. The underlying runtime software provides means to set the CppImplementationDataTypeElement as not valid at the sending end of a communication and determine its validity at the receiving end. A None value is a no-op and does not overwrite an existing isOptional.
        """
        if value is not None:
            self.isOptional = value
        return self

    def getSwDataDefProps(self) -> Optional[SwDataDefProps]:
        """
        The properties of this ImplementationDataTypeElement.
        """
        return self.swDataDefProps

    def setSwDataDefProps(self, value: Optional[SwDataDefProps]) -> ImplementationDataTypeElement:
        """
        The properties of this ImplementationDataTypeElement. A None value is a no-op and does not overwrite an existing swDataDefProps.
        """
        if value is not None:
            self.swDataDefProps = value
        return self

    def createImplementationDataTypeElement(self, short_name: str) -> ImplementationDataTypeElement:
        """
        Element of an array, struct, or union in case of a nested declaration (i.e. without using "typedefs"). The aggregation of ImplementionDataTypeElement is subject to variability with the purpose to support the conditional existence of elements inside a ImplementationDataType representing a structure.
        """
        if not self.IsElementExists(short_name, ImplementationDataTypeElement):
            type_element = ImplementationDataTypeElement(self, short_name)
            self.addElement(type_element)
            self.subElements.append(type_element)
        return self.getElement(short_name, ImplementationDataTypeElement)

    def getSubElements(self) -> List[ImplementationDataTypeElement]:
        """
        Element of an array, struct, or union in case of a nested declaration (i.e. without using "typedefs"). The aggregation of ImplementionDataTypeElement is subject to variability with the purpose to support the conditional existence of elements inside a ImplementationDataType representing a structure.
        """
        return self.subElements


class AbstractImplementationDataType(AutosarDataType, ABC):
    """This meta-class represents an abstract base class for different flavors of ImplementationDataType."""

    # AbstractImplementationDataType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.14, p.267
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractImplementationDataType:
            raise TypeError("AbstractImplementationDataType is an abstract class.")

        super().__init__(parent, short_name)


class ImplementationDataType(AbstractImplementationDataType):
    """
    Describes a reusable data type on the implementation level. This will
    typically correspond to a typedef in C-code.
    """

    # ImplementationDataType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf, Table D.37, p.321
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDynamicArraySizeProfile          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDynamicArraySizeProfile          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIsStructWithOptionalElement      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIsStructWithOptionalElement      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] createImplementationDataTypeElement [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSubElements                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createSymbolProps                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSymbolProps                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getTypeEmitter                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTypeEmitter                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    # Category constant for type reference implementation data types
    CATEGORY_TYPE_REFERENCE = "TYPE_REFERENCE"
    # Category constant for value implementation data types
    CATEGORY_TYPE_VALUE = "VALUE"
    # Category constant for structure implementation data types
    CATEGORY_TYPE_STRUCTURE = "STRUCTURE"
    # Category constant for data reference implementation data types
    CATEGORY_DATA_REFERENCE = "DATA_REFERENCE"
    # Category constant for array implementation data types
    CATEGORY_ARRAY = "ARRAY"

    def __init__(self, parent: ARObject, short_name: str):
        """
        Initializes the ImplementationDataType with a parent and short name.

        Args:
            parent: The parent ARObject that contains this implementation data type
            short_name: The unique short name of this implementation data type
        """
        super().__init__(parent, short_name)

        # Specifies the profile which the array will follow in case this data
        # type is a variable size array.
        self.dynamicArraySizeProfile: Optional[String] = None
        # Indicates that the ImplementationDataType has been created with the
        # intention to define at least one element of the structure as
        # optional.
        self.isStructWithOptionalElement: Optional[Boolean] = None
        # Specifies an element of an array, struct, or union data type.
        self.subElements: List[ImplementationDataTypeElement] = []
        # The SymbolProps for the ImplementationDataType.
        self.symbolProps: Optional[SymbolProps] = None
        # Controls which part of the AUTOSAR toolchain is supposed to trigger
        # data type definitions.
        self.typeEmitter: Optional[NameToken] = None

    def getDynamicArraySizeProfile(self) -> Optional[String]:
        """
        Gets the profile which the array will follow in case this data type is
        a variable size array.

        Returns:
            String: The dynamic array size profile
        """
        return self.dynamicArraySizeProfile

    def setDynamicArraySizeProfile(self, value: Optional[String]) -> "ImplementationDataType":
        """
        Sets the profile which the array will follow in case this data type is
        a variable size array. A None value is a no-op and does not overwrite
        an existing profile.

        Args:
            value: The dynamic array size profile to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dynamicArraySizeProfile = value
        return self

    def getIsStructWithOptionalElement(self) -> Optional[Boolean]:
        """
        Gets the flag indicating whether the ImplementationDataType has been
        created with the intention to define at least one element of the
        structure as optional.

        Returns:
            Boolean: The flag for optional elements in the structure
        """
        return self.isStructWithOptionalElement

    def setIsStructWithOptionalElement(self, value: Optional[Boolean]) -> "ImplementationDataType":
        """
        Sets the flag indicating whether the ImplementationDataType has been
        created with the intention to define at least one element of the
        structure as optional. A None value is a no-op and does not overwrite
        an existing flag.

        Args:
            value: The flag for optional elements in the structure to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.isStructWithOptionalElement = value
        return self

    def createImplementationDataTypeElement(self, short_name: str) -> ImplementationDataTypeElement:
        """
        Creates and adds an ImplementationDataTypeElement to this
        ImplementationDataType's sub-elements, or returns the existing element
        with the same short name.

        Args:
            short_name: The short name for the new implementation data type
                element

        Returns:
            The created ImplementationDataTypeElement instance
        """
        if not self.IsElementExists(short_name, ImplementationDataTypeElement):
            type_element = ImplementationDataTypeElement(self, short_name)
            self.addElement(type_element)
            self.subElements.append(type_element)
        return self.getElement(short_name, ImplementationDataTypeElement)

    def getSubElements(self) -> List[ImplementationDataTypeElement]:
        """
        Gets the list of sub-elements of this ImplementationDataType.

        Returns:
            List of ImplementationDataTypeElement instances
        """
        return self.subElements

    def createSymbolProps(self, short_name: str) -> SymbolProps:
        """
        Creates and adds the SymbolProps for this ImplementationDataType, or
        returns the existing SymbolProps.

        Args:
            short_name: The short name for the new SymbolProps

        Returns:
            The created SymbolProps instance
        """
        if not self.IsElementExists(short_name, SymbolProps):
            symbol_props = SymbolProps(self, short_name)
            self.addElement(symbol_props)
            self.symbolProps = symbol_props
        return self.symbolProps

    def getSymbolProps(self) -> Optional[SymbolProps]:
        """
        Gets the SymbolProps for this ImplementationDataType.

        Returns:
            SymbolProps: The symbol properties
        """
        return self.symbolProps

    def getTypeEmitter(self) -> Optional[NameToken]:
        """
        Gets the type emitter that controls which part of the AUTOSAR
        toolchain is supposed to trigger data type definitions.

        Returns:
            NameToken: The type emitter
        """
        return self.typeEmitter

    def setTypeEmitter(self, value: Optional[NameToken]) -> "ImplementationDataType":
        """
        Sets the type emitter that controls which part of the AUTOSAR
        toolchain is supposed to trigger data type definitions. A None value is
        a no-op and does not overwrite an existing type emitter.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.typeEmitter = value
        return self


class ArrayImplPolicyEnum(AREnum):
    """
    This meta-class provides values to configure the implementation of the payload part of an array.
    """

    # ArrayImplPolicyEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.18, p.276
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This configuration demands the implementation of the payload as an array. Tags: atp.EnumerationLiteralIndex=0
    PAYLOAD_AS_ARRAY = "payloadAsArray"

    # This configuration demands the implementation of the payload as a pointer to an array. Tags: atp.EnumerationLiteralIndex=1
    PAYLOAD_AS_POINTER_TO_ARRAY = "payloadAsPointerToArray"

    def __init__(self):
        super().__init__(
            (
                ArrayImplPolicyEnum.PAYLOAD_AS_ARRAY,
                ArrayImplPolicyEnum.PAYLOAD_AS_POINTER_TO_ARRAY,
            )
        )


class ArraySizeSemanticsEnum(AREnum):
    """
    This type controls how the information about the number of elements in an ApplicationArrayDataType is to be interpreted.
    """

    # ArraySizeSemanticsEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.10, p.253
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on ApplicationArrayElement.arraySizeSemantics, DiagnosticDataElement.arraySizeSemantics, ImplementationDataTypeElement.arraySizeSemantics, SwTextProps.arraySizeSemantics
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # This means that the ApplicationArrayDataType will always have a fixed number of elements. Tags: atp.EnumerationLiteralIndex=0
    FIXED_SIZE = "fixedSize"

    # This implies that the actual number of elements in the ApplicationArrayDataType might vary at run-time. The value of arraySize represents the maximum number of elements in the array. Tags: atp.EnumerationLiteralIndex=1
    VARIABLE_SIZE = "variableSize"

    def __init__(self):
        super().__init__(
            [
                ArraySizeSemanticsEnum.FIXED_SIZE,
                ArraySizeSemanticsEnum.VARIABLE_SIZE,
            ]
        )
