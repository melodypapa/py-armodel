from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class VariableInAtomicSwcInstanceRef(ARObject, ABC):
    """
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::VariableInAtomicSwcInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 941, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is VariableInAtomicSwcInstanceRef:
            raise TypeError("VariableInAtomicSwcInstanceRef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpAbstract xml.
        # sequenceOffset=30.
        self._abstractTarget: RefType = None

    @property
    def abstract_target(self) -> RefType:
        """Get abstractTarget (Pythonic accessor)."""
        return self._abstractTarget

    @abstract_target.setter
    def abstract_target(self, value: RefType) -> None:
        """
        Set abstractTarget with validation.
        
        Args:
            value: The abstractTarget to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._abstractTarget = None
            return

        self._abstractTarget = value
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAbstractTarget(self) -> RefType:
        """
        AUTOSAR-compliant getter for abstractTarget.
        
        Returns:
            The abstractTarget value
        
        Note:
            Delegates to abstract_target property (CODING_RULE_V2_00017)
        """
        return self.abstract_target  # Delegates to property

    def setAbstractTarget(self, value: RefType) -> "VariableInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for abstractTarget with method chaining.
        
        Args:
            value: The abstractTarget to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to abstract_target property setter (gets validation automatically)
        """
        self.abstract_target = value  # Delegates to property setter
        return self

    def getBase(self) -> "AtomicSwComponent":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "AtomicSwComponent") -> "VariableInAtomicSwcInstanceRef":
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

    def setContextPort(self, value: RefType) -> "VariableInAtomicSwcInstanceRef":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_abstract_target(self, value: Optional[RefType]) -> "VariableInAtomicSwcInstanceRef":
        """
        Set abstractTarget and return self for chaining.
        
        Args:
            value: The abstractTarget to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_abstract_target("value")
        """
        self.abstract_target = value  # Use property setter (gets validation)
        return self

    def with_base(self, value: Optional["AtomicSwComponent"]) -> "VariableInAtomicSwcInstanceRef":
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

    def with_context_port(self, value: Optional[RefType]) -> "VariableInAtomicSwcInstanceRef":
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