from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswScheduleEvent


class BswInternalTriggerOccurredEvent(BswScheduleEvent):
    """
    A BswEvent, which can happen sporadically. The event is activated by
    explicit calls from the module to the BSW Scheduler. The main purpose for
    such an event is to cause a context switch, e.g. from an ISR context into a
    task context. Activation and switching are handled within the same module or
    cluster only.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 91, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The activation point is the source of this event.
        self._eventSourcePoint: RefType = None

    @property
    def event_source_point(self) -> RefType:
        """Get eventSourcePoint (Pythonic accessor)."""
        return self._eventSourcePoint

    @event_source_point.setter
    def event_source_point(self, value: RefType) -> None:
        """
        Set eventSourcePoint with validation.

        Args:
            value: The eventSourcePoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventSourcePoint = None
            return

        self._eventSourcePoint = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventSourcePoint(self) -> RefType:
        """
        AUTOSAR-compliant getter for eventSourcePoint.

        Returns:
            The eventSourcePoint value

        Note:
            Delegates to event_source_point property (CODING_RULE_V2_00017)
        """
        return self.event_source_point  # Delegates to property

    def setEventSourcePoint(self, value: RefType) -> "BswInternalTriggerOccurredEvent":
        """
        AUTOSAR-compliant setter for eventSourcePoint with method chaining.

        Args:
            value: The eventSourcePoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_source_point property setter (gets validation automatically)
        """
        self.event_source_point = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_source_point(self, value: Optional[RefType]) -> "BswInternalTriggerOccurredEvent":
        """
        Set eventSourcePoint and return self for chaining.

        Args:
            value: The eventSourcePoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_source_point("value")
        """
        self.event_source_point = value  # Use property setter (gets validation)
        return self
