"""
AUTOSAR Package - InstanceRef

Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior::InstanceRef
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)




class InnerDataPrototypeGroupInCompositionInstanceRef(ARObject):
    """
    This meta-class represents the ability to define an InstanceRef to a nested
    DataPrototypeGroup
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior::InstanceRef::InnerDataPrototypeGroupInCompositionInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 954, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the base of the instanceRef.
        # atpDerived 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate
                # Template R23-11.
        self._base: Optional["CompositionSw"] = None

    @property
    def base(self) -> Optional["CompositionSw"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["CompositionSw"]) -> None:
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

        if not isinstance(value, CompositionSw):
            raise TypeError(
                f"base must be CompositionSw or None, got {type(value).__name__}"
            )
        self._base = value
        # This represents the nested structure of SwComponent Prototypes.
        # xml.
        # sequenceOffset=20 (ordered).
        self._contextSw: List["SwComponent"] = []

    @property
    def context_sw(self) -> List["SwComponent"]:
        """Get contextSw (Pythonic accessor)."""
        return self._contextSw
        # This represents the target of the InstanceRef xml.
        # sequenceOffset=30.
        self._targetData: Optional["RefType"] = None

    @property
    def target_data(self) -> Optional["RefType"]:
        """Get targetData (Pythonic accessor)."""
        return self._targetData

    @target_data.setter
    def target_data(self, value: Optional["RefType"]) -> None:
        """
        Set targetData with validation.
        
        Args:
            value: The targetData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetData = None
            return

        self._targetData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "CompositionSw":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "CompositionSw") -> "InnerDataPrototypeGroupInCompositionInstanceRef":
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

    def getContextSw(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for contextSw.
        
        Returns:
            The contextSw value
        
        Note:
            Delegates to context_sw property (CODING_RULE_V2_00017)
        """
        return self.context_sw  # Delegates to property

    def getTargetData(self) -> "RefType":
        """
        AUTOSAR-compliant getter for targetData.
        
        Returns:
            The targetData value
        
        Note:
            Delegates to target_data property (CODING_RULE_V2_00017)
        """
        return self.target_data  # Delegates to property

    def setTargetData(self, value: "RefType") -> "InnerDataPrototypeGroupInCompositionInstanceRef":
        """
        AUTOSAR-compliant setter for targetData with method chaining.
        
        Args:
            value: The targetData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_data property setter (gets validation automatically)
        """
        self.target_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["CompositionSw"]) -> "InnerDataPrototypeGroupInCompositionInstanceRef":
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

    def with_target_data(self, value: Optional[RefType]) -> "InnerDataPrototypeGroupInCompositionInstanceRef":
        """
        Set targetData and return self for chaining.
        
        Args:
            value: The targetData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_data("value")
        """
        self.target_data = value  # Use property setter (gets validation)
        return self



class InnerRunnableEntityGroupInCompositionInstanceRef(ARObject):
    """
    This meta-class represents the ability to define an InstanceRef to a nested
    RunnableEntityGroup.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior::InstanceRef::InnerRunnableEntityGroupInCompositionInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 956, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the base of the InstanceRef.
        # atpDerived.
        self._base: Optional["CompositionSw"] = None

    @property
    def base(self) -> Optional["CompositionSw"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["CompositionSw"]) -> None:
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

        if not isinstance(value, CompositionSw):
            raise TypeError(
                f"base must be CompositionSw or None, got {type(value).__name__}"
            )
        self._base = value
        # This represents the nested structure of SwComponent Prototypes.
        # xml.
        # sequenceOffset=20 (ordered).
        self._contextSw: List["SwComponent"] = []

    @property
    def context_sw(self) -> List["SwComponent"]:
        """Get contextSw (Pythonic accessor)."""
        return self._contextSw
        # This represents the target association of the InstanceRef.
        # xml.
        # sequenceOffset=30.
        self._targetRunnable: "RefType" = None

    @property
    def target_runnable(self) -> "RefType":
        """Get targetRunnable (Pythonic accessor)."""
        return self._targetRunnable

    @target_runnable.setter
    def target_runnable(self, value: "RefType") -> None:
        """
        Set targetRunnable with validation.
        
        Args:
            value: The targetRunnable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        self._targetRunnable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "CompositionSw":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "CompositionSw") -> "InnerRunnableEntityGroupInCompositionInstanceRef":
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

    def getContextSw(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for contextSw.
        
        Returns:
            The contextSw value
        
        Note:
            Delegates to context_sw property (CODING_RULE_V2_00017)
        """
        return self.context_sw  # Delegates to property

    def getTargetRunnable(self) -> "RefType":
        """
        AUTOSAR-compliant getter for targetRunnable.
        
        Returns:
            The targetRunnable value
        
        Note:
            Delegates to target_runnable property (CODING_RULE_V2_00017)
        """
        return self.target_runnable  # Delegates to property

    def setTargetRunnable(self, value: "RefType") -> "InnerRunnableEntityGroupInCompositionInstanceRef":
        """
        AUTOSAR-compliant setter for targetRunnable with method chaining.
        
        Args:
            value: The targetRunnable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_runnable property setter (gets validation automatically)
        """
        self.target_runnable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["CompositionSw"]) -> "InnerRunnableEntityGroupInCompositionInstanceRef":
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

    def with_target_runnable(self, value: RefType) -> "InnerRunnableEntityGroupInCompositionInstanceRef":
        """
        Set targetRunnable and return self for chaining.
        
        Args:
            value: The targetRunnable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_runnable("value")
        """
        self.target_runnable = value  # Use property setter (gets validation)
        return self



class RunnableEntityInCompositionInstanceRef(ARObject):
    """
    This meta-class represents the ability to define an InstanceRef to a
    RunnableEntity in the context of a CompositionSwComponentType.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior::InstanceRef::RunnableEntityInCompositionInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 956, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the base of the InstanceRef.
        # atpDerived.
        self._base: Optional["CompositionSw"] = None

    @property
    def base(self) -> Optional["CompositionSw"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["CompositionSw"]) -> None:
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

        if not isinstance(value, CompositionSw):
            raise TypeError(
                f"base must be CompositionSw or None, got {type(value).__name__}"
            )
        self._base = value
        # This represents the nested structure of SwComponent Prototypes.
        # xml.
        # sequenceOffset=20 (ordered).
        self._contextSw: List["SwComponent"] = []

    @property
    def context_sw(self) -> List["SwComponent"]:
        """Get contextSw (Pythonic accessor)."""
        return self._contextSw
        # This represents the target RunnableEntity.
        # xml.
        # sequenceOffset=30.
        self._targetRunnable: Optional["RunnableEntity"] = None

    @property
    def target_runnable(self) -> Optional["RunnableEntity"]:
        """Get targetRunnable (Pythonic accessor)."""
        return self._targetRunnable

    @target_runnable.setter
    def target_runnable(self, value: Optional["RunnableEntity"]) -> None:
        """
        Set targetRunnable with validation.
        
        Args:
            value: The targetRunnable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetRunnable = None
            return

        if not isinstance(value, RunnableEntity):
            raise TypeError(
                f"targetRunnable must be RunnableEntity or None, got {type(value).__name__}"
            )
        self._targetRunnable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "CompositionSw":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "CompositionSw") -> "RunnableEntityInCompositionInstanceRef":
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

    def getContextSw(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for contextSw.
        
        Returns:
            The contextSw value
        
        Note:
            Delegates to context_sw property (CODING_RULE_V2_00017)
        """
        return self.context_sw  # Delegates to property

    def getTargetRunnable(self) -> "RunnableEntity":
        """
        AUTOSAR-compliant getter for targetRunnable.
        
        Returns:
            The targetRunnable value
        
        Note:
            Delegates to target_runnable property (CODING_RULE_V2_00017)
        """
        return self.target_runnable  # Delegates to property

    def setTargetRunnable(self, value: "RunnableEntity") -> "RunnableEntityInCompositionInstanceRef":
        """
        AUTOSAR-compliant setter for targetRunnable with method chaining.
        
        Args:
            value: The targetRunnable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_runnable property setter (gets validation automatically)
        """
        self.target_runnable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["CompositionSw"]) -> "RunnableEntityInCompositionInstanceRef":
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

    def with_target_runnable(self, value: Optional["RunnableEntity"]) -> "RunnableEntityInCompositionInstanceRef":
        """
        Set targetRunnable and return self for chaining.
        
        Args:
            value: The targetRunnable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_runnable("value")
        """
        self.target_runnable = value  # Use property setter (gets validation)
        return self



class VariableDataPrototypeInCompositionInstanceRef(ARObject):
    """
    This meta-class represents the ability to define an InstanceRef to a
    VariableDataPrototype in the context of a CompositionSwComponentType.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ImplicitCommunicationBehavior::InstanceRef::VariableDataPrototypeInCompositionInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 959, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the base of the InstanceRef.
        # atpDerived.
        self._base: Optional["CompositionSw"] = None

    @property
    def base(self) -> Optional["CompositionSw"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["CompositionSw"]) -> None:
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

        if not isinstance(value, CompositionSw):
            raise TypeError(
                f"base must be CompositionSw or None, got {type(value).__name__}"
            )
        self._base = value
        # This represents a reference to a context PortPrototype.
        # xml.
        # sequenceOffset=30.
        self._contextPort: Optional["RefType"] = None

    @property
    def context_port(self) -> Optional["RefType"]:
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: Optional["RefType"]) -> None:
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
        # This represents the nested structure of SwComponent Prototypes.
        # xml.
        # sequenceOffset=20 (ordered).
        self._contextSw: List["SwComponent"] = []

    @property
    def context_sw(self) -> List["SwComponent"]:
        """Get contextSw (Pythonic accessor)."""
        return self._contextSw
        # This represents the target VariableDataPrototype.
        # xml.
        # sequenceOffset=40.
        self._targetVariable: Optional["RefType"] = None

    @property
    def target_variable(self) -> Optional["RefType"]:
        """Get targetVariable (Pythonic accessor)."""
        return self._targetVariable

    @target_variable.setter
    def target_variable(self, value: Optional["RefType"]) -> None:
        """
        Set targetVariable with validation.
        
        Args:
            value: The targetVariable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetVariable = None
            return

        self._targetVariable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "CompositionSw":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "CompositionSw") -> "VariableDataPrototypeInCompositionInstanceRef":
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

    def getContextPort(self) -> "RefType":
        """
        AUTOSAR-compliant getter for contextPort.
        
        Returns:
            The contextPort value
        
        Note:
            Delegates to context_port property (CODING_RULE_V2_00017)
        """
        return self.context_port  # Delegates to property

    def setContextPort(self, value: "RefType") -> "VariableDataPrototypeInCompositionInstanceRef":
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

    def getContextSw(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for contextSw.
        
        Returns:
            The contextSw value
        
        Note:
            Delegates to context_sw property (CODING_RULE_V2_00017)
        """
        return self.context_sw  # Delegates to property

    def getTargetVariable(self) -> "RefType":
        """
        AUTOSAR-compliant getter for targetVariable.
        
        Returns:
            The targetVariable value
        
        Note:
            Delegates to target_variable property (CODING_RULE_V2_00017)
        """
        return self.target_variable  # Delegates to property

    def setTargetVariable(self, value: "RefType") -> "VariableDataPrototypeInCompositionInstanceRef":
        """
        AUTOSAR-compliant setter for targetVariable with method chaining.
        
        Args:
            value: The targetVariable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_variable property setter (gets validation automatically)
        """
        self.target_variable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["CompositionSw"]) -> "VariableDataPrototypeInCompositionInstanceRef":
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

    def with_context_port(self, value: Optional[RefType]) -> "VariableDataPrototypeInCompositionInstanceRef":
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

    def with_target_variable(self, value: Optional[RefType]) -> "VariableDataPrototypeInCompositionInstanceRef":
        """
        Set targetVariable and return self for chaining.
        
        Args:
            value: The targetVariable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_variable("value")
        """
        self.target_variable = value  # Use property setter (gets validation)
        return self