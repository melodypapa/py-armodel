from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TransmissionAcknowledgementRequest(ARObject):
    """
    Requests transmission acknowledgement that data has been sent successfully.
    Success/failure is reported via a SendPoint of a RunnableEntity.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::TransmissionAcknowledgementRequest
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 180, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Number of seconds before an error is reported or in case redundancy, the
        # value is sent again.
        self._timeout: Optional["TimeValue"] = None

    @property
    def timeout(self) -> Optional["TimeValue"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeout with validation.
        
        Args:
            value: The timeout to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeout = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeout.
        
        Returns:
            The timeout value
        
        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "TimeValue") -> "TransmissionAcknowledgementRequest":
        """
        AUTOSAR-compliant setter for timeout with method chaining.
        
        Args:
            value: The timeout to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_timeout(self, value: Optional["TimeValue"]) -> "TransmissionAcknowledgementRequest":
        """
        Set timeout and return self for chaining.
        
        Args:
            value: The timeout to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self