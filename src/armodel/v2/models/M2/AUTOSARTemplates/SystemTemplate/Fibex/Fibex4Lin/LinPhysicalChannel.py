from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import PhysicalChannel


class LinPhysicalChannel(PhysicalChannel):
    """
    LIN specific attributes to the physicalChannel

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology::LinPhysicalChannel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 99, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute shall be used to set an idle timeout period the enclosing
                # LinPhysicalChannel.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._busIdleTimeout: Optional["TimeValue"] = None

    @property
    def bus_idle_timeout(self) -> Optional["TimeValue"]:
        """Get busIdleTimeout (Pythonic accessor)."""
        return self._busIdleTimeout

    @bus_idle_timeout.setter
    def bus_idle_timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set busIdleTimeout with validation.

        Args:
            value: The busIdleTimeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._busIdleTimeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"busIdleTimeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._busIdleTimeout = value
        # Schedule tables organize the timings of the frames for the transmitted frames
                # are variable, the shall be variable, too.
        # atpVariation.
        self._scheduleTable: List["LinScheduleTable"] = []

    @property
    def schedule_table(self) -> List["LinScheduleTable"]:
        """Get scheduleTable (Pythonic accessor)."""
        return self._scheduleTable

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBusIdleTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for busIdleTimeout.

        Returns:
            The busIdleTimeout value

        Note:
            Delegates to bus_idle_timeout property (CODING_RULE_V2_00017)
        """
        return self.bus_idle_timeout  # Delegates to property

    def setBusIdleTimeout(self, value: "TimeValue") -> "LinPhysicalChannel":
        """
        AUTOSAR-compliant setter for busIdleTimeout with method chaining.

        Args:
            value: The busIdleTimeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to bus_idle_timeout property setter (gets validation automatically)
        """
        self.bus_idle_timeout = value  # Delegates to property setter
        return self

    def getScheduleTable(self) -> List["LinScheduleTable"]:
        """
        AUTOSAR-compliant getter for scheduleTable.

        Returns:
            The scheduleTable value

        Note:
            Delegates to schedule_table property (CODING_RULE_V2_00017)
        """
        return self.schedule_table  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bus_idle_timeout(self, value: Optional["TimeValue"]) -> "LinPhysicalChannel":
        """
        Set busIdleTimeout and return self for chaining.

        Args:
            value: The busIdleTimeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bus_idle_timeout("value")
        """
        self.bus_idle_timeout = value  # Use property setter (gets validation)
        return self
