"""
This module contains classes for representing AUTOSAR data types
in the SWComponentTemplate module. It includes application and
implementation data types, as well as datatype mapping classes
used to map between different type representations.
"""

from typing import List, Optional, cast
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import ModeRequestTypeMap
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ApplicationArrayElement, ApplicationRecordElement
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from abc import ABC


class AutosarDataType(ARElement, ABC):
    """Abstract base class for user defined AUTOSAR data types for software."""

    # AutosarDataType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.1, p.232
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSwDataDefProps            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwDataDefProps            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is AutosarDataType:
            raise TypeError("AutosarDataType is an abstract class.")

        super().__init__(parent, short_name)

        # The properties of this AutosarDataType.
        self.swDataDefProps: Optional[SwDataDefProps] = None

    def getSwDataDefProps(self) -> Optional[SwDataDefProps]:
        """The properties of this AutosarDataType."""
        return self.swDataDefProps

    def setSwDataDefProps(self, value: Optional[SwDataDefProps]) -> "AutosarDataType":
        """The properties of this AutosarDataType. A None value is a no-op and is not set."""
        if value is not None:
            self.swDataDefProps = value
        return self


class ApplicationDataType(AutosarDataType, ABC):
    """
    ApplicationDataType defines a data type from the application point of view. Especially it should be used whenever something "physical" is at stake. An ApplicationDataType represents a set of values as seen in the application model, such as measurement units. It does not consider implementation details such as bit-size, endianess, etc. It should be possible to model the application level aspects of a VFB system by using ApplicationData Types only.
    """

    # ApplicationDataType method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.2, p.232 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ApplicationDataType:
            raise TypeError("ApplicationDataType is an abstract class.")

        super().__init__(parent, short_name)


class ApplicationPrimitiveDataType(ApplicationDataType):
    """
    A primitive data type defines a set of allowed values.
    """

    # ApplicationPrimitiveDataType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.5, p.241 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ApplicationCompositeDataType(ApplicationDataType, ABC):
    """
    Abstract base class for all application data types composed of other data types.
    """

    # ApplicationCompositeDataType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.6, p.241 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is ApplicationCompositeDataType:
            raise TypeError("ApplicationCompositeDataType is an abstract class.")

        super().__init__(parent, short_name)


class ArraySizeHandlingEnum(AREnum):
    """
    This enumeration defines different ways to handle the sizes of variable size arrays.
    """

    # ArraySizeHandlingEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.11, p.254
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on ApplicationArrayElement.arraySizeHandling, ImplementationDataTypeElement.arraySizeHandling (R23-11)

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
    An application data type which is an array, each element is of the same application data type.

    [constr_1907] Existence of attribute ApplicationArrayDataType.element: For each ApplicationArrayDataType, the aggregation of ApplicationArrayElement in the role element shall exist at the time when the RTE is generated.
    """

    # ApplicationArrayDataType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.8, p.252
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                      [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDynamicArraySizeProfile    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDynamicArraySizeProfile    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] createApplicationArrayElement [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getApplicationArrayElement    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Specifies the profile which the array will follow if it is a variable size array.
        self.dynamicArraySizeProfile: Optional[String] = None

        # This association implements the concept of an array element. That is, in some cases it is necessary to be able to identify single array elements, e.g. as input values for an interpolation routine.
        self.element: Optional[ApplicationArrayElement] = None

    def getDynamicArraySizeProfile(self) -> Optional[String]:
        """
        Specifies the profile which the array will follow if it is a variable size array.
        """
        return self.dynamicArraySizeProfile

    def setDynamicArraySizeProfile(self, value: Optional[String]) -> "ApplicationArrayDataType":
        """
        Specifies the profile which the array will follow if it is a variable size array. A None value is a no-op and does not overwrite an existing dynamicArraySizeProfile.
        """
        if value is not None:
            self.dynamicArraySizeProfile = value
        return self

    def createApplicationArrayElement(self, short_name: str) -> ApplicationArrayElement:
        """
        This association implements the concept of an array element. That is, in some cases it is necessary to be able to identify single array elements, e.g. as input values for an interpolation routine.
        """
        if not self.IsReferrableElementExists(short_name, ApplicationArrayElement):
            array_element = ApplicationArrayElement(self, short_name)
            self.addReferrableElement(array_element)
            self.element = array_element
        return cast(ApplicationArrayElement, self.getReferrableElement(short_name, ApplicationArrayElement))

    def getApplicationArrayElement(self) -> Optional[ApplicationArrayElement]:
        """
        This association implements the concept of an array element. That is, in some cases it is necessary to be able to identify single array elements, e.g. as input values for an interpolation routine.
        """
        return self.element


class ApplicationRecordDataType(ApplicationCompositeDataType):
    """
    An application data type which can be decomposed into prototypes of other application data types.
    """

    # ApplicationRecordDataType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.12, p.261 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createApplicationRecordElement [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getApplicationRecordElements   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.recordElements: List[ApplicationRecordElement] = []

    def createApplicationRecordElement(self, short_name: str) -> ApplicationRecordElement:
        if not self.IsReferrableElementExists(short_name, ApplicationRecordElement):
            record_element = ApplicationRecordElement(self, short_name)
            self.addReferrableElement(record_element)
            self.recordElements.append(record_element)
        return cast(ApplicationRecordElement, self.getReferrableElement(short_name, ApplicationRecordElement))

    def getApplicationRecordElements(self) -> List[ApplicationRecordElement]:
        return self.recordElements


class DataTypeMap(ARObject):
    """
    This class represents the relationship between ApplicationDataType and its implementing AbstractImplementationDataType.
    """

    # DataTypeMap method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.3, p.233
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getApplicationDataTypeRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setApplicationDataTypeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getImplementationDataTypeRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setImplementationDataTypeRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This is the corresponding ApplicationDataType [constr_1903]
        self.applicationDataTypeRef: Optional[RefType] = None

        # This is the corresponding AbstractImplementationDataType. [constr_1904]
        self.implementationDataTypeRef: Optional[RefType] = None

    def getApplicationDataTypeRef(self) -> Optional[RefType]:
        """
        This is the corresponding ApplicationDataType [constr_1903]
        """
        return self.applicationDataTypeRef

    def setApplicationDataTypeRef(self, value: Optional[RefType]) -> "DataTypeMap":
        """
        This is the corresponding ApplicationDataType [constr_1903] A None value is a no-op and does not overwrite an existing applicationDataTypeRef.
        """
        if value is not None:
            self.applicationDataTypeRef = value
        return self

    def getImplementationDataTypeRef(self) -> Optional[RefType]:
        """
        This is the corresponding AbstractImplementationDataType. [constr_1904]
        """
        return self.implementationDataTypeRef

    def setImplementationDataTypeRef(self, value: Optional[RefType]) -> "DataTypeMap":
        """
        This is the corresponding AbstractImplementationDataType. [constr_1904] A None value is a no-op and does not overwrite an existing implementationDataTypeRef.
        """
        if value is not None:
            self.implementationDataTypeRef = value
        return self


class DataTypeMappingSet(AtpBlueprintable):
    """
    This class represents a list of mappings between ApplicationDataTypes and ImplementationDataTypes. In addition, it can contain mappings between ImplementationDataTypes and ModeDeclarationGroups.
    """

    # DataTypeMappingSet method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.4, p.234 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addDataTypeMap          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataTypeMaps         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addModeRequestTypeMap   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModeRequestTypeMaps  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This is one particular association between an Application DataType and its AbstractImplementationDataType.
        self.dataTypeMaps: List[DataTypeMap] = []

        # This is one particular association between an Mode DeclarationGroup and its AbstractImplementationData Type.
        self.modeRequestTypeMaps: List[ModeRequestTypeMap] = []

    def addDataTypeMap(self, type_map: Optional[DataTypeMap]) -> "DataTypeMappingSet":
        """
        This is one particular association between an Application DataType and its AbstractImplementationDataType.
        A None value is a no-op and does not add an item.
        """
        if type_map is not None:
            self.dataTypeMaps.append(type_map)
        return self

    def getDataTypeMaps(self) -> List[DataTypeMap]:
        """
        This is one particular association between an Application DataType and its AbstractImplementationDataType.
        """
        return self.dataTypeMaps

    def addModeRequestTypeMap(self, map: Optional[ModeRequestTypeMap]) -> "DataTypeMappingSet":
        """
        This is one particular association between an Mode DeclarationGroup and its AbstractImplementationData Type.
        A None value is a no-op and does not add an item.
        """
        if map is not None:
            self.modeRequestTypeMaps.append(map)
        return self

    def getModeRequestTypeMaps(self) -> List[ModeRequestTypeMap]:
        """
        This is one particular association between an Mode DeclarationGroup and its AbstractImplementationData Type.
        """
        return self.modeRequestTypeMaps
