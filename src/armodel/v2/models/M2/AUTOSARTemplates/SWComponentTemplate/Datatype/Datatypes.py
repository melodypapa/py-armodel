"""
AUTOSAR Package - Datatypes

Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes
"""


from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    String,
)


class AutosarDataType(ARElement, ABC):
    """
    Abstract base class for user defined AUTOSAR data types for software.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes::AutosarDataType

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 306, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 302, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 231, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2001, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 44, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AutosarDataType:
            raise TypeError("AutosarDataType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The properties of this AutosarDataType.
        # atpSplitable.
        self._swDataDef: Optional["SwDataDefProps"] = None

    @property
    def sw_data_def(self) -> Optional["SwDataDefProps"]:
        """Get swDataDef (Pythonic accessor)."""
        return self._swDataDef

    @sw_data_def.setter
    def sw_data_def(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set swDataDef with validation.

        Args:
            value: The swDataDef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swDataDef = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"swDataDef must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._swDataDef = value

    def with_data_type_map(self, value):
        """
        Set data_type_map and return self for chaining.

        Args:
            value: The data_type_map to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_type_map("value")
        """
        self.data_type_map = value  # Use property setter (gets validation)
        return self

    def with_mode_request(self, value):
        """
        Set mode_request and return self for chaining.

        Args:
            value: The mode_request to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_request("value")
        """
        self.mode_request = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSwDataDef(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for swDataDef.

        Returns:
            The swDataDef value

        Note:
            Delegates to sw_data_def property (CODING_RULE_V2_00017)
        """
        return self.sw_data_def  # Delegates to property

    def setSwDataDef(self, value: "SwDataDefProps") -> AutosarDataType:
        """
        AUTOSAR-compliant setter for swDataDef with method chaining.

        Args:
            value: The swDataDef to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_data_def property setter (gets validation automatically)
        """
        self.sw_data_def = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_data_def(self, value: Optional["SwDataDefProps"]) -> AutosarDataType:
        """
        Set swDataDef and return self for chaining.

        Args:
            value: The swDataDef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_data_def("value")
        """
        self.sw_data_def = value  # Use property setter (gets validation)
        return self



class DataTypeMappingSet(ARElement):
    """
    This class represents a list of mappings between ApplicationDataTypes and
    ImplementationDataTypes. In addition, it can contain mappings between
    ImplementationDataTypes and ModeDeclarationGroups.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes::DataTypeMappingSet

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 311, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 234, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2015, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 180, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular association between an Application its
        # AbstractImplementationDataType.
        self._dataTypeMap: List[DataTypeMap] = []

    @property
    def data_type_map(self) -> List[DataTypeMap]:
        """Get dataTypeMap (Pythonic accessor)."""
        return self._dataTypeMap
        # This is one particular association between an Mode and its
        # AbstractImplementationData.
        self._modeRequest: List["ModeRequestTypeMap"] = []

    @property
    def mode_request(self) -> List["ModeRequestTypeMap"]:
        """Get modeRequest (Pythonic accessor)."""
        return self._modeRequest

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataTypeMap(self) -> List[DataTypeMap]:
        """
        AUTOSAR-compliant getter for dataTypeMap.

        Returns:
            The dataTypeMap value

        Note:
            Delegates to data_type_map property (CODING_RULE_V2_00017)
        """
        return self.data_type_map  # Delegates to property

    def getModeRequest(self) -> List["ModeRequestTypeMap"]:
        """
        AUTOSAR-compliant getter for modeRequest.

        Returns:
            The modeRequest value

        Note:
            Delegates to mode_request property (CODING_RULE_V2_00017)
        """
        return self.mode_request  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DataTypeMap(ARObject):
    """
    This class represents the relationship between ApplicationDataType and its
    implementing Abstract ImplementationDataType.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes::DataTypeMap

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 232, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2015, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the corresponding ApplicationDataType.
        self._applicationDataType: Optional[ApplicationDataType] = None

    @property
    def application_data_type(self) -> Optional[ApplicationDataType]:
        """Get applicationDataType (Pythonic accessor)."""
        return self._applicationDataType

    @application_data_type.setter
    def application_data_type(self, value: Optional[ApplicationDataType]) -> None:
        """
        Set applicationDataType with validation.

        Args:
            value: The applicationDataType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._applicationDataType = None
            return

        if not isinstance(value, ApplicationDataType):
            raise TypeError(
                f"applicationDataType must be ApplicationDataType or None, got {type(value).__name__}"
            )
        self._applicationDataType = value
        self._implementation: Optional["AbstractImplementation"] = None

    @property
    def implementation(self) -> Optional["AbstractImplementation"]:
        """Get implementation (Pythonic accessor)."""
        return self._implementation

    @implementation.setter
    def implementation(self, value: Optional["AbstractImplementation"]) -> None:
        """
        Set implementation with validation.

        Args:
            value: The implementation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implementation = None
            return

        if not isinstance(value, AbstractImplementation):
            raise TypeError(
                f"implementation must be AbstractImplementation or None, got {type(value).__name__}"
            )
        self._implementation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplicationDataType(self) -> ApplicationDataType:
        """
        AUTOSAR-compliant getter for applicationDataType.

        Returns:
            The applicationDataType value

        Note:
            Delegates to application_data_type property (CODING_RULE_V2_00017)
        """
        return self.application_data_type  # Delegates to property

    def setApplicationDataType(self, value: ApplicationDataType) -> DataTypeMap:
        """
        AUTOSAR-compliant setter for applicationDataType with method chaining.

        Args:
            value: The applicationDataType to set

        Returns:
            self for method chaining

        Note:
            Delegates to application_data_type property setter (gets validation automatically)
        """
        self.application_data_type = value  # Delegates to property setter
        return self

    def getImplementation(self) -> "AbstractImplementation":
        """
        AUTOSAR-compliant getter for implementation.

        Returns:
            The implementation value

        Note:
            Delegates to implementation property (CODING_RULE_V2_00017)
        """
        return self.implementation  # Delegates to property

    def setImplementation(self, value: "AbstractImplementation") -> DataTypeMap:
        """
        AUTOSAR-compliant setter for implementation with method chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Note:
            Delegates to implementation property setter (gets validation automatically)
        """
        self.implementation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application_data_type(self, value: Optional[ApplicationDataType]) -> DataTypeMap:
        """
        Set applicationDataType and return self for chaining.

        Args:
            value: The applicationDataType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application_data_type("value")
        """
        self.application_data_type = value  # Use property setter (gets validation)
        return self

    def with_implementation(self, value: Optional["AbstractImplementation"]) -> DataTypeMap:
        """
        Set implementation and return self for chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implementation("value")
        """
        self.implementation = value  # Use property setter (gets validation)
        return self



class ApplicationDataType(AutosarDataType, ABC):
    """
    ApplicationDataType defines a data type from the application point of view.
    Especially it should be used whenever something "physical" is at stake. An
    ApplicationDataType represents a set of values as seen in the application
    model, such as measurement units. It does not consider implementation
    details such as bit-size, endianess, etc. It should be possible to model the
    application level aspects of a VFB system by using ApplicationData Types
    only.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes::ApplicationDataType

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 302, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 299, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 232, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1996, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 34, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 160, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is ApplicationDataType:
            raise TypeError("ApplicationDataType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ApplicationPrimitiveDataType(ApplicationDataType):
    """
    A primitive data type defines a set of allowed values.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes::ApplicationPrimitiveDataType

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 230, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 241, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1997, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 34, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ApplicationCompositeDataType(ApplicationDataType, ABC):
    """
    Abstract base class for all application data types composed of other data
    types.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes::ApplicationCompositeDataType

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 241, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1996, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 34, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is ApplicationCompositeDataType:
            raise TypeError("ApplicationCompositeDataType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ApplicationArrayDataType(ApplicationCompositeDataType):
    """
    An application data type which is an array, each element is of the same
    application data type.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes::ApplicationArrayDataType

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 252, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1995, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 35, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the profile which the array will follow if it is a size array.
        self._dynamicArray: Optional[String] = None

    @property
    def dynamic_array(self) -> Optional[String]:
        """Get dynamicArray (Pythonic accessor)."""
        return self._dynamicArray

    @dynamic_array.setter
    def dynamic_array(self, value: Optional[String]) -> None:
        """
        Set dynamicArray with validation.

        Args:
            value: The dynamicArray to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamicArray = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"dynamicArray must be String or str or None, got {type(value).__name__}"
            )
        self._dynamicArray = value
                # is necessary to be able single array elements, e.
        # g.
        # as input values for routine.
        self._element: Optional["ApplicationArray"] = None

    @property
    def element(self) -> Optional["ApplicationArray"]:
        """Get element (Pythonic accessor)."""
        return self._element

    @element.setter
    def element(self, value: Optional["ApplicationArray"]) -> None:
        """
        Set element with validation.

        Args:
            value: The element to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._element = None
            return

        if not isinstance(value, ApplicationArray):
            raise TypeError(
                f"element must be ApplicationArray or None, got {type(value).__name__}"
            )
        self._element = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDynamicArray(self) -> String:
        """
        AUTOSAR-compliant getter for dynamicArray.

        Returns:
            The dynamicArray value

        Note:
            Delegates to dynamic_array property (CODING_RULE_V2_00017)
        """
        return self.dynamic_array  # Delegates to property

    def setDynamicArray(self, value: String) -> ApplicationArrayDataType:
        """
        AUTOSAR-compliant setter for dynamicArray with method chaining.

        Args:
            value: The dynamicArray to set

        Returns:
            self for method chaining

        Note:
            Delegates to dynamic_array property setter (gets validation automatically)
        """
        self.dynamic_array = value  # Delegates to property setter
        return self

    def getElement(self) -> "ApplicationArray":
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    def setElement(self, value: "ApplicationArray") -> ApplicationArrayDataType:
        """
        AUTOSAR-compliant setter for element with method chaining.

        Args:
            value: The element to set

        Returns:
            self for method chaining

        Note:
            Delegates to element property setter (gets validation automatically)
        """
        self.element = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dynamic_array(self, value: Optional[String]) -> ApplicationArrayDataType:
        """
        Set dynamicArray and return self for chaining.

        Args:
            value: The dynamicArray to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dynamic_array("value")
        """
        self.dynamic_array = value  # Use property setter (gets validation)
        return self

    def with_element(self, value: Optional["ApplicationArray"]) -> ApplicationArrayDataType:
        """
        Set element and return self for chaining.

        Args:
            value: The element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_element("value")
        """
        self.element = value  # Use property setter (gets validation)
        return self



class ApplicationRecordDataType(ApplicationCompositeDataType):
    """
    An application data type which can be decomposed into prototypes of other
    application data types.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes::ApplicationRecordDataType

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 261, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1997, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 34, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies an element of a record.
        # The aggregation of ApplicationRecordElement is subject with the purpose to
                # support the conditional elements inside a ApplicationrecordData atpVariation.
        self._element: List[ApplicationRecord] = []

    @property
    def element(self) -> List[ApplicationRecord]:
        """Get element (Pythonic accessor)."""
        return self._element

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElement(self) -> List[ApplicationRecord]:
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


class ArraySizeHandlingEnum(AREnum):
    """
    ArraySizeHandlingEnum enumeration

This enumeration defines different ways to handle the sizes of variable size arrays. Aggregated by ApplicationArrayElement.arraySizeHandling, ImplementationDataTypeElement.arraySizeHandling

Package: M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes
    """
    # All elements of the variable size array may have different sizes.
    allIndicesDifferentArraySize = "0"

    # All elements of the variable size array have the same size.
    allIndicesSameArraySize = "1"

    # Component Template
    Software = "None"

    # CP R23-11
    AUTOSAR = "None"

    # The size of all dimensions of the variable size array is determined by the size of the contained array ElementTypeSize element.
    inheritedFromArray = "2"
