from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents import RTEEvent


class DataWriteCompletedEvent(RTEEvent):
    """
    This event is raised when an implicit write access was successful or an
    error occurred.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::DataWriteCompletedEvent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 542, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced VariableAccess raises this DataWrite the implicit write access
        # was an error occurred.
        self._eventSource: Optional["VariableAccess"] = None

    @property
    def event_source(self) -> Optional["VariableAccess"]:
        """Get eventSource (Pythonic accessor)."""
        return self._eventSource

    @event_source.setter
    def event_source(self, value: Optional["VariableAccess"]) -> None:
        """
        Set eventSource with validation.

        Args:
            value: The eventSource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventSource = None
            return

        if not isinstance(value, VariableAccess):
            raise TypeError(
                f"eventSource must be VariableAccess or None, got {type(value).__name__}"
            )
        self._eventSource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventSource(self) -> "VariableAccess":
        """
        AUTOSAR-compliant getter for eventSource.

        Returns:
            The eventSource value

        Note:
            Delegates to event_source property (CODING_RULE_V2_00017)
        """
        return self.event_source  # Delegates to property

    def setEventSource(self, value: "VariableAccess") -> "DataWriteCompletedEvent":
        """
        AUTOSAR-compliant setter for eventSource with method chaining.

        Args:
            value: The eventSource to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_source property setter (gets validation automatically)
        """
        self.event_source = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_source(self, value: Optional["VariableAccess"]) -> "DataWriteCompletedEvent":
        """
        Set eventSource and return self for chaining.

        Args:
            value: The eventSource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_source("value")
        """
        self.event_source = value  # Use property setter (gets validation)
        return self
