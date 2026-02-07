from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


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
        self._consumedEvent: List[RefType] = []

    @property
    def consumed_event(self) -> List[RefType]:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"eventGroup must be PositiveInteger or None, got {type(value).__name__}"
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"multicast must be PositiveInteger or None, got {type(value).__name__}"
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
        self._routingGroup: List[RefType] = []

    @property
    def routing_group(self) -> List[RefType]:
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

    def getConsumedEvent(self) -> List[RefType]:
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

    def getRoutingGroup(self) -> List[RefType]:
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
