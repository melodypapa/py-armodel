from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class CpSwClusterToDiagEventMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a
    CpSoftwareClusterResource with a Diagnostic Event. This allows for
    indicating that the CpSoftwareClusterResource is used to convey the
    reporting or status query of the mapped DiagnosticEvent.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::CpSoftwareCluster::CpSwClusterToDiagEventMapping
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 272, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the mapped CpSoftwareCluster Resource.
        # atp.
        # Status=draft.
        self._cpSoftware: Optional["CpSoftwareCluster"] = None

    @property
    def cp_software(self) -> Optional["CpSoftwareCluster"]:
        """Get cpSoftware (Pythonic accessor)."""
        return self._cpSoftware

    @cp_software.setter
    def cp_software(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set cpSoftware with validation.
        
        Args:
            value: The cpSoftware to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cpSoftware = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"cpSoftware must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._cpSoftware = value
        # This reference identifies the mapped DiagnosticEvent.
        self._diagnosticEvent: Optional["DiagnosticEvent"] = None

    @property
    def diagnostic_event(self) -> Optional["DiagnosticEvent"]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set diagnosticEvent with validation.
        
        Args:
            value: The diagnosticEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCpSoftware(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for cpSoftware.
        
        Returns:
            The cpSoftware value
        
        Note:
            Delegates to cp_software property (CODING_RULE_V2_00017)
        """
        return self.cp_software  # Delegates to property

    def setCpSoftware(self, value: "CpSoftwareCluster") -> "CpSwClusterToDiagEventMapping":
        """
        AUTOSAR-compliant setter for cpSoftware with method chaining.
        
        Args:
            value: The cpSoftware to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to cp_software property setter (gets validation automatically)
        """
        self.cp_software = value  # Delegates to property setter
        return self

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.
        
        Returns:
            The diagnosticEvent value
        
        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> "CpSwClusterToDiagEventMapping":
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.
        
        Args:
            value: The diagnosticEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cp_software(self, value: Optional["CpSoftwareCluster"]) -> "CpSwClusterToDiagEventMapping":
        """
        Set cpSoftware and return self for chaining.
        
        Args:
            value: The cpSoftware to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_cp_software("value")
        """
        self.cp_software = value  # Use property setter (gets validation)
        return self

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> "CpSwClusterToDiagEventMapping":
        """
        Set diagnosticEvent and return self for chaining.
        
        Args:
            value: The diagnosticEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self