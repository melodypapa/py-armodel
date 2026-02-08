from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable


class CyclicTiming(Describable):
    """
    Specification of a cyclic sending behavior.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::CyclicTiming

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 396, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the time until first transmission of This attribute
        # defines the time between Com_ the first transmission of the cyclic this
        # transmission request for this I-PDU.
        self._timeOffset: Optional["TimeRangeType"] = None

    @property
    def time_offset(self) -> Optional["TimeRangeType"]:
        """Get timeOffset (Pythonic accessor)."""
        return self._timeOffset

    @time_offset.setter
    def time_offset(self, value: Optional["TimeRangeType"]) -> None:
        """
        Set timeOffset with validation.

        Args:
            value: The timeOffset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeOffset = None
            return

        if not isinstance(value, TimeRangeType):
            raise TypeError(
                f"timeOffset must be TimeRangeType or None, got {type(value).__name__}"
            )
        self._timeOffset = value
        # Period of the repetition of cyclic transmissions.
        self._timePeriod: Optional["TimeRangeType"] = None

    @property
    def time_period(self) -> Optional["TimeRangeType"]:
        """Get timePeriod (Pythonic accessor)."""
        return self._timePeriod

    @time_period.setter
    def time_period(self, value: Optional["TimeRangeType"]) -> None:
        """
        Set timePeriod with validation.

        Args:
            value: The timePeriod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timePeriod = None
            return

        if not isinstance(value, TimeRangeType):
            raise TypeError(
                f"timePeriod must be TimeRangeType or None, got {type(value).__name__}"
            )
        self._timePeriod = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimeOffset(self) -> "TimeRangeType":
        """
        AUTOSAR-compliant getter for timeOffset.

        Returns:
            The timeOffset value

        Note:
            Delegates to time_offset property (CODING_RULE_V2_00017)
        """
        return self.time_offset  # Delegates to property

    def setTimeOffset(self, value: "TimeRangeType") -> "CyclicTiming":
        """
        AUTOSAR-compliant setter for timeOffset with method chaining.

        Args:
            value: The timeOffset to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_offset property setter (gets validation automatically)
        """
        self.time_offset = value  # Delegates to property setter
        return self

    def getTimePeriod(self) -> "TimeRangeType":
        """
        AUTOSAR-compliant getter for timePeriod.

        Returns:
            The timePeriod value

        Note:
            Delegates to time_period property (CODING_RULE_V2_00017)
        """
        return self.time_period  # Delegates to property

    def setTimePeriod(self, value: "TimeRangeType") -> "CyclicTiming":
        """
        AUTOSAR-compliant setter for timePeriod with method chaining.

        Args:
            value: The timePeriod to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_period property setter (gets validation automatically)
        """
        self.time_period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_time_offset(self, value: Optional["TimeRangeType"]) -> "CyclicTiming":
        """
        Set timeOffset and return self for chaining.

        Args:
            value: The timeOffset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_offset("value")
        """
        self.time_offset = value  # Use property setter (gets validation)
        return self

    def with_time_period(self, value: Optional["TimeRangeType"]) -> "CyclicTiming":
        """
        Set timePeriod and return self for chaining.

        Args:
            value: The timePeriod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_period("value")
        """
        self.time_period = value  # Use property setter (gets validation)
        return self
