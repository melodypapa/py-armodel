from typing import List


class IEEE1722TpConfig(TpConfig):
    """
    Definition of the IEEE1722Tp protocol.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 636, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of IEEE1722Tp connections.
        # atpVariation.
        self._tpConnection: List["IEEE1722TpConnection"] = []

    @property
    def tp_connection(self) -> List["IEEE1722TpConnection"]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpConnection(self) -> List["IEEE1722TpConnection"]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
