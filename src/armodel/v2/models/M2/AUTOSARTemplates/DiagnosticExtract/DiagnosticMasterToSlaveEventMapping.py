from typing import Optional


class DiagnosticMasterToSlaveEventMapping(DiagnosticMapping):
    """
    This meta-class provides the ability to map a master diagnostic event with a
    slave diagnostic event such that reporting of the master event with a given
    value also reports the slave event with the same value

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticMasterToSlaveEventMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 256, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the master diagnostic event.
        self._masterEvent: Optional["DiagnosticEvent"] = None

    @property
    def master_event(self) -> Optional["DiagnosticEvent"]:
        """Get masterEvent (Pythonic accessor)."""
        return self._masterEvent

    @master_event.setter
    def master_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set masterEvent with validation.

        Args:
            value: The masterEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._masterEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"masterEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._masterEvent = value
        # This represents the slave diagnostic event.
        self._slaveEvent: Optional["DiagnosticEvent"] = None

    @property
    def slave_event(self) -> Optional["DiagnosticEvent"]:
        """Get slaveEvent (Pythonic accessor)."""
        return self._slaveEvent

    @slave_event.setter
    def slave_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set slaveEvent with validation.

        Args:
            value: The slaveEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._slaveEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"slaveEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._slaveEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMasterEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for masterEvent.

        Returns:
            The masterEvent value

        Note:
            Delegates to master_event property (CODING_RULE_V2_00017)
        """
        return self.master_event  # Delegates to property

    def setMasterEvent(self, value: "DiagnosticEvent") -> "DiagnosticMasterToSlaveEventMapping":
        """
        AUTOSAR-compliant setter for masterEvent with method chaining.

        Args:
            value: The masterEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to master_event property setter (gets validation automatically)
        """
        self.master_event = value  # Delegates to property setter
        return self

    def getSlaveEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for slaveEvent.

        Returns:
            The slaveEvent value

        Note:
            Delegates to slave_event property (CODING_RULE_V2_00017)
        """
        return self.slave_event  # Delegates to property

    def setSlaveEvent(self, value: "DiagnosticEvent") -> "DiagnosticMasterToSlaveEventMapping":
        """
        AUTOSAR-compliant setter for slaveEvent with method chaining.

        Args:
            value: The slaveEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to slave_event property setter (gets validation automatically)
        """
        self.slave_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_master_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticMasterToSlaveEventMapping":
        """
        Set masterEvent and return self for chaining.

        Args:
            value: The masterEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_master_event("value")
        """
        self.master_event = value  # Use property setter (gets validation)
        return self

    def with_slave_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticMasterToSlaveEventMapping":
        """
        Set slaveEvent and return self for chaining.

        Args:
            value: The slaveEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_slave_event("value")
        """
        self.slave_event = value  # Use property setter (gets validation)
        return self
