from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"subscribe must be PositiveInteger or None, got {type(value).__name__}"
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"timeToLive must be PositiveInteger or None, got {type(value).__name__}"
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