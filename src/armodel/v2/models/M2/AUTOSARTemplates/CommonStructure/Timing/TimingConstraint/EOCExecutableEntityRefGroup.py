from typing import List, Optional


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
        # This association references the TimingDescriptionEvent that plays the role of
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxCycle must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxCycle = value
        # In case of a Repetitive Execution Order Constraint this the number of cycles
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

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxCycles must be Integer or None, got {type(value).__name__}"
            )
        self._maxCycles = value
        # In case of a Repetitive Execution Order Constraint this the number of slots
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

        if not isinstance(value, Integer):
            raise TypeError(
                f"maxSlots must be Integer or None, got {type(value).__name__}"
            )
        self._maxSlots = value
        # Repetitive Execution Order Constraint only: number of ExecutableEntitys
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxSlotsPer must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxSlotsPer = value
        # This association is used to establish hierarchies of EOCEER Groups and
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
