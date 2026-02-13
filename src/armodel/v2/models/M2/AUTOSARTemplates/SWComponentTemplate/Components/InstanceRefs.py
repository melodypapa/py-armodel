"""
AUTOSAR Package - InstanceRefs

Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (    AtomicSwComponent,    SwComponent,)from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (    AbstractProvidedPort,    AbstractRequiredPort,    ClientServerOperation,)from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure import (    ModeDeclaration,)

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
        self._abstractTarget: Optional[RefType] = None

    @property
    def abstract_target(self) -> Optional[RefType]:
        """Get abstractTarget (Pythonic accessor)."""
        return self._abstractTarget

    @abstract_target.setter
    def abstract_target(self, value: Optional[RefType]) -> None:
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
        # sequenceOffset=10.
        self._base: Optional[AtomicSwComponent] = None

    @property
    def base(self) -> Optional[AtomicSwComponent]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional[AtomicSwComponent]) -> None:
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
        self._contextPort: Optional[RefType] = None

    @property
    def context_port(self) -> Optional[RefType]:
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: Optional[RefType]) -> None:
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

    def with_context(self, value):
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

    def setAbstractTarget(self, value: RefType) -> VariableInAtomicSwcInstanceRef:
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

    def getBase(self) -> AtomicSwComponent:
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: AtomicSwComponent) -> VariableInAtomicSwcInstanceRef:
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

    def setContextPort(self, value: RefType) -> VariableInAtomicSwcInstanceRef:
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

    def with_abstract_target(self, value: Optional[RefType]) -> VariableInAtomicSwcInstanceRef:
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

    def with_base(self, value: Optional[AtomicSwComponent]) -> VariableInAtomicSwcInstanceRef:
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

    def with_context_port(self, value: Optional[RefType]) -> VariableInAtomicSwcInstanceRef:
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
        self._base: Optional[AtomicSwComponent] = None

    @property
    def base(self) -> Optional[AtomicSwComponent]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional[AtomicSwComponent]) -> None:
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
        # sequenceOffset=30.
        self._contextModeGroupPrototype: Optional[RefType] = None

    @property
    def context_mode_group_prototype(self) -> Optional[RefType]:
        """Get contextModeGroupPrototype (Pythonic accessor)."""
        return self._contextModeGroupPrototype

    @context_mode_group_prototype.setter
    def context_mode_group_prototype(self, value: Optional[RefType]) -> None:
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
        # sequenceOffset=20.
        self._contextPortPrototype: Optional[AbstractRequiredPort] = None

    @property
    def context_port_prototype(self) -> Optional[AbstractRequiredPort]:
        """Get contextPortPrototype (Pythonic accessor)."""
        return self._contextPortPrototype

    @context_port_prototype.setter
    def context_port_prototype(self, value: Optional[AbstractRequiredPort]) -> None:
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
        # sequenceOffset=40.
        self._targetModeDeclaration: Optional[ModeDeclaration] = None

    @property
    def target_mode_declaration(self) -> Optional[ModeDeclaration]:
        """Get targetModeDeclaration (Pythonic accessor)."""
        return self._targetModeDeclaration

    @target_mode_declaration.setter
    def target_mode_declaration(self, value: Optional[ModeDeclaration]) -> None:
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

    def getBase(self) -> AtomicSwComponent:
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: AtomicSwComponent) -> RModeInAtomicSwcInstanceRef:
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

    def setContextModeGroupPrototype(self, value: RefType) -> RModeInAtomicSwcInstanceRef:
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

    def getContextPortPrototype(self) -> AbstractRequiredPort:
        """
        AUTOSAR-compliant getter for contextPortPrototype.

        Returns:
            The contextPortPrototype value

        Note:
            Delegates to context_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_port_prototype  # Delegates to property

    def setContextPortPrototype(self, value: AbstractRequiredPort) -> RModeInAtomicSwcInstanceRef:
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

    def setTargetModeDeclaration(self, value: "ModeDeclaration") -> RModeInAtomicSwcInstanceRef:
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

    def with_base(self, value: Optional[AtomicSwComponent]) -> RModeInAtomicSwcInstanceRef:
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

    def with_context_mode_group_prototype(self, value: Optional[RefType]) -> RModeInAtomicSwcInstanceRef:
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

    def with_context_port_prototype(self, value: Optional[AbstractRequiredPort]) -> RModeInAtomicSwcInstanceRef:
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

    def with_target_mode_declaration(self, value: Optional[ModeDeclaration]) -> RModeInAtomicSwcInstanceRef:
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



class InnerPortGroupInCompositionInstanceRef(ARObject):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::InnerPortGroupInCompositionInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 943, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived xml.
        # sequenceOffset=10.
        self._base: Optional[CompositionSw] = None

    @property
    def base(self) -> Optional[CompositionSw]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional[CompositionSw]) -> None:
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
        # sequenceOffset=20.
        self._context: List[SwComponent] = []

    @property
    def context(self) -> List[SwComponent]:
        """Get context (Pythonic accessor)."""
        return self._context
        # Links a PortGroup in a composition to another PortGroup, defined in a
        # component which is part of this shall be at most per contained
        # SwComponentPrototype.
        self._target: Optional[RefType] = None

    @property
    def target(self) -> Optional[RefType]:
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: Optional[RefType]) -> None:
        """
        Set target with validation.

        Args:
            value: The target to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._target = None
            return

        self._target = value

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

    def setBase(self, value: "CompositionSw") -> InnerPortGroupInCompositionInstanceRef:
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

    def getContext(self) -> List[SwComponent]:
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def getTarget(self) -> RefType:
        """
        AUTOSAR-compliant getter for target.

        Returns:
            The target value

        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: RefType) -> InnerPortGroupInCompositionInstanceRef:
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

    def with_base(self, value: Optional[CompositionSw]) -> InnerPortGroupInCompositionInstanceRef:
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

    def with_target(self, value: Optional[RefType]) -> InnerPortGroupInCompositionInstanceRef:
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



class TriggerInAtomicSwcInstanceRef(ARObject, ABC):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::TriggerInAtomicSwcInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 944, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is TriggerInAtomicSwcInstanceRef:
            raise TypeError("TriggerInAtomicSwcInstanceRef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived xml.
        # sequenceOffset=10.
        self._base: Optional[AtomicSwComponent] = None

    @property
    def base(self) -> Optional[AtomicSwComponent]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional[AtomicSwComponent]) -> None:
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
        self._contextPort: Optional[RefType] = None

    @property
    def context_port(self) -> Optional[RefType]:
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: Optional[RefType]) -> None:
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
        self._target: Optional[RefType] = None

    @property
    def target(self) -> Optional[RefType]:
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: Optional[RefType]) -> None:
        """
        Set target with validation.

        Args:
            value: The target to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._target = None
            return

        self._target = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> AtomicSwComponent:
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: AtomicSwComponent) -> TriggerInAtomicSwcInstanceRef:
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

    def setContextPort(self, value: RefType) -> TriggerInAtomicSwcInstanceRef:
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

    def getTarget(self) -> RefType:
        """
        AUTOSAR-compliant getter for target.

        Returns:
            The target value

        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: RefType) -> TriggerInAtomicSwcInstanceRef:
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

    def with_base(self, value: Optional[AtomicSwComponent]) -> TriggerInAtomicSwcInstanceRef:
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

    def with_context_port(self, value: Optional[RefType]) -> TriggerInAtomicSwcInstanceRef:
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

    def with_target(self, value: Optional[RefType]) -> TriggerInAtomicSwcInstanceRef:
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
        self._base: Optional[AtomicSwComponent] = None

    @property
    def base(self) -> Optional[AtomicSwComponent]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional[AtomicSwComponent]) -> None:
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
        self._contextPort: Optional[RefType] = None

    @property
    def context_port(self) -> Optional[RefType]:
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: Optional[RefType]) -> None:
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
        self._targetOperation: Optional[ClientServerOperation] = None

    @property
    def target_operation(self) -> Optional[ClientServerOperation]:
        """Get targetOperation (Pythonic accessor)."""
        return self._targetOperation

    @target_operation.setter
    def target_operation(self, value: Optional[ClientServerOperation]) -> None:
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

    def getBase(self) -> AtomicSwComponent:
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: AtomicSwComponent) -> OperationInAtomicSwcInstanceRef:
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

    def setContextPort(self, value: RefType) -> OperationInAtomicSwcInstanceRef:
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

    def getTargetOperation(self) -> ClientServerOperation:
        """
        AUTOSAR-compliant getter for targetOperation.

        Returns:
            The targetOperation value

        Note:
            Delegates to target_operation property (CODING_RULE_V2_00017)
        """
        return self.target_operation  # Delegates to property

    def setTargetOperation(self, value: ClientServerOperation) -> OperationInAtomicSwcInstanceRef:
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

    def with_base(self, value: Optional[AtomicSwComponent]) -> OperationInAtomicSwcInstanceRef:
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

    def with_context_port(self, value: Optional[RefType]) -> OperationInAtomicSwcInstanceRef:
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

    def with_target_operation(self, value: Optional[ClientServerOperation]) -> OperationInAtomicSwcInstanceRef:
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



class ModeGroupInAtomicSwcInstanceRef(ARObject, ABC):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::ModeGroupInAtomicSwcInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 961, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is ModeGroupInAtomicSwcInstanceRef:
            raise TypeError("ModeGroupInAtomicSwcInstanceRef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived xml.
        # sequenceOffset=10.
        self._base: Optional[AtomicSwComponent] = None

    @property
    def base(self) -> Optional[AtomicSwComponent]:
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: Optional[AtomicSwComponent]) -> None:
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
        self._contextPort: Optional[RefType] = None

    @property
    def context_port(self) -> Optional[RefType]:
        """Get contextPort (Pythonic accessor)."""
        return self._contextPort

    @context_port.setter
    def context_port(self, value: Optional[RefType]) -> None:
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
        # sequenceOffset=30.
        self._target: Optional[RefType] = None

    @property
    def target(self) -> Optional[RefType]:
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: Optional[RefType]) -> None:
        """
        Set target with validation.

        Args:
            value: The target to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._target = None
            return

        self._target = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> AtomicSwComponent:
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: AtomicSwComponent) -> ModeGroupInAtomicSwcInstanceRef:
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

    def setContextPort(self, value: RefType) -> ModeGroupInAtomicSwcInstanceRef:
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

    def getTarget(self) -> RefType:
        """
        AUTOSAR-compliant getter for target.

        Returns:
            The target value

        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: RefType) -> ModeGroupInAtomicSwcInstanceRef:
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

    def with_base(self, value: Optional[AtomicSwComponent]) -> ModeGroupInAtomicSwcInstanceRef:
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

    def with_context_port(self, value: Optional[RefType]) -> ModeGroupInAtomicSwcInstanceRef:
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

    def with_target(self, value: Optional[RefType]) -> ModeGroupInAtomicSwcInstanceRef:
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



class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::RVariableInAtomicSwcInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 943, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tags: xml.
        # sequenceOffset=20.
        self._contextRPortPrototype: Optional[AbstractRequiredPort] = None

    @property
    def context_r_port_prototype(self) -> Optional[AbstractRequiredPort]:
        """Get contextRPortPrototype (Pythonic accessor)."""
        return self._contextRPortPrototype

    @context_r_port_prototype.setter
    def context_r_port_prototype(self, value: Optional[AbstractRequiredPort]) -> None:
        """
        Set contextRPortPrototype with validation.

        Args:
            value: The contextRPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextRPortPrototype = None
            return

        if not isinstance(value, AbstractRequiredPort):
            raise TypeError(
                f"contextRPortPrototype must be AbstractRequiredPort or None, got {type(value).__name__}"
            )
        self._contextRPortPrototype = value
        # sequenceOffset=30.
        self._targetDataElement: Optional[RefType] = None

    @property
    def target_data_element(self) -> Optional[RefType]:
        """Get targetDataElement (Pythonic accessor)."""
        return self._targetDataElement

    @target_data_element.setter
    def target_data_element(self, value: Optional[RefType]) -> None:
        """
        Set targetDataElement with validation.

        Args:
            value: The targetDataElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetDataElement = None
            return

        self._targetDataElement = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextRPortPrototype(self) -> AbstractRequiredPort:
        """
        AUTOSAR-compliant getter for contextRPortPrototype.

        Returns:
            The contextRPortPrototype value

        Note:
            Delegates to context_r_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_r_port_prototype  # Delegates to property

    def setContextRPortPrototype(self, value: AbstractRequiredPort) -> RVariableInAtomicSwcInstanceRef:
        """
        AUTOSAR-compliant setter for contextRPortPrototype with method chaining.

        Args:
            value: The contextRPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_r_port_prototype property setter (gets validation automatically)
        """
        self.context_r_port_prototype = value  # Delegates to property setter
        return self

    def getTargetDataElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetDataElement.

        Returns:
            The targetDataElement value

        Note:
            Delegates to target_data_element property (CODING_RULE_V2_00017)
        """
        return self.target_data_element  # Delegates to property

    def setTargetDataElement(self, value: RefType) -> RVariableInAtomicSwcInstanceRef:
        """
        AUTOSAR-compliant setter for targetDataElement with method chaining.

        Args:
            value: The targetDataElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_data_element property setter (gets validation automatically)
        """
        self.target_data_element = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_r_port_prototype(self, value: Optional[AbstractRequiredPort]) -> RVariableInAtomicSwcInstanceRef:
        """
        Set contextRPortPrototype and return self for chaining.

        Args:
            value: The contextRPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_r_port_prototype("value")
        """
        self.context_r_port_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_data_element(self, value: Optional[RefType]) -> RVariableInAtomicSwcInstanceRef:
        """
        Set targetDataElement and return self for chaining.

        Args:
            value: The targetDataElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_data_element("value")
        """
        self.target_data_element = value  # Use property setter (gets validation)
        return self



class RTriggerInAtomicSwcInstanceRef(TriggerInAtomicSwcInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::RTriggerInAtomicSwcInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 945, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tags: xml.
        # sequenceOffset=20.
        self._contextRPortPrototype: Optional[AbstractRequiredPort] = None

    @property
    def context_r_port_prototype(self) -> Optional[AbstractRequiredPort]:
        """Get contextRPortPrototype (Pythonic accessor)."""
        return self._contextRPortPrototype

    @context_r_port_prototype.setter
    def context_r_port_prototype(self, value: Optional[AbstractRequiredPort]) -> None:
        """
        Set contextRPortPrototype with validation.

        Args:
            value: The contextRPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextRPortPrototype = None
            return

        if not isinstance(value, AbstractRequiredPort):
            raise TypeError(
                f"contextRPortPrototype must be AbstractRequiredPort or None, got {type(value).__name__}"
            )
        self._contextRPortPrototype = value
        # sequenceOffset=30.
        self._targetTrigger: Optional[RefType] = None

    @property
    def target_trigger(self) -> Optional[RefType]:
        """Get targetTrigger (Pythonic accessor)."""
        return self._targetTrigger

    @target_trigger.setter
    def target_trigger(self, value: Optional[RefType]) -> None:
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

    def getContextRPortPrototype(self) -> AbstractRequiredPort:
        """
        AUTOSAR-compliant getter for contextRPortPrototype.

        Returns:
            The contextRPortPrototype value

        Note:
            Delegates to context_r_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_r_port_prototype  # Delegates to property

    def setContextRPortPrototype(self, value: AbstractRequiredPort) -> RTriggerInAtomicSwcInstanceRef:
        """
        AUTOSAR-compliant setter for contextRPortPrototype with method chaining.

        Args:
            value: The contextRPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_r_port_prototype property setter (gets validation automatically)
        """
        self.context_r_port_prototype = value  # Delegates to property setter
        return self

    def getTargetTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetTrigger.

        Returns:
            The targetTrigger value

        Note:
            Delegates to target_trigger property (CODING_RULE_V2_00017)
        """
        return self.target_trigger  # Delegates to property

    def setTargetTrigger(self, value: RefType) -> RTriggerInAtomicSwcInstanceRef:
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

    def with_context_r_port_prototype(self, value: Optional[AbstractRequiredPort]) -> RTriggerInAtomicSwcInstanceRef:
        """
        Set contextRPortPrototype and return self for chaining.

        Args:
            value: The contextRPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_r_port_prototype("value")
        """
        self.context_r_port_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_trigger(self, value: Optional[RefType]) -> RTriggerInAtomicSwcInstanceRef:
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



class PTriggerInAtomicSwcTypeInstanceRef(TriggerInAtomicSwcInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::PTriggerInAtomicSwcTypeInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 946, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tags: xml.
        # sequenceOffset=20.
        self._contextPPortPrototype: Optional[AbstractProvidedPort] = None

    @property
    def context_p_port_prototype(self) -> Optional[AbstractProvidedPort]:
        """Get contextPPortPrototype (Pythonic accessor)."""
        return self._contextPPortPrototype

    @context_p_port_prototype.setter
    def context_p_port_prototype(self, value: Optional[AbstractProvidedPort]) -> None:
        """
        Set contextPPortPrototype with validation.

        Args:
            value: The contextPPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextPPortPrototype = None
            return

        if not isinstance(value, AbstractProvidedPort):
            raise TypeError(
                f"contextPPortPrototype must be AbstractProvidedPort or None, got {type(value).__name__}"
            )
        self._contextPPortPrototype = value
        # sequenceOffset=30.
        self._targetTrigger: Optional[RefType] = None

    @property
    def target_trigger(self) -> Optional[RefType]:
        """Get targetTrigger (Pythonic accessor)."""
        return self._targetTrigger

    @target_trigger.setter
    def target_trigger(self, value: Optional[RefType]) -> None:
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

    def getContextPPortPrototype(self) -> AbstractProvidedPort:
        """
        AUTOSAR-compliant getter for contextPPortPrototype.

        Returns:
            The contextPPortPrototype value

        Note:
            Delegates to context_p_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_p_port_prototype  # Delegates to property

    def setContextPPortPrototype(self, value: AbstractProvidedPort) -> PTriggerInAtomicSwcTypeInstanceRef:
        """
        AUTOSAR-compliant setter for contextPPortPrototype with method chaining.

        Args:
            value: The contextPPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_p_port_prototype property setter (gets validation automatically)
        """
        self.context_p_port_prototype = value  # Delegates to property setter
        return self

    def getTargetTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetTrigger.

        Returns:
            The targetTrigger value

        Note:
            Delegates to target_trigger property (CODING_RULE_V2_00017)
        """
        return self.target_trigger  # Delegates to property

    def setTargetTrigger(self, value: RefType) -> PTriggerInAtomicSwcTypeInstanceRef:
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

    def with_context_p_port_prototype(self, value: Optional[AbstractProvidedPort]) -> PTriggerInAtomicSwcTypeInstanceRef:
        """
        Set contextPPortPrototype and return self for chaining.

        Args:
            value: The contextPPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_p_port_prototype("value")
        """
        self.context_p_port_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_trigger(self, value: Optional[RefType]) -> PTriggerInAtomicSwcTypeInstanceRef:
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



class ROperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::ROperationInAtomicSwcInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 947, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tags: xml.
        # sequenceOffset=20.
        self._contextRPortPrototype: Optional[AbstractRequiredPort] = None

    @property
    def context_r_port_prototype(self) -> Optional[AbstractRequiredPort]:
        """Get contextRPortPrototype (Pythonic accessor)."""
        return self._contextRPortPrototype

    @context_r_port_prototype.setter
    def context_r_port_prototype(self, value: Optional[AbstractRequiredPort]) -> None:
        """
        Set contextRPortPrototype with validation.

        Args:
            value: The contextRPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextRPortPrototype = None
            return

        if not isinstance(value, AbstractRequiredPort):
            raise TypeError(
                f"contextRPortPrototype must be AbstractRequiredPort or None, got {type(value).__name__}"
            )
        self._contextRPortPrototype = value
        # sequenceOffset=30.
        self._targetRequiredOperation: Optional[ClientServerOperation] = None

    @property
    def target_required_operation(self) -> Optional[ClientServerOperation]:
        """Get targetRequiredOperation (Pythonic accessor)."""
        return self._targetRequiredOperation

    @target_required_operation.setter
    def target_required_operation(self, value: Optional[ClientServerOperation]) -> None:
        """
        Set targetRequiredOperation with validation.

        Args:
            value: The targetRequiredOperation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetRequiredOperation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"targetRequiredOperation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._targetRequiredOperation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextRPortPrototype(self) -> AbstractRequiredPort:
        """
        AUTOSAR-compliant getter for contextRPortPrototype.

        Returns:
            The contextRPortPrototype value

        Note:
            Delegates to context_r_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_r_port_prototype  # Delegates to property

    def setContextRPortPrototype(self, value: AbstractRequiredPort) -> ROperationInAtomicSwcInstanceRef:
        """
        AUTOSAR-compliant setter for contextRPortPrototype with method chaining.

        Args:
            value: The contextRPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_r_port_prototype property setter (gets validation automatically)
        """
        self.context_r_port_prototype = value  # Delegates to property setter
        return self

    def getTargetRequiredOperation(self) -> ClientServerOperation:
        """
        AUTOSAR-compliant getter for targetRequiredOperation.

        Returns:
            The targetRequiredOperation value

        Note:
            Delegates to target_required_operation property (CODING_RULE_V2_00017)
        """
        return self.target_required_operation  # Delegates to property

    def setTargetRequiredOperation(self, value: ClientServerOperation) -> ROperationInAtomicSwcInstanceRef:
        """
        AUTOSAR-compliant setter for targetRequiredOperation with method chaining.

        Args:
            value: The targetRequiredOperation to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_required_operation property setter (gets validation automatically)
        """
        self.target_required_operation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_r_port_prototype(self, value: Optional[AbstractRequiredPort]) -> ROperationInAtomicSwcInstanceRef:
        """
        Set contextRPortPrototype and return self for chaining.

        Args:
            value: The contextRPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_r_port_prototype("value")
        """
        self.context_r_port_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_required_operation(self, value: Optional[ClientServerOperation]) -> ROperationInAtomicSwcInstanceRef:
        """
        Set targetRequiredOperation and return self for chaining.

        Args:
            value: The targetRequiredOperation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_required_operation("value")
        """
        self.target_required_operation = value  # Use property setter (gets validation)
        return self



class POperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::POperationInAtomicSwcInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 948, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tags: xml.
        # sequenceOffset=20.
        self._contextPPortPrototype: Optional[AbstractProvidedPort] = None

    @property
    def context_p_port_prototype(self) -> Optional[AbstractProvidedPort]:
        """Get contextPPortPrototype (Pythonic accessor)."""
        return self._contextPPortPrototype

    @context_p_port_prototype.setter
    def context_p_port_prototype(self, value: Optional[AbstractProvidedPort]) -> None:
        """
        Set contextPPortPrototype with validation.

        Args:
            value: The contextPPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextPPortPrototype = None
            return

        if not isinstance(value, AbstractProvidedPort):
            raise TypeError(
                f"contextPPortPrototype must be AbstractProvidedPort or None, got {type(value).__name__}"
            )
        self._contextPPortPrototype = value
        # sequenceOffset=30.
        self._targetProvidedOperation: Optional[ClientServerOperation] = None

    @property
    def target_provided_operation(self) -> Optional[ClientServerOperation]:
        """Get targetProvidedOperation (Pythonic accessor)."""
        return self._targetProvidedOperation

    @target_provided_operation.setter
    def target_provided_operation(self, value: Optional[ClientServerOperation]) -> None:
        """
        Set targetProvidedOperation with validation.

        Args:
            value: The targetProvidedOperation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetProvidedOperation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"targetProvidedOperation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._targetProvidedOperation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextPPortPrototype(self) -> AbstractProvidedPort:
        """
        AUTOSAR-compliant getter for contextPPortPrototype.

        Returns:
            The contextPPortPrototype value

        Note:
            Delegates to context_p_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_p_port_prototype  # Delegates to property

    def setContextPPortPrototype(self, value: AbstractProvidedPort) -> POperationInAtomicSwcInstanceRef:
        """
        AUTOSAR-compliant setter for contextPPortPrototype with method chaining.

        Args:
            value: The contextPPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_p_port_prototype property setter (gets validation automatically)
        """
        self.context_p_port_prototype = value  # Delegates to property setter
        return self

    def getTargetProvidedOperation(self) -> ClientServerOperation:
        """
        AUTOSAR-compliant getter for targetProvidedOperation.

        Returns:
            The targetProvidedOperation value

        Note:
            Delegates to target_provided_operation property (CODING_RULE_V2_00017)
        """
        return self.target_provided_operation  # Delegates to property

    def setTargetProvidedOperation(self, value: ClientServerOperation) -> POperationInAtomicSwcInstanceRef:
        """
        AUTOSAR-compliant setter for targetProvidedOperation with method chaining.

        Args:
            value: The targetProvidedOperation to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_provided_operation property setter (gets validation automatically)
        """
        self.target_provided_operation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_p_port_prototype(self, value: Optional[AbstractProvidedPort]) -> POperationInAtomicSwcInstanceRef:
        """
        Set contextPPortPrototype and return self for chaining.

        Args:
            value: The contextPPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_p_port_prototype("value")
        """
        self.context_p_port_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_provided_operation(self, value: Optional[ClientServerOperation]) -> POperationInAtomicSwcInstanceRef:
        """
        Set targetProvidedOperation and return self for chaining.

        Args:
            value: The targetProvidedOperation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_provided_operation("value")
        """
        self.target_provided_operation = value  # Use property setter (gets validation)
        return self



class RModeGroupInAtomicSWCInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::RModeGroupInAtomicSWCInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 948, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tags: xml.
        # sequenceOffset=20.
        self._contextRPortPrototype: Optional[AbstractRequiredPort] = None

    @property
    def context_r_port_prototype(self) -> Optional[AbstractRequiredPort]:
        """Get contextRPortPrototype (Pythonic accessor)."""
        return self._contextRPortPrototype

    @context_r_port_prototype.setter
    def context_r_port_prototype(self, value: Optional[AbstractRequiredPort]) -> None:
        """
        Set contextRPortPrototype with validation.

        Args:
            value: The contextRPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextRPortPrototype = None
            return

        if not isinstance(value, AbstractRequiredPort):
            raise TypeError(
                f"contextRPortPrototype must be AbstractRequiredPort or None, got {type(value).__name__}"
            )
        self._contextRPortPrototype = value
        # sequenceOffset=30.
        self._targetMode: Optional[RefType] = None

    @property
    def target_mode(self) -> Optional[RefType]:
        """Get targetMode (Pythonic accessor)."""
        return self._targetMode

    @target_mode.setter
    def target_mode(self, value: Optional[RefType]) -> None:
        """
        Set targetMode with validation.

        Args:
            value: The targetMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetMode = None
            return

        self._targetMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextRPortPrototype(self) -> AbstractRequiredPort:
        """
        AUTOSAR-compliant getter for contextRPortPrototype.

        Returns:
            The contextRPortPrototype value

        Note:
            Delegates to context_r_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_r_port_prototype  # Delegates to property

    def setContextRPortPrototype(self, value: AbstractRequiredPort) -> RModeGroupInAtomicSWCInstanceRef:
        """
        AUTOSAR-compliant setter for contextRPortPrototype with method chaining.

        Args:
            value: The contextRPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_r_port_prototype property setter (gets validation automatically)
        """
        self.context_r_port_prototype = value  # Delegates to property setter
        return self

    def getTargetMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetMode.

        Returns:
            The targetMode value

        Note:
            Delegates to target_mode property (CODING_RULE_V2_00017)
        """
        return self.target_mode  # Delegates to property

    def setTargetMode(self, value: RefType) -> RModeGroupInAtomicSWCInstanceRef:
        """
        AUTOSAR-compliant setter for targetMode with method chaining.

        Args:
            value: The targetMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_mode property setter (gets validation automatically)
        """
        self.target_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_r_port_prototype(self, value: Optional[AbstractRequiredPort]) -> RModeGroupInAtomicSWCInstanceRef:
        """
        Set contextRPortPrototype and return self for chaining.

        Args:
            value: The contextRPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_r_port_prototype("value")
        """
        self.context_r_port_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_mode(self, value: Optional[RefType]) -> RModeGroupInAtomicSWCInstanceRef:
        """
        Set targetMode and return self for chaining.

        Args:
            value: The targetMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_mode("value")
        """
        self.target_mode = value  # Use property setter (gets validation)
        return self



class PModeGroupInAtomicSwcInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::InstanceRefs::PModeGroupInAtomicSwcInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 949, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tags: xml.
        # sequenceOffset=20.
        self._contextPPortPrototype: Optional[AbstractProvidedPort] = None

    @property
    def context_p_port_prototype(self) -> Optional[AbstractProvidedPort]:
        """Get contextPPortPrototype (Pythonic accessor)."""
        return self._contextPPortPrototype

    @context_p_port_prototype.setter
    def context_p_port_prototype(self, value: Optional[AbstractProvidedPort]) -> None:
        """
        Set contextPPortPrototype with validation.

        Args:
            value: The contextPPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextPPortPrototype = None
            return

        if not isinstance(value, AbstractProvidedPort):
            raise TypeError(
                f"contextPPortPrototype must be AbstractProvidedPort or None, got {type(value).__name__}"
            )
        self._contextPPortPrototype = value
        # sequenceOffset=30.
        self._targetMode: Optional[RefType] = None

    @property
    def target_mode(self) -> Optional[RefType]:
        """Get targetMode (Pythonic accessor)."""
        return self._targetMode

    @target_mode.setter
    def target_mode(self, value: Optional[RefType]) -> None:
        """
        Set targetMode with validation.

        Args:
            value: The targetMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetMode = None
            return

        self._targetMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextPPortPrototype(self) -> AbstractProvidedPort:
        """
        AUTOSAR-compliant getter for contextPPortPrototype.

        Returns:
            The contextPPortPrototype value

        Note:
            Delegates to context_p_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_p_port_prototype  # Delegates to property

    def setContextPPortPrototype(self, value: AbstractProvidedPort) -> PModeGroupInAtomicSwcInstanceRef:
        """
        AUTOSAR-compliant setter for contextPPortPrototype with method chaining.

        Args:
            value: The contextPPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_p_port_prototype property setter (gets validation automatically)
        """
        self.context_p_port_prototype = value  # Delegates to property setter
        return self

    def getTargetMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetMode.

        Returns:
            The targetMode value

        Note:
            Delegates to target_mode property (CODING_RULE_V2_00017)
        """
        return self.target_mode  # Delegates to property

    def setTargetMode(self, value: RefType) -> PModeGroupInAtomicSwcInstanceRef:
        """
        AUTOSAR-compliant setter for targetMode with method chaining.

        Args:
            value: The targetMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_mode property setter (gets validation automatically)
        """
        self.target_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_p_port_prototype(self, value: Optional[AbstractProvidedPort]) -> PModeGroupInAtomicSwcInstanceRef:
        """
        Set contextPPortPrototype and return self for chaining.

        Args:
            value: The contextPPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_p_port_prototype("value")
        """
        self.context_p_port_prototype = value  # Use property setter (gets validation)
        return self

    def with_target_mode(self, value: Optional[RefType]) -> PModeGroupInAtomicSwcInstanceRef:
        """
        Set targetMode and return self for chaining.

        Args:
            value: The targetMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_mode("value")
        """
        self.target_mode = value  # Use property setter (gets validation)
        return self
