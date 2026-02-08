from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    TpConfig,
)


class FlexrayTpConfig(TpConfig):
    """
    This element defines exactly one FlexRay ISO TP Configuration. One
    FlexRayTpConfig element shall be created for each FlexRay Network in the
    System that uses Flex Ray Iso Tp.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 592, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configuration of FlexRay TP Pdu Pools.
        # atpVariation.
        self._pduPool: List["FlexrayTpPduPool"] = []

    @property
    def pdu_pool(self) -> List["FlexrayTpPduPool"]:
        """Get pduPool (Pythonic accessor)."""
        return self._pduPool
        # Collection of TpAddresses.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpAddress: List["TpAddress"] = []

    @property
    def tp_address(self) -> List["TpAddress"]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress
        # Configuration of FlexRay TP Connection Controls.
        # Stereotypes: atpSplitable; atpVariation.
        self._tpConnection: List["FlexrayTpConnection"] = []

    @property
    def tp_connection(self) -> List["FlexrayTpConnection"]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection
        # Collection of TP Ecus because EcuInstance can vary.
        # atpVariation.
        self._tpEcu: List["FlexrayTpEcu"] = []

    @property
    def tp_ecu(self) -> List["FlexrayTpEcu"]:
        """Get tpEcu (Pythonic accessor)."""
        return self._tpEcu
        # Senders and receivers of FlexRay TP messages.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpNode: List["FlexrayTpNode"] = []

    @property
    def tp_node(self) -> List["FlexrayTpNode"]:
        """Get tpNode (Pythonic accessor)."""
        return self._tpNode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPduPool(self) -> List["FlexrayTpPduPool"]:
        """
        AUTOSAR-compliant getter for pduPool.

        Returns:
            The pduPool value

        Note:
            Delegates to pdu_pool property (CODING_RULE_V2_00017)
        """
        return self.pdu_pool  # Delegates to property

    def getTpAddress(self) -> List["TpAddress"]:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def getTpConnection(self) -> List["FlexrayTpConnection"]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    def getTpEcu(self) -> List["FlexrayTpEcu"]:
        """
        AUTOSAR-compliant getter for tpEcu.

        Returns:
            The tpEcu value

        Note:
            Delegates to tp_ecu property (CODING_RULE_V2_00017)
        """
        return self.tp_ecu  # Delegates to property

    def getTpNode(self) -> List["FlexrayTpNode"]:
        """
        AUTOSAR-compliant getter for tpNode.

        Returns:
            The tpNode value

        Note:
            Delegates to tp_node property (CODING_RULE_V2_00017)
        """
        return self.tp_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
