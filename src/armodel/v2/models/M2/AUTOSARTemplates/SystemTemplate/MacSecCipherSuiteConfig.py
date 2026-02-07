from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class MacSecCipherSuiteConfig(ARObject):
    """
    This meta-class defines the cipher suite configuration to use with MACsec.
    cipherSuitePriority is present in case the MKA instance acts as a Key Server
    to select the cipher suite to use for MACsec. (cid:53) 175 of 2090 Document
    ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11
    (cid:52)
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::MacSecCipherSuiteConfig
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 175, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # In case the MKA instance acts as a Key Server, the is used to select the
        # Cipher Suite to use with the supported Ciphers.
        self._cipherSuite: Optional["PositiveInteger"] = None

    @property
    def cipher_suite(self) -> Optional["PositiveInteger"]:
        """Get cipherSuite (Pythonic accessor)."""
        return self._cipherSuite

    @cipher_suite.setter
    def cipher_suite(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set cipherSuite with validation.
        
        Args:
            value: The cipherSuite to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cipherSuite = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"cipherSuite must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._cipherSuite = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCipherSuite(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for cipherSuite.
        
        Returns:
            The cipherSuite value
        
        Note:
            Delegates to cipher_suite property (CODING_RULE_V2_00017)
        """
        return self.cipher_suite  # Delegates to property

    def setCipherSuite(self, value: "PositiveInteger") -> "MacSecCipherSuiteConfig":
        """
        AUTOSAR-compliant setter for cipherSuite with method chaining.
        
        Args:
            value: The cipherSuite to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to cipher_suite property setter (gets validation automatically)
        """
        self.cipher_suite = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cipher_suite(self, value: Optional["PositiveInteger"]) -> "MacSecCipherSuiteConfig":
        """
        Set cipherSuite and return self for chaining.
        
        Args:
            value: The cipherSuite to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_cipher_suite("value")
        """
        self.cipher_suite = value  # Use property setter (gets validation)
        return self