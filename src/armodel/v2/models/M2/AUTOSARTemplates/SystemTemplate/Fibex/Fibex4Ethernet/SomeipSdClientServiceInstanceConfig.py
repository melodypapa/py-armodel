from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement


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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priority must be PositiveInteger or None, got {type(value).__name__}"
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"serviceFind must be PositiveInteger or None, got {type(value).__name__}"
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
