"""
AUTOSAR Package - SecurityExtractTemplate

Package: M2::AUTOSARTemplates::SecurityExtractTemplate
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    PositiveInteger,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class SecurityEventContextProps(Identifiable):
    """
    This meta-class specifies the SecurityEventDefinition to be mapped to an
    IdsmInstance and adds mapping-dependent properties of this security event
    valid only for this specific mapping.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventContextProps

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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"persistent must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._persistent = value
                # SecurityEventMappingProps with properties.
        # atpVariation.
        self._securityEvent: Optional[SecurityEventDefinition] = None

    @property
    def security_event(self) -> Optional[SecurityEventDefinition]:
        """Get securityEvent (Pythonic accessor)."""
        return self._securityEvent

    @security_event.setter
    def security_event(self, value: Optional[SecurityEventDefinition]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sensorInstance must be PositiveInteger or str or None, got {type(value).__name__}"
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"severity must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._severity = value

    def with_element(self, value):
        """
        Set element and return self for chaining.

        Args:
            value: The element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_element("value")
        """
        self.element = value  # Use property setter (gets validation)
        return self

    def with_block_if_state(self, value):
        """
        Set block_if_state and return self for chaining.

        Args:
            value: The block_if_state to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_block_if_state("value")
        """
        self.block_if_state = value  # Use property setter (gets validation)
        return self

    def with_block_state(self, value):
        """
        Set block_state and return self for chaining.

        Args:
            value: The block_state to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_block_state("value")
        """
        self.block_state = value  # Use property setter (gets validation)
        return self

    def with_mapped_security(self, value):
        """
        Set mapped_security and return self for chaining.

        Args:
            value: The mapped_security to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapped_security("value")
        """
        self.mapped_security = value  # Use property setter (gets validation)
        return self

    def with_comm(self, value):
        """
        Set comm and return self for chaining.

        Args:
            value: The comm to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_comm("value")
        """
        self.comm = value  # Use property setter (gets validation)
        return self

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

    def setContextData(self, value: "SecurityEventContext") -> SecurityEventContextProps:
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

    def setDefault(self, value: "SecurityEventReporting") -> SecurityEventContextProps:
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

    def setPersistent(self, value: "Boolean") -> SecurityEventContextProps:
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

    def getSecurityEvent(self) -> SecurityEventDefinition:
        """
        AUTOSAR-compliant getter for securityEvent.

        Returns:
            The securityEvent value

        Note:
            Delegates to security_event property (CODING_RULE_V2_00017)
        """
        return self.security_event  # Delegates to property

    def setSecurityEvent(self, value: SecurityEventDefinition) -> SecurityEventContextProps:
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

    def setSensorInstance(self, value: "PositiveInteger") -> SecurityEventContextProps:
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

    def setSeverity(self, value: "PositiveInteger") -> SecurityEventContextProps:
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

    def with_context_data(self, value: Optional["SecurityEventContext"]) -> SecurityEventContextProps:
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

    def with_default(self, value: Optional["SecurityEventReporting"]) -> SecurityEventContextProps:
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

    def with_persistent(self, value: Optional["Boolean"]) -> SecurityEventContextProps:
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

    def with_security_event(self, value: Optional[SecurityEventDefinition]) -> SecurityEventContextProps:
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

    def with_sensor_instance(self, value: Optional["PositiveInteger"]) -> SecurityEventContextProps:
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

    def with_severity(self, value: Optional["PositiveInteger"]) -> SecurityEventContextProps:
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



class IdsDesign(ARElement):
    """
    This meta-class represents the root element of a SecurityExtract file for
    IDS development. It defines the scope of an IDS to be designed and
    implemented by referencing all SecurityExtract meta-classes that need to be
    included into the IDS development process.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsDesign

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 16, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference includes an element with IDS related the IdsDesign.
        # atpVariation.
        self._element: List[IdsCommonElement] = []

    @property
    def element(self) -> List[IdsCommonElement]:
        """Get element (Pythonic accessor)."""
        return self._element

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getElement(self) -> List[IdsCommonElement]:
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AbstractSecurityEventFilter(Identifiable, ABC):
    """
    This meta-class acts as a base class for security event filters.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::AbstractSecurityEventFilter

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 21, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AbstractSecurityEventFilter:
            raise TypeError("AbstractSecurityEventFilter is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class IdsmRateLimitation(Identifiable):
    """
    This meta-class represents the configuration of a rate limitation filter for
    security events. This means that security events are dropped if the number
    of events (of any type) processed within a configurable time window is
    greater than a configurable threshold.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsmRateLimitation

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 28, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute configures the threshold for dropping events if the number of
        # all processed security the threshold in the respective time.
        self._maxEventsIn: "PositiveInteger" = None

    @property
    def max_events_in(self) -> "PositiveInteger":
        """Get maxEventsIn (Pythonic accessor)."""
        return self._maxEventsIn

    @max_events_in.setter
    def max_events_in(self, value: "PositiveInteger") -> None:
        """
        Set maxEventsIn with validation.

        Args:
            value: The maxEventsIn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxEventsIn must be PositiveInteger or str, got {type(value).__name__}"
            )
        self._maxEventsIn = value
        # security events if the number of all events exceeds the configurable the
        # respective time interval.
        self._timeInterval: "Float" = None

    @property
    def time_interval(self) -> "Float":
        """Get timeInterval (Pythonic accessor)."""
        return self._timeInterval

    @time_interval.setter
    def time_interval(self, value: "Float") -> None:
        """
        Set timeInterval with validation.

        Args:
            value: The timeInterval to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"timeInterval must be Float or float, got {type(value).__name__}"
            )
        self._timeInterval = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxEventsIn(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxEventsIn.

        Returns:
            The maxEventsIn value

        Note:
            Delegates to max_events_in property (CODING_RULE_V2_00017)
        """
        return self.max_events_in  # Delegates to property

    def setMaxEventsIn(self, value: "PositiveInteger") -> IdsmRateLimitation:
        """
        AUTOSAR-compliant setter for maxEventsIn with method chaining.

        Args:
            value: The maxEventsIn to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_events_in property setter (gets validation automatically)
        """
        self.max_events_in = value  # Delegates to property setter
        return self

    def getTimeInterval(self) -> "Float":
        """
        AUTOSAR-compliant getter for timeInterval.

        Returns:
            The timeInterval value

        Note:
            Delegates to time_interval property (CODING_RULE_V2_00017)
        """
        return self.time_interval  # Delegates to property

    def setTimeInterval(self, value: "Float") -> IdsmRateLimitation:
        """
        AUTOSAR-compliant setter for timeInterval with method chaining.

        Args:
            value: The timeInterval to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_interval property setter (gets validation automatically)
        """
        self.time_interval = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_events_in(self, value: "PositiveInteger") -> IdsmRateLimitation:
        """
        Set maxEventsIn and return self for chaining.

        Args:
            value: The maxEventsIn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_events_in("value")
        """
        self.max_events_in = value  # Use property setter (gets validation)
        return self

    def with_time_interval(self, value: "Float") -> IdsmRateLimitation:
        """
        Set timeInterval and return self for chaining.

        Args:
            value: The timeInterval to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_interval("value")
        """
        self.time_interval = value  # Use property setter (gets validation)
        return self



class IdsmTrafficLimitation(Identifiable):
    """
    This meta-class represents the configuration of a traffic limitation filter
    for Security Events. This means that security events are dropped if the size
    (in terms of bandwidth) of security events (of any type) processed within a
    configurable time window is greater than a configurable threshold.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsmTrafficLimitation

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 28, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute configures the threshold for dropping events if the size of
        # all processed security events threshold in the respective time interval.
        self._maxBytesIn: Optional["PositiveInteger"] = None

    @property
    def max_bytes_in(self) -> Optional["PositiveInteger"]:
        """Get maxBytesIn (Pythonic accessor)."""
        return self._maxBytesIn

    @max_bytes_in.setter
    def max_bytes_in(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxBytesIn with validation.

        Args:
            value: The maxBytesIn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxBytesIn = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxBytesIn must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxBytesIn = value
        # security events if the size of all events exceeds the configurable the
        # respective time interval.
        self._timeInterval: Optional["Float"] = None

    @property
    def time_interval(self) -> Optional["Float"]:
        """Get timeInterval (Pythonic accessor)."""
        return self._timeInterval

    @time_interval.setter
    def time_interval(self, value: Optional["Float"]) -> None:
        """
        Set timeInterval with validation.

        Args:
            value: The timeInterval to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeInterval = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"timeInterval must be Float or float or None, got {type(value).__name__}"
            )
        self._timeInterval = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxBytesIn(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxBytesIn.

        Returns:
            The maxBytesIn value

        Note:
            Delegates to max_bytes_in property (CODING_RULE_V2_00017)
        """
        return self.max_bytes_in  # Delegates to property

    def setMaxBytesIn(self, value: "PositiveInteger") -> IdsmTrafficLimitation:
        """
        AUTOSAR-compliant setter for maxBytesIn with method chaining.

        Args:
            value: The maxBytesIn to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_bytes_in property setter (gets validation automatically)
        """
        self.max_bytes_in = value  # Delegates to property setter
        return self

    def getTimeInterval(self) -> "Float":
        """
        AUTOSAR-compliant getter for timeInterval.

        Returns:
            The timeInterval value

        Note:
            Delegates to time_interval property (CODING_RULE_V2_00017)
        """
        return self.time_interval  # Delegates to property

    def setTimeInterval(self, value: "Float") -> IdsmTrafficLimitation:
        """
        AUTOSAR-compliant setter for timeInterval with method chaining.

        Args:
            value: The timeInterval to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_interval property setter (gets validation automatically)
        """
        self.time_interval = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_bytes_in(self, value: Optional["PositiveInteger"]) -> IdsmTrafficLimitation:
        """
        Set maxBytesIn and return self for chaining.

        Args:
            value: The maxBytesIn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_bytes_in("value")
        """
        self.max_bytes_in = value  # Use property setter (gets validation)
        return self

    def with_time_interval(self, value: Optional["Float"]) -> IdsmTrafficLimitation:
        """
        Set timeInterval and return self for chaining.

        Args:
            value: The timeInterval to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_interval("value")
        """
        self.time_interval = value  # Use property setter (gets validation)
        return self



class BlockState(Identifiable):
    """
    This meta-class defines a block state that is part of the collection of
    block states belonging to a specific IdsmInstance. The IdsM shall discard
    any reported security event that is mapped to a filter chain containing a
    SecurityEventStateFilter that references the block state which is currently
    active in the IdsM.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::BlockState

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 52, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class IdsCommonElement(ARElement, ABC):
    """
    This meta-class represents a common base class for IDS related elements of
    the Security Extract. It does not contribute any specific functionality
    other than the ability to become the target of a reference.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsCommonElement

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 62, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is IdsCommonElement:
            raise TypeError("IdsCommonElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class IdsmSignatureSupportAp(ARObject):
    """
    This meta-class defines, for the Adaptive Platform, the cryptographic
    algorithm and key to be used by the IdsM instance for providing signature
    information in QSEv messages.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsmSignatureSupportAp

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 64, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the cryptographic algorithm to be providing
        # authentication information in QSEv content of this attribute shall comply to
        # Primitives Naming Convention".
        self._cryptoPrimitive: "String" = None

    @property
    def crypto_primitive(self) -> "String":
        """Get cryptoPrimitive (Pythonic accessor)."""
        return self._cryptoPrimitive

    @crypto_primitive.setter
    def crypto_primitive(self, value: "String") -> None:
        """
        Set cryptoPrimitive with validation.

        Args:
            value: The cryptoPrimitive to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"cryptoPrimitive must be String or str, got {type(value).__name__}"
            )
        self._cryptoPrimitive = value
        # algorithm for providing in QSEv messages.
        self._keySlot: Optional["CryptoKeySlot"] = None

    @property
    def key_slot(self) -> Optional["CryptoKeySlot"]:
        """Get keySlot (Pythonic accessor)."""
        return self._keySlot

    @key_slot.setter
    def key_slot(self, value: Optional["CryptoKeySlot"]) -> None:
        """
        Set keySlot with validation.

        Args:
            value: The keySlot to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keySlot = None
            return

        if not isinstance(value, CryptoKeySlot):
            raise TypeError(
                f"keySlot must be CryptoKeySlot or None, got {type(value).__name__}"
            )
        self._keySlot = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCryptoPrimitive(self) -> "String":
        """
        AUTOSAR-compliant getter for cryptoPrimitive.

        Returns:
            The cryptoPrimitive value

        Note:
            Delegates to crypto_primitive property (CODING_RULE_V2_00017)
        """
        return self.crypto_primitive  # Delegates to property

    def setCryptoPrimitive(self, value: "String") -> IdsmSignatureSupportAp:
        """
        AUTOSAR-compliant setter for cryptoPrimitive with method chaining.

        Args:
            value: The cryptoPrimitive to set

        Returns:
            self for method chaining

        Note:
            Delegates to crypto_primitive property setter (gets validation automatically)
        """
        self.crypto_primitive = value  # Delegates to property setter
        return self

    def getKeySlot(self) -> "CryptoKeySlot":
        """
        AUTOSAR-compliant getter for keySlot.

        Returns:
            The keySlot value

        Note:
            Delegates to key_slot property (CODING_RULE_V2_00017)
        """
        return self.key_slot  # Delegates to property

    def setKeySlot(self, value: "CryptoKeySlot") -> IdsmSignatureSupportAp:
        """
        AUTOSAR-compliant setter for keySlot with method chaining.

        Args:
            value: The keySlot to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_slot property setter (gets validation automatically)
        """
        self.key_slot = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_crypto_primitive(self, value: "String") -> IdsmSignatureSupportAp:
        """
        Set cryptoPrimitive and return self for chaining.

        Args:
            value: The cryptoPrimitive to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crypto_primitive("value")
        """
        self.crypto_primitive = value  # Use property setter (gets validation)
        return self

    def with_key_slot(self, value: Optional["CryptoKeySlot"]) -> IdsmSignatureSupportAp:
        """
        Set keySlot and return self for chaining.

        Args:
            value: The keySlot to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_slot("value")
        """
        self.key_slot = value  # Use property setter (gets validation)
        return self



class IdsmSignatureSupportCp(ARObject):
    """
    This meta-class defines, for the Classic Platform, the cryptographic
    algorithm and key to be used by the IdsM instance for providing signature
    information in QSEv messages.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsmSignatureSupportCp

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 64, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference dennotes the cryptographic primitives for information in QSEv
        # messages.
        self._authentication: Optional["CryptoServicePrimitive"] = None

    @property
    def authentication(self) -> Optional["CryptoServicePrimitive"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    @authentication.setter
    def authentication(self, value: Optional["CryptoServicePrimitive"]) -> None:
        """
        Set authentication with validation.

        Args:
            value: The authentication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._authentication = None
            return

        if not isinstance(value, CryptoServicePrimitive):
            raise TypeError(
                f"authentication must be CryptoServicePrimitive or None, got {type(value).__name__}"
            )
        self._authentication = value
        # algorithm for providing in QSEv messages.
        self._cryptoService: Optional["CryptoServiceKey"] = None

    @property
    def crypto_service(self) -> Optional["CryptoServiceKey"]:
        """Get cryptoService (Pythonic accessor)."""
        return self._cryptoService

    @crypto_service.setter
    def crypto_service(self, value: Optional["CryptoServiceKey"]) -> None:
        """
        Set cryptoService with validation.

        Args:
            value: The cryptoService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cryptoService = None
            return

        if not isinstance(value, CryptoServiceKey):
            raise TypeError(
                f"cryptoService must be CryptoServiceKey or None, got {type(value).__name__}"
            )
        self._cryptoService = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> "CryptoServicePrimitive":
        """
        AUTOSAR-compliant getter for authentication.

        Returns:
            The authentication value

        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def setAuthentication(self, value: "CryptoServicePrimitive") -> IdsmSignatureSupportCp:
        """
        AUTOSAR-compliant setter for authentication with method chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Note:
            Delegates to authentication property setter (gets validation automatically)
        """
        self.authentication = value  # Delegates to property setter
        return self

    def getCryptoService(self) -> "CryptoServiceKey":
        """
        AUTOSAR-compliant getter for cryptoService.

        Returns:
            The cryptoService value

        Note:
            Delegates to crypto_service property (CODING_RULE_V2_00017)
        """
        return self.crypto_service  # Delegates to property

    def setCryptoService(self, value: "CryptoServiceKey") -> IdsmSignatureSupportCp:
        """
        AUTOSAR-compliant setter for cryptoService with method chaining.

        Args:
            value: The cryptoService to set

        Returns:
            self for method chaining

        Note:
            Delegates to crypto_service property setter (gets validation automatically)
        """
        self.crypto_service = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_authentication(self, value: Optional["CryptoServicePrimitive"]) -> IdsmSignatureSupportCp:
        """
        Set authentication and return self for chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_authentication("value")
        """
        self.authentication = value  # Use property setter (gets validation)
        return self

    def with_crypto_service(self, value: Optional["CryptoServiceKey"]) -> IdsmSignatureSupportCp:
        """
        Set cryptoService and return self for chaining.

        Args:
            value: The cryptoService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crypto_service("value")
        """
        self.crypto_service = value  # Use property setter (gets validation)
        return self



class SecurityEventContextData(ARObject):
    """
    This meta-class represents the possibility that context data can be attached
    to the aggregating Security EventDefinition. If this meta-class does not
    exist for a SecurityEventDefinition, then no context data shall be provided
    for this SecurityEventDefinition.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventContextData

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 66, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SecurityEventStateFilter(AbstractSecurityEventFilter):
    """
    This meta-class represents the configuration of a state filter for security
    events. The referenced states represent a block list, i.e. the security
    events are dropped if the referenced state is the active state in the
    relevant state machine (which depends on whether the IdsM instance runs on
    the Classic or the Adaptive Platform).

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventStateFilter

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 22, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # For the CP, this reference defines the states of the block That means, if a
        # security event (mapped to the filter which the SecurityEventStateFilter
        # belongs to) is the currently active block state in the IdsM of the referenced
        # block listed states, the IdsM shall reported security event.
        self._blockIfState: List[BlockState] = []

    @property
    def block_if_state(self) -> List[BlockState]:
        """Get blockIfState (Pythonic accessor)."""
        return self._blockIfState

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlockIfState(self) -> List[BlockState]:
        """
        AUTOSAR-compliant getter for blockIfState.

        Returns:
            The blockIfState value

        Note:
            Delegates to block_if_state property (CODING_RULE_V2_00017)
        """
        return self.block_if_state  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SecurityEventOneEveryNFilter(AbstractSecurityEventFilter):
    """
    This meta-class represents the configuration of a sampling (i.e. every n-th
    event is sampled) filter for security events.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventOneEveryNFilter

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 24, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the configuration of the sampling it configures the
        # parameter "n" that controls how (n-1) shall be dropped after a sampled event
        # new sample is created.
        self._n: Optional["PositiveInteger"] = None

    @property
    def n(self) -> Optional["PositiveInteger"]:
        """Get n (Pythonic accessor)."""
        return self._n

    @n.setter
    def n(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set n with validation.

        Args:
            value: The n to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._n = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"n must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._n = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getN(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for n.

        Returns:
            The n value

        Note:
            Delegates to n property (CODING_RULE_V2_00017)
        """
        return self.n  # Delegates to property

    def setN(self, value: "PositiveInteger") -> SecurityEventOneEveryNFilter:
        """
        AUTOSAR-compliant setter for n with method chaining.

        Args:
            value: The n to set

        Returns:
            self for method chaining

        Note:
            Delegates to n property setter (gets validation automatically)
        """
        self.n = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_n(self, value: Optional["PositiveInteger"]) -> SecurityEventOneEveryNFilter:
        """
        Set n and return self for chaining.

        Args:
            value: The n to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_n("value")
        """
        self.n = value  # Use property setter (gets validation)
        return self



class SecurityEventAggregationFilter(AbstractSecurityEventFilter):
    """
    This meta-class represents the aggregation filter that aggregates all
    security events occurring within a configured time frame into one (i.e. the
    last reported) security event.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventAggregationFilter

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 24, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attributes defines whether the context data of the first or last
        # time-aggregated security event shall be used for qualified security event.
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
        # for the aggregation filter.
        self._minimum: Optional["TimeValue"] = None

    @property
    def minimum(self) -> Optional["TimeValue"]:
        """Get minimum (Pythonic accessor)."""
        return self._minimum

    @minimum.setter
    def minimum(self, value: Optional["TimeValue"]) -> None:
        """
        Set minimum with validation.

        Args:
            value: The minimum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimum = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minimum must be TimeValue or None, got {type(value).__name__}"
            )
        self._minimum = value

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

    def setContextData(self, value: "SecurityEventContext") -> SecurityEventAggregationFilter:
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

    def getMinimum(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minimum.

        Returns:
            The minimum value

        Note:
            Delegates to minimum property (CODING_RULE_V2_00017)
        """
        return self.minimum  # Delegates to property

    def setMinimum(self, value: "TimeValue") -> SecurityEventAggregationFilter:
        """
        AUTOSAR-compliant setter for minimum with method chaining.

        Args:
            value: The minimum to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum property setter (gets validation automatically)
        """
        self.minimum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_context_data(self, value: Optional["SecurityEventContext"]) -> SecurityEventAggregationFilter:
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

    def with_minimum(self, value: Optional["TimeValue"]) -> SecurityEventAggregationFilter:
        """
        Set minimum and return self for chaining.

        Args:
            value: The minimum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum("value")
        """
        self.minimum = value  # Use property setter (gets validation)
        return self



class SecurityEventThresholdFilter(AbstractSecurityEventFilter):
    """
    This meta-class represents the threshold filter that drops (repeatedly at
    each beginning of a configurable time interval) a configurable number of
    security events . All subsequently arriving security events (within the
    configured time interval) pass the filter.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventThresholdFilter

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 26, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute configures the time interval in seconds for filter operation.
        self._intervalLength: Optional["TimeValue"] = None

    @property
    def interval_length(self) -> Optional["TimeValue"]:
        """Get intervalLength (Pythonic accessor)."""
        return self._intervalLength

    @interval_length.setter
    def interval_length(self, value: Optional["TimeValue"]) -> None:
        """
        Set intervalLength with validation.

        Args:
            value: The intervalLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._intervalLength = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"intervalLength must be TimeValue or None, got {type(value).__name__}"
            )
        self._intervalLength = value
        # e.
        # how security events in the configured time frame are subsequent events start
                # to pass the filter.
        self._threshold: Optional["PositiveInteger"] = None

    @property
    def threshold(self) -> Optional["PositiveInteger"]:
        """Get threshold (Pythonic accessor)."""
        return self._threshold

    @threshold.setter
    def threshold(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set threshold with validation.

        Args:
            value: The threshold to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._threshold = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"threshold must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._threshold = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIntervalLength(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for intervalLength.

        Returns:
            The intervalLength value

        Note:
            Delegates to interval_length property (CODING_RULE_V2_00017)
        """
        return self.interval_length  # Delegates to property

    def setIntervalLength(self, value: "TimeValue") -> SecurityEventThresholdFilter:
        """
        AUTOSAR-compliant setter for intervalLength with method chaining.

        Args:
            value: The intervalLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to interval_length property setter (gets validation automatically)
        """
        self.interval_length = value  # Delegates to property setter
        return self

    def getThreshold(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for threshold.

        Returns:
            The threshold value

        Note:
            Delegates to threshold property (CODING_RULE_V2_00017)
        """
        return self.threshold  # Delegates to property

    def setThreshold(self, value: "PositiveInteger") -> SecurityEventThresholdFilter:
        """
        AUTOSAR-compliant setter for threshold with method chaining.

        Args:
            value: The threshold to set

        Returns:
            self for method chaining

        Note:
            Delegates to threshold property setter (gets validation automatically)
        """
        self.threshold = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_interval_length(self, value: Optional["TimeValue"]) -> SecurityEventThresholdFilter:
        """
        Set intervalLength and return self for chaining.

        Args:
            value: The intervalLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_interval_length("value")
        """
        self.interval_length = value  # Use property setter (gets validation)
        return self

    def with_threshold(self, value: Optional["PositiveInteger"]) -> SecurityEventThresholdFilter:
        """
        Set threshold and return self for chaining.

        Args:
            value: The threshold to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_threshold("value")
        """
        self.threshold = value  # Use property setter (gets validation)
        return self



class SecurityEventDefinition(IdsCommonElement):
    """
    This meta-class defines a security-related event as part of the intrusion
    detection system.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventDefinition

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 259, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 17, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation defines optionally an alternative Event for the
        # SecurityEventDefinition in case there is a shortNames.
        self._eventSymbol: Optional["SymbolProps"] = None

    @property
    def event_symbol(self) -> Optional["SymbolProps"]:
        """Get eventSymbol (Pythonic accessor)."""
        return self._eventSymbol

    @event_symbol.setter
    def event_symbol(self, value: Optional["SymbolProps"]) -> None:
        """
        Set eventSymbol with validation.

        Args:
            value: The eventSymbol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventSymbol = None
            return

        if not isinstance(value, SymbolProps):
            raise TypeError(
                f"eventSymbol must be SymbolProps or None, got {type(value).__name__}"
            )
        self._eventSymbol = value
        # The identification shall be the scope of the IDS.
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"id must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._id = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventSymbol(self) -> "SymbolProps":
        """
        AUTOSAR-compliant getter for eventSymbol.

        Returns:
            The eventSymbol value

        Note:
            Delegates to event_symbol property (CODING_RULE_V2_00017)
        """
        return self.event_symbol  # Delegates to property

    def setEventSymbol(self, value: "SymbolProps") -> SecurityEventDefinition:
        """
        AUTOSAR-compliant setter for eventSymbol with method chaining.

        Args:
            value: The eventSymbol to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_symbol property setter (gets validation automatically)
        """
        self.event_symbol = value  # Delegates to property setter
        return self

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> SecurityEventDefinition:
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_symbol(self, value: Optional["SymbolProps"]) -> SecurityEventDefinition:
        """
        Set eventSymbol and return self for chaining.

        Args:
            value: The eventSymbol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_symbol("value")
        """
        self.event_symbol = value  # Use property setter (gets validation)
        return self

    def with_id(self, value: Optional["PositiveInteger"]) -> SecurityEventDefinition:
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self



class SecurityEventFilterChain(IdsCommonElement):
    """
    This meta-class represents a configurable chain of filters used to qualify
    security events. The different filters of this filter chain are applied in
    the follow order: SecurityEventStateFilter, SecurityEventOneEvery NFilter,
    SecurityEventAggregationFilter, SecurityEventThresholdFilter.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventFilterChain

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 20, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents the aggregation filter in the chain.
        self._aggregation: Optional["SecurityEvent"] = None

    @property
    def aggregation(self) -> Optional["SecurityEvent"]:
        """Get aggregation (Pythonic accessor)."""
        return self._aggregation

    @aggregation.setter
    def aggregation(self, value: Optional["SecurityEvent"]) -> None:
        """
        Set aggregation with validation.

        Args:
            value: The aggregation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aggregation = None
            return

        if not isinstance(value, SecurityEvent):
            raise TypeError(
                f"aggregation must be SecurityEvent or None, got {type(value).__name__}"
            )
        self._aggregation = value
        self._oneEveryN: Optional["SecurityEventOneEvery"] = None

    @property
    def one_every_n(self) -> Optional["SecurityEventOneEvery"]:
        """Get oneEveryN (Pythonic accessor)."""
        return self._oneEveryN

    @one_every_n.setter
    def one_every_n(self, value: Optional["SecurityEventOneEvery"]) -> None:
        """
        Set oneEveryN with validation.

        Args:
            value: The oneEveryN to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._oneEveryN = None
            return

        if not isinstance(value, SecurityEventOneEvery):
            raise TypeError(
                f"oneEveryN must be SecurityEventOneEvery or None, got {type(value).__name__}"
            )
        self._oneEveryN = value
        # AUTOSAR_FO_TPS_SecurityExtractTemplate Template R23-11.
        self._state: Optional[SecurityEventStateFilter] = None

    @property
    def state(self) -> Optional[SecurityEventStateFilter]:
        """Get state (Pythonic accessor)."""
        return self._state

    @state.setter
    def state(self, value: Optional[SecurityEventStateFilter]) -> None:
        """
        Set state with validation.

        Args:
            value: The state to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._state = None
            return

        if not isinstance(value, SecurityEventStateFilter):
            raise TypeError(
                f"state must be SecurityEventStateFilter or None, got {type(value).__name__}"
            )
        self._state = value
        self._threshold: Optional["SecurityEventThreshold"] = None

    @property
    def threshold(self) -> Optional["SecurityEventThreshold"]:
        """Get threshold (Pythonic accessor)."""
        return self._threshold

    @threshold.setter
    def threshold(self, value: Optional["SecurityEventThreshold"]) -> None:
        """
        Set threshold with validation.

        Args:
            value: The threshold to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._threshold = None
            return

        if not isinstance(value, SecurityEventThreshold):
            raise TypeError(
                f"threshold must be SecurityEventThreshold or None, got {type(value).__name__}"
            )
        self._threshold = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAggregation(self) -> "SecurityEvent":
        """
        AUTOSAR-compliant getter for aggregation.

        Returns:
            The aggregation value

        Note:
            Delegates to aggregation property (CODING_RULE_V2_00017)
        """
        return self.aggregation  # Delegates to property

    def setAggregation(self, value: "SecurityEvent") -> SecurityEventFilterChain:
        """
        AUTOSAR-compliant setter for aggregation with method chaining.

        Args:
            value: The aggregation to set

        Returns:
            self for method chaining

        Note:
            Delegates to aggregation property setter (gets validation automatically)
        """
        self.aggregation = value  # Delegates to property setter
        return self

    def getOneEveryN(self) -> "SecurityEventOneEvery":
        """
        AUTOSAR-compliant getter for oneEveryN.

        Returns:
            The oneEveryN value

        Note:
            Delegates to one_every_n property (CODING_RULE_V2_00017)
        """
        return self.one_every_n  # Delegates to property

    def setOneEveryN(self, value: "SecurityEventOneEvery") -> SecurityEventFilterChain:
        """
        AUTOSAR-compliant setter for oneEveryN with method chaining.

        Args:
            value: The oneEveryN to set

        Returns:
            self for method chaining

        Note:
            Delegates to one_every_n property setter (gets validation automatically)
        """
        self.one_every_n = value  # Delegates to property setter
        return self

    def getState(self) -> SecurityEventStateFilter:
        """
        AUTOSAR-compliant getter for state.

        Returns:
            The state value

        Note:
            Delegates to state property (CODING_RULE_V2_00017)
        """
        return self.state  # Delegates to property

    def setState(self, value: SecurityEventStateFilter) -> SecurityEventFilterChain:
        """
        AUTOSAR-compliant setter for state with method chaining.

        Args:
            value: The state to set

        Returns:
            self for method chaining

        Note:
            Delegates to state property setter (gets validation automatically)
        """
        self.state = value  # Delegates to property setter
        return self

    def getThreshold(self) -> "SecurityEventThreshold":
        """
        AUTOSAR-compliant getter for threshold.

        Returns:
            The threshold value

        Note:
            Delegates to threshold property (CODING_RULE_V2_00017)
        """
        return self.threshold  # Delegates to property

    def setThreshold(self, value: "SecurityEventThreshold") -> SecurityEventFilterChain:
        """
        AUTOSAR-compliant setter for threshold with method chaining.

        Args:
            value: The threshold to set

        Returns:
            self for method chaining

        Note:
            Delegates to threshold property setter (gets validation automatically)
        """
        self.threshold = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_aggregation(self, value: Optional["SecurityEvent"]) -> SecurityEventFilterChain:
        """
        Set aggregation and return self for chaining.

        Args:
            value: The aggregation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_aggregation("value")
        """
        self.aggregation = value  # Use property setter (gets validation)
        return self

    def with_one_every_n(self, value: Optional["SecurityEventOneEvery"]) -> SecurityEventFilterChain:
        """
        Set oneEveryN and return self for chaining.

        Args:
            value: The oneEveryN to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_one_every_n("value")
        """
        self.one_every_n = value  # Use property setter (gets validation)
        return self

    def with_state(self, value: Optional[SecurityEventStateFilter]) -> SecurityEventFilterChain:
        """
        Set state and return self for chaining.

        Args:
            value: The state to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_state("value")
        """
        self.state = value  # Use property setter (gets validation)
        return self

    def with_threshold(self, value: Optional["SecurityEventThreshold"]) -> SecurityEventFilterChain:
        """
        Set threshold and return self for chaining.

        Args:
            value: The threshold to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_threshold("value")
        """
        self.threshold = value  # Use property setter (gets validation)
        return self



class IdsmInstance(IdsCommonElement):
    """
    This meta-class provides the ability to create a relation between an
    EcuInstance and a specific class of filters for security events that apply
    for all security events reported on the referenced EcuInstance.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsmInstance

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 44, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference defines the BlockState in the collection.
        self._blockState: List[BlockState] = []

    @property
    def block_state(self) -> List[BlockState]:
        """Get blockState (Pythonic accessor)."""
        return self._blockState
        # This reference identifies the EcuInstance whose security any type) shall be
        # limited by the specific class atpVariation.
        self._ecuInstance: Optional["EcuInstance"] = None

    @property
    def ecu_instance(self) -> Optional["EcuInstance"]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional["EcuInstance"]) -> None:
        """
        Set ecuInstance with validation.

        Args:
            value: The ecuInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuInstance = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"ecuInstance must be EcuInstance or None, got {type(value).__name__}"
            )
        self._ecuInstance = value
        # security events.
        self._idsmInstanceId: Optional["PositiveInteger"] = None

    @property
    def idsm_instance_id(self) -> Optional["PositiveInteger"]:
        """Get idsmInstanceId (Pythonic accessor)."""
        return self._idsmInstanceId

    @idsm_instance_id.setter
    def idsm_instance_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set idsmInstanceId with validation.

        Args:
            value: The idsmInstanceId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._idsmInstanceId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"idsmInstanceId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._idsmInstanceId = value
        # IdsM configuration on a specific.
        self._idsmModule: Optional["IdsmModule"] = None

    @property
    def idsm_module(self) -> Optional["IdsmModule"]:
        """Get idsmModule (Pythonic accessor)."""
        return self._idsmModule

    @idsm_module.setter
    def idsm_module(self, value: Optional["IdsmModule"]) -> None:
        """
        Set idsmModule with validation.

        Args:
            value: The idsmModule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._idsmModule = None
            return

        if not isinstance(value, IdsmModule):
            raise TypeError(
                f"idsmModule must be IdsmModule or None, got {type(value).__name__}"
            )
        self._idsmModule = value
                # events on the related EcuInstance.
        # atpVariation.
        self._rateLimitation: Optional[IdsmRateLimitation] = None

    @property
    def rate_limitation(self) -> Optional[IdsmRateLimitation]:
        """Get rateLimitation (Pythonic accessor)."""
        return self._rateLimitation

    @rate_limitation.setter
    def rate_limitation(self, value: Optional[IdsmRateLimitation]) -> None:
        """
        Set rateLimitation with validation.

        Args:
            value: The rateLimitation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rateLimitation = None
            return

        if not isinstance(value, IdsmRateLimitation):
            raise TypeError(
                f"rateLimitation must be IdsmRateLimitation or None, got {type(value).__name__}"
            )
        self._rateLimitation = value
                # signature to the QSEv messages it sends network.
        # The cryptographic algorithm and key to for this signature is further
                # specified by the specifically for the Classic.
        self._signature: Optional["IdsmSignatureSupport"] = None

    @property
    def signature(self) -> Optional["IdsmSignatureSupport"]:
        """Get signature (Pythonic accessor)."""
        return self._signature

    @signature.setter
    def signature(self, value: Optional["IdsmSignatureSupport"]) -> None:
        """
        Set signature with validation.

        Args:
            value: The signature to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._signature = None
            return

        if not isinstance(value, IdsmSignatureSupport):
            raise TypeError(
                f"signature must be IdsmSignatureSupport or None, got {type(value).__name__}"
            )
        self._signature = value
                # the QSEv messages it sends onto the if this attribute does not exist, no
                # timestamp added to the QSEv messages.
        # of this attribute further specifies the as follows: - "AUTOSAR" defines
                # timestamp format according to Time-Base Manager - Any other string
                # proprietary timestamp format.
        # string defining a proprietary timestamp format prefixed by a company-specific
                # name fragment to.
        self._timestamp: Optional["String"] = None

    @property
    def timestamp(self) -> Optional["String"]:
        """Get timestamp (Pythonic accessor)."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: Optional["String"]) -> None:
        """
        Set timestamp with validation.

        Args:
            value: The timestamp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timestamp = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"timestamp must be String or str or None, got {type(value).__name__}"
            )
        self._timestamp = value
                # events on the related EcuInstance.
        # atpVariation.
        self._trafficLimitation: Optional[IdsmTrafficLimitation] = None

    @property
    def traffic_limitation(self) -> Optional[IdsmTrafficLimitation]:
        """Get trafficLimitation (Pythonic accessor)."""
        return self._trafficLimitation

    @traffic_limitation.setter
    def traffic_limitation(self, value: Optional[IdsmTrafficLimitation]) -> None:
        """
        Set trafficLimitation with validation.

        Args:
            value: The trafficLimitation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trafficLimitation = None
            return

        if not isinstance(value, IdsmTrafficLimitation):
            raise TypeError(
                f"trafficLimitation must be IdsmTrafficLimitation or None, got {type(value).__name__}"
            )
        self._trafficLimitation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlockState(self) -> List[BlockState]:
        """
        AUTOSAR-compliant getter for blockState.

        Returns:
            The blockState value

        Note:
            Delegates to block_state property (CODING_RULE_V2_00017)
        """
        return self.block_state  # Delegates to property

    def getEcuInstance(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: "EcuInstance") -> IdsmInstance:
        """
        AUTOSAR-compliant setter for ecuInstance with method chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_instance property setter (gets validation automatically)
        """
        self.ecu_instance = value  # Delegates to property setter
        return self

    def getIdsmInstanceId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for idsmInstanceId.

        Returns:
            The idsmInstanceId value

        Note:
            Delegates to idsm_instance_id property (CODING_RULE_V2_00017)
        """
        return self.idsm_instance_id  # Delegates to property

    def setIdsmInstanceId(self, value: "PositiveInteger") -> IdsmInstance:
        """
        AUTOSAR-compliant setter for idsmInstanceId with method chaining.

        Args:
            value: The idsmInstanceId to set

        Returns:
            self for method chaining

        Note:
            Delegates to idsm_instance_id property setter (gets validation automatically)
        """
        self.idsm_instance_id = value  # Delegates to property setter
        return self

    def getIdsmModule(self) -> "IdsmModule":
        """
        AUTOSAR-compliant getter for idsmModule.

        Returns:
            The idsmModule value

        Note:
            Delegates to idsm_module property (CODING_RULE_V2_00017)
        """
        return self.idsm_module  # Delegates to property

    def setIdsmModule(self, value: "IdsmModule") -> IdsmInstance:
        """
        AUTOSAR-compliant setter for idsmModule with method chaining.

        Args:
            value: The idsmModule to set

        Returns:
            self for method chaining

        Note:
            Delegates to idsm_module property setter (gets validation automatically)
        """
        self.idsm_module = value  # Delegates to property setter
        return self

    def getRateLimitation(self) -> IdsmRateLimitation:
        """
        AUTOSAR-compliant getter for rateLimitation.

        Returns:
            The rateLimitation value

        Note:
            Delegates to rate_limitation property (CODING_RULE_V2_00017)
        """
        return self.rate_limitation  # Delegates to property

    def setRateLimitation(self, value: IdsmRateLimitation) -> IdsmInstance:
        """
        AUTOSAR-compliant setter for rateLimitation with method chaining.

        Args:
            value: The rateLimitation to set

        Returns:
            self for method chaining

        Note:
            Delegates to rate_limitation property setter (gets validation automatically)
        """
        self.rate_limitation = value  # Delegates to property setter
        return self

    def getSignature(self) -> "IdsmSignatureSupport":
        """
        AUTOSAR-compliant getter for signature.

        Returns:
            The signature value

        Note:
            Delegates to signature property (CODING_RULE_V2_00017)
        """
        return self.signature  # Delegates to property

    def setSignature(self, value: "IdsmSignatureSupport") -> IdsmInstance:
        """
        AUTOSAR-compliant setter for signature with method chaining.

        Args:
            value: The signature to set

        Returns:
            self for method chaining

        Note:
            Delegates to signature property setter (gets validation automatically)
        """
        self.signature = value  # Delegates to property setter
        return self

    def getTimestamp(self) -> "String":
        """
        AUTOSAR-compliant getter for timestamp.

        Returns:
            The timestamp value

        Note:
            Delegates to timestamp property (CODING_RULE_V2_00017)
        """
        return self.timestamp  # Delegates to property

    def setTimestamp(self, value: "String") -> IdsmInstance:
        """
        AUTOSAR-compliant setter for timestamp with method chaining.

        Args:
            value: The timestamp to set

        Returns:
            self for method chaining

        Note:
            Delegates to timestamp property setter (gets validation automatically)
        """
        self.timestamp = value  # Delegates to property setter
        return self

    def getTrafficLimitation(self) -> IdsmTrafficLimitation:
        """
        AUTOSAR-compliant getter for trafficLimitation.

        Returns:
            The trafficLimitation value

        Note:
            Delegates to traffic_limitation property (CODING_RULE_V2_00017)
        """
        return self.traffic_limitation  # Delegates to property

    def setTrafficLimitation(self, value: IdsmTrafficLimitation) -> IdsmInstance:
        """
        AUTOSAR-compliant setter for trafficLimitation with method chaining.

        Args:
            value: The trafficLimitation to set

        Returns:
            self for method chaining

        Note:
            Delegates to traffic_limitation property setter (gets validation automatically)
        """
        self.traffic_limitation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> IdsmInstance:
        """
        Set ecuInstance and return self for chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_instance("value")
        """
        self.ecu_instance = value  # Use property setter (gets validation)
        return self

    def with_idsm_instance_id(self, value: Optional["PositiveInteger"]) -> IdsmInstance:
        """
        Set idsmInstanceId and return self for chaining.

        Args:
            value: The idsmInstanceId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_idsm_instance_id("value")
        """
        self.idsm_instance_id = value  # Use property setter (gets validation)
        return self

    def with_idsm_module(self, value: Optional["IdsmModule"]) -> IdsmInstance:
        """
        Set idsmModule and return self for chaining.

        Args:
            value: The idsmModule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_idsm_module("value")
        """
        self.idsm_module = value  # Use property setter (gets validation)
        return self

    def with_rate_limitation(self, value: Optional[IdsmRateLimitation]) -> IdsmInstance:
        """
        Set rateLimitation and return self for chaining.

        Args:
            value: The rateLimitation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rate_limitation("value")
        """
        self.rate_limitation = value  # Use property setter (gets validation)
        return self

    def with_signature(self, value: Optional["IdsmSignatureSupport"]) -> IdsmInstance:
        """
        Set signature and return self for chaining.

        Args:
            value: The signature to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signature("value")
        """
        self.signature = value  # Use property setter (gets validation)
        return self

    def with_timestamp(self, value: Optional["String"]) -> IdsmInstance:
        """
        Set timestamp and return self for chaining.

        Args:
            value: The timestamp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timestamp("value")
        """
        self.timestamp = value  # Use property setter (gets validation)
        return self

    def with_traffic_limitation(self, value: Optional[IdsmTrafficLimitation]) -> IdsmInstance:
        """
        Set trafficLimitation and return self for chaining.

        Args:
            value: The trafficLimitation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_traffic_limitation("value")
        """
        self.traffic_limitation = value  # Use property setter (gets validation)
        return self



class IdsMapping(IdsCommonElement, ABC):
    """
    This meta-class serves as abstract base class for mappings related to an IDS
    design.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsMapping

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 62, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is IdsMapping:
            raise TypeError("IdsMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class IdsmProperties(IdsCommonElement):
    """
    This meta-class provides the ability to aggregate filters for security
    events.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsmProperties

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 63, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents the collection of rate filters for security
        # events in the enclosing 97 Document ID 980:
        # AUTOSAR_FO_TPS_SecurityExtractTemplate Template R23-11.
        self._rateLimitation: List[IdsmRateLimitation] = []

    @property
    def rate_limitation(self) -> List[IdsmRateLimitation]:
        """Get rateLimitation (Pythonic accessor)."""
        return self._rateLimitation
        # This aggregation represents the collection of traffic filters for security
        # events in the enclosing.
        self._trafficLimitation: List[IdsmTrafficLimitation] = []

    @property
    def traffic_limitation(self) -> List[IdsmTrafficLimitation]:
        """Get trafficLimitation (Pythonic accessor)."""
        return self._trafficLimitation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRateLimitation(self) -> List[IdsmRateLimitation]:
        """
        AUTOSAR-compliant getter for rateLimitation.

        Returns:
            The rateLimitation value

        Note:
            Delegates to rate_limitation property (CODING_RULE_V2_00017)
        """
        return self.rate_limitation  # Delegates to property

    def getTrafficLimitation(self) -> List[IdsmTrafficLimitation]:
        """
        AUTOSAR-compliant getter for trafficLimitation.

        Returns:
            The trafficLimitation value

        Note:
            Delegates to traffic_limitation property (CODING_RULE_V2_00017)
        """
        return self.traffic_limitation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SecurityEventContextMapping(IdsMapping, ABC):
    """
    This meta-class represents the ability to create an association between a
    collection of security events, an IdsM instance which handles the security
    events and the filter chains applicable to the security events.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventContextMapping

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 32, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is SecurityEventContextMapping:
            raise TypeError("SecurityEventContextMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference defines the filter chain to be applied to of the referenced
        # security events (depending on the atpVariation.
        self._filterChain: Optional["SecurityEventFilter"] = None

    @property
    def filter_chain(self) -> Optional["SecurityEventFilter"]:
        """Get filterChain (Pythonic accessor)."""
        return self._filterChain

    @filter_chain.setter
    def filter_chain(self, value: Optional["SecurityEventFilter"]) -> None:
        """
        Set filterChain with validation.

        Args:
            value: The filterChain to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filterChain = None
            return

        if not isinstance(value, SecurityEventFilter):
            raise TypeError(
                f"filterChain must be SecurityEventFilter or None, got {type(value).__name__}"
            )
        self._filterChain = value
        # atpVariation 97 Document ID 980: AUTOSAR_FO_TPS_SecurityExtractTemplate
                # Template R23-11.
        self._idsmInstance: Optional[IdsmInstance] = None

    @property
    def idsm_instance(self) -> Optional[IdsmInstance]:
        """Get idsmInstance (Pythonic accessor)."""
        return self._idsmInstance

    @idsm_instance.setter
    def idsm_instance(self, value: Optional[IdsmInstance]) -> None:
        """
        Set idsmInstance with validation.

        Args:
            value: The idsmInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._idsmInstance = None
            return

        if not isinstance(value, IdsmInstance):
            raise TypeError(
                f"idsmInstance must be IdsmInstance or None, got {type(value).__name__}"
            )
        self._idsmInstance = value
                # SecurityEventDefinitions to be mapped to an Idsm additional mapping-dependent
                # properties.
        # atpVariation.
        self._mappedSecurity: List["SecurityEventContext"] = []

    @property
    def mapped_security(self) -> List["SecurityEventContext"]:
        """Get mappedSecurity (Pythonic accessor)."""
        return self._mappedSecurity

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFilterChain(self) -> "SecurityEventFilter":
        """
        AUTOSAR-compliant getter for filterChain.

        Returns:
            The filterChain value

        Note:
            Delegates to filter_chain property (CODING_RULE_V2_00017)
        """
        return self.filter_chain  # Delegates to property

    def setFilterChain(self, value: "SecurityEventFilter") -> SecurityEventContextMapping:
        """
        AUTOSAR-compliant setter for filterChain with method chaining.

        Args:
            value: The filterChain to set

        Returns:
            self for method chaining

        Note:
            Delegates to filter_chain property setter (gets validation automatically)
        """
        self.filter_chain = value  # Delegates to property setter
        return self

    def getIdsmInstance(self) -> IdsmInstance:
        """
        AUTOSAR-compliant getter for idsmInstance.

        Returns:
            The idsmInstance value

        Note:
            Delegates to idsm_instance property (CODING_RULE_V2_00017)
        """
        return self.idsm_instance  # Delegates to property

    def setIdsmInstance(self, value: IdsmInstance) -> SecurityEventContextMapping:
        """
        AUTOSAR-compliant setter for idsmInstance with method chaining.

        Args:
            value: The idsmInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to idsm_instance property setter (gets validation automatically)
        """
        self.idsm_instance = value  # Delegates to property setter
        return self

    def getMappedSecurity(self) -> List["SecurityEventContext"]:
        """
        AUTOSAR-compliant getter for mappedSecurity.

        Returns:
            The mappedSecurity value

        Note:
            Delegates to mapped_security property (CODING_RULE_V2_00017)
        """
        return self.mapped_security  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_filter_chain(self, value: Optional["SecurityEventFilter"]) -> SecurityEventContextMapping:
        """
        Set filterChain and return self for chaining.

        Args:
            value: The filterChain to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filter_chain("value")
        """
        self.filter_chain = value  # Use property setter (gets validation)
        return self

    def with_idsm_instance(self, value: Optional[IdsmInstance]) -> SecurityEventContextMapping:
        """
        Set idsmInstance and return self for chaining.

        Args:
            value: The idsmInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_idsm_instance("value")
        """
        self.idsm_instance = value  # Use property setter (gets validation)
        return self



class SecurityEventContextMappingBswModule(SecurityEventContextMapping):
    """
    This meta-class represents the ability to associate a collection of security
    events with an IdsM instance and with the executional context of a BSW
    module in which this IdsM instance can receive reports for these security
    events.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventContextMappingBswModule

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 38, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to identify the name of the BSW in whose executional
        # context a security event can set of BSW module names is standardized by.
        self._affectedBsw: Optional["String"] = None

    @property
    def affected_bsw(self) -> Optional["String"]:
        """Get affectedBsw (Pythonic accessor)."""
        return self._affectedBsw

    @affected_bsw.setter
    def affected_bsw(self, value: Optional["String"]) -> None:
        """
        Set affectedBsw with validation.

        Args:
            value: The affectedBsw to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._affectedBsw = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"affectedBsw must be String or str or None, got {type(value).__name__}"
            )
        self._affectedBsw = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAffectedBsw(self) -> "String":
        """
        AUTOSAR-compliant getter for affectedBsw.

        Returns:
            The affectedBsw value

        Note:
            Delegates to affected_bsw property (CODING_RULE_V2_00017)
        """
        return self.affected_bsw  # Delegates to property

    def setAffectedBsw(self, value: "String") -> SecurityEventContextMappingBswModule:
        """
        AUTOSAR-compliant setter for affectedBsw with method chaining.

        Args:
            value: The affectedBsw to set

        Returns:
            self for method chaining

        Note:
            Delegates to affected_bsw property setter (gets validation automatically)
        """
        self.affected_bsw = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_affected_bsw(self, value: Optional["String"]) -> SecurityEventContextMappingBswModule:
        """
        Set affectedBsw and return self for chaining.

        Args:
            value: The affectedBsw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_affected_bsw("value")
        """
        self.affected_bsw = value  # Use property setter (gets validation)
        return self



class SecurityEventContextMappingFunctionalCluster(SecurityEventContextMapping):
    """
    This meta-class represents the ability to associate a collection of security
    events with an IdsM instance and with the executional context of a
    functional cluster in which this IdsM instance can receive reports for these
    security events.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventContextMappingFunctionalCluster

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 39, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to identify the name of the functional in whose
        # executional context a security event can The set of functional cluster names
        # is standardized.
        self._affected: "String" = None

    @property
    def affected(self) -> "String":
        """Get affected (Pythonic accessor)."""
        return self._affected

    @affected.setter
    def affected(self, value: "String") -> None:
        """
        Set affected with validation.

        Args:
            value: The affected to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"affected must be String or str, got {type(value).__name__}"
            )
        self._affected = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAffected(self) -> "String":
        """
        AUTOSAR-compliant getter for affected.

        Returns:
            The affected value

        Note:
            Delegates to affected property (CODING_RULE_V2_00017)
        """
        return self.affected  # Delegates to property

    def setAffected(self, value: "String") -> SecurityEventContextMappingFunctionalCluster:
        """
        AUTOSAR-compliant setter for affected with method chaining.

        Args:
            value: The affected to set

        Returns:
            self for method chaining

        Note:
            Delegates to affected property setter (gets validation automatically)
        """
        self.affected = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_affected(self, value: "String") -> SecurityEventContextMappingFunctionalCluster:
        """
        Set affected and return self for chaining.

        Args:
            value: The affected to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_affected("value")
        """
        self.affected = value  # Use property setter (gets validation)
        return self



class SecurityEventContextMappingCommConnector(SecurityEventContextMapping):
    """
    This meta-class represents the ability to associate a collection of security
    events with an IdsM instance and with the executional context related to a
    CommunicationConnector in which this IdsM instance can receive reports for
    these security events.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventContextMappingCommConnector

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 40, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the respective Communication Connector for which
        # the collection of security events can atpVariation.
        self._comm: List["Communication"] = []

    @property
    def comm(self) -> List["Communication"]:
        """Get comm (Pythonic accessor)."""
        return self._comm

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComm(self) -> List["Communication"]:
        """
        AUTOSAR-compliant getter for comm.

        Returns:
            The comm value

        Note:
            Delegates to comm property (CODING_RULE_V2_00017)
        """
        return self.comm  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SecurityEventContextMappingApplication(SecurityEventContextMapping):
    """
    This meta-class represents the ability to associate a collection of security
    events with an IdsM instance and with the executional context of an
    application (e.g. name of SWC on CP or name of SWCL on AP) in which this
    IdsM instance can receive reports for these security events.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventContextMappingApplication

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 42, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to identify the name of the in whose executional
        # context a security event This application can be, for example, a name
        # Software Component (for CP) or a Software Cluster AP).
        self._affected: "String" = None

    @property
    def affected(self) -> "String":
        """Get affected (Pythonic accessor)."""
        return self._affected

    @affected.setter
    def affected(self, value: "String") -> None:
        """
        Set affected with validation.

        Args:
            value: The affected to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"affected must be String or str, got {type(value).__name__}"
            )
        self._affected = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAffected(self) -> "String":
        """
        AUTOSAR-compliant getter for affected.

        Returns:
            The affected value

        Note:
            Delegates to affected property (CODING_RULE_V2_00017)
        """
        return self.affected  # Delegates to property

    def setAffected(self, value: "String") -> SecurityEventContextMappingApplication:
        """
        AUTOSAR-compliant setter for affected with method chaining.

        Args:
            value: The affected to set

        Returns:
            self for method chaining

        Note:
            Delegates to affected property setter (gets validation automatically)
        """
        self.affected = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_affected(self, value: "String") -> SecurityEventContextMappingApplication:
        """
        Set affected and return self for chaining.

        Args:
            value: The affected to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_affected("value")
        """
        self.affected = value  # Use property setter (gets validation)
        return self


class SecurityEventContextDataSourceEnum(AREnum):
    """
    SecurityEventContextDataSourceEnum enumeration

This enumeration controls the elements used to creating the resulting qualified security event Tags: atp.Status=candidate Aggregated by SecurityEventAggregationFilter.contextDataSource

Package: M2::AUTOSARTemplates::SecurityExtractTemplate
    """
    # Context data of first received security event shall be used for resulting qualified security event.
    useFirstContextData = "0"

    # Context data of last received security event shall be used for resulting qualified security event.
    useLastContextData = "1"



class SecurityEventReportingModeEnum(AREnum):
    """
    SecurityEventReportingModeEnum enumeration

This enumeration controls the reporting mode of a security event. Tags: atp.Status=candidate Aggregated by SecurityEventContextProps.defaultReportingMode

Package: M2::AUTOSARTemplates::SecurityExtractTemplate
    """
    # Only the main security event properties such as its ID are processed. Any additional context data (if
    brief = "1"

    # The reported security event without its context data (if existing) is processed further but the filter chain Filters is bypassed.
    briefBypassing = "3"

    # The main properties and the context data (if existing) of the reported security event are processed
    detailed = "2"

    # Extract Template
    Security = "None"

    # FO R23-11
    AUTOSAR = "None"

    # The reported security event including its context data (if existing) is processed further but the filter Filters chain is bypassed.
    detailedBypassing = "4"

    # The reported security event is not further processed by the IdsM and therefore discarded.
    off = "0"
