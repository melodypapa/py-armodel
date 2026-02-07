from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ModeRequestTypeMap(ARObject):
    """
    Specifies a mapping between a ModeDeclarationGroup and an
    ImplementationDataType. This ImplementationDataType shall be used to
    implement the ModeDeclarationGroup.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ModeDeclaration::ModeRequestTypeMap
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 44, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 115, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the corresponding AbstractImplementationData Type.
        # It shall be modeled along the idea of an "unsigned type.
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
        # This is the corresponding ModeDeclarationGroup.
        self._modeGroup: RefType = None

    @property
    def mode_group(self) -> RefType:
        """Get modeGroup (Pythonic accessor)."""
        return self._modeGroup

    @mode_group.setter
    def mode_group(self, value: RefType) -> None:
        """
        Set modeGroup with validation.
        
        Args:
            value: The modeGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroup = None
            return

        self._modeGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getImplementation(self) -> "AbstractImplementation":
        """
        AUTOSAR-compliant getter for implementation.
        
        Returns:
            The implementation value
        
        Note:
            Delegates to implementation property (CODING_RULE_V2_00017)
        """
        return self.implementation  # Delegates to property

    def setImplementation(self, value: "AbstractImplementation") -> "ModeRequestTypeMap":
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

    def getModeGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for modeGroup.
        
        Returns:
            The modeGroup value
        
        Note:
            Delegates to mode_group property (CODING_RULE_V2_00017)
        """
        return self.mode_group  # Delegates to property

    def setModeGroup(self, value: RefType) -> "ModeRequestTypeMap":
        """
        AUTOSAR-compliant setter for modeGroup with method chaining.
        
        Args:
            value: The modeGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mode_group property setter (gets validation automatically)
        """
        self.mode_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_implementation(self, value: Optional["AbstractImplementation"]) -> "ModeRequestTypeMap":
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

    def with_mode_group(self, value: Optional[RefType]) -> "ModeRequestTypeMap":
        """
        Set modeGroup and return self for chaining.
        
        Args:
            value: The modeGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mode_group("value")
        """
        self.mode_group = value  # Use property setter (gets validation)
        return self