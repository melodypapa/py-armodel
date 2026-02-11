"""
AUTOSAR Package - TimingClock

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock
"""


from __future__ import annotations
from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class TimingClock(Identifiable, ABC):
    """
    Describes an abstract clock.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock::TimingClock

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 252, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TimingClock:
            raise TypeError("TimingClock is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refers to a physical time base reference on the atpVariation.
        self._platformTime: Optional["GlobalTimeDomain"] = None

    @property
    def platform_time(self) -> Optional["GlobalTimeDomain"]:
        """Get platformTime (Pythonic accessor)."""
        return self._platformTime

    @platform_time.setter
    def platform_time(self, value: Optional["GlobalTimeDomain"]) -> None:
        """
        Set platformTime with validation.

        Args:
            value: The platformTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._platformTime = None
            return

        if not isinstance(value, GlobalTimeDomain):
            raise TypeError(
                f"platformTime must be GlobalTimeDomain or None, got {type(value).__name__}"
            )
        self._platformTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPlatformTime(self) -> "GlobalTimeDomain":
        """
        AUTOSAR-compliant getter for platformTime.

        Returns:
            The platformTime value

        Note:
            Delegates to platform_time property (CODING_RULE_V2_00017)
        """
        return self.platform_time  # Delegates to property

    def setPlatformTime(self, value: "GlobalTimeDomain") -> TimingClock:
        """
        AUTOSAR-compliant setter for platformTime with method chaining.

        Args:
            value: The platformTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to platform_time property setter (gets validation automatically)
        """
        self.platform_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_platform_time(self, value: Optional["GlobalTimeDomain"]) -> TimingClock:
        """
        Set platformTime and return self for chaining.

        Args:
            value: The platformTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_platform_time("value")
        """
        self.platform_time = value  # Use property setter (gets validation)
        return self



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
        self._lower: Optional[TimingClock] = None

    @property
    def lower(self) -> Optional[TimingClock]:
        """Get lower (Pythonic accessor)."""
        return self._lower

    @lower.setter
    def lower(self, value: Optional[TimingClock]) -> None:
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
        self._upper: Optional[TimingClock] = None

    @property
    def upper(self) -> Optional[TimingClock]:
        """Get upper (Pythonic accessor)."""
        return self._upper

    @upper.setter
    def upper(self, value: Optional[TimingClock]) -> None:
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

    def setAccuracy(self, value: "MultidimensionalTime") -> TimingClockSyncAccuracy:
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

    def getLower(self) -> TimingClock:
        """
        AUTOSAR-compliant getter for lower.

        Returns:
            The lower value

        Note:
            Delegates to lower property (CODING_RULE_V2_00017)
        """
        return self.lower  # Delegates to property

    def setLower(self, value: TimingClock) -> TimingClockSyncAccuracy:
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

    def getUpper(self) -> TimingClock:
        """
        AUTOSAR-compliant getter for upper.

        Returns:
            The upper value

        Note:
            Delegates to upper property (CODING_RULE_V2_00017)
        """
        return self.upper  # Delegates to property

    def setUpper(self, value: TimingClock) -> TimingClockSyncAccuracy:
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

    def with_accuracy(self, value: Optional["MultidimensionalTime"]) -> TimingClockSyncAccuracy:
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

    def with_lower(self, value: Optional[TimingClock]) -> TimingClockSyncAccuracy:
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

    def with_upper(self, value: Optional[TimingClock]) -> TimingClockSyncAccuracy:
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



class TDLETZoneClock(TimingClock):
    """
    Describes a LET zone clock.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingClock::TDLETZoneClock

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

    def setAccuracyExt(self, value: "MultidimensionalTime") -> TDLETZoneClock:
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

    def setAccuracyInt(self, value: "MultidimensionalTime") -> TDLETZoneClock:
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

    def with_accuracy_ext(self, value: Optional["MultidimensionalTime"]) -> TDLETZoneClock:
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

    def with_accuracy_int(self, value: Optional["MultidimensionalTime"]) -> TDLETZoneClock:
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
