from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DoIpLogicTesterAddressProps(AbstractDoIpLogicAddressProps):
    """
    This meta-class acts as a target for references to the
    DoIpLogicTesterAddress and collects DoIpLogic TesterAddress specific
    settings.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::DoIP::DoIpLogicTesterAddressProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 556, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DoIPRoutingActivation describing the routing activations of
        # the DoIPTester.
        self._doIpTester: List["DoIpRoutingActivation"] = []

    @property
    def do_ip_tester(self) -> List["DoIpRoutingActivation"]:
        """Get doIpTester (Pythonic accessor)."""
        return self._doIpTester

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDoIpTester(self) -> List["DoIpRoutingActivation"]:
        """
        AUTOSAR-compliant getter for doIpTester.
        
        Returns:
            The doIpTester value
        
        Note:
            Delegates to do_ip_tester property (CODING_RULE_V2_00017)
        """
        return self.do_ip_tester  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====