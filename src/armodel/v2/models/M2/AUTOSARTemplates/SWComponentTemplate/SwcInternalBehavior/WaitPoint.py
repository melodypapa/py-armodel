from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class WaitPoint(Identifiable):
    """
    This defines a wait-point for which the RunnableEntity can wait.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 550, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Time in seconds before the WaitPoint times out and the call returns with an
        # error indicating the.
        self._timeout: Optional["TimeValue"] = None

    @property
    def timeout(self) -> Optional["TimeValue"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeout with validation.

        Args:
            value: The timeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeout = value
        self._trigger: Optional["RTEEvent"] = None

    @property
    def trigger(self) -> Optional["RTEEvent"]:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    @trigger.setter
    def trigger(self, value: Optional["RTEEvent"]) -> None:
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

        if not isinstance(value, RTEEvent):
            raise TypeError(
                f"trigger must be RTEEvent or None, got {type(value).__name__}"
            )
        self._trigger = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeout.

        Returns:
            The timeout value

        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "TimeValue") -> "WaitPoint":
        """
        AUTOSAR-compliant setter for timeout with method chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    def getTrigger(self) -> "RTEEvent":
        """
        AUTOSAR-compliant getter for trigger.

        Returns:
            The trigger value

        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    def setTrigger(self, value: "RTEEvent") -> "WaitPoint":
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

    def with_timeout(self, value: Optional["TimeValue"]) -> "WaitPoint":
        """
        Set timeout and return self for chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self

    def with_trigger(self, value: Optional["RTEEvent"]) -> "WaitPoint":
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
