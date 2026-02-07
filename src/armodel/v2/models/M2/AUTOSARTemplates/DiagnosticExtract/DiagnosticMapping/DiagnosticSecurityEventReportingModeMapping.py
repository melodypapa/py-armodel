from typing import Optional


class DiagnosticSecurityEventReportingModeMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to associate a location in a DID with
    a security event. The purpose of this mapping is that the location in the
    DID contains the setting of the reporting mode for the specific security
    event. This means that the reporting mode of the security event can be set
    via the diagnostic service WriteDataByIdentifier.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::ServiceMapping::DiagnosticSecurityEventReportingModeMapping

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 243, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the data element that carries the the reporting
        # mode.
        self._dataElement: Optional["DiagnosticDataElement"] = None

    @property
    def data_element(self) -> Optional["DiagnosticDataElement"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional["DiagnosticDataElement"]) -> None:
        """
        Set dataElement with validation.

        Args:
            value: The dataElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        if not isinstance(value, DiagnosticDataElement):
            raise TypeError(
                f"dataElement must be DiagnosticDataElement or None, got {type(value).__name__}"
            )
        self._dataElement = value
        # This reference identifies the mapped security event.
        # atp.
        # Status=candidate.
        self._securityEvent: Optional["SecurityEventContext"] = None

    @property
    def security_event(self) -> Optional["SecurityEventContext"]:
        """Get securityEvent (Pythonic accessor)."""
        return self._securityEvent

    @security_event.setter
    def security_event(self, value: Optional["SecurityEventContext"]) -> None:
        """
        Set securityEvent with validation.

        Args:
            value: The securityEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._securityEvent = None
            return

        if not isinstance(value, SecurityEventContext):
            raise TypeError(
                f"securityEvent must be SecurityEventContext or None, got {type(value).__name__}"
            )
        self._securityEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> "DiagnosticDataElement":
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: "DiagnosticDataElement") -> "DiagnosticSecurityEventReportingModeMapping":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getSecurityEvent(self) -> "SecurityEventContext":
        """
        AUTOSAR-compliant getter for securityEvent.

        Returns:
            The securityEvent value

        Note:
            Delegates to security_event property (CODING_RULE_V2_00017)
        """
        return self.security_event  # Delegates to property

    def setSecurityEvent(self, value: "SecurityEventContext") -> "DiagnosticSecurityEventReportingModeMapping":
        """
        AUTOSAR-compliant setter for securityEvent with method chaining.

        Args:
            value: The securityEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to security_event property setter (gets validation automatically)
        """
        self.security_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element(self, value: Optional["DiagnosticDataElement"]) -> "DiagnosticSecurityEventReportingModeMapping":
        """
        Set dataElement and return self for chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_security_event(self, value: Optional["SecurityEventContext"]) -> "DiagnosticSecurityEventReportingModeMapping":
        """
        Set securityEvent and return self for chaining.

        Args:
            value: The securityEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_security_event("value")
        """
        self.security_event = value  # Use property setter (gets validation)
        return self
