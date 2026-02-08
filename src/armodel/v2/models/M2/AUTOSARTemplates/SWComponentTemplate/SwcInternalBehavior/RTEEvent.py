from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    AbstractEvent,
)


class RTEEvent(AbstractEvent, ABC):
    """
    Abstract base class for all RTE-related events

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 327, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 541, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 208, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 238, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is RTEEvent:
            raise TypeError("RTEEvent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # disabled by: RModeInAtomicSwc.
        self._disabledModeInstanceRef: List["ModeDeclaration"] = []

    @property
    def disabled_mode_instance_ref(self) -> List["ModeDeclaration"]:
        """Get disabledModeInstanceRef (Pythonic accessor)."""
        return self._disabledModeInstanceRef
        # The referenced RunnableEntity starts when the is raised.
        self._startOnEvent: Optional["RunnableEntity"] = None

    @property
    def start_on_event(self) -> Optional["RunnableEntity"]:
        """Get startOnEvent (Pythonic accessor)."""
        return self._startOnEvent

    @start_on_event.setter
    def start_on_event(self, value: Optional["RunnableEntity"]) -> None:
        """
        Set startOnEvent with validation.

        Args:
            value: The startOnEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._startOnEvent = None
            return

        if not isinstance(value, RunnableEntity):
            raise TypeError(
                f"startOnEvent must be RunnableEntity or None, got {type(value).__name__}"
            )
        self._startOnEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDisabledModeInstanceRef(self) -> List["ModeDeclaration"]:
        """
        AUTOSAR-compliant getter for disabledModeInstanceRef.

        Returns:
            The disabledModeInstanceRef value

        Note:
            Delegates to disabled_mode_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.disabled_mode_instance_ref  # Delegates to property

    def getStartOnEvent(self) -> "RunnableEntity":
        """
        AUTOSAR-compliant getter for startOnEvent.

        Returns:
            The startOnEvent value

        Note:
            Delegates to start_on_event property (CODING_RULE_V2_00017)
        """
        return self.start_on_event  # Delegates to property

    def setStartOnEvent(self, value: "RunnableEntity") -> "RTEEvent":
        """
        AUTOSAR-compliant setter for startOnEvent with method chaining.

        Args:
            value: The startOnEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to start_on_event property setter (gets validation automatically)
        """
        self.start_on_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_start_on_event(self, value: Optional["RunnableEntity"]) -> "RTEEvent":
        """
        Set startOnEvent and return self for chaining.

        Args:
            value: The startOnEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_start_on_event("value")
        """
        self.start_on_event = value  # Use property setter (gets validation)
        return self
