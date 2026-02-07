from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class SectionNamePrefix(ImplementationProps):
    """
    A prefix to be used for generated code artifacts defining a memory section
    name in the source code of the using module or SWC.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::MemorySectionUsage::SectionNamePrefix
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 147, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 412, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional reference that allows to Indicate the code artifact containing the
                # preprocessor implementation sections with this prefix.
        # of this link supersedes the usage of a memory with the default name (derived
                # from the.
        self._implementedIn: RefType = None

    @property
    def implemented_in(self) -> RefType:
        """Get implementedIn (Pythonic accessor)."""
        return self._implementedIn

    @implemented_in.setter
    def implemented_in(self, value: RefType) -> None:
        """
        Set implementedIn with validation.
        
        Args:
            value: The implementedIn to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implementedIn = None
            return

        self._implementedIn = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getImplementedIn(self) -> RefType:
        """
        AUTOSAR-compliant getter for implementedIn.
        
        Returns:
            The implementedIn value
        
        Note:
            Delegates to implemented_in property (CODING_RULE_V2_00017)
        """
        return self.implemented_in  # Delegates to property

    def setImplementedIn(self, value: RefType) -> "SectionNamePrefix":
        """
        AUTOSAR-compliant setter for implementedIn with method chaining.
        
        Args:
            value: The implementedIn to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to implemented_in property setter (gets validation automatically)
        """
        self.implemented_in = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_implemented_in(self, value: Optional[RefType]) -> "SectionNamePrefix":
        """
        Set implementedIn and return self for chaining.
        
        Args:
            value: The implementedIn to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_implemented_in("value")
        """
        self.implemented_in = value  # Use property setter (gets validation)
        return self