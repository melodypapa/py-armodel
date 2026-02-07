from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class EthTpConnection(TpConnection):
    """
    A connection identifies which PduTriggerings shall be handled using the "TP"
    semantics.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::EthTpConnection
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 618, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a PduTriggering that shall be transported "TP" semantics.
        self._tpSdu: List[RefType] = []

    @property
    def tp_sdu(self) -> List[RefType]:
        """Get tpSdu (Pythonic accessor)."""
        return self._tpSdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpSdu(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for tpSdu.
        
        Returns:
            The tpSdu value
        
        Note:
            Delegates to tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.tp_sdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====