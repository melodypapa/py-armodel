from typing import List, Optional


class ExecutionOrderConstraint(TimingConstraint):
    """
    This constraint is used to restrict the order of execution for a set of
    ExecutableEntitys. The ExecutionOrderConstraint can be used in any timing
    view. The various scopes for ExecutionOrderConstraint are described below.
    Generally, each ExecutionOrder Constraint has a scope of software components
    and can reference all ExecutableEntitys available in the corresponding
    internal behavior (RunnableEntity and BswModuleEntity) either directly or by
    the events activating respectively starting them (RteEvent and BswEvent). On
    VFB level an ExecutionOrderConstraint can be specified for RunnableEntities
    part of the composition hierarchy referenced by the VfbTiming. On SW-C level
    an ExecutionOrderConstraint can be specified for RunnableEntities part of
    the Internal Behavior referenced by the SwcTiming. On System level an
    ExecutionOrderConstraint can be specified for RunnableEntities part of the
    composition hierarchy of the system referenced by the SystemTiming. On BSW
    Module level, an ExectionOrderConstraint can be specified for
    BswModuleEntities part of an BswInternalBehavior referenced by the
    BswModuleTiming. On ECU level an ExecutionOrderConstraint can be specified
    for all ExecutableEntitys and Events available via the EcucValueCollection,
    covering ECU Extract and BSW Module Configuration, referenced by the
    EcuTiming.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint::ExecutionOrderConstraint

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 118, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the composition SW-C type playing the role of a SW-C containing
        # further SW-Cs and represents the the Execution Order Constraint.
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
        # Specifies the specific type of ExecutionOrderConstraint.
        self._executionOrder: Optional["ExecutionOrder"] = None

    @property
    def execution_order(self) -> Optional["ExecutionOrder"]:
        """Get executionOrder (Pythonic accessor)."""
        return self._executionOrder

    @execution_order.setter
    def execution_order(self, value: Optional["ExecutionOrder"]) -> None:
        """
        Set executionOrder with validation.

        Args:
            value: The executionOrder to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._executionOrder = None
            return

        if not isinstance(value, ExecutionOrder):
            raise TypeError(
                f"executionOrder must be ExecutionOrder or None, got {type(value).__name__}"
            )
        self._executionOrder = value
        # Controls whether the order of execution specified by this can be
        # intentionally ignored (TRUE), or shall be.
        self._ignoreOrder: Optional["Boolean"] = None

    @property
    def ignore_order(self) -> Optional["Boolean"]:
        """Get ignoreOrder (Pythonic accessor)."""
        return self._ignoreOrder

    @ignore_order.setter
    def ignore_order(self, value: Optional["Boolean"]) -> None:
        """
        Set ignoreOrder with validation.

        Args:
            value: The ignoreOrder to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ignoreOrder = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"ignoreOrder must be Boolean or None, got {type(value).__name__}"
            )
        self._ignoreOrder = value
        # Indicates whether the ExecutionOrderConstraint is only Executable Entities
        # (FALSE) or only to RTE Events (TRUE).
        self._isEvent: Optional["Boolean"] = None

    @property
    def is_event(self) -> Optional["Boolean"]:
        """Get isEvent (Pythonic accessor)."""
        return self._isEvent

    @is_event.setter
    def is_event(self, value: Optional["Boolean"]) -> None:
        """
        Set isEvent with validation.

        Args:
            value: The isEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isEvent = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"isEvent must be Boolean or None, got {type(value).__name__}"
            )
        self._isEvent = value
        # This aggregation represents an unordered collection of to RunnableEntities
                # which shall be considered ExecutionOrderConstraint.
        # The role does not imply collection of references itself shall be ordered.
        self._orderedElement: List["EOCExecutableEntity"] = []

    @property
    def ordered_element(self) -> List["EOCExecutableEntity"]:
        """Get orderedElement (Pythonic accessor)."""
        return self._orderedElement
        # Indicates that the ExecutionOrderConstraints permits that Executable Entity
        # is referenced multiple times (TRUE) only once (FALSE) in the constraint.
        self._permitMultiple: Optional["Boolean"] = None

    @property
    def permit_multiple(self) -> Optional["Boolean"]:
        """Get permitMultiple (Pythonic accessor)."""
        return self._permitMultiple

    @permit_multiple.setter
    def permit_multiple(self, value: Optional["Boolean"]) -> None:
        """
        Set permitMultiple with validation.

        Args:
            value: The permitMultiple to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._permitMultiple = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"permitMultiple must be Boolean or None, got {type(value).__name__}"
            )
        self._permitMultiple = value

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

    def setBase(self, value: "CompositionSw") -> "ExecutionOrderConstraint":
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

    def getExecutionOrder(self) -> "ExecutionOrder":
        """
        AUTOSAR-compliant getter for executionOrder.

        Returns:
            The executionOrder value

        Note:
            Delegates to execution_order property (CODING_RULE_V2_00017)
        """
        return self.execution_order  # Delegates to property

    def setExecutionOrder(self, value: "ExecutionOrder") -> "ExecutionOrderConstraint":
        """
        AUTOSAR-compliant setter for executionOrder with method chaining.

        Args:
            value: The executionOrder to set

        Returns:
            self for method chaining

        Note:
            Delegates to execution_order property setter (gets validation automatically)
        """
        self.execution_order = value  # Delegates to property setter
        return self

    def getIgnoreOrder(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for ignoreOrder.

        Returns:
            The ignoreOrder value

        Note:
            Delegates to ignore_order property (CODING_RULE_V2_00017)
        """
        return self.ignore_order  # Delegates to property

    def setIgnoreOrder(self, value: "Boolean") -> "ExecutionOrderConstraint":
        """
        AUTOSAR-compliant setter for ignoreOrder with method chaining.

        Args:
            value: The ignoreOrder to set

        Returns:
            self for method chaining

        Note:
            Delegates to ignore_order property setter (gets validation automatically)
        """
        self.ignore_order = value  # Delegates to property setter
        return self

    def getIsEvent(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isEvent.

        Returns:
            The isEvent value

        Note:
            Delegates to is_event property (CODING_RULE_V2_00017)
        """
        return self.is_event  # Delegates to property

    def setIsEvent(self, value: "Boolean") -> "ExecutionOrderConstraint":
        """
        AUTOSAR-compliant setter for isEvent with method chaining.

        Args:
            value: The isEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_event property setter (gets validation automatically)
        """
        self.is_event = value  # Delegates to property setter
        return self

    def getOrderedElement(self) -> List["EOCExecutableEntity"]:
        """
        AUTOSAR-compliant getter for orderedElement.

        Returns:
            The orderedElement value

        Note:
            Delegates to ordered_element property (CODING_RULE_V2_00017)
        """
        return self.ordered_element  # Delegates to property

    def getPermitMultiple(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for permitMultiple.

        Returns:
            The permitMultiple value

        Note:
            Delegates to permit_multiple property (CODING_RULE_V2_00017)
        """
        return self.permit_multiple  # Delegates to property

    def setPermitMultiple(self, value: "Boolean") -> "ExecutionOrderConstraint":
        """
        AUTOSAR-compliant setter for permitMultiple with method chaining.

        Args:
            value: The permitMultiple to set

        Returns:
            self for method chaining

        Note:
            Delegates to permit_multiple property setter (gets validation automatically)
        """
        self.permit_multiple = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: Optional["CompositionSw"]) -> "ExecutionOrderConstraint":
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

    def with_execution_order(self, value: Optional["ExecutionOrder"]) -> "ExecutionOrderConstraint":
        """
        Set executionOrder and return self for chaining.

        Args:
            value: The executionOrder to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_execution_order("value")
        """
        self.execution_order = value  # Use property setter (gets validation)
        return self

    def with_ignore_order(self, value: Optional["Boolean"]) -> "ExecutionOrderConstraint":
        """
        Set ignoreOrder and return self for chaining.

        Args:
            value: The ignoreOrder to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ignore_order("value")
        """
        self.ignore_order = value  # Use property setter (gets validation)
        return self

    def with_is_event(self, value: Optional["Boolean"]) -> "ExecutionOrderConstraint":
        """
        Set isEvent and return self for chaining.

        Args:
            value: The isEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_event("value")
        """
        self.is_event = value  # Use property setter (gets validation)
        return self

    def with_permit_multiple(self, value: Optional["Boolean"]) -> "ExecutionOrderConstraint":
        """
        Set permitMultiple and return self for chaining.

        Args:
            value: The permitMultiple to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_permit_multiple("value")
        """
        self.permit_multiple = value  # Use property setter (gets validation)
        return self
