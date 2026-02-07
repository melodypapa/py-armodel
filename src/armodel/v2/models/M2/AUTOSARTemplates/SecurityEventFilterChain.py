from typing import Optional


class SecurityEventFilterChain(IdsCommonElement):
    """
    This meta-class represents a configurable chain of filters used to qualify
    security events. The different filters of this filter chain are applied in
    the follow order: SecurityEventStateFilter, SecurityEventOneEvery NFilter,
    SecurityEventAggregationFilter, SecurityEventThresholdFilter.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventFilterChain

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 20, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents the aggregation filter in the chain.
        self._aggregation: Optional["SecurityEvent"] = None

    @property
    def aggregation(self) -> Optional["SecurityEvent"]:
        """Get aggregation (Pythonic accessor)."""
        return self._aggregation

    @aggregation.setter
    def aggregation(self, value: Optional["SecurityEvent"]) -> None:
        """
        Set aggregation with validation.

        Args:
            value: The aggregation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aggregation = None
            return

        if not isinstance(value, SecurityEvent):
            raise TypeError(
                f"aggregation must be SecurityEvent or None, got {type(value).__name__}"
            )
        self._aggregation = value
        # This aggregation represents the sampling filter in the filter.
        self._oneEveryN: Optional["SecurityEventOneEvery"] = None

    @property
    def one_every_n(self) -> Optional["SecurityEventOneEvery"]:
        """Get oneEveryN (Pythonic accessor)."""
        return self._oneEveryN

    @one_every_n.setter
    def one_every_n(self, value: Optional["SecurityEventOneEvery"]) -> None:
        """
        Set oneEveryN with validation.

        Args:
            value: The oneEveryN to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._oneEveryN = None
            return

        if not isinstance(value, SecurityEventOneEvery):
            raise TypeError(
                f"oneEveryN must be SecurityEventOneEvery or None, got {type(value).__name__}"
            )
        self._oneEveryN = value
        # This aggregation represents the state filter in the event 97 Document ID 980:
        # AUTOSAR_FO_TPS_SecurityExtractTemplate Template R23-11.
        self._state: Optional["SecurityEventStateFilter"] = None

    @property
    def state(self) -> Optional["SecurityEventStateFilter"]:
        """Get state (Pythonic accessor)."""
        return self._state

    @state.setter
    def state(self, value: Optional["SecurityEventStateFilter"]) -> None:
        """
        Set state with validation.

        Args:
            value: The state to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._state = None
            return

        if not isinstance(value, SecurityEventStateFilter):
            raise TypeError(
                f"state must be SecurityEventStateFilter or None, got {type(value).__name__}"
            )
        self._state = value
        # This aggregation represents the threshold filter in the filter.
        self._threshold: Optional["SecurityEventThreshold"] = None

    @property
    def threshold(self) -> Optional["SecurityEventThreshold"]:
        """Get threshold (Pythonic accessor)."""
        return self._threshold

    @threshold.setter
    def threshold(self, value: Optional["SecurityEventThreshold"]) -> None:
        """
        Set threshold with validation.

        Args:
            value: The threshold to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._threshold = None
            return

        if not isinstance(value, SecurityEventThreshold):
            raise TypeError(
                f"threshold must be SecurityEventThreshold or None, got {type(value).__name__}"
            )
        self._threshold = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAggregation(self) -> "SecurityEvent":
        """
        AUTOSAR-compliant getter for aggregation.

        Returns:
            The aggregation value

        Note:
            Delegates to aggregation property (CODING_RULE_V2_00017)
        """
        return self.aggregation  # Delegates to property

    def setAggregation(self, value: "SecurityEvent") -> "SecurityEventFilterChain":
        """
        AUTOSAR-compliant setter for aggregation with method chaining.

        Args:
            value: The aggregation to set

        Returns:
            self for method chaining

        Note:
            Delegates to aggregation property setter (gets validation automatically)
        """
        self.aggregation = value  # Delegates to property setter
        return self

    def getOneEveryN(self) -> "SecurityEventOneEvery":
        """
        AUTOSAR-compliant getter for oneEveryN.

        Returns:
            The oneEveryN value

        Note:
            Delegates to one_every_n property (CODING_RULE_V2_00017)
        """
        return self.one_every_n  # Delegates to property

    def setOneEveryN(self, value: "SecurityEventOneEvery") -> "SecurityEventFilterChain":
        """
        AUTOSAR-compliant setter for oneEveryN with method chaining.

        Args:
            value: The oneEveryN to set

        Returns:
            self for method chaining

        Note:
            Delegates to one_every_n property setter (gets validation automatically)
        """
        self.one_every_n = value  # Delegates to property setter
        return self

    def getState(self) -> "SecurityEventStateFilter":
        """
        AUTOSAR-compliant getter for state.

        Returns:
            The state value

        Note:
            Delegates to state property (CODING_RULE_V2_00017)
        """
        return self.state  # Delegates to property

    def setState(self, value: "SecurityEventStateFilter") -> "SecurityEventFilterChain":
        """
        AUTOSAR-compliant setter for state with method chaining.

        Args:
            value: The state to set

        Returns:
            self for method chaining

        Note:
            Delegates to state property setter (gets validation automatically)
        """
        self.state = value  # Delegates to property setter
        return self

    def getThreshold(self) -> "SecurityEventThreshold":
        """
        AUTOSAR-compliant getter for threshold.

        Returns:
            The threshold value

        Note:
            Delegates to threshold property (CODING_RULE_V2_00017)
        """
        return self.threshold  # Delegates to property

    def setThreshold(self, value: "SecurityEventThreshold") -> "SecurityEventFilterChain":
        """
        AUTOSAR-compliant setter for threshold with method chaining.

        Args:
            value: The threshold to set

        Returns:
            self for method chaining

        Note:
            Delegates to threshold property setter (gets validation automatically)
        """
        self.threshold = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_aggregation(self, value: Optional["SecurityEvent"]) -> "SecurityEventFilterChain":
        """
        Set aggregation and return self for chaining.

        Args:
            value: The aggregation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_aggregation("value")
        """
        self.aggregation = value  # Use property setter (gets validation)
        return self

    def with_one_every_n(self, value: Optional["SecurityEventOneEvery"]) -> "SecurityEventFilterChain":
        """
        Set oneEveryN and return self for chaining.

        Args:
            value: The oneEveryN to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_one_every_n("value")
        """
        self.one_every_n = value  # Use property setter (gets validation)
        return self

    def with_state(self, value: Optional["SecurityEventStateFilter"]) -> "SecurityEventFilterChain":
        """
        Set state and return self for chaining.

        Args:
            value: The state to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_state("value")
        """
        self.state = value  # Use property setter (gets validation)
        return self

    def with_threshold(self, value: Optional["SecurityEventThreshold"]) -> "SecurityEventFilterChain":
        """
        Set threshold and return self for chaining.

        Args:
            value: The threshold to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_threshold("value")
        """
        self.threshold = value  # Use property setter (gets validation)
        return self
