"""
AUTOSAR Package - ExecutionOrderConstraint

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.__init__ import (
    TimingConstraint,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"ignoreOrder must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._ignoreOrder = value
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isEvent must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isEvent = value
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"permitMultiple must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._permitMultiple = value

    def with_ordered_element(self, value):
        """
        Set ordered_element and return self for chaining.

        Args:
            value: The ordered_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ordered_element("value")
        """
        self.ordered_element = value  # Use property setter (gets validation)
        return self

    def with_direct_successor(self, value):
        """
        Set direct_successor and return self for chaining.

        Args:
            value: The direct_successor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direct_successor("value")
        """
        self.direct_successor = value  # Use property setter (gets validation)
        return self

    def with_let_interval(self, value):
        """
        Set let_interval and return self for chaining.

        Args:
            value: The let_interval to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_let_interval("value")
        """
        self.let_interval = value  # Use property setter (gets validation)
        return self

    def with_nested_element(self, value):
        """
        Set nested_element and return self for chaining.

        Args:
            value: The nested_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nested_element("value")
        """
        self.nested_element = value  # Use property setter (gets validation)
        return self

    def with_successor(self, value):
        """
        Set successor and return self for chaining.

        Args:
            value: The successor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_successor("value")
        """
        self.successor = value  # Use property setter (gets validation)
        return self

    def with_successor(self, value):
        """
        Set successor and return self for chaining.

        Args:
            value: The successor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_successor("value")
        """
        self.successor = value  # Use property setter (gets validation)
        return self

    def with_successor(self, value):
        """
        Set successor and return self for chaining.

        Args:
            value: The successor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_successor("value")
        """
        self.successor = value  # Use property setter (gets validation)
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



class EOCExecutableEntityRefAbstract(Identifiable, ABC):
    """
    This is the abstractions for Execution Order Constraint Executable Entity
    References (leaves) and Execution Order Constraint Executable Entity
    Reference Groups (composites).

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint::EOCExecutableEntityRefAbstract

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 119, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EOCExecutableEntityRefAbstract:
            raise TypeError("EOCExecutableEntityRefAbstract is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The direct successor of an executable entity or a group of entities.
        self._directSuccessor: List["EOCExecutableEntity"] = []

    @property
    def direct_successor(self) -> List["EOCExecutableEntity"]:
        """Get directSuccessor (Pythonic accessor)."""
        return self._directSuccessor

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDirectSuccessor(self) -> List["EOCExecutableEntity"]:
        """
        AUTOSAR-compliant getter for directSuccessor.

        Returns:
            The directSuccessor value

        Note:
            Delegates to direct_successor property (CODING_RULE_V2_00017)
        """
        return self.direct_successor  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EOCExecutableEntityRefGroup(EOCExecutableEntityRefAbstract):
    """
    This is used to specify a group (composite) consisting of Execution Order
    Constraint Executable Entity References (leaves) and/or further Execution
    Order Constraint Executable Entity Reference Groups (composite).

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint::EOCExecutableEntityRefGroup

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 119, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the data exchange paradigm between ExecutableEntitys within a LET
                # interval.
        # atp.
        # Status=draft.
        self._letData: Optional["LetDataExchange"] = None

    @property
    def let_data(self) -> Optional["LetDataExchange"]:
        """Get letData (Pythonic accessor)."""
        return self._letData

    @let_data.setter
    def let_data(self, value: Optional["LetDataExchange"]) -> None:
        """
        Set letData with validation.

        Args:
            value: The letData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._letData = None
            return

        if not isinstance(value, LetDataExchange):
            raise TypeError(
                f"letData must be LetDataExchange or None, got {type(value).__name__}"
            )
        self._letData = value
        # a LET interval the executable the group are assigned to.
        self._letInterval: List["TimingDescriptionEvent"] = []

    @property
    def let_interval(self) -> List["TimingDescriptionEvent"]:
        """Get letInterval (Pythonic accessor)."""
        return self._letInterval
        # Repetitive Execution Order Constraint only: number of repetitions (cycles) of
                # the event in the Order Constraint.
        # 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing Extensions for
                # Classic R23-11.
        self._maxCycle: Optional["PositiveInteger"] = None

    @property
    def max_cycle(self) -> Optional["PositiveInteger"]:
        """Get maxCycle (Pythonic accessor)."""
        return self._maxCycle

    @max_cycle.setter
    def max_cycle(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxCycle with validation.

        Args:
            value: The maxCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxCycle = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxCycle must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxCycle = value
        # the Execution is considering.
        self._maxCycles: Optional["Integer"] = None

    @property
    def max_cycles(self) -> Optional["Integer"]:
        """Get maxCycles (Pythonic accessor)."""
        return self._maxCycles

    @max_cycles.setter
    def max_cycles(self, value: Optional["Integer"]) -> None:
        """
        Set maxCycles with validation.

        Args:
            value: The maxCycles to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxCycles = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxCycles must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxCycles = value
        # every cycle of the Constraint is consisting of.
        self._maxSlots: Optional["Integer"] = None

    @property
    def max_slots(self) -> Optional["Integer"]:
        """Get maxSlots (Pythonic accessor)."""
        return self._maxSlots

    @max_slots.setter
    def max_slots(self, value: Optional["Integer"]) -> None:
        """
        Set maxSlots with validation.

        Args:
            value: The maxSlots to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSlots = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxSlots must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxSlots = value
        # (slots) that are a given order within a cycle, for the Repetitive Constraint.
        self._maxSlotsPer: Optional["PositiveInteger"] = None

    @property
    def max_slots_per(self) -> Optional["PositiveInteger"]:
        """Get maxSlotsPer (Pythonic accessor)."""
        return self._maxSlotsPer

    @max_slots_per.setter
    def max_slots_per(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxSlotsPer with validation.

        Args:
            value: The maxSlotsPer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSlotsPer = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxSlotsPer must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxSlotsPer = value
        # References.
        self._nestedElement: List["EOCExecutableEntity"] = []

    @property
    def nested_element(self) -> List["EOCExecutableEntity"]:
        """Get nestedElement (Pythonic accessor)."""
        return self._nestedElement
        # The logical successor of an executable entity or a group executable entities.
        self._successor: List["EOCExecutableEntity"] = []

    @property
    def successor(self) -> List["EOCExecutableEntity"]:
        """Get successor (Pythonic accessor)."""
        return self._successor
        # In case of a Repetitive Execution Order Constraint this the timing
        # description event cycle.
        self._triggeringEvent: Optional["TimingDescriptionEvent"] = None

    @property
    def triggering_event(self) -> Optional["TimingDescriptionEvent"]:
        """Get triggeringEvent (Pythonic accessor)."""
        return self._triggeringEvent

    @triggering_event.setter
    def triggering_event(self, value: Optional["TimingDescriptionEvent"]) -> None:
        """
        Set triggeringEvent with validation.

        Args:
            value: The triggeringEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._triggeringEvent = None
            return

        if not isinstance(value, TimingDescriptionEvent):
            raise TypeError(
                f"triggeringEvent must be TimingDescriptionEvent or None, got {type(value).__name__}"
            )
        self._triggeringEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLetData(self) -> "LetDataExchange":
        """
        AUTOSAR-compliant getter for letData.

        Returns:
            The letData value

        Note:
            Delegates to let_data property (CODING_RULE_V2_00017)
        """
        return self.let_data  # Delegates to property

    def setLetData(self, value: "LetDataExchange") -> "EOCExecutableEntityRefGroup":
        """
        AUTOSAR-compliant setter for letData with method chaining.

        Args:
            value: The letData to set

        Returns:
            self for method chaining

        Note:
            Delegates to let_data property setter (gets validation automatically)
        """
        self.let_data = value  # Delegates to property setter
        return self

    def getLetInterval(self) -> List["TimingDescriptionEvent"]:
        """
        AUTOSAR-compliant getter for letInterval.

        Returns:
            The letInterval value

        Note:
            Delegates to let_interval property (CODING_RULE_V2_00017)
        """
        return self.let_interval  # Delegates to property

    def getMaxCycle(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxCycle.

        Returns:
            The maxCycle value

        Note:
            Delegates to max_cycle property (CODING_RULE_V2_00017)
        """
        return self.max_cycle  # Delegates to property

    def setMaxCycle(self, value: "PositiveInteger") -> "EOCExecutableEntityRefGroup":
        """
        AUTOSAR-compliant setter for maxCycle with method chaining.

        Args:
            value: The maxCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_cycle property setter (gets validation automatically)
        """
        self.max_cycle = value  # Delegates to property setter
        return self

    def getMaxCycles(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxCycles.

        Returns:
            The maxCycles value

        Note:
            Delegates to max_cycles property (CODING_RULE_V2_00017)
        """
        return self.max_cycles  # Delegates to property

    def setMaxCycles(self, value: "Integer") -> "EOCExecutableEntityRefGroup":
        """
        AUTOSAR-compliant setter for maxCycles with method chaining.

        Args:
            value: The maxCycles to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_cycles property setter (gets validation automatically)
        """
        self.max_cycles = value  # Delegates to property setter
        return self

    def getMaxSlots(self) -> "Integer":
        """
        AUTOSAR-compliant getter for maxSlots.

        Returns:
            The maxSlots value

        Note:
            Delegates to max_slots property (CODING_RULE_V2_00017)
        """
        return self.max_slots  # Delegates to property

    def setMaxSlots(self, value: "Integer") -> "EOCExecutableEntityRefGroup":
        """
        AUTOSAR-compliant setter for maxSlots with method chaining.

        Args:
            value: The maxSlots to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_slots property setter (gets validation automatically)
        """
        self.max_slots = value  # Delegates to property setter
        return self

    def getMaxSlotsPer(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxSlotsPer.

        Returns:
            The maxSlotsPer value

        Note:
            Delegates to max_slots_per property (CODING_RULE_V2_00017)
        """
        return self.max_slots_per  # Delegates to property

    def setMaxSlotsPer(self, value: "PositiveInteger") -> "EOCExecutableEntityRefGroup":
        """
        AUTOSAR-compliant setter for maxSlotsPer with method chaining.

        Args:
            value: The maxSlotsPer to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_slots_per property setter (gets validation automatically)
        """
        self.max_slots_per = value  # Delegates to property setter
        return self

    def getNestedElement(self) -> List["EOCExecutableEntity"]:
        """
        AUTOSAR-compliant getter for nestedElement.

        Returns:
            The nestedElement value

        Note:
            Delegates to nested_element property (CODING_RULE_V2_00017)
        """
        return self.nested_element  # Delegates to property

    def getSuccessor(self) -> List["EOCExecutableEntity"]:
        """
        AUTOSAR-compliant getter for successor.

        Returns:
            The successor value

        Note:
            Delegates to successor property (CODING_RULE_V2_00017)
        """
        return self.successor  # Delegates to property

    def getTriggeringEvent(self) -> "TimingDescriptionEvent":
        """
        AUTOSAR-compliant getter for triggeringEvent.

        Returns:
            The triggeringEvent value

        Note:
            Delegates to triggering_event property (CODING_RULE_V2_00017)
        """
        return self.triggering_event  # Delegates to property

    def setTriggeringEvent(self, value: "TimingDescriptionEvent") -> "EOCExecutableEntityRefGroup":
        """
        AUTOSAR-compliant setter for triggeringEvent with method chaining.

        Args:
            value: The triggeringEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to triggering_event property setter (gets validation automatically)
        """
        self.triggering_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_let_data(self, value: Optional["LetDataExchange"]) -> "EOCExecutableEntityRefGroup":
        """
        Set letData and return self for chaining.

        Args:
            value: The letData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_let_data("value")
        """
        self.let_data = value  # Use property setter (gets validation)
        return self

    def with_max_cycle(self, value: Optional["PositiveInteger"]) -> "EOCExecutableEntityRefGroup":
        """
        Set maxCycle and return self for chaining.

        Args:
            value: The maxCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_cycle("value")
        """
        self.max_cycle = value  # Use property setter (gets validation)
        return self

    def with_max_cycles(self, value: Optional["Integer"]) -> "EOCExecutableEntityRefGroup":
        """
        Set maxCycles and return self for chaining.

        Args:
            value: The maxCycles to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_cycles("value")
        """
        self.max_cycles = value  # Use property setter (gets validation)
        return self

    def with_max_slots(self, value: Optional["Integer"]) -> "EOCExecutableEntityRefGroup":
        """
        Set maxSlots and return self for chaining.

        Args:
            value: The maxSlots to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_slots("value")
        """
        self.max_slots = value  # Use property setter (gets validation)
        return self

    def with_max_slots_per(self, value: Optional["PositiveInteger"]) -> "EOCExecutableEntityRefGroup":
        """
        Set maxSlotsPer and return self for chaining.

        Args:
            value: The maxSlotsPer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_slots_per("value")
        """
        self.max_slots_per = value  # Use property setter (gets validation)
        return self

    def with_triggering_event(self, value: Optional["TimingDescriptionEvent"]) -> "EOCExecutableEntityRefGroup":
        """
        Set triggeringEvent and return self for chaining.

        Args:
            value: The triggeringEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_triggering_event("value")
        """
        self.triggering_event = value  # Use property setter (gets validation)
        return self



class EOCExecutableEntityRef(EOCExecutableEntityRefAbstract):
    """
    This is used to define a reference to an ExecutableEntity If the
    ExecutionOrderConstraint is defined on VFB, System or ECU level, a reference
    to the Sw ComponentPrototype, via the ComponentInCompositionInstanceRef, the
    referenced ExecutableEntity belongs to, shall be provided as context
    information.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint::EOCExecutableEntityRef

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 120, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the BSW module instance the BSW module belongs to.
        self._bswModule: Optional["BswImplementation"] = None

    @property
    def bsw_module(self) -> Optional["BswImplementation"]:
        """Get bswModule (Pythonic accessor)."""
        return self._bswModule

    @bsw_module.setter
    def bsw_module(self, value: Optional["BswImplementation"]) -> None:
        """
        Set bswModule with validation.

        Args:
            value: The bswModule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswModule = None
            return

        if not isinstance(value, BswImplementation):
            raise TypeError(
                f"bswModule must be BswImplementation or None, got {type(value).__name__}"
            )
        self._bswModule = value
        # by: ComponentIn.
        self._componentCompositionInstanceRef: Optional["SwComponent"] = None

    @property
    def component_composition_instance_ref(self) -> Optional["SwComponent"]:
        """Get componentCompositionInstanceRef (Pythonic accessor)."""
        return self._componentCompositionInstanceRef

    @component_composition_instance_ref.setter
    def component_composition_instance_ref(self, value: Optional["SwComponent"]) -> None:
        """
        Set componentCompositionInstanceRef with validation.

        Args:
            value: The componentCompositionInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._componentCompositionInstanceRef = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"componentCompositionInstanceRef must be SwComponent or None, got {type(value).__name__}"
            )
        self._componentCompositionInstanceRef = value
        self._executable: Optional["ExecutableEntity"] = None

    @property
    def executable(self) -> Optional["ExecutableEntity"]:
        """Get executable (Pythonic accessor)."""
        return self._executable

    @executable.setter
    def executable(self, value: Optional["ExecutableEntity"]) -> None:
        """
        Set executable with validation.

        Args:
            value: The executable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._executable = None
            return

        if not isinstance(value, ExecutableEntity):
            raise TypeError(
                f"executable must be ExecutableEntity or None, got {type(value).__name__}"
            )
        self._executable = value
        self._successor: List["EOCExecutableEntity"] = []

    @property
    def successor(self) -> List["EOCExecutableEntity"]:
        """Get successor (Pythonic accessor)."""
        return self._successor

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswModule(self) -> "BswImplementation":
        """
        AUTOSAR-compliant getter for bswModule.

        Returns:
            The bswModule value

        Note:
            Delegates to bsw_module property (CODING_RULE_V2_00017)
        """
        return self.bsw_module  # Delegates to property

    def setBswModule(self, value: "BswImplementation") -> "EOCExecutableEntityRef":
        """
        AUTOSAR-compliant setter for bswModule with method chaining.

        Args:
            value: The bswModule to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_module property setter (gets validation automatically)
        """
        self.bsw_module = value  # Delegates to property setter
        return self

    def getComponentCompositionInstanceRef(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for componentCompositionInstanceRef.

        Returns:
            The componentCompositionInstanceRef value

        Note:
            Delegates to component_composition_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.component_composition_instance_ref  # Delegates to property

    def setComponentCompositionInstanceRef(self, value: "SwComponent") -> "EOCExecutableEntityRef":
        """
        AUTOSAR-compliant setter for componentCompositionInstanceRef with method chaining.

        Args:
            value: The componentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to component_composition_instance_ref property setter (gets validation automatically)
        """
        self.component_composition_instance_ref = value  # Delegates to property setter
        return self

    def getExecutable(self) -> "ExecutableEntity":
        """
        AUTOSAR-compliant getter for executable.

        Returns:
            The executable value

        Note:
            Delegates to executable property (CODING_RULE_V2_00017)
        """
        return self.executable  # Delegates to property

    def setExecutable(self, value: "ExecutableEntity") -> "EOCExecutableEntityRef":
        """
        AUTOSAR-compliant setter for executable with method chaining.

        Args:
            value: The executable to set

        Returns:
            self for method chaining

        Note:
            Delegates to executable property setter (gets validation automatically)
        """
        self.executable = value  # Delegates to property setter
        return self

    def getSuccessor(self) -> List["EOCExecutableEntity"]:
        """
        AUTOSAR-compliant getter for successor.

        Returns:
            The successor value

        Note:
            Delegates to successor property (CODING_RULE_V2_00017)
        """
        return self.successor  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_module(self, value: Optional["BswImplementation"]) -> "EOCExecutableEntityRef":
        """
        Set bswModule and return self for chaining.

        Args:
            value: The bswModule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_module("value")
        """
        self.bsw_module = value  # Use property setter (gets validation)
        return self

    def with_component_composition_instance_ref(self, value: Optional["SwComponent"]) -> "EOCExecutableEntityRef":
        """
        Set componentCompositionInstanceRef and return self for chaining.

        Args:
            value: The componentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_component_composition_instance_ref("value")
        """
        self.component_composition_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_executable(self, value: Optional["ExecutableEntity"]) -> "EOCExecutableEntityRef":
        """
        Set executable and return self for chaining.

        Args:
            value: The executable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_executable("value")
        """
        self.executable = value  # Use property setter (gets validation)
        return self



class EOCEventRef(EOCExecutableEntityRefAbstract):
    """
    This is used to define a reference to an RTE or BSW Event.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint::EOCEventRef

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 120, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the BSW module instance the BSW event is to.
        self._bswModule: Optional["BswImplementation"] = None

    @property
    def bsw_module(self) -> Optional["BswImplementation"]:
        """Get bswModule (Pythonic accessor)."""
        return self._bswModule

    @bsw_module.setter
    def bsw_module(self, value: Optional["BswImplementation"]) -> None:
        """
        Set bswModule with validation.

        Args:
            value: The bswModule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswModule = None
            return

        if not isinstance(value, BswImplementation):
            raise TypeError(
                f"bswModule must be BswImplementation or None, got {type(value).__name__}"
            )
        self._bswModule = value
        # by: ComponentIn.
        self._componentCompositionInstanceRef: Optional["SwComponent"] = None

    @property
    def component_composition_instance_ref(self) -> Optional["SwComponent"]:
        """Get componentCompositionInstanceRef (Pythonic accessor)."""
        return self._componentCompositionInstanceRef

    @component_composition_instance_ref.setter
    def component_composition_instance_ref(self, value: Optional["SwComponent"]) -> None:
        """
        Set componentCompositionInstanceRef with validation.

        Args:
            value: The componentCompositionInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._componentCompositionInstanceRef = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"componentCompositionInstanceRef must be SwComponent or None, got {type(value).__name__}"
            )
        self._componentCompositionInstanceRef = value
        self._event: Optional["AbstractEvent"] = None

    @property
    def event(self) -> Optional["AbstractEvent"]:
        """Get event (Pythonic accessor)."""
        return self._event

    @event.setter
    def event(self, value: Optional["AbstractEvent"]) -> None:
        """
        Set event with validation.

        Args:
            value: The event to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._event = None
            return

        if not isinstance(value, AbstractEvent):
            raise TypeError(
                f"event must be AbstractEvent or None, got {type(value).__name__}"
            )
        self._event = value
        self._successor: List["EOCExecutableEntity"] = []

    @property
    def successor(self) -> List["EOCExecutableEntity"]:
        """Get successor (Pythonic accessor)."""
        return self._successor

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswModule(self) -> "BswImplementation":
        """
        AUTOSAR-compliant getter for bswModule.

        Returns:
            The bswModule value

        Note:
            Delegates to bsw_module property (CODING_RULE_V2_00017)
        """
        return self.bsw_module  # Delegates to property

    def setBswModule(self, value: "BswImplementation") -> "EOCEventRef":
        """
        AUTOSAR-compliant setter for bswModule with method chaining.

        Args:
            value: The bswModule to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_module property setter (gets validation automatically)
        """
        self.bsw_module = value  # Delegates to property setter
        return self

    def getComponentCompositionInstanceRef(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for componentCompositionInstanceRef.

        Returns:
            The componentCompositionInstanceRef value

        Note:
            Delegates to component_composition_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.component_composition_instance_ref  # Delegates to property

    def setComponentCompositionInstanceRef(self, value: "SwComponent") -> "EOCEventRef":
        """
        AUTOSAR-compliant setter for componentCompositionInstanceRef with method chaining.

        Args:
            value: The componentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to component_composition_instance_ref property setter (gets validation automatically)
        """
        self.component_composition_instance_ref = value  # Delegates to property setter
        return self

    def getEvent(self) -> "AbstractEvent":
        """
        AUTOSAR-compliant getter for event.

        Returns:
            The event value

        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def setEvent(self, value: "AbstractEvent") -> "EOCEventRef":
        """
        AUTOSAR-compliant setter for event with method chaining.

        Args:
            value: The event to set

        Returns:
            self for method chaining

        Note:
            Delegates to event property setter (gets validation automatically)
        """
        self.event = value  # Delegates to property setter
        return self

    def getSuccessor(self) -> List["EOCExecutableEntity"]:
        """
        AUTOSAR-compliant getter for successor.

        Returns:
            The successor value

        Note:
            Delegates to successor property (CODING_RULE_V2_00017)
        """
        return self.successor  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_module(self, value: Optional["BswImplementation"]) -> "EOCEventRef":
        """
        Set bswModule and return self for chaining.

        Args:
            value: The bswModule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_module("value")
        """
        self.bsw_module = value  # Use property setter (gets validation)
        return self

    def with_component_composition_instance_ref(self, value: Optional["SwComponent"]) -> "EOCEventRef":
        """
        Set componentCompositionInstanceRef and return self for chaining.

        Args:
            value: The componentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_component_composition_instance_ref("value")
        """
        self.component_composition_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_event(self, value: Optional["AbstractEvent"]) -> "EOCEventRef":
        """
        Set event and return self for chaining.

        Args:
            value: The event to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event("value")
        """
        self.event = value  # Use property setter (gets validation)
        return self


class ExecutionOrderConstraintTypeEnum(AREnum):
    """
    ExecutionOrderConstraintTypeEnum enumeration

Specifies the type of the executionOrderConstraintType for a ExecutionOrderConstraint. Aggregated by ExecutionOrderConstraint.executionOrderConstraintType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint
    """
    # Specifies that the Execution Order Constraint specifies a hierarchical execution order constraint.
    hierarchicalEOC = "0"

    # Specifies that the Execution Order Constraint specifies an ordinary execution order constraint.
    ordinaryEOC = "1"

    # Specifies that the Execution Order Constraint specifies a repetitive execution order constraint.
    repetitiveEOC = "2"



class LetDataExchangeParadigmEnum(AREnum):
    """
    LetDataExchangeParadigmEnum enumeration

Specifies the data exchange paradigm between ExecutableEntitys within a LET interval. Tags: atp.Status=draft Aggregated by EOCExecutableEntityRefGroup.letDataExchangeParadigm

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::ExecutionOrderConstraint
    """
    # All ExecutableEntitys mapped to this LET interval exchange data ONLY at the release and terminate event of the LET interval. This allows for a straightforward translation of the required label buffering but results in longer
    interLetOnly = "0"

    # The ExecutableEntitys that belong to the same EOCExecutableEntityRefGroup and are mapped to this LET interval are executed in the order defined by the EOCExecutableEntityRefGroup and exchange data directly within this LET interval according to implicit semantics. Only at the borders of the LET interval or between independent
    intraLetEOC = "1"
