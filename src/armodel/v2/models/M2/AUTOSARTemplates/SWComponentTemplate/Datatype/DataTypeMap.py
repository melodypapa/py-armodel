from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

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
        self._applicationDataType: Optional["ApplicationDataType"] = None

    @property
    def application_data_type(self) -> Optional["ApplicationDataType"]:
        """Get applicationDataType (Pythonic accessor)."""
        return self._applicationDataType

    @application_data_type.setter
    def application_data_type(self, value: Optional["ApplicationDataType"]) -> None:
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
        # This is the corresponding AbstractImplementationData Type.
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

    def getApplicationDataType(self) -> "ApplicationDataType":
        """
        AUTOSAR-compliant getter for applicationDataType.
        
        Returns:
            The applicationDataType value
        
        Note:
            Delegates to application_data_type property (CODING_RULE_V2_00017)
        """
        return self.application_data_type  # Delegates to property

    def setApplicationDataType(self, value: "ApplicationDataType") -> "DataTypeMap":
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

    def setImplementation(self, value: "AbstractImplementation") -> "DataTypeMap":
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

    def with_application_data_type(self, value: Optional["ApplicationDataType"]) -> "DataTypeMap":
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

    def with_implementation(self, value: Optional["AbstractImplementation"]) -> "DataTypeMap":
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