from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class IdsmTrafficLimitation(Identifiable):
    """
    This meta-class represents the configuration of a traffic limitation filter
    for Security Events. This means that security events are dropped if the size
    (in terms of bandwidth) of security events (of any type) processed within a
    configurable time window is greater than a configurable threshold.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsmTrafficLimitation

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 28, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute configures the threshold for dropping events if the size of
        # all processed security events threshold in the respective time interval.
        self._maxBytesIn: Optional["PositiveInteger"] = None

    @property
    def max_bytes_in(self) -> Optional["PositiveInteger"]:
        """Get maxBytesIn (Pythonic accessor)."""
        return self._maxBytesIn

    @max_bytes_in.setter
    def max_bytes_in(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxBytesIn with validation.

        Args:
            value: The maxBytesIn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxBytesIn = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxBytesIn must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxBytesIn = value
        # This attribute configures the length of the time interval in dropping
        # security events if the size of all events exceeds the configurable the
        # respective time interval.
        self._timeInterval: Optional["Float"] = None

    @property
    def time_interval(self) -> Optional["Float"]:
        """Get timeInterval (Pythonic accessor)."""
        return self._timeInterval

    @time_interval.setter
    def time_interval(self, value: Optional["Float"]) -> None:
        """
        Set timeInterval with validation.

        Args:
            value: The timeInterval to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeInterval = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"timeInterval must be Float or None, got {type(value).__name__}"
            )
        self._timeInterval = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxBytesIn(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxBytesIn.

        Returns:
            The maxBytesIn value

        Note:
            Delegates to max_bytes_in property (CODING_RULE_V2_00017)
        """
        return self.max_bytes_in  # Delegates to property

    def setMaxBytesIn(self, value: "PositiveInteger") -> "IdsmTrafficLimitation":
        """
        AUTOSAR-compliant setter for maxBytesIn with method chaining.

        Args:
            value: The maxBytesIn to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_bytes_in property setter (gets validation automatically)
        """
        self.max_bytes_in = value  # Delegates to property setter
        return self

    def getTimeInterval(self) -> "Float":
        """
        AUTOSAR-compliant getter for timeInterval.

        Returns:
            The timeInterval value

        Note:
            Delegates to time_interval property (CODING_RULE_V2_00017)
        """
        return self.time_interval  # Delegates to property

    def setTimeInterval(self, value: "Float") -> "IdsmTrafficLimitation":
        """
        AUTOSAR-compliant setter for timeInterval with method chaining.

        Args:
            value: The timeInterval to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_interval property setter (gets validation automatically)
        """
        self.time_interval = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_bytes_in(self, value: Optional["PositiveInteger"]) -> "IdsmTrafficLimitation":
        """
        Set maxBytesIn and return self for chaining.

        Args:
            value: The maxBytesIn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_bytes_in("value")
        """
        self.max_bytes_in = value  # Use property setter (gets validation)
        return self

    def with_time_interval(self, value: Optional["Float"]) -> "IdsmTrafficLimitation":
        """
        Set timeInterval and return self for chaining.

        Args:
            value: The timeInterval to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_interval("value")
        """
        self.time_interval = value  # Use property setter (gets validation)
        return self
