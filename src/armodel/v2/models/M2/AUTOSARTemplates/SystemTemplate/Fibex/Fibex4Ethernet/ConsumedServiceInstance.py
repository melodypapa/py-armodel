from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import AbstractServiceInstance

    RefType,
)


class ConsumedServiceInstance(AbstractServiceInstance):
    """
    Service instances that are consumed by the ECU that is connected via the
    ApplicationEndpoint to a CommunicationConnector.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances

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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"autoRequire must be Boolean or None, got {type(value).__name__}"
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
        self._consumedEvent: List[RefType] = []

    @property
    def consumed_event(self) -> List[RefType]:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"serviceIdentifier must be PositiveInteger or None, got {type(value).__name__}"
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

    def getConsumedEvent(self) -> List[RefType]:
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
