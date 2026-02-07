from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class RModeInAtomicSwcInstanceRef(ARObject):
    """
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::RModeInAtomicSwcInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 943, Classic Platform
      R23-11)
    """
    def __init__(self):
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
        # Tags: xml.
        # sequenceOffset=30.
        self._contextModeGroupPrototype: RefType = None

    @property
    def context_mode_group_prototype(self) -> RefType:
        """Get contextModeGroupPrototype (Pythonic accessor)."""
        return self._contextModeGroupPrototype

    @context_mode_group_prototype.setter
    def context_mode_group_prototype(self, value: RefType) -> None:
        """
        Set contextModeGroupPrototype with validation.
        
        Args:
            value: The contextModeGroupPrototype to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextModeGroupPrototype = None
            return

        self._contextModeGroupPrototype = value
        # Tags: xml.
        # sequenceOffset=20.
        self._contextPortPrototype: Optional["AbstractRequiredPort"] = None

    @property
    def context_port_prototype(self) -> Optional["AbstractRequiredPort"]:
        """Get contextPortPrototype (Pythonic accessor)."""
        return self._contextPortPrototype

    @context_port_prototype.setter
    def context_port_prototype(self, value: Optional["AbstractRequiredPort"]) -> None:
        """
        Set contextPortPrototype with validation.
        
        Args:
            value: The contextPortPrototype to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextPortPrototype = None
            return

        if not isinstance(value, AbstractRequiredPort):
            raise TypeError(
                f"contextPortPrototype must be AbstractRequiredPort or None, got {type(value).__name__}"
            )
        self._contextPortPrototype = value
        # Tags: xml.
        # sequenceOffset=40.
        self._targetModeDeclaration: Optional["ModeDeclaration"] = None

    @property
    def target_mode_declaration(self) -> Optional["ModeDeclaration"]:
        """Get targetModeDeclaration (Pythonic accessor)."""
        return self._targetModeDeclaration

    @target_mode_declaration.setter
    def target_mode_declaration(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set targetModeDeclaration with validation.
        
        Args:
            value: The targetModeDeclaration to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetModeDeclaration = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"targetModeDeclaration must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._targetModeDeclaration = value

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

    def setBase(self, value: "AtomicSwComponent") -> "RModeInAtomicSwcInstanceRef":
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

    def getContextModeGroupPrototype(self) -> RefType:
        """
        AUTOSAR-compliant getter for contextModeGroupPrototype.
        
        Returns:
            The contextModeGroupPrototype value
        
        Note:
            Delegates to context_mode_group_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_mode_group_prototype  # Delegates to property

    def setContextModeGroupPrototype(self, value: RefType) -> "RModeInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for contextModeGroupPrototype with method chaining.
        
        Args:
            value: The contextModeGroupPrototype to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to context_mode_group_prototype property setter (gets validation automatically)
        """
        self.context_mode_group_prototype = value  # Delegates to property setter
        return self

    def getContextPortPrototype(self) -> "AbstractRequiredPort":
        """
        AUTOSAR-compliant getter for contextPortPrototype.
        
        Returns:
            The contextPortPrototype value
        
        Note:
            Delegates to context_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_port_prototype  # Delegates to property

    def setContextPortPrototype(self, value: "AbstractRequiredPort") -> "RModeInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for contextPortPrototype with method chaining.
        
        Args:
            value: The contextPortPrototype to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to context_port_prototype property setter (gets validation automatically)
        """
        self.context_port_prototype = value  # Delegates to property setter
        return self

    def getTargetModeDeclaration(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for targetModeDeclaration.
        
        Returns:
            The targetModeDeclaration value
        
        Note:
            Delegates to target_mode_declaration property (CODING_RULE_V2_00017)
        """
        return self.target_mode_declaration  # Delegates to property

    def setTargetModeDeclaration(self, value: "ModeDeclaration") -> "RModeInAtomicSwcInstanceRef":
        """
        AUTOSAR-compliant setter for targetModeDeclaration with method chaining.
        
        Args:
            value: The targetModeDeclaration to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_mode_declaration property setter (gets validation automatically)
        """
        self.target_mode_declaration = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["AtomicSwComponent"]) -> "RModeInAtomicSwcInstanceRef":
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

    def with_context_mode_group_prototype(self, value: Optional[RefType]) -> "RModeInAtomicSwcInstanceRef":
        """
        Set contextModeGroupPrototype and return self for chaining.
        
        Args:
            value: The contextModeGroupPrototype to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_context_mode_group_prototype("value")
        """
        self.context_mode_group_prototype = value  # Use property setter (gets validation)
        return self

    def with_context_port_prototype(self, value: Optional["AbstractRequiredPort"]) -> "RModeInAtomicSwcInstanceRef":
        """
        Set contextPortPrototype and return self for chaining.
        
        Args:
            value: The contextPortPrototype to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_context_port_prototype("value")
        """
        self.context_port_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_mode_declaration(self, value: Optional["ModeDeclaration"]) -> "RModeInAtomicSwcInstanceRef":
        """
        Set targetModeDeclaration and return self for chaining.
        
        Args:
            value: The targetModeDeclaration to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_mode_declaration("value")
        """
        self.target_mode_declaration = value  # Use property setter (gets validation)
        return self