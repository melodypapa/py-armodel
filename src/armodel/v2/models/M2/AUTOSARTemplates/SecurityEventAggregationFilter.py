from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SecurityExtractTemplate import AbstractSecurityEventFilter


class SecurityEventAggregationFilter(AbstractSecurityEventFilter):
    """
    This meta-class represents the aggregation filter that aggregates all
    security events occurring within a configured time frame into one (i.e. the
    last reported) security event.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventAggregationFilter

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 24, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attributes defines whether the context data of the first or last
        # time-aggregated security event shall be used for qualified security event.
        self._contextData: Optional["SecurityEventContext"] = None

    @property
    def context_data(self) -> Optional["SecurityEventContext"]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData

    @context_data.setter
    def context_data(self, value: Optional["SecurityEventContext"]) -> None:
        """
        Set contextData with validation.

        Args:
            value: The contextData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextData = None
            return

        if not isinstance(value, SecurityEventContext):
            raise TypeError(
                f"contextData must be SecurityEventContext or None, got {type(value).__name__}"
            )
        self._contextData = value
        # This attribute represents the configuration of the minimum window in seconds
        # for the aggregation filter.
        self._minimum: Optional["TimeValue"] = None

    @property
    def minimum(self) -> Optional["TimeValue"]:
        """Get minimum (Pythonic accessor)."""
        return self._minimum

    @minimum.setter
    def minimum(self, value: Optional["TimeValue"]) -> None:
        """
        Set minimum with validation.

        Args:
            value: The minimum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimum = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minimum must be TimeValue or None, got {type(value).__name__}"
            )
        self._minimum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextData(self) -> "SecurityEventContext":
        """
        AUTOSAR-compliant getter for contextData.

        Returns:
            The contextData value

        Note:
            Delegates to context_data property (CODING_RULE_V2_00017)
        """
        return self.context_data  # Delegates to property

    def setContextData(self, value: "SecurityEventContext") -> "SecurityEventAggregationFilter":
        """
        AUTOSAR-compliant setter for contextData with method chaining.

        Args:
            value: The contextData to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_data property setter (gets validation automatically)
        """
        self.context_data = value  # Delegates to property setter
        return self

    def getMinimum(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minimum.

        Returns:
            The minimum value

        Note:
            Delegates to minimum property (CODING_RULE_V2_00017)
        """
        return self.minimum  # Delegates to property

    def setMinimum(self, value: "TimeValue") -> "SecurityEventAggregationFilter":
        """
        AUTOSAR-compliant setter for minimum with method chaining.

        Args:
            value: The minimum to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum property setter (gets validation automatically)
        """
        self.minimum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_data(self, value: Optional["SecurityEventContext"]) -> "SecurityEventAggregationFilter":
        """
        Set contextData and return self for chaining.

        Args:
            value: The contextData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_data("value")
        """
        self.context_data = value  # Use property setter (gets validation)
        return self

    def with_minimum(self, value: Optional["TimeValue"]) -> "SecurityEventAggregationFilter":
        """
        Set minimum and return self for chaining.

        Args:
            value: The minimum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum("value")
        """
        self.minimum = value  # Use property setter (gets validation)
        return self
