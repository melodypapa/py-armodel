from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import TDEventCom

    RefType,
)


class TDEventFrameEthernet(TDEventCom):
    """
    This is used to describe timing description events related to the exchange
    of Ethernet frames between an Ethernet communication controller and the BSW
    Ethernet interface and driver module.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 69, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the SocketConnection by the means of which Data Units (PDU) are
        # transmitted or received Ethernet Frame.
        self._staticSocket: Optional["StaticSocketConnection"] = None

    @property
    def static_socket(self) -> Optional["StaticSocketConnection"]:
        """Get staticSocket (Pythonic accessor)."""
        return self._staticSocket

    @static_socket.setter
    def static_socket(self, value: Optional["StaticSocketConnection"]) -> None:
        """
        Set staticSocket with validation.

        Args:
            value: The staticSocket to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._staticSocket = None
            return

        if not isinstance(value, StaticSocketConnection):
            raise TypeError(
                f"staticSocket must be StaticSocketConnection or None, got {type(value).__name__}"
            )
        self._staticSocket = value
        # This is used to describe the specific event type of a.
        self._tdEventType: Optional["TDEventFrameEthernet"] = None

    @property
    def td_event_type(self) -> Optional["TDEventFrameEthernet"]:
        """Get tdEventType (Pythonic accessor)."""
        return self._tdEventType

    @td_event_type.setter
    def td_event_type(self, value: Optional["TDEventFrameEthernet"]) -> None:
        """
        Set tdEventType with validation.

        Args:
            value: The tdEventType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventType = None
            return

        if not isinstance(value, TDEventFrameEthernet):
            raise TypeError(
                f"tdEventType must be TDEventFrameEthernet or None, got {type(value).__name__}"
            )
        self._tdEventType = value
        # Specifies the header identifier or a range of header if contained in the
        # Ethernet frame let the.
        self._tdHeaderIdFilter: List["TDHeaderIdRange"] = []

    @property
    def td_header_id_filter(self) -> List["TDHeaderIdRange"]:
        """Get tdHeaderIdFilter (Pythonic accessor)."""
        return self._tdHeaderIdFilter
        # Specifies the PDU that if contained in the Ethernet frame the
        # TDEventFrameEthernet occur.
        self._tdPduTriggering: List[RefType] = []

    @property
    def td_pdu_triggering(self) -> List[RefType]:
        """Get tdPduTriggering (Pythonic accessor)."""
        return self._tdPduTriggering

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getStaticSocket(self) -> "StaticSocketConnection":
        """
        AUTOSAR-compliant getter for staticSocket.

        Returns:
            The staticSocket value

        Note:
            Delegates to static_socket property (CODING_RULE_V2_00017)
        """
        return self.static_socket  # Delegates to property

    def setStaticSocket(self, value: "StaticSocketConnection") -> "TDEventFrameEthernet":
        """
        AUTOSAR-compliant setter for staticSocket with method chaining.

        Args:
            value: The staticSocket to set

        Returns:
            self for method chaining

        Note:
            Delegates to static_socket property setter (gets validation automatically)
        """
        self.static_socket = value  # Delegates to property setter
        return self

    def getTdEventType(self) -> "TDEventFrameEthernet":
        """
        AUTOSAR-compliant getter for tdEventType.

        Returns:
            The tdEventType value

        Note:
            Delegates to td_event_type property (CODING_RULE_V2_00017)
        """
        return self.td_event_type  # Delegates to property

    def setTdEventType(self, value: "TDEventFrameEthernet") -> "TDEventFrameEthernet":
        """
        AUTOSAR-compliant setter for tdEventType with method chaining.

        Args:
            value: The tdEventType to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_type property setter (gets validation automatically)
        """
        self.td_event_type = value  # Delegates to property setter
        return self

    def getTdHeaderIdFilter(self) -> List["TDHeaderIdRange"]:
        """
        AUTOSAR-compliant getter for tdHeaderIdFilter.

        Returns:
            The tdHeaderIdFilter value

        Note:
            Delegates to td_header_id_filter property (CODING_RULE_V2_00017)
        """
        return self.td_header_id_filter  # Delegates to property

    def getTdPduTriggering(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for tdPduTriggering.

        Returns:
            The tdPduTriggering value

        Note:
            Delegates to td_pdu_triggering property (CODING_RULE_V2_00017)
        """
        return self.td_pdu_triggering  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_static_socket(self, value: Optional["StaticSocketConnection"]) -> "TDEventFrameEthernet":
        """
        Set staticSocket and return self for chaining.

        Args:
            value: The staticSocket to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_static_socket("value")
        """
        self.static_socket = value  # Use property setter (gets validation)
        return self

    def with_td_event_type(self, value: Optional["TDEventFrameEthernet"]) -> "TDEventFrameEthernet":
        """
        Set tdEventType and return self for chaining.

        Args:
            value: The tdEventType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_type("value")
        """
        self.td_event_type = value  # Use property setter (gets validation)
        return self
