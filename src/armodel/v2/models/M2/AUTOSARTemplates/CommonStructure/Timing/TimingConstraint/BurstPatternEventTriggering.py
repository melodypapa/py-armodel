from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import EventTriggeringConstraint


class BurstPatternEventTriggering(EventTriggeringConstraint):
    """
    Describes the maximum number of occurrences of the same event in a given
    time interval. Typically used to model a worst case activation scenario.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint::BurstPatternEventTriggering

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 109, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum number of event occurrences within the time interval.
        # The event may never occur, or may times between 1 and the parameter specified
                # then the event least the number of times specified by at maximum by.
        self._maxNumberOf: Optional["PositiveInteger"] = None

    @property
    def max_number_of(self) -> Optional["PositiveInteger"]:
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNumberOf with validation.

        Args:
            value: The maxNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOf = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxNumberOf must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        # Specifies the minimum distance between subsequent of the event within the
        # given time interval.
        self._minimumInter: Optional["MultidimensionalTime"] = None

    @property
    def minimum_inter(self) -> Optional["MultidimensionalTime"]:
        """Get minimumInter (Pythonic accessor)."""
        return self._minimumInter

    @minimum_inter.setter
    def minimum_inter(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set minimumInter with validation.

        Args:
            value: The minimumInter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumInter = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"minimumInter must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._minimumInter = value
        # The minimum number of event occurrences within the time interval.
        self._minNumberOf: Optional["PositiveInteger"] = None

    @property
    def min_number_of(self) -> Optional["PositiveInteger"]:
        """Get minNumberOf (Pythonic accessor)."""
        return self._minNumberOf

    @min_number_of.setter
    def min_number_of(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minNumberOf with validation.

        Args:
            value: The minNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minNumberOf = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minNumberOf must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minNumberOf = value
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
        # arbitrary points in the given time interval.
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
        # The time distance between the beginnings of subsequent the given burst
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

    def getMaxNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "PositiveInteger") -> "BurstPatternEventTriggering":
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
        return self

    def getMinimumInter(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for minimumInter.

        Returns:
            The minimumInter value

        Note:
            Delegates to minimum_inter property (CODING_RULE_V2_00017)
        """
        return self.minimum_inter  # Delegates to property

    def setMinimumInter(self, value: "MultidimensionalTime") -> "BurstPatternEventTriggering":
        """
        AUTOSAR-compliant setter for minimumInter with method chaining.

        Args:
            value: The minimumInter to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum_inter property setter (gets validation automatically)
        """
        self.minimum_inter = value  # Delegates to property setter
        return self

    def getMinNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minNumberOf.

        Returns:
            The minNumberOf value

        Note:
            Delegates to min_number_of property (CODING_RULE_V2_00017)
        """
        return self.min_number_of  # Delegates to property

    def setMinNumberOf(self, value: "PositiveInteger") -> "BurstPatternEventTriggering":
        """
        AUTOSAR-compliant setter for minNumberOf with method chaining.

        Args:
            value: The minNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_number_of property setter (gets validation automatically)
        """
        self.min_number_of = value  # Delegates to property setter
        return self

    def getPatternJitter(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for patternJitter.

        Returns:
            The patternJitter value

        Note:
            Delegates to pattern_jitter property (CODING_RULE_V2_00017)
        """
        return self.pattern_jitter  # Delegates to property

    def setPatternJitter(self, value: "MultidimensionalTime") -> "BurstPatternEventTriggering":
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

    def setPatternLength(self, value: "MultidimensionalTime") -> "BurstPatternEventTriggering":
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

    def setPatternPeriod(self, value: "MultidimensionalTime") -> "BurstPatternEventTriggering":
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

    def with_max_number_of(self, value: Optional["PositiveInteger"]) -> "BurstPatternEventTriggering":
        """
        Set maxNumberOf and return self for chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self

    def with_minimum_inter(self, value: Optional["MultidimensionalTime"]) -> "BurstPatternEventTriggering":
        """
        Set minimumInter and return self for chaining.

        Args:
            value: The minimumInter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum_inter("value")
        """
        self.minimum_inter = value  # Use property setter (gets validation)
        return self

    def with_min_number_of(self, value: Optional["PositiveInteger"]) -> "BurstPatternEventTriggering":
        """
        Set minNumberOf and return self for chaining.

        Args:
            value: The minNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_number_of("value")
        """
        self.min_number_of = value  # Use property setter (gets validation)
        return self

    def with_pattern_jitter(self, value: Optional["MultidimensionalTime"]) -> "BurstPatternEventTriggering":
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

    def with_pattern_length(self, value: Optional["MultidimensionalTime"]) -> "BurstPatternEventTriggering":
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

    def with_pattern_period(self, value: Optional["MultidimensionalTime"]) -> "BurstPatternEventTriggering":
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
