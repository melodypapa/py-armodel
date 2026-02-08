from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticCommonElement,
    DiagnosticEvent,
    DiagnosticIumprKind,
)


class DiagnosticIumpr(DiagnosticCommonElement):
    """
    This meta-class represents the ability to model the in-use monitor
    performance ratio. The latter computes to the number of times a fault could
    have been found divided by the number of times the vehicle conditions have
    been properly fulfilled.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticEvent::DiagnosticIumpr

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 210, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference represents the DiagnosticEvent that the IUMPR computation.
        self._event: Optional["DiagnosticEvent"] = None

    @property
    def event(self) -> Optional["DiagnosticEvent"]:
        """Get event (Pythonic accessor)."""
        return self._event

    @event.setter
    def event(self, value: Optional["DiagnosticEvent"]) -> None:
        """
        Set event with validation.

        Args:
            value: The event to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._event = None
            return

        if not isinstance(value, DiagnosticEvent):
            raise TypeError(
                f"event must be DiagnosticEvent or None, got {type(value).__name__}"
            )
        self._event = value
        # This attribute controls the behavior of how the ratio is.
        self._ratioKind: Optional["DiagnosticIumprKind"] = None

    @property
    def ratio_kind(self) -> Optional["DiagnosticIumprKind"]:
        """Get ratioKind (Pythonic accessor)."""
        return self._ratioKind

    @ratio_kind.setter
    def ratio_kind(self, value: Optional["DiagnosticIumprKind"]) -> None:
        """
        Set ratioKind with validation.

        Args:
            value: The ratioKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ratioKind = None
            return

        if not isinstance(value, DiagnosticIumprKind):
            raise TypeError(
                f"ratioKind must be DiagnosticIumprKind or None, got {type(value).__name__}"
            )
        self._ratioKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEvent(self) -> "DiagnosticEvent":
        """
        AUTOSAR-compliant getter for event.

        Returns:
            The event value

        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def setEvent(self, value: "DiagnosticEvent") -> "DiagnosticIumpr":
        """
        AUTOSAR-compliant setter for event with method chaining.

        Args:
            value: The event to set

        Returns:
            self for method chaining

        Note:
            Delegates to event property setter (gets validation automatically)
        """
        self.event = value  # Delegates to property setter
        return self

    def getRatioKind(self) -> "DiagnosticIumprKind":
        """
        AUTOSAR-compliant getter for ratioKind.

        Returns:
            The ratioKind value

        Note:
            Delegates to ratio_kind property (CODING_RULE_V2_00017)
        """
        return self.ratio_kind  # Delegates to property

    def setRatioKind(self, value: "DiagnosticIumprKind") -> "DiagnosticIumpr":
        """
        AUTOSAR-compliant setter for ratioKind with method chaining.

        Args:
            value: The ratioKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to ratio_kind property setter (gets validation automatically)
        """
        self.ratio_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticIumpr":
        """
        Set event and return self for chaining.

        Args:
            value: The event to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event("value")
        """
        self.event = value  # Use property setter (gets validation)
        return self

    def with_ratio_kind(self, value: Optional["DiagnosticIumprKind"]) -> "DiagnosticIumpr":
        """
        Set ratioKind and return self for chaining.

        Args:
            value: The ratioKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ratio_kind("value")
        """
        self.ratio_kind = value  # Use property setter (gets validation)
        return self
