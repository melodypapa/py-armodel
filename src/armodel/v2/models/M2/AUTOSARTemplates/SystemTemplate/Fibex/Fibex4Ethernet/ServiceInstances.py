"""
AUTOSAR Package - ServiceInstances

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    Referrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.__init__ import (
    FibexElement,
)


class ConsumedEventGroup(Identifiable):
    """
    This element represents an event-group to which the service consumer wants
    to subscribe.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::ConsumedEventGroup
    
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"autoRequire must be Boolean or bool or None, got {type(value).__name__}"
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"eventGroup must be PositiveInteger or str or None, got {type(value).__name__}"
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value
        # The ServiceDiscovery module is able to activate and PDU routing for receiving
        # events.
        self._routingGroup: List["RefType"] = []

    @property
    def routing_group(self) -> List["RefType"]:
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

    def with_pdu_activation(self, value):
        """
        Set pdu_activation and return self for chaining.

        Args:
            value: The pdu_activation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdu_activation("value")
        """
        self.pdu_activation = value  # Use property setter (gets validation)
        return self

    def with_routing_group(self, value):
        """
        Set routing_group and return self for chaining.

        Args:
            value: The routing_group to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_routing_group("value")
        """
        self.routing_group = value  # Use property setter (gets validation)
        return self

    def with_connection(self, value):
        """
        Set connection and return self for chaining.

        Args:
            value: The connection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connection("value")
        """
        self.connection = value  # Use property setter (gets validation)
        return self

    def with_socket_address(self, value):
        """
        Set socket_address and return self for chaining.

        Args:
            value: The socket_address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_socket_address("value")
        """
        self.socket_address = value  # Use property setter (gets validation)
        return self

    def with_static_socket(self, value):
        """
        Set static_socket and return self for chaining.

        Args:
            value: The static_socket to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_static_socket("value")
        """
        self.static_socket = value  # Use property setter (gets validation)
        return self

    def with_service_instance(self, value):
        """
        Set service_instance and return self for chaining.

        Args:
            value: The service_instance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_instance("value")
        """
        self.service_instance = value  # Use property setter (gets validation)
        return self

    def with_capability(self, value):
        """
        Set capability and return self for chaining.

        Args:
            value: The capability to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_capability("value")
        """
        self.capability = value  # Use property setter (gets validation)
        return self

    def with_routing_group(self, value):
        """
        Set routing_group and return self for chaining.

        Args:
            value: The routing_group to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_routing_group("value")
        """
        self.routing_group = value  # Use property setter (gets validation)
        return self

    def with_i_pdu_identifier(self, value):
        """
        Set i_pdu_identifier and return self for chaining.

        Args:
            value: The i_pdu_identifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_pdu_identifier("value")
        """
        self.i_pdu_identifier = value  # Use property setter (gets validation)
        return self

    def with_i_pdu_identifier(self, value):
        """
        Set i_pdu_identifier and return self for chaining.

        Args:
            value: The i_pdu_identifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_pdu_identifier("value")
        """
        self.i_pdu_identifier = value  # Use property setter (gets validation)
        return self

    def with_consumed_event(self, value):
        """
        Set consumed_event and return self for chaining.

        Args:
            value: The consumed_event to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_consumed_event("value")
        """
        self.consumed_event = value  # Use property setter (gets validation)
        return self

    def with_pdu_activation(self, value):
        """
        Set pdu_activation and return self for chaining.

        Args:
            value: The pdu_activation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdu_activation("value")
        """
        self.pdu_activation = value  # Use property setter (gets validation)
        return self

    def with_routing_group(self, value):
        """
        Set routing_group and return self for chaining.

        Args:
            value: The routing_group to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_routing_group("value")
        """
        self.routing_group = value  # Use property setter (gets validation)
        return self

    def with_consumed(self, value):
        """
        Set consumed and return self for chaining.

        Args:
            value: The consumed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_consumed("value")
        """
        self.consumed = value  # Use property setter (gets validation)
        return self

    def with_i_pdu_identifier(self, value):
        """
        Set i_pdu_identifier and return self for chaining.

        Args:
            value: The i_pdu_identifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_pdu_identifier("value")
        """
        self.i_pdu_identifier = value  # Use property setter (gets validation)
        return self

    def with_allowed_service(self, value):
        """
        Set allowed_service and return self for chaining.

        Args:
            value: The allowed_service to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_allowed_service("value")
        """
        self.allowed_service = value  # Use property setter (gets validation)
        return self

    def with_blocklisted(self, value):
        """
        Set blocklisted and return self for chaining.

        Args:
            value: The blocklisted to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_blocklisted("value")
        """
        self.blocklisted = value  # Use property setter (gets validation)
        return self

    def with_consumed_event(self, value):
        """
        Set consumed_event and return self for chaining.

        Args:
            value: The consumed_event to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_consumed_event("value")
        """
        self.consumed_event = value  # Use property setter (gets validation)
        return self

    def with_allowed_service(self, value):
        """
        Set allowed_service and return self for chaining.

        Args:
            value: The allowed_service to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_allowed_service("value")
        """
        self.allowed_service = value  # Use property setter (gets validation)
        return self

    def with_event_handler(self, value):
        """
        Set event_handler and return self for chaining.

        Args:
            value: The event_handler to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_handler("value")
        """
        self.event_handler = value  # Use property setter (gets validation)
        return self

    def with_remote_multicast(self, value):
        """
        Set remote_multicast and return self for chaining.

        Args:
            value: The remote_multicast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_remote_multicast("value")
        """
        self.remote_multicast = value  # Use property setter (gets validation)
        return self

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

    def getRoutingGroup(self) -> List["RefType"]:
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



class SoAdConfig(ARObject):
    """
    SoAd Configuration for one specific Physical Channel.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::SoAdConfig
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 451, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of SocketConnectionBundles.
        # Stereotypes: atpSplitable; atpVariation 2090 Document ID 63:
                # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._connection: List["SocketConnection"] = []

    @property
    def connection(self) -> List["SocketConnection"]:
        """Get connection (Pythonic accessor)."""
        return self._connection
        # Collection of SoAdAddresses.
        # atpVariation.
        self._socketAddress: List["SocketAddress"] = []

    @property
    def socket_address(self) -> List["SocketAddress"]:
        """Get socketAddress (Pythonic accessor)."""
        return self._socketAddress

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnection(self) -> List["SocketConnection"]:
        """
        AUTOSAR-compliant getter for connection.
        
        Returns:
            The connection value
        
        Note:
            Delegates to connection property (CODING_RULE_V2_00017)
        """
        return self.connection  # Delegates to property

    def getSocketAddress(self) -> List["SocketAddress"]:
        """
        AUTOSAR-compliant getter for socketAddress.
        
        Returns:
            The socketAddress value
        
        Note:
            Delegates to socket_address property (CODING_RULE_V2_00017)
        """
        return self.socket_address  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SocketAddress(Identifiable):
    """
    This meta-class represents a socket address towards the rest of the
    meta-model. The actual semantics of the represented socket address, however,
    is contributed by aggregation of an ApplicationEndpoint.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::SocketAddress
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 452, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a list of IPv6 Extension Headers allowed for SocketConnection.
        # If no list is referenced all IPv6 are allowed and processed.
        self._allowedIPv6Ext: Optional["RefType"] = None

    @property
    def allowed_i_pv6_ext(self) -> Optional["RefType"]:
        """Get allowedIPv6Ext (Pythonic accessor)."""
        return self._allowedIPv6Ext

    @allowed_i_pv6_ext.setter
    def allowed_i_pv6_ext(self, value: Optional["RefType"]) -> None:
        """
        Set allowedIPv6Ext with validation.
        
        Args:
            value: The allowedIPv6Ext to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._allowedIPv6Ext = None
            return

        self._allowedIPv6Ext = value
        # Reference to a list of TCP options allowed for this Socket.
        self._allowedTcp: Optional["RefType"] = None

    @property
    def allowed_tcp(self) -> Optional["RefType"]:
        """Get allowedTcp (Pythonic accessor)."""
        return self._allowedTcp

    @allowed_tcp.setter
    def allowed_tcp(self, value: Optional["RefType"]) -> None:
        """
        Set allowedTcp with validation.
        
        Args:
            value: The allowedTcp to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._allowedTcp = None
            return

        self._allowedTcp = value
        # Application addressing.
        self._applicationEndpoint: Optional["ApplicationEndpoint"] = None

    @property
    def application_endpoint(self) -> Optional["ApplicationEndpoint"]:
        """Get applicationEndpoint (Pythonic accessor)."""
        return self._applicationEndpoint

    @application_endpoint.setter
    def application_endpoint(self, value: Optional["ApplicationEndpoint"]) -> None:
        """
        Set applicationEndpoint with validation.
        
        Args:
            value: The applicationEndpoint to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._applicationEndpoint = None
            return

        if not isinstance(value, ApplicationEndpoint):
            raise TypeError(
                f"applicationEndpoint must be ApplicationEndpoint or None, got {type(value).__name__}"
            )
        self._applicationEndpoint = value
        # Association to a CommunicationConnector in the description.
        # This reference shall be used if the an IP unicast address for an is part of
                # the model.
        self._connector: Optional["EthernetCommunication"] = None

    @property
    def connector(self) -> Optional["EthernetCommunication"]:
        """Get connector (Pythonic accessor)."""
        return self._connector

    @connector.setter
    def connector(self, value: Optional["EthernetCommunication"]) -> None:
        """
        Set connector with validation.
        
        Args:
            value: The connector to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connector = None
            return

        if not isinstance(value, EthernetCommunication):
            raise TypeError(
                f"connector must be EthernetCommunication or None, got {type(value).__name__}"
            )
        self._connector = value
        # The 6-bit Differentiated Service Field in the IP headers be used for
                # classifying network traffic.
        # If not set a zero is used to indicate packets that have not.
        self._differentiated: Optional["PositiveInteger"] = None

    @property
    def differentiated(self) -> Optional["PositiveInteger"]:
        """Get differentiated (Pythonic accessor)."""
        return self._differentiated

    @differentiated.setter
    def differentiated(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set differentiated with validation.
        
        Args:
            value: The differentiated to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._differentiated = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"differentiated must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._differentiated = value
        # The 20-bit Flow Label field in the IPv6 header may be a source to label
                # sequences of packets for which special handling by the IPv6 routers, such as
                # of service.
        # If not set a Flow Label of used to indicate packets that have not been 2090
                # Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._flowLabel: Optional["PositiveInteger"] = None

    @property
    def flow_label(self) -> Optional["PositiveInteger"]:
        """Get flowLabel (Pythonic accessor)."""
        return self._flowLabel

    @flow_label.setter
    def flow_label(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set flowLabel with validation.
        
        Args:
            value: The flowLabel to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._flowLabel = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"flowLabel must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._flowLabel = value
        # Association to a CommunicationConnector in the topology description.
        # This reference shall be used if the an IP multicast address, i.
        # e.
        # if ApplicationEndpoint references a describes an IP Address in the IP Such a
                # SocketAddress contains those Ecus (via the multicastConnector the model that
                # will receive multicast the SocketAddress that is defined by the and
                # NetworkEndpoint, Address and UDP Port combination.
        self._multicast: List["EthernetCommunication"] = []

    @property
    def multicast(self) -> List["EthernetCommunication"]:
        """Get multicast (Pythonic accessor)."""
        return self._multicast
        # Defines whether the Path MTU Discovery shall be for the related socket.
        self._pathMtu: Optional["Boolean"] = None

    @property
    def path_mtu(self) -> Optional["Boolean"]:
        """Get pathMtu (Pythonic accessor)."""
        return self._pathMtu

    @path_mtu.setter
    def path_mtu(self, value: Optional["Boolean"]) -> None:
        """
        Set pathMtu with validation.
        
        Args:
            value: The pathMtu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pathMtu = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"pathMtu must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._pathMtu = value
        # Defines the time in seconds which shall pass before a with Pdu collection
        # enabled shall be transmitted to layer after the first Pdu has been put into
        # the.
        self._pduCollection: Optional["TimeValue"] = None

    @property
    def pdu_collection(self) -> Optional["TimeValue"]:
        """Get pduCollection (Pythonic accessor)."""
        return self._pduCollection

    @pdu_collection.setter
    def pdu_collection(self, value: Optional["TimeValue"]) -> None:
        """
        Set pduCollection with validation.
        
        Args:
            value: The pduCollection to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pduCollection = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"pduCollection must be TimeValue or None, got {type(value).__name__}"
            )
        self._pduCollection = value
        # Definition of a static SocketConnection.
        # atpSplitable; atpVariation.
        self._staticSocket: List["StaticSocketConnection"] = []

    @property
    def static_socket(self) -> List["StaticSocketConnection"]:
        """Get staticSocket (Pythonic accessor)."""
        return self._staticSocket
        # Specifies if UDP checksum handling shall be enabled (udpChecksumEnabled) or
        # skipped (udpChecksum the related socket connection.
        self._udpChecksum: Optional["UdpChecksum"] = None

    @property
    def udp_checksum(self) -> Optional["UdpChecksum"]:
        """Get udpChecksum (Pythonic accessor)."""
        return self._udpChecksum

    @udp_checksum.setter
    def udp_checksum(self, value: Optional["UdpChecksum"]) -> None:
        """
        Set udpChecksum with validation.
        
        Args:
            value: The udpChecksum to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._udpChecksum = None
            return

        if not isinstance(value, UdpChecksum):
            raise TypeError(
                f"udpChecksum must be UdpChecksum or None, got {type(value).__name__}"
            )
        self._udpChecksum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllowedIPv6Ext(self) -> "RefType":
        """
        AUTOSAR-compliant getter for allowedIPv6Ext.
        
        Returns:
            The allowedIPv6Ext value
        
        Note:
            Delegates to allowed_i_pv6_ext property (CODING_RULE_V2_00017)
        """
        return self.allowed_i_pv6_ext  # Delegates to property

    def setAllowedIPv6Ext(self, value: "RefType") -> "SocketAddress":
        """
        AUTOSAR-compliant setter for allowedIPv6Ext with method chaining.
        
        Args:
            value: The allowedIPv6Ext to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to allowed_i_pv6_ext property setter (gets validation automatically)
        """
        self.allowed_i_pv6_ext = value  # Delegates to property setter
        return self

    def getAllowedTcp(self) -> "RefType":
        """
        AUTOSAR-compliant getter for allowedTcp.
        
        Returns:
            The allowedTcp value
        
        Note:
            Delegates to allowed_tcp property (CODING_RULE_V2_00017)
        """
        return self.allowed_tcp  # Delegates to property

    def setAllowedTcp(self, value: "RefType") -> "SocketAddress":
        """
        AUTOSAR-compliant setter for allowedTcp with method chaining.
        
        Args:
            value: The allowedTcp to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to allowed_tcp property setter (gets validation automatically)
        """
        self.allowed_tcp = value  # Delegates to property setter
        return self

    def getApplicationEndpoint(self) -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant getter for applicationEndpoint.
        
        Returns:
            The applicationEndpoint value
        
        Note:
            Delegates to application_endpoint property (CODING_RULE_V2_00017)
        """
        return self.application_endpoint  # Delegates to property

    def setApplicationEndpoint(self, value: "ApplicationEndpoint") -> "SocketAddress":
        """
        AUTOSAR-compliant setter for applicationEndpoint with method chaining.
        
        Args:
            value: The applicationEndpoint to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to application_endpoint property setter (gets validation automatically)
        """
        self.application_endpoint = value  # Delegates to property setter
        return self

    def getConnector(self) -> "EthernetCommunication":
        """
        AUTOSAR-compliant getter for connector.
        
        Returns:
            The connector value
        
        Note:
            Delegates to connector property (CODING_RULE_V2_00017)
        """
        return self.connector  # Delegates to property

    def setConnector(self, value: "EthernetCommunication") -> "SocketAddress":
        """
        AUTOSAR-compliant setter for connector with method chaining.
        
        Args:
            value: The connector to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to connector property setter (gets validation automatically)
        """
        self.connector = value  # Delegates to property setter
        return self

    def getDifferentiated(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for differentiated.
        
        Returns:
            The differentiated value
        
        Note:
            Delegates to differentiated property (CODING_RULE_V2_00017)
        """
        return self.differentiated  # Delegates to property

    def setDifferentiated(self, value: "PositiveInteger") -> "SocketAddress":
        """
        AUTOSAR-compliant setter for differentiated with method chaining.
        
        Args:
            value: The differentiated to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to differentiated property setter (gets validation automatically)
        """
        self.differentiated = value  # Delegates to property setter
        return self

    def getFlowLabel(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for flowLabel.
        
        Returns:
            The flowLabel value
        
        Note:
            Delegates to flow_label property (CODING_RULE_V2_00017)
        """
        return self.flow_label  # Delegates to property

    def setFlowLabel(self, value: "PositiveInteger") -> "SocketAddress":
        """
        AUTOSAR-compliant setter for flowLabel with method chaining.
        
        Args:
            value: The flowLabel to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to flow_label property setter (gets validation automatically)
        """
        self.flow_label = value  # Delegates to property setter
        return self

    def getMulticast(self) -> List["EthernetCommunication"]:
        """
        AUTOSAR-compliant getter for multicast.
        
        Returns:
            The multicast value
        
        Note:
            Delegates to multicast property (CODING_RULE_V2_00017)
        """
        return self.multicast  # Delegates to property

    def getPathMtu(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for pathMtu.
        
        Returns:
            The pathMtu value
        
        Note:
            Delegates to path_mtu property (CODING_RULE_V2_00017)
        """
        return self.path_mtu  # Delegates to property

    def setPathMtu(self, value: "Boolean") -> "SocketAddress":
        """
        AUTOSAR-compliant setter for pathMtu with method chaining.
        
        Args:
            value: The pathMtu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to path_mtu property setter (gets validation automatically)
        """
        self.path_mtu = value  # Delegates to property setter
        return self

    def getPduCollection(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for pduCollection.
        
        Returns:
            The pduCollection value
        
        Note:
            Delegates to pdu_collection property (CODING_RULE_V2_00017)
        """
        return self.pdu_collection  # Delegates to property

    def setPduCollection(self, value: "TimeValue") -> "SocketAddress":
        """
        AUTOSAR-compliant setter for pduCollection with method chaining.
        
        Args:
            value: The pduCollection to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pdu_collection property setter (gets validation automatically)
        """
        self.pdu_collection = value  # Delegates to property setter
        return self

    def getStaticSocket(self) -> List["StaticSocketConnection"]:
        """
        AUTOSAR-compliant getter for staticSocket.
        
        Returns:
            The staticSocket value
        
        Note:
            Delegates to static_socket property (CODING_RULE_V2_00017)
        """
        return self.static_socket  # Delegates to property

    def getUdpChecksum(self) -> "UdpChecksum":
        """
        AUTOSAR-compliant getter for udpChecksum.
        
        Returns:
            The udpChecksum value
        
        Note:
            Delegates to udp_checksum property (CODING_RULE_V2_00017)
        """
        return self.udp_checksum  # Delegates to property

    def setUdpChecksum(self, value: "UdpChecksum") -> "SocketAddress":
        """
        AUTOSAR-compliant setter for udpChecksum with method chaining.
        
        Args:
            value: The udpChecksum to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to udp_checksum property setter (gets validation automatically)
        """
        self.udp_checksum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_allowed_i_pv6_ext(self, value: Optional[RefType]) -> "SocketAddress":
        """
        Set allowedIPv6Ext and return self for chaining.
        
        Args:
            value: The allowedIPv6Ext to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_allowed_i_pv6_ext("value")
        """
        self.allowed_i_pv6_ext = value  # Use property setter (gets validation)
        return self

    def with_allowed_tcp(self, value: Optional[RefType]) -> "SocketAddress":
        """
        Set allowedTcp and return self for chaining.
        
        Args:
            value: The allowedTcp to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_allowed_tcp("value")
        """
        self.allowed_tcp = value  # Use property setter (gets validation)
        return self

    def with_application_endpoint(self, value: Optional["ApplicationEndpoint"]) -> "SocketAddress":
        """
        Set applicationEndpoint and return self for chaining.
        
        Args:
            value: The applicationEndpoint to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_application_endpoint("value")
        """
        self.application_endpoint = value  # Use property setter (gets validation)
        return self

    def with_connector(self, value: Optional["EthernetCommunication"]) -> "SocketAddress":
        """
        Set connector and return self for chaining.
        
        Args:
            value: The connector to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_connector("value")
        """
        self.connector = value  # Use property setter (gets validation)
        return self

    def with_differentiated(self, value: Optional["PositiveInteger"]) -> "SocketAddress":
        """
        Set differentiated and return self for chaining.
        
        Args:
            value: The differentiated to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_differentiated("value")
        """
        self.differentiated = value  # Use property setter (gets validation)
        return self

    def with_flow_label(self, value: Optional["PositiveInteger"]) -> "SocketAddress":
        """
        Set flowLabel and return self for chaining.
        
        Args:
            value: The flowLabel to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_flow_label("value")
        """
        self.flow_label = value  # Use property setter (gets validation)
        return self

    def with_path_mtu(self, value: Optional["Boolean"]) -> "SocketAddress":
        """
        Set pathMtu and return self for chaining.
        
        Args:
            value: The pathMtu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_path_mtu("value")
        """
        self.path_mtu = value  # Use property setter (gets validation)
        return self

    def with_pdu_collection(self, value: Optional["TimeValue"]) -> "SocketAddress":
        """
        Set pduCollection and return self for chaining.
        
        Args:
            value: The pduCollection to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pdu_collection("value")
        """
        self.pdu_collection = value  # Use property setter (gets validation)
        return self

    def with_udp_checksum(self, value: Optional["UdpChecksum"]) -> "SocketAddress":
        """
        Set udpChecksum and return self for chaining.
        
        Args:
            value: The udpChecksum to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_udp_checksum("value")
        """
        self.udp_checksum = value  # Use property setter (gets validation)
        return self



class ServiceInstanceCollectionSet(FibexElement):
    """
    Collection of ServiceInstances
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::ServiceInstanceCollectionSet
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 476, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ServiceInstances that are part of the collection.
        # atpSplitable; atpVariation.
        self._serviceInstance: List["AbstractService"] = []

    @property
    def service_instance(self) -> List["AbstractService"]:
        """Get serviceInstance (Pythonic accessor)."""
        return self._serviceInstance

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getServiceInstance(self) -> List["AbstractService"]:
        """
        AUTOSAR-compliant getter for serviceInstance.
        
        Returns:
            The serviceInstance value
        
        Note:
            Delegates to service_instance property (CODING_RULE_V2_00017)
        """
        return self.service_instance  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AbstractServiceInstance(Identifiable, ABC):
    """
    Provided and Consumed Ethernet Service Instances that are available at the
    ApplicationEndpoint.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::AbstractServiceInstance
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 476, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is AbstractServiceInstance:
            raise TypeError("AbstractServiceInstance is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A sequence of records to store arbitrary name/value pairs additional
        # information about the named atpVariation.
        self._capability: List["TagWithOptionalValue"] = []

    @property
    def capability(self) -> List["TagWithOptionalValue"]:
        """Get capability (Pythonic accessor)."""
        return self._capability
        # Major Version of the ServiceInterface.
        # Value can be set to that represents the Major Version of the service.
        self._majorVersion: Optional["PositiveInteger"] = None

    @property
    def major_version(self) -> Optional["PositiveInteger"]:
        """Get majorVersion (Pythonic accessor)."""
        return self._majorVersion

    @major_version.setter
    def major_version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set majorVersion with validation.
        
        Args:
            value: The majorVersion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._majorVersion = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"majorVersion must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._majorVersion = value
        # The ServiceDiscovery module is able to activate and deactivate the PDU
                # routing for ClientServerOperations methods).
        # atpVariation.
        self._method: Optional["PduActivationRouting"] = None

    @property
    def method(self) -> Optional["PduActivationRouting"]:
        """Get method (Pythonic accessor)."""
        return self._method

    @method.setter
    def method(self, value: Optional["PduActivationRouting"]) -> None:
        """
        Set method with validation.
        
        Args:
            value: The method to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._method = None
            return

        if not isinstance(value, PduActivationRouting):
            raise TypeError(
                f"method must be PduActivationRouting or None, got {type(value).__name__}"
            )
        self._method = value
        # The ServiceDiscovery module is able to activate and PDU routing from and to
        # TCP/IP-sockets.
        self._routingGroup: List["RefType"] = []

    @property
    def routing_group(self) -> List["RefType"]:
        """Get routingGroup (Pythonic accessor)."""
        return self._routingGroup

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCapability(self) -> List["TagWithOptionalValue"]:
        """
        AUTOSAR-compliant getter for capability.
        
        Returns:
            The capability value
        
        Note:
            Delegates to capability property (CODING_RULE_V2_00017)
        """
        return self.capability  # Delegates to property

    def getMajorVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for majorVersion.
        
        Returns:
            The majorVersion value
        
        Note:
            Delegates to major_version property (CODING_RULE_V2_00017)
        """
        return self.major_version  # Delegates to property

    def setMajorVersion(self, value: "PositiveInteger") -> "AbstractServiceInstance":
        """
        AUTOSAR-compliant setter for majorVersion with method chaining.
        
        Args:
            value: The majorVersion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to major_version property setter (gets validation automatically)
        """
        self.major_version = value  # Delegates to property setter
        return self

    def getMethod(self) -> "PduActivationRouting":
        """
        AUTOSAR-compliant getter for method.
        
        Returns:
            The method value
        
        Note:
            Delegates to method property (CODING_RULE_V2_00017)
        """
        return self.method  # Delegates to property

    def setMethod(self, value: "PduActivationRouting") -> "AbstractServiceInstance":
        """
        AUTOSAR-compliant setter for method with method chaining.
        
        Args:
            value: The method to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to method property setter (gets validation automatically)
        """
        self.method = value  # Delegates to property setter
        return self

    def getRoutingGroup(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for routingGroup.
        
        Returns:
            The routingGroup value
        
        Note:
            Delegates to routing_group property (CODING_RULE_V2_00017)
        """
        return self.routing_group  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_major_version(self, value: Optional["PositiveInteger"]) -> "AbstractServiceInstance":
        """
        Set majorVersion and return self for chaining.
        
        Args:
            value: The majorVersion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_major_version("value")
        """
        self.major_version = value  # Use property setter (gets validation)
        return self

    def with_method(self, value: Optional["PduActivationRouting"]) -> "AbstractServiceInstance":
        """
        Set method and return self for chaining.
        
        Args:
            value: The method to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_method("value")
        """
        self.method = value  # Use property setter (gets validation)
        return self



class PduActivationRoutingGroup(Identifiable):
    """
    Group of Pdus that can be activated or deactivated for transmission over a
    socket connection.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::PduActivationRoutingGroup
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 488, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the type of a RoutingGroup.
        # There are RoutingGroups that activate the data path for unicast events of an
                # event group.
        # And there are activate the data path for initial are triggered, namely events
                # that are sent out server side after a client got subscribed.
        # Please this attribute is only valid for event Receiver communication) and
                # omitted in MethodActivationRoutingGroups.
        self._eventGroup: Optional["RefType"] = None

    @property
    def event_group(self) -> Optional["RefType"]:
        """Get eventGroup (Pythonic accessor)."""
        return self._eventGroup

    @event_group.setter
    def event_group(self, value: Optional["RefType"]) -> None:
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

        self._eventGroup = value
        # PduIdentifiers assigned for transmission over Udp in case the referencing
        # PduActivationRoutingGroup is.
        self._iPduIdentifier: List["SoConIPduIdentifier"] = []

    @property
    def i_pdu_identifier(self) -> List["SoConIPduIdentifier"]:
        """Get iPduIdentifier (Pythonic accessor)."""
        return self._iPduIdentifier

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for eventGroup.
        
        Returns:
            The eventGroup value
        
        Note:
            Delegates to event_group property (CODING_RULE_V2_00017)
        """
        return self.event_group  # Delegates to property

    def setEventGroup(self, value: "RefType") -> "PduActivationRoutingGroup":
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

    def getIPduIdentifier(self) -> List["SoConIPduIdentifier"]:
        """
        AUTOSAR-compliant getter for iPduIdentifier.
        
        Returns:
            The iPduIdentifier value
        
        Note:
            Delegates to i_pdu_identifier property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_identifier  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_group(self, value: Optional[RefType]) -> "PduActivationRoutingGroup":
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



class SoConIPduIdentifier(Referrable):
    """
    Identification of Pdu content on a socket connection. This Identifier is
    required in case that multiple Pdus are transmitted over the same socket
    connection.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::SoConIPduIdentifier
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 489, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If multiple Pdus are transmitted over the same connection can be used to
        # distinguish between the constraints on constructing the headerId for see
        # PRS_SOMEIP_00245.
        self._headerId: Optional["PositiveInteger"] = None

    @property
    def header_id(self) -> Optional["PositiveInteger"]:
        """Get headerId (Pythonic accessor)."""
        return self._headerId

    @header_id.setter
    def header_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set headerId with validation.
        
        Args:
            value: The headerId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._headerId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"headerId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._headerId = value
        # Defines whether the referenced Pdu contributes to the triggering of the
        # socket transmission if Pdu collection is this socket.
        self._pduCollection: Optional["RefType"] = None

    @property
    def pdu_collection(self) -> Optional["RefType"]:
        """Get pduCollection (Pythonic accessor)."""
        return self._pduCollection

    @pdu_collection.setter
    def pdu_collection(self, value: Optional["RefType"]) -> None:
        """
        Set pduCollection with validation.
        
        Args:
            value: The pduCollection to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pduCollection = None
            return

        self._pduCollection = value
        # Reference to a Pdu that is transmitted over a socket.
        self._pduTriggering: Optional["RefType"] = None

    @property
    def pdu_triggering(self) -> Optional["RefType"]:
        """Get pduTriggering (Pythonic accessor)."""
        return self._pduTriggering

    @pdu_triggering.setter
    def pdu_triggering(self, value: Optional["RefType"]) -> None:
        """
        Set pduTriggering with validation.
        
        Args:
            value: The pduTriggering to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pduTriggering = None
            return

        self._pduTriggering = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHeaderId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for headerId.
        
        Returns:
            The headerId value
        
        Note:
            Delegates to header_id property (CODING_RULE_V2_00017)
        """
        return self.header_id  # Delegates to property

    def setHeaderId(self, value: "PositiveInteger") -> "SoConIPduIdentifier":
        """
        AUTOSAR-compliant setter for headerId with method chaining.
        
        Args:
            value: The headerId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to header_id property setter (gets validation automatically)
        """
        self.header_id = value  # Delegates to property setter
        return self

    def getPduCollection(self) -> "RefType":
        """
        AUTOSAR-compliant getter for pduCollection.
        
        Returns:
            The pduCollection value
        
        Note:
            Delegates to pdu_collection property (CODING_RULE_V2_00017)
        """
        return self.pdu_collection  # Delegates to property

    def setPduCollection(self, value: "RefType") -> "SoConIPduIdentifier":
        """
        AUTOSAR-compliant setter for pduCollection with method chaining.
        
        Args:
            value: The pduCollection to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pdu_collection property setter (gets validation automatically)
        """
        self.pdu_collection = value  # Delegates to property setter
        return self

    def getPduTriggering(self) -> "RefType":
        """
        AUTOSAR-compliant getter for pduTriggering.
        
        Returns:
            The pduTriggering value
        
        Note:
            Delegates to pdu_triggering property (CODING_RULE_V2_00017)
        """
        return self.pdu_triggering  # Delegates to property

    def setPduTriggering(self, value: "RefType") -> "SoConIPduIdentifier":
        """
        AUTOSAR-compliant setter for pduTriggering with method chaining.
        
        Args:
            value: The pduTriggering to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pdu_triggering property setter (gets validation automatically)
        """
        self.pdu_triggering = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_header_id(self, value: Optional["PositiveInteger"]) -> "SoConIPduIdentifier":
        """
        Set headerId and return self for chaining.
        
        Args:
            value: The headerId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_header_id("value")
        """
        self.header_id = value  # Use property setter (gets validation)
        return self

    def with_pdu_collection(self, value: Optional[RefType]) -> "SoConIPduIdentifier":
        """
        Set pduCollection and return self for chaining.
        
        Args:
            value: The pduCollection to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pdu_collection("value")
        """
        self.pdu_collection = value  # Use property setter (gets validation)
        return self

    def with_pdu_triggering(self, value: Optional[RefType]) -> "SoConIPduIdentifier":
        """
        Set pduTriggering and return self for chaining.
        
        Args:
            value: The pduTriggering to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pdu_triggering("value")
        """
        self.pdu_triggering = value  # Use property setter (gets validation)
        return self



class SocketConnectionIpduIdentifierSet(FibexElement):
    """
    Collection of PduIdentifiers used for transmission over a Socket Connection
    with the header option.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::SocketConnectionIpduIdentifierSet
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 490, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of IPduIdentifiers that are transmitted over.
        self._iPduIdentifier: List["SoConIPduIdentifier"] = []

    @property
    def i_pdu_identifier(self) -> List["SoConIPduIdentifier"]:
        """Get iPduIdentifier (Pythonic accessor)."""
        return self._iPduIdentifier

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPduIdentifier(self) -> List["SoConIPduIdentifier"]:
        """
        AUTOSAR-compliant getter for iPduIdentifier.
        
        Returns:
            The iPduIdentifier value
        
        Note:
            Delegates to i_pdu_identifier property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_identifier  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EventHandler(Identifiable):
    """
    This element represents an event group as part of the Provided Service
    Instance.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::EventHandler
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 492, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # All consumers of the event are referenced here.
        # atp.
        # Status=obsolete.
        self._consumedEvent: List["RefType"] = []

    @property
    def consumed_event(self) -> List["RefType"]:
        """Get consumedEvent (Pythonic accessor)."""
        return self._consumedEvent
        # Unique Identifier that identifies the EventGroup in SOME/ This Identifier is
        # sent as Eventgroup ID in SOME/IP messages.
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"eventGroup must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._eventGroup = value
        # Multicast Address that is used for event communication in IP-Multicast case.
        # It is the destination address to server sends the multicast event messages if
                # is exceeded.
        # is transmitted in the SD-SubscribeEvent to client (answer to SD-Subscribe
                # atpVariation.
        self._eventMulticast: Optional["ApplicationEndpoint"] = None

    @property
    def event_multicast(self) -> Optional["ApplicationEndpoint"]:
        """Get eventMulticast (Pythonic accessor)."""
        return self._eventMulticast

    @event_multicast.setter
    def event_multicast(self, value: Optional["ApplicationEndpoint"]) -> None:
        """
        Set eventMulticast with validation.
        
        Args:
            value: The eventMulticast to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventMulticast = None
            return

        if not isinstance(value, ApplicationEndpoint):
            raise TypeError(
                f"eventMulticast must be ApplicationEndpoint or None, got {type(value).__name__}"
            )
        self._eventMulticast = value
        # Specifies the number of subscribed clients that trigger the to change the
                # transmission of events to multicast.
        # to 0 only unicast will be used.
        # If configured the first client will be already served by multicast.
        # If 2 the first client will be server with unicast soon as the second client
                # arrives both will be multicast.
        # not influence the handling of initial events, served using unicast only.
        self._multicast: Optional["PositiveInteger"] = None

    @property
    def multicast(self) -> Optional["PositiveInteger"]:
        """Get multicast (Pythonic accessor)."""
        return self._multicast

    @multicast.setter
    def multicast(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set multicast with validation.
        
        Args:
            value: The multicast to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._multicast = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"multicast must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._multicast = value
        # The ServiceDiscovery module is able to activate and deactivate the PDU
        # routing for events.
        self._pduActivation: List["PduActivationRouting"] = []

    @property
    def pdu_activation(self) -> List["PduActivationRouting"]:
        """Get pduActivation (Pythonic accessor)."""
        return self._pduActivation
        # The ServiceDiscovery module is able to activate and PDU routing for events.
        self._routingGroup: List["RefType"] = []

    @property
    def routing_group(self) -> List["RefType"]:
        """Get routingGroup (Pythonic accessor)."""
        return self._routingGroup
        # Server configuration parameter for Service-Discovery.
        self._sdServerConfig: Optional["SdServerConfig"] = None

    @property
    def sd_server_config(self) -> Optional["SdServerConfig"]:
        """Get sdServerConfig (Pythonic accessor)."""
        return self._sdServerConfig

    @sd_server_config.setter
    def sd_server_config(self, value: Optional["SdServerConfig"]) -> None:
        """
        Set sdServerConfig with validation.
        
        Args:
            value: The sdServerConfig to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdServerConfig = None
            return

        if not isinstance(value, SdServerConfig):
            raise TypeError(
                f"sdServerConfig must be SdServerConfig or None, got {type(value).__name__}"
            )
        self._sdServerConfig = value
        # Server Timing configuration settings that are EventGroup specific.
        # atpVariation.
        self._sdServerEg: Optional["SomeipSdServerEvent"] = None

    @property
    def sd_server_eg(self) -> Optional["SomeipSdServerEvent"]:
        """Get sdServerEg (Pythonic accessor)."""
        return self._sdServerEg

    @sd_server_eg.setter
    def sd_server_eg(self, value: Optional["SomeipSdServerEvent"]) -> None:
        """
        Set sdServerEg with validation.
        
        Args:
            value: The sdServerEg to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdServerEg = None
            return

        if not isinstance(value, SomeipSdServerEvent):
            raise TypeError(
                f"sdServerEg must be SomeipSdServerEvent or None, got {type(value).__name__}"
            )
        self._sdServerEg = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConsumedEvent(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for consumedEvent.
        
        Returns:
            The consumedEvent value
        
        Note:
            Delegates to consumed_event property (CODING_RULE_V2_00017)
        """
        return self.consumed_event  # Delegates to property

    def getEventGroup(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for eventGroup.
        
        Returns:
            The eventGroup value
        
        Note:
            Delegates to event_group property (CODING_RULE_V2_00017)
        """
        return self.event_group  # Delegates to property

    def setEventGroup(self, value: "PositiveInteger") -> "EventHandler":
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

    def getEventMulticast(self) -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant getter for eventMulticast.
        
        Returns:
            The eventMulticast value
        
        Note:
            Delegates to event_multicast property (CODING_RULE_V2_00017)
        """
        return self.event_multicast  # Delegates to property

    def setEventMulticast(self, value: "ApplicationEndpoint") -> "EventHandler":
        """
        AUTOSAR-compliant setter for eventMulticast with method chaining.
        
        Args:
            value: The eventMulticast to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_multicast property setter (gets validation automatically)
        """
        self.event_multicast = value  # Delegates to property setter
        return self

    def getMulticast(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for multicast.
        
        Returns:
            The multicast value
        
        Note:
            Delegates to multicast property (CODING_RULE_V2_00017)
        """
        return self.multicast  # Delegates to property

    def setMulticast(self, value: "PositiveInteger") -> "EventHandler":
        """
        AUTOSAR-compliant setter for multicast with method chaining.
        
        Args:
            value: The multicast to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to multicast property setter (gets validation automatically)
        """
        self.multicast = value  # Delegates to property setter
        return self

    def getPduActivation(self) -> List["PduActivationRouting"]:
        """
        AUTOSAR-compliant getter for pduActivation.
        
        Returns:
            The pduActivation value
        
        Note:
            Delegates to pdu_activation property (CODING_RULE_V2_00017)
        """
        return self.pdu_activation  # Delegates to property

    def getRoutingGroup(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for routingGroup.
        
        Returns:
            The routingGroup value
        
        Note:
            Delegates to routing_group property (CODING_RULE_V2_00017)
        """
        return self.routing_group  # Delegates to property

    def getSdServerConfig(self) -> "SdServerConfig":
        """
        AUTOSAR-compliant getter for sdServerConfig.
        
        Returns:
            The sdServerConfig value
        
        Note:
            Delegates to sd_server_config property (CODING_RULE_V2_00017)
        """
        return self.sd_server_config  # Delegates to property

    def setSdServerConfig(self, value: "SdServerConfig") -> "EventHandler":
        """
        AUTOSAR-compliant setter for sdServerConfig with method chaining.
        
        Args:
            value: The sdServerConfig to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sd_server_config property setter (gets validation automatically)
        """
        self.sd_server_config = value  # Delegates to property setter
        return self

    def getSdServerEg(self) -> "SomeipSdServerEvent":
        """
        AUTOSAR-compliant getter for sdServerEg.
        
        Returns:
            The sdServerEg value
        
        Note:
            Delegates to sd_server_eg property (CODING_RULE_V2_00017)
        """
        return self.sd_server_eg  # Delegates to property

    def setSdServerEg(self, value: "SomeipSdServerEvent") -> "EventHandler":
        """
        AUTOSAR-compliant setter for sdServerEg with method chaining.
        
        Args:
            value: The sdServerEg to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sd_server_eg property setter (gets validation automatically)
        """
        self.sd_server_eg = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_group(self, value: Optional["PositiveInteger"]) -> "EventHandler":
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

    def with_event_multicast(self, value: Optional["ApplicationEndpoint"]) -> "EventHandler":
        """
        Set eventMulticast and return self for chaining.
        
        Args:
            value: The eventMulticast to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_multicast("value")
        """
        self.event_multicast = value  # Use property setter (gets validation)
        return self

    def with_multicast(self, value: Optional["PositiveInteger"]) -> "EventHandler":
        """
        Set multicast and return self for chaining.
        
        Args:
            value: The multicast to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_multicast("value")
        """
        self.multicast = value  # Use property setter (gets validation)
        return self

    def with_sd_server_config(self, value: Optional["SdServerConfig"]) -> "EventHandler":
        """
        Set sdServerConfig and return self for chaining.
        
        Args:
            value: The sdServerConfig to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sd_server_config("value")
        """
        self.sd_server_config = value  # Use property setter (gets validation)
        return self

    def with_sd_server_eg(self, value: Optional["SomeipSdServerEvent"]) -> "EventHandler":
        """
        Set sdServerEg and return self for chaining.
        
        Args:
            value: The sdServerEg to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sd_server_eg("value")
        """
        self.sd_server_eg = value  # Use property setter (gets validation)
        return self



class SomeipSdServerServiceInstanceConfig(ARElement):
    """
    Server specific settings that are relevant for the configuration of SOME/IP
    Service-Discovery.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::SomeipSdServerServiceInstanceConfig
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 513, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Controls offer behavior of the server.
        self._initialOfferBehavior: Optional["InitialSdDelayConfig"] = None

    @property
    def initial_offer_behavior(self) -> Optional["InitialSdDelayConfig"]:
        """Get initialOfferBehavior (Pythonic accessor)."""
        return self._initialOfferBehavior

    @initial_offer_behavior.setter
    def initial_offer_behavior(self, value: Optional["InitialSdDelayConfig"]) -> None:
        """
        Set initialOfferBehavior with validation.
        
        Args:
            value: The initialOfferBehavior to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialOfferBehavior = None
            return

        if not isinstance(value, InitialSdDelayConfig):
            raise TypeError(
                f"initialOfferBehavior must be InitialSdDelayConfig or None, got {type(value).__name__}"
            )
        self._initialOfferBehavior = value
        # Optional attribute to define cyclic offers.
        # Cyclic offer is the delay is set (in seconds) and greater then 0.
        self._offerCyclicDelay: Optional["TimeValue"] = None

    @property
    def offer_cyclic_delay(self) -> Optional["TimeValue"]:
        """Get offerCyclicDelay (Pythonic accessor)."""
        return self._offerCyclicDelay

    @offer_cyclic_delay.setter
    def offer_cyclic_delay(self, value: Optional["TimeValue"]) -> None:
        """
        Set offerCyclicDelay with validation.
        
        Args:
            value: The offerCyclicDelay to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._offerCyclicDelay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"offerCyclicDelay must be TimeValue or None, got {type(value).__name__}"
            )
        self._offerCyclicDelay = value
        # This attribute defines the VLAN frame priority for Service that result from
                # ProvidedSomeip are referencing the SomeipSd StopOffer Values from 0 (best 7
                # (highest) are allowed.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value
        # Maximum/Minimum allowable response delay to entries by multicast in seconds.
        # The Service Discovery answers to entries that were transported in a message
                # (e.
        # g.
        # FindService).
        self._request: Optional["RequestResponseDelay"] = None

    @property
    def request(self) -> Optional["RequestResponseDelay"]:
        """Get request (Pythonic accessor)."""
        return self._request

    @request.setter
    def request(self, value: Optional["RequestResponseDelay"]) -> None:
        """
        Set request with validation.
        
        Args:
            value: The request to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._request = None
            return

        if not isinstance(value, RequestResponseDelay):
            raise TypeError(
                f"request must be RequestResponseDelay or None, got {type(value).__name__}"
            )
        self._request = value
        # Defines the time in seconds the service offer is valid.
        self._serviceOffer: Optional["PositiveInteger"] = None

    @property
    def service_offer(self) -> Optional["PositiveInteger"]:
        """Get serviceOffer (Pythonic accessor)."""
        return self._serviceOffer

    @service_offer.setter
    def service_offer(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set serviceOffer with validation.
        
        Args:
            value: The serviceOffer to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceOffer = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"serviceOffer must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._serviceOffer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitialOfferBehavior(self) -> "InitialSdDelayConfig":
        """
        AUTOSAR-compliant getter for initialOfferBehavior.
        
        Returns:
            The initialOfferBehavior value
        
        Note:
            Delegates to initial_offer_behavior property (CODING_RULE_V2_00017)
        """
        return self.initial_offer_behavior  # Delegates to property

    def setInitialOfferBehavior(self, value: "InitialSdDelayConfig") -> "SomeipSdServerServiceInstanceConfig":
        """
        AUTOSAR-compliant setter for initialOfferBehavior with method chaining.
        
        Args:
            value: The initialOfferBehavior to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to initial_offer_behavior property setter (gets validation automatically)
        """
        self.initial_offer_behavior = value  # Delegates to property setter
        return self

    def getOfferCyclicDelay(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for offerCyclicDelay.
        
        Returns:
            The offerCyclicDelay value
        
        Note:
            Delegates to offer_cyclic_delay property (CODING_RULE_V2_00017)
        """
        return self.offer_cyclic_delay  # Delegates to property

    def setOfferCyclicDelay(self, value: "TimeValue") -> "SomeipSdServerServiceInstanceConfig":
        """
        AUTOSAR-compliant setter for offerCyclicDelay with method chaining.
        
        Args:
            value: The offerCyclicDelay to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to offer_cyclic_delay property setter (gets validation automatically)
        """
        self.offer_cyclic_delay = value  # Delegates to property setter
        return self

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.
        
        Returns:
            The priority value
        
        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "SomeipSdServerServiceInstanceConfig":
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

    def getRequest(self) -> "RequestResponseDelay":
        """
        AUTOSAR-compliant getter for request.
        
        Returns:
            The request value
        
        Note:
            Delegates to request property (CODING_RULE_V2_00017)
        """
        return self.request  # Delegates to property

    def setRequest(self, value: "RequestResponseDelay") -> "SomeipSdServerServiceInstanceConfig":
        """
        AUTOSAR-compliant setter for request with method chaining.
        
        Args:
            value: The request to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to request property setter (gets validation automatically)
        """
        self.request = value  # Delegates to property setter
        return self

    def getServiceOffer(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for serviceOffer.
        
        Returns:
            The serviceOffer value
        
        Note:
            Delegates to service_offer property (CODING_RULE_V2_00017)
        """
        return self.service_offer  # Delegates to property

    def setServiceOffer(self, value: "PositiveInteger") -> "SomeipSdServerServiceInstanceConfig":
        """
        AUTOSAR-compliant setter for serviceOffer with method chaining.
        
        Args:
            value: The serviceOffer to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to service_offer property setter (gets validation automatically)
        """
        self.service_offer = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_initial_offer_behavior(self, value: Optional["InitialSdDelayConfig"]) -> "SomeipSdServerServiceInstanceConfig":
        """
        Set initialOfferBehavior and return self for chaining.
        
        Args:
            value: The initialOfferBehavior to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_initial_offer_behavior("value")
        """
        self.initial_offer_behavior = value  # Use property setter (gets validation)
        return self

    def with_offer_cyclic_delay(self, value: Optional["TimeValue"]) -> "SomeipSdServerServiceInstanceConfig":
        """
        Set offerCyclicDelay and return self for chaining.
        
        Args:
            value: The offerCyclicDelay to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_offer_cyclic_delay("value")
        """
        self.offer_cyclic_delay = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "SomeipSdServerServiceInstanceConfig":
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

    def with_request(self, value: Optional["RequestResponseDelay"]) -> "SomeipSdServerServiceInstanceConfig":
        """
        Set request and return self for chaining.
        
        Args:
            value: The request to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_request("value")
        """
        self.request = value  # Use property setter (gets validation)
        return self

    def with_service_offer(self, value: Optional["PositiveInteger"]) -> "SomeipSdServerServiceInstanceConfig":
        """
        Set serviceOffer and return self for chaining.
        
        Args:
            value: The serviceOffer to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_service_offer("value")
        """
        self.service_offer = value  # Use property setter (gets validation)
        return self



class InitialSdDelayConfig(ARObject):
    """
    This element is used to configure the offer behavior of the server and the
    find behavior on the client.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::InitialSdDelayConfig
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 514, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Max Value in seconds to delay randomly the first offer (if by SdServerConfig)
        # or the transmission of a (if aggregated by SdClientConfig).
        self._initialDelayMax: Optional["TimeValue"] = None

    @property
    def initial_delay_max(self) -> Optional["TimeValue"]:
        """Get initialDelayMax (Pythonic accessor)."""
        return self._initialDelayMax

    @initial_delay_max.setter
    def initial_delay_max(self, value: Optional["TimeValue"]) -> None:
        """
        Set initialDelayMax with validation.
        
        Args:
            value: The initialDelayMax to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialDelayMax = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"initialDelayMax must be TimeValue or None, got {type(value).__name__}"
            )
        self._initialDelayMax = value
        # Min Value in seconds to delay randomly the first offer or transmission of a
        # find message (if aggregated by Sd.
        self._initialDelayMin: Optional["TimeValue"] = None

    @property
    def initial_delay_min(self) -> Optional["TimeValue"]:
        """Get initialDelayMin (Pythonic accessor)."""
        return self._initialDelayMin

    @initial_delay_min.setter
    def initial_delay_min(self, value: Optional["TimeValue"]) -> None:
        """
        Set initialDelayMin with validation.
        
        Args:
            value: The initialDelayMin to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialDelayMin = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"initialDelayMin must be TimeValue or None, got {type(value).__name__}"
            )
        self._initialDelayMin = value
        # Describes the maximum amount of offer repetitions (if by SdServerConfig) or
        # the maximum amount repetitions (if aggregated by SdClientConfig).
        self._initial: Optional["PositiveInteger"] = None

    @property
    def initial(self) -> Optional["PositiveInteger"]:
        """Get initial (Pythonic accessor)."""
        return self._initial

    @initial.setter
    def initial(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set initial with validation.
        
        Args:
            value: The initial to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initial = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"initial must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._initial = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitialDelayMax(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for initialDelayMax.
        
        Returns:
            The initialDelayMax value
        
        Note:
            Delegates to initial_delay_max property (CODING_RULE_V2_00017)
        """
        return self.initial_delay_max  # Delegates to property

    def setInitialDelayMax(self, value: "TimeValue") -> "InitialSdDelayConfig":
        """
        AUTOSAR-compliant setter for initialDelayMax with method chaining.
        
        Args:
            value: The initialDelayMax to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to initial_delay_max property setter (gets validation automatically)
        """
        self.initial_delay_max = value  # Delegates to property setter
        return self

    def getInitialDelayMin(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for initialDelayMin.
        
        Returns:
            The initialDelayMin value
        
        Note:
            Delegates to initial_delay_min property (CODING_RULE_V2_00017)
        """
        return self.initial_delay_min  # Delegates to property

    def setInitialDelayMin(self, value: "TimeValue") -> "InitialSdDelayConfig":
        """
        AUTOSAR-compliant setter for initialDelayMin with method chaining.
        
        Args:
            value: The initialDelayMin to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to initial_delay_min property setter (gets validation automatically)
        """
        self.initial_delay_min = value  # Delegates to property setter
        return self

    def getInitial(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for initial.
        
        Returns:
            The initial value
        
        Note:
            Delegates to initial property (CODING_RULE_V2_00017)
        """
        return self.initial  # Delegates to property

    def setInitial(self, value: "PositiveInteger") -> "InitialSdDelayConfig":
        """
        AUTOSAR-compliant setter for initial with method chaining.
        
        Args:
            value: The initial to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to initial property setter (gets validation automatically)
        """
        self.initial = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_initial_delay_max(self, value: Optional["TimeValue"]) -> "InitialSdDelayConfig":
        """
        Set initialDelayMax and return self for chaining.
        
        Args:
            value: The initialDelayMax to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_initial_delay_max("value")
        """
        self.initial_delay_max = value  # Use property setter (gets validation)
        return self

    def with_initial_delay_min(self, value: Optional["TimeValue"]) -> "InitialSdDelayConfig":
        """
        Set initialDelayMin and return self for chaining.
        
        Args:
            value: The initialDelayMin to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_initial_delay_min("value")
        """
        self.initial_delay_min = value  # Use property setter (gets validation)
        return self

    def with_initial(self, value: Optional["PositiveInteger"]) -> "InitialSdDelayConfig":
        """
        Set initial and return self for chaining.
        
        Args:
            value: The initial to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_initial("value")
        """
        self.initial = value  # Use property setter (gets validation)
        return self



class RequestResponseDelay(ARObject):
    """
    Time to wait before answering the query.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::RequestResponseDelay
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 515, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum allowable response delay to entries received by seconds.
        self._maxValue: Optional["TimeValue"] = None

    @property
    def max_value(self) -> Optional["TimeValue"]:
        """Get maxValue (Pythonic accessor)."""
        return self._maxValue

    @max_value.setter
    def max_value(self, value: Optional["TimeValue"]) -> None:
        """
        Set maxValue with validation.
        
        Args:
            value: The maxValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxValue = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"maxValue must be TimeValue or None, got {type(value).__name__}"
            )
        self._maxValue = value
        # Minimum allowable response delay to entries received by seconds.
        self._minValue: Optional["TimeValue"] = None

    @property
    def min_value(self) -> Optional["TimeValue"]:
        """Get minValue (Pythonic accessor)."""
        return self._minValue

    @min_value.setter
    def min_value(self, value: Optional["TimeValue"]) -> None:
        """
        Set minValue with validation.
        
        Args:
            value: The minValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minValue = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minValue must be TimeValue or None, got {type(value).__name__}"
            )
        self._minValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxValue(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for maxValue.
        
        Returns:
            The maxValue value
        
        Note:
            Delegates to max_value property (CODING_RULE_V2_00017)
        """
        return self.max_value  # Delegates to property

    def setMaxValue(self, value: "TimeValue") -> "RequestResponseDelay":
        """
        AUTOSAR-compliant setter for maxValue with method chaining.
        
        Args:
            value: The maxValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_value property setter (gets validation automatically)
        """
        self.max_value = value  # Delegates to property setter
        return self

    def getMinValue(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minValue.
        
        Returns:
            The minValue value
        
        Note:
            Delegates to min_value property (CODING_RULE_V2_00017)
        """
        return self.min_value  # Delegates to property

    def setMinValue(self, value: "TimeValue") -> "RequestResponseDelay":
        """
        AUTOSAR-compliant setter for minValue with method chaining.
        
        Args:
            value: The minValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to min_value property setter (gets validation automatically)
        """
        self.min_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_value(self, value: Optional["TimeValue"]) -> "RequestResponseDelay":
        """
        Set maxValue and return self for chaining.
        
        Args:
            value: The maxValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_value("value")
        """
        self.max_value = value  # Use property setter (gets validation)
        return self

    def with_min_value(self, value: Optional["TimeValue"]) -> "RequestResponseDelay":
        """
        Set minValue and return self for chaining.
        
        Args:
            value: The minValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_min_value("value")
        """
        self.min_value = value  # Use property setter (gets validation)
        return self



class SomeipSdServerEventGroupTimingConfig(ARElement):
    """
    EventGroup specific timing configuration settings.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::SomeipSdServerEventGroupTimingConfig
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 517, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The Service Discovery shall delay answers to unicast triggered by multicast
                # messages (e.
        # g.
        # after Offer Service).
        self._request: Optional["RequestResponseDelay"] = None

    @property
    def request(self) -> Optional["RequestResponseDelay"]:
        """Get request (Pythonic accessor)."""
        return self._request

    @request.setter
    def request(self, value: Optional["RequestResponseDelay"]) -> None:
        """
        Set request with validation.
        
        Args:
            value: The request to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._request = None
            return

        if not isinstance(value, RequestResponseDelay):
            raise TypeError(
                f"request must be RequestResponseDelay or None, got {type(value).__name__}"
            )
        self._request = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequest(self) -> "RequestResponseDelay":
        """
        AUTOSAR-compliant getter for request.
        
        Returns:
            The request value
        
        Note:
            Delegates to request property (CODING_RULE_V2_00017)
        """
        return self.request  # Delegates to property

    def setRequest(self, value: "RequestResponseDelay") -> "SomeipSdServerEventGroupTimingConfig":
        """
        AUTOSAR-compliant setter for request with method chaining.
        
        Args:
            value: The request to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to request property setter (gets validation automatically)
        """
        self.request = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_request(self, value: Optional["RequestResponseDelay"]) -> "SomeipSdServerEventGroupTimingConfig":
        """
        Set request and return self for chaining.
        
        Args:
            value: The request to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_request("value")
        """
        self.request = value  # Use property setter (gets validation)
        return self



class SomeipSdClientEventGroupTimingConfig(ARElement):
    """
    This meta-class is used to specify configuration related to service
    discovery in the context of an event group on SOME/IP.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::SomeipSdClientEventGroupTimingConfig
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 521, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The Service Discovery shall delay answers to unicast triggered by multicast
                # messages (e.
        # g.
        # after Offer Service).
        self._request: Optional["RequestResponseDelay"] = None

    @property
    def request(self) -> Optional["RequestResponseDelay"]:
        """Get request (Pythonic accessor)."""
        return self._request

    @request.setter
    def request(self, value: Optional["RequestResponseDelay"]) -> None:
        """
        Set request with validation.
        
        Args:
            value: The request to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._request = None
            return

        if not isinstance(value, RequestResponseDelay):
            raise TypeError(
                f"request must be RequestResponseDelay or None, got {type(value).__name__}"
            )
        self._request = value
        # This attribute define the maximum counts of retries to to an Eventgroup.
        # If the value is set to 0 no shall be done.
        # If the value is set to 255 the retry done as along as the Eventgroup is
                # requested SubscribeEventGroupAck was received.
        self._subscribe: Optional["PositiveInteger"] = None

    @property
    def subscribe(self) -> Optional["PositiveInteger"]:
        """Get subscribe (Pythonic accessor)."""
        return self._subscribe

    @subscribe.setter
    def subscribe(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set subscribe with validation.
        
        Args:
            value: The subscribe to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._subscribe = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"subscribe must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._subscribe = value
        # Defines the time in seconds the subscription of this event by the client.
        # this value is sent from the client server in the SD-subscribeEvent message.
        self._timeToLive: Optional["PositiveInteger"] = None

    @property
    def time_to_live(self) -> Optional["PositiveInteger"]:
        """Get timeToLive (Pythonic accessor)."""
        return self._timeToLive

    @time_to_live.setter
    def time_to_live(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set timeToLive with validation.
        
        Args:
            value: The timeToLive to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeToLive = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"timeToLive must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._timeToLive = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRequest(self) -> "RequestResponseDelay":
        """
        AUTOSAR-compliant getter for request.
        
        Returns:
            The request value
        
        Note:
            Delegates to request property (CODING_RULE_V2_00017)
        """
        return self.request  # Delegates to property

    def setRequest(self, value: "RequestResponseDelay") -> "SomeipSdClientEventGroupTimingConfig":
        """
        AUTOSAR-compliant setter for request with method chaining.
        
        Args:
            value: The request to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to request property setter (gets validation automatically)
        """
        self.request = value  # Delegates to property setter
        return self

    def getSubscribe(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for subscribe.
        
        Returns:
            The subscribe value
        
        Note:
            Delegates to subscribe property (CODING_RULE_V2_00017)
        """
        return self.subscribe  # Delegates to property

    def setSubscribe(self, value: "PositiveInteger") -> "SomeipSdClientEventGroupTimingConfig":
        """
        AUTOSAR-compliant setter for subscribe with method chaining.
        
        Args:
            value: The subscribe to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to subscribe property setter (gets validation automatically)
        """
        self.subscribe = value  # Delegates to property setter
        return self

    def getTimeToLive(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for timeToLive.
        
        Returns:
            The timeToLive value
        
        Note:
            Delegates to time_to_live property (CODING_RULE_V2_00017)
        """
        return self.time_to_live  # Delegates to property

    def setTimeToLive(self, value: "PositiveInteger") -> "SomeipSdClientEventGroupTimingConfig":
        """
        AUTOSAR-compliant setter for timeToLive with method chaining.
        
        Args:
            value: The timeToLive to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_to_live property setter (gets validation automatically)
        """
        self.time_to_live = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_request(self, value: Optional["RequestResponseDelay"]) -> "SomeipSdClientEventGroupTimingConfig":
        """
        Set request and return self for chaining.
        
        Args:
            value: The request to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_request("value")
        """
        self.request = value  # Use property setter (gets validation)
        return self

    def with_subscribe(self, value: Optional["PositiveInteger"]) -> "SomeipSdClientEventGroupTimingConfig":
        """
        Set subscribe and return self for chaining.
        
        Args:
            value: The subscribe to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_subscribe("value")
        """
        self.subscribe = value  # Use property setter (gets validation)
        return self

    def with_time_to_live(self, value: Optional["PositiveInteger"]) -> "SomeipSdClientEventGroupTimingConfig":
        """
        Set timeToLive and return self for chaining.
        
        Args:
            value: The timeToLive to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_to_live("value")
        """
        self.time_to_live = value  # Use property setter (gets validation)
        return self



class ConsumedProvidedServiceInstanceGroup(FibexElement):
    """
    The AUTOSAR ServiceDiscovery is able to start and to stop ClientServices and
    Server Services,respectively, at runtime. A SdServiceGroup contains several
    ClientServices and Server Services, respectively.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::ConsumedProvidedServiceInstanceGroup
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 523, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference assigns a set of ProvidedServiceInstances to the
                # ConsumedProvidedServiceInstanceGroup.
        # atpVariation.
        self._consumed: List["ConsumedService"] = []

    @property
    def consumed(self) -> List["ConsumedService"]:
        """Get consumed (Pythonic accessor)."""
        return self._consumed
        # This reference assigns a set of ConsumedService Instances to the
        # ConsumedProvidedServiceInstance atpVariation.
        self._providedService: List["ProvidedService"] = []

    @property
    def provided_service(self) -> List["ProvidedService"]:
        """Get providedService (Pythonic accessor)."""
        return self._providedService

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConsumed(self) -> List["ConsumedService"]:
        """
        AUTOSAR-compliant getter for consumed.
        
        Returns:
            The consumed value
        
        Note:
            Delegates to consumed property (CODING_RULE_V2_00017)
        """
        return self.consumed  # Delegates to property

    def getProvidedService(self) -> List["ProvidedService"]:
        """
        AUTOSAR-compliant getter for providedService.
        
        Returns:
            The providedService value
        
        Note:
            Delegates to provided_service property (CODING_RULE_V2_00017)
        """
        return self.provided_service  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class StaticSocketConnection(Identifiable):
    """
    Definition of static SocketConnection between the Socket that is defined by
    the aggregating Socket Address and the remoteAddress.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::StaticSocketConnection
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 543, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Assignment of IPduIdentifiers that are transmitted over SocketConnection.
        # atpVariation 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._iPduIdentifier: List["SoConIPduIdentifier"] = []

    @property
    def i_pdu_identifier(self) -> List["SoConIPduIdentifier"]:
        """Get iPduIdentifier (Pythonic accessor)."""
        return self._iPduIdentifier
        # RemoteAddress of the static SocketConnection.
        # atpVariation.
        self._remoteAddress: Optional["SocketAddress"] = None

    @property
    def remote_address(self) -> Optional["SocketAddress"]:
        """Get remoteAddress (Pythonic accessor)."""
        return self._remoteAddress

    @remote_address.setter
    def remote_address(self, value: Optional["SocketAddress"]) -> None:
        """
        Set remoteAddress with validation.
        
        Args:
            value: The remoteAddress to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._remoteAddress = None
            return

        if not isinstance(value, SocketAddress):
            raise TypeError(
                f"remoteAddress must be SocketAddress or None, got {type(value).__name__}"
            )
        self._remoteAddress = value
        # Specifies the time in seconds how long TCP connect are repeated to reach
                # SOAD_SOCON_ONLINE.
        # is restricted to socket connection groups initiating a TCP connection and are
                # under SoAd.
        self._tcpConnect: Optional["TimeValue"] = None

    @property
    def tcp_connect(self) -> Optional["TimeValue"]:
        """Get tcpConnect (Pythonic accessor)."""
        return self._tcpConnect

    @tcp_connect.setter
    def tcp_connect(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpConnect with validation.
        
        Args:
            value: The tcpConnect to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpConnect = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpConnect must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpConnect = value
        # Defines whether the local Address (that is aggregating does a listen or a
        # connect.
        self._tcpRole: Optional["TcpRoleEnum"] = None

    @property
    def tcp_role(self) -> Optional["TcpRoleEnum"]:
        """Get tcpRole (Pythonic accessor)."""
        return self._tcpRole

    @tcp_role.setter
    def tcp_role(self, value: Optional["TcpRoleEnum"]) -> None:
        """
        Set tcpRole with validation.
        
        Args:
            value: The tcpRole to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpRole = None
            return

        if not isinstance(value, TcpRoleEnum):
            raise TypeError(
                f"tcpRole must be TcpRoleEnum or None, got {type(value).__name__}"
            )
        self._tcpRole = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPduIdentifier(self) -> List["SoConIPduIdentifier"]:
        """
        AUTOSAR-compliant getter for iPduIdentifier.
        
        Returns:
            The iPduIdentifier value
        
        Note:
            Delegates to i_pdu_identifier property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_identifier  # Delegates to property

    def getRemoteAddress(self) -> "SocketAddress":
        """
        AUTOSAR-compliant getter for remoteAddress.
        
        Returns:
            The remoteAddress value
        
        Note:
            Delegates to remote_address property (CODING_RULE_V2_00017)
        """
        return self.remote_address  # Delegates to property

    def setRemoteAddress(self, value: "SocketAddress") -> "StaticSocketConnection":
        """
        AUTOSAR-compliant setter for remoteAddress with method chaining.
        
        Args:
            value: The remoteAddress to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to remote_address property setter (gets validation automatically)
        """
        self.remote_address = value  # Delegates to property setter
        return self

    def getTcpConnect(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpConnect.
        
        Returns:
            The tcpConnect value
        
        Note:
            Delegates to tcp_connect property (CODING_RULE_V2_00017)
        """
        return self.tcp_connect  # Delegates to property

    def setTcpConnect(self, value: "TimeValue") -> "StaticSocketConnection":
        """
        AUTOSAR-compliant setter for tcpConnect with method chaining.
        
        Args:
            value: The tcpConnect to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tcp_connect property setter (gets validation automatically)
        """
        self.tcp_connect = value  # Delegates to property setter
        return self

    def getTcpRole(self) -> "TcpRoleEnum":
        """
        AUTOSAR-compliant getter for tcpRole.
        
        Returns:
            The tcpRole value
        
        Note:
            Delegates to tcp_role property (CODING_RULE_V2_00017)
        """
        return self.tcp_role  # Delegates to property

    def setTcpRole(self, value: "TcpRoleEnum") -> "StaticSocketConnection":
        """
        AUTOSAR-compliant setter for tcpRole with method chaining.
        
        Args:
            value: The tcpRole to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tcp_role property setter (gets validation automatically)
        """
        self.tcp_role = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_remote_address(self, value: Optional["SocketAddress"]) -> "StaticSocketConnection":
        """
        Set remoteAddress and return self for chaining.
        
        Args:
            value: The remoteAddress to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_remote_address("value")
        """
        self.remote_address = value  # Use property setter (gets validation)
        return self

    def with_tcp_connect(self, value: Optional["TimeValue"]) -> "StaticSocketConnection":
        """
        Set tcpConnect and return self for chaining.
        
        Args:
            value: The tcpConnect to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tcp_connect("value")
        """
        self.tcp_connect = value  # Use property setter (gets validation)
        return self

    def with_tcp_role(self, value: Optional["TcpRoleEnum"]) -> "StaticSocketConnection":
        """
        Set tcpRole and return self for chaining.
        
        Args:
            value: The tcpRole to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tcp_role("value")
        """
        self.tcp_role = value  # Use property setter (gets validation)
        return self



class SomeipSdClientServiceInstanceConfig(ARElement):
    """
    Client specific settings that are relevant for the configuration of SOME/IP
    Service-Discovery.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::SomeipSdClientServiceInstanceConfig
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2058, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Controls initial find behavior of clients.
        self._initialFindBehavior: Optional["InitialSdDelayConfig"] = None

    @property
    def initial_find_behavior(self) -> Optional["InitialSdDelayConfig"]:
        """Get initialFindBehavior (Pythonic accessor)."""
        return self._initialFindBehavior

    @initial_find_behavior.setter
    def initial_find_behavior(self, value: Optional["InitialSdDelayConfig"]) -> None:
        """
        Set initialFindBehavior with validation.
        
        Args:
            value: The initialFindBehavior to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialFindBehavior = None
            return

        if not isinstance(value, InitialSdDelayConfig):
            raise TypeError(
                f"initialFindBehavior must be InitialSdDelayConfig or None, got {type(value).__name__}"
            )
        self._initialFindBehavior = value
        # This attribute defines the VLAN frame priority for Service that result from
        # RequiredSomeip are referncing this SomeipSdClient SubscribeEventGroup, Stop
        # from 0 (best effort) to 7 allowed.
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value
        # This attribute represents the ability to define the time in the service find
                # is valid.
        # Note! The TTL value for is not used and shall be ignored by service.
        # This configuration is only kept for Default value if not specified shall.
        self._serviceFind: Optional["PositiveInteger"] = None

    @property
    def service_find(self) -> Optional["PositiveInteger"]:
        """Get serviceFind (Pythonic accessor)."""
        return self._serviceFind

    @service_find.setter
    def service_find(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set serviceFind with validation.
        
        Args:
            value: The serviceFind to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceFind = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"serviceFind must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._serviceFind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitialFindBehavior(self) -> "InitialSdDelayConfig":
        """
        AUTOSAR-compliant getter for initialFindBehavior.
        
        Returns:
            The initialFindBehavior value
        
        Note:
            Delegates to initial_find_behavior property (CODING_RULE_V2_00017)
        """
        return self.initial_find_behavior  # Delegates to property

    def setInitialFindBehavior(self, value: "InitialSdDelayConfig") -> "SomeipSdClientServiceInstanceConfig":
        """
        AUTOSAR-compliant setter for initialFindBehavior with method chaining.
        
        Args:
            value: The initialFindBehavior to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to initial_find_behavior property setter (gets validation automatically)
        """
        self.initial_find_behavior = value  # Delegates to property setter
        return self

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.
        
        Returns:
            The priority value
        
        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "SomeipSdClientServiceInstanceConfig":
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

    def getServiceFind(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for serviceFind.
        
        Returns:
            The serviceFind value
        
        Note:
            Delegates to service_find property (CODING_RULE_V2_00017)
        """
        return self.service_find  # Delegates to property

    def setServiceFind(self, value: "PositiveInteger") -> "SomeipSdClientServiceInstanceConfig":
        """
        AUTOSAR-compliant setter for serviceFind with method chaining.
        
        Args:
            value: The serviceFind to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to service_find property setter (gets validation automatically)
        """
        self.service_find = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_initial_find_behavior(self, value: Optional["InitialSdDelayConfig"]) -> "SomeipSdClientServiceInstanceConfig":
        """
        Set initialFindBehavior and return self for chaining.
        
        Args:
            value: The initialFindBehavior to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_initial_find_behavior("value")
        """
        self.initial_find_behavior = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "SomeipSdClientServiceInstanceConfig":
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

    def with_service_find(self, value: Optional["PositiveInteger"]) -> "SomeipSdClientServiceInstanceConfig":
        """
        Set serviceFind and return self for chaining.
        
        Args:
            value: The serviceFind to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_service_find("value")
        """
        self.service_find = value  # Use property setter (gets validation)
        return self



class SomeipServiceVersion(ARObject):
    """
    This meta-class represents the ability to describe a version of a SOME/IP
    Service.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::SomeipServiceVersion
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2059, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Major Version of the ServiceInterface.
        self._majorVersion: Optional["PositiveInteger"] = None

    @property
    def major_version(self) -> Optional["PositiveInteger"]:
        """Get majorVersion (Pythonic accessor)."""
        return self._majorVersion

    @major_version.setter
    def major_version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set majorVersion with validation.
        
        Args:
            value: The majorVersion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._majorVersion = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"majorVersion must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._majorVersion = value
        # Minor Version of the ServiceInterface.
        self._minorVersion: Optional["PositiveInteger"] = None

    @property
    def minor_version(self) -> Optional["PositiveInteger"]:
        """Get minorVersion (Pythonic accessor)."""
        return self._minorVersion

    @minor_version.setter
    def minor_version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minorVersion with validation.
        
        Args:
            value: The minorVersion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minorVersion = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minorVersion must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minorVersion = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMajorVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for majorVersion.
        
        Returns:
            The majorVersion value
        
        Note:
            Delegates to major_version property (CODING_RULE_V2_00017)
        """
        return self.major_version  # Delegates to property

    def setMajorVersion(self, value: "PositiveInteger") -> "SomeipServiceVersion":
        """
        AUTOSAR-compliant setter for majorVersion with method chaining.
        
        Args:
            value: The majorVersion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to major_version property setter (gets validation automatically)
        """
        self.major_version = value  # Delegates to property setter
        return self

    def getMinorVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minorVersion.
        
        Returns:
            The minorVersion value
        
        Note:
            Delegates to minor_version property (CODING_RULE_V2_00017)
        """
        return self.minor_version  # Delegates to property

    def setMinorVersion(self, value: "PositiveInteger") -> "SomeipServiceVersion":
        """
        AUTOSAR-compliant setter for minorVersion with method chaining.
        
        Args:
            value: The minorVersion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to minor_version property setter (gets validation automatically)
        """
        self.minor_version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_major_version(self, value: Optional["PositiveInteger"]) -> "SomeipServiceVersion":
        """
        Set majorVersion and return self for chaining.
        
        Args:
            value: The majorVersion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_major_version("value")
        """
        self.major_version = value  # Use property setter (gets validation)
        return self

    def with_minor_version(self, value: Optional["PositiveInteger"]) -> "SomeipServiceVersion":
        """
        Set minorVersion and return self for chaining.
        
        Args:
            value: The minorVersion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_minor_version("value")
        """
        self.minor_version = value  # Use property setter (gets validation)
        return self



class ConsumedServiceInstance(AbstractServiceInstance):
    """
    Service instances that are consumed by the ECU that is connected via the
    ApplicationEndpoint to a CommunicationConnector.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::ConsumedServiceInstance
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 980, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 500, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # NetworkEndpoint on which the ProvidedServiceInstance is communicating with
                # this ConsumedService allowed to be located so that the ACL check in is
                # successful and the connection is be established.
        # atpVariation.
        self._allowedService: List["NetworkEndpoint"] = []

    @property
    def allowed_service(self) -> List["NetworkEndpoint"]:
        """Get allowedService (Pythonic accessor)."""
        return self._allowedService
        # Defines that this ConsumedServiceInstance shall be for) by the service
        # discovery at ECU.
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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"autoRequire must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._autoRequire = value
        # Collection of blocklisted versions atp.
        # Status=draft.
        self._blocklisted: List["SomeipServiceVersion"] = []

    @property
    def blocklisted(self) -> List["SomeipServiceVersion"]:
        """Get blocklisted (Pythonic accessor)."""
        return self._blocklisted
        # Selection of event-groups the consumer wants to for.
        # atpVariation.
        self._consumedEvent: List["RefType"] = []

    @property
    def consumed_event(self) -> List["RefType"]:
        """Get consumedEvent (Pythonic accessor)."""
        return self._consumedEvent
        # Multicast Address that is used by the client to subscribe the server: This
        # enables the multicast subscription atpVariation.
        self._eventMulticast: Optional["ApplicationEndpoint"] = None

    @property
    def event_multicast(self) -> Optional["ApplicationEndpoint"]:
        """Get eventMulticast (Pythonic accessor)."""
        return self._eventMulticast

    @event_multicast.setter
    def event_multicast(self, value: Optional["ApplicationEndpoint"]) -> None:
        """
        Set eventMulticast with validation.
        
        Args:
            value: The eventMulticast to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventMulticast = None
            return

        if not isinstance(value, ApplicationEndpoint):
            raise TypeError(
                f"eventMulticast must be ApplicationEndpoint or None, got {type(value).__name__}"
            )
        self._eventMulticast = value
        # This attribute represents the ability to describe the service instance ID.
        self._instance: Optional["AnyServiceInstanceId"] = None

    @property
    def instance(self) -> Optional["AnyServiceInstanceId"]:
        """Get instance (Pythonic accessor)."""
        return self._instance

    @instance.setter
    def instance(self, value: Optional["AnyServiceInstanceId"]) -> None:
        """
        Set instance with validation.
        
        Args:
            value: The instance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._instance = None
            return

        if not isinstance(value, AnyServiceInstanceId):
            raise TypeError(
                f"instance must be AnyServiceInstanceId or None, got {type(value).__name__}"
            )
        self._instance = value
        # or both).
        # atpVariation.
        self._localUnicast: "ApplicationEndpoint" = None

    @property
    def local_unicast(self) -> "ApplicationEndpoint":
        """Get localUnicast (Pythonic accessor)."""
        return self._localUnicast

    @local_unicast.setter
    def local_unicast(self, value: "ApplicationEndpoint") -> None:
        """
        Set localUnicast with validation.
        
        Args:
            value: The localUnicast to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, ApplicationEndpoint):
            raise TypeError(
                f"localUnicast must be ApplicationEndpoint, got {type(value).__name__}"
            )
        self._localUnicast = value
        # Minor Version of the ServiceInterface.
        # Value can be set to that represents the Minor Version of the or to ANY.
        self._minorVersion: Optional["AnyVersionString"] = None

    @property
    def minor_version(self) -> Optional["AnyVersionString"]:
        """Get minorVersion (Pythonic accessor)."""
        return self._minorVersion

    @minor_version.setter
    def minor_version(self, value: Optional["AnyVersionString"]) -> None:
        """
        Set minorVersion with validation.
        
        Args:
            value: The minorVersion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minorVersion = None
            return

        if not isinstance(value, AnyVersionString):
            raise TypeError(
                f"minorVersion must be AnyVersionString or None, got {type(value).__name__}"
            )
        self._minorVersion = value
        # Reference to a providedServiceInstance to get the instanceIdentifier
        # information from the ProvidedService 1228 Document ID 62:
        # AUTOSAR_CP_TPS_SoftwareComponentTemplate Template R23-11.
        self._providedService: Optional["ProvidedService"] = None

    @property
    def provided_service(self) -> Optional["ProvidedService"]:
        """Get providedService (Pythonic accessor)."""
        return self._providedService

    @provided_service.setter
    def provided_service(self, value: Optional["ProvidedService"]) -> None:
        """
        Set providedService with validation.
        
        Args:
            value: The providedService to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._providedService = None
            return

        if not isinstance(value, ProvidedService):
            raise TypeError(
                f"providedService must be ProvidedService or None, got {type(value).__name__}"
            )
        self._providedService = value
        # provider is located.
        # This reference shall ONLY be the remote address is determined from the not at
                # runtime from the Service atpVariation.
        self._remoteUnicast: "ApplicationEndpoint" = None

    @property
    def remote_unicast(self) -> "ApplicationEndpoint":
        """Get remoteUnicast (Pythonic accessor)."""
        return self._remoteUnicast

    @remote_unicast.setter
    def remote_unicast(self, value: "ApplicationEndpoint") -> None:
        """
        Set remoteUnicast with validation.
        
        Args:
            value: The remoteUnicast to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, ApplicationEndpoint):
            raise TypeError(
                f"remoteUnicast must be ApplicationEndpoint, got {type(value).__name__}"
            )
        self._remoteUnicast = value
        # Service Discovery Client configuration.
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
        # Client specific configuration settings relevant for the SOME/IP service
                # discovery.
        # atpVariation.
        self._sdClientTimer: Optional["SomeipSdClientService"] = None

    @property
    def sd_client_timer(self) -> Optional["SomeipSdClientService"]:
        """Get sdClientTimer (Pythonic accessor)."""
        return self._sdClientTimer

    @sd_client_timer.setter
    def sd_client_timer(self, value: Optional["SomeipSdClientService"]) -> None:
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

        if not isinstance(value, SomeipSdClientService):
            raise TypeError(
                f"sdClientTimer must be SomeipSdClientService or None, got {type(value).__name__}"
            )
        self._sdClientTimer = value
        # This attribute represents the ability to describe the SOME/ ID that is
        # searched.
        self._serviceIdentifier: Optional["PositiveInteger"] = None

    @property
    def service_identifier(self) -> Optional["PositiveInteger"]:
        """Get serviceIdentifier (Pythonic accessor)."""
        return self._serviceIdentifier

    @service_identifier.setter
    def service_identifier(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set serviceIdentifier with validation.
        
        Args:
            value: The serviceIdentifier to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceIdentifier = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"serviceIdentifier must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._serviceIdentifier = value
        # Defines the service discovery find behavior.
        # Tags: atp.
        # Status=draft.
        self._versionDriven: Optional["ServiceVersion"] = None

    @property
    def version_driven(self) -> Optional["ServiceVersion"]:
        """Get versionDriven (Pythonic accessor)."""
        return self._versionDriven

    @version_driven.setter
    def version_driven(self, value: Optional["ServiceVersion"]) -> None:
        """
        Set versionDriven with validation.
        
        Args:
            value: The versionDriven to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._versionDriven = None
            return

        if not isinstance(value, ServiceVersion):
            raise TypeError(
                f"versionDriven must be ServiceVersion or None, got {type(value).__name__}"
            )
        self._versionDriven = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllowedService(self) -> List["NetworkEndpoint"]:
        """
        AUTOSAR-compliant getter for allowedService.
        
        Returns:
            The allowedService value
        
        Note:
            Delegates to allowed_service property (CODING_RULE_V2_00017)
        """
        return self.allowed_service  # Delegates to property

    def getAutoRequire(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for autoRequire.
        
        Returns:
            The autoRequire value
        
        Note:
            Delegates to auto_require property (CODING_RULE_V2_00017)
        """
        return self.auto_require  # Delegates to property

    def setAutoRequire(self, value: "Boolean") -> "ConsumedServiceInstance":
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

    def getBlocklisted(self) -> List["SomeipServiceVersion"]:
        """
        AUTOSAR-compliant getter for blocklisted.
        
        Returns:
            The blocklisted value
        
        Note:
            Delegates to blocklisted property (CODING_RULE_V2_00017)
        """
        return self.blocklisted  # Delegates to property

    def getConsumedEvent(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for consumedEvent.
        
        Returns:
            The consumedEvent value
        
        Note:
            Delegates to consumed_event property (CODING_RULE_V2_00017)
        """
        return self.consumed_event  # Delegates to property

    def getEventMulticast(self) -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant getter for eventMulticast.
        
        Returns:
            The eventMulticast value
        
        Note:
            Delegates to event_multicast property (CODING_RULE_V2_00017)
        """
        return self.event_multicast  # Delegates to property

    def setEventMulticast(self, value: "ApplicationEndpoint") -> "ConsumedServiceInstance":
        """
        AUTOSAR-compliant setter for eventMulticast with method chaining.
        
        Args:
            value: The eventMulticast to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to event_multicast property setter (gets validation automatically)
        """
        self.event_multicast = value  # Delegates to property setter
        return self

    def getInstance(self) -> "AnyServiceInstanceId":
        """
        AUTOSAR-compliant getter for instance.
        
        Returns:
            The instance value
        
        Note:
            Delegates to instance property (CODING_RULE_V2_00017)
        """
        return self.instance  # Delegates to property

    def setInstance(self, value: "AnyServiceInstanceId") -> "ConsumedServiceInstance":
        """
        AUTOSAR-compliant setter for instance with method chaining.
        
        Args:
            value: The instance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to instance property setter (gets validation automatically)
        """
        self.instance = value  # Delegates to property setter
        return self

    def getLocalUnicast(self) -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant getter for localUnicast.
        
        Returns:
            The localUnicast value
        
        Note:
            Delegates to local_unicast property (CODING_RULE_V2_00017)
        """
        return self.local_unicast  # Delegates to property

    def setLocalUnicast(self, value: "ApplicationEndpoint") -> "ConsumedServiceInstance":
        """
        AUTOSAR-compliant setter for localUnicast with method chaining.
        
        Args:
            value: The localUnicast to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to local_unicast property setter (gets validation automatically)
        """
        self.local_unicast = value  # Delegates to property setter
        return self

    def getMinorVersion(self) -> "AnyVersionString":
        """
        AUTOSAR-compliant getter for minorVersion.
        
        Returns:
            The minorVersion value
        
        Note:
            Delegates to minor_version property (CODING_RULE_V2_00017)
        """
        return self.minor_version  # Delegates to property

    def setMinorVersion(self, value: "AnyVersionString") -> "ConsumedServiceInstance":
        """
        AUTOSAR-compliant setter for minorVersion with method chaining.
        
        Args:
            value: The minorVersion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to minor_version property setter (gets validation automatically)
        """
        self.minor_version = value  # Delegates to property setter
        return self

    def getProvidedService(self) -> "ProvidedService":
        """
        AUTOSAR-compliant getter for providedService.
        
        Returns:
            The providedService value
        
        Note:
            Delegates to provided_service property (CODING_RULE_V2_00017)
        """
        return self.provided_service  # Delegates to property

    def setProvidedService(self, value: "ProvidedService") -> "ConsumedServiceInstance":
        """
        AUTOSAR-compliant setter for providedService with method chaining.
        
        Args:
            value: The providedService to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to provided_service property setter (gets validation automatically)
        """
        self.provided_service = value  # Delegates to property setter
        return self

    def getRemoteUnicast(self) -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant getter for remoteUnicast.
        
        Returns:
            The remoteUnicast value
        
        Note:
            Delegates to remote_unicast property (CODING_RULE_V2_00017)
        """
        return self.remote_unicast  # Delegates to property

    def setRemoteUnicast(self, value: "ApplicationEndpoint") -> "ConsumedServiceInstance":
        """
        AUTOSAR-compliant setter for remoteUnicast with method chaining.
        
        Args:
            value: The remoteUnicast to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to remote_unicast property setter (gets validation automatically)
        """
        self.remote_unicast = value  # Delegates to property setter
        return self

    def getSdClientConfig(self) -> "SdClientConfig":
        """
        AUTOSAR-compliant getter for sdClientConfig.
        
        Returns:
            The sdClientConfig value
        
        Note:
            Delegates to sd_client_config property (CODING_RULE_V2_00017)
        """
        return self.sd_client_config  # Delegates to property

    def setSdClientConfig(self, value: "SdClientConfig") -> "ConsumedServiceInstance":
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

    def getSdClientTimer(self) -> "SomeipSdClientService":
        """
        AUTOSAR-compliant getter for sdClientTimer.
        
        Returns:
            The sdClientTimer value
        
        Note:
            Delegates to sd_client_timer property (CODING_RULE_V2_00017)
        """
        return self.sd_client_timer  # Delegates to property

    def setSdClientTimer(self, value: "SomeipSdClientService") -> "ConsumedServiceInstance":
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

    def getServiceIdentifier(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for serviceIdentifier.
        
        Returns:
            The serviceIdentifier value
        
        Note:
            Delegates to service_identifier property (CODING_RULE_V2_00017)
        """
        return self.service_identifier  # Delegates to property

    def setServiceIdentifier(self, value: "PositiveInteger") -> "ConsumedServiceInstance":
        """
        AUTOSAR-compliant setter for serviceIdentifier with method chaining.
        
        Args:
            value: The serviceIdentifier to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to service_identifier property setter (gets validation automatically)
        """
        self.service_identifier = value  # Delegates to property setter
        return self

    def getVersionDriven(self) -> "ServiceVersion":
        """
        AUTOSAR-compliant getter for versionDriven.
        
        Returns:
            The versionDriven value
        
        Note:
            Delegates to version_driven property (CODING_RULE_V2_00017)
        """
        return self.version_driven  # Delegates to property

    def setVersionDriven(self, value: "ServiceVersion") -> "ConsumedServiceInstance":
        """
        AUTOSAR-compliant setter for versionDriven with method chaining.
        
        Args:
            value: The versionDriven to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to version_driven property setter (gets validation automatically)
        """
        self.version_driven = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_auto_require(self, value: Optional["Boolean"]) -> "ConsumedServiceInstance":
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

    def with_event_multicast(self, value: Optional["ApplicationEndpoint"]) -> "ConsumedServiceInstance":
        """
        Set eventMulticast and return self for chaining.
        
        Args:
            value: The eventMulticast to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_event_multicast("value")
        """
        self.event_multicast = value  # Use property setter (gets validation)
        return self

    def with_instance(self, value: Optional["AnyServiceInstanceId"]) -> "ConsumedServiceInstance":
        """
        Set instance and return self for chaining.
        
        Args:
            value: The instance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_instance("value")
        """
        self.instance = value  # Use property setter (gets validation)
        return self

    def with_local_unicast(self, value: "ApplicationEndpoint") -> "ConsumedServiceInstance":
        """
        Set localUnicast and return self for chaining.
        
        Args:
            value: The localUnicast to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_local_unicast("value")
        """
        self.local_unicast = value  # Use property setter (gets validation)
        return self

    def with_minor_version(self, value: Optional["AnyVersionString"]) -> "ConsumedServiceInstance":
        """
        Set minorVersion and return self for chaining.
        
        Args:
            value: The minorVersion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_minor_version("value")
        """
        self.minor_version = value  # Use property setter (gets validation)
        return self

    def with_provided_service(self, value: Optional["ProvidedService"]) -> "ConsumedServiceInstance":
        """
        Set providedService and return self for chaining.
        
        Args:
            value: The providedService to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_provided_service("value")
        """
        self.provided_service = value  # Use property setter (gets validation)
        return self

    def with_remote_unicast(self, value: "ApplicationEndpoint") -> "ConsumedServiceInstance":
        """
        Set remoteUnicast and return self for chaining.
        
        Args:
            value: The remoteUnicast to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_remote_unicast("value")
        """
        self.remote_unicast = value  # Use property setter (gets validation)
        return self

    def with_sd_client_config(self, value: Optional["SdClientConfig"]) -> "ConsumedServiceInstance":
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

    def with_sd_client_timer(self, value: Optional["SomeipSdClientService"]) -> "ConsumedServiceInstance":
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

    def with_service_identifier(self, value: Optional["PositiveInteger"]) -> "ConsumedServiceInstance":
        """
        Set serviceIdentifier and return self for chaining.
        
        Args:
            value: The serviceIdentifier to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_service_identifier("value")
        """
        self.service_identifier = value  # Use property setter (gets validation)
        return self

    def with_version_driven(self, value: Optional["ServiceVersion"]) -> "ConsumedServiceInstance":
        """
        Set versionDriven and return self for chaining.
        
        Args:
            value: The versionDriven to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_version_driven("value")
        """
        self.version_driven = value  # Use property setter (gets validation)
        return self



class ProvidedServiceInstance(AbstractServiceInstance):
    """
    Service instances that are provided by the ECU that is connected via the
    ApplicationEndpoint to a CommunicationConnector.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::ProvidedServiceInstance
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1000, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 485, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # NetworkEndpoints on which the ConsumedService that are communicating with
                # this Provided allowed to be located so that the in the ServiceDiscovery is
                # successful and the allowed to be established.
        # atpVariation.
        self._allowedService: List["NetworkEndpoint"] = []

    @property
    def allowed_service(self) -> List["NetworkEndpoint"]:
        """Get allowedService (Pythonic accessor)."""
        return self._allowedService
        # Defines that this ProvidedServiceInstance shall be the service discovery at
        # ECU start.
        self._autoAvailable: Optional["Boolean"] = None

    @property
    def auto_available(self) -> Optional["Boolean"]:
        """Get autoAvailable (Pythonic accessor)."""
        return self._autoAvailable

    @auto_available.setter
    def auto_available(self, value: Optional["Boolean"]) -> None:
        """
        Set autoAvailable with validation.
        
        Args:
            value: The autoAvailable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._autoAvailable = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"autoAvailable must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._autoAvailable = value
        # Collection of event groups provided by the Provided atpVariation.
        self._eventHandler: List["EventHandler"] = []

    @property
    def event_handler(self) -> List["EventHandler"]:
        """Get eventHandler (Pythonic accessor)."""
        return self._eventHandler
        # Instance identifier.
        # Can be used for e.
        # g.
        # service discovery identify the instance of the service.
        self._instance: Optional["PositiveInteger"] = None

    @property
    def instance(self) -> Optional["PositiveInteger"]:
        """Get instance (Pythonic accessor)."""
        return self._instance

    @instance.setter
    def instance(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set instance with validation.
        
        Args:
            value: The instance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._instance = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"instance must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._instance = value
        # Defines the value to be used for load balancing weight in service offer.
        # Higher value means higher probability to.
        self._loadBalancing: Optional["PositiveInteger"] = None

    @property
    def load_balancing(self) -> Optional["PositiveInteger"]:
        """Get loadBalancing (Pythonic accessor)."""
        return self._loadBalancing

    @load_balancing.setter
    def load_balancing(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set loadBalancing with validation.
        
        Args:
            value: The loadBalancing to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._loadBalancing = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"loadBalancing must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._loadBalancing = value
        # or both).
        # atpVariation.
        self._localUnicast: "ApplicationEndpoint" = None

    @property
    def local_unicast(self) -> "ApplicationEndpoint":
        """Get localUnicast (Pythonic accessor)."""
        return self._localUnicast

    @local_unicast.setter
    def local_unicast(self, value: "ApplicationEndpoint") -> None:
        """
        Set localUnicast with validation.
        
        Args:
            value: The localUnicast to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, ApplicationEndpoint):
            raise TypeError(
                f"localUnicast must be ApplicationEndpoint, got {type(value).__name__}"
            )
        self._localUnicast = value
        # Minor Version of the Service that is provided by this.
        self._minorVersion: Optional["PositiveInteger"] = None

    @property
    def minor_version(self) -> Optional["PositiveInteger"]:
        """Get minorVersion (Pythonic accessor)."""
        return self._minorVersion

    @minor_version.setter
    def minor_version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minorVersion with validation.
        
        Args:
            value: The minorVersion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minorVersion = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minorVersion must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minorVersion = value
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value
        # This reference defines the remote multicast subscribed of service consumers.
        # This reference shall be used if the remote address of the clients is the
                # configuration and not at runtime.
        # atpVariation.
        self._remoteMulticast: List["ApplicationEndpoint"] = []

    @property
    def remote_multicast(self) -> List["ApplicationEndpoint"]:
        """Get remoteMulticast (Pythonic accessor)."""
        return self._remoteMulticast
        # This reference defines the remote addresses of service This reference shall
                # ONLY be used if the of the clients is determined from the not at runtime.
        # atpVariation 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate
                # Template R23-11.
        self._remoteUnicast: List["ApplicationEndpoint"] = []

    @property
    def remote_unicast(self) -> List["ApplicationEndpoint"]:
        """Get remoteUnicast (Pythonic accessor)."""
        return self._remoteUnicast
        # Service Discovery Server configuration.
        self._sdServerConfig: Optional["SdServerConfig"] = None

    @property
    def sd_server_config(self) -> Optional["SdServerConfig"]:
        """Get sdServerConfig (Pythonic accessor)."""
        return self._sdServerConfig

    @sd_server_config.setter
    def sd_server_config(self, value: Optional["SdServerConfig"]) -> None:
        """
        Set sdServerConfig with validation.
        
        Args:
            value: The sdServerConfig to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdServerConfig = None
            return

        if not isinstance(value, SdServerConfig):
            raise TypeError(
                f"sdServerConfig must be SdServerConfig or None, got {type(value).__name__}"
            )
        self._sdServerConfig = value
        # Server specific configuration settings relevant for the SOME/IP service
                # discovery.
        # atpVariation.
        self._sdServerTimer: Optional["SomeipSdServer"] = None

    @property
    def sd_server_timer(self) -> Optional["SomeipSdServer"]:
        """Get sdServerTimer (Pythonic accessor)."""
        return self._sdServerTimer

    @sd_server_timer.setter
    def sd_server_timer(self, value: Optional["SomeipSdServer"]) -> None:
        """
        Set sdServerTimer with validation.
        
        Args:
            value: The sdServerTimer to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdServerTimer = None
            return

        if not isinstance(value, SomeipSdServer):
            raise TypeError(
                f"sdServerTimer must be SomeipSdServer or None, got {type(value).__name__}"
            )
        self._sdServerTimer = value
        # This attribute represents the ability to describe the SOME/ ID that is
        # offered.
        self._serviceIdentifier: Optional["PositiveInteger"] = None

    @property
    def service_identifier(self) -> Optional["PositiveInteger"]:
        """Get serviceIdentifier (Pythonic accessor)."""
        return self._serviceIdentifier

    @service_identifier.setter
    def service_identifier(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set serviceIdentifier with validation.
        
        Args:
            value: The serviceIdentifier to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceIdentifier = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"serviceIdentifier must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._serviceIdentifier = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllowedService(self) -> List["NetworkEndpoint"]:
        """
        AUTOSAR-compliant getter for allowedService.
        
        Returns:
            The allowedService value
        
        Note:
            Delegates to allowed_service property (CODING_RULE_V2_00017)
        """
        return self.allowed_service  # Delegates to property

    def getAutoAvailable(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for autoAvailable.
        
        Returns:
            The autoAvailable value
        
        Note:
            Delegates to auto_available property (CODING_RULE_V2_00017)
        """
        return self.auto_available  # Delegates to property

    def setAutoAvailable(self, value: "Boolean") -> "ProvidedServiceInstance":
        """
        AUTOSAR-compliant setter for autoAvailable with method chaining.
        
        Args:
            value: The autoAvailable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to auto_available property setter (gets validation automatically)
        """
        self.auto_available = value  # Delegates to property setter
        return self

    def getEventHandler(self) -> List["EventHandler"]:
        """
        AUTOSAR-compliant getter for eventHandler.
        
        Returns:
            The eventHandler value
        
        Note:
            Delegates to event_handler property (CODING_RULE_V2_00017)
        """
        return self.event_handler  # Delegates to property

    def getInstance(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for instance.
        
        Returns:
            The instance value
        
        Note:
            Delegates to instance property (CODING_RULE_V2_00017)
        """
        return self.instance  # Delegates to property

    def setInstance(self, value: "PositiveInteger") -> "ProvidedServiceInstance":
        """
        AUTOSAR-compliant setter for instance with method chaining.
        
        Args:
            value: The instance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to instance property setter (gets validation automatically)
        """
        self.instance = value  # Delegates to property setter
        return self

    def getLoadBalancing(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for loadBalancing.
        
        Returns:
            The loadBalancing value
        
        Note:
            Delegates to load_balancing property (CODING_RULE_V2_00017)
        """
        return self.load_balancing  # Delegates to property

    def setLoadBalancing(self, value: "PositiveInteger") -> "ProvidedServiceInstance":
        """
        AUTOSAR-compliant setter for loadBalancing with method chaining.
        
        Args:
            value: The loadBalancing to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to load_balancing property setter (gets validation automatically)
        """
        self.load_balancing = value  # Delegates to property setter
        return self

    def getLocalUnicast(self) -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant getter for localUnicast.
        
        Returns:
            The localUnicast value
        
        Note:
            Delegates to local_unicast property (CODING_RULE_V2_00017)
        """
        return self.local_unicast  # Delegates to property

    def setLocalUnicast(self, value: "ApplicationEndpoint") -> "ProvidedServiceInstance":
        """
        AUTOSAR-compliant setter for localUnicast with method chaining.
        
        Args:
            value: The localUnicast to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to local_unicast property setter (gets validation automatically)
        """
        self.local_unicast = value  # Delegates to property setter
        return self

    def getMinorVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minorVersion.
        
        Returns:
            The minorVersion value
        
        Note:
            Delegates to minor_version property (CODING_RULE_V2_00017)
        """
        return self.minor_version  # Delegates to property

    def setMinorVersion(self, value: "PositiveInteger") -> "ProvidedServiceInstance":
        """
        AUTOSAR-compliant setter for minorVersion with method chaining.
        
        Args:
            value: The minorVersion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to minor_version property setter (gets validation automatically)
        """
        self.minor_version = value  # Delegates to property setter
        return self

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.
        
        Returns:
            The priority value
        
        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "ProvidedServiceInstance":
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

    def getRemoteMulticast(self) -> List["ApplicationEndpoint"]:
        """
        AUTOSAR-compliant getter for remoteMulticast.
        
        Returns:
            The remoteMulticast value
        
        Note:
            Delegates to remote_multicast property (CODING_RULE_V2_00017)
        """
        return self.remote_multicast  # Delegates to property

    def getRemoteUnicast(self) -> List["ApplicationEndpoint"]:
        """
        AUTOSAR-compliant getter for remoteUnicast.
        
        Returns:
            The remoteUnicast value
        
        Note:
            Delegates to remote_unicast property (CODING_RULE_V2_00017)
        """
        return self.remote_unicast  # Delegates to property

    def getSdServerConfig(self) -> "SdServerConfig":
        """
        AUTOSAR-compliant getter for sdServerConfig.
        
        Returns:
            The sdServerConfig value
        
        Note:
            Delegates to sd_server_config property (CODING_RULE_V2_00017)
        """
        return self.sd_server_config  # Delegates to property

    def setSdServerConfig(self, value: "SdServerConfig") -> "ProvidedServiceInstance":
        """
        AUTOSAR-compliant setter for sdServerConfig with method chaining.
        
        Args:
            value: The sdServerConfig to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sd_server_config property setter (gets validation automatically)
        """
        self.sd_server_config = value  # Delegates to property setter
        return self

    def getSdServerTimer(self) -> "SomeipSdServer":
        """
        AUTOSAR-compliant getter for sdServerTimer.
        
        Returns:
            The sdServerTimer value
        
        Note:
            Delegates to sd_server_timer property (CODING_RULE_V2_00017)
        """
        return self.sd_server_timer  # Delegates to property

    def setSdServerTimer(self, value: "SomeipSdServer") -> "ProvidedServiceInstance":
        """
        AUTOSAR-compliant setter for sdServerTimer with method chaining.
        
        Args:
            value: The sdServerTimer to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sd_server_timer property setter (gets validation automatically)
        """
        self.sd_server_timer = value  # Delegates to property setter
        return self

    def getServiceIdentifier(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for serviceIdentifier.
        
        Returns:
            The serviceIdentifier value
        
        Note:
            Delegates to service_identifier property (CODING_RULE_V2_00017)
        """
        return self.service_identifier  # Delegates to property

    def setServiceIdentifier(self, value: "PositiveInteger") -> "ProvidedServiceInstance":
        """
        AUTOSAR-compliant setter for serviceIdentifier with method chaining.
        
        Args:
            value: The serviceIdentifier to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to service_identifier property setter (gets validation automatically)
        """
        self.service_identifier = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_auto_available(self, value: Optional["Boolean"]) -> "ProvidedServiceInstance":
        """
        Set autoAvailable and return self for chaining.
        
        Args:
            value: The autoAvailable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_auto_available("value")
        """
        self.auto_available = value  # Use property setter (gets validation)
        return self

    def with_instance(self, value: Optional["PositiveInteger"]) -> "ProvidedServiceInstance":
        """
        Set instance and return self for chaining.
        
        Args:
            value: The instance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_instance("value")
        """
        self.instance = value  # Use property setter (gets validation)
        return self

    def with_load_balancing(self, value: Optional["PositiveInteger"]) -> "ProvidedServiceInstance":
        """
        Set loadBalancing and return self for chaining.
        
        Args:
            value: The loadBalancing to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_load_balancing("value")
        """
        self.load_balancing = value  # Use property setter (gets validation)
        return self

    def with_local_unicast(self, value: "ApplicationEndpoint") -> "ProvidedServiceInstance":
        """
        Set localUnicast and return self for chaining.
        
        Args:
            value: The localUnicast to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_local_unicast("value")
        """
        self.local_unicast = value  # Use property setter (gets validation)
        return self

    def with_minor_version(self, value: Optional["PositiveInteger"]) -> "ProvidedServiceInstance":
        """
        Set minorVersion and return self for chaining.
        
        Args:
            value: The minorVersion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_minor_version("value")
        """
        self.minor_version = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "ProvidedServiceInstance":
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

    def with_sd_server_config(self, value: Optional["SdServerConfig"]) -> "ProvidedServiceInstance":
        """
        Set sdServerConfig and return self for chaining.
        
        Args:
            value: The sdServerConfig to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sd_server_config("value")
        """
        self.sd_server_config = value  # Use property setter (gets validation)
        return self

    def with_sd_server_timer(self, value: Optional["SomeipSdServer"]) -> "ProvidedServiceInstance":
        """
        Set sdServerTimer and return self for chaining.
        
        Args:
            value: The sdServerTimer to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sd_server_timer("value")
        """
        self.sd_server_timer = value  # Use property setter (gets validation)
        return self

    def with_service_identifier(self, value: Optional["PositiveInteger"]) -> "ProvidedServiceInstance":
        """
        Set serviceIdentifier and return self for chaining.
        
        Args:
            value: The serviceIdentifier to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_service_identifier("value")
        """
        self.service_identifier = value  # Use property setter (gets validation)
        return self


class PduCollectionTriggerEnum(AREnum):
    """
    PduCollectionTriggerEnum enumeration

Defines whether a Pdu contributes to the triggering of the data transmission if Pdu collection is enabled. Aggregated by ContainedIPduProps.trigger, IEEE1722TpAcfBusPart.collectionTrigger, SocketConnectionIpdu Identifier.pduCollectionTrigger, SoConIPduIdentifier.pduCollectionTrigger

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances
    """
    # Pdu will trigger the transmission of the data.
    always = "0"

    # Pdu will be buffered and will not trigger the transmission of the data.
    never = "1"



class UdpChecksumCalculationEnum(AREnum):
    """
    UdpChecksumCalculationEnum enumeration

This enumeration defines the UDP checksum calculation. Aggregated by SocketAddress.udpChecksumHandling, SocketConnectionBundle.udpChecksumHandling

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances
    """
    # Udp checksum handling shall be disabled
    udpChecksumDisabled = "1"

    # Udp checksum handling shall be enabled
    udpChecksumEnabled = "0"



class EventGroupControlTypeEnum(AREnum):
    """
    EventGroupControlTypeEnum enumeration

Types of a RoutingGroups for the event communication. Aggregated by PduActivationRoutingGroup.eventGroupControlType, SoAdRoutingGroup.eventGroupControlType

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances
    """
    # Activate the data path for unicast events and triggered unicast events that are sent out after a client TriggerUnicast got subscribed.
    activationAnd = "0"

    # Activate the data path for multicast events of an EventGroup.
    activationMulticast = "1"

    # Activate the data path for unicast events of an EventGroup.
    activationUnicast = "2"

    # Activate the data path for triggered unicast events that are sent out after a client got subscribed.
    triggerUnicast = "3"



class PduCollectionSemanticsEnum(AREnum):
    """
    PduCollectionSemanticsEnum enumeration

Defines the collection semantics for the PDU collection feature. Aggregated by SocketConnectionIpduIdentifier.pduCollectionSemantics, SoConIPduIdentifier.pduCollection Semantics

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances
    """
    # Only the latest PDU instances are transmitted.
    lastIsBest = "0"

    # All instances of PDUs are transmitted.
    queued = "1"



class ServiceVersionAcceptanceKindEnum(AREnum):
    """
    ServiceVersionAcceptanceKindEnum enumeration

Defined the possible acceptance kinds for required service instances. Aggregated by ConsumedServiceInstance.versionDrivenFindBehavior, RequiredSomeipServiceInstance.version DrivenFindBehavior

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances
    """
    # Search for ANY or specific minor version service instance and select either ALL returned service Version instances (in case of ANY) or exactly the specific minor version service instances defined in required
    exactOrAnyMinor = "0"

    # Template
    System = "None"

    # CP R23-11
    AUTOSAR = "None"

    # Search for ANY minor version service instance and select only those service instances which have Version an equal or greater minor version than given in requiredMinorVersion.
    minimumMinor = "1"



class TcpRoleEnum(AREnum):
    """
    TcpRoleEnum enumeration

This enumeration defines whether a TCP node has the tcp server role or the client role. Aggregated by StaticSocketConnection.tcpRole

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances
    """
    # Connects the client to a remote TCP host.
    connect = "0"

    # Socket is put into the server mode (listen for connections).
    listen = "1"
