"""
This module contains classes for representing AUTOSAR data types
in the SWComponentTemplate module. It includes application and
implementation data types, as well as datatype mapping classes
used to map between different type representations.
"""

from abc import ABC
from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeRequestTypeMap,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    ApplicationArrayElement,
    ApplicationRecordElement,
)
from armodel.v2.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwDataDefProps,
)


class AutosarDataType(AtpType, ABC):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is AutosarDataType:
            raise TypeError("AutosarDataType is an abstract class.")

        super().__init__(parent, short_name)

        self.swDataDefProps: Union[Union[SwDataDefProps, None] , None] = None

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        self.swDataDefProps = value
        return self


class ApplicationDataType(AutosarDataType, ABC):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is ApplicationDataType:
            raise TypeError("ApplicationDataType is an abstract class.")

        super().__init__(parent, short_name)


class ApplicationPrimitiveDataType(ApplicationDataType):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)


class ApplicationCompositeDataType(ApplicationDataType, ABC):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        if type(self) is ApplicationCompositeDataType:
            raise TypeError("ApplicationCompositeDataType is an abstract class.")

        super().__init__(parent, short_name)


class ApplicationArrayDataType(ApplicationCompositeDataType):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.dynamicArraySizeProfile: Union[Union[String, None] , None] = None
        self.element: Union[Union[ApplicationArrayElement, None] , None] = None

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
    def __init__(self, parent: ARObject, short_name: str) -> None:
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

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:

        self.applicationDataTypeRef: Union[Union[RefType, None] , None] = None
        self.implementationDataTypeRef: Union[Union[RefType, None] , None] = None

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
    def __init__(self, parent: ARObject, short_name: str) -> None:
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
