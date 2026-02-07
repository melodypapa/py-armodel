from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticRoutineNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic
    Communication Manager (Dcm) which are not related to a particular item (e.g.
    a PID). The main use case is the mapping of service ports to the Dcm which
    are not related to a particular item.
    
    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticRoutineNeeds
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 247, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 126, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 780, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This denotes the type of diagnostic routine which is implemented by the
        # referenced server port.
        self._diagRoutine: Optional["DiagnosticRoutineType"] = None

    @property
    def diag_routine(self) -> Optional["DiagnosticRoutineType"]:
        """Get diagRoutine (Pythonic accessor)."""
        return self._diagRoutine

    @diag_routine.setter
    def diag_routine(self, value: Optional["DiagnosticRoutineType"]) -> None:
        """
        Set diagRoutine with validation.
        
        Args:
            value: The diagRoutine to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagRoutine = None
            return

        if not isinstance(value, DiagnosticRoutineType):
            raise TypeError(
                f"diagRoutine must be DiagnosticRoutineType or None, got {type(value).__name__}"
            )
        self._diagRoutine = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagRoutine(self) -> "DiagnosticRoutineType":
        """
        AUTOSAR-compliant getter for diagRoutine.
        
        Returns:
            The diagRoutine value
        
        Note:
            Delegates to diag_routine property (CODING_RULE_V2_00017)
        """
        return self.diag_routine  # Delegates to property

    def setDiagRoutine(self, value: "DiagnosticRoutineType") -> "DiagnosticRoutineNeeds":
        """
        AUTOSAR-compliant setter for diagRoutine with method chaining.
        
        Args:
            value: The diagRoutine to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to diag_routine property setter (gets validation automatically)
        """
        self.diag_routine = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diag_routine(self, value: Optional["DiagnosticRoutineType"]) -> "DiagnosticRoutineNeeds":
        """
        Set diagRoutine and return self for chaining.
        
        Args:
            value: The diagRoutine to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_diag_routine("value")
        """
        self.diag_routine = value  # Use property setter (gets validation)
        return self