from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import TDEventVfbPort

    RefType,
)


class TDEventTrigger(TDEventVfbPort):
    """
    This is used to describe timing events related to triggers at VFB level.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 58, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The specific type of this timing event.
        self._tdEventTrigger: RefType = None

    @property
    def td_event_trigger(self) -> RefType:
        """Get tdEventTrigger (Pythonic accessor)."""
        return self._tdEventTrigger

    @td_event_trigger.setter
    def td_event_trigger(self, value: RefType) -> None:
        """
        Set tdEventTrigger with validation.

        Args:
            value: The tdEventTrigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventTrigger = None
            return

        self._tdEventTrigger = value
        # The trigger which is provided (released) or required the given context.
        self._trigger: RefType = None

    @property
    def trigger(self) -> RefType:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    @trigger.setter
    def trigger(self, value: RefType) -> None:
        """
        Set trigger with validation.

        Args:
            value: The trigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trigger = None
            return

        self._trigger = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTdEventTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for tdEventTrigger.

        Returns:
            The tdEventTrigger value

        Note:
            Delegates to td_event_trigger property (CODING_RULE_V2_00017)
        """
        return self.td_event_trigger  # Delegates to property

    def setTdEventTrigger(self, value: RefType) -> "TDEventTrigger":
        """
        AUTOSAR-compliant setter for tdEventTrigger with method chaining.

        Args:
            value: The tdEventTrigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_trigger property setter (gets validation automatically)
        """
        self.td_event_trigger = value  # Delegates to property setter
        return self

    def getTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for trigger.

        Returns:
            The trigger value

        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    def setTrigger(self, value: RefType) -> "TDEventTrigger":
        """
        AUTOSAR-compliant setter for trigger with method chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to trigger property setter (gets validation automatically)
        """
        self.trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_td_event_trigger(self, value: Optional[RefType]) -> "TDEventTrigger":
        """
        Set tdEventTrigger and return self for chaining.

        Args:
            value: The tdEventTrigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_trigger("value")
        """
        self.td_event_trigger = value  # Use property setter (gets validation)
        return self

    def with_trigger(self, value: Optional[RefType]) -> "TDEventTrigger":
        """
        Set trigger and return self for chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger("value")
        """
        self.trigger = value  # Use property setter (gets validation)
        return self
