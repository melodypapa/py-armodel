from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class CpSwClusterToDiagRoutineSubfunctionMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a
    CpSoftwareClusterResource with a subfunction of a DiagnosticRoutine. This
    allows for indicating that the CpSoftwareClusterResource is used to convey
    the calling or result return of the mapped DiagnosticRoutine.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::CpSoftwareCluster::CpSwClusterToDiagRoutineSubfunctionMapping
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 274, Classic Platform
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
        # This reference identifies the mapped subfunction of a DiagnosticRoutine.
        self._routine: Optional["DiagnosticRoutine"] = None

    @property
    def routine(self) -> Optional["DiagnosticRoutine"]:
        """Get routine (Pythonic accessor)."""
        return self._routine

    @routine.setter
    def routine(self, value: Optional["DiagnosticRoutine"]) -> None:
        """
        Set routine with validation.
        
        Args:
            value: The routine to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._routine = None
            return

        if not isinstance(value, DiagnosticRoutine):
            raise TypeError(
                f"routine must be DiagnosticRoutine or None, got {type(value).__name__}"
            )
        self._routine = value

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

    def setCpSoftware(self, value: "CpSoftwareCluster") -> "CpSwClusterToDiagRoutineSubfunctionMapping":
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

    def getRoutine(self) -> "DiagnosticRoutine":
        """
        AUTOSAR-compliant getter for routine.
        
        Returns:
            The routine value
        
        Note:
            Delegates to routine property (CODING_RULE_V2_00017)
        """
        return self.routine  # Delegates to property

    def setRoutine(self, value: "DiagnosticRoutine") -> "CpSwClusterToDiagRoutineSubfunctionMapping":
        """
        AUTOSAR-compliant setter for routine with method chaining.
        
        Args:
            value: The routine to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to routine property setter (gets validation automatically)
        """
        self.routine = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cp_software(self, value: Optional["CpSoftwareCluster"]) -> "CpSwClusterToDiagRoutineSubfunctionMapping":
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

    def with_routine(self, value: Optional["DiagnosticRoutine"]) -> "CpSwClusterToDiagRoutineSubfunctionMapping":
        """
        Set routine and return self for chaining.
        
        Args:
            value: The routine to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_routine("value")
        """
        self.routine = value  # Use property setter (gets validation)
        return self