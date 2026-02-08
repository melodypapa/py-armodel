from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class Ipv6FragmentationProps(ARObject):
    """
    This meta-class specifies the configuration options for IPv6 packet
    fragmentation/reassembly.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 148, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the timeout in seconds after which an datagram gets discarded.
        self._tcpIpIp: Optional["TimeValue"] = None

    @property
    def tcp_ip_ip(self) -> Optional["TimeValue"]:
        """Get tcpIpIp (Pythonic accessor)."""
        return self._tcpIpIp

    @tcp_ip_ip.setter
    def tcp_ip_ip(self, value: Optional["TimeValue"]) -> None:
        """
        Set tcpIpIp with validation.

        Args:
            value: The tcpIpIp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIp = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"tcpIpIp must be TimeValue or None, got {type(value).__name__}"
            )
        self._tcpIpIp = value
        # Size of each fragment tx buffer in bytes.
        self._tcpIpIpReassemblyBufferSize: Optional["PositiveInteger"] = None

    @property
    def tcp_ip_ip_reassembly_buffer_size(self) -> Optional["PositiveInteger"]:
        """Get tcpIpIpReassemblyBufferSize (Pythonic accessor)."""
        return self._tcpIpIpReassemblyBufferSize

    @tcp_ip_ip_reassembly_buffer_size.setter
    def tcp_ip_ip_reassembly_buffer_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpIpIpReassemblyBufferSize with validation.

        Args:
            value: The tcpIpIpReassemblyBufferSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIpReassemblyBufferSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpIpIpReassemblyBufferSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpIpIpReassemblyBufferSize = value
        # These buffers will be used if the IpV6 receives packets the upper layer that
                # do not fit into the MTU and thus be fragmented.
        # of 0 disables tx fragmentation.
        self._tcpIpIpTx: Optional["PositiveInteger"] = None

    @property
    def tcp_ip_ip_tx(self) -> Optional["PositiveInteger"]:
        """Get tcpIpIpTx (Pythonic accessor)."""
        return self._tcpIpIpTx

    @tcp_ip_ip_tx.setter
    def tcp_ip_ip_tx(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpIpIpTx with validation.

        Args:
            value: The tcpIpIpTx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIpTx = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpIpIpTx must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpIpIpTx = value
        # Size of each fragment tx buffer in bytes.
        self._tcpIpIpTxFragmentBufferSize: Optional["PositiveInteger"] = None

    @property
    def tcp_ip_ip_tx_fragment_buffer_size(self) -> Optional["PositiveInteger"]:
        """Get tcpIpIpTxFragmentBufferSize (Pythonic accessor)."""
        return self._tcpIpIpTxFragmentBufferSize

    @tcp_ip_ip_tx_fragment_buffer_size.setter
    def tcp_ip_ip_tx_fragment_buffer_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tcpIpIpTxFragmentBufferSize with validation.

        Args:
            value: The tcpIpIpTxFragmentBufferSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tcpIpIpTxFragmentBufferSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"tcpIpIpTxFragmentBufferSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._tcpIpIpTxFragmentBufferSize = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTcpIpIp(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for tcpIpIp.

        Returns:
            The tcpIpIp value

        Note:
            Delegates to tcp_ip_ip property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip  # Delegates to property

    def setTcpIpIp(self, value: "TimeValue") -> "Ipv6FragmentationProps":
        """
        AUTOSAR-compliant setter for tcpIpIp with method chaining.

        Args:
            value: The tcpIpIp to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip property setter (gets validation automatically)
        """
        self.tcp_ip_ip = value  # Delegates to property setter
        return self

    def getTcpIpIpReassemblyBufferSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpIpIpReassemblyBufferSize.

        Returns:
            The tcpIpIpReassemblyBufferSize value

        Note:
            Delegates to tcp_ip_ip_reassembly_buffer_size property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip_reassembly_buffer_size  # Delegates to property

    def setTcpIpIpReassemblyBufferSize(self, value: "PositiveInteger") -> "Ipv6FragmentationProps":
        """
        AUTOSAR-compliant setter for tcpIpIpReassemblyBufferSize with method chaining.

        Args:
            value: The tcpIpIpReassemblyBufferSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip_reassembly_buffer_size property setter (gets validation automatically)
        """
        self.tcp_ip_ip_reassembly_buffer_size = value  # Delegates to property setter
        return self

    def getTcpIpIpTx(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpIpIpTx.

        Returns:
            The tcpIpIpTx value

        Note:
            Delegates to tcp_ip_ip_tx property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip_tx  # Delegates to property

    def setTcpIpIpTx(self, value: "PositiveInteger") -> "Ipv6FragmentationProps":
        """
        AUTOSAR-compliant setter for tcpIpIpTx with method chaining.

        Args:
            value: The tcpIpIpTx to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip_tx property setter (gets validation automatically)
        """
        self.tcp_ip_ip_tx = value  # Delegates to property setter
        return self

    def getTcpIpIpTxFragmentBufferSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tcpIpIpTxFragmentBufferSize.

        Returns:
            The tcpIpIpTxFragmentBufferSize value

        Note:
            Delegates to tcp_ip_ip_tx_fragment_buffer_size property (CODING_RULE_V2_00017)
        """
        return self.tcp_ip_ip_tx_fragment_buffer_size  # Delegates to property

    def setTcpIpIpTxFragmentBufferSize(self, value: "PositiveInteger") -> "Ipv6FragmentationProps":
        """
        AUTOSAR-compliant setter for tcpIpIpTxFragmentBufferSize with method chaining.

        Args:
            value: The tcpIpIpTxFragmentBufferSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to tcp_ip_ip_tx_fragment_buffer_size property setter (gets validation automatically)
        """
        self.tcp_ip_ip_tx_fragment_buffer_size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tcp_ip_ip(self, value: Optional["TimeValue"]) -> "Ipv6FragmentationProps":
        """
        Set tcpIpIp and return self for chaining.

        Args:
            value: The tcpIpIp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip("value")
        """
        self.tcp_ip_ip = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ip_reassembly_buffer_size(self, value: Optional["PositiveInteger"]) -> "Ipv6FragmentationProps":
        """
        Set tcpIpIpReassemblyBufferSize and return self for chaining.

        Args:
            value: The tcpIpIpReassemblyBufferSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip_reassembly_buffer_size("value")
        """
        self.tcp_ip_ip_reassembly_buffer_size = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ip_tx(self, value: Optional["PositiveInteger"]) -> "Ipv6FragmentationProps":
        """
        Set tcpIpIpTx and return self for chaining.

        Args:
            value: The tcpIpIpTx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip_tx("value")
        """
        self.tcp_ip_ip_tx = value  # Use property setter (gets validation)
        return self

    def with_tcp_ip_ip_tx_fragment_buffer_size(self, value: Optional["PositiveInteger"]) -> "Ipv6FragmentationProps":
        """
        Set tcpIpIpTxFragmentBufferSize and return self for chaining.

        Args:
            value: The tcpIpIpTxFragmentBufferSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tcp_ip_ip_tx_fragment_buffer_size("value")
        """
        self.tcp_ip_ip_tx_fragment_buffer_size = value  # Use property setter (gets validation)
        return self
