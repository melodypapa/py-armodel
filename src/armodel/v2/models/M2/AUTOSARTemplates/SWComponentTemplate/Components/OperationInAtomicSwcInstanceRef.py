from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class OperationInAtomicSwcInstanceRef(ARObject, ABC):
    """
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::OperationInAtomicSwcInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 946, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is OperationInAtomicSwcInstanceRef:
            raise TypeError("OperationInAtomicSwcInstanceRef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived xml.
        # sequenceOffset=10.
        self._base: Optional["AtomicSwComponent"] = None

    @property
    def base(self) -> Optional["AtomicSwComponent"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["AtomicSwComponent"]) -> None:
        """
        Set base with validation.
        
        Args:
            value: The base to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._base = None
            return

        if not isinstance(value, AtomicSwComponent):
            raise TypeError(
                f"base must be AtomicSwComponent or None, got {type(value).__name__}"
            )
        self._base = value
        # Stereotypes: atpAbstract.
        self._contextPort: RefType = None

    @property
    def context_port(self) -> RefType:
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: RefType) -> None:
        """
        Set contextPort with validation.
        
        Args:
            value: The contextPort to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextPort = None
            return

        self._contextPort = value
        # Stereotypes: atpAbstract.
        self._targetOperation: Optional["ClientServerOperation"] = None

    @property
    def target_operation(self) -> Optional["ClientServerOperation"]:
        """Get targetOperation (Pythonic accessor)."""
        return self._targetOperation

    @target_operation.setter
    def target_operation(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set targetOperation with validation.
        
        Args:
            value: The targetOperation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetOperation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"targetOperation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._targetOperation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "AtomicSwComponent":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "AtomicSwComponent") -> "OperationInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for base with method chaining.
        
        Args:
            value: The base to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
        return self

    def getContextPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for contextPort.
        
        Returns:
            The contextPort value
        
        Note:
            Delegates to context_port property (CODING_RULE_V2_00017)
        """
        return self.context_port  # Delegates to property

    def setContextPort(self, value: RefType) -> "OperationInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for contextPort with method chaining.
        
        Args:
            value: The contextPort to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to context_port property setter (gets validation automatically)
        """
        self.context_port = value  # Delegates to property setter
        return self

    def getTargetOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for targetOperation.
        
        Returns:
            The targetOperation value
        
        Note:
            Delegates to target_operation property (CODING_RULE_V2_00017)
        """
        return self.target_operation  # Delegates to property

    def setTargetOperation(self, value: "ClientServerOperation") -> "OperationInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for targetOperation with method chaining.
        
        Args:
            value: The targetOperation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_operation property setter (gets validation automatically)
        """
        self.target_operation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["AtomicSwComponent"]) -> "OperationInAtomicSwcInstanceRef":
        """
        Set base and return self for chaining.
        
        Args:
            value: The base to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_context_port(self, value: Optional[RefType]) -> "OperationInAtomicSwcInstanceRef":
        """
        Set contextPort and return self for chaining.
        
        Args:
            value: The contextPort to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_context_port("value")
        """
        self.context_port = value  # Use property setter (gets validation)
        return self

    def with_target_operation(self, value: Optional["ClientServerOperation"]) -> "OperationInAtomicSwcInstanceRef":
        """
        Set targetOperation and return self for chaining.
        
        Args:
            value: The targetOperation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_operation("value")
        """
        self.target_operation = value  # Use property setter (gets validation)
        return self