from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class InstanceEventInCompositionInstanceRef(ARObject):
    """

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Composition::InstanceRefs

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

    def setBase(self, value: "CompositionSw") -> "InstanceEventInCompositionInstanceRef":
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

    def setTargetEvent(self, value: "RTEEvent") -> "InstanceEventInCompositionInstanceRef":
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

    def with_base(self, value: Optional["CompositionSw"]) -> "InstanceEventInCompositionInstanceRef":
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

    def with_target_event(self, value: Optional["RTEEvent"]) -> "InstanceEventInCompositionInstanceRef":
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
