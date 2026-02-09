"""
AUTOSAR Package - ClearDiagnosticInfo

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ClearDiagnosticInfo
"""

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
    DiagnosticServiceInstance,
)


class DiagnosticClearDiagnosticInformation(DiagnosticServiceInstance):
    """
    This represents an instance of the "Clear Diagnostic Information" diagnostic
    service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ClearDiagnosticInfo::DiagnosticClearDiagnosticInformation
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 137, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference substantiates that abstract reference in the role serviceClass
                # for this specific concrete class.
        # among all DiagnosticClearDiagnostic the given context.
        self._clearDiagnostic: Optional["DiagnosticClear"] = None

    @property
    def clear_diagnostic(self) -> Optional["DiagnosticClear"]:
        """Get clearDiagnostic (Pythonic accessor)."""
        return self._clearDiagnostic

    @clear_diagnostic.setter
    def clear_diagnostic(self, value: Optional["DiagnosticClear"]) -> None:
        """
        Set clearDiagnostic with validation.
        
        Args:
            value: The clearDiagnostic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clearDiagnostic = None
            return

        if not isinstance(value, DiagnosticClear):
            raise TypeError(
                f"clearDiagnostic must be DiagnosticClear or None, got {type(value).__name__}"
            )
        self._clearDiagnostic = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClearDiagnostic(self) -> "DiagnosticClear":
        """
        AUTOSAR-compliant getter for clearDiagnostic.
        
        Returns:
            The clearDiagnostic value
        
        Note:
            Delegates to clear_diagnostic property (CODING_RULE_V2_00017)
        """
        return self.clear_diagnostic  # Delegates to property

    def setClearDiagnostic(self, value: "DiagnosticClear") -> "DiagnosticClearDiagnosticInformation":
        """
        AUTOSAR-compliant setter for clearDiagnostic with method chaining.
        
        Args:
            value: The clearDiagnostic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to clear_diagnostic property setter (gets validation automatically)
        """
        self.clear_diagnostic = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_clear_diagnostic(self, value: Optional["DiagnosticClear"]) -> "DiagnosticClearDiagnosticInformation":
        """
        Set clearDiagnostic and return self for chaining.
        
        Args:
            value: The clearDiagnostic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_clear_diagnostic("value")
        """
        self.clear_diagnostic = value  # Use property setter (gets validation)
        return self



class DiagnosticClearDiagnosticInformationClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Clear
    Diagnostic Information" diagnostic service.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::ClearDiagnosticInfo::DiagnosticClearDiagnosticInformationClass
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 137, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
