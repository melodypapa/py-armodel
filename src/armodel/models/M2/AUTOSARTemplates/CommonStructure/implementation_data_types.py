from abc import ABCMeta
from typing import List

from ..GenericStructure.GeneralTemplateClasses.ArObject import ARObject

from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, ARNumerical

from ...MSR.DataDictionary.data_def_properties import SwDataDefProps
from ..GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean
from ....datatype import AutosarDataType
from ..SWComponentTemplate.components import SymbolProps

class AbstractImplementationDataTypeElement(Identifiable):
    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
    ARRAY_SIZE_SEMANTICS_FIXED_SIZE = "FIXED-SIZE"
    ARRAY_SIZE_SEMANTICS_VARIABLE_SIZE = "VARIABLE_SIZE"

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        self.arrayImplPolicy = None             # type: ARLiteral
        self.arraySize = None                   # type: ARNumerical
        self.arraySizeHandling = None           # type: ARLiteral
        self.arraySizeSemantics = None          # type: ARLiteral
        self.isOptional = None                  # type: ARBoolean
        self.swDataDefProps = None              # type: SwDataDefProps

    def getArrayImplPolicy(self):
        return self.arrayImplPolicy

    def setArrayImplPolicy(self, value):
        self.arrayImplPolicy = value
        return self

    def getArraySize(self):
        return self.arraySize

    def setArraySize(self, value):
        self.arraySize = value
        return self

    def getArraySizeHandling(self):
        return self.arraySizeHandling

    def setArraySizeHandling(self, value):
        self.arraySizeHandling = value
        return self

    def getArraySizeSemantics(self):
        return self.arraySizeSemantics

    def setArraySizeSemantics(self, value):
        self.arraySizeSemantics = value
        return self

    def getIsOptional(self):
        return self.isOptional

    def setIsOptional(self, value):
        self.isOptional = value
        return self

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        self.swDataDefProps = value
        return self
    
    def createImplementationDataTypeElement(self, short_name: str): # type: (...) -> ImplementationDataTypeElement
        if (short_name not in self.elements):
            event = ImplementationDataTypeElement(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]
    
    def getImplementationDataTypeElements(self):                    # type：(...) -> List[ImplementationDataTypeElement]
        return list(filter(lambda c: isinstance(c, ImplementationDataTypeElement), self.elements.values()))


class AbstractImplementationDataType(AutosarDataType, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AbstractImplementationDataType:
            raise NotImplementedError("AbstractImplementationDataType is an abstract class.")

        super().__init__(parent, short_name)

class ImplementationDataType(AbstractImplementationDataType):

    CATEGORY_TYPE_REFERENCE = "TYPE_REFERENCE"
    CATEGORY_TYPE_VALUE = "VALUE"
    CATEGORY_TYPE_STRUCTURE = "STRUCTURE"
    CATEGORY_DATA_REFERENCE = "DATA_REFERENCE"
    CATEGORY_ARRAY = "ARRAY"

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.arrayImplPolicy = None
        self.arraySize = None
        self.arraySizeHandling = None                   # type: ARLiteral
        self.arraySizeSemantics = None                  # type: ARLiteral
        
        self.subElements = []                           # type: List[str]
        self.symbolProps = None                         # type: SymbolProps
        self._type_emitter = None                       # type: ARLiteral

        self._array_type = None         # ImplementationDataType
        self._struct_type = None        # ImplementationDataType

    
    def createImplementationDataTypeElement(self, short_name: str) -> ImplementationDataTypeElement:     
        self.subElements.append(short_name)
        if (short_name not in self.elements):
            event = ImplementationDataTypeElement(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getImplementationDataTypeElements(self) -> List[ImplementationDataTypeElement]:
        elements = []
        for sub_element in self.subElements:
            elements.append(self.elements[sub_element])
        return elements
        # return filter(lambda c: isinstance(c, ImplementationDataTypeElement), self.elements.values())

    def getArrayElementType(self) -> str:
        return self._array_type

    def setArrayElementType(self, type: str):
        self._array_type = type
        return self

    def setTypeEmitter(self, emitter: str):
        self._type_emitter = emitter
        return self
    
    def getTypeEmitter(self) -> str:
        return self._type_emitter
    
    def setStructElementType(self, type: str):
        self._struct_type = type
        return self
    
    def getStructElementType(self) -> str:
        return self._struct_type
    
    def createSymbolProps(self, short_name: str) -> SymbolProps:
        if short_name not in self.element:
            symbol_props = SymbolProps(self, short_name)
            self.elements[short_name] = symbol_props
            self.symbolProps = symbol_props
        return self.symbolProps
    
    def getSymbolProps(self) -> SymbolProps:
        return self.symbolProps