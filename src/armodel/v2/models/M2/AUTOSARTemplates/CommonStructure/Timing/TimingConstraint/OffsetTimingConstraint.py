from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    MultidimensionalTime,
    TimingConstraint,
    TimingDescriptionEvent,
)


class OffsetTimingConstraint(TimingConstraint):
    """
    Bounds the time offset between the occurrence of two timing events, without
    requiring a direct functional dependency between the source and the target.
    If the target event occurs, it is expected to occur earliest with the
    minimum, and latest with the maximum offset relatively after the occurrence
    of the source event. Note: not every source event occurrence shall be
    followed by a target event occurrence. In contrast to
    LatencyTimingConstraint, there shall not necessarily be a causal dependency
    between the source and target event.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::OffsetConstraint::OffsetTimingConstraint

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 114, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum offset the target event occurs relatively occurrence of the
        # source event.
        self._maximum: Optional["MultidimensionalTime"] = None

    @property
    def maximum(self) -> Optional["MultidimensionalTime"]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set maximum with validation.

        Args:
            value: The maximum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"maximum must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._maximum = value
        # The mimum offset the target event occurs relatively after of the source
        # event.
        self._minimum: Optional["MultidimensionalTime"] = None

    @property
    def minimum(self) -> Optional["MultidimensionalTime"]:
        """Get minimum (Pythonic accessor)."""
        return self._minimum

    @minimum.setter
    def minimum(self, value: Optional["MultidimensionalTime"]) -> None:
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

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"minimum must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._minimum = value
        # The timing event that the target event is to be.
        self._source: Optional["TimingDescriptionEvent"] = None

    @property
    def source(self) -> Optional["TimingDescriptionEvent"]:
        """Get source (Pythonic accessor)."""
        return self._source

    @source.setter
    def source(self, value: Optional["TimingDescriptionEvent"]) -> None:
        """
        Set source with validation.

        Args:
            value: The source to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._source = None
            return

        if not isinstance(value, TimingDescriptionEvent):
            raise TypeError(
                f"source must be TimingDescriptionEvent or None, got {type(value).__name__}"
            )
        self._source = value
        # The timing event which is expected to occur timely after event.
        self._target: Optional["TimingDescriptionEvent"] = None

    @property
    def target(self) -> Optional["TimingDescriptionEvent"]:
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: Optional["TimingDescriptionEvent"]) -> None:
        """
        Set target with validation.

        Args:
            value: The target to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._target = None
            return

        if not isinstance(value, TimingDescriptionEvent):
            raise TypeError(
                f"target must be TimingDescriptionEvent or None, got {type(value).__name__}"
            )
        self._target = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaximum(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: "MultidimensionalTime") -> "OffsetTimingConstraint":
        """
        AUTOSAR-compliant setter for maximum with method chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    def getMinimum(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for minimum.

        Returns:
            The minimum value

        Note:
            Delegates to minimum property (CODING_RULE_V2_00017)
        """
        return self.minimum  # Delegates to property

    def setMinimum(self, value: "MultidimensionalTime") -> "OffsetTimingConstraint":
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

    def getSource(self) -> "TimingDescriptionEvent":
        """
        AUTOSAR-compliant getter for source.

        Returns:
            The source value

        Note:
            Delegates to source property (CODING_RULE_V2_00017)
        """
        return self.source  # Delegates to property

    def setSource(self, value: "TimingDescriptionEvent") -> "OffsetTimingConstraint":
        """
        AUTOSAR-compliant setter for source with method chaining.

        Args:
            value: The source to set

        Returns:
            self for method chaining

        Note:
            Delegates to source property setter (gets validation automatically)
        """
        self.source = value  # Delegates to property setter
        return self

    def getTarget(self) -> "TimingDescriptionEvent":
        """
        AUTOSAR-compliant getter for target.

        Returns:
            The target value

        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: "TimingDescriptionEvent") -> "OffsetTimingConstraint":
        """
        AUTOSAR-compliant setter for target with method chaining.

        Args:
            value: The target to set

        Returns:
            self for method chaining

        Note:
            Delegates to target property setter (gets validation automatically)
        """
        self.target = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_maximum(self, value: Optional["MultidimensionalTime"]) -> "OffsetTimingConstraint":
        """
        Set maximum and return self for chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self

    def with_minimum(self, value: Optional["MultidimensionalTime"]) -> "OffsetTimingConstraint":
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

    def with_source(self, value: Optional["TimingDescriptionEvent"]) -> "OffsetTimingConstraint":
        """
        Set source and return self for chaining.

        Args:
            value: The source to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source("value")
        """
        self.source = value  # Use property setter (gets validation)
        return self

    def with_target(self, value: Optional["TimingDescriptionEvent"]) -> "OffsetTimingConstraint":
        """
        Set target and return self for chaining.

        Args:
            value: The target to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target("value")
        """
        self.target = value  # Use property setter (gets validation)
        return self
