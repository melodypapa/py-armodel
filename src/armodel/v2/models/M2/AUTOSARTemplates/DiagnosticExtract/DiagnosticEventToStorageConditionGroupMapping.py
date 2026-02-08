from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DiagnosticEvent,
    DiagnosticMapping,
    DiagnosticStorage,
)


class DiagnosticEventToStorageConditionGroupMapping(DiagnosticMapping):
    """
    Defines which StorageConditionGroup is applicable for a DiagnosticEvent.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticEventToStorageConditionGroupMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 248, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DiagnosticEvent to which a Storage assigned.
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
        # Reference to a StorageConditionGroup assigned to a DiagnosticEvent.
        self._storage: Optional["DiagnosticStorage"] = None

    @property
    def storage(self) -> Optional["DiagnosticStorage"]:
        """Get storage (Pythonic accessor)."""
        return self._storage

    @storage.setter
    def storage(self, value: Optional["DiagnosticStorage"]) -> None:
        """
        Set storage with validation.

        Args:
            value: The storage to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._storage = None
            return

        if not isinstance(value, DiagnosticStorage):
            raise TypeError(
                f"storage must be DiagnosticStorage or None, got {type(value).__name__}"
            )
        self._storage = value

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

    def setDiagnosticEvent(self, value: "DiagnosticEvent") -> "DiagnosticEventToStorageConditionGroupMapping":
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

    def getStorage(self) -> "DiagnosticStorage":
        """
        AUTOSAR-compliant getter for storage.

        Returns:
            The storage value

        Note:
            Delegates to storage property (CODING_RULE_V2_00017)
        """
        return self.storage  # Delegates to property

    def setStorage(self, value: "DiagnosticStorage") -> "DiagnosticEventToStorageConditionGroupMapping":
        """
        AUTOSAR-compliant setter for storage with method chaining.

        Args:
            value: The storage to set

        Returns:
            self for method chaining

        Note:
            Delegates to storage property setter (gets validation automatically)
        """
        self.storage = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic_event(self, value: Optional["DiagnosticEvent"]) -> "DiagnosticEventToStorageConditionGroupMapping":
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

    def with_storage(self, value: Optional["DiagnosticStorage"]) -> "DiagnosticEventToStorageConditionGroupMapping":
        """
        Set storage and return self for chaining.

        Args:
            value: The storage to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_storage("value")
        """
        self.storage = value  # Use property setter (gets validation)
        return self
