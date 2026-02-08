from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    MultidimensionalTime,
    TimingClock,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class TimingClockSyncAccuracy(Identifiable):
    """
    Describes the synchronization accuracy between exactly two TDClocks.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock::TimingClockSyncAccuracy

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 252, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Synchronization accuracy, treated as zero if not given.
        self._accuracy: Optional["MultidimensionalTime"] = None

    @property
    def accuracy(self) -> Optional["MultidimensionalTime"]:
        """Get accuracy (Pythonic accessor)."""
        return self._accuracy

    @accuracy.setter
    def accuracy(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set accuracy with validation.

        Args:
            value: The accuracy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accuracy = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"accuracy must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._accuracy = value
        # References a target clock.
        self._lower: Optional["TimingClock"] = None

    @property
    def lower(self) -> Optional["TimingClock"]:
        """Get lower (Pythonic accessor)."""
        return self._lower

    @lower.setter
    def lower(self, value: Optional["TimingClock"]) -> None:
        """
        Set lower with validation.

        Args:
            value: The lower to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lower = None
            return

        if not isinstance(value, TimingClock):
            raise TypeError(
                f"lower must be TimingClock or None, got {type(value).__name__}"
            )
        self._lower = value
        # References a source clock.
        self._upper: Optional["TimingClock"] = None

    @property
    def upper(self) -> Optional["TimingClock"]:
        """Get upper (Pythonic accessor)."""
        return self._upper

    @upper.setter
    def upper(self, value: Optional["TimingClock"]) -> None:
        """
        Set upper with validation.

        Args:
            value: The upper to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upper = None
            return

        if not isinstance(value, TimingClock):
            raise TypeError(
                f"upper must be TimingClock or None, got {type(value).__name__}"
            )
        self._upper = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccuracy(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for accuracy.

        Returns:
            The accuracy value

        Note:
            Delegates to accuracy property (CODING_RULE_V2_00017)
        """
        return self.accuracy  # Delegates to property

    def setAccuracy(self, value: "MultidimensionalTime") -> "TimingClockSyncAccuracy":
        """
        AUTOSAR-compliant setter for accuracy with method chaining.

        Args:
            value: The accuracy to set

        Returns:
            self for method chaining

        Note:
            Delegates to accuracy property setter (gets validation automatically)
        """
        self.accuracy = value  # Delegates to property setter
        return self

    def getLower(self) -> "TimingClock":
        """
        AUTOSAR-compliant getter for lower.

        Returns:
            The lower value

        Note:
            Delegates to lower property (CODING_RULE_V2_00017)
        """
        return self.lower  # Delegates to property

    def setLower(self, value: "TimingClock") -> "TimingClockSyncAccuracy":
        """
        AUTOSAR-compliant setter for lower with method chaining.

        Args:
            value: The lower to set

        Returns:
            self for method chaining

        Note:
            Delegates to lower property setter (gets validation automatically)
        """
        self.lower = value  # Delegates to property setter
        return self

    def getUpper(self) -> "TimingClock":
        """
        AUTOSAR-compliant getter for upper.

        Returns:
            The upper value

        Note:
            Delegates to upper property (CODING_RULE_V2_00017)
        """
        return self.upper  # Delegates to property

    def setUpper(self, value: "TimingClock") -> "TimingClockSyncAccuracy":
        """
        AUTOSAR-compliant setter for upper with method chaining.

        Args:
            value: The upper to set

        Returns:
            self for method chaining

        Note:
            Delegates to upper property setter (gets validation automatically)
        """
        self.upper = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_accuracy(self, value: Optional["MultidimensionalTime"]) -> "TimingClockSyncAccuracy":
        """
        Set accuracy and return self for chaining.

        Args:
            value: The accuracy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_accuracy("value")
        """
        self.accuracy = value  # Use property setter (gets validation)
        return self

    def with_lower(self, value: Optional["TimingClock"]) -> "TimingClockSyncAccuracy":
        """
        Set lower and return self for chaining.

        Args:
            value: The lower to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lower("value")
        """
        self.lower = value  # Use property setter (gets validation)
        return self

    def with_upper(self, value: Optional["TimingClock"]) -> "TimingClockSyncAccuracy":
        """
        Set upper and return self for chaining.

        Args:
            value: The upper to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_upper("value")
        """
        self.upper = value  # Use property setter (gets validation)
        return self
