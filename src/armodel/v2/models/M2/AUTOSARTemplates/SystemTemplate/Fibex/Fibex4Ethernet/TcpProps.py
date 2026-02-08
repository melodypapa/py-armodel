from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class TcpProps(ARObject):
    """
    This meta-class specifies the configuration options for TCP (Transmission
    Control Protocol).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 154, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Enables (TRUE) or disables (FALSE) support of TCP avoidance algorithm
        # according to IETF RFC.
        self._tcpCongestion: Optional["Boolean"] = None

    @property
    def tcp_congestion(self) -> Optional["Boolean"]:
        """Get tcpCongestion (Pythonic accessor)."""
        return self._tcpCongestion

    @tcp_congestion.setter
    def tcp_congestion(self, value: Optional["Boolean"]) -> None:
        """
        Set tcpCongestion with validation.

        Args:
            value: The tcpCongestion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpCongestion = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"tcpCongestion must be Boolean or None, got {type(value).__name__}"
            )
        self._tcpCongestion = value
        # The maximal time an acknowledgement is delayed for in seconds.
        self._tcpDelayedAck: Optional["TimeValue"] = None

    @property
    def tcp_delayed_ack(self) -> Optional["TimeValue"]:
        """Get tcpDelayedAck (Pythonic accessor)."""
        return self._tcpDelayedAck

    @tcp_delayed_ack.setter
    def tcp_delayed_ack(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpDelayedAck with validation.

        Args:
            value: The tcpDelayedAck to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpDelayedAck = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpDelayedAck must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpDelayedAck = value
        # Enables (TRUE) or disables (FALSE) support of TCP Fast according to IETF RFC
        # 5681.
        self._tcpFast: Optional["Boolean"] = None

    @property
    def tcp_fast(self) -> Optional["Boolean"]:
        """Get tcpFast (Pythonic accessor)."""
        return self._tcpFast

    @tcp_fast.setter
    def tcp_fast(self, value: Optional["Boolean"]) -> None:
        """
        Set tcpFast with validation.

        Args:
            value: The tcpFast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpFast = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"tcpFast must be Boolean or None, got {type(value).__name__}"
            )
        self._tcpFast = value
        # Timeout in [s] to receive a FIN from the remote node this node has initiated
                # connection termination), i.
        # e.
        # waiting in FINWAIT-2 for a connection from the remote TCP.
        self._tcpFin: Optional["TimeValue"] = None

    @property
    def tcp_fin(self) -> Optional["TimeValue"]:
        """Get tcpFin (Pythonic accessor)."""
        return self._tcpFin

    @tcp_fin.setter
    def tcp_fin(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpFin with validation.

        Args:
            value: The tcpFin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpFin = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpFin must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpFin = value
        # Specifies the time in [s] between the last data packet sent ACKs are not
        # considered data) and the first.
        self._tcpKeepAlive: Optional["TimeValue"] = None

    @property
    def tcp_keep_alive(self) -> Optional["TimeValue"]:
        """Get tcpKeepAlive (Pythonic accessor)."""
        return self._tcpKeepAlive

    @tcp_keep_alive.setter
    def tcp_keep_alive(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpKeepAlive with validation.

        Args:
            value: The tcpKeepAlive to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpKeepAlive = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpKeepAlive must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpKeepAlive = value
        # Maximum number of times that a TCP segment is the TCP connection is closed.
        # This only valid if tcpRetransmissionTimeout is This parameter also applies
                # for FIN.
        self._tcpMaxRtx: Optional["PositiveInteger"] = None

    @property
    def tcp_max_rtx(self) -> Optional["PositiveInteger"]:
        """Get tcpMaxRtx (Pythonic accessor)."""
        return self._tcpMaxRtx

    @tcp_max_rtx.setter
    def tcp_max_rtx(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpMaxRtx with validation.

        Args:
            value: The tcpMaxRtx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpMaxRtx = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpMaxRtx must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpMaxRtx = value
        # Maximum segment lifetime in [s].
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._tcpMsl: Optional["TimeValue"] = None

    @property
    def tcp_msl(self) -> Optional["TimeValue"]:
        """Get tcpMsl (Pythonic accessor)."""
        return self._tcpMsl

    @tcp_msl.setter
    def tcp_msl(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpMsl with validation.

        Args:
            value: The tcpMsl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpMsl = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpMsl must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpMsl = value
        # Enables (TRUE) or disables (FALSE) support of Nagle’s according to IETF RFC
                # 1122 (chapter 4.
        # 2.
        # 3.
        # 4 Send Data).
        # If enabled the Nagle’s algorithm is default for all TCP sockets, but can be
                # Socket (with the attribute TcpTp.
        # nagle.
        self._tcpNagle: Optional["Boolean"] = None

    @property
    def tcp_nagle(self) -> Optional["Boolean"]:
        """Get tcpNagle (Pythonic accessor)."""
        return self._tcpNagle

    @tcp_nagle.setter
    def tcp_nagle(self, value: Optional["Boolean"]) -> None:
        """
        Set tcpNagle with validation.

        Args:
            value: The tcpNagle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpNagle = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"tcpNagle must be Boolean or None, got {type(value).__name__}"
            )
        self._tcpNagle = value
        # Default value of maximum receive window in bytes.
        self._tcpReceiveWindowMax: Optional["PositiveInteger"] = None

    @property
    def tcp_receive_window_max(self) -> Optional["PositiveInteger"]:
        """Get tcpReceiveWindowMax (Pythonic accessor)."""
        return self._tcpReceiveWindowMax

    @tcp_receive_window_max.setter
    def tcp_receive_window_max(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpReceiveWindowMax with validation.

        Args:
            value: The tcpReceiveWindowMax to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpReceiveWindowMax = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpReceiveWindowMax must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpReceiveWindowMax = value
        # Timeout in [s] before an unacknowledged TCP segment sent again.
        # If the timeout is disabled, no TCP segments be retransmitted.
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
        # Enables (TRUE) or disables (FALSE) support of TCP start algorithm according
        # to IETF RFC 5681.
        self._tcpSlowStart: Optional["Boolean"] = None

    @property
    def tcp_slow_start(self) -> Optional["Boolean"]:
        """Get tcpSlowStart (Pythonic accessor)."""
        return self._tcpSlowStart

    @tcp_slow_start.setter
    def tcp_slow_start(self, value: Optional["Boolean"]) -> None:
        """
        Set tcpSlowStart with validation.

        Args:
            value: The tcpSlowStart to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpSlowStart = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"tcpSlowStart must be Boolean or None, got {type(value).__name__}"
            )
        self._tcpSlowStart = value
        # Maximum number of times that a TCP SYN is.
        self._tcpSynMaxRtx: Optional["PositiveInteger"] = None

    @property
    def tcp_syn_max_rtx(self) -> Optional["PositiveInteger"]:
        """Get tcpSynMaxRtx (Pythonic accessor)."""
        return self._tcpSynMaxRtx

    @tcp_syn_max_rtx.setter
    def tcp_syn_max_rtx(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpSynMaxRtx with validation.

        Args:
            value: The tcpSynMaxRtx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpSynMaxRtx = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpSynMaxRtx must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpSynMaxRtx = value
        # Timeout in [s] to complete a remotely initiated TCP establishment, i.
        # e.
        # maximum time waiting in a confirming connection request having both received
                # and sent a.
        self._tcpSynReceived: Optional["TimeValue"] = None

    @property
    def tcp_syn_received(self) -> Optional["TimeValue"]:
        """Get tcpSynReceived (Pythonic accessor)."""
        return self._tcpSynReceived

    @tcp_syn_received.setter
    def tcp_syn_received(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpSynReceived with validation.

        Args:
            value: The tcpSynReceived to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpSynReceived = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpSynReceived must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpSynReceived = value
        # Default Time-to-live value of outgoing TCP packets.
        self._tcpTtl: Optional["PositiveInteger"] = None

    @property
    def tcp_ttl(self) -> Optional["PositiveInteger"]:
        """Get tcpTtl (Pythonic accessor)."""
        return self._tcpTtl

    @tcp_ttl.setter
    def tcp_ttl(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpTtl with validation.

        Args:
            value: The tcpTtl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpTtl = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpTtl must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpTtl = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpCongestion(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for tcpCongestion.

        Returns:
            The tcpCongestion value

        Note:
            Delegates to tcp_congestion property (CODING_RULE_V2_00017)
        """
        return self.tcp_congestion  # Delegates to property

    def setTcpCongestion(self, value: "Boolean") -> "TcpProps":
        """
        AUTOSAR-compliant setter for tcpCongestion with method chaining.

        Args:
            value: The tcpCongestion to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_congestion property setter (gets validation automatically)
        """
        self.tcp_congestion = value  # Delegates to property setter
        return self

    def getTcpDelayedAck(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpDelayedAck.

        Returns:
            The tcpDelayedAck value

        Note:
            Delegates to tcp_delayed_ack property (CODING_RULE_V2_00017)
        """
        return self.tcp_delayed_ack  # Delegates to property

    def setTcpDelayedAck(self, value: "TimeValue") -> "TcpProps":
        """
        AUTOSAR-compliant setter for tcpDelayedAck with method chaining.

        Args:
            value: The tcpDelayedAck to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_delayed_ack property setter (gets validation automatically)
        """
        self.tcp_delayed_ack = value  # Delegates to property setter
        return self

    def getTcpFast(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for tcpFast.

        Returns:
            The tcpFast value

        Note:
            Delegates to tcp_fast property (CODING_RULE_V2_00017)
        """
        return self.tcp_fast  # Delegates to property

    def setTcpFast(self, value: "Boolean") -> "TcpProps":
        """
        AUTOSAR-compliant setter for tcpFast with method chaining.

        Args:
            value: The tcpFast to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_fast property setter (gets validation automatically)
        """
        self.tcp_fast = value  # Delegates to property setter
        return self

    def getTcpFin(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpFin.

        Returns:
            The tcpFin value

        Note:
            Delegates to tcp_fin property (CODING_RULE_V2_00017)
        """
        return self.tcp_fin  # Delegates to property

    def setTcpFin(self, value: "TimeValue") -> "TcpProps":
        """
        AUTOSAR-compliant setter for tcpFin with method chaining.

        Args:
            value: The tcpFin to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_fin property setter (gets validation automatically)
        """
        self.tcp_fin = value  # Delegates to property setter
        return self

    def getTcpKeepAlive(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpKeepAlive.

        Returns:
            The tcpKeepAlive value

        Note:
            Delegates to tcp_keep_alive property (CODING_RULE_V2_00017)
        """
        return self.tcp_keep_alive  # Delegates to property

    def setTcpKeepAlive(self, value: "TimeValue") -> "TcpProps":
        """
        AUTOSAR-compliant setter for tcpKeepAlive with method chaining.

        Args:
            value: The tcpKeepAlive to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_keep_alive property setter (gets validation automatically)
        """
        self.tcp_keep_alive = value  # Delegates to property setter
        return self

    def getTcpMaxRtx(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpMaxRtx.

        Returns:
            The tcpMaxRtx value

        Note:
            Delegates to tcp_max_rtx property (CODING_RULE_V2_00017)
        """
        return self.tcp_max_rtx  # Delegates to property

    def setTcpMaxRtx(self, value: "PositiveInteger") -> "TcpProps":
        """
        AUTOSAR-compliant setter for tcpMaxRtx with method chaining.

        Args:
            value: The tcpMaxRtx to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_max_rtx property setter (gets validation automatically)
        """
        self.tcp_max_rtx = value  # Delegates to property setter
        return self

    def getTcpMsl(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpMsl.

        Returns:
            The tcpMsl value

        Note:
            Delegates to tcp_msl property (CODING_RULE_V2_00017)
        """
        return self.tcp_msl  # Delegates to property

    def setTcpMsl(self, value: "TimeValue") -> "TcpProps":
        """
        AUTOSAR-compliant setter for tcpMsl with method chaining.

        Args:
            value: The tcpMsl to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_msl property setter (gets validation automatically)
        """
        self.tcp_msl = value  # Delegates to property setter
        return self

    def getTcpNagle(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for tcpNagle.

        Returns:
            The tcpNagle value

        Note:
            Delegates to tcp_nagle property (CODING_RULE_V2_00017)
        """
        return self.tcp_nagle  # Delegates to property

    def setTcpNagle(self, value: "Boolean") -> "TcpProps":
        """
        AUTOSAR-compliant setter for tcpNagle with method chaining.

        Args:
            value: The tcpNagle to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_nagle property setter (gets validation automatically)
        """
        self.tcp_nagle = value  # Delegates to property setter
        return self

    def getTcpReceiveWindowMax(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpReceiveWindowMax.

        Returns:
            The tcpReceiveWindowMax value

        Note:
            Delegates to tcp_receive_window_max property (CODING_RULE_V2_00017)
        """
        return self.tcp_receive_window_max  # Delegates to property

    def setTcpReceiveWindowMax(self, value: "PositiveInteger") -> "TcpProps":
        """
        AUTOSAR-compliant setter for tcpReceiveWindowMax with method chaining.

        Args:
            value: The tcpReceiveWindowMax to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_receive_window_max property setter (gets validation automatically)
        """
        self.tcp_receive_window_max = value  # Delegates to property setter
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

    def setTcp(self, value: "TimeValue") -> "TcpProps":
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

    def getTcpSlowStart(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for tcpSlowStart.

        Returns:
            The tcpSlowStart value

        Note:
            Delegates to tcp_slow_start property (CODING_RULE_V2_00017)
        """
        return self.tcp_slow_start  # Delegates to property

    def setTcpSlowStart(self, value: "Boolean") -> "TcpProps":
        """
        AUTOSAR-compliant setter for tcpSlowStart with method chaining.

        Args:
            value: The tcpSlowStart to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_slow_start property setter (gets validation automatically)
        """
        self.tcp_slow_start = value  # Delegates to property setter
        return self

    def getTcpSynMaxRtx(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpSynMaxRtx.

        Returns:
            The tcpSynMaxRtx value

        Note:
            Delegates to tcp_syn_max_rtx property (CODING_RULE_V2_00017)
        """
        return self.tcp_syn_max_rtx  # Delegates to property

    def setTcpSynMaxRtx(self, value: "PositiveInteger") -> "TcpProps":
        """
        AUTOSAR-compliant setter for tcpSynMaxRtx with method chaining.

        Args:
            value: The tcpSynMaxRtx to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_syn_max_rtx property setter (gets validation automatically)
        """
        self.tcp_syn_max_rtx = value  # Delegates to property setter
        return self

    def getTcpSynReceived(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpSynReceived.

        Returns:
            The tcpSynReceived value

        Note:
            Delegates to tcp_syn_received property (CODING_RULE_V2_00017)
        """
        return self.tcp_syn_received  # Delegates to property

    def setTcpSynReceived(self, value: "TimeValue") -> "TcpProps":
        """
        AUTOSAR-compliant setter for tcpSynReceived with method chaining.

        Args:
            value: The tcpSynReceived to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_syn_received property setter (gets validation automatically)
        """
        self.tcp_syn_received = value  # Delegates to property setter
        return self

    def getTcpTtl(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpTtl.

        Returns:
            The tcpTtl value

        Note:
            Delegates to tcp_ttl property (CODING_RULE_V2_00017)
        """
        return self.tcp_ttl  # Delegates to property

    def setTcpTtl(self, value: "PositiveInteger") -> "TcpProps":
        """
        AUTOSAR-compliant setter for tcpTtl with method chaining.

        Args:
            value: The tcpTtl to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ttl property setter (gets validation automatically)
        """
        self.tcp_ttl = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_congestion(self, value: Optional["Boolean"]) -> "TcpProps":
        """
        Set tcpCongestion and return self for chaining.

        Args:
            value: The tcpCongestion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_congestion("value")
        """
        self.tcp_congestion = value  # Use property setter (gets validation)
        return self

    def with_tcp_delayed_ack(self, value: Optional["TimeValue"]) -> "TcpProps":
        """
        Set tcpDelayedAck and return self for chaining.

        Args:
            value: The tcpDelayedAck to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_delayed_ack("value")
        """
        self.tcp_delayed_ack = value  # Use property setter (gets validation)
        return self

    def with_tcp_fast(self, value: Optional["Boolean"]) -> "TcpProps":
        """
        Set tcpFast and return self for chaining.

        Args:
            value: The tcpFast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_fast("value")
        """
        self.tcp_fast = value  # Use property setter (gets validation)
        return self

    def with_tcp_fin(self, value: Optional["TimeValue"]) -> "TcpProps":
        """
        Set tcpFin and return self for chaining.

        Args:
            value: The tcpFin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_fin("value")
        """
        self.tcp_fin = value  # Use property setter (gets validation)
        return self

    def with_tcp_keep_alive(self, value: Optional["TimeValue"]) -> "TcpProps":
        """
        Set tcpKeepAlive and return self for chaining.

        Args:
            value: The tcpKeepAlive to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_keep_alive("value")
        """
        self.tcp_keep_alive = value  # Use property setter (gets validation)
        return self

    def with_tcp_max_rtx(self, value: Optional["PositiveInteger"]) -> "TcpProps":
        """
        Set tcpMaxRtx and return self for chaining.

        Args:
            value: The tcpMaxRtx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_max_rtx("value")
        """
        self.tcp_max_rtx = value  # Use property setter (gets validation)
        return self

    def with_tcp_msl(self, value: Optional["TimeValue"]) -> "TcpProps":
        """
        Set tcpMsl and return self for chaining.

        Args:
            value: The tcpMsl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_msl("value")
        """
        self.tcp_msl = value  # Use property setter (gets validation)
        return self

    def with_tcp_nagle(self, value: Optional["Boolean"]) -> "TcpProps":
        """
        Set tcpNagle and return self for chaining.

        Args:
            value: The tcpNagle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_nagle("value")
        """
        self.tcp_nagle = value  # Use property setter (gets validation)
        return self

    def with_tcp_receive_window_max(self, value: Optional["PositiveInteger"]) -> "TcpProps":
        """
        Set tcpReceiveWindowMax and return self for chaining.

        Args:
            value: The tcpReceiveWindowMax to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_receive_window_max("value")
        """
        self.tcp_receive_window_max = value  # Use property setter (gets validation)
        return self

    def with_tcp(self, value: Optional["TimeValue"]) -> "TcpProps":
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

    def with_tcp_slow_start(self, value: Optional["Boolean"]) -> "TcpProps":
        """
        Set tcpSlowStart and return self for chaining.

        Args:
            value: The tcpSlowStart to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_slow_start("value")
        """
        self.tcp_slow_start = value  # Use property setter (gets validation)
        return self

    def with_tcp_syn_max_rtx(self, value: Optional["PositiveInteger"]) -> "TcpProps":
        """
        Set tcpSynMaxRtx and return self for chaining.

        Args:
            value: The tcpSynMaxRtx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_syn_max_rtx("value")
        """
        self.tcp_syn_max_rtx = value  # Use property setter (gets validation)
        return self

    def with_tcp_syn_received(self, value: Optional["TimeValue"]) -> "TcpProps":
        """
        Set tcpSynReceived and return self for chaining.

        Args:
            value: The tcpSynReceived to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_syn_received("value")
        """
        self.tcp_syn_received = value  # Use property setter (gets validation)
        return self

    def with_tcp_ttl(self, value: Optional["PositiveInteger"]) -> "TcpProps":
        """
        Set tcpTtl and return self for chaining.

        Args:
            value: The tcpTtl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ttl("value")
        """
        self.tcp_ttl = value  # Use property setter (gets validation)
        return self
