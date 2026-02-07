from typing import List, Optional


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
        # prototype.
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
        # The AbstractEvent (event) whose execution order is the contraint.
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
        # The logical successor of an executable entity or a group executable entities.
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
