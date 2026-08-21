"""
This module contains classes for representing AUTOSAR data types
in the SWComponentTemplate module. It includes application and
implementation data types, as well as datatype mapping classes
used to map between different type representations.
"""

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeRequestTypeMap
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpType, AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, RefType, String
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


class ArraySizeHandlingEnum(AREnum):
    """
    This enumeration defines different ways to handle the sizes of variable size arrays.
    """

    # ArraySizeHandlingEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.11, p.253
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on ApplicationArrayElement.arraySizeHandling, ImplementationDataTypeElement.arraySizeHandling
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # All elements of the variable size array may have different sizes. Tags: atp.EnumerationLiteralIndex=0
    ALL_INDICES_DIFFERENT_ARRAY_SIZE = "allIndicesDifferentArraySize"

    # All elements of the variable size array have the same size. Tags: atp.EnumerationLiteralIndex=1
    ALL_INDICES_SAME_ARRAY_SIZE = "allIndicesSameArraySize"

    # The size of all dimensions of the variable size array is determined by the size of the contained array element. Tags: atp.EnumerationLiteralIndex=2
    INHERITED_FROM_ARRAY_ELEMENT_TYPE_SIZE = "inheritedFromArrayElementTypeSize"

    def __init__(self):
        super().__init__(
            [
                ArraySizeHandlingEnum.ALL_INDICES_DIFFERENT_ARRAY_SIZE,
                ArraySizeHandlingEnum.ALL_INDICES_SAME_ARRAY_SIZE,
                ArraySizeHandlingEnum.INHERITED_FROM_ARRAY_ELEMENT_TYPE_SIZE,
            ]
        )


class ApplicationArrayDataType(ApplicationCompositeDataType):
    """
    An application data type which is an array, each element is of the same application data type. Tags: atp.recommendedPackage=ApplicationDataTypes
    """

    # ApplicationArrayDataType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.8, p.252
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDynamicArraySizeProfile       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDynamicArraySizeProfile       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getApplicationArrayElement       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] createApplicationArrayElement    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies the profile which the array will follow if it is a variable size array.
        self.dynamicArraySizeProfile: Optional[String] = None

        # This association implements the concept of an array element. That is, in some cases it is necessary to be able to identify single array elements, e.g. as input values for an interpolation routine.
        self.element: Optional[ApplicationArrayElement] = None

    def getDynamicArraySizeProfile(self) -> Optional[String]:
        """
        Specifies the profile which the array will follow if it is a variable size array.

        Returns:
            Optional[String]: The dynamicArraySizeProfile
        """
        return self.dynamicArraySizeProfile

    def setDynamicArraySizeProfile(self, value: Optional[String]) -> "ApplicationArrayDataType":
        """
        Specifies the profile which the array will follow if it is a variable size array. A None value is a no-op and does not overwrite an existing dynamicArraySizeProfile.

        Args:
            value: The dynamicArraySizeProfile to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dynamicArraySizeProfile = value
        return self

    def getApplicationArrayElement(self) -> Optional[ApplicationArrayElement]:
        """
        This association implements the concept of an array element. That is, in some cases it is necessary to be able to identify single array elements, e.g. as input values for an interpolation routine. Named getApplicationArrayElement instead of getElement to avoid clashing with the ARObject element registry lookup.

        Returns:
            Optional[ApplicationArrayElement]: The element aggregation
        """
        return self.element

    def createApplicationArrayElement(self, short_name: str) -> ApplicationArrayElement:
        """
        This association implements the concept of an array element. That is, in some cases it is necessary to be able to identify single array elements, e.g. as input values for an interpolation routine.

        Args:
            short_name: The short name of the ApplicationArrayElement to create

        Returns:
            The newly created or existing ApplicationArrayElement instance
        """
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
        if not self.IsElementExists(short_name):
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
