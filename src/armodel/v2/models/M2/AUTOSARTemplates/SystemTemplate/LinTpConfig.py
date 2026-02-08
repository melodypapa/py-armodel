from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    LinTpConnection,
    LinTpNode,
    TpAddress,
    TpConfig,
)


class LinTpConfig(TpConfig):
    """
    This element defines exactly one Lin TP Configuration. One LinTpConfig
    element shall be created for each Lin Network in the System.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::LinTpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 614, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of TpAddresses.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpAddress: List["TpAddress"] = []

    @property
    def tp_address(self) -> List["TpAddress"]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress
        # Configuration of LIN TP channels.
        # because TpNode can vary.
        # atpVariation.
        self._tpConnection: List["LinTpConnection"] = []

    @property
    def tp_connection(self) -> List["LinTpConnection"]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection
        # Senders and receivers of LIN TP messages.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpNode: List["LinTpNode"] = []

    @property
    def tp_node(self) -> List["LinTpNode"]:
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

    def getTpConnection(self) -> List["LinTpConnection"]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    def getTpNode(self) -> List["LinTpNode"]:
        """
        AUTOSAR-compliant getter for tpNode.

        Returns:
            The tpNode value

        Note:
            Delegates to tp_node property (CODING_RULE_V2_00017)
        """
        return self.tp_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
