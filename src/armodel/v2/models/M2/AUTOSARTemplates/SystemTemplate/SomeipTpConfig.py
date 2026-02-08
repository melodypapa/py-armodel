from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    SomeipTpChannel,
    SomeipTpConnection,
    TpConfig,
)


class SomeipTpConfig(TpConfig):
    """
    This element defines exactly one SOME/IP TP Configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::SomeipTpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 619, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of SomeipTpChannels that are collecting that are valid for a
        # collection of.
        self._tpChannel: List["SomeipTpChannel"] = []

    @property
    def tp_channel(self) -> List["SomeipTpChannel"]:
        """Get tpChannel (Pythonic accessor)."""
        return self._tpChannel
        # Senders and receivers of SOME/IP TP messages.
        self._tpConnection: List["SomeipTpConnection"] = []

    @property
    def tp_connection(self) -> List["SomeipTpConnection"]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpChannel(self) -> List["SomeipTpChannel"]:
        """
        AUTOSAR-compliant getter for tpChannel.

        Returns:
            The tpChannel value

        Note:
            Delegates to tp_channel property (CODING_RULE_V2_00017)
        """
        return self.tp_channel  # Delegates to property

    def getTpConnection(self) -> List["SomeipTpConnection"]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
