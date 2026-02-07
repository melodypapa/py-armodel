from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DoIpTpConfig(TpConfig):
    """
    This element defines exactly one DoIpTp Configuration that is used to
    configure all DoIPChannels available in a DoIpInterface. Each DoIPChannel
    describes a connection between a doIpSourceAddress and a doIpTargetAddress
    and the exchange of DcmIPdus between the PduR and DoIP.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::DoIpTpConfig
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 555, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of logical DoIP Addresses.
        self._doIpLogicAddress: List["DoIpLogicAddress"] = []

    @property
    def do_ip_logic_address(self) -> List["DoIpLogicAddress"]:
        """Get doIpLogicAddress (Pythonic accessor)."""
        return self._doIpLogicAddress
        # Collection of unidirectional connections between a source a target address.
        self._tpConnection: List["DoIpTpConnection"] = []

    @property
    def tp_connection(self) -> List["DoIpTpConnection"]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDoIpLogicAddress(self) -> List["DoIpLogicAddress"]:
        """
        AUTOSAR-compliant getter for doIpLogicAddress.
        
        Returns:
            The doIpLogicAddress value
        
        Note:
            Delegates to do_ip_logic_address property (CODING_RULE_V2_00017)
        """
        return self.do_ip_logic_address  # Delegates to property

    def getTpConnection(self) -> List["DoIpTpConnection"]:
        """
        AUTOSAR-compliant getter for tpConnection.
        
        Returns:
            The tpConnection value
        
        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====