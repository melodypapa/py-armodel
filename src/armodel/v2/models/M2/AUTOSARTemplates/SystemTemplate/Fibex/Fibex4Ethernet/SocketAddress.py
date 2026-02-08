from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ApplicationEndpoint,
    EthernetCommunication,
    StaticSocketConnection,
    TimeValue,
    UdpChecksum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
)


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
        self._allowedIPv6Ext: RefType = None

    @property
    def allowed_i_pv6_ext(self) -> RefType:
        """Get allowedIPv6Ext (Pythonic accessor)."""
        return self._allowedIPv6Ext

    @allowed_i_pv6_ext.setter
    def allowed_i_pv6_ext(self, value: RefType) -> None:
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
        self._allowedTcp: RefType = None

    @property
    def allowed_tcp(self) -> RefType:
        """Get allowedTcp (Pythonic accessor)."""
        return self._allowedTcp

    @allowed_tcp.setter
    def allowed_tcp(self, value: RefType) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"differentiated must be PositiveInteger or None, got {type(value).__name__}"
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"flowLabel must be PositiveInteger or None, got {type(value).__name__}"
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"pathMtu must be Boolean or None, got {type(value).__name__}"
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

    def getAllowedIPv6Ext(self) -> RefType:
        """
        AUTOSAR-compliant getter for allowedIPv6Ext.

        Returns:
            The allowedIPv6Ext value

        Note:
            Delegates to allowed_i_pv6_ext property (CODING_RULE_V2_00017)
        """
        return self.allowed_i_pv6_ext  # Delegates to property

    def setAllowedIPv6Ext(self, value: RefType) -> "SocketAddress":
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

    def getAllowedTcp(self) -> RefType:
        """
        AUTOSAR-compliant getter for allowedTcp.

        Returns:
            The allowedTcp value

        Note:
            Delegates to allowed_tcp property (CODING_RULE_V2_00017)
        """
        return self.allowed_tcp  # Delegates to property

    def setAllowedTcp(self, value: RefType) -> "SocketAddress":
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
