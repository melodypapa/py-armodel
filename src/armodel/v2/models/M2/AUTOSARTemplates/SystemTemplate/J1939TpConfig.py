from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    J1939TpConnection,
    J1939TpNode,
    TpAddress,
    TpConfig,
)


class J1939TpConfig(TpConfig):
    """
    This element defines exactly one J1939 TP Configuration. One J1939TpConfig
    element shall be created for each J1939 Network in the System.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::J1939TpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 623, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of TP Adresses.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpAddress: List["TpAddress"] = []

    @property
    def tp_address(self) -> List["TpAddress"]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress
        # Configuration of J1939 TP connections.
        # because TpNode can vary.
        # atpVariation 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._tpConnection: List["J1939TpConnection"] = []

    @property
    def tp_connection(self) -> List["J1939TpConnection"]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection
        # Senders and receivers of J1939 TP messages.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpNode: List["J1939TpNode"] = []

    @property
    def tp_node(self) -> List["J1939TpNode"]:
        """Get tpNode (Pythonic accessor)."""
        return self._tpNode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpAddress(self) -> List["TpAddress"]:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def getTpConnection(self) -> List["J1939TpConnection"]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    def getTpNode(self) -> List["J1939TpNode"]:
        """
        AUTOSAR-compliant getter for tpNode.

        Returns:
            The tpNode value

        Note:
            Delegates to tp_node property (CODING_RULE_V2_00017)
        """
        return self.tp_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
