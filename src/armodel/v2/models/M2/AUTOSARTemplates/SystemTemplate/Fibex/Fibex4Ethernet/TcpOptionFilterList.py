from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TcpOptionFilterList(Identifiable):
    """
    Permitted list for the filtering of TCP options.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::TcpOptionFilterSet::TcpOptionFilterList
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 457, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # TCP option kind allowed by this filter.
        self._allowedTcpOption: List["PositiveInteger"] = []

    @property
    def allowed_tcp_option(self) -> List["PositiveInteger"]:
        """Get allowedTcpOption (Pythonic accessor)."""
        return self._allowedTcpOption

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAllowedTcpOption(self) -> List["PositiveInteger"]:
        """
        AUTOSAR-compliant getter for allowedTcpOption.
        
        Returns:
            The allowedTcpOption value
        
        Note:
            Delegates to allowed_tcp_option property (CODING_RULE_V2_00017)
        """
        return self.allowed_tcp_option  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====