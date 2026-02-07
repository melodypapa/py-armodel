from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class SecureCommunicationPropsSet(FibexElement):
    """
    Collection of properties used to configure SecuredIPdus.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SecureCommunicationPropsSet
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 370, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Authentication properties used to configure Secured IPdus.
        self._authentication: List["SecureCommunication"] = []

    @property
    def authentication(self) -> List["SecureCommunication"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication
        # Freshness properties used to configure SecuredIPdus.
        self._freshnessProps: List["SecureCommunication"] = []

    @property
    def freshness_props(self) -> List["SecureCommunication"]:
        """Get freshnessProps (Pythonic accessor)."""
        return self._freshnessProps

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> List["SecureCommunication"]:
        """
        AUTOSAR-compliant getter for authentication.
        
        Returns:
            The authentication value
        
        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def getFreshnessProps(self) -> List["SecureCommunication"]:
        """
        AUTOSAR-compliant getter for freshnessProps.
        
        Returns:
            The freshnessProps value
        
        Note:
            Delegates to freshness_props property (CODING_RULE_V2_00017)
        """
        return self.freshness_props  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====