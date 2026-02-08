from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    AbstractSecurityEventFilter,
    TimeValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SecurityEventThresholdFilter(AbstractSecurityEventFilter):
    """
    This meta-class represents the threshold filter that drops (repeatedly at
    each beginning of a configurable time interval) a configurable number of
    security events . All subsequently arriving security events (within the
    configured time interval) pass the filter.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventThresholdFilter

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 26, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute configures the time interval in seconds for filter operation.
        self._intervalLength: Optional["TimeValue"] = None

    @property
    def interval_length(self) -> Optional["TimeValue"]:
        """Get intervalLength (Pythonic accessor)."""
        return self._intervalLength

    @interval_length.setter
    def interval_length(self, value: Optional["TimeValue"]) -> None:
        """
        Set intervalLength with validation.

        Args:
            value: The intervalLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._intervalLength = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"intervalLength must be TimeValue or None, got {type(value).__name__}"
            )
        self._intervalLength = value
        # This attribute configures the threshold number, i.
        # e.
        # how security events in the configured time frame are subsequent events start
                # to pass the filter.
        self._threshold: Optional["PositiveInteger"] = None

    @property
    def threshold(self) -> Optional["PositiveInteger"]:
        """Get threshold (Pythonic accessor)."""
        return self._threshold

    @threshold.setter
    def threshold(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"threshold must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._threshold = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntervalLength(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for intervalLength.

        Returns:
            The intervalLength value

        Note:
            Delegates to interval_length property (CODING_RULE_V2_00017)
        """
        return self.interval_length  # Delegates to property

    def setIntervalLength(self, value: "TimeValue") -> "SecurityEventThresholdFilter":
        """
        AUTOSAR-compliant setter for intervalLength with method chaining.

        Args:
            value: The intervalLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to interval_length property setter (gets validation automatically)
        """
        self.interval_length = value  # Delegates to property setter
        return self

    def getThreshold(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for threshold.

        Returns:
            The threshold value

        Note:
            Delegates to threshold property (CODING_RULE_V2_00017)
        """
        return self.threshold  # Delegates to property

    def setThreshold(self, value: "PositiveInteger") -> "SecurityEventThresholdFilter":
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

    def with_interval_length(self, value: Optional["TimeValue"]) -> "SecurityEventThresholdFilter":
        """
        Set intervalLength and return self for chaining.

        Args:
            value: The intervalLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_interval_length("value")
        """
        self.interval_length = value  # Use property setter (gets validation)
        return self

    def with_threshold(self, value: Optional["PositiveInteger"]) -> "SecurityEventThresholdFilter":
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
