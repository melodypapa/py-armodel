from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class IPSecRule(Identifiable):
    """
    This element defines an IPsec rule that describes communication traffic that
    is monitored, protected and filtered.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 571, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the direction in which the traffic is If this
        # attribute is not set a bidirectional traffic assumed.
        self._direction: Optional["Communication"] = None

    @property
    def direction(self) -> Optional["Communication"]:
        """Get direction (Pythonic accessor)."""
        return self._direction

    @direction.setter
    def direction(self, value: Optional["Communication"]) -> None:
        """
        Set direction with validation.

        Args:
            value: The direction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._direction = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"direction must be Communication or None, got {type(value).__name__}"
            )
        self._direction = value
        # Header type specifying the IPsec security mechanism.
        self._headerType: Optional["IPsecHeaderTypeEnum"] = None

    @property
    def header_type(self) -> Optional["IPsecHeaderTypeEnum"]:
        """Get headerType (Pythonic accessor)."""
        return self._headerType

    @header_type.setter
    def header_type(self, value: Optional["IPsecHeaderTypeEnum"]) -> None:
        """
        Set headerType with validation.

        Args:
            value: The headerType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._headerType = None
            return

        if not isinstance(value, IPsecHeaderTypeEnum):
            raise TypeError(
                f"headerType must be IPsecHeaderTypeEnum or None, got {type(value).__name__}"
            )
        self._headerType = value
        # This attribute defines the relevant IP protocol used in the Database (SPD)
        # entry.
        self._ipProtocol: Optional["IPsecIpProtocolEnum"] = None

    @property
    def ip_protocol(self) -> Optional["IPsecIpProtocolEnum"]:
        """Get ipProtocol (Pythonic accessor)."""
        return self._ipProtocol

    @ip_protocol.setter
    def ip_protocol(self, value: Optional["IPsecIpProtocolEnum"]) -> None:
        """
        Set ipProtocol with validation.

        Args:
            value: The ipProtocol to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ipProtocol = None
            return

        if not isinstance(value, IPsecIpProtocolEnum):
            raise TypeError(
                f"ipProtocol must be IPsecIpProtocolEnum or None, got {type(value).__name__}"
            )
        self._ipProtocol = value
        # This reference identifies the applicable certificate used for local
        # authentication.
        self._localCertificate: List["CryptoService"] = []

    @property
    def local_certificate(self) -> List["CryptoService"]:
        """Get localCertificate (Pythonic accessor)."""
        return self._localCertificate
        # This attribute defines how the local participant should be authentication.
        self._localId: Optional["String"] = None

    @property
    def local_id(self) -> Optional["String"]:
        """Get localId (Pythonic accessor)."""
        return self._localId

    @local_id.setter
    def local_id(self, value: Optional["String"]) -> None:
        """
        Set localId with validation.

        Args:
            value: The localId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._localId = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"localId must be String or None, got {type(value).__name__}"
            )
        self._localId = value
        # This attribute restricts the traffic monitoring and defines a value for the
                # local port range.
        # attribute is not set then this rule shall be effective local ports.
        # that port ranges are currently not supported AUTOSAR AP’s operating system
                # backend.
        # If AP involved, each IPsec rule may only contain a.
        self._localPortRange: Optional["PositiveInteger"] = None

    @property
    def local_port_range(self) -> Optional["PositiveInteger"]:
        """Get localPortRange (Pythonic accessor)."""
        return self._localPortRange

    @local_port_range.setter
    def local_port_range(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set localPortRange with validation.

        Args:
            value: The localPortRange to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._localPortRange = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"localPortRange must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._localPortRange = value
        # This attribute defines the type of the connection.
        self._mode: Optional["IPsecModeEnum"] = None

    @property
    def mode(self) -> Optional["IPsecModeEnum"]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: Optional["IPsecModeEnum"]) -> None:
        """
        Set mode with validation.

        Args:
            value: The mode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        if not isinstance(value, IPsecModeEnum):
            raise TypeError(
                f"mode must be IPsecModeEnum or None, got {type(value).__name__}"
            )
        self._mode = value
        # An IPsec policy defines the rules that determine which IP traffic needs to be
        # secured using IPsec and traffic is secured.
        self._policy: Optional["IPsecPolicyEnum"] = None

    @property
    def policy(self) -> Optional["IPsecPolicyEnum"]:
        """Get policy (Pythonic accessor)."""
        return self._policy

    @policy.setter
    def policy(self, value: Optional["IPsecPolicyEnum"]) -> None:
        """
        Set policy with validation.

        Args:
            value: The policy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._policy = None
            return

        if not isinstance(value, IPsecPolicyEnum):
            raise TypeError(
                f"policy must be IPsecPolicyEnum or None, got {type(value).__name__}"
            )
        self._policy = value
        # This reference identifies the applicable cryptograhic key authentication.
        self._preSharedKey: Optional["CryptoServiceKey"] = None

    @property
    def pre_shared_key(self) -> Optional["CryptoServiceKey"]:
        """Get preSharedKey (Pythonic accessor)."""
        return self._preSharedKey

    @pre_shared_key.setter
    def pre_shared_key(self, value: Optional["CryptoServiceKey"]) -> None:
        """
        Set preSharedKey with validation.

        Args:
            value: The preSharedKey to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._preSharedKey = None
            return

        if not isinstance(value, CryptoServiceKey):
            raise TypeError(
                f"preSharedKey must be CryptoServiceKey or None, got {type(value).__name__}"
            )
        self._preSharedKey = value
        # This attribute defines the priority of the IPSecRule (SPD processing of
        # entries is based on priority, the highest priority "0".
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
        # This reference identifies the applicable certificate used for a remote
        # authentication.
        self._remote: List["CryptoService"] = []

    @property
    def remote(self) -> List["CryptoService"]:
        """Get remote (Pythonic accessor)."""
        return self._remote
        # This attribute defines how the remote participant should for authentication.
        self._remoteId: Optional["String"] = None

    @property
    def remote_id(self) -> Optional["String"]:
        """Get remoteId (Pythonic accessor)."""
        return self._remoteId

    @remote_id.setter
    def remote_id(self, value: Optional["String"]) -> None:
        """
        Set remoteId with validation.

        Args:
            value: The remoteId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._remoteId = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"remoteId must be String or None, got {type(value).__name__}"
            )
        self._remoteId = value
        # Definition of the remote NetworkEndpoint.
        # With this the connection between the local Network the remote NetworkEndpoint
                # is described the traffic is monitored.
        self._remoteIp: List["NetworkEndpoint"] = []

    @property
    def remote_ip(self) -> List["NetworkEndpoint"]:
        """Get remoteIp (Pythonic accessor)."""
        return self._remoteIp
        # This attribute restricts the traffic monitoring and defines a value for the
                # remote port range.
        # attribute is not set then this rule shall be effective local ports.
        # that port ranges are currently not supported AUTOSAR AP’s operating system
                # backend.
        # If AP involved, each IPsec rule may only contain a.
        self._remotePort: Optional["PositiveInteger"] = None

    @property
    def remote_port(self) -> Optional["PositiveInteger"]:
        """Get remotePort (Pythonic accessor)."""
        return self._remotePort

    @remote_port.setter
    def remote_port(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set remotePort with validation.

        Args:
            value: The remotePort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._remotePort = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"remotePort must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._remotePort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDirection(self) -> "Communication":
        """
        AUTOSAR-compliant getter for direction.

        Returns:
            The direction value

        Note:
            Delegates to direction property (CODING_RULE_V2_00017)
        """
        return self.direction  # Delegates to property

    def setDirection(self, value: "Communication") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for direction with method chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Note:
            Delegates to direction property setter (gets validation automatically)
        """
        self.direction = value  # Delegates to property setter
        return self

    def getHeaderType(self) -> "IPsecHeaderTypeEnum":
        """
        AUTOSAR-compliant getter for headerType.

        Returns:
            The headerType value

        Note:
            Delegates to header_type property (CODING_RULE_V2_00017)
        """
        return self.header_type  # Delegates to property

    def setHeaderType(self, value: "IPsecHeaderTypeEnum") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for headerType with method chaining.

        Args:
            value: The headerType to set

        Returns:
            self for method chaining

        Note:
            Delegates to header_type property setter (gets validation automatically)
        """
        self.header_type = value  # Delegates to property setter
        return self

    def getIpProtocol(self) -> "IPsecIpProtocolEnum":
        """
        AUTOSAR-compliant getter for ipProtocol.

        Returns:
            The ipProtocol value

        Note:
            Delegates to ip_protocol property (CODING_RULE_V2_00017)
        """
        return self.ip_protocol  # Delegates to property

    def setIpProtocol(self, value: "IPsecIpProtocolEnum") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for ipProtocol with method chaining.

        Args:
            value: The ipProtocol to set

        Returns:
            self for method chaining

        Note:
            Delegates to ip_protocol property setter (gets validation automatically)
        """
        self.ip_protocol = value  # Delegates to property setter
        return self

    def getLocalCertificate(self) -> List["CryptoService"]:
        """
        AUTOSAR-compliant getter for localCertificate.

        Returns:
            The localCertificate value

        Note:
            Delegates to local_certificate property (CODING_RULE_V2_00017)
        """
        return self.local_certificate  # Delegates to property

    def getLocalId(self) -> "String":
        """
        AUTOSAR-compliant getter for localId.

        Returns:
            The localId value

        Note:
            Delegates to local_id property (CODING_RULE_V2_00017)
        """
        return self.local_id  # Delegates to property

    def setLocalId(self, value: "String") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for localId with method chaining.

        Args:
            value: The localId to set

        Returns:
            self for method chaining

        Note:
            Delegates to local_id property setter (gets validation automatically)
        """
        self.local_id = value  # Delegates to property setter
        return self

    def getLocalPortRange(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for localPortRange.

        Returns:
            The localPortRange value

        Note:
            Delegates to local_port_range property (CODING_RULE_V2_00017)
        """
        return self.local_port_range  # Delegates to property

    def setLocalPortRange(self, value: "PositiveInteger") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for localPortRange with method chaining.

        Args:
            value: The localPortRange to set

        Returns:
            self for method chaining

        Note:
            Delegates to local_port_range property setter (gets validation automatically)
        """
        self.local_port_range = value  # Delegates to property setter
        return self

    def getMode(self) -> "IPsecModeEnum":
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: "IPsecModeEnum") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for mode with method chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    def getPolicy(self) -> "IPsecPolicyEnum":
        """
        AUTOSAR-compliant getter for policy.

        Returns:
            The policy value

        Note:
            Delegates to policy property (CODING_RULE_V2_00017)
        """
        return self.policy  # Delegates to property

    def setPolicy(self, value: "IPsecPolicyEnum") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for policy with method chaining.

        Args:
            value: The policy to set

        Returns:
            self for method chaining

        Note:
            Delegates to policy property setter (gets validation automatically)
        """
        self.policy = value  # Delegates to property setter
        return self

    def getPreSharedKey(self) -> "CryptoServiceKey":
        """
        AUTOSAR-compliant getter for preSharedKey.

        Returns:
            The preSharedKey value

        Note:
            Delegates to pre_shared_key property (CODING_RULE_V2_00017)
        """
        return self.pre_shared_key  # Delegates to property

    def setPreSharedKey(self, value: "CryptoServiceKey") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for preSharedKey with method chaining.

        Args:
            value: The preSharedKey to set

        Returns:
            self for method chaining

        Note:
            Delegates to pre_shared_key property setter (gets validation automatically)
        """
        self.pre_shared_key = value  # Delegates to property setter
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

    def setPriority(self, value: "PositiveInteger") -> "IPSecRule":
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

    def getRemote(self) -> List["CryptoService"]:
        """
        AUTOSAR-compliant getter for remote.

        Returns:
            The remote value

        Note:
            Delegates to remote property (CODING_RULE_V2_00017)
        """
        return self.remote  # Delegates to property

    def getRemoteId(self) -> "String":
        """
        AUTOSAR-compliant getter for remoteId.

        Returns:
            The remoteId value

        Note:
            Delegates to remote_id property (CODING_RULE_V2_00017)
        """
        return self.remote_id  # Delegates to property

    def setRemoteId(self, value: "String") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for remoteId with method chaining.

        Args:
            value: The remoteId to set

        Returns:
            self for method chaining

        Note:
            Delegates to remote_id property setter (gets validation automatically)
        """
        self.remote_id = value  # Delegates to property setter
        return self

    def getRemoteIp(self) -> List["NetworkEndpoint"]:
        """
        AUTOSAR-compliant getter for remoteIp.

        Returns:
            The remoteIp value

        Note:
            Delegates to remote_ip property (CODING_RULE_V2_00017)
        """
        return self.remote_ip  # Delegates to property

    def getRemotePort(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for remotePort.

        Returns:
            The remotePort value

        Note:
            Delegates to remote_port property (CODING_RULE_V2_00017)
        """
        return self.remote_port  # Delegates to property

    def setRemotePort(self, value: "PositiveInteger") -> "IPSecRule":
        """
        AUTOSAR-compliant setter for remotePort with method chaining.

        Args:
            value: The remotePort to set

        Returns:
            self for method chaining

        Note:
            Delegates to remote_port property setter (gets validation automatically)
        """
        self.remote_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_direction(self, value: Optional["Communication"]) -> "IPSecRule":
        """
        Set direction and return self for chaining.

        Args:
            value: The direction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direction("value")
        """
        self.direction = value  # Use property setter (gets validation)
        return self

    def with_header_type(self, value: Optional["IPsecHeaderTypeEnum"]) -> "IPSecRule":
        """
        Set headerType and return self for chaining.

        Args:
            value: The headerType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_header_type("value")
        """
        self.header_type = value  # Use property setter (gets validation)
        return self

    def with_ip_protocol(self, value: Optional["IPsecIpProtocolEnum"]) -> "IPSecRule":
        """
        Set ipProtocol and return self for chaining.

        Args:
            value: The ipProtocol to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ip_protocol("value")
        """
        self.ip_protocol = value  # Use property setter (gets validation)
        return self

    def with_local_id(self, value: Optional["String"]) -> "IPSecRule":
        """
        Set localId and return self for chaining.

        Args:
            value: The localId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_local_id("value")
        """
        self.local_id = value  # Use property setter (gets validation)
        return self

    def with_local_port_range(self, value: Optional["PositiveInteger"]) -> "IPSecRule":
        """
        Set localPortRange and return self for chaining.

        Args:
            value: The localPortRange to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_local_port_range("value")
        """
        self.local_port_range = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value: Optional["IPsecModeEnum"]) -> "IPSecRule":
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    def with_policy(self, value: Optional["IPsecPolicyEnum"]) -> "IPSecRule":
        """
        Set policy and return self for chaining.

        Args:
            value: The policy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_policy("value")
        """
        self.policy = value  # Use property setter (gets validation)
        return self

    def with_pre_shared_key(self, value: Optional["CryptoServiceKey"]) -> "IPSecRule":
        """
        Set preSharedKey and return self for chaining.

        Args:
            value: The preSharedKey to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pre_shared_key("value")
        """
        self.pre_shared_key = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "IPSecRule":
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

    def with_remote_id(self, value: Optional["String"]) -> "IPSecRule":
        """
        Set remoteId and return self for chaining.

        Args:
            value: The remoteId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_remote_id("value")
        """
        self.remote_id = value  # Use property setter (gets validation)
        return self

    def with_remote_port(self, value: Optional["PositiveInteger"]) -> "IPSecRule":
        """
        Set remotePort and return self for chaining.

        Args:
            value: The remotePort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_remote_port("value")
        """
        self.remote_port = value  # Use property setter (gets validation)
        return self
