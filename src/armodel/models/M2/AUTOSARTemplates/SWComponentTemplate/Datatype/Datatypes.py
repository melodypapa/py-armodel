from typing import List
from ...CommonStructure.ModeDeclaration import ModeRequestTypeMap
from ...GenericStructure.AbstractStructure import AtpType
from ...GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ...GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from ...GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from ...SWComponentTemplate.Datatype.DataPrototypes import ApplicationArrayElement, ApplicationRecordElement
from ....MSR.DataDictionary.DataDefProperties import SwDataDefProps
from abc import ABCMeta

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