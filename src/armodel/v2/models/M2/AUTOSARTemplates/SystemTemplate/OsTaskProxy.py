from typing import Optional


class OsTaskProxy(ARElement):
    """
    This meta-class represents a proxy for an OsTask in the System Description.

    Package: M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping::OsTaskProxy

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 208, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the period in seconds of this task of a cyclically
                # activated task.
        # Please note that this informative and not directly relevant for the But the
                # attribute value can be mapped OS configuration to support configuration work
                # a fixed set of OsTasks.
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
        # This attribute defines the preemptability of the task.
        self._preemptability: Optional["OsTaskPreemptability"] = None

    @property
    def preemptability(self) -> Optional["OsTaskPreemptability"]:
        """Get preemptability (Pythonic accessor)."""
        return self._preemptability

    @preemptability.setter
    def preemptability(self, value: Optional["OsTaskPreemptability"]) -> None:
        """
        Set preemptability with validation.

        Args:
            value: The preemptability to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._preemptability = None
            return

        if not isinstance(value, OsTaskPreemptability):
            raise TypeError(
                f"preemptability must be OsTaskPreemptability or None, got {type(value).__name__}"
            )
        self._preemptability = value
        # This attribute defines the priority of a task as a relative the values show
        # only the relative ordering of.
        self._priority: Optional["PositiveInteger"] = None

    @property
    def priority(self) -> Optional["PositiveInteger"]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._priority = value

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

    def setPeriod(self, value: "TimeValue") -> "OsTaskProxy":
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

    def getPreemptability(self) -> "OsTaskPreemptability":
        """
        AUTOSAR-compliant getter for preemptability.

        Returns:
            The preemptability value

        Note:
            Delegates to preemptability property (CODING_RULE_V2_00017)
        """
        return self.preemptability  # Delegates to property

    def setPreemptability(self, value: "OsTaskPreemptability") -> "OsTaskProxy":
        """
        AUTOSAR-compliant setter for preemptability with method chaining.

        Args:
            value: The preemptability to set

        Returns:
            self for method chaining

        Note:
            Delegates to preemptability property setter (gets validation automatically)
        """
        self.preemptability = value  # Delegates to property setter
        return self

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "OsTaskProxy":
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_period(self, value: Optional["TimeValue"]) -> "OsTaskProxy":
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

    def with_preemptability(self, value: Optional["OsTaskPreemptability"]) -> "OsTaskProxy":
        """
        Set preemptability and return self for chaining.

        Args:
            value: The preemptability to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_preemptability("value")
        """
        self.preemptability = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "OsTaskProxy":
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self
