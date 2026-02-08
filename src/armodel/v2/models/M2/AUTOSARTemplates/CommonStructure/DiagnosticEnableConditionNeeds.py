from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticCapabilityElement,
)


class DiagnosticEnableConditionNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component to provide the
    capability to set an enable condition.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 762, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the initial status for enable or disable of of event reports of a
        # diagnostic event.
        self._initialStatus: Optional["EventAcceptanceStatus"] = None

    @property
    def initial_status(self) -> Optional["EventAcceptanceStatus"]:
        """Get initialStatus (Pythonic accessor)."""
        return self._initialStatus

    @initial_status.setter
    def initial_status(self, value: Optional["EventAcceptanceStatus"]) -> None:
        """
        Set initialStatus with validation.

        Args:
            value: The initialStatus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialStatus = None
            return

        if not isinstance(value, EventAcceptanceStatus):
            raise TypeError(
                f"initialStatus must be EventAcceptanceStatus or None, got {type(value).__name__}"
            )
        self._initialStatus = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitialStatus(self) -> "EventAcceptanceStatus":
        """
        AUTOSAR-compliant getter for initialStatus.

        Returns:
            The initialStatus value

        Note:
            Delegates to initial_status property (CODING_RULE_V2_00017)
        """
        return self.initial_status  # Delegates to property

    def setInitialStatus(self, value: "EventAcceptanceStatus") -> "DiagnosticEnableConditionNeeds":
        """
        AUTOSAR-compliant setter for initialStatus with method chaining.

        Args:
            value: The initialStatus to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_status property setter (gets validation automatically)
        """
        self.initial_status = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_initial_status(self, value: Optional["EventAcceptanceStatus"]) -> "DiagnosticEnableConditionNeeds":
        """
        Set initialStatus and return self for chaining.

        Args:
            value: The initialStatus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_status("value")
        """
        self.initial_status = value  # Use property setter (gets validation)
        return self
