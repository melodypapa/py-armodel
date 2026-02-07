from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class J1939SharedAddressCluster(Identifiable):
    """
    This meta-class represents the ability to identify several J1939Clusters
    that share a common address space for the routing of messages
    
    Package: M2::AUTOSARTemplates::SystemTemplate::J1939SharedAddressCluster
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 694, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This identifies the J1939Clusters that share a common space.
        self._participating: List["J1939Cluster"] = []

    @property
    def participating(self) -> List["J1939Cluster"]:
        """Get participating (Pythonic accessor)."""
        return self._participating

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getParticipating(self) -> List["J1939Cluster"]:
        """
        AUTOSAR-compliant getter for participating.
        
        Returns:
            The participating value
        
        Note:
            Delegates to participating property (CODING_RULE_V2_00017)
        """
        return self.participating  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====