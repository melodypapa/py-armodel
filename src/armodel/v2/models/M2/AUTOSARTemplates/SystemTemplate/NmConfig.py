from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class NmConfig(FibexElement):
    """
    Contains the all configuration elements for AUTOSAR Nm.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::NmConfig
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 672, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of NmClusterCouplings Derived, because NmCluster can vary.
        # atpVariation.
        self._nmCluster: List["NmClusterCoupling"] = []

    @property
    def nm_cluster(self) -> List["NmClusterCoupling"]:
        """Get nmCluster (Pythonic accessor)."""
        return self._nmCluster
        # Collection of NM ECUs because EcuInstance can be atpVariation.
        self._nmIfEcu: List["NmEcu"] = []

    @property
    def nm_if_ecu(self) -> List["NmEcu"]:
        """Get nmIfEcu (Pythonic accessor)."""
        return self._nmIfEcu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNmCluster(self) -> List["NmClusterCoupling"]:
        """
        AUTOSAR-compliant getter for nmCluster.
        
        Returns:
            The nmCluster value
        
        Note:
            Delegates to nm_cluster property (CODING_RULE_V2_00017)
        """
        return self.nm_cluster  # Delegates to property

    def getNmIfEcu(self) -> List["NmEcu"]:
        """
        AUTOSAR-compliant getter for nmIfEcu.
        
        Returns:
            The nmIfEcu value
        
        Note:
            Delegates to nm_if_ecu property (CODING_RULE_V2_00017)
        """
        return self.nm_if_ecu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====