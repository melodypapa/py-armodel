from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priority must be PositiveInteger or None, got {type(value).__name__}"
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"serviceOffer must be PositiveInteger or None, got {type(value).__name__}"
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