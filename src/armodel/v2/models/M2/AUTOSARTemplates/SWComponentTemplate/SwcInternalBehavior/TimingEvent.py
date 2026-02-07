from typing import Optional


class TimingEvent(RTEEvent):
    """
    This event is used to start RunnableEntities that shall be executed
    periodically.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::RTEEvents::TimingEvent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 532, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 254, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The value makes an assumption about the time offset of activation of the
                # RunnableEntity triggered by the relative to the periodic activation of base
                # of this TimingEvent.
        # Unit: second.
        self._offset: Optional["TimeValue"] = None

    @property
    def offset(self) -> Optional["TimeValue"]:
        """Get offset (Pythonic accessor)."""
        return self._offset

    @offset.setter
    def offset(self, value: Optional["TimeValue"]) -> None:
        """
        Set offset with validation.

        Args:
            value: The offset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._offset = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"offset must be TimeValue or None, got {type(value).__name__}"
            )
        self._offset = value
        # Period of timing event in seconds.
        # The value of this be greater than zero.
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

    def getOffset(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for offset.

        Returns:
            The offset value

        Note:
            Delegates to offset property (CODING_RULE_V2_00017)
        """
        return self.offset  # Delegates to property

    def setOffset(self, value: "TimeValue") -> "TimingEvent":
        """
        AUTOSAR-compliant setter for offset with method chaining.

        Args:
            value: The offset to set

        Returns:
            self for method chaining

        Note:
            Delegates to offset property setter (gets validation automatically)
        """
        self.offset = value  # Delegates to property setter
        return self

    def getPeriod(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for period.

        Returns:
            The period value

        Note:
            Delegates to period property (CODING_RULE_V2_00017)
        """
        return self.period  # Delegates to property

    def setPeriod(self, value: "TimeValue") -> "TimingEvent":
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

    def with_offset(self, value: Optional["TimeValue"]) -> "TimingEvent":
        """
        Set offset and return self for chaining.

        Args:
            value: The offset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_offset("value")
        """
        self.offset = value  # Use property setter (gets validation)
        return self

    def with_period(self, value: Optional["TimeValue"]) -> "TimingEvent":
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
