from typing import Optional


class BswTimingEvent(BswScheduleEvent):
    """
    A recurring BswEvent driven by a time period.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswTimingEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 88, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 217, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Requirement for the time period (in seconds) by which is triggered.
        self._period: Optional["TimeValue"] = None

    @property
    def period(self) -> Optional["TimeValue"]:
        """Get period (Pythonic accessor)."""
        return self._period

    @period.setter
    def period(self, value: Optional["TimeValue"]) -> None:
        """
        Set period with validation.

        Args:
            value: The period to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._period = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"period must be TimeValue or None, got {type(value).__name__}"
            )
        self._period = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPeriod(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for period.

        Returns:
            The period value

        Note:
            Delegates to period property (CODING_RULE_V2_00017)
        """
        return self.period  # Delegates to property

    def setPeriod(self, value: "TimeValue") -> "BswTimingEvent":
        """
        AUTOSAR-compliant setter for period with method chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Note:
            Delegates to period property setter (gets validation automatically)
        """
        self.period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_period(self, value: Optional["TimeValue"]) -> "BswTimingEvent":
        """
        Set period and return self for chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_period("value")
        """
        self.period = value  # Use property setter (gets validation)
        return self
