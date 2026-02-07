from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DltEcu(ARElement):
    """
    This element represents an Ecu or Machine that produces logging and tracing
    information.
    
    Package: M2::AUTOSARTemplates::LogAndTraceExtract::DltEcu
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2018, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 8, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Application on DltEcu that provides log or trace data.
        # atpVariation.
        self._application: List["DltApplication"] = []

    @property
    def application(self) -> List["DltApplication"]:
        """Get application (Pythonic accessor)."""
        return self._application
        # This attribute defines the name of the ECU for use within protocol.
        self._ecuId: Optional["String"] = None

    @property
    def ecu_id(self) -> Optional["String"]:
        """Get ecuId (Pythonic accessor)."""
        return self._ecuId

    @ecu_id.setter
    def ecu_id(self, value: Optional["String"]) -> None:
        """
        Set ecuId with validation.
        
        Args:
            value: The ecuId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuId = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"ecuId must be String or None, got {type(value).__name__}"
            )
        self._ecuId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> List["DltApplication"]:
        """
        AUTOSAR-compliant getter for application.
        
        Returns:
            The application value
        
        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def getEcuId(self) -> "String":
        """
        AUTOSAR-compliant getter for ecuId.
        
        Returns:
            The ecuId value
        
        Note:
            Delegates to ecu_id property (CODING_RULE_V2_00017)
        """
        return self.ecu_id  # Delegates to property

    def setEcuId(self, value: "String") -> "DltEcu":
        """
        AUTOSAR-compliant setter for ecuId with method chaining.
        
        Args:
            value: The ecuId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ecu_id property setter (gets validation automatically)
        """
        self.ecu_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_id(self, value: Optional["String"]) -> "DltEcu":
        """
        Set ecuId and return self for chaining.
        
        Args:
            value: The ecuId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ecu_id("value")
        """
        self.ecu_id = value  # Use property setter (gets validation)
        return self