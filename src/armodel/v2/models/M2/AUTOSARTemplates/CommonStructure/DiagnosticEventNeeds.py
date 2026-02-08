from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticCapabilityElement,
)


class DiagnosticEventNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs on the configuration of the Diagnostic Event
    Manager for one diagnostic event. Its shortName can be regarded as a symbol
    identifying the diagnostic event from the viewpoint of the component or
    module which owns this element. In case the diagnostic event specifies a
    production error, the shortName shall be the name of the production error.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 258, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 311, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 756, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference contains the link to a function identifier FiM which is used
        # by the monitor before result.
        self._deferringFid: List["FunctionInhibitionNeeds"] = []

    @property
    def deferring_fid(self) -> List["FunctionInhibitionNeeds"]:
        """Get deferringFid (Pythonic accessor)."""
        return self._deferringFid
        # Specifies the abstract need on the Debounce Algorithm applied by the
        # Diagnostic Event Manager.
        self._diagEvent: Optional["DiagEventDebounce"] = None

    @property
    def diag_event(self) -> Optional["DiagEventDebounce"]:
        """Get diagEvent (Pythonic accessor)."""
        return self._diagEvent

    @diag_event.setter
    def diag_event(self, value: Optional["DiagEventDebounce"]) -> None:
        """
        Set diagEvent with validation.

        Args:
            value: The diagEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagEvent = None
            return

        if not isinstance(value, DiagEventDebounce):
            raise TypeError(
                f"diagEvent must be DiagEventDebounce or None, got {type(value).__name__}"
            )
        self._diagEvent = value
        # This represents the primary Function Inhibition Identifier inhibition of the
                # diagnostic monitor.
        # The FID inhibit the monitoring of a symptom or the detected faults.
        self._inhibitingFid: Optional["FunctionInhibitionNeeds"] = None

    @property
    def inhibiting_fid(self) -> Optional["FunctionInhibitionNeeds"]:
        """Get inhibitingFid (Pythonic accessor)."""
        return self._inhibitingFid

    @inhibiting_fid.setter
    def inhibiting_fid(self, value: Optional["FunctionInhibitionNeeds"]) -> None:
        """
        Set inhibitingFid with validation.

        Args:
            value: The inhibitingFid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._inhibitingFid = None
            return

        if not isinstance(value, FunctionInhibitionNeeds):
            raise TypeError(
                f"inhibitingFid must be FunctionInhibitionNeeds or None, got {type(value).__name__}"
            )
        self._inhibitingFid = value
        # This represents the secondary Function Inhibition used for inhibition of the
                # diagnostic monitor.
        # Any FID inhibitions leads to an inhibition of the a symptom or the reporting
                # of detected.
        self._inhibiting: List["FunctionInhibitionNeeds"] = []

    @property
    def inhibiting(self) -> List["FunctionInhibitionNeeds"]:
        """Get inhibiting (Pythonic accessor)."""
        return self._inhibiting
        # If the Event uses a prestored freeze-frame (using the PrestoreFreezeFrame and
                # ClearPrestored of the service interface DiagnosticMonitor) indicates if the
                # Event requires the data to be non-volatile memory.
        # TRUE = Dem shall store data in non-volatile memory, FALSE = Data lost at
                # shutdown (not stored in Nvm).
        self._prestored: Optional["Boolean"] = None

    @property
    def prestored(self) -> Optional["Boolean"]:
        """Get prestored (Pythonic accessor)."""
        return self._prestored

    @prestored.setter
    def prestored(self, value: Optional["Boolean"]) -> None:
        """
        Set prestored with validation.

        Args:
            value: The prestored to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._prestored = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"prestored must be Boolean or None, got {type(value).__name__}"
            )
        self._prestored = value
        # This attribute defines whether additional monitor data be added to the
        # reporting of events.
        self._usesMonitor: Optional["Boolean"] = None

    @property
    def uses_monitor(self) -> Optional["Boolean"]:
        """Get usesMonitor (Pythonic accessor)."""
        return self._usesMonitor

    @uses_monitor.setter
    def uses_monitor(self, value: Optional["Boolean"]) -> None:
        """
        Set usesMonitor with validation.

        Args:
            value: The usesMonitor to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usesMonitor = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"usesMonitor must be Boolean or None, got {type(value).__name__}"
            )
        self._usesMonitor = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDeferringFid(self) -> List["FunctionInhibitionNeeds"]:
        """
        AUTOSAR-compliant getter for deferringFid.

        Returns:
            The deferringFid value

        Note:
            Delegates to deferring_fid property (CODING_RULE_V2_00017)
        """
        return self.deferring_fid  # Delegates to property

    def getDiagEvent(self) -> "DiagEventDebounce":
        """
        AUTOSAR-compliant getter for diagEvent.

        Returns:
            The diagEvent value

        Note:
            Delegates to diag_event property (CODING_RULE_V2_00017)
        """
        return self.diag_event  # Delegates to property

    def setDiagEvent(self, value: "DiagEventDebounce") -> "DiagnosticEventNeeds":
        """
        AUTOSAR-compliant setter for diagEvent with method chaining.

        Args:
            value: The diagEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diag_event property setter (gets validation automatically)
        """
        self.diag_event = value  # Delegates to property setter
        return self

    def getInhibitingFid(self) -> "FunctionInhibitionNeeds":
        """
        AUTOSAR-compliant getter for inhibitingFid.

        Returns:
            The inhibitingFid value

        Note:
            Delegates to inhibiting_fid property (CODING_RULE_V2_00017)
        """
        return self.inhibiting_fid  # Delegates to property

    def setInhibitingFid(self, value: "FunctionInhibitionNeeds") -> "DiagnosticEventNeeds":
        """
        AUTOSAR-compliant setter for inhibitingFid with method chaining.

        Args:
            value: The inhibitingFid to set

        Returns:
            self for method chaining

        Note:
            Delegates to inhibiting_fid property setter (gets validation automatically)
        """
        self.inhibiting_fid = value  # Delegates to property setter
        return self

    def getInhibiting(self) -> List["FunctionInhibitionNeeds"]:
        """
        AUTOSAR-compliant getter for inhibiting.

        Returns:
            The inhibiting value

        Note:
            Delegates to inhibiting property (CODING_RULE_V2_00017)
        """
        return self.inhibiting  # Delegates to property

    def getPrestored(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for prestored.

        Returns:
            The prestored value

        Note:
            Delegates to prestored property (CODING_RULE_V2_00017)
        """
        return self.prestored  # Delegates to property

    def setPrestored(self, value: "Boolean") -> "DiagnosticEventNeeds":
        """
        AUTOSAR-compliant setter for prestored with method chaining.

        Args:
            value: The prestored to set

        Returns:
            self for method chaining

        Note:
            Delegates to prestored property setter (gets validation automatically)
        """
        self.prestored = value  # Delegates to property setter
        return self

    def getUsesMonitor(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for usesMonitor.

        Returns:
            The usesMonitor value

        Note:
            Delegates to uses_monitor property (CODING_RULE_V2_00017)
        """
        return self.uses_monitor  # Delegates to property

    def setUsesMonitor(self, value: "Boolean") -> "DiagnosticEventNeeds":
        """
        AUTOSAR-compliant setter for usesMonitor with method chaining.

        Args:
            value: The usesMonitor to set

        Returns:
            self for method chaining

        Note:
            Delegates to uses_monitor property setter (gets validation automatically)
        """
        self.uses_monitor = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diag_event(self, value: Optional["DiagEventDebounce"]) -> "DiagnosticEventNeeds":
        """
        Set diagEvent and return self for chaining.

        Args:
            value: The diagEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diag_event("value")
        """
        self.diag_event = value  # Use property setter (gets validation)
        return self

    def with_inhibiting_fid(self, value: Optional["FunctionInhibitionNeeds"]) -> "DiagnosticEventNeeds":
        """
        Set inhibitingFid and return self for chaining.

        Args:
            value: The inhibitingFid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_inhibiting_fid("value")
        """
        self.inhibiting_fid = value  # Use property setter (gets validation)
        return self

    def with_prestored(self, value: Optional["Boolean"]) -> "DiagnosticEventNeeds":
        """
        Set prestored and return self for chaining.

        Args:
            value: The prestored to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_prestored("value")
        """
        self.prestored = value  # Use property setter (gets validation)
        return self

    def with_uses_monitor(self, value: Optional["Boolean"]) -> "DiagnosticEventNeeds":
        """
        Set usesMonitor and return self for chaining.

        Args:
            value: The usesMonitor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uses_monitor("value")
        """
        self.uses_monitor = value  # Use property setter (gets validation)
        return self
