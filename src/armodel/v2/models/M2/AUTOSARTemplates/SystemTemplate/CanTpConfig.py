from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    CanTpAddress,
    CanTpChannel,
    CanTpConnection,
    CanTpEcu,
    CanTpNode,
    TpConfig,
)


class CanTpConfig(TpConfig):
    """
    This element defines exactly one CAN TP Configuration. One CanTpConfig
    element shall be created for each CAN Network in the System.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::CanTpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 606, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of TP Addresses.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpAddress: List["CanTpAddress"] = []

    @property
    def tp_address(self) -> List["CanTpAddress"]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress
        # Configuration of CAN TP channels.
        # atpVariation.
        self._tpChannel: List["CanTpChannel"] = []

    @property
    def tp_channel(self) -> List["CanTpChannel"]:
        """Get tpChannel (Pythonic accessor)."""
        return self._tpChannel
        # Senders and receivers of CAN TP messages.
        # because TpNode can vary.
        # atpVariation.
        self._tpConnection: List["CanTpConnection"] = []

    @property
    def tp_connection(self) -> List["CanTpConnection"]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection
        # Collection of TP Ecus because EcuInstance can vary.
        # atpVariation.
        self._tpEcu: List["CanTpEcu"] = []

    @property
    def tp_ecu(self) -> List["CanTpEcu"]:
        """Get tpEcu (Pythonic accessor)."""
        return self._tpEcu
        # Senders and receivers of Can TP messages.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpNode: List["CanTpNode"] = []

    @property
    def tp_node(self) -> List["CanTpNode"]:
        """Get tpNode (Pythonic accessor)."""
        return self._tpNode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpAddress(self) -> List["CanTpAddress"]:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def getTpChannel(self) -> List["CanTpChannel"]:
        """
        AUTOSAR-compliant getter for tpChannel.

        Returns:
            The tpChannel value

        Note:
            Delegates to tp_channel property (CODING_RULE_V2_00017)
        """
        return self.tp_channel  # Delegates to property

    def getTpConnection(self) -> List["CanTpConnection"]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    def getTpEcu(self) -> List["CanTpEcu"]:
        """
        AUTOSAR-compliant getter for tpEcu.

        Returns:
            The tpEcu value

        Note:
            Delegates to tp_ecu property (CODING_RULE_V2_00017)
        """
        return self.tp_ecu  # Delegates to property

    def getTpNode(self) -> List["CanTpNode"]:
        """
        AUTOSAR-compliant getter for tpNode.

        Returns:
            The tpNode value

        Note:
            Delegates to tp_node property (CODING_RULE_V2_00017)
        """
        return self.tp_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
