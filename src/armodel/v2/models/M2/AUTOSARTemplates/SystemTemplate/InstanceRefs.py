"""
AUTOSAR Package - InstanceRefs

Package: M2::AUTOSARTemplates::SystemTemplate::InstanceRefs
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ComponentInSystemInstanceRef(ARObject):
    """
    
    Package: M2::AUTOSARTemplates::SystemTemplate::InstanceRefs::ComponentInSystemInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 999, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived.
        self._base: Optional["System"] = None

    @property
    def base(self) -> Optional["System"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["System"]) -> None:
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

        if not isinstance(value, System):
            raise TypeError(
                f"base must be System or None, got {type(value).__name__}"
            )
        self._base = value
        # sequenceOffset=20.
        self._context: Optional["RootSwComposition"] = None

    @property
    def context(self) -> Optional["RootSwComposition"]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional["RootSwComposition"]) -> None:
        """
        Set context with validation.
        
        Args:
            value: The context to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._context = None
            return

        if not isinstance(value, RootSwComposition):
            raise TypeError(
                f"context must be RootSwComposition or None, got {type(value).__name__}"
            )
        self._context = value
        # sequenceOffset=40.
        self._target: "SwComponent" = None

    @property
    def target(self) -> "SwComponent":
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: "SwComponent") -> None:
        """
        Set target with validation.
        
        Args:
            value: The target to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, SwComponent):
            raise TypeError(
                f"target must be SwComponent, got {type(value).__name__}"
            )
        self._target = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "System":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "System") -> "ComponentInSystemInstanceRef":
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

    def getContext(self) -> "RootSwComposition":
        """
        AUTOSAR-compliant getter for context.
        
        Returns:
            The context value
        
        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: "RootSwComposition") -> "ComponentInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for context with method chaining.
        
        Args:
            value: The context to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to context property setter (gets validation automatically)
        """
        self.context = value  # Delegates to property setter
        return self

    def getTarget(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for target.
        
        Returns:
            The target value
        
        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: "SwComponent") -> "ComponentInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for target with method chaining.
        
        Args:
            value: The target to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target property setter (gets validation automatically)
        """
        self.target = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["System"]) -> "ComponentInSystemInstanceRef":
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

    def with_context(self, value: Optional["RootSwComposition"]) -> "ComponentInSystemInstanceRef":
        """
        Set context and return self for chaining.
        
        Args:
            value: The context to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_target(self, value: "SwComponent") -> "ComponentInSystemInstanceRef":
        """
        Set target and return self for chaining.
        
        Args:
            value: The target to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target("value")
        """
        self.target = value  # Use property setter (gets validation)
        return self



class OperationInSystemInstanceRef(ARObject):
    """
    
    Package: M2::AUTOSARTemplates::SystemTemplate::InstanceRefs::OperationInSystemInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1001, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived.
        self._base: Optional["System"] = None

    @property
    def base(self) -> Optional["System"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["System"]) -> None:
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

        if not isinstance(value, System):
            raise TypeError(
                f"base must be System or None, got {type(value).__name__}"
            )
        self._base = value
        # sequenceOffset=20.
        self._context: Optional["RootSwComposition"] = None

    @property
    def context(self) -> Optional["RootSwComposition"]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional["RootSwComposition"]) -> None:
        """
        Set context with validation.
        
        Args:
            value: The context to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._context = None
            return

        if not isinstance(value, RootSwComposition):
            raise TypeError(
                f"context must be RootSwComposition or None, got {type(value).__name__}"
            )
        self._context = value
        # sequenceOffset=40.
        self._contextPort: "RefType" = None

    @property
    def context_port(self) -> "RefType":
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: "RefType") -> None:
        """
        Set contextPort with validation.
        
        Args:
            value: The contextPort to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        self._contextPort = value
        # sequenceOffset=50.
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

    def getBase(self) -> "System":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "System") -> "OperationInSystemInstanceRef":
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

    def getContext(self) -> "RootSwComposition":
        """
        AUTOSAR-compliant getter for context.
        
        Returns:
            The context value
        
        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: "RootSwComposition") -> "OperationInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for context with method chaining.
        
        Args:
            value: The context to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to context property setter (gets validation automatically)
        """
        self.context = value  # Delegates to property setter
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

    def setContextPort(self, value: "RefType") -> "OperationInSystemInstanceRef":
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

    def setTargetOperation(self, value: "ClientServerOperation") -> "OperationInSystemInstanceRef":
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

    def with_base(self, value: Optional["System"]) -> "OperationInSystemInstanceRef":
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

    def with_context(self, value: Optional["RootSwComposition"]) -> "OperationInSystemInstanceRef":
        """
        Set context and return self for chaining.
        
        Args:
            value: The context to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_context_port(self, value: RefType) -> "OperationInSystemInstanceRef":
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

    def with_target_operation(self, value: Optional["ClientServerOperation"]) -> "OperationInSystemInstanceRef":
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



class VariableDataPrototypeInSystemInstanceRef(ARObject):
    """
    
    Package: M2::AUTOSARTemplates::SystemTemplate::InstanceRefs::VariableDataPrototypeInSystemInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1003, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived.
        self._base: Optional["System"] = None

    @property
    def base(self) -> Optional["System"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["System"]) -> None:
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

        if not isinstance(value, System):
            raise TypeError(
                f"base must be System or None, got {type(value).__name__}"
            )
        self._base = value

    @property
    def context(self) -> Optional["RootSwComposition"]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional["RootSwComposition"]) -> None:
        """
        Set context with validation.
        
        Args:
            value: The context to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._context = None
            return

        if not isinstance(value, RootSwComposition):
            raise TypeError(
                f"context must be RootSwComposition or None, got {type(value).__name__}"
            )
        self._context = value

    @property
    def context_port(self) -> "RefType":
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: "RefType") -> None:
        """
        Set contextPort with validation.
        
        Args:
            value: The contextPort to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        self._contextPort = value

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

    def getBase(self) -> "System":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "System") -> "VariableDataPrototypeInSystemInstanceRef":
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

    def getContext(self) -> "RootSwComposition":
        """
        AUTOSAR-compliant getter for context.
        
        Returns:
            The context value
        
        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: "RootSwComposition") -> "VariableDataPrototypeInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for context with method chaining.
        
        Args:
            value: The context to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to context property setter (gets validation automatically)
        """
        self.context = value  # Delegates to property setter
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

    def setContextPort(self, value: "RefType") -> "VariableDataPrototypeInSystemInstanceRef":
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

    def getTargetData(self) -> "RefType":
        """
        AUTOSAR-compliant getter for targetData.
        
        Returns:
            The targetData value
        
        Note:
            Delegates to target_data property (CODING_RULE_V2_00017)
        """
        return self.target_data  # Delegates to property

    def setTargetData(self, value: "RefType") -> "VariableDataPrototypeInSystemInstanceRef":
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

    def with_base(self, value: Optional["System"]) -> "VariableDataPrototypeInSystemInstanceRef":
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

    def with_context(self, value: Optional["RootSwComposition"]) -> "VariableDataPrototypeInSystemInstanceRef":
        """
        Set context and return self for chaining.
        
        Args:
            value: The context to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_context_port(self, value: RefType) -> "VariableDataPrototypeInSystemInstanceRef":
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

    def with_target_data(self, value: Optional[RefType]) -> "VariableDataPrototypeInSystemInstanceRef":
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



class TriggerInSystemInstanceRef(ARObject):
    """
    
    Package: M2::AUTOSARTemplates::SystemTemplate::InstanceRefs::TriggerInSystemInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1005, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents that base of the InstanceRef.
        self._base: Optional["System"] = None

    @property
    def base(self) -> Optional["System"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["System"]) -> None:
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

        if not isinstance(value, System):
            raise TypeError(
                f"base must be System or None, got {type(value).__name__}"
            )
        self._base = value
        # context of the Instance.
        self._context: Optional["RootSwComposition"] = None

    @property
    def context(self) -> Optional["RootSwComposition"]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional["RootSwComposition"]) -> None:
        """
        Set context with validation.
        
        Args:
            value: The context to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._context = None
            return

        if not isinstance(value, RootSwComposition):
            raise TypeError(
                f"context must be RootSwComposition or None, got {type(value).__name__}"
            )
        self._context = value
        self._contextPort: "RefType" = None

    @property
    def context_port(self) -> "RefType":
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: "RefType") -> None:
        """
        Set contextPort with validation.
        
        Args:
            value: The contextPort to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        self._contextPort = value
        self._targetTrigger: Optional["RefType"] = None

    @property
    def target_trigger(self) -> Optional["RefType"]:
        """Get targetTrigger (Pythonic accessor)."""
        return self._targetTrigger

    @target_trigger.setter
    def target_trigger(self, value: Optional["RefType"]) -> None:
        """
        Set targetTrigger with validation.
        
        Args:
            value: The targetTrigger to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetTrigger = None
            return

        self._targetTrigger = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "System":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "System") -> "TriggerInSystemInstanceRef":
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

    def getContext(self) -> "RootSwComposition":
        """
        AUTOSAR-compliant getter for context.
        
        Returns:
            The context value
        
        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: "RootSwComposition") -> "TriggerInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for context with method chaining.
        
        Args:
            value: The context to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to context property setter (gets validation automatically)
        """
        self.context = value  # Delegates to property setter
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

    def setContextPort(self, value: "RefType") -> "TriggerInSystemInstanceRef":
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

    def getTargetTrigger(self) -> "RefType":
        """
        AUTOSAR-compliant getter for targetTrigger.
        
        Returns:
            The targetTrigger value
        
        Note:
            Delegates to target_trigger property (CODING_RULE_V2_00017)
        """
        return self.target_trigger  # Delegates to property

    def setTargetTrigger(self, value: "RefType") -> "TriggerInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for targetTrigger with method chaining.
        
        Args:
            value: The targetTrigger to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_trigger property setter (gets validation automatically)
        """
        self.target_trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["System"]) -> "TriggerInSystemInstanceRef":
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

    def with_context(self, value: Optional["RootSwComposition"]) -> "TriggerInSystemInstanceRef":
        """
        Set context and return self for chaining.
        
        Args:
            value: The context to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_context_port(self, value: RefType) -> "TriggerInSystemInstanceRef":
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

    def with_target_trigger(self, value: Optional[RefType]) -> "TriggerInSystemInstanceRef":
        """
        Set targetTrigger and return self for chaining.
        
        Args:
            value: The targetTrigger to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_trigger("value")
        """
        self.target_trigger = value  # Use property setter (gets validation)
        return self



class PortGroupInSystemInstanceRef(ARObject):
    """
    
    Package: M2::AUTOSARTemplates::SystemTemplate::InstanceRefs::PortGroupInSystemInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1007, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived.
        self._base: Optional["System"] = None

    @property
    def base(self) -> Optional["System"]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional["System"]) -> None:
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

        if not isinstance(value, System):
            raise TypeError(
                f"base must be System or None, got {type(value).__name__}"
            )
        self._base = value
        # sequenceOffset=20.
        self._context: Optional["RootSwComposition"] = None

    @property
    def context(self) -> Optional["RootSwComposition"]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional["RootSwComposition"]) -> None:
        """
        Set context with validation.
        
        Args:
            value: The context to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._context = None
            return

        if not isinstance(value, RootSwComposition):
            raise TypeError(
                f"context must be RootSwComposition or None, got {type(value).__name__}"
            )
        self._context = value
        # CompositionSwComponentType.
        self._target: "RefType" = None

    @property
    def target(self) -> "RefType":
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: "RefType") -> None:
        """
        Set target with validation.
        
        Args:
            value: The target to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        self._target = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "System":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "System") -> "PortGroupInSystemInstanceRef":
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

    def getContext(self) -> "RootSwComposition":
        """
        AUTOSAR-compliant getter for context.
        
        Returns:
            The context value
        
        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: "RootSwComposition") -> "PortGroupInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for context with method chaining.
        
        Args:
            value: The context to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to context property setter (gets validation automatically)
        """
        self.context = value  # Delegates to property setter
        return self

    def getTarget(self) -> "RefType":
        """
        AUTOSAR-compliant getter for target.
        
        Returns:
            The target value
        
        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: "RefType") -> "PortGroupInSystemInstanceRef":
        """
        AUTOSAR-compliant setter for target with method chaining.
        
        Args:
            value: The target to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target property setter (gets validation automatically)
        """
        self.target = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["System"]) -> "PortGroupInSystemInstanceRef":
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

    def with_context(self, value: Optional["RootSwComposition"]) -> "PortGroupInSystemInstanceRef":
        """
        Set context and return self for chaining.
        
        Args:
            value: The context to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_context("value")
        """
        self.context = value  # Use property setter (gets validation)
        return self

    def with_target(self, value: RefType) -> "PortGroupInSystemInstanceRef":
        """
        Set target and return self for chaining.
        
        Args:
            value: The target to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target("value")
        """
        self.target = value  # Use property setter (gets validation)
        return self
