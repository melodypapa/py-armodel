from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class SecurityEventContextProps(Identifiable):
    """
    This meta-class specifies the SecurityEventDefinition to be mapped to an
    IdsmInstance and adds mapping-dependent properties of this security event
    valid only for this specific mapping.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 258, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 33, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents the definition of optional data for security
                # events.
        # atpVariation.
        self._contextData: Optional["SecurityEventContext"] = None

    @property
    def context_data(self) -> Optional["SecurityEventContext"]:
        """Get contextData (Pythonic accessor)."""
        return self._contextData

    @context_data.setter
    def context_data(self, value: Optional["SecurityEventContext"]) -> None:
        """
        Set contextData with validation.

        Args:
            value: The contextData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._contextData = None
            return

        if not isinstance(value, SecurityEventContext):
            raise TypeError(
                f"contextData must be SecurityEventContext or None, got {type(value).__name__}"
            )
        self._contextData = value
        # event.
        self._default: Optional["SecurityEventReporting"] = None

    @property
    def default(self) -> Optional["SecurityEventReporting"]:
        """Get default (Pythonic accessor)."""
        return self._default

    @default.setter
    def default(self, value: Optional["SecurityEventReporting"]) -> None:
        """
        Set default with validation.

        Args:
            value: The default to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._default = None
            return

        if not isinstance(value, SecurityEventReporting):
            raise TypeError(
                f"default must be SecurityEventReporting or None, got {type(value).__name__}"
            )
        self._default = value
        # shall be stored persistently by IdsmInstance or not.
        self._persistent: Optional["Boolean"] = None

    @property
    def persistent(self) -> Optional["Boolean"]:
        """Get persistent (Pythonic accessor)."""
        return self._persistent

    @persistent.setter
    def persistent(self, value: Optional["Boolean"]) -> None:
        """
        Set persistent with validation.

        Args:
            value: The persistent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._persistent = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"persistent must be Boolean or None, got {type(value).__name__}"
            )
        self._persistent = value
                # SecurityEventMappingProps with properties.
        # atpVariation.
        self._securityEvent: Optional["SecurityEventDefinition"] = None

    @property
    def security_event(self) -> Optional["SecurityEventDefinition"]:
        """Get securityEvent (Pythonic accessor)."""
        return self._securityEvent

    @security_event.setter
    def security_event(self, value: Optional["SecurityEventDefinition"]) -> None:
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

        if not isinstance(value, SecurityEventDefinition):
            raise TypeError(
                f"securityEvent must be SecurityEventDefinition or None, got {type(value).__name__}"
            )
        self._securityEvent = value
                # security event.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._sensorInstance: Optional["PositiveInteger"] = None

    @property
    def sensor_instance(self) -> Optional["PositiveInteger"]:
        """Get sensorInstance (Pythonic accessor)."""
        return self._sensorInstance

    @sensor_instance.setter
    def sensor_instance(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sensorInstance with validation.

        Args:
            value: The sensorInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sensorInstance = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"sensorInstance must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._sensorInstance = value
        # Please note that currently, the severity of specific integer values is not
                # specified but left to the party responsible for the IDS (e.
        # g.
        # the OEM).
        self._severity: Optional["PositiveInteger"] = None

    @property
    def severity(self) -> Optional["PositiveInteger"]:
        """Get severity (Pythonic accessor)."""
        return self._severity

    @severity.setter
    def severity(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set severity with validation.

        Args:
            value: The severity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._severity = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"severity must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._severity = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContextData(self) -> "SecurityEventContext":
        """
        AUTOSAR-compliant getter for contextData.

        Returns:
            The contextData value

        Note:
            Delegates to context_data property (CODING_RULE_V2_00017)
        """
        return self.context_data  # Delegates to property

    def setContextData(self, value: "SecurityEventContext") -> "SecurityEventContextProps":
        """
        AUTOSAR-compliant setter for contextData with method chaining.

        Args:
            value: The contextData to set

        Returns:
            self for method chaining

        Note:
            Delegates to context_data property setter (gets validation automatically)
        """
        self.context_data = value  # Delegates to property setter
        return self

    def getDefault(self) -> "SecurityEventReporting":
        """
        AUTOSAR-compliant getter for default.

        Returns:
            The default value

        Note:
            Delegates to default property (CODING_RULE_V2_00017)
        """
        return self.default  # Delegates to property

    def setDefault(self, value: "SecurityEventReporting") -> "SecurityEventContextProps":
        """
        AUTOSAR-compliant setter for default with method chaining.

        Args:
            value: The default to set

        Returns:
            self for method chaining

        Note:
            Delegates to default property setter (gets validation automatically)
        """
        self.default = value  # Delegates to property setter
        return self

    def getPersistent(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for persistent.

        Returns:
            The persistent value

        Note:
            Delegates to persistent property (CODING_RULE_V2_00017)
        """
        return self.persistent  # Delegates to property

    def setPersistent(self, value: "Boolean") -> "SecurityEventContextProps":
        """
        AUTOSAR-compliant setter for persistent with method chaining.

        Args:
            value: The persistent to set

        Returns:
            self for method chaining

        Note:
            Delegates to persistent property setter (gets validation automatically)
        """
        self.persistent = value  # Delegates to property setter
        return self

    def getSecurityEvent(self) -> "SecurityEventDefinition":
        """
        AUTOSAR-compliant getter for securityEvent.

        Returns:
            The securityEvent value

        Note:
            Delegates to security_event property (CODING_RULE_V2_00017)
        """
        return self.security_event  # Delegates to property

    def setSecurityEvent(self, value: "SecurityEventDefinition") -> "SecurityEventContextProps":
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

    def getSensorInstance(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sensorInstance.

        Returns:
            The sensorInstance value

        Note:
            Delegates to sensor_instance property (CODING_RULE_V2_00017)
        """
        return self.sensor_instance  # Delegates to property

    def setSensorInstance(self, value: "PositiveInteger") -> "SecurityEventContextProps":
        """
        AUTOSAR-compliant setter for sensorInstance with method chaining.

        Args:
            value: The sensorInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to sensor_instance property setter (gets validation automatically)
        """
        self.sensor_instance = value  # Delegates to property setter
        return self

    def getSeverity(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for severity.

        Returns:
            The severity value

        Note:
            Delegates to severity property (CODING_RULE_V2_00017)
        """
        return self.severity  # Delegates to property

    def setSeverity(self, value: "PositiveInteger") -> "SecurityEventContextProps":
        """
        AUTOSAR-compliant setter for severity with method chaining.

        Args:
            value: The severity to set

        Returns:
            self for method chaining

        Note:
            Delegates to severity property setter (gets validation automatically)
        """
        self.severity = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_data(self, value: Optional["SecurityEventContext"]) -> "SecurityEventContextProps":
        """
        Set contextData and return self for chaining.

        Args:
            value: The contextData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_context_data("value")
        """
        self.context_data = value  # Use property setter (gets validation)
        return self

    def with_default(self, value: Optional["SecurityEventReporting"]) -> "SecurityEventContextProps":
        """
        Set default and return self for chaining.

        Args:
            value: The default to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default("value")
        """
        self.default = value  # Use property setter (gets validation)
        return self

    def with_persistent(self, value: Optional["Boolean"]) -> "SecurityEventContextProps":
        """
        Set persistent and return self for chaining.

        Args:
            value: The persistent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_persistent("value")
        """
        self.persistent = value  # Use property setter (gets validation)
        return self

    def with_security_event(self, value: Optional["SecurityEventDefinition"]) -> "SecurityEventContextProps":
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

    def with_sensor_instance(self, value: Optional["PositiveInteger"]) -> "SecurityEventContextProps":
        """
        Set sensorInstance and return self for chaining.

        Args:
            value: The sensorInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sensor_instance("value")
        """
        self.sensor_instance = value  # Use property setter (gets validation)
        return self

    def with_severity(self, value: Optional["PositiveInteger"]) -> "SecurityEventContextProps":
        """
        Set severity and return self for chaining.

        Args:
            value: The severity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_severity("value")
        """
        self.severity = value  # Use property setter (gets validation)
        return self
