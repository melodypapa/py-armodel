from typing import Optional


class DiagnosticCommunicationManagerNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic
    Communication Manager (Dcm) which are not related to a particular item (e.g.
    a PID or DiagnosticRoutineNeeds). The main use case is the mapping of
    service ports to the Dcm which are not related to a particular item.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticCommunicationManagerNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 248, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 779, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the ability to define whether the usage of PortInterface
        # ServiceRequestNotification has the of being initiated by a manufacturer or by
        # a.
        self._serviceRequest: Optional["DiagnosticService"] = None

    @property
    def service_request(self) -> Optional["DiagnosticService"]:
        """Get serviceRequest (Pythonic accessor)."""
        return self._serviceRequest

    @service_request.setter
    def service_request(self, value: Optional["DiagnosticService"]) -> None:
        """
        Set serviceRequest with validation.

        Args:
            value: The serviceRequest to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceRequest = None
            return

        if not isinstance(value, DiagnosticService):
            raise TypeError(
                f"serviceRequest must be DiagnosticService or None, got {type(value).__name__}"
            )
        self._serviceRequest = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getServiceRequest(self) -> "DiagnosticService":
        """
        AUTOSAR-compliant getter for serviceRequest.

        Returns:
            The serviceRequest value

        Note:
            Delegates to service_request property (CODING_RULE_V2_00017)
        """
        return self.service_request  # Delegates to property

    def setServiceRequest(self, value: "DiagnosticService") -> "DiagnosticCommunicationManagerNeeds":
        """
        AUTOSAR-compliant setter for serviceRequest with method chaining.

        Args:
            value: The serviceRequest to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_request property setter (gets validation automatically)
        """
        self.service_request = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_service_request(self, value: Optional["DiagnosticService"]) -> "DiagnosticCommunicationManagerNeeds":
        """
        Set serviceRequest and return self for chaining.

        Args:
            value: The serviceRequest to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_request("value")
        """
        self.service_request = value  # Use property setter (gets validation)
        return self
