from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class IPv6ExtHeaderFilterSet(ARElement):
    """
    Set of IPv6 Extension Header Filters.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::IPv6HeaderFilterList::IPv6ExtHeaderFilterSet
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 455, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # In order to permit or deny certain types of IPv6 extension a permitted list
        # of IPv6 extension headers can be.
        self._extHeaderFilter: List[RefType] = []

    @property
    def ext_header_filter(self) -> List[RefType]:
        """Get extHeaderFilter (Pythonic accessor)."""
        return self._extHeaderFilter

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getExtHeaderFilter(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for extHeaderFilter.
        
        Returns:
            The extHeaderFilter value
        
        Note:
            Delegates to ext_header_filter property (CODING_RULE_V2_00017)
        """
        return self.ext_header_filter  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====