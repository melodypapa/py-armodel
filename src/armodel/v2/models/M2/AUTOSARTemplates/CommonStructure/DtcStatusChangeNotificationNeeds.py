from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticCapabilityElement,
)


class DtcStatusChangeNotificationNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component interested to
    get information regarding any DTC status change.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 776, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute determines the time when the notification the DTC operation
                # shall be executed.
        # This attribute relevant for the configuration of the ClearDtc.
        self._notificationTime: Optional["DiagnosticClearDtc"] = None

    @property
    def notification_time(self) -> Optional["DiagnosticClearDtc"]:
        """Get notificationTime (Pythonic accessor)."""
        return self._notificationTime

    @notification_time.setter
    def notification_time(self, value: Optional["DiagnosticClearDtc"]) -> None:
        """
        Set notificationTime with validation.

        Args:
            value: The notificationTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._notificationTime = None
            return

        if not isinstance(value, DiagnosticClearDtc):
            raise TypeError(
                f"notificationTime must be DiagnosticClearDtc or None, got {type(value).__name__}"
            )
        self._notificationTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNotificationTime(self) -> "DiagnosticClearDtc":
        """
        AUTOSAR-compliant getter for notificationTime.

        Returns:
            The notificationTime value

        Note:
            Delegates to notification_time property (CODING_RULE_V2_00017)
        """
        return self.notification_time  # Delegates to property

    def setNotificationTime(self, value: "DiagnosticClearDtc") -> "DtcStatusChangeNotificationNeeds":
        """
        AUTOSAR-compliant setter for notificationTime with method chaining.

        Args:
            value: The notificationTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to notification_time property setter (gets validation automatically)
        """
        self.notification_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_notification_time(self, value: Optional["DiagnosticClearDtc"]) -> "DtcStatusChangeNotificationNeeds":
        """
        Set notificationTime and return self for chaining.

        Args:
            value: The notificationTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_notification_time("value")
        """
        self.notification_time = value  # Use property setter (gets validation)
        return self
