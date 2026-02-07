from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class CommunicationBufferLocking(SwcSupportedFeature):
    """
    The aggregation of this meta-class specifies that a RunnableEntity supports
    locked communication buffers supplied by the RTE. It is able to cope with
    the error RTE_E_COM_BUSY.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::PortAPIOptions::CommunicationBufferLocking
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 595, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to indicate the intended buffer locking behavior.
        self._supportBuffer: Optional["SupportBufferLocking"] = None

    @property
    def support_buffer(self) -> Optional["SupportBufferLocking"]:
        """Get supportBuffer (Pythonic accessor)."""
        return self._supportBuffer

    @support_buffer.setter
    def support_buffer(self, value: Optional["SupportBufferLocking"]) -> None:
        """
        Set supportBuffer with validation.
        
        Args:
            value: The supportBuffer to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supportBuffer = None
            return

        if not isinstance(value, SupportBufferLocking):
            raise TypeError(
                f"supportBuffer must be SupportBufferLocking or None, got {type(value).__name__}"
            )
        self._supportBuffer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSupportBuffer(self) -> "SupportBufferLocking":
        """
        AUTOSAR-compliant getter for supportBuffer.
        
        Returns:
            The supportBuffer value
        
        Note:
            Delegates to support_buffer property (CODING_RULE_V2_00017)
        """
        return self.support_buffer  # Delegates to property

    def setSupportBuffer(self, value: "SupportBufferLocking") -> "CommunicationBufferLocking":
        """
        AUTOSAR-compliant setter for supportBuffer with method chaining.
        
        Args:
            value: The supportBuffer to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to support_buffer property setter (gets validation automatically)
        """
        self.support_buffer = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_support_buffer(self, value: Optional["SupportBufferLocking"]) -> "CommunicationBufferLocking":
        """
        Set supportBuffer and return self for chaining.
        
        Args:
            value: The supportBuffer to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_support_buffer("value")
        """
        self.support_buffer = value  # Use property setter (gets validation)
        return self