from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class OperationInvokedEvent(RTEEvent):
    """
    This event is raised when the ClientServerOperation referenced in
    OperationInvokedEvent.operation shall be invoked.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::OperationInvokedEvent
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 325, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 543, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: POperationInAtomicSwc.
        self._operationInstanceRef: Optional["ClientServerOperation"] = None

    @property
    def operation_instance_ref(self) -> Optional["ClientServerOperation"]:
        """Get operationInstanceRef (Pythonic accessor)."""
        return self._operationInstanceRef

    @operation_instance_ref.setter
    def operation_instance_ref(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set operationInstanceRef with validation.
        
        Args:
            value: The operationInstanceRef to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operationInstanceRef = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"operationInstanceRef must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._operationInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperationInstanceRef(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for operationInstanceRef.
        
        Returns:
            The operationInstanceRef value
        
        Note:
            Delegates to operation_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.operation_instance_ref  # Delegates to property

    def setOperationInstanceRef(self, value: "ClientServerOperation") -> "OperationInvokedEvent":
        """
        AUTOSAR-compliant setter for operationInstanceRef with method chaining.
        
        Args:
            value: The operationInstanceRef to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to operation_instance_ref property setter (gets validation automatically)
        """
        self.operation_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation_instance_ref(self, value: Optional["ClientServerOperation"]) -> "OperationInvokedEvent":
        """
        Set operationInstanceRef and return self for chaining.
        
        Args:
            value: The operationInstanceRef to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_operation_instance_ref("value")
        """
        self.operation_instance_ref = value  # Use property setter (gets validation)
        return self