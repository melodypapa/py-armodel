"""
This module contains classes for representing AUTOSAR data types
in the SWComponentTemplate module. It includes application and
implementation data types, as well as datatype mapping classes
used to map between different type representations.
"""

from typing import List
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeRequestTypeMap
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpType, AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ApplicationArrayElement, ApplicationRecordElement
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from abc import ABC


class AutosarDataType(AtpType, ABC):
    """
    Abstract base class for all AUTOSAR data types within the SW component
    template.
    """
    # AutosarDataType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getSwDataDefProps            [x] impl  [ ] docstring  [ ] test
    # [ ] setSwDataDefProps            [x] impl  [ ] docstring  [ ] test


    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AutosarDataType:
            raise TypeError("AutosarDataType is an abstract class.")

        super().__init__(parent, short_name)

        self.swDataDefProps: SwDataDefProps = None

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        self.swDataDefProps = value
        return self


class ApplicationDataType(AutosarDataType, ABC):
    """
    Abstract base class for all application data types.
    """
    # ApplicationDataType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test


    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ApplicationDataType:
            raise TypeError("ApplicationDataType is an abstract class.")

        super().__init__(parent, short_name)


class ApplicationPrimitiveDataType(ApplicationDataType):
    """
    An application data type that represents a primitive (non-composite)
    data type.
    """
    # ApplicationPrimitiveDataType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test


    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ApplicationCompositeDataType(ApplicationDataType, ABC):
    """
    Abstract base class for application composite data types such as
    arrays and records.
    """
    # ApplicationCompositeDataType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test


    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ApplicationCompositeDataType:
            raise TypeError("ApplicationCompositeDataType is an abstract class.")

        super().__init__(parent, short_name)


class ApplicationArrayDataType(ApplicationCompositeDataType):
    """
    An application data type representing an array with elements of the
    same type.
    """
    # ApplicationArrayDataType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getDynamicArraySizeProfile   [x] impl  [ ] docstring  [ ] test
    # [ ] setDynamicArraySizeProfile   [x] impl  [ ] docstring  [ ] test
    # [ ] createApplicationArrayElement [x] impl  [ ] docstring  [ ] test


    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dynamicArraySizeProfile: String = None
        self.element: ApplicationArrayElement = None

    def getDynamicArraySizeProfile(self):
        return self.dynamicArraySizeProfile

    def setDynamicArraySizeProfile(self, value):
        if value is not None:
            self.dynamicArraySizeProfile = value
        return self

    def createApplicationArrayElement(self, short_name: str) -> ApplicationArrayElement:
        if not self.IsElementExists(short_name):
            array_element = ApplicationArrayElement(self, short_name)
            self.addElement(array_element)
            self.element = array_element
        return self.getElement(short_name, ApplicationArrayElement)


class ApplicationRecordDataType(ApplicationCompositeDataType):
    """
    An application data type representing a record with fields of possibly
    different types.
    """
    # ApplicationRecordDataType method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] createApplicationRecordElement [x] impl  [ ] docstring  [ ] test
    # [ ] getApplicationRecordElements [x] impl  [ ] docstring  [ ] test


    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.record_elements: List[ApplicationRecordElement] = []

    def createApplicationRecordElement(self, short_name: str) -> ApplicationRecordElement:
        if (not self.IsElementExists(short_name)):
            record_element = ApplicationRecordElement(self, short_name)
            self.addElement(record_element)
            self.record_elements.append(record_element)
        return self.getElement(short_name, ApplicationRecordElement)

    def getApplicationRecordElements(self) -> List[ApplicationRecordElement]:
        return self.record_elements


class DataTypeMap(ARObject):
    """
    Maps an application data type to an implementation data type.
    """
    # DataTypeMap method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getApplicationDataTypeRef    [x] impl  [ ] docstring  [ ] test
    # [ ] setApplicationDataTypeRef    [x] impl  [ ] docstring  [ ] test
    # [ ] getImplementationDataTypeRef [x] impl  [ ] docstring  [ ] test
    # [ ] setImplementationDataTypeRef [x] impl  [ ] docstring  [ ] test


    def __init__(self):

        self.applicationDataTypeRef: RefType = None
        self.implementationDataTypeRef: RefType = None

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


class DataTypeMappingSet(AtpBlueprintable):
    """
    A set of data type maps and mode request type maps that define
    mappings between application and implementation data types.
    """
    # DataTypeMappingSet method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] addDataTypeMap               [x] impl  [ ] docstring  [ ] test
    # [ ] getDataTypeMaps              [x] impl  [ ] docstring  [ ] test
    # [ ] addModeRequestTypeMap        [x] impl  [ ] docstring  [ ] test
    # [ ] getModeRequestTypeMaps       [x] impl  [ ] docstring  [ ] test


    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.dataTypeMaps: List[DataTypeMap] = []
        self.modeRequestTypeMaps: List[ModeRequestTypeMap] = []

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
