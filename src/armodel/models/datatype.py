from abc import ABCMeta
from typing import List

from .ar_object import ARLiteral, ARNumerical
from .ar_ref import RefType
from .ar_package import Referrable
from .general_structure import ARElement, ARObject, Identifiable
from .data_prototype import ApplicationCompositeElementDataPrototype, ApplicationRecordElement
from .data_dictionary import SwDataDefProps
from .common_structure import ImplementationDataTypeElement, ModeRequestTypeMap

class ImplementationProps(Referrable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ImplementationProps:
            raise NotImplementedError("ImplementationProps is an abstract class.")

        super().__init__(parent, short_name)
        self.symbol = ""

class SymbolProps(ImplementationProps):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.symbol = None    # type: ARLiteral

class BaseTypeDefinition(ARObject):
    def __init__(self):
        super().__init__()
    
class BaseTypeDirectDefinition(BaseTypeDefinition):
    def __init__(self):
        super().__init__()

        self.base_type_encoding = None
        self.base_type_size = None                # type: ARNumerical
        self.byteOrder = None                   # type: str
        self.mem_alignment = None                # type: ARNumerical
        self.native_declaration = None      

class BaseType(ARElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == BaseType:
            raise NotImplementedError("BaseType is an abstract class.")

        super().__init__(parent, short_name)

        self.baseTypeDefinition = BaseTypeDirectDefinition()

class SwBaseType(BaseType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

class AtpType(ARElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AtpType:
            raise NotImplementedError("AtpType is an abstract class.")

        super().__init__(parent, short_name)


class AutosarDataType(AtpType, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AutosarDataType:
            raise NotImplementedError("AutosarDataType is an abstract class.")

        super().__init__(parent, short_name)
        self.sw_data_def_props = None   # type: SwDataDefProps


class ApplicationDataType(AutosarDataType, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ApplicationDataType:
            raise NotImplementedError("ApplicationDataType is an abstract class.")

        super().__init__(parent, short_name)


class ApplicationPrimitiveDataType(ApplicationDataType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ApplicationCompositeDataType(ApplicationDataType, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ApplicationCompositeDataType:
            raise NotImplementedError("ApplicationCompositeDataType is an abstract class.")

        super().__init__(parent, short_name)

class ApplicationArrayElement(ApplicationCompositeElementDataPrototype):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.arraySizeHandling = None               # type: str
        self.arraySizeSemantics = None              # type: str
        self.indexDataTypeRef = None                # type: RefType
        self.maxNumberOfElements = None             # type: ARNumerical

    def setArraySizeHandling(self, handling: str):
        self.arraySizeHandling = handling
        return self
    
    def setArraySizeSemantics(self, semantics: str):
        self.arraySizeSemantics = semantics
        return self
    
    def setIndexDataTypeRef(self, ref: RefType):
        self.indexDataTypeRef = ref
        return self
    
    def setMaxNumberOfElements(self, number: ARNumerical):
        self.maxNumberOfElements = number
        return self

class ApplicationArrayDataType(ApplicationCompositeDataType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dynamic_array_size_profile = None      # type: ARLiteral
        self.element = None                         # type: ApplicationArrayElement

    def createApplicationArrayElement(self, short_name: str) -> ApplicationArrayElement:
        if (short_name not in self.elements):
            array_element = ApplicationArrayElement(self, short_name)
            self.elements[short_name] = array_element
            self.element = self.elements[short_name]
        return self.elements[short_name]
    
class ApplicationRecordDataType(ApplicationCompositeDataType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.record_elements = []

    def createApplicationRecordElement(self, short_name: str) -> ApplicationRecordElement:
        if (short_name not in self.elements):
            record_element = ApplicationRecordElement(self, short_name)
            self.elements[short_name] = record_element
            self.record_elements.append(self.elements[short_name])
        return self.elements[short_name]

    def getApplicationRecordElements(self) -> List[ApplicationRecordElement]:
        return self.record_elements

class AbstractImplementationDataType(AutosarDataType, metaclass=ABCMeta):
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
        
        self.sub_elements = []      # type: List[str]
        self._symbol_props = None    # type: SymbolProps
        self._type_emitter = None    # type: ARLiteral

        self._array_type = None     # ImplementationDataType
        self._struct_type = None    # ImplementationDataType

    #type:  ImplementationDataTypeElement
    def createImplementationDataTypeElement(self, short_name: str):
        self.sub_elements.append(short_name)
        if (short_name not in self.elements):
            event = ImplementationDataTypeElement(self, short_name)
            self.elements[short_name] = event
        return self.elements[short_name]

    def getImplementationDataTypeElements(self) -> List[ImplementationDataTypeElement]:
        elements = []
        for sub_element in self.sub_elements:
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
        if self._symbol_props is None:
            self._symbol_props = SymbolProps(self, short_name)
        return self._symbol_props
    
    def getSymbolProps(self) -> SymbolProps:
        return self._symbol_props


class DataTypeMap(ARObject):
    def __init__(self):
        self.application_data_type_ref = None       # type: RefType
        self.implementation_data_type_ref = None    # type: RefType

class DataTypeMappingSet(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        
        self._dataTypeMaps = []                     # type: List[DataTypeMap]
        self._modeRequestTypeMaps = []              # type: List[ModeRequestTypeMap]

    def addDataTypeMap(self, type_map: DataTypeMap):
        self._dataTypeMaps.append(type_map)

    def getDataTypeMaps(self) -> List[DataTypeMap]:
        return self._dataTypeMaps
    
    def addModeRequestTypeMap(self, map: ModeRequestTypeMap):
        self._modeRequestTypeMaps.append(map)

    def getModeRequestTypeMaps(self) -> List[ModeRequestTypeMap]:
        return self._modeRequestTypeMaps
    

