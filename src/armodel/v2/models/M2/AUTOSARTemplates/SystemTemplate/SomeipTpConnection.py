from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SomeipTpConnection(ARObject):
    """
    A connection identifies the sender and the receiver of this particular
    communication. The SOME/IP TP module routes a Pdu through this connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::SomeipTpConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 620, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Assignment of configuration properties valid for this.
        self._tpChannel: Optional["SomeipTpChannel"] = None

    @property
    def tp_channel(self) -> Optional["SomeipTpChannel"]:
        """Get tpChannel (Pythonic accessor)."""
        return self._tpChannel

    @tp_channel.setter
    def tp_channel(self, value: Optional["SomeipTpChannel"]) -> None:
        """
        Set tpChannel with validation.

        Args:
            value: The tpChannel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpChannel = None
            return

        if not isinstance(value, SomeipTpChannel):
            raise TypeError(
                f"tpChannel must be SomeipTpChannel or None, got {type(value).__name__}"
            )
        self._tpChannel = value
        # Reference to an IPdu that is segmented by the Transport.
        self._tpSdu: RefType = None

    @property
    def tp_sdu(self) -> RefType:
        """Get tpSdu (Pythonic accessor)."""
        return self._tpSdu

    @tp_sdu.setter
    def tp_sdu(self, value: RefType) -> None:
        """
        Set tpSdu with validation.

        Args:
            value: The tpSdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpSdu = None
            return

        self._tpSdu = value
        # Reference to the segmented IPdu.
        self._transportPdu: RefType = None

    @property
    def transport_pdu(self) -> RefType:
        """Get transportPdu (Pythonic accessor)."""
        return self._transportPdu

    @transport_pdu.setter
    def transport_pdu(self, value: RefType) -> None:
        """
        Set transportPdu with validation.

        Args:
            value: The transportPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transportPdu = None
            return

        self._transportPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpChannel(self) -> "SomeipTpChannel":
        """
        AUTOSAR-compliant getter for tpChannel.

        Returns:
            The tpChannel value

        Note:
            Delegates to tp_channel property (CODING_RULE_V2_00017)
        """
        return self.tp_channel  # Delegates to property

    def setTpChannel(self, value: "SomeipTpChannel") -> "SomeipTpConnection":
        """
        AUTOSAR-compliant setter for tpChannel with method chaining.

        Args:
            value: The tpChannel to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_channel property setter (gets validation automatically)
        """
        self.tp_channel = value  # Delegates to property setter
        return self

    def getTpSdu(self) -> RefType:
        """
        AUTOSAR-compliant getter for tpSdu.

        Returns:
            The tpSdu value

        Note:
            Delegates to tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.tp_sdu  # Delegates to property

    def setTpSdu(self, value: RefType) -> "SomeipTpConnection":
        """
        AUTOSAR-compliant setter for tpSdu with method chaining.

        Args:
            value: The tpSdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_sdu property setter (gets validation automatically)
        """
        self.tp_sdu = value  # Delegates to property setter
        return self

    def getTransportPdu(self) -> RefType:
        """
        AUTOSAR-compliant getter for transportPdu.

        Returns:
            The transportPdu value

        Note:
            Delegates to transport_pdu property (CODING_RULE_V2_00017)
        """
        return self.transport_pdu  # Delegates to property

    def setTransportPdu(self, value: RefType) -> "SomeipTpConnection":
        """
        AUTOSAR-compliant setter for transportPdu with method chaining.

        Args:
            value: The transportPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to transport_pdu property setter (gets validation automatically)
        """
        self.transport_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tp_channel(self, value: Optional["SomeipTpChannel"]) -> "SomeipTpConnection":
        """
        Set tpChannel and return self for chaining.

        Args:
            value: The tpChannel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_channel("value")
        """
        self.tp_channel = value  # Use property setter (gets validation)
        return self

    def with_tp_sdu(self, value: Optional[RefType]) -> "SomeipTpConnection":
        """
        Set tpSdu and return self for chaining.

        Args:
            value: The tpSdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_sdu("value")
        """
        self.tp_sdu = value  # Use property setter (gets validation)
        return self

    def with_transport_pdu(self, value: Optional[RefType]) -> "SomeipTpConnection":
        """
        Set transportPdu and return self for chaining.

        Args:
            value: The transportPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transport_pdu("value")
        """
        self.transport_pdu = value  # Use property setter (gets validation)
        return self
