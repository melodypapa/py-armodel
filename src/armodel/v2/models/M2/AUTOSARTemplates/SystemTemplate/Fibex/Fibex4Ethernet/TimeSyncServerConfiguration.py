from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
    Referrable,
)


class TimeSyncServerConfiguration(Referrable):
    """
    Defines the configuration of the time synchronisation server.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 470, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Server Priority.
        self._priority: Optional["PositiveInteger"] = None

    @property
    def priority(self) -> Optional["PositiveInteger"]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._priority = value
        # Synchronisation interval used by the time synchronisation seconds).
        self._syncInterval: Optional["TimeValue"] = None

    @property
    def sync_interval(self) -> Optional["TimeValue"]:
        """Get syncInterval (Pythonic accessor)."""
        return self._syncInterval

    @sync_interval.setter
    def sync_interval(self, value: Optional["TimeValue"]) -> None:
        """
        Set syncInterval with validation.

        Args:
            value: The syncInterval to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncInterval = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"syncInterval must be TimeValue or None, got {type(value).__name__}"
            )
        self._syncInterval = value
        # Identifier of the TimeSyncServer.
        self._timeSyncServerIdentifier: Optional["String"] = None

    @property
    def time_sync_server_identifier(self) -> Optional["String"]:
        """Get timeSyncServerIdentifier (Pythonic accessor)."""
        return self._timeSyncServerIdentifier

    @time_sync_server_identifier.setter
    def time_sync_server_identifier(self, value: Optional["String"]) -> None:
        """
        Set timeSyncServerIdentifier with validation.

        Args:
            value: The timeSyncServerIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSyncServerIdentifier = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"timeSyncServerIdentifier must be String or None, got {type(value).__name__}"
            )
        self._timeSyncServerIdentifier = value
        # Defines the time synchronisation technology used.
        # Possible values are: NTP_RFC958, PTP_ AVB_ others.
        self._timeSync: Optional["TimeSyncTechnology"] = None

    @property
    def time_sync(self) -> Optional["TimeSyncTechnology"]:
        """Get timeSync (Pythonic accessor)."""
        return self._timeSync

    @time_sync.setter
    def time_sync(self, value: Optional["TimeSyncTechnology"]) -> None:
        """
        Set timeSync with validation.

        Args:
            value: The timeSync to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeSync = None
            return

        if not isinstance(value, TimeSyncTechnology):
            raise TypeError(
                f"timeSync must be TimeSyncTechnology or None, got {type(value).__name__}"
            )
        self._timeSync = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "TimeSyncServerConfiguration":
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    def getSyncInterval(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for syncInterval.

        Returns:
            The syncInterval value

        Note:
            Delegates to sync_interval property (CODING_RULE_V2_00017)
        """
        return self.sync_interval  # Delegates to property

    def setSyncInterval(self, value: "TimeValue") -> "TimeSyncServerConfiguration":
        """
        AUTOSAR-compliant setter for syncInterval with method chaining.

        Args:
            value: The syncInterval to set

        Returns:
            self for method chaining

        Note:
            Delegates to sync_interval property setter (gets validation automatically)
        """
        self.sync_interval = value  # Delegates to property setter
        return self

    def getTimeSyncServerIdentifier(self) -> "String":
        """
        AUTOSAR-compliant getter for timeSyncServerIdentifier.

        Returns:
            The timeSyncServerIdentifier value

        Note:
            Delegates to time_sync_server_identifier property (CODING_RULE_V2_00017)
        """
        return self.time_sync_server_identifier  # Delegates to property

    def setTimeSyncServerIdentifier(self, value: "String") -> "TimeSyncServerConfiguration":
        """
        AUTOSAR-compliant setter for timeSyncServerIdentifier with method chaining.

        Args:
            value: The timeSyncServerIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_sync_server_identifier property setter (gets validation automatically)
        """
        self.time_sync_server_identifier = value  # Delegates to property setter
        return self

    def getTimeSync(self) -> "TimeSyncTechnology":
        """
        AUTOSAR-compliant getter for timeSync.

        Returns:
            The timeSync value

        Note:
            Delegates to time_sync property (CODING_RULE_V2_00017)
        """
        return self.time_sync  # Delegates to property

    def setTimeSync(self, value: "TimeSyncTechnology") -> "TimeSyncServerConfiguration":
        """
        AUTOSAR-compliant setter for timeSync with method chaining.

        Args:
            value: The timeSync to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_sync property setter (gets validation automatically)
        """
        self.time_sync = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_priority(self, value: Optional["PositiveInteger"]) -> "TimeSyncServerConfiguration":
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self

    def with_sync_interval(self, value: Optional["TimeValue"]) -> "TimeSyncServerConfiguration":
        """
        Set syncInterval and return self for chaining.

        Args:
            value: The syncInterval to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sync_interval("value")
        """
        self.sync_interval = value  # Use property setter (gets validation)
        return self

    def with_time_sync_server_identifier(self, value: Optional["String"]) -> "TimeSyncServerConfiguration":
        """
        Set timeSyncServerIdentifier and return self for chaining.

        Args:
            value: The timeSyncServerIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_sync_server_identifier("value")
        """
        self.time_sync_server_identifier = value  # Use property setter (gets validation)
        return self

    def with_time_sync(self, value: Optional["TimeSyncTechnology"]) -> "TimeSyncServerConfiguration":
        """
        Set timeSync and return self for chaining.

        Args:
            value: The timeSync to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_sync("value")
        """
        self.time_sync = value  # Use property setter (gets validation)
        return self
