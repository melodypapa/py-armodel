from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import TpConfig


class EthTpConfig(TpConfig):
    """
    This element defines which PduTriggerings shall be handled using "TP"
    semantics.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::EthTpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 617, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Senders and receivers of SOME/IP TP messages.
        self._tpConnection: List["EthTpConnection"] = []

    @property
    def tp_connection(self) -> List["EthTpConnection"]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpConnection(self) -> List["EthTpConnection"]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
