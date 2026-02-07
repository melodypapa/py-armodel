from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class LinErrorResponse(ARObject):
    """
    Each slave node shall publish a one bit signal, named response_error, to the
    master node in one of its transmitted unconditional frames. The
    response_error signal shall be set whenever a frame (except for event
    triggered frame responses) that is transmitted or received by the slave node
    contains an error in the frame response. The response_error signal shall be
    cleared when the unconditional frame containing the response_error signal is
    successfully transmitted.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication::LinErrorResponse
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 97, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This ISignal shall be taken to transport the responseError.
        self._responseError: RefType = None

    @property
    def response_error(self) -> RefType:
        """Get responseError (Pythonic accessor)."""
        return self._responseError

    @response_error.setter
    def response_error(self, value: RefType) -> None:
        """
        Set responseError with validation.
        
        Args:
            value: The responseError to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._responseError = None
            return

        self._responseError = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getResponseError(self) -> RefType:
        """
        AUTOSAR-compliant getter for responseError.
        
        Returns:
            The responseError value
        
        Note:
            Delegates to response_error property (CODING_RULE_V2_00017)
        """
        return self.response_error  # Delegates to property

    def setResponseError(self, value: RefType) -> "LinErrorResponse":
        """
        AUTOSAR-compliant setter for responseError with method chaining.
        
        Args:
            value: The responseError to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to response_error property setter (gets validation automatically)
        """
        self.response_error = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_response_error(self, value: Optional[RefType]) -> "LinErrorResponse":
        """
        Set responseError and return self for chaining.
        
        Args:
            value: The responseError to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_response_error("value")
        """
        self.response_error = value  # Use property setter (gets validation)
        return self