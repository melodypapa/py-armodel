from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ApplicationEndpoint(Identifiable):
    """
    An application endpoint is the endpoint on an Ecu in terms of application
    addressing (e.g. socket). The application endpoint represents e.g. the
    listen socket in client-server-based communication.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::ApplicationEndpoint

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 457, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Consumed service instances.
        # Tags: atp.
        # Status=obsolete.
        self._consumed: List["ConsumedService"] = []

    @property
    def consumed(self) -> List["ConsumedService"]:
        """Get consumed (Pythonic accessor)."""
        return self._consumed
        # This attribute defines the maximal number of clients the is able to deal with
                # in case of Service Discovery.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._maxNumberOf: Optional["PositiveInteger"] = None

    @property
    def max_number_of(self) -> Optional["PositiveInteger"]:
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNumberOf with validation.

        Args:
            value: The maxNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOf = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxNumberOf must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        # Reference to the network address.
        self._networkEndpoint: Optional["NetworkEndpoint"] = None

    @property
    def network_endpoint(self) -> Optional["NetworkEndpoint"]:
        """Get networkEndpoint (Pythonic accessor)."""
        return self._networkEndpoint

    @network_endpoint.setter
    def network_endpoint(self, value: Optional["NetworkEndpoint"]) -> None:
        """
        Set networkEndpoint with validation.

        Args:
            value: The networkEndpoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._networkEndpoint = None
            return

        if not isinstance(value, NetworkEndpoint):
            raise TypeError(
                f"networkEndpoint must be NetworkEndpoint or None, got {type(value).__name__}"
            )
        self._networkEndpoint = value
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
        # Provided service instances.
        # Tags: atp.
        # Status=obsolete.
        self._providedService: List["ProvidedService"] = []

    @property
    def provided_service(self) -> List["ProvidedService"]:
        """Get providedService (Pythonic accessor)."""
        return self._providedService
        # This reference identifies the applicable TlsCryptoService Mapping that adds
        # the ability for TLS-based encryption enclosing ApplicationEndpoint.
        self._tlsCrypto: Optional["TlsCryptoService"] = None

    @property
    def tls_crypto(self) -> Optional["TlsCryptoService"]:
        """Get tlsCrypto (Pythonic accessor)."""
        return self._tlsCrypto

    @tls_crypto.setter
    def tls_crypto(self, value: Optional["TlsCryptoService"]) -> None:
        """
        Set tlsCrypto with validation.

        Args:
            value: The tlsCrypto to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tlsCrypto = None
            return

        if not isinstance(value, TlsCryptoService):
            raise TypeError(
                f"tlsCrypto must be TlsCryptoService or None, got {type(value).__name__}"
            )
        self._tlsCrypto = value
        # Configuration of the used transport protocol.
        self._tpConfigurationConfiguration: Optional["TransportProtocol"] = None

    @property
    def tp_configuration_configuration(self) -> Optional["TransportProtocol"]:
        """Get tpConfigurationConfiguration (Pythonic accessor)."""
        return self._tpConfigurationConfiguration

    @tp_configuration_configuration.setter
    def tp_configuration_configuration(self, value: Optional["TransportProtocol"]) -> None:
        """
        Set tpConfigurationConfiguration with validation.

        Args:
            value: The tpConfigurationConfiguration to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpConfigurationConfiguration = None
            return

        if not isinstance(value, TransportProtocol):
            raise TypeError(
                f"tpConfigurationConfiguration must be TransportProtocol or None, got {type(value).__name__}"
            )
        self._tpConfigurationConfiguration = value

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

    def getMaxNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "PositiveInteger") -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
        return self

    def getNetworkEndpoint(self) -> "NetworkEndpoint":
        """
        AUTOSAR-compliant getter for networkEndpoint.

        Returns:
            The networkEndpoint value

        Note:
            Delegates to network_endpoint property (CODING_RULE_V2_00017)
        """
        return self.network_endpoint  # Delegates to property

    def setNetworkEndpoint(self, value: "NetworkEndpoint") -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant setter for networkEndpoint with method chaining.

        Args:
            value: The networkEndpoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to network_endpoint property setter (gets validation automatically)
        """
        self.network_endpoint = value  # Delegates to property setter
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

    def setPriority(self, value: "PositiveInteger") -> "ApplicationEndpoint":
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

    def getProvidedService(self) -> List["ProvidedService"]:
        """
        AUTOSAR-compliant getter for providedService.

        Returns:
            The providedService value

        Note:
            Delegates to provided_service property (CODING_RULE_V2_00017)
        """
        return self.provided_service  # Delegates to property

    def getTlsCrypto(self) -> "TlsCryptoService":
        """
        AUTOSAR-compliant getter for tlsCrypto.

        Returns:
            The tlsCrypto value

        Note:
            Delegates to tls_crypto property (CODING_RULE_V2_00017)
        """
        return self.tls_crypto  # Delegates to property

    def setTlsCrypto(self, value: "TlsCryptoService") -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant setter for tlsCrypto with method chaining.

        Args:
            value: The tlsCrypto to set

        Returns:
            self for method chaining

        Note:
            Delegates to tls_crypto property setter (gets validation automatically)
        """
        self.tls_crypto = value  # Delegates to property setter
        return self

    def getTpConfigurationConfiguration(self) -> "TransportProtocol":
        """
        AUTOSAR-compliant getter for tpConfigurationConfiguration.

        Returns:
            The tpConfigurationConfiguration value

        Note:
            Delegates to tp_configuration_configuration property (CODING_RULE_V2_00017)
        """
        return self.tp_configuration_configuration  # Delegates to property

    def setTpConfigurationConfiguration(self, value: "TransportProtocol") -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant setter for tpConfigurationConfiguration with method chaining.

        Args:
            value: The tpConfigurationConfiguration to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_configuration_configuration property setter (gets validation automatically)
        """
        self.tp_configuration_configuration = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_number_of(self, value: Optional["PositiveInteger"]) -> "ApplicationEndpoint":
        """
        Set maxNumberOf and return self for chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self

    def with_network_endpoint(self, value: Optional["NetworkEndpoint"]) -> "ApplicationEndpoint":
        """
        Set networkEndpoint and return self for chaining.

        Args:
            value: The networkEndpoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network_endpoint("value")
        """
        self.network_endpoint = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "ApplicationEndpoint":
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

    def with_tls_crypto(self, value: Optional["TlsCryptoService"]) -> "ApplicationEndpoint":
        """
        Set tlsCrypto and return self for chaining.

        Args:
            value: The tlsCrypto to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tls_crypto("value")
        """
        self.tls_crypto = value  # Use property setter (gets validation)
        return self

    def with_tp_configuration_configuration(self, value: Optional["TransportProtocol"]) -> "ApplicationEndpoint":
        """
        Set tpConfigurationConfiguration and return self for chaining.

        Args:
            value: The tpConfigurationConfiguration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_configuration_configuration("value")
        """
        self.tp_configuration_configuration = value  # Use property setter (gets validation)
        return self
