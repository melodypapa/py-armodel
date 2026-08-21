from abc import ABC
from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean, AREnum, ARLiteral, ARNumerical, NameToken, String
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import AutosarDataType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import SymbolProps


class AbstractImplementationDataTypeElement(AtpStructureElement, ABC):
    """
    Abstract base class for implementation data type elements.
    """

    # AbstractImplementationDataTypeElement method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name: str):
        if type(self) is AbstractImplementationDataTypeElement:
            raise TypeError("AbstractImplementationDataTypeElement is an abstract class.")
        super().__init__(parent, short_name)


class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
    """
    Element of an implementation data type defining array properties,
    optional flag, sub-elements, and data definition properties.
    """

    # ImplementationDataTypeElement method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [x] test
    # [ ] getArrayImplPolicy           [x] impl  [ ] docstring  [x] test
    # [ ] setArrayImplPolicy           [x] impl  [ ] docstring  [x] test
    # [ ] getArraySize                 [x] impl  [ ] docstring  [x] test
    # [ ] setArraySize                 [x] impl  [ ] docstring  [x] test
    # [ ] getArraySizeHandling         [x] impl  [ ] docstring  [x] test
    # [ ] setArraySizeHandling         [x] impl  [ ] docstring  [x] test
    # [ ] getArraySizeSemantics        [x] impl  [ ] docstring  [x] test
    # [ ] setArraySizeSemantics        [x] impl  [ ] docstring  [x] test
    # [ ] getIsOptional                [x] impl  [ ] docstring  [x] test
    # [ ] setIsOptional                [x] impl  [ ] docstring  [x] test
    # [ ] getSwDataDefProps            [x] impl  [ ] docstring  [x] test
    # [ ] setSwDataDefProps            [x] impl  [ ] docstring  [x] test
    # [ ] createImplementationDataTypeElement [x] impl  [ ] docstring  [x] test
    # [ ] getSubElements               [x] impl  [ ] docstring  [x] test

    ARRAY_SIZE_SEMANTICS_FIXED_SIZE = "FIXED-SIZE"
    ARRAY_SIZE_SEMANTICS_VARIABLE_SIZE = "VARIABLE_SIZE"

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        self.arrayImplPolicy: ARLiteral = None
        self.arraySize: ARNumerical = None
        self.arraySizeHandling: ARLiteral = None
        self.arraySizeSemantics: ARLiteral = None
        self.isOptional: ARBoolean = None
        self.subElements: List[ImplementationDataTypeElement] = []
        self.swDataDefProps: SwDataDefProps = None

    def getArrayImplPolicy(self) -> ARLiteral:
        return self.arrayImplPolicy

    def setArrayImplPolicy(self, value: ARLiteral):
        if value is not None:
            self.arrayImplPolicy = value
        return self

    def getArraySize(self) -> ARNumerical:
        return self.arraySize

    def setArraySize(self, value: ARNumerical):
        if value is not None:
            self.arraySize = value
        return self

    def getArraySizeHandling(self) -> ARLiteral:
        return self.arraySizeHandling

    def setArraySizeHandling(self, value: ARLiteral):
        if value is not None:
            self.arraySizeHandling = value
        return self

    def getArraySizeSemantics(self):
        return self.arraySizeSemantics

    def setArraySizeSemantics(self, value):
        if value is not None:
            self.arraySizeSemantics = value
        return self

    def getIsOptional(self):
        return self.isOptional

    def setIsOptional(self, value):
        if value is not None:
            self.isOptional = value
        return self

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        if value is not None:
            self.swDataDefProps = value
        return self

    def createImplementationDataTypeElement(self, short_name: str) -> "ImplementationDataTypeElement":
        if not self.IsElementExists(short_name):
            type_element = ImplementationDataTypeElement(self, short_name)
            self.addElement(type_element)
            self.subElements.append(type_element)
        return self.getElement(short_name, ImplementationDataTypeElement)

    def getSubElements(self) -> List["ImplementationDataTypeElement"]:
        return self.subElements


class AbstractImplementationDataType(AutosarDataType, ABC):
    """
    Abstract base class for implementation data types.
    """

    # AbstractImplementationDataType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

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
        self.isStructWithOptionalElement: Optional[ARBoolean] = None
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

    def getIsStructWithOptionalElement(self) -> Optional[ARBoolean]:
        """
        Gets the flag indicating whether the ImplementationDataType has been
        created with the intention to define at least one element of the
        structure as optional.

        Returns:
            ARBoolean: The flag for optional elements in the structure
        """
        return self.isStructWithOptionalElement

    def setIsStructWithOptionalElement(self, value: Optional[ARBoolean]) -> "ImplementationDataType":
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
        if not self.IsElementExists(short_name):
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
        if short_name not in self.elements:
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
    Enumeration for array implementation policy.
    """

    # ArrayImplPolicyEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    DYNAMIC = "dynamic"
    STATIC = "static"

    def __init__(self):
        super().__init__(
            (
                ArrayImplPolicyEnum.DYNAMIC,
                ArrayImplPolicyEnum.STATIC,
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
