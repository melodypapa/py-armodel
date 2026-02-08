from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import GlobalTimeDomain
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

    def setPlatformTime(self, value: "GlobalTimeDomain") -> "TimingClock":
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

    def with_platform_time(self, value: Optional["GlobalTimeDomain"]) -> "TimingClock":
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
