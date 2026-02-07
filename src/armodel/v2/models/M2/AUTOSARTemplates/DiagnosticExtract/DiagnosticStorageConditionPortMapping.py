from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticStorageConditionPortMapping(DiagnosticSwMapping):
    """
    Defines to which SWC service ports with DiagnosticStorageConditionNeeds the
    DiagnosticStorage Condition is mapped.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticStorageConditionPortMapping
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 253, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the StorageCondition which is mapped to a SWC service port with
        # DiagnosticStorageCondition.
        self._diagnostic: Optional["DiagnosticStorage"] = None

    @property
    def diagnostic(self) -> Optional["DiagnosticStorage"]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, value: Optional["DiagnosticStorage"]) -> None:
        """
        Set diagnostic with validation.
        
        Args:
            value: The diagnostic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnostic = None
            return

        if not isinstance(value, DiagnosticStorage):
            raise TypeError(
                f"diagnostic must be DiagnosticStorage or None, got {type(value).__name__}"
            )
        self._diagnostic = value
        # Reference to a SwcServiceDependencyType that links ServiceNeeds to SWC
        # service ports.
        self._swcFlatService: Optional["SwcService"] = None

    @property
    def swc_flat_service(self) -> Optional["SwcService"]:
        """Get swcFlatService (Pythonic accessor)."""
        return self._swcFlatService

    @swc_flat_service.setter
    def swc_flat_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcFlatService with validation.
        
        Args:
            value: The swcFlatService to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcFlatService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcFlatService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcFlatService = value
        # ServiceNeeds to SWC service ports.
        # implemented by: SwcServiceDependency.
        self._swcService: Optional["SwcService"] = None

    @property
    def swc_service(self) -> Optional["SwcService"]:
        """Get swcService (Pythonic accessor)."""
        return self._swcService

    @swc_service.setter
    def swc_service(self, value: Optional["SwcService"]) -> None:
        """
        Set swcService with validation.
        
        Args:
            value: The swcService to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcService = None
            return

        if not isinstance(value, SwcService):
            raise TypeError(
                f"swcService must be SwcService or None, got {type(value).__name__}"
            )
        self._swcService = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnostic(self) -> "DiagnosticStorage":
        """
        AUTOSAR-compliant getter for diagnostic.
        
        Returns:
            The diagnostic value
        
        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def setDiagnostic(self, value: "DiagnosticStorage") -> "DiagnosticStorageConditionPortMapping":
        """
        AUTOSAR-compliant setter for diagnostic with method chaining.
        
        Args:
            value: The diagnostic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to diagnostic property setter (gets validation automatically)
        """
        self.diagnostic = value  # Delegates to property setter
        return self

    def getSwcFlatService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcFlatService.
        
        Returns:
            The swcFlatService value
        
        Note:
            Delegates to swc_flat_service property (CODING_RULE_V2_00017)
        """
        return self.swc_flat_service  # Delegates to property

    def setSwcFlatService(self, value: "SwcService") -> "DiagnosticStorageConditionPortMapping":
        """
        AUTOSAR-compliant setter for swcFlatService with method chaining.
        
        Args:
            value: The swcFlatService to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to swc_flat_service property setter (gets validation automatically)
        """
        self.swc_flat_service = value  # Delegates to property setter
        return self

    def getSwcService(self) -> "SwcService":
        """
        AUTOSAR-compliant getter for swcService.
        
        Returns:
            The swcService value
        
        Note:
            Delegates to swc_service property (CODING_RULE_V2_00017)
        """
        return self.swc_service  # Delegates to property

    def setSwcService(self, value: "SwcService") -> "DiagnosticStorageConditionPortMapping":
        """
        AUTOSAR-compliant setter for swcService with method chaining.
        
        Args:
            value: The swcService to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to swc_service property setter (gets validation automatically)
        """
        self.swc_service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic(self, value: Optional["DiagnosticStorage"]) -> "DiagnosticStorageConditionPortMapping":
        """
        Set diagnostic and return self for chaining.
        
        Args:
            value: The diagnostic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_diagnostic("value")
        """
        self.diagnostic = value  # Use property setter (gets validation)
        return self

    def with_swc_flat_service(self, value: Optional["SwcService"]) -> "DiagnosticStorageConditionPortMapping":
        """
        Set swcFlatService and return self for chaining.
        
        Args:
            value: The swcFlatService to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_swc_flat_service("value")
        """
        self.swc_flat_service = value  # Use property setter (gets validation)
        return self

    def with_swc_service(self, value: Optional["SwcService"]) -> "DiagnosticStorageConditionPortMapping":
        """
        Set swcService and return self for chaining.
        
        Args:
            value: The swcService to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_swc_service("value")
        """
        self.swc_service = value  # Use property setter (gets validation)
        return self