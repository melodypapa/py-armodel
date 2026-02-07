from typing import Optional


class TcpTp(TcpUdpConfig):
    """
    Content Model for TCP configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::TcpTp

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 460, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum number of times that TCP retransmits an data segment before aborting
        # the connection.
        self._keepAlive: Optional["PositiveInteger"] = None

    @property
    def keep_alive(self) -> Optional["PositiveInteger"]:
        """Get keepAlive (Pythonic accessor)."""
        return self._keepAlive

    @keep_alive.setter
    def keep_alive(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set keepAlive with validation.

        Args:
            value: The keepAlive to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keepAlive = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"keepAlive must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._keepAlive = value
        # Indicates if Keep-Alive messages are sent.
        self._keepAlives: Optional["Boolean"] = None

    @property
    def keep_alives(self) -> Optional["Boolean"]:
        """Get keepAlives (Pythonic accessor)."""
        return self._keepAlives

    @keep_alives.setter
    def keep_alives(self, value: Optional["Boolean"]) -> None:
        """
        Set keepAlives with validation.

        Args:
            value: The keepAlives to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keepAlives = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"keepAlives must be Boolean or None, got {type(value).__name__}"
            )
        self._keepAlives = value
        # Specifies the time in seconds between the last data and the first keepalive
        # probe.
        self._keepAliveTime: Optional["TimeValue"] = None

    @property
    def keep_alive_time(self) -> Optional["TimeValue"]:
        """Get keepAliveTime (Pythonic accessor)."""
        return self._keepAliveTime

    @keep_alive_time.setter
    def keep_alive_time(self, value: Optional["TimeValue"]) -> None:
        """
        Set keepAliveTime with validation.

        Args:
            value: The keepAliveTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keepAliveTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"keepAliveTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._keepAliveTime = value
        # Indicates if Nagle’s Algorithm is used.
        self._naglesAlgorithm: Optional["Boolean"] = None

    @property
    def nagles_algorithm(self) -> Optional["Boolean"]:
        """Get naglesAlgorithm (Pythonic accessor)."""
        return self._naglesAlgorithm

    @nagles_algorithm.setter
    def nagles_algorithm(self, value: Optional["Boolean"]) -> None:
        """
        Set naglesAlgorithm with validation.

        Args:
            value: The naglesAlgorithm to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._naglesAlgorithm = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"naglesAlgorithm must be Boolean or None, got {type(value).__name__}"
            )
        self._naglesAlgorithm = value
        # Minimum size of the TCP receive window in bytes.
        self._receiveWindowMin: Optional["PositiveInteger"] = None

    @property
    def receive_window_min(self) -> Optional["PositiveInteger"]:
        """Get receiveWindowMin (Pythonic accessor)."""
        return self._receiveWindowMin

    @receive_window_min.setter
    def receive_window_min(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set receiveWindowMin with validation.

        Args:
            value: The receiveWindowMin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._receiveWindowMin = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"receiveWindowMin must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._receiveWindowMin = value
        # Defines the timeout in seconds before an TCP segment is sent again.
        # If the tcp is not defined or set to "INF", no shall be re-transmitted.
        self._tcp: Optional["TimeValue"] = None

    @property
    def tcp(self) -> Optional["TimeValue"]:
        """Get tcp (Pythonic accessor)."""
        return self._tcp

    @tcp.setter
    def tcp(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcp with validation.

        Args:
            value: The tcp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcp = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcp must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcp = value
        # TCP Port configuration.
        self._tcpTpPort: Optional["TpPort"] = None

    @property
    def tcp_tp_port(self) -> Optional["TpPort"]:
        """Get tcpTpPort (Pythonic accessor)."""
        return self._tcpTpPort

    @tcp_tp_port.setter
    def tcp_tp_port(self, value: Optional["TpPort"]) -> None:
        """
        Set tcpTpPort with validation.

        Args:
            value: The tcpTpPort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpTpPort = None
            return

        if not isinstance(value, TpPort):
            raise TypeError(
                f"tcpTpPort must be TpPort or None, got {type(value).__name__}"
            )
        self._tcpTpPort = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getKeepAlive(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for keepAlive.

        Returns:
            The keepAlive value

        Note:
            Delegates to keep_alive property (CODING_RULE_V2_00017)
        """
        return self.keep_alive  # Delegates to property

    def setKeepAlive(self, value: "PositiveInteger") -> "TcpTp":
        """
        AUTOSAR-compliant setter for keepAlive with method chaining.

        Args:
            value: The keepAlive to set

        Returns:
            self for method chaining

        Note:
            Delegates to keep_alive property setter (gets validation automatically)
        """
        self.keep_alive = value  # Delegates to property setter
        return self

    def getKeepAlives(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for keepAlives.

        Returns:
            The keepAlives value

        Note:
            Delegates to keep_alives property (CODING_RULE_V2_00017)
        """
        return self.keep_alives  # Delegates to property

    def setKeepAlives(self, value: "Boolean") -> "TcpTp":
        """
        AUTOSAR-compliant setter for keepAlives with method chaining.

        Args:
            value: The keepAlives to set

        Returns:
            self for method chaining

        Note:
            Delegates to keep_alives property setter (gets validation automatically)
        """
        self.keep_alives = value  # Delegates to property setter
        return self

    def getKeepAliveTime(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for keepAliveTime.

        Returns:
            The keepAliveTime value

        Note:
            Delegates to keep_alive_time property (CODING_RULE_V2_00017)
        """
        return self.keep_alive_time  # Delegates to property

    def setKeepAliveTime(self, value: "TimeValue") -> "TcpTp":
        """
        AUTOSAR-compliant setter for keepAliveTime with method chaining.

        Args:
            value: The keepAliveTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to keep_alive_time property setter (gets validation automatically)
        """
        self.keep_alive_time = value  # Delegates to property setter
        return self

    def getNaglesAlgorithm(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for naglesAlgorithm.

        Returns:
            The naglesAlgorithm value

        Note:
            Delegates to nagles_algorithm property (CODING_RULE_V2_00017)
        """
        return self.nagles_algorithm  # Delegates to property

    def setNaglesAlgorithm(self, value: "Boolean") -> "TcpTp":
        """
        AUTOSAR-compliant setter for naglesAlgorithm with method chaining.

        Args:
            value: The naglesAlgorithm to set

        Returns:
            self for method chaining

        Note:
            Delegates to nagles_algorithm property setter (gets validation automatically)
        """
        self.nagles_algorithm = value  # Delegates to property setter
        return self

    def getReceiveWindowMin(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for receiveWindowMin.

        Returns:
            The receiveWindowMin value

        Note:
            Delegates to receive_window_min property (CODING_RULE_V2_00017)
        """
        return self.receive_window_min  # Delegates to property

    def setReceiveWindowMin(self, value: "PositiveInteger") -> "TcpTp":
        """
        AUTOSAR-compliant setter for receiveWindowMin with method chaining.

        Args:
            value: The receiveWindowMin to set

        Returns:
            self for method chaining

        Note:
            Delegates to receive_window_min property setter (gets validation automatically)
        """
        self.receive_window_min = value  # Delegates to property setter
        return self

    def getTcp(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcp.

        Returns:
            The tcp value

        Note:
            Delegates to tcp property (CODING_RULE_V2_00017)
        """
        return self.tcp  # Delegates to property

    def setTcp(self, value: "TimeValue") -> "TcpTp":
        """
        AUTOSAR-compliant setter for tcp with method chaining.

        Args:
            value: The tcp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp property setter (gets validation automatically)
        """
        self.tcp = value  # Delegates to property setter
        return self

    def getTcpTpPort(self) -> "TpPort":
        """
        AUTOSAR-compliant getter for tcpTpPort.

        Returns:
            The tcpTpPort value

        Note:
            Delegates to tcp_tp_port property (CODING_RULE_V2_00017)
        """
        return self.tcp_tp_port  # Delegates to property

    def setTcpTpPort(self, value: "TpPort") -> "TcpTp":
        """
        AUTOSAR-compliant setter for tcpTpPort with method chaining.

        Args:
            value: The tcpTpPort to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_tp_port property setter (gets validation automatically)
        """
        self.tcp_tp_port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_keep_alive(self, value: Optional["PositiveInteger"]) -> "TcpTp":
        """
        Set keepAlive and return self for chaining.

        Args:
            value: The keepAlive to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_keep_alive("value")
        """
        self.keep_alive = value  # Use property setter (gets validation)
        return self

    def with_keep_alives(self, value: Optional["Boolean"]) -> "TcpTp":
        """
        Set keepAlives and return self for chaining.

        Args:
            value: The keepAlives to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_keep_alives("value")
        """
        self.keep_alives = value  # Use property setter (gets validation)
        return self

    def with_keep_alive_time(self, value: Optional["TimeValue"]) -> "TcpTp":
        """
        Set keepAliveTime and return self for chaining.

        Args:
            value: The keepAliveTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_keep_alive_time("value")
        """
        self.keep_alive_time = value  # Use property setter (gets validation)
        return self

    def with_nagles_algorithm(self, value: Optional["Boolean"]) -> "TcpTp":
        """
        Set naglesAlgorithm and return self for chaining.

        Args:
            value: The naglesAlgorithm to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nagles_algorithm("value")
        """
        self.nagles_algorithm = value  # Use property setter (gets validation)
        return self

    def with_receive_window_min(self, value: Optional["PositiveInteger"]) -> "TcpTp":
        """
        Set receiveWindowMin and return self for chaining.

        Args:
            value: The receiveWindowMin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_receive_window_min("value")
        """
        self.receive_window_min = value  # Use property setter (gets validation)
        return self

    def with_tcp(self, value: Optional["TimeValue"]) -> "TcpTp":
        """
        Set tcp and return self for chaining.

        Args:
            value: The tcp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp("value")
        """
        self.tcp = value  # Use property setter (gets validation)
        return self

    def with_tcp_tp_port(self, value: Optional["TpPort"]) -> "TcpTp":
        """
        Set tcpTpPort and return self for chaining.

        Args:
            value: The tcpTpPort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_tp_port("value")
        """
        self.tcp_tp_port = value  # Use property setter (gets validation)
        return self
