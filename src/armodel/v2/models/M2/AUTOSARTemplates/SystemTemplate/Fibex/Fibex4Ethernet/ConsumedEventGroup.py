from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ConsumedEventGroup(Identifiable):
    """
    This element represents an event-group to which the service consumer wants
    to subscribe.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 978, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 504, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the application endpoint where the events of the group are received
                # in case of multicast reception.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._application: Optional["ApplicationEndpoint"] = None

    @property
    def application(self) -> Optional["ApplicationEndpoint"]:
        """Get application (Pythonic accessor)."""
        return self._application

    @application.setter
    def application(self, value: Optional["ApplicationEndpoint"]) -> None:
        """
        Set application with validation.

        Args:
            value: The application to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._application = None
            return

        if not isinstance(value, ApplicationEndpoint):
            raise TypeError(
                f"application must be ApplicationEndpoint or None, got {type(value).__name__}"
            )
        self._application = value
        # Defines that this ConsumedEventGroup shall be as soon as the corresponding
                # requested.
        # This could be at if ConsumedServiceInstance.
        # autoRequire is TRUE or as soon as the ConsumedServiceInstance by the
                # application, if ConsumedService set to FALSE.
        self._autoRequire: Optional["Boolean"] = None

    @property
    def auto_require(self) -> Optional["Boolean"]:
        """Get autoRequire (Pythonic accessor)."""
        return self._autoRequire

    @auto_require.setter
    def auto_require(self, value: Optional["Boolean"]) -> None:
        """
        Set autoRequire with validation.

        Args:
            value: The autoRequire to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._autoRequire = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"autoRequire must be Boolean or None, got {type(value).__name__}"
            )
        self._autoRequire = value
        # EventGroup ID.
        # Shall be unique within one system to service discovery.
        self._eventGroup: Optional["PositiveInteger"] = None

    @property
    def event_group(self) -> Optional["PositiveInteger"]:
        """Get eventGroup (Pythonic accessor)."""
        return self._eventGroup

    @event_group.setter
    def event_group(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set eventGroup with validation.

        Args:
            value: The eventGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventGroup = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"eventGroup must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._eventGroup = value
        # This reference defines the multicast address or a address resource where the
                # events of the event received.
        # multicast address is determined via configuration at runtime via service
                # discovery this reference the multicast address over which the events will
                # multicast address is determined at runtime via this reference shall be used
                # to define local multicast address resources, i.
        # e.
        # in the TcpIp module in which the multicast stored at runtime.
        # Please note that in this case address may be defined as ANY UDP port IP
                # address since the multicast address will be runtime.
        # If several multicast addresses are be used the ConsumedEventGroup shall
                # different ApplicationEndpoint objects to reserve resources in the
                # configuration.
        # atpVariation.
        self._eventMulticast: List["ApplicationEndpoint"] = []

    @property
    def event_multicast(self) -> List["ApplicationEndpoint"]:
        """Get eventMulticast (Pythonic accessor)."""
        return self._eventMulticast
        # The ServiceDiscovery module is able to activate and deactivate the PDU
        # routing for receiving events.
        self._pduActivation: List["PduActivationRouting"] = []

    @property
    def pdu_activation(self) -> List["PduActivationRouting"]:
        """Get pduActivation (Pythonic accessor)."""
        return self._pduActivation
        # Defines the frame priority where values from 0 (best 7 (highest) are allowed.
        self._priority: Optional["PositiveInteger"] = None

    @property
    def priority(self) -> Optional["PositiveInteger"]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._priority = value
        # The ServiceDiscovery module is able to activate and PDU routing for receiving
        # events.
        self._routingGroup: List[RefType] = []

    @property
    def routing_group(self) -> List[RefType]:
        """Get routingGroup (Pythonic accessor)."""
        return self._routingGroup
        # The readiness to receive events is defined by the Service the
                # ConsumedEventGroup.
        # The Event know about this announcement to decide submission of events.
        # Therefore the Event be configured with Service-Discovery Client.
        self._sdClientConfig: Optional["SdClientConfig"] = None

    @property
    def sd_client_config(self) -> Optional["SdClientConfig"]:
        """Get sdClientConfig (Pythonic accessor)."""
        return self._sdClientConfig

    @sd_client_config.setter
    def sd_client_config(self, value: Optional["SdClientConfig"]) -> None:
        """
        Set sdClientConfig with validation.

        Args:
            value: The sdClientConfig to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdClientConfig = None
            return

        if not isinstance(value, SdClientConfig):
            raise TypeError(
                f"sdClientConfig must be SdClientConfig or None, got {type(value).__name__}"
            )
        self._sdClientConfig = value
        # Client Timing configuration settings that are EventGroup specific.
        # atpVariation.
        self._sdClientTimer: Optional["SomeipSdClientEvent"] = None

    @property
    def sd_client_timer(self) -> Optional["SomeipSdClientEvent"]:
        """Get sdClientTimer (Pythonic accessor)."""
        return self._sdClientTimer

    @sd_client_timer.setter
    def sd_client_timer(self, value: Optional["SomeipSdClientEvent"]) -> None:
        """
        Set sdClientTimer with validation.

        Args:
            value: The sdClientTimer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdClientTimer = None
            return

        if not isinstance(value, SomeipSdClientEvent):
            raise TypeError(
                f"sdClientTimer must be SomeipSdClientEvent or None, got {type(value).__name__}"
            )
        self._sdClientTimer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplication(self) -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant getter for application.

        Returns:
            The application value

        Note:
            Delegates to application property (CODING_RULE_V2_00017)
        """
        return self.application  # Delegates to property

    def setApplication(self, value: "ApplicationEndpoint") -> "ConsumedEventGroup":
        """
        AUTOSAR-compliant setter for application with method chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Note:
            Delegates to application property setter (gets validation automatically)
        """
        self.application = value  # Delegates to property setter
        return self

    def getAutoRequire(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for autoRequire.

        Returns:
            The autoRequire value

        Note:
            Delegates to auto_require property (CODING_RULE_V2_00017)
        """
        return self.auto_require  # Delegates to property

    def setAutoRequire(self, value: "Boolean") -> "ConsumedEventGroup":
        """
        AUTOSAR-compliant setter for autoRequire with method chaining.

        Args:
            value: The autoRequire to set

        Returns:
            self for method chaining

        Note:
            Delegates to auto_require property setter (gets validation automatically)
        """
        self.auto_require = value  # Delegates to property setter
        return self

    def getEventGroup(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for eventGroup.

        Returns:
            The eventGroup value

        Note:
            Delegates to event_group property (CODING_RULE_V2_00017)
        """
        return self.event_group  # Delegates to property

    def setEventGroup(self, value: "PositiveInteger") -> "ConsumedEventGroup":
        """
        AUTOSAR-compliant setter for eventGroup with method chaining.

        Args:
            value: The eventGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_group property setter (gets validation automatically)
        """
        self.event_group = value  # Delegates to property setter
        return self

    def getEventMulticast(self) -> List["ApplicationEndpoint"]:
        """
        AUTOSAR-compliant getter for eventMulticast.

        Returns:
            The eventMulticast value

        Note:
            Delegates to event_multicast property (CODING_RULE_V2_00017)
        """
        return self.event_multicast  # Delegates to property

    def getPduActivation(self) -> List["PduActivationRouting"]:
        """
        AUTOSAR-compliant getter for pduActivation.

        Returns:
            The pduActivation value

        Note:
            Delegates to pdu_activation property (CODING_RULE_V2_00017)
        """
        return self.pdu_activation  # Delegates to property

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "ConsumedEventGroup":
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    def getRoutingGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for routingGroup.

        Returns:
            The routingGroup value

        Note:
            Delegates to routing_group property (CODING_RULE_V2_00017)
        """
        return self.routing_group  # Delegates to property

    def getSdClientConfig(self) -> "SdClientConfig":
        """
        AUTOSAR-compliant getter for sdClientConfig.

        Returns:
            The sdClientConfig value

        Note:
            Delegates to sd_client_config property (CODING_RULE_V2_00017)
        """
        return self.sd_client_config  # Delegates to property

    def setSdClientConfig(self, value: "SdClientConfig") -> "ConsumedEventGroup":
        """
        AUTOSAR-compliant setter for sdClientConfig with method chaining.

        Args:
            value: The sdClientConfig to set

        Returns:
            self for method chaining

        Note:
            Delegates to sd_client_config property setter (gets validation automatically)
        """
        self.sd_client_config = value  # Delegates to property setter
        return self

    def getSdClientTimer(self) -> "SomeipSdClientEvent":
        """
        AUTOSAR-compliant getter for sdClientTimer.

        Returns:
            The sdClientTimer value

        Note:
            Delegates to sd_client_timer property (CODING_RULE_V2_00017)
        """
        return self.sd_client_timer  # Delegates to property

    def setSdClientTimer(self, value: "SomeipSdClientEvent") -> "ConsumedEventGroup":
        """
        AUTOSAR-compliant setter for sdClientTimer with method chaining.

        Args:
            value: The sdClientTimer to set

        Returns:
            self for method chaining

        Note:
            Delegates to sd_client_timer property setter (gets validation automatically)
        """
        self.sd_client_timer = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application(self, value: Optional["ApplicationEndpoint"]) -> "ConsumedEventGroup":
        """
        Set application and return self for chaining.

        Args:
            value: The application to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application("value")
        """
        self.application = value  # Use property setter (gets validation)
        return self

    def with_auto_require(self, value: Optional["Boolean"]) -> "ConsumedEventGroup":
        """
        Set autoRequire and return self for chaining.

        Args:
            value: The autoRequire to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_auto_require("value")
        """
        self.auto_require = value  # Use property setter (gets validation)
        return self

    def with_event_group(self, value: Optional["PositiveInteger"]) -> "ConsumedEventGroup":
        """
        Set eventGroup and return self for chaining.

        Args:
            value: The eventGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_group("value")
        """
        self.event_group = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "ConsumedEventGroup":
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self

    def with_sd_client_config(self, value: Optional["SdClientConfig"]) -> "ConsumedEventGroup":
        """
        Set sdClientConfig and return self for chaining.

        Args:
            value: The sdClientConfig to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sd_client_config("value")
        """
        self.sd_client_config = value  # Use property setter (gets validation)
        return self

    def with_sd_client_timer(self, value: Optional["SomeipSdClientEvent"]) -> "ConsumedEventGroup":
        """
        Set sdClientTimer and return self for chaining.

        Args:
            value: The sdClientTimer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sd_client_timer("value")
        """
        self.sd_client_timer = value  # Use property setter (gets validation)
        return self
