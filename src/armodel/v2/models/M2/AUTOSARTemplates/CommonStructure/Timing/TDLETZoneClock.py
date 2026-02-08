from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock import (
    TimingClock,
)


class TDLETZoneClock(TimingClock):
    """
    Describes a LET zone clock.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 252, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # External synchronization accuracy within the LET Zone/.
        self._accuracyExt: Optional["MultidimensionalTime"] = None

    @property
    def accuracy_ext(self) -> Optional["MultidimensionalTime"]:
        """Get accuracyExt (Pythonic accessor)."""
        return self._accuracyExt

    @accuracy_ext.setter
    def accuracy_ext(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set accuracyExt with validation.

        Args:
            value: The accuracyExt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accuracyExt = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"accuracyExt must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._accuracyExt = value
        # Internal synchronization accuracy within the LET Zone/.
        self._accuracyInt: Optional["MultidimensionalTime"] = None

    @property
    def accuracy_int(self) -> Optional["MultidimensionalTime"]:
        """Get accuracyInt (Pythonic accessor)."""
        return self._accuracyInt

    @accuracy_int.setter
    def accuracy_int(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set accuracyInt with validation.

        Args:
            value: The accuracyInt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accuracyInt = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"accuracyInt must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._accuracyInt = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccuracyExt(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for accuracyExt.

        Returns:
            The accuracyExt value

        Note:
            Delegates to accuracy_ext property (CODING_RULE_V2_00017)
        """
        return self.accuracy_ext  # Delegates to property

    def setAccuracyExt(self, value: "MultidimensionalTime") -> "TDLETZoneClock":
        """
        AUTOSAR-compliant setter for accuracyExt with method chaining.

        Args:
            value: The accuracyExt to set

        Returns:
            self for method chaining

        Note:
            Delegates to accuracy_ext property setter (gets validation automatically)
        """
        self.accuracy_ext = value  # Delegates to property setter
        return self

    def getAccuracyInt(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for accuracyInt.

        Returns:
            The accuracyInt value

        Note:
            Delegates to accuracy_int property (CODING_RULE_V2_00017)
        """
        return self.accuracy_int  # Delegates to property

    def setAccuracyInt(self, value: "MultidimensionalTime") -> "TDLETZoneClock":
        """
        AUTOSAR-compliant setter for accuracyInt with method chaining.

        Args:
            value: The accuracyInt to set

        Returns:
            self for method chaining

        Note:
            Delegates to accuracy_int property setter (gets validation automatically)
        """
        self.accuracy_int = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_accuracy_ext(self, value: Optional["MultidimensionalTime"]) -> "TDLETZoneClock":
        """
        Set accuracyExt and return self for chaining.

        Args:
            value: The accuracyExt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_accuracy_ext("value")
        """
        self.accuracy_ext = value  # Use property setter (gets validation)
        return self

    def with_accuracy_int(self, value: Optional["MultidimensionalTime"]) -> "TDLETZoneClock":
        """
        Set accuracyInt and return self for chaining.

        Args:
            value: The accuracyInt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_accuracy_int("value")
        """
        self.accuracy_int = value  # Use property setter (gets validation)
        return self
