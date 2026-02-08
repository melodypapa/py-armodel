from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ApplicationDataType,
    DiagnosticCapabilityElement,
    DiagnosticEventNeeds,
    DiagnosticMonitor,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class ObdMonitorServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration
    of OBD Services in relation to a particular on-board monitoring test
    supported by this component or module. (OBD Service 06).

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ObdMonitorServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 324, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 797, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # reference to an ApplicationDataType that describes the of the data reported
        # by the software-component to.
        self._applicationData: Optional["ApplicationDataType"] = None

    @property
    def application_data(self) -> Optional["ApplicationDataType"]:
        """Get applicationData (Pythonic accessor)."""
        return self._applicationData

    @application_data.setter
    def application_data(self, value: Optional["ApplicationDataType"]) -> None:
        """
        Set applicationData with validation.

        Args:
            value: The applicationData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._applicationData = None
            return

        if not isinstance(value, ApplicationDataType):
            raise TypeError(
                f"applicationData must be ApplicationDataType or None, got {type(value).__name__}"
            )
        self._applicationData = value
        # This reference identifies the corresponding diagnostic.
        self._eventNeeds: Optional["DiagnosticEventNeeds"] = None

    @property
    def event_needs(self) -> Optional["DiagnosticEventNeeds"]:
        """Get eventNeeds (Pythonic accessor)."""
        return self._eventNeeds

    @event_needs.setter
    def event_needs(self, value: Optional["DiagnosticEventNeeds"]) -> None:
        """
        Set eventNeeds with validation.

        Args:
            value: The eventNeeds to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventNeeds = None
            return

        if not isinstance(value, DiagnosticEventNeeds):
            raise TypeError(
                f"eventNeeds must be DiagnosticEventNeeds or None, got {type(value).__name__}"
            )
        self._eventNeeds = value
        # Unit and scaling ID according to ISO 15031-5.
        self._unitAndScalingId: Optional["PositiveInteger"] = None

    @property
    def unit_and_scaling_id(self) -> Optional["PositiveInteger"]:
        """Get unitAndScalingId (Pythonic accessor)."""
        return self._unitAndScalingId

    @unit_and_scaling_id.setter
    def unit_and_scaling_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set unitAndScalingId with validation.

        Args:
            value: The unitAndScalingId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unitAndScalingId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"unitAndScalingId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._unitAndScalingId = value
        # This attribute indicates the settings for the acceptance of to the Dem.
        self._updateKind: Optional["DiagnosticMonitor"] = None

    @property
    def update_kind(self) -> Optional["DiagnosticMonitor"]:
        """Get updateKind (Pythonic accessor)."""
        return self._updateKind

    @update_kind.setter
    def update_kind(self, value: Optional["DiagnosticMonitor"]) -> None:
        """
        Set updateKind with validation.

        Args:
            value: The updateKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._updateKind = None
            return

        if not isinstance(value, DiagnosticMonitor):
            raise TypeError(
                f"updateKind must be DiagnosticMonitor or None, got {type(value).__name__}"
            )
        self._updateKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplicationData(self) -> "ApplicationDataType":
        """
        AUTOSAR-compliant getter for applicationData.

        Returns:
            The applicationData value

        Note:
            Delegates to application_data property (CODING_RULE_V2_00017)
        """
        return self.application_data  # Delegates to property

    def setApplicationData(self, value: "ApplicationDataType") -> "ObdMonitorServiceNeeds":
        """
        AUTOSAR-compliant setter for applicationData with method chaining.

        Args:
            value: The applicationData to set

        Returns:
            self for method chaining

        Note:
            Delegates to application_data property setter (gets validation automatically)
        """
        self.application_data = value  # Delegates to property setter
        return self

    def getEventNeeds(self) -> "DiagnosticEventNeeds":
        """
        AUTOSAR-compliant getter for eventNeeds.

        Returns:
            The eventNeeds value

        Note:
            Delegates to event_needs property (CODING_RULE_V2_00017)
        """
        return self.event_needs  # Delegates to property

    def setEventNeeds(self, value: "DiagnosticEventNeeds") -> "ObdMonitorServiceNeeds":
        """
        AUTOSAR-compliant setter for eventNeeds with method chaining.

        Args:
            value: The eventNeeds to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_needs property setter (gets validation automatically)
        """
        self.event_needs = value  # Delegates to property setter
        return self

    def getUnitAndScalingId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for unitAndScalingId.

        Returns:
            The unitAndScalingId value

        Note:
            Delegates to unit_and_scaling_id property (CODING_RULE_V2_00017)
        """
        return self.unit_and_scaling_id  # Delegates to property

    def setUnitAndScalingId(self, value: "PositiveInteger") -> "ObdMonitorServiceNeeds":
        """
        AUTOSAR-compliant setter for unitAndScalingId with method chaining.

        Args:
            value: The unitAndScalingId to set

        Returns:
            self for method chaining

        Note:
            Delegates to unit_and_scaling_id property setter (gets validation automatically)
        """
        self.unit_and_scaling_id = value  # Delegates to property setter
        return self

    def getUpdateKind(self) -> "DiagnosticMonitor":
        """
        AUTOSAR-compliant getter for updateKind.

        Returns:
            The updateKind value

        Note:
            Delegates to update_kind property (CODING_RULE_V2_00017)
        """
        return self.update_kind  # Delegates to property

    def setUpdateKind(self, value: "DiagnosticMonitor") -> "ObdMonitorServiceNeeds":
        """
        AUTOSAR-compliant setter for updateKind with method chaining.

        Args:
            value: The updateKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to update_kind property setter (gets validation automatically)
        """
        self.update_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application_data(self, value: Optional["ApplicationDataType"]) -> "ObdMonitorServiceNeeds":
        """
        Set applicationData and return self for chaining.

        Args:
            value: The applicationData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application_data("value")
        """
        self.application_data = value  # Use property setter (gets validation)
        return self

    def with_event_needs(self, value: Optional["DiagnosticEventNeeds"]) -> "ObdMonitorServiceNeeds":
        """
        Set eventNeeds and return self for chaining.

        Args:
            value: The eventNeeds to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_needs("value")
        """
        self.event_needs = value  # Use property setter (gets validation)
        return self

    def with_unit_and_scaling_id(self, value: Optional["PositiveInteger"]) -> "ObdMonitorServiceNeeds":
        """
        Set unitAndScalingId and return self for chaining.

        Args:
            value: The unitAndScalingId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unit_and_scaling_id("value")
        """
        self.unit_and_scaling_id = value  # Use property setter (gets validation)
        return self

    def with_update_kind(self, value: Optional["DiagnosticMonitor"]) -> "ObdMonitorServiceNeeds":
        """
        Set updateKind and return self for chaining.

        Args:
            value: The updateKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_update_kind("value")
        """
        self.update_kind = value  # Use property setter (gets validation)
        return self
