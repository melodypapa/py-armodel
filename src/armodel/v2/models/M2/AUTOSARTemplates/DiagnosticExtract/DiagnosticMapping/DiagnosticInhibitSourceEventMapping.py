from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping import (
    DiagnosticMapping,
)


class DiagnosticInhibitSourceEventMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to map a
    DiagnosticFunctionInhibitSource directly to alternatively one
    DiagnosticEvent or one DiagnosticFimSummaryEvent. This model element shall
    be used if the approach via the alias events is not applicable, i.e. when
    diagnostic events defined by the Dem are already available at the time the
    Fim configuration within the diagnostic extract is created.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::FimMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 260, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the reference to the diagnostic event.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._diagnosticEvent: Optional["DiagnosticEvent"] = None

    @property
    def diagnostic_event(self) -> Optional["DiagnosticEvent"]:
        """Get diagnosticEvent (Pythonic accessor)."""
        return self._diagnosticEvent

    @diagnostic_event.setter
    def diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set diagnosticEvent with validation.

        Args:
            value: The diagnosticEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticEvent = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"diagnosticEvent must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._diagnosticEvent = value
        # This represents the reference to the event group.
        self._eventGroupGroup: Optional["DiagnosticFimEvent"] = None

    @property
    def event_group_group(self) -> Optional["DiagnosticFimEvent"]:
        """Get eventGroupGroup (Pythonic accessor)."""
        return self._eventGroupGroup

    @event_group_group.setter
    def event_group_group(self, value: Optional["DiagnosticFimEvent"]) -> None:
        """
        Set eventGroupGroup with validation.

        Args:
            value: The eventGroupGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventGroupGroup = None
            return

        if not isinstance(value, DiagnosticFimEvent):
            raise TypeError(
                f"eventGroupGroup must be DiagnosticFimEvent or None, got {type(value).__name__}"
            )
        self._eventGroupGroup = value
        # This represents the reference to the inhibition source.
        self._inhibitionSource: Optional["DiagnosticFunction"] = None

    @property
    def inhibition_source(self) -> Optional["DiagnosticFunction"]:
        """Get inhibitionSource (Pythonic accessor)."""
        return self._inhibitionSource

    @inhibition_source.setter
    def inhibition_source(self, value: Optional["DiagnosticFunction"]) -> None:
        """
        Set inhibitionSource with validation.

        Args:
            value: The inhibitionSource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._inhibitionSource = None
            return

        if not isinstance(value, DiagnosticFunction):
            raise TypeError(
                f"inhibitionSource must be DiagnosticFunction or None, got {type(value).__name__}"
            )
        self._inhibitionSource = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnosticEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for diagnosticEvent.

        Returns:
            The diagnosticEvent value

        Note:
            Delegates to diagnostic_event property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_event  # Delegates to property

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> "DiagnosticInhibitSourceEventMapping":
        """
        AUTOSAR-compliant setter for diagnosticEvent with method chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_event property setter (gets validation automatically)
        """
        self.diagnostic_event = value  # Delegates to property setter
        return self

    def getEventGroupGroup(self) -> "DiagnosticFimEvent":
        """
        AUTOSAR-compliant getter for eventGroupGroup.

        Returns:
            The eventGroupGroup value

        Note:
            Delegates to event_group_group property (CODING_RULE_V2_00017)
        """
        return self.event_group_group  # Delegates to property

    def setEventGroupGroup(self, value: "DiagnosticFimEvent") -> "DiagnosticInhibitSourceEventMapping":
        """
        AUTOSAR-compliant setter for eventGroupGroup with method chaining.

        Args:
            value: The eventGroupGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_group_group property setter (gets validation automatically)
        """
        self.event_group_group = value  # Delegates to property setter
        return self

    def getInhibitionSource(self) -> "DiagnosticFunction":
        """
        AUTOSAR-compliant getter for inhibitionSource.

        Returns:
            The inhibitionSource value

        Note:
            Delegates to inhibition_source property (CODING_RULE_V2_00017)
        """
        return self.inhibition_source  # Delegates to property

    def setInhibitionSource(self, value: "DiagnosticFunction") -> "DiagnosticInhibitSourceEventMapping":
        """
        AUTOSAR-compliant setter for inhibitionSource with method chaining.

        Args:
            value: The inhibitionSource to set

        Returns:
            self for method chaining

        Note:
            Delegates to inhibition_source property setter (gets validation automatically)
        """
        self.inhibition_source = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticInhibitSourceEventMapping":
        """
        Set diagnosticEvent and return self for chaining.

        Args:
            value: The diagnosticEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_event("value")
        """
        self.diagnostic_event = value  # Use property setter (gets validation)
        return self

    def with_event_group_group(self, value: Optional["DiagnosticFimEvent"]) -> "DiagnosticInhibitSourceEventMapping":
        """
        Set eventGroupGroup and return self for chaining.

        Args:
            value: The eventGroupGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_group_group("value")
        """
        self.event_group_group = value  # Use property setter (gets validation)
        return self

    def with_inhibition_source(self, value: Optional["DiagnosticFunction"]) -> "DiagnosticInhibitSourceEventMapping":
        """
        Set inhibitionSource and return self for chaining.

        Args:
            value: The inhibitionSource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_inhibition_source("value")
        """
        self.inhibition_source = value  # Use property setter (gets validation)
        return self
