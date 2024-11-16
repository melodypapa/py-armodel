from abc import ABCMeta
from typing import List

from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical

from .M2.MSR.data_dictionary.data_def_properties import SwDataDefProps
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from .ar_ref import RefType
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from .M2.AUTOSARTemplates.sw_component_template.data_type.data_prototypes import ApplicationCompositeElementDataPrototype, ApplicationRecordElement
from .common_structure import ModeRequestTypeMap

class BaseTypeDefinition(ARObject):
    def __init__(self):
        super().__init__()
    
class BaseTypeDirectDefinition(BaseTypeDefinition):
    def __init__(self):
        super().__init__()

        self.base_type_encoding = None
        self.base_type_size = None                  # type: ARNumerical
        self.byteOrder = None                       # type: str
        self.mem_alignment = None                   # type: ARNumerical
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


class AutosarDataType(AtpType, metaclass = ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == AutosarDataType:
            raise NotImplementedError("AutosarDataType is an abstract class.")

        super().__init__(parent, short_name)

        self.swDataDefProps = None                  # type: SwDataDefProps

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        self.swDataDefProps = value
        return self

class ApplicationDataType(AutosarDataType, metaclass = ABCMeta):
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
    

