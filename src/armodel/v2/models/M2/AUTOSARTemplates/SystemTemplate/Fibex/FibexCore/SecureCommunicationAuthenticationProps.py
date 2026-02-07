from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SecureCommunicationAuthenticationProps(Identifiable):
    """
    Authentication properties used to configure SecuredIPdus.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SecureCommunicationAuthenticationProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 371, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the length in bits of the code to be included in the
        # payload of the.
        self._authInfoTx: Optional["PositiveInteger"] = None

    @property
    def auth_info_tx(self) -> Optional["PositiveInteger"]:
        """Get authInfoTx (Pythonic accessor)."""
        return self._authInfoTx

    @auth_info_tx.setter
    def auth_info_tx(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set authInfoTx with validation.
        
        Args:
            value: The authInfoTx to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._authInfoTx = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"authInfoTx must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._authInfoTx = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthInfoTx(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for authInfoTx.
        
        Returns:
            The authInfoTx value
        
        Note:
            Delegates to auth_info_tx property (CODING_RULE_V2_00017)
        """
        return self.auth_info_tx  # Delegates to property

    def setAuthInfoTx(self, value: "PositiveInteger") -> "SecureCommunicationAuthenticationProps":
        """
        AUTOSAR-compliant setter for authInfoTx with method chaining.
        
        Args:
            value: The authInfoTx to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to auth_info_tx property setter (gets validation automatically)
        """
        self.auth_info_tx = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_auth_info_tx(self, value: Optional["PositiveInteger"]) -> "SecureCommunicationAuthenticationProps":
        """
        Set authInfoTx and return self for chaining.
        
        Args:
            value: The authInfoTx to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_auth_info_tx("value")
        """
        self.auth_info_tx = value  # Use property setter (gets validation)
        return self