from abc import ABCMeta
from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, ARNumerical, Boolean, String
from ....M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean
from ....M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import AutosarDataType
from ....M2.AUTOSARTemplates.SWComponentTemplate.Components import SymbolProps


class AbstractImplementationDataTypeElement(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent, short_name: str):
        if type(self) is AbstractImplementationDataTypeElement:
            raise TypeError("AbstractImplementationDataTypeElement is an abstract class.")
        super().__init__(parent, short_name)


class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
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
        if (not self.IsElementExists(short_name)):
            type_element = ImplementationDataTypeElement(self, short_name)
            self.addElement(type_element)
            self.subElements.append(type_element)
        return self.getElement(short_name, ImplementationDataTypeElement)

    def getSubElements(self) -> List["ImplementationDataTypeElement"]:
        return self.subElements


class AbstractImplementationDataType(AutosarDataType, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AbstractImplementationDataType:
            raise NotImplementedError("AbstractImplementationDataType is an abstract class.")

        super().__init__(parent, short_name)


class ImplementationDataType(AbstractImplementationDataType):
    """
    Represents an implementation data type in AUTOSAR models.
    This class defines how data types are implemented in code, including arrays, structures, and data references.
    """

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

        # Profile for dynamic array size (for variable-size arrays)
        self.dynamicArraySizeProfile: String = None
        # Flag indicating if this structure contains optional elements
        self.isStructWithOptionalElement: Boolean = None
        # List of sub-elements in this implementation data type
        self.subElements: List['ImplementationDataTypeElement'] = []
        # Symbol properties for this implementation data type
        self.symbolProps: SymbolProps = None
        # Type emitter for code generation
        self.typeEmitter: ARLiteral = None

    def getDynamicArraySizeProfile(self):
        """
        Gets the profile for dynamic array size (for variable-size arrays).

        Returns:
            String: The dynamic array size profile
        """
        return self.dynamicArraySizeProfile

    def setDynamicArraySizeProfile(self, value):
        """
        Sets the profile for dynamic array size (for variable-size arrays).
        Only sets the value if it is not None.

        Args:
            value: The dynamic array size profile to set

        Returns:
            self for method chaining
        """
        self.dynamicArraySizeProfile = value
        return self

    def getIsStructWithOptionalElement(self):
        """
        Gets the flag indicating if this structure contains optional elements.

        Returns:
            Boolean: The flag for optional elements in structure
        """
        return self.isStructWithOptionalElement

    def setIsStructWithOptionalElement(self, value):
        """
        Sets the flag indicating if this structure contains optional elements.
        Only sets the value if it is not None.

        Args:
            value: The flag for optional elements in structure to set

        Returns:
            self for method chaining
        """
        self.isStructWithOptionalElement = value
        return self

    def createImplementationDataTypeElement(self, short_name: str) -> 'ImplementationDataTypeElement':
        """
        Creates and adds an ImplementationDataTypeElement to this implementation data type's sub-elements.

        Args:
            short_name: The short name for the new implementation data type element

        Returns:
            The created ImplementationDataTypeElement instance
        """
        if not self.IsElementExists(short_name):
            type_element = ImplementationDataTypeElement(self, short_name)
            self.addElement(type_element)
            self.subElements.append(type_element)
        return self.getElement(short_name)

    def getSubElements(self) -> List['ImplementationDataTypeElement']:
        """
        Gets the list of sub-elements in this implementation data type.

        Returns:
            List of ImplementationDataTypeElement instances
        """
        return self.subElements

    def getArrayElementType(self) -> str:
        """
        Gets the array element type for this implementation data type.
        This is an internal property used for tracking the array type.

        Returns:
            str: The array element type
        """
        return getattr(self, '_array_type', None)

    def setArrayElementType(self, type: str):
        """
        Sets the array element type for this implementation data type.
        This is an internal property used for tracking the array type.

        Args:
            type: The array element type to set

        Returns:
            self for method chaining
        """
        self._array_type = type
        return self

    def setTypeEmitter(self, emitter: str):
        """
        Sets the type emitter for code generation for this implementation data type.
        The type emitter defines how the type should be emitted in generated code.

        Args:
            emitter: The type emitter to set

        Returns:
            self for method chaining
        """
        self.typeEmitter = emitter
        return self

    def getTypeEmitter(self) -> str:
        """
        Gets the type emitter for code generation for this implementation data type.
        The type emitter defines how the type should be emitted in generated code.

        Returns:
            str: The type emitter
        """
        return self.typeEmitter

    def setStructElementType(self, type: str):
        """
        Sets the structure element type for this implementation data type.
        This is an internal property used for tracking the structure type.

        Args:
            type: The structure element type to set

        Returns:
            self for method chaining
        """
        self._struct_type = type
        return self

    def getStructElementType(self) -> str:
        """
        Gets the structure element type for this implementation data type.
        This is an internal property used for tracking the structure type.

        Returns:
            str: The structure element type
        """
        return getattr(self, '_struct_type', None)

    def createSymbolProps(self, short_name: str) -> SymbolProps:
        """
        Creates and adds SymbolProps to this implementation data type.

        Args:
            short_name: The short name for the new symbol properties

        Returns:
            The created SymbolProps instance
        """
        if short_name not in self.elements:
            symbol_props = SymbolProps(self, short_name)
            self.addElement(symbol_props)
            self.symbolProps = symbol_props
        return self.symbolProps

    def getSymbolProps(self) -> SymbolProps:
        """
        Gets the symbol properties for this implementation data type.

        Returns:
            SymbolProps: The symbol properties
        """
        return self.symbolProps
