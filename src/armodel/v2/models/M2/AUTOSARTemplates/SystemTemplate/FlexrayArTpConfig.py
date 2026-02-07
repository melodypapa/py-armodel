from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class FlexrayArTpConfig(TpConfig):
    """
    This element defines exactly one FlexRay Autosar TP Configuration. One
    FlexrayArTpConfig element shall be created for each FlexRay Network in the
    System that uses Flex Ray Autosar TP.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayArTpConfig
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 599, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of TpAddresses.
        # atpVariation.
        self._tpAddress: List["TpAddress"] = []

    @property
    def tp_address(self) -> List["TpAddress"]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress
        # Configuration of FlexRay Autosar Transport Protocol atpVariation.
        self._tpChannel: List["FlexrayArTpChannel"] = []

    @property
    def tp_channel(self) -> List["FlexrayArTpChannel"]:
        """Get tpChannel (Pythonic accessor)."""
        return self._tpChannel
        # Senders and receivers of TP messages.
        # atpVariation.
        self._tpNode: List["FlexrayArTpNode"] = []

    @property
    def tp_node(self) -> List["FlexrayArTpNode"]:
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

    def getTpChannel(self) -> List["FlexrayArTpChannel"]:
        """
        AUTOSAR-compliant getter for tpChannel.
        
        Returns:
            The tpChannel value
        
        Note:
            Delegates to tp_channel property (CODING_RULE_V2_00017)
        """
        return self.tp_channel  # Delegates to property

    def getTpNode(self) -> List["FlexrayArTpNode"]:
        """
        AUTOSAR-compliant getter for tpNode.
        
        Returns:
            The tpNode value
        
        Note:
            Delegates to tp_node property (CODING_RULE_V2_00017)
        """
        return self.tp_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====