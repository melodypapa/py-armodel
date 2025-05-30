from abc import ABCMeta
from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, ARNumerical, Boolean, String
from ....M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean
from ....M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import AutosarDataType
from ....M2.AUTOSARTemplates.SWComponentTemplate.Components import SymbolProps


class AbstractImplementationDataTypeElement(Identifiable):
    def __init__(self, parent, short_name: str):
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

    CATEGORY_TYPE_REFERENCE = "TYPE_REFERENCE"
    CATEGORY_TYPE_VALUE = "VALUE"
    CATEGORY_TYPE_STRUCTURE = "STRUCTURE"
    CATEGORY_DATA_REFERENCE = "DATA_REFERENCE"
    CATEGORY_ARRAY = "ARRAY"

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dynamicArraySizeProfile = None             # type: String
        self.isStructWithOptionalElement = None         # type: Boolean
        
        self.subElements = []                           # type: List[ImplementationDataTypeElement]
        self.symbolProps = None                         # type: SymbolProps
        self.typeEmitter = None                         # type: ARLiteral

    def getDynamicArraySizeProfile(self):
        return self.dynamicArraySizeProfile

    def setDynamicArraySizeProfile(self, value):
        self.dynamicArraySizeProfile = value
        return self

    def getIsStructWithOptionalElement(self):
        return self.isStructWithOptionalElement

    def setIsStructWithOptionalElement(self, value):
        self.isStructWithOptionalElement = value
        return self

    def createImplementationDataTypeElement(self, short_name: str) -> ImplementationDataTypeElement:
        if not self.IsElementExists(short_name):
            type_element = ImplementationDataTypeElement(self, short_name)
            self.addElement(type_element)
            self.subElements.append(type_element)
        return self.getElement(short_name)

    def getSubElements(self) -> List[ImplementationDataTypeElement]:
        return self.subElements

    def getArrayElementType(self) -> str:
        return self._array_type

    def setArrayElementType(self, type: str):
        self._array_type = type
        return self

    def setTypeEmitter(self, emitter: str):
        self.typeEmitter = emitter
        return self
    
    def getTypeEmitter(self) -> str:
        return self.typeEmitter
    
    def setStructElementType(self, type: str):
        self._struct_type = type
        return self
    
    def getStructElementType(self) -> str:
        return self._struct_type
    
    def createSymbolProps(self, short_name: str) -> SymbolProps:
        if short_name not in self.elements:
            symbol_props = SymbolProps(self, short_name)
            self.addElement(symbol_props)
            self.symbolProps = symbol_props
        return self.symbolProps
    
    def getSymbolProps(self) -> SymbolProps:
        return self.symbolProps
