from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticCapabilityElement,
)


class ObdRatioServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration
    of OBD Services in relation to a particular "ratio monitoring" which is
    supported by this component or module.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 795, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines how the DEM is connected to the component or to perform the IUMPR (In
        # use monitor service.
        self._connectionType: Optional["ObdRatioConnection"] = None

    @property
    def connection_type(self) -> Optional["ObdRatioConnection"]:
        """Get connectionType (Pythonic accessor)."""
        return self._connectionType

    @connection_type.setter
    def connection_type(self, value: Optional["ObdRatioConnection"]) -> None:
        """
        Set connectionType with validation.

        Args:
            value: The connectionType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connectionType = None
            return

        if not isinstance(value, ObdRatioConnection):
            raise TypeError(
                f"connectionType must be ObdRatioConnection or None, got {type(value).__name__}"
            )
        self._connectionType = value
        # The rate based monitored Diagnostic Event.
        self._rateBasedMonitoredEvent: Optional["DiagnosticEventNeeds"] = None

    @property
    def rate_based_monitored_event(self) -> Optional["DiagnosticEventNeeds"]:
        """Get rateBasedMonitoredEvent (Pythonic accessor)."""
        return self._rateBasedMonitoredEvent

    @rate_based_monitored_event.setter
    def rate_based_monitored_event(self, value: Optional["DiagnosticEventNeeds"]) -> None:
        """
        Set rateBasedMonitoredEvent with validation.

        Args:
            value: The rateBasedMonitoredEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rateBasedMonitoredEvent = None
            return

        if not isinstance(value, DiagnosticEventNeeds):
            raise TypeError(
                f"rateBasedMonitoredEvent must be DiagnosticEventNeeds or None, got {type(value).__name__}"
            )
        self._rateBasedMonitoredEvent = value
        # This represents the primary Function Inhibition Identifier the rate based
                # monitor.
        # This is an optional.
        self._usedFid: Optional["FunctionInhibitionNeeds"] = None

    @property
    def used_fid(self) -> Optional["FunctionInhibitionNeeds"]:
        """Get usedFid (Pythonic accessor)."""
        return self._usedFid

    @used_fid.setter
    def used_fid(self, value: Optional["FunctionInhibitionNeeds"]) -> None:
        """
        Set usedFid with validation.

        Args:
            value: The usedFid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usedFid = None
            return

        if not isinstance(value, FunctionInhibitionNeeds):
            raise TypeError(
                f"usedFid must be FunctionInhibitionNeeds or None, got {type(value).__name__}"
            )
        self._usedFid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnectionType(self) -> "ObdRatioConnection":
        """
        AUTOSAR-compliant getter for connectionType.

        Returns:
            The connectionType value

        Note:
            Delegates to connection_type property (CODING_RULE_V2_00017)
        """
        return self.connection_type  # Delegates to property

    def setConnectionType(self, value: "ObdRatioConnection") -> "ObdRatioServiceNeeds":
        """
        AUTOSAR-compliant setter for connectionType with method chaining.

        Args:
            value: The connectionType to set

        Returns:
            self for method chaining

        Note:
            Delegates to connection_type property setter (gets validation automatically)
        """
        self.connection_type = value  # Delegates to property setter
        return self

    def getRateBasedMonitoredEvent(self) -> "DiagnosticEventNeeds":
        """
        AUTOSAR-compliant getter for rateBasedMonitoredEvent.

        Returns:
            The rateBasedMonitoredEvent value

        Note:
            Delegates to rate_based_monitored_event property (CODING_RULE_V2_00017)
        """
        return self.rate_based_monitored_event  # Delegates to property

    def setRateBasedMonitoredEvent(self, value: "DiagnosticEventNeeds") -> "ObdRatioServiceNeeds":
        """
        AUTOSAR-compliant setter for rateBasedMonitoredEvent with method chaining.

        Args:
            value: The rateBasedMonitoredEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to rate_based_monitored_event property setter (gets validation automatically)
        """
        self.rate_based_monitored_event = value  # Delegates to property setter
        return self

    def getUsedFid(self) -> "FunctionInhibitionNeeds":
        """
        AUTOSAR-compliant getter for usedFid.

        Returns:
            The usedFid value

        Note:
            Delegates to used_fid property (CODING_RULE_V2_00017)
        """
        return self.used_fid  # Delegates to property

    def setUsedFid(self, value: "FunctionInhibitionNeeds") -> "ObdRatioServiceNeeds":
        """
        AUTOSAR-compliant setter for usedFid with method chaining.

        Args:
            value: The usedFid to set

        Returns:
            self for method chaining

        Note:
            Delegates to used_fid property setter (gets validation automatically)
        """
        self.used_fid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_connection_type(self, value: Optional["ObdRatioConnection"]) -> "ObdRatioServiceNeeds":
        """
        Set connectionType and return self for chaining.

        Args:
            value: The connectionType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connection_type("value")
        """
        self.connection_type = value  # Use property setter (gets validation)
        return self

    def with_rate_based_monitored_event(self, value: Optional["DiagnosticEventNeeds"]) -> "ObdRatioServiceNeeds":
        """
        Set rateBasedMonitoredEvent and return self for chaining.

        Args:
            value: The rateBasedMonitoredEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rate_based_monitored_event("value")
        """
        self.rate_based_monitored_event = value  # Use property setter (gets validation)
        return self

    def with_used_fid(self, value: Optional["FunctionInhibitionNeeds"]) -> "ObdRatioServiceNeeds":
        """
        Set usedFid and return self for chaining.

        Args:
            value: The usedFid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_used_fid("value")
        """
        self.used_fid = value  # Use property setter (gets validation)
        return self
