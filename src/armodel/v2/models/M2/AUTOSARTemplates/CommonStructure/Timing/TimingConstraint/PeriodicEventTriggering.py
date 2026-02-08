from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.EventTriggeringConstraint import EventTriggeringConstraint


class PeriodicEventTriggering(EventTriggeringConstraint):
    """
    Describes the behavior of an event with a strict periodic occurrence
    pattern, given by period. Additionally, it is possible to soften the
    strictness of the periodic occurrence behavior by specifying a jitter, so
    that there can be a deviation from the period up to the size of the jitter.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingConstraint::EventTriggeringConstraint::PeriodicEventTriggering

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 101, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum deviation of the periodic event occurrence.
        self._jitter: Optional["MultidimensionalTime"] = None

    @property
    def jitter(self) -> Optional["MultidimensionalTime"]:
        """Get jitter (Pythonic accessor)."""
        return self._jitter

    @jitter.setter
    def jitter(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set jitter with validation.

        Args:
            value: The jitter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._jitter = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"jitter must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._jitter = value
        # The minimum time distance between subsequent occurrences of the associated
                # event.
        # minimumInterArrivalTime is less than the the jitter, then the no effect on
                # the the constraint.
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
        # The periodic distance between subsequent occurrences event.
        self._period: Optional["MultidimensionalTime"] = None

    @property
    def period(self) -> Optional["MultidimensionalTime"]:
        """Get period (Pythonic accessor)."""
        return self._period

    @period.setter
    def period(self, value: Optional["MultidimensionalTime"]) -> None:
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

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"period must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._period = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getJitter(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for jitter.

        Returns:
            The jitter value

        Note:
            Delegates to jitter property (CODING_RULE_V2_00017)
        """
        return self.jitter  # Delegates to property

    def setJitter(self, value: "MultidimensionalTime") -> "PeriodicEventTriggering":
        """
        AUTOSAR-compliant setter for jitter with method chaining.

        Args:
            value: The jitter to set

        Returns:
            self for method chaining

        Note:
            Delegates to jitter property setter (gets validation automatically)
        """
        self.jitter = value  # Delegates to property setter
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

    def setMinimumInter(self, value: "MultidimensionalTime") -> "PeriodicEventTriggering":
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

    def getPeriod(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for period.

        Returns:
            The period value

        Note:
            Delegates to period property (CODING_RULE_V2_00017)
        """
        return self.period  # Delegates to property

    def setPeriod(self, value: "MultidimensionalTime") -> "PeriodicEventTriggering":
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

    def with_jitter(self, value: Optional["MultidimensionalTime"]) -> "PeriodicEventTriggering":
        """
        Set jitter and return self for chaining.

        Args:
            value: The jitter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_jitter("value")
        """
        self.jitter = value  # Use property setter (gets validation)
        return self

    def with_minimum_inter(self, value: Optional["MultidimensionalTime"]) -> "PeriodicEventTriggering":
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

    def with_period(self, value: Optional["MultidimensionalTime"]) -> "PeriodicEventTriggering":
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
