from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class CpSwClusterResourceToDiagDataElemMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a
    CpSoftwareClusterResource with a DiagnosticData Element. This allows for
    indicating that the CpSoftwareClusterResource is used to convey the
    Diagnostic DataElement.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::CpSoftwareCluster::CpSwClusterResourceToDiagDataElemMapping
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 273, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the affected CpSoftwareClusterResource.
        # Tags: atp.
        # Status=draft Resource.
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
        # This reference represents the affected DiagnosticData.
        self._diagnosticData: Optional["DiagnosticDataElement"] = None

    @property
    def diagnostic_data(self) -> Optional["DiagnosticDataElement"]:
        """Get diagnosticData (Pythonic accessor)."""
        return self._diagnosticData

    @diagnostic_data.setter
    def diagnostic_data(self, value: Optional["DiagnosticDataElement"]) -> None:
        """
        Set diagnosticData with validation.
        
        Args:
            value: The diagnosticData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticData = None
            return

        if not isinstance(value, DiagnosticDataElement):
            raise TypeError(
                f"diagnosticData must be DiagnosticDataElement or None, got {type(value).__name__}"
            )
        self._diagnosticData = value

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

    def setCpSoftware(self, value: "CpSoftwareCluster") -> "CpSwClusterResourceToDiagDataElemMapping":
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

    def getDiagnosticData(self) -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant getter for diagnosticData.
        
        Returns:
            The diagnosticData value
        
        Note:
            Delegates to diagnostic_data property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_data  # Delegates to property

    def setDiagnosticData(self, value: "DiagnosticDataElement") -> "CpSwClusterResourceToDiagDataElemMapping":
        """
        AUTOSAR-compliant setter for diagnosticData with method chaining.
        
        Args:
            value: The diagnosticData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to diagnostic_data property setter (gets validation automatically)
        """
        self.diagnostic_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cp_software(self, value: Optional["CpSoftwareCluster"]) -> "CpSwClusterResourceToDiagDataElemMapping":
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

    def with_diagnostic_data(self, value: Optional["DiagnosticDataElement"]) -> "CpSwClusterResourceToDiagDataElemMapping":
        """
        Set diagnosticData and return self for chaining.
        
        Args:
            value: The diagnosticData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_diagnostic_data("value")
        """
        self.diagnostic_data = value  # Use property setter (gets validation)
        return self