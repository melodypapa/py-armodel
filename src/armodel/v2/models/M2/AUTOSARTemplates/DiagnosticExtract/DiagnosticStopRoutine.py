from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticStopRoutine(DiagnosticRoutineSubfunction):
    """
    This represents the ability to stop a diagnostic routine.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::CommonDiagnostics::DiagnosticStopRoutine
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 125, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the request parameters.
        self._request: List["DiagnosticParameter"] = []

    @property
    def request(self) -> List["DiagnosticParameter"]:
        """Get request (Pythonic accessor)."""
        return self._request
        # This represents the response parameters.
        self._response: List["DiagnosticParameter"] = []

    @property
    def response(self) -> List["DiagnosticParameter"]:
        """Get response (Pythonic accessor)."""
        return self._response

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequest(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for request.
        
        Returns:
            The request value
        
        Note:
            Delegates to request property (CODING_RULE_V2_00017)
        """
        return self.request  # Delegates to property

    def getResponse(self) -> List["DiagnosticParameter"]:
        """
        AUTOSAR-compliant getter for response.
        
        Returns:
            The response value
        
        Note:
            Delegates to response property (CODING_RULE_V2_00017)
        """
        return self.response  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====