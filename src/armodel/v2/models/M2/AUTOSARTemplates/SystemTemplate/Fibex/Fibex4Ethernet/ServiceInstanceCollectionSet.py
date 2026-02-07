from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class ServiceInstanceCollectionSet(FibexElement):
    """
    Collection of ServiceInstances
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::ServiceInstanceCollectionSet
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 476, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ServiceInstances that are part of the collection.
        # atpSplitable; atpVariation.
        self._serviceInstance: List["AbstractService"] = []

    @property
    def service_instance(self) -> List["AbstractService"]:
        """Get serviceInstance (Pythonic accessor)."""
        return self._serviceInstance

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getServiceInstance(self) -> List["AbstractService"]:
        """
        AUTOSAR-compliant getter for serviceInstance.
        
        Returns:
            The serviceInstance value
        
        Note:
            Delegates to service_instance property (CODING_RULE_V2_00017)
        """
        return self.service_instance  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====