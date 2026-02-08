from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import TimeValue
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SomeipTpChannel(Identifiable):
    """
    This element is used to assign properties to SomeipTpConnections that are
    referencing this SomeipTp Channel.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::SomeipTpChannel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 620, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the number of segments that shall be a burst ignoring
                # separationTime.
        # then only be applied between bursts.
        # configured, SeparationTime will be applied between.
        self._burstSize: Optional["PositiveInteger"] = None

    @property
    def burst_size(self) -> Optional["PositiveInteger"]:
        """Get burstSize (Pythonic accessor)."""
        return self._burstSize

    @burst_size.setter
    def burst_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set burstSize with validation.

        Args:
            value: The burstSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._burstSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"burstSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._burstSize = value
        # Timer to monitor the successful reception.
        # It is started first NPdu is received, restarted after reception NPdus, and is
                # stopped when the last been received.
        self._rxTimeoutTime: Optional["TimeValue"] = None

    @property
    def rx_timeout_time(self) -> Optional["TimeValue"]:
        """Get rxTimeoutTime (Pythonic accessor)."""
        return self._rxTimeoutTime

    @rx_timeout_time.setter
    def rx_timeout_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set rxTimeoutTime with validation.

        Args:
            value: The rxTimeoutTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rxTimeoutTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"rxTimeoutTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._rxTimeoutTime = value
        # Sets the duration of the minimum time in seconds the module shall wait
        # between the NPdus.
        self._separationTime: Optional["TimeValue"] = None

    @property
    def separation_time(self) -> Optional["TimeValue"]:
        """Get separationTime (Pythonic accessor)."""
        return self._separationTime

    @separation_time.setter
    def separation_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set separationTime with validation.

        Args:
            value: The separationTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._separationTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"separationTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._separationTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBurstSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for burstSize.

        Returns:
            The burstSize value

        Note:
            Delegates to burst_size property (CODING_RULE_V2_00017)
        """
        return self.burst_size  # Delegates to property

    def setBurstSize(self, value: "PositiveInteger") -> "SomeipTpChannel":
        """
        AUTOSAR-compliant setter for burstSize with method chaining.

        Args:
            value: The burstSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to burst_size property setter (gets validation automatically)
        """
        self.burst_size = value  # Delegates to property setter
        return self

    def getRxTimeoutTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for rxTimeoutTime.

        Returns:
            The rxTimeoutTime value

        Note:
            Delegates to rx_timeout_time property (CODING_RULE_V2_00017)
        """
        return self.rx_timeout_time  # Delegates to property

    def setRxTimeoutTime(self, value: "TimeValue") -> "SomeipTpChannel":
        """
        AUTOSAR-compliant setter for rxTimeoutTime with method chaining.

        Args:
            value: The rxTimeoutTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to rx_timeout_time property setter (gets validation automatically)
        """
        self.rx_timeout_time = value  # Delegates to property setter
        return self

    def getSeparationTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for separationTime.

        Returns:
            The separationTime value

        Note:
            Delegates to separation_time property (CODING_RULE_V2_00017)
        """
        return self.separation_time  # Delegates to property

    def setSeparationTime(self, value: "TimeValue") -> "SomeipTpChannel":
        """
        AUTOSAR-compliant setter for separationTime with method chaining.

        Args:
            value: The separationTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to separation_time property setter (gets validation automatically)
        """
        self.separation_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_burst_size(self, value: Optional["PositiveInteger"]) -> "SomeipTpChannel":
        """
        Set burstSize and return self for chaining.

        Args:
            value: The burstSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_burst_size("value")
        """
        self.burst_size = value  # Use property setter (gets validation)
        return self

    def with_rx_timeout_time(self, value: Optional["TimeValue"]) -> "SomeipTpChannel":
        """
        Set rxTimeoutTime and return self for chaining.

        Args:
            value: The rxTimeoutTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rx_timeout_time("value")
        """
        self.rx_timeout_time = value  # Use property setter (gets validation)
        return self

    def with_separation_time(self, value: Optional["TimeValue"]) -> "SomeipTpChannel":
        """
        Set separationTime and return self for chaining.

        Args:
            value: The separationTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_separation_time("value")
        """
        self.separation_time = value  # Use property setter (gets validation)
        return self
