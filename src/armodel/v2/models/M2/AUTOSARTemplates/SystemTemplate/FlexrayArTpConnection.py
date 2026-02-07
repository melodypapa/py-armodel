from typing import List, Optional


class FlexrayArTpConnection(TpConnection):
    """
    A connection within a channel identifies the sender and the receiver of this
    particular communication. The FlexRay Autosar Tp module routes a Pdu through
    this connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayArTpConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 603, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This parameter defines the number of PDUs that shall be for this connection
                # when it is active.
        # The range.
        self._connectionPrio: Optional["Integer"] = None

    @property
    def connection_prio(self) -> Optional["Integer"]:
        """Get connectionPrio (Pythonic accessor)."""
        return self._connectionPrio

    @connection_prio.setter
    def connection_prio(self, value: Optional["Integer"]) -> None:
        """
        Set connectionPrio with validation.

        Args:
            value: The connectionPrio to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connectionPrio = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"connectionPrio must be Integer or None, got {type(value).__name__}"
            )
        self._connectionPrio = value
        # Reference to the IPdu that is segmented by the Transport address of the
        # transmitted NPdu is the configured source Communication target address of the
        # transmitted NPdu is the configured target Communication.
        self._directTpSdu: Optional["IPdu"] = None

    @property
    def direct_tp_sdu(self) -> Optional["IPdu"]:
        """Get directTpSdu (Pythonic accessor)."""
        return self._directTpSdu

    @direct_tp_sdu.setter
    def direct_tp_sdu(self, value: Optional["IPdu"]) -> None:
        """
        Set directTpSdu with validation.

        Args:
            value: The directTpSdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._directTpSdu = None
            return

        if not isinstance(value, IPdu):
            raise TypeError(
                f"directTpSdu must be IPdu or None, got {type(value).__name__}"
            )
        self._directTpSdu = value
        # TP address for 1:n connections.
        self._multicast: Optional["TpAddress"] = None

    @property
    def multicast(self) -> Optional["TpAddress"]:
        """Get multicast (Pythonic accessor)."""
        return self._multicast

    @multicast.setter
    def multicast(self, value: Optional["TpAddress"]) -> None:
        """
        Set multicast with validation.

        Args:
            value: The multicast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._multicast = None
            return

        if not isinstance(value, TpAddress):
            raise TypeError(
                f"multicast must be TpAddress or None, got {type(value).__name__}"
            )
        self._multicast = value
        # Reference to the IPdu that is segmented by the Transport support of both
                # sending and receiving is used, references the IPdu used for the direction.
        # address of the transmitted NPdu is the configured target Communication target
                # address of the transmitted NPdu is the configured source Communication.
        self._reversedTpSdu: Optional["IPdu"] = None

    @property
    def reversed_tp_sdu(self) -> Optional["IPdu"]:
        """Get reversedTpSdu (Pythonic accessor)."""
        return self._reversedTpSdu

    @reversed_tp_sdu.setter
    def reversed_tp_sdu(self, value: Optional["IPdu"]) -> None:
        """
        Set reversedTpSdu with validation.

        Args:
            value: The reversedTpSdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._reversedTpSdu = None
            return

        if not isinstance(value, IPdu):
            raise TypeError(
                f"reversedTpSdu must be IPdu or None, got {type(value).__name__}"
            )
        self._reversedTpSdu = value
        # The source of the TP connection.
        self._source: Optional["FlexrayArTpNode"] = None

    @property
    def source(self) -> Optional["FlexrayArTpNode"]:
        """Get source (Pythonic accessor)."""
        return self._source

    @source.setter
    def source(self, value: Optional["FlexrayArTpNode"]) -> None:
        """
        Set source with validation.

        Args:
            value: The source to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._source = None
            return

        if not isinstance(value, FlexrayArTpNode):
            raise TypeError(
                f"source must be FlexrayArTpNode or None, got {type(value).__name__}"
            )
        self._source = value
        # The target of the TP connection.
        self._target: List["FlexrayArTpNode"] = []

    @property
    def target(self) -> List["FlexrayArTpNode"]:
        """Get target (Pythonic accessor)."""
        return self._target

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnectionPrio(self) -> "Integer":
        """
        AUTOSAR-compliant getter for connectionPrio.

        Returns:
            The connectionPrio value

        Note:
            Delegates to connection_prio property (CODING_RULE_V2_00017)
        """
        return self.connection_prio  # Delegates to property

    def setConnectionPrio(self, value: "Integer") -> "FlexrayArTpConnection":
        """
        AUTOSAR-compliant setter for connectionPrio with method chaining.

        Args:
            value: The connectionPrio to set

        Returns:
            self for method chaining

        Note:
            Delegates to connection_prio property setter (gets validation automatically)
        """
        self.connection_prio = value  # Delegates to property setter
        return self

    def getDirectTpSdu(self) -> "IPdu":
        """
        AUTOSAR-compliant getter for directTpSdu.

        Returns:
            The directTpSdu value

        Note:
            Delegates to direct_tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.direct_tp_sdu  # Delegates to property

    def setDirectTpSdu(self, value: "IPdu") -> "FlexrayArTpConnection":
        """
        AUTOSAR-compliant setter for directTpSdu with method chaining.

        Args:
            value: The directTpSdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to direct_tp_sdu property setter (gets validation automatically)
        """
        self.direct_tp_sdu = value  # Delegates to property setter
        return self

    def getMulticast(self) -> "TpAddress":
        """
        AUTOSAR-compliant getter for multicast.

        Returns:
            The multicast value

        Note:
            Delegates to multicast property (CODING_RULE_V2_00017)
        """
        return self.multicast  # Delegates to property

    def setMulticast(self, value: "TpAddress") -> "FlexrayArTpConnection":
        """
        AUTOSAR-compliant setter for multicast with method chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Note:
            Delegates to multicast property setter (gets validation automatically)
        """
        self.multicast = value  # Delegates to property setter
        return self

    def getReversedTpSdu(self) -> "IPdu":
        """
        AUTOSAR-compliant getter for reversedTpSdu.

        Returns:
            The reversedTpSdu value

        Note:
            Delegates to reversed_tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.reversed_tp_sdu  # Delegates to property

    def setReversedTpSdu(self, value: "IPdu") -> "FlexrayArTpConnection":
        """
        AUTOSAR-compliant setter for reversedTpSdu with method chaining.

        Args:
            value: The reversedTpSdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to reversed_tp_sdu property setter (gets validation automatically)
        """
        self.reversed_tp_sdu = value  # Delegates to property setter
        return self

    def getSource(self) -> "FlexrayArTpNode":
        """
        AUTOSAR-compliant getter for source.

        Returns:
            The source value

        Note:
            Delegates to source property (CODING_RULE_V2_00017)
        """
        return self.source  # Delegates to property

    def setSource(self, value: "FlexrayArTpNode") -> "FlexrayArTpConnection":
        """
        AUTOSAR-compliant setter for source with method chaining.

        Args:
            value: The source to set

        Returns:
            self for method chaining

        Note:
            Delegates to source property setter (gets validation automatically)
        """
        self.source = value  # Delegates to property setter
        return self

    def getTarget(self) -> List["FlexrayArTpNode"]:
        """
        AUTOSAR-compliant getter for target.

        Returns:
            The target value

        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_connection_prio(self, value: Optional["Integer"]) -> "FlexrayArTpConnection":
        """
        Set connectionPrio and return self for chaining.

        Args:
            value: The connectionPrio to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connection_prio("value")
        """
        self.connection_prio = value  # Use property setter (gets validation)
        return self

    def with_direct_tp_sdu(self, value: Optional["IPdu"]) -> "FlexrayArTpConnection":
        """
        Set directTpSdu and return self for chaining.

        Args:
            value: The directTpSdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direct_tp_sdu("value")
        """
        self.direct_tp_sdu = value  # Use property setter (gets validation)
        return self

    def with_multicast(self, value: Optional["TpAddress"]) -> "FlexrayArTpConnection":
        """
        Set multicast and return self for chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_multicast("value")
        """
        self.multicast = value  # Use property setter (gets validation)
        return self

    def with_reversed_tp_sdu(self, value: Optional["IPdu"]) -> "FlexrayArTpConnection":
        """
        Set reversedTpSdu and return self for chaining.

        Args:
            value: The reversedTpSdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reversed_tp_sdu("value")
        """
        self.reversed_tp_sdu = value  # Use property setter (gets validation)
        return self

    def with_source(self, value: Optional["FlexrayArTpNode"]) -> "FlexrayArTpConnection":
        """
        Set source and return self for chaining.

        Args:
            value: The source to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source("value")
        """
        self.source = value  # Use property setter (gets validation)
        return self
