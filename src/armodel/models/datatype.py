from abc import ABCMeta
from typing import List
from .general_structure import ARElement, Referrable, ARObject
from .data_prototype import ApplicationArrayElement, ApplicationRecordElement
from .data_dictionary import SwDataDefProps
from .common_structure import ImplementationDataTypeElement


class ImplementationProps(Referrable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == ImplementationProps:
            raise NotImplementedError("ImplementationProps is an abstract class.")

        super().__init__(parent, short_name)
        self.symbol = ""


class SymbolProps(ImplementationProps):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class BaseType(ARElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == BaseType:
            raise NotImplementedError("BaseType is an abstract class.")

        super().__init__(parent, short_name)
        self.base_type_definition = None  # Type: BaseTypeDefinition


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


class ApplicationArrayDataType(ApplicationCompositeDataType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dynamic_array_size_profile = ""
        self.element = None


class ApplicationRecordDataType(ApplicationCompositeDataType):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

    def createApplicationRecordElement(self, short_name: str) -> ApplicationRecordElement:
        if (short_name not in self.elements):
            record_element = ApplicationRecordElement(self, short_name)
            self.elements[short_name] = record_element
        return self.elements[short_name]


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
        self.sub_elements = []      # List(str)
        self.symbol_props = None    # SymbolProps
        self.type_emitter = None

        self._array_type = None     # ImplementationDataType

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


class DataTypeMap(ARObject):
    def __init__(self):
        self.application_data_type_ref = None  # type: RefType
        self.implementation_data_type_ref = None  # type: RefType


class DataTypeMappingSet(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
        self.data_type_maps = []  # type: List[DataTypeMap]

    def addDataTypeMap(self, type_map: DataTypeMap):
        self.data_type_maps.append(type_map)

    def getDataTypeMaps(self) -> List[DataTypeMap]:
        return self.data_type_maps
