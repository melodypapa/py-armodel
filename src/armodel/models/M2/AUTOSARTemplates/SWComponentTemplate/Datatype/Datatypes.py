from typing import List
from .....M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeRequestTypeMap
from .....M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpType
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType, String
from .....M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ApplicationArrayElement, ApplicationRecordElement
from .....M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
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

        self.dynamicArraySizeProfile = None         # type: String
        self.element = None                         # type: ApplicationArrayElement

    def getDynamicArraySizeProfile(self):
        return self.dynamicArraySizeProfile

    def setDynamicArraySizeProfile(self, value):
        if value is not None:
            self.dynamicArraySizeProfile = value
        return self

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

        self.applicationDataTypeRef = None                  # type: RefType
        self.implementationDataTypeRef = None               # type: RefType

    def getApplicationDataTypeRef(self):
        return self.applicationDataTypeRef

    def setApplicationDataTypeRef(self, value):
        self.applicationDataTypeRef = value
        return self

    def getImplementationDataTypeRef(self):
        return self.implementationDataTypeRef

    def setImplementationDataTypeRef(self, value):
        self.implementationDataTypeRef = value
        return self

class DataTypeMappingSet(ARElement):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataTypeMaps = []                              # type: List[DataTypeMap]
        self.modeRequestTypeMaps = []                       # type: List[ModeRequestTypeMap]

    def addDataTypeMap(self, type_map: DataTypeMap):
        self.dataTypeMaps.append(type_map)
        return self

    def getDataTypeMaps(self) -> List[DataTypeMap]:
        return self.dataTypeMaps

    def addModeRequestTypeMap(self, map: ModeRequestTypeMap):
        self.modeRequestTypeMaps.append(map)
        return self

    def getModeRequestTypeMaps(self) -> List[ModeRequestTypeMap]:
        return self.modeRequestTypeMaps