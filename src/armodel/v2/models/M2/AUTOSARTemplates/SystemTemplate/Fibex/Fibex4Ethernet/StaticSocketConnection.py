from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class StaticSocketConnection(Identifiable):
    """
    Definition of static SocketConnection between the Socket that is defined by
    the aggregating Socket Address and the remoteAddress.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 543, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Assignment of IPduIdentifiers that are transmitted over SocketConnection.
        # atpVariation 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._iPduIdentifier: List["SoConIPduIdentifier"] = []

    @property
    def i_pdu_identifier(self) -> List["SoConIPduIdentifier"]:
        """Get iPduIdentifier (Pythonic accessor)."""
        return self._iPduIdentifier
        # RemoteAddress of the static SocketConnection.
        # atpVariation.
        self._remoteAddress: Optional["SocketAddress"] = None

    @property
    def remote_address(self) -> Optional["SocketAddress"]:
        """Get remoteAddress (Pythonic accessor)."""
        return self._remoteAddress

    @remote_address.setter
    def remote_address(self, value: Optional["SocketAddress"]) -> None:
        """
        Set remoteAddress with validation.

        Args:
            value: The remoteAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._remoteAddress = None
            return

        if not isinstance(value, SocketAddress):
            raise TypeError(
                f"remoteAddress must be SocketAddress or None, got {type(value).__name__}"
            )
        self._remoteAddress = value
        # Specifies the time in seconds how long TCP connect are repeated to reach
                # SOAD_SOCON_ONLINE.
        # is restricted to socket connection groups initiating a TCP connection and are
                # under SoAd.
        self._tcpConnect: Optional["TimeValue"] = None

    @property
    def tcp_connect(self) -> Optional["TimeValue"]:
        """Get tcpConnect (Pythonic accessor)."""
        return self._tcpConnect

    @tcp_connect.setter
    def tcp_connect(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpConnect with validation.

        Args:
            value: The tcpConnect to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpConnect = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpConnect must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpConnect = value
        # Defines whether the local Address (that is aggregating does a listen or a
        # connect.
        self._tcpRole: Optional["TcpRoleEnum"] = None

    @property
    def tcp_role(self) -> Optional["TcpRoleEnum"]:
        """Get tcpRole (Pythonic accessor)."""
        return self._tcpRole

    @tcp_role.setter
    def tcp_role(self, value: Optional["TcpRoleEnum"]) -> None:
        """
        Set tcpRole with validation.

        Args:
            value: The tcpRole to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpRole = None
            return

        if not isinstance(value, TcpRoleEnum):
            raise TypeError(
                f"tcpRole must be TcpRoleEnum or None, got {type(value).__name__}"
            )
        self._tcpRole = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPduIdentifier(self) -> List["SoConIPduIdentifier"]:
        """
        AUTOSAR-compliant getter for iPduIdentifier.

        Returns:
            The iPduIdentifier value

        Note:
            Delegates to i_pdu_identifier property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_identifier  # Delegates to property

    def getRemoteAddress(self) -> "SocketAddress":
        """
        AUTOSAR-compliant getter for remoteAddress.

        Returns:
            The remoteAddress value

        Note:
            Delegates to remote_address property (CODING_RULE_V2_00017)
        """
        return self.remote_address  # Delegates to property

    def setRemoteAddress(self, value: "SocketAddress") -> "StaticSocketConnection":
        """
        AUTOSAR-compliant setter for remoteAddress with method chaining.

        Args:
            value: The remoteAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to remote_address property setter (gets validation automatically)
        """
        self.remote_address = value  # Delegates to property setter
        return self

    def getTcpConnect(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpConnect.

        Returns:
            The tcpConnect value

        Note:
            Delegates to tcp_connect property (CODING_RULE_V2_00017)
        """
        return self.tcp_connect  # Delegates to property

    def setTcpConnect(self, value: "TimeValue") -> "StaticSocketConnection":
        """
        AUTOSAR-compliant setter for tcpConnect with method chaining.

        Args:
            value: The tcpConnect to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_connect property setter (gets validation automatically)
        """
        self.tcp_connect = value  # Delegates to property setter
        return self

    def getTcpRole(self) -> "TcpRoleEnum":
        """
        AUTOSAR-compliant getter for tcpRole.

        Returns:
            The tcpRole value

        Note:
            Delegates to tcp_role property (CODING_RULE_V2_00017)
        """
        return self.tcp_role  # Delegates to property

    def setTcpRole(self, value: "TcpRoleEnum") -> "StaticSocketConnection":
        """
        AUTOSAR-compliant setter for tcpRole with method chaining.

        Args:
            value: The tcpRole to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_role property setter (gets validation automatically)
        """
        self.tcp_role = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_remote_address(self, value: Optional["SocketAddress"]) -> "StaticSocketConnection":
        """
        Set remoteAddress and return self for chaining.

        Args:
            value: The remoteAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_remote_address("value")
        """
        self.remote_address = value  # Use property setter (gets validation)
        return self

    def with_tcp_connect(self, value: Optional["TimeValue"]) -> "StaticSocketConnection":
        """
        Set tcpConnect and return self for chaining.

        Args:
            value: The tcpConnect to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_connect("value")
        """
        self.tcp_connect = value  # Use property setter (gets validation)
        return self

    def with_tcp_role(self, value: Optional["TcpRoleEnum"]) -> "StaticSocketConnection":
        """
        Set tcpRole and return self for chaining.

        Args:
            value: The tcpRole to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_role("value")
        """
        self.tcp_role = value  # Use property setter (gets validation)
        return self
