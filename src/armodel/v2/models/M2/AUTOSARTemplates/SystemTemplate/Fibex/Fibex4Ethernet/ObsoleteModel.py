"""
AUTOSAR Package - ObsoleteModel

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ObsoleteModel
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.__init__ import (
    FibexElement,
    SocketAddress,
)


class SoAdRoutingGroup(FibexElement):
    """
    Routing of Pdus in the SoAd can be activated or deactivated. The ShortName
    of this element shall contain the RoutingGroupId.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ObsoleteModel::SoAdRoutingGroup

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2057, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the type of a RoutingGroup.
        # There are RoutingGroups that activate the data path for unicast events of an
                # event group.
        # And there are activate the data path for initial are triggered, namely events
                # that are sent out server side after a client got subscribed.
        # that this attribute is only valid for event Receiver communication) and
                # omitted in MethodActivationRoutingGroups.
        self._eventGroup: Optional[RefType] = None

    @property
    def event_group(self) -> Optional[RefType]:
        """Get eventGroup (Pythonic accessor)."""
        return self._eventGroup

    @event_group.setter
    def event_group(self, value: Optional[RefType]) -> None:
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

    def with_pdu(self, value):
        """
        Set pdu and return self for chaining.

        Args:
            value: The pdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdu("value")
        """
        self.pdu = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for eventGroup.

        Returns:
            The eventGroup value

        Note:
            Delegates to event_group property (CODING_RULE_V2_00017)
        """
        return self.event_group  # Delegates to property

    def setEventGroup(self, value: RefType) -> SoAdRoutingGroup:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_group(self, value: Optional[RefType]) -> SoAdRoutingGroup:
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



class SocketConnection(Describable):
    """
    The SoAd serves as a (De)Multiplexer between different PDU sources and the
    TCP/IP stack.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ObsoleteModel::SocketConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2057, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If set to true the Server "learns" the client IP address on request.
        # This means that the statically IP Address of the related client shall be If
                # set to false the Server only accepts statically address, e.
        # g.
        # 192.
        # 168.
        # 1.
        # 2.
        # This means that configured IP Address of the Client shall be.
        self._clientIpAddr: Optional[Boolean] = None

    @property
    def client_ip_addr(self) -> Optional[Boolean]:
        """Get clientIpAddr (Pythonic accessor)."""
        return self._clientIpAddr

    @client_ip_addr.setter
    def client_ip_addr(self, value: Optional[Boolean]) -> None:
        """
        Set clientIpAddr with validation.

        Args:
            value: The clientIpAddr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clientIpAddr = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"clientIpAddr must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._clientIpAddr = value
                # requester communication.
        # Please note that the client may data.
        self._clientPort: Optional["SocketAddress"] = None

    @property
    def client_port(self) -> Optional["SocketAddress"]:
        """Get clientPort (Pythonic accessor)."""
        return self._clientPort

    @client_port.setter
    def client_port(self, value: Optional["SocketAddress"]) -> None:
        """
        Set clientPort with validation.

        Args:
            value: The clientPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clientPort = None
            return

        if not isinstance(value, SocketAddress):
            raise TypeError(
                f"clientPort must be SocketAddress or None, got {type(value).__name__}"
            )
        self._clientPort = value
        # This means that the statically Port of the related client shall be ignored.
        # If set the Server only accepts statically configured Port.
        # that the statically configured Port of the Client used.
        self._clientPortFrom: Optional[Boolean] = None

    @property
    def client_port_from(self) -> Optional[Boolean]:
        """Get clientPortFrom (Pythonic accessor)."""
        return self._clientPortFrom

    @client_port_from.setter
    def client_port_from(self, value: Optional[Boolean]) -> None:
        """
        Set clientPortFrom with validation.

        Args:
            value: The clientPortFrom to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clientPortFrom = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"clientPortFrom must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._clientPortFrom = value
                # over by SoAd Ethernet).
        # Multiple IPdus can be one socket connection.
        self._pdu: List["SocketConnectionIpdu"] = []

    @property
    def pdu(self) -> List["SocketConnectionIpdu"]:
        """Get pdu (Pythonic accessor)."""
        return self._pdu
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
                # IP Address information.
        # If this attribute not set to none the value determines the service used
                # client to obtain the IP Address information for the this attribute is set to
                # none the client statically configured IP Address information.
        self._runtimeIp: Optional["RuntimeAddress"] = None

    @property
    def runtime_ip(self) -> Optional["RuntimeAddress"]:
        """Get runtimeIp (Pythonic accessor)."""
        return self._runtimeIp

    @runtime_ip.setter
    def runtime_ip(self, value: Optional["RuntimeAddress"]) -> None:
        """
        Set runtimeIp with validation.

        Args:
            value: The runtimeIp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._runtimeIp = None
            return

        if not isinstance(value, RuntimeAddress):
            raise TypeError(
                f"runtimeIp must be RuntimeAddress or None, got {type(value).__name__}"
            )
        self._runtimeIp = value
                # Port information.
        # If this attribute is not none the value determines the service used by the
                # obtain the Port information for the Socket this attribute is set to none the
                # client uses configured Port information.
        self._runtimePort: Optional["RuntimeAddress"] = None

    @property
    def runtime_port(self) -> Optional["RuntimeAddress"]:
        """Get runtimePort (Pythonic accessor)."""
        return self._runtimePort

    @runtime_port.setter
    def runtime_port(self, value: Optional["RuntimeAddress"]) -> None:
        """
        Set runtimePort with validation.

        Args:
            value: The runtimePort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._runtimePort = None
            return

        if not isinstance(value, RuntimeAddress):
            raise TypeError(
                f"runtimePort must be RuntimeAddress or None, got {type(value).__name__}"
            )
        self._runtimePort = value
        # within its context.
        self._shortLabel: Optional["Identifier"] = None

    @property
    def short_label(self) -> Optional["Identifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["Identifier"]) -> None:
        """
        Set shortLabel with validation.

        Args:
            value: The shortLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"shortLabel must be Identifier or str or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClientIpAddr(self) -> Boolean:
        """
        AUTOSAR-compliant getter for clientIpAddr.

        Returns:
            The clientIpAddr value

        Note:
            Delegates to client_ip_addr property (CODING_RULE_V2_00017)
        """
        return self.client_ip_addr  # Delegates to property

    def setClientIpAddr(self, value: Boolean) -> SocketConnection:
        """
        AUTOSAR-compliant setter for clientIpAddr with method chaining.

        Args:
            value: The clientIpAddr to set

        Returns:
            self for method chaining

        Note:
            Delegates to client_ip_addr property setter (gets validation automatically)
        """
        self.client_ip_addr = value  # Delegates to property setter
        return self

    def getClientPort(self) -> SocketAddress:
        """
        AUTOSAR-compliant getter for clientPort.

        Returns:
            The clientPort value

        Note:
            Delegates to client_port property (CODING_RULE_V2_00017)
        """
        return self.client_port  # Delegates to property

    def setClientPort(self, value: SocketAddress) -> SocketConnection:
        """
        AUTOSAR-compliant setter for clientPort with method chaining.

        Args:
            value: The clientPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to client_port property setter (gets validation automatically)
        """
        self.client_port = value  # Delegates to property setter
        return self

    def getClientPortFrom(self) -> Boolean:
        """
        AUTOSAR-compliant getter for clientPortFrom.

        Returns:
            The clientPortFrom value

        Note:
            Delegates to client_port_from property (CODING_RULE_V2_00017)
        """
        return self.client_port_from  # Delegates to property

    def setClientPortFrom(self, value: Boolean) -> SocketConnection:
        """
        AUTOSAR-compliant setter for clientPortFrom with method chaining.

        Args:
            value: The clientPortFrom to set

        Returns:
            self for method chaining

        Note:
            Delegates to client_port_from property setter (gets validation automatically)
        """
        self.client_port_from = value  # Delegates to property setter
        return self

    def getPdu(self) -> List["SocketConnectionIpdu"]:
        """
        AUTOSAR-compliant getter for pdu.

        Returns:
            The pdu value

        Note:
            Delegates to pdu property (CODING_RULE_V2_00017)
        """
        return self.pdu  # Delegates to property

    def getPduCollection(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for pduCollection.

        Returns:
            The pduCollection value

        Note:
            Delegates to pdu_collection property (CODING_RULE_V2_00017)
        """
        return self.pdu_collection  # Delegates to property

    def setPduCollection(self, value: "TimeValue") -> SocketConnection:
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

    def getRuntimeIp(self) -> "RuntimeAddress":
        """
        AUTOSAR-compliant getter for runtimeIp.

        Returns:
            The runtimeIp value

        Note:
            Delegates to runtime_ip property (CODING_RULE_V2_00017)
        """
        return self.runtime_ip  # Delegates to property

    def setRuntimeIp(self, value: "RuntimeAddress") -> SocketConnection:
        """
        AUTOSAR-compliant setter for runtimeIp with method chaining.

        Args:
            value: The runtimeIp to set

        Returns:
            self for method chaining

        Note:
            Delegates to runtime_ip property setter (gets validation automatically)
        """
        self.runtime_ip = value  # Delegates to property setter
        return self

    def getRuntimePort(self) -> "RuntimeAddress":
        """
        AUTOSAR-compliant getter for runtimePort.

        Returns:
            The runtimePort value

        Note:
            Delegates to runtime_port property (CODING_RULE_V2_00017)
        """
        return self.runtime_port  # Delegates to property

    def setRuntimePort(self, value: "RuntimeAddress") -> SocketConnection:
        """
        AUTOSAR-compliant setter for runtimePort with method chaining.

        Args:
            value: The runtimePort to set

        Returns:
            self for method chaining

        Note:
            Delegates to runtime_port property setter (gets validation automatically)
        """
        self.runtime_port = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> Identifier:
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: Identifier) -> SocketConnection:
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_client_ip_addr(self, value: Optional[Boolean]) -> SocketConnection:
        """
        Set clientIpAddr and return self for chaining.

        Args:
            value: The clientIpAddr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_ip_addr("value")
        """
        self.client_ip_addr = value  # Use property setter (gets validation)
        return self

    def with_client_port(self, value: Optional["SocketAddress"]) -> SocketConnection:
        """
        Set clientPort and return self for chaining.

        Args:
            value: The clientPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_port("value")
        """
        self.client_port = value  # Use property setter (gets validation)
        return self

    def with_client_port_from(self, value: Optional[Boolean]) -> SocketConnection:
        """
        Set clientPortFrom and return self for chaining.

        Args:
            value: The clientPortFrom to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_port_from("value")
        """
        self.client_port_from = value  # Use property setter (gets validation)
        return self

    def with_pdu_collection(self, value: Optional["TimeValue"]) -> SocketConnection:
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

    def with_runtime_ip(self, value: Optional["RuntimeAddress"]) -> SocketConnection:
        """
        Set runtimeIp and return self for chaining.

        Args:
            value: The runtimeIp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_runtime_ip("value")
        """
        self.runtime_ip = value  # Use property setter (gets validation)
        return self

    def with_runtime_port(self, value: Optional["RuntimeAddress"]) -> SocketConnection:
        """
        Set runtimePort and return self for chaining.

        Args:
            value: The runtimePort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_runtime_port("value")
        """
        self.runtime_port = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> SocketConnection:
        """
        Set shortLabel and return self for chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self
