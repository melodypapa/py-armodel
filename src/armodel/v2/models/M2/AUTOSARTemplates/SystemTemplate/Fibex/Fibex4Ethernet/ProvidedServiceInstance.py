from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import AbstractServiceInstance


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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"autoAvailable must be Boolean or None, got {type(value).__name__}"
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"instance must be PositiveInteger or None, got {type(value).__name__}"
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"loadBalancing must be PositiveInteger or None, got {type(value).__name__}"
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minorVersion must be PositiveInteger or None, got {type(value).__name__}"
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priority must be PositiveInteger or None, got {type(value).__name__}"
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"serviceIdentifier must be PositiveInteger or None, got {type(value).__name__}"
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
