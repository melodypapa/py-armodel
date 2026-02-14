"""
AUTOSAR Package - InstanceRefs

Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstanceRefs
"""


from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ComponentInCompositionInstanceRef(ARObject):
    """
    The ComponentInCompositionInstanceRef points to a concrete
    SwComponentPrototype within a CompositionSwComponentType.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstanceRefs::ComponentInCompositionInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 950, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 219, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived xml.
        # sequenceOffset=10.
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
        # Tags: xml.
        # sequenceOffset=20 (ordered).
        self._context: List["SwComponent"] = []

    @property
    def context(self) -> List["SwComponent"]:
        """Get context (Pythonic accessor)."""
        return self._context
        # Tags: xml.
        # sequenceOffset=30.
        self._target: Optional["SwComponent"] = None

    @property
    def target(self) -> Optional["SwComponent"]:
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: Optional["SwComponent"]) -> None:
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

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"target must be SwComponent or None, got {type(value).__name__}"
            )
        self._target = value

    def with_context_prototype(self, value):
        """
        Set context_prototype and return self for chaining.

        Args:
            value: The context_prototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_prototype("value")
        """
        self.context_prototype = value  # Use property setter (gets validation)
        return self

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

    def setBase(self, value: "CompositionSw") -> ComponentInCompositionInstanceRef:
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

    def getContext(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def getTarget(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for target.

        Returns:
            The target value

        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: "SwComponent") -> ComponentInCompositionInstanceRef:
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

    def with_base(self, value: Optional["CompositionSw"]) -> ComponentInCompositionInstanceRef:
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

    def with_target(self, value: Optional["SwComponent"]) -> ComponentInCompositionInstanceRef:
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



class PortInCompositionTypeInstanceRef(ARObject, ABC):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstanceRefs::PortInCompositionTypeInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 950, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is PortInCompositionTypeInstanceRef:
            raise TypeError("PortInCompositionTypeInstanceRef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpAbstract Tags: xml.
        # sequenceOffset=20.
        self._abstractContext: Optional["SwComponent"] = None

    @property
    def abstract_context(self) -> Optional["SwComponent"]:
        """Get abstractContext (Pythonic accessor)."""
        return self._abstractContext

    @abstract_context.setter
    def abstract_context(self, value: Optional["SwComponent"]) -> None:
        """
        Set abstractContext with validation.

        Args:
            value: The abstractContext to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._abstractContext = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"abstractContext must be SwComponent or None, got {type(value).__name__}"
            )
        self._abstractContext = value
        # sequenceOffset=10.
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
        self._targetPort: Optional[RefType] = None

    @property
    def target_port(self) -> Optional[RefType]:
        """Get targetPort (Pythonic accessor)."""
        return self._targetPort

    @target_port.setter
    def target_port(self, value: Optional[RefType]) -> None:
        """
        Set targetPort with validation.

        Args:
            value: The targetPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetPort = None
            return

        self._targetPort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAbstractContext(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for abstractContext.

        Returns:
            The abstractContext value

        Note:
            Delegates to abstract_context property (CODING_RULE_V2_00017)
        """
        return self.abstract_context  # Delegates to property

    def setAbstractContext(self, value: "SwComponent") -> PortInCompositionTypeInstanceRef:
        """
        AUTOSAR-compliant setter for abstractContext with method chaining.

        Args:
            value: The abstractContext to set

        Returns:
            self for method chaining

        Note:
            Delegates to abstract_context property setter (gets validation automatically)
        """
        self.abstract_context = value  # Delegates to property setter
        return self

    def getBase(self) -> "CompositionSw":
        """
        AUTOSAR-compliant getter for base.

        Returns:
            The base value

        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "CompositionSw") -> PortInCompositionTypeInstanceRef:
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

    def getTargetPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetPort.

        Returns:
            The targetPort value

        Note:
            Delegates to target_port property (CODING_RULE_V2_00017)
        """
        return self.target_port  # Delegates to property

    def setTargetPort(self, value: RefType) -> PortInCompositionTypeInstanceRef:
        """
        AUTOSAR-compliant setter for targetPort with method chaining.

        Args:
            value: The targetPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_port property setter (gets validation automatically)
        """
        self.target_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_abstract_context(self, value: Optional["SwComponent"]) -> PortInCompositionTypeInstanceRef:
        """
        Set abstractContext and return self for chaining.

        Args:
            value: The abstractContext to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_abstract_context("value")
        """
        self.abstract_context = value  # Use property setter (gets validation)
        return self

    def with_base(self, value: Optional["CompositionSw"]) -> PortInCompositionTypeInstanceRef:
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

    def with_target_port(self, value: Optional[RefType]) -> PortInCompositionTypeInstanceRef:
        """
        Set targetPort and return self for chaining.

        Args:
            value: The targetPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_port("value")
        """
        self.target_port = value  # Use property setter (gets validation)
        return self



class InstanceEventInCompositionInstanceRef(ARObject):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstanceRefs::InstanceEventInCompositionInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 959, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Stereotypes: atpDerived xml.
        # sequenceOffset=10.
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
        # sequenceOffset=20.
        self._contextPrototype: List["SwComponent"] = []

    @property
    def context_prototype(self) -> List["SwComponent"]:
        """Get contextPrototype (Pythonic accessor)."""
        return self._contextPrototype
        # Tags: xml.
        # sequenceOffset=30.
        self._targetEvent: Optional["RTEEvent"] = None

    @property
    def target_event(self) -> Optional["RTEEvent"]:
        """Get targetEvent (Pythonic accessor)."""
        return self._targetEvent

    @target_event.setter
    def target_event(self, value: Optional["RTEEvent"]) -> None:
        """
        Set targetEvent with validation.

        Args:
            value: The targetEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetEvent = None
            return

        if not isinstance(value, RTEEvent):
            raise TypeError(
                f"targetEvent must be RTEEvent or None, got {type(value).__name__}"
            )
        self._targetEvent = value

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

    def setBase(self, value: "CompositionSw") -> InstanceEventInCompositionInstanceRef:
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

    def getContextPrototype(self) -> List["SwComponent"]:
        """
        AUTOSAR-compliant getter for contextPrototype.

        Returns:
            The contextPrototype value

        Note:
            Delegates to context_prototype property (CODING_RULE_V2_00017)
        """
        return self.context_prototype  # Delegates to property

    def getTargetEvent(self) -> "RTEEvent":
        """
        AUTOSAR-compliant getter for targetEvent.

        Returns:
            The targetEvent value

        Note:
            Delegates to target_event property (CODING_RULE_V2_00017)
        """
        return self.target_event  # Delegates to property

    def setTargetEvent(self, value: "RTEEvent") -> InstanceEventInCompositionInstanceRef:
        """
        AUTOSAR-compliant setter for targetEvent with method chaining.

        Args:
            value: The targetEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_event property setter (gets validation automatically)
        """
        self.target_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["CompositionSw"]) -> InstanceEventInCompositionInstanceRef:
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

    def with_target_event(self, value: Optional["RTEEvent"]) -> InstanceEventInCompositionInstanceRef:
        """
        Set targetEvent and return self for chaining.

        Args:
            value: The targetEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_event("value")
        """
        self.target_event = value  # Use property setter (gets validation)
        return self



class PPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstanceRefs::PPortInCompositionInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 951, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tags: xml.
        # sequenceOffset=20.
        self._context: Optional["SwComponent"] = None

    @property
    def context(self) -> Optional["SwComponent"]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional["SwComponent"]) -> None:
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

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"context must be SwComponent or None, got {type(value).__name__}"
            )
        self._context = value
        # sequenceOffset=30.
        self._targetPPortPrototype: Optional["AbstractProvidedPort"] = None

    @property
    def target_p_port_prototype(self) -> Optional["AbstractProvidedPort"]:
        """Get targetPPortPrototype (Pythonic accessor)."""
        return self._targetPPortPrototype

    @target_p_port_prototype.setter
    def target_p_port_prototype(self, value: Optional["AbstractProvidedPort"]) -> None:
        """
        Set targetPPortPrototype with validation.

        Args:
            value: The targetPPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetPPortPrototype = None
            return

        if not isinstance(value, AbstractProvidedPort):
            raise TypeError(
                f"targetPPortPrototype must be AbstractProvidedPort or None, got {type(value).__name__}"
            )
        self._targetPPortPrototype = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContext(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: "SwComponent") -> PPortInCompositionInstanceRef:
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

    def getTargetPPortPrototype(self) -> "AbstractProvidedPort":
        """
        AUTOSAR-compliant getter for targetPPortPrototype.

        Returns:
            The targetPPortPrototype value

        Note:
            Delegates to target_p_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.target_p_port_prototype  # Delegates to property

    def setTargetPPortPrototype(self, value: "AbstractProvidedPort") -> PPortInCompositionInstanceRef:
        """
        AUTOSAR-compliant setter for targetPPortPrototype with method chaining.

        Args:
            value: The targetPPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_p_port_prototype property setter (gets validation automatically)
        """
        self.target_p_port_prototype = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context(self, value: Optional["SwComponent"]) -> PPortInCompositionInstanceRef:
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

    def with_target_p_port_prototype(self, value: Optional["AbstractProvidedPort"]) -> PPortInCompositionInstanceRef:
        """
        Set targetPPortPrototype and return self for chaining.

        Args:
            value: The targetPPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_p_port_prototype("value")
        """
        self.target_p_port_prototype = value  # Use property setter (gets validation)
        return self



class RPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstanceRefs::RPortInCompositionInstanceRef

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 952, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 459, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Tags: xml.
        # sequenceOffset=20.
        self._context: Optional["SwComponent"] = None

    @property
    def context(self) -> Optional["SwComponent"]:
        """Get context (Pythonic accessor)."""
        return self._context

    @context.setter
    def context(self, value: Optional["SwComponent"]) -> None:
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

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"context must be SwComponent or None, got {type(value).__name__}"
            )
        self._context = value
        # sequenceOffset=30.
        self._targetRPortPrototype: Optional["AbstractRequiredPort"] = None

    @property
    def target_r_port_prototype(self) -> Optional["AbstractRequiredPort"]:
        """Get targetRPortPrototype (Pythonic accessor)."""
        return self._targetRPortPrototype

    @target_r_port_prototype.setter
    def target_r_port_prototype(self, value: Optional["AbstractRequiredPort"]) -> None:
        """
        Set targetRPortPrototype with validation.

        Args:
            value: The targetRPortPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetRPortPrototype = None
            return

        if not isinstance(value, AbstractRequiredPort):
            raise TypeError(
                f"targetRPortPrototype must be AbstractRequiredPort or None, got {type(value).__name__}"
            )
        self._targetRPortPrototype = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContext(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for context.

        Returns:
            The context value

        Note:
            Delegates to context property (CODING_RULE_V2_00017)
        """
        return self.context  # Delegates to property

    def setContext(self, value: "SwComponent") -> RPortInCompositionInstanceRef:
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

    def getTargetRPortPrototype(self) -> "AbstractRequiredPort":
        """
        AUTOSAR-compliant getter for targetRPortPrototype.

        Returns:
            The targetRPortPrototype value

        Note:
            Delegates to target_r_port_prototype property (CODING_RULE_V2_00017)
        """
        return self.target_r_port_prototype  # Delegates to property

    def setTargetRPortPrototype(self, value: "AbstractRequiredPort") -> RPortInCompositionInstanceRef:
        """
        AUTOSAR-compliant setter for targetRPortPrototype with method chaining.

        Args:
            value: The targetRPortPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_r_port_prototype property setter (gets validation automatically)
        """
        self.target_r_port_prototype = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context(self, value: Optional["SwComponent"]) -> RPortInCompositionInstanceRef:
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

    def with_target_r_port_prototype(self, value: Optional["AbstractRequiredPort"]) -> RPortInCompositionInstanceRef:
        """
        Set targetRPortPrototype and return self for chaining.

        Args:
            value: The targetRPortPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_r_port_prototype("value")
        """
        self.target_r_port_prototype = value  # Use property setter (gets validation)
        return self
