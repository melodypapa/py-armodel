from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import (
    EventTriggeringConstraint,
)


class ConcretePatternEventTriggering(EventTriggeringConstraint):
    """
    Describes the behavior of an event that occurs according to a precisely
    known pattern.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 106, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The offset for each occurrence of the event in the interval.
        # A list of point-in-times in the time by the parameter patternLength at which
                # occurs.
        self._offset: List["MultidimensionalTime"] = []

    @property
    def offset(self) -> List["MultidimensionalTime"]:
        """Get offset (Pythonic accessor)."""
        return self._offset
        # The maximum deviation of the time interval’s starting the beginning of the
                # given period.
        # This only applicable in conjunction with the.
        self._patternJitter: Optional["MultidimensionalTime"] = None

    @property
    def pattern_jitter(self) -> Optional["MultidimensionalTime"]:
        """Get patternJitter (Pythonic accessor)."""
        return self._patternJitter

    @pattern_jitter.setter
    def pattern_jitter(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set patternJitter with validation.

        Args:
            value: The patternJitter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._patternJitter = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"patternJitter must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._patternJitter = value
        # The duration of the time interval within which the event The event occurs at
        # concrete points in the given time interval.
        self._patternLength: Optional["MultidimensionalTime"] = None

    @property
    def pattern_length(self) -> Optional["MultidimensionalTime"]:
        """Get patternLength (Pythonic accessor)."""
        return self._patternLength

    @pattern_length.setter
    def pattern_length(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set patternLength with validation.

        Args:
            value: The patternLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._patternLength = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"patternLength must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._patternLength = value
        # The time distance between the beginnings of subsequent the given concrete
        # pattern.
        self._patternPeriod: Optional["MultidimensionalTime"] = None

    @property
    def pattern_period(self) -> Optional["MultidimensionalTime"]:
        """Get patternPeriod (Pythonic accessor)."""
        return self._patternPeriod

    @pattern_period.setter
    def pattern_period(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set patternPeriod with validation.

        Args:
            value: The patternPeriod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._patternPeriod = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"patternPeriod must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._patternPeriod = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOffset(self) -> List["MultidimensionalTime"]:
        """
        AUTOSAR-compliant getter for offset.

        Returns:
            The offset value

        Note:
            Delegates to offset property (CODING_RULE_V2_00017)
        """
        return self.offset  # Delegates to property

    def getPatternJitter(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for patternJitter.

        Returns:
            The patternJitter value

        Note:
            Delegates to pattern_jitter property (CODING_RULE_V2_00017)
        """
        return self.pattern_jitter  # Delegates to property

    def setPatternJitter(self, value: "MultidimensionalTime") -> "ConcretePatternEventTriggering":
        """
        AUTOSAR-compliant setter for patternJitter with method chaining.

        Args:
            value: The patternJitter to set

        Returns:
            self for method chaining

        Note:
            Delegates to pattern_jitter property setter (gets validation automatically)
        """
        self.pattern_jitter = value  # Delegates to property setter
        return self

    def getPatternLength(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for patternLength.

        Returns:
            The patternLength value

        Note:
            Delegates to pattern_length property (CODING_RULE_V2_00017)
        """
        return self.pattern_length  # Delegates to property

    def setPatternLength(self, value: "MultidimensionalTime") -> "ConcretePatternEventTriggering":
        """
        AUTOSAR-compliant setter for patternLength with method chaining.

        Args:
            value: The patternLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to pattern_length property setter (gets validation automatically)
        """
        self.pattern_length = value  # Delegates to property setter
        return self

    def getPatternPeriod(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for patternPeriod.

        Returns:
            The patternPeriod value

        Note:
            Delegates to pattern_period property (CODING_RULE_V2_00017)
        """
        return self.pattern_period  # Delegates to property

    def setPatternPeriod(self, value: "MultidimensionalTime") -> "ConcretePatternEventTriggering":
        """
        AUTOSAR-compliant setter for patternPeriod with method chaining.

        Args:
            value: The patternPeriod to set

        Returns:
            self for method chaining

        Note:
            Delegates to pattern_period property setter (gets validation automatically)
        """
        self.pattern_period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_pattern_jitter(self, value: Optional["MultidimensionalTime"]) -> "ConcretePatternEventTriggering":
        """
        Set patternJitter and return self for chaining.

        Args:
            value: The patternJitter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pattern_jitter("value")
        """
        self.pattern_jitter = value  # Use property setter (gets validation)
        return self

    def with_pattern_length(self, value: Optional["MultidimensionalTime"]) -> "ConcretePatternEventTriggering":
        """
        Set patternLength and return self for chaining.

        Args:
            value: The patternLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pattern_length("value")
        """
        self.pattern_length = value  # Use property setter (gets validation)
        return self

    def with_pattern_period(self, value: Optional["MultidimensionalTime"]) -> "ConcretePatternEventTriggering":
        """
        Set patternPeriod and return self for chaining.

        Args:
            value: The patternPeriod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pattern_period("value")
        """
        self.pattern_period = value  # Use property setter (gets validation)
        return self
