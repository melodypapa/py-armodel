from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class MacSecCryptoAlgoConfig(ARObject):
    """
    This meta-class defines the cryptography configuration for MACsec.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::MacSecCryptoAlgoConfig
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 175, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the MACsec capability.
        self._capability: Optional["MacSecCapabilityEnum"] = None

    @property
    def capability(self) -> Optional["MacSecCapabilityEnum"]:
        """Get capability (Pythonic accessor)."""
        return self._capability

    @capability.setter
    def capability(self, value: Optional["MacSecCapabilityEnum"]) -> None:
        """
        Set capability with validation.
        
        Args:
            value: The capability to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._capability = None
            return

        if not isinstance(value, MacSecCapabilityEnum):
            raise TypeError(
                f"capability must be MacSecCapabilityEnum or None, got {type(value).__name__}"
            )
        self._capability = value
        # Tags: atp.
        # Status=candidate.
        self._cipherSuite: "MacSecCipherSuite" = None

    @property
    def cipher_suite(self) -> "MacSecCipherSuite":
        """Get cipherSuite (Pythonic accessor)."""
        return self._cipherSuite

    @cipher_suite.setter
    def cipher_suite(self, value: "MacSecCipherSuite") -> None:
        """
        Set cipherSuite with validation.
        
        Args:
            value: The cipherSuite to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, MacSecCipherSuite):
            raise TypeError(
                f"cipherSuite must be MacSecCipherSuite, got {type(value).__name__}"
            )
        self._cipherSuite = value
        # The MACsec confidentiality offset specifies the number of bytes starting from
                # the frame header.
        # MACsec encrypts bytes after the offset in a frame.
        self._confidentiality: Optional["MacSecConfidentiality"] = None

    @property
    def confidentiality(self) -> Optional["MacSecConfidentiality"]:
        """Get confidentiality (Pythonic accessor)."""
        return self._confidentiality

    @confidentiality.setter
    def confidentiality(self, value: Optional["MacSecConfidentiality"]) -> None:
        """
        Set confidentiality with validation.
        
        Args:
            value: The confidentiality to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._confidentiality = None
            return

        if not isinstance(value, MacSecConfidentiality):
            raise TypeError(
                f"confidentiality must be MacSecConfidentiality or None, got {type(value).__name__}"
            )
        self._confidentiality = value
        # In case replay protection is active, this attribute defines replay protection
        # window.
        self._replayProtection: Optional["PositiveInteger"] = None

    @property
    def replay_protection(self) -> Optional["PositiveInteger"]:
        """Get replayProtection (Pythonic accessor)."""
        return self._replayProtection

    @replay_protection.setter
    def replay_protection(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set replayProtection with validation.
        
        Args:
            value: The replayProtection to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._replayProtection = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"replayProtection must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._replayProtection = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCapability(self) -> "MacSecCapabilityEnum":
        """
        AUTOSAR-compliant getter for capability.
        
        Returns:
            The capability value
        
        Note:
            Delegates to capability property (CODING_RULE_V2_00017)
        """
        return self.capability  # Delegates to property

    def setCapability(self, value: "MacSecCapabilityEnum") -> "MacSecCryptoAlgoConfig":
        """
        AUTOSAR-compliant setter for capability with method chaining.
        
        Args:
            value: The capability to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to capability property setter (gets validation automatically)
        """
        self.capability = value  # Delegates to property setter
        return self

    def getCipherSuite(self) -> "MacSecCipherSuite":
        """
        AUTOSAR-compliant getter for cipherSuite.
        
        Returns:
            The cipherSuite value
        
        Note:
            Delegates to cipher_suite property (CODING_RULE_V2_00017)
        """
        return self.cipher_suite  # Delegates to property

    def setCipherSuite(self, value: "MacSecCipherSuite") -> "MacSecCryptoAlgoConfig":
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

    def getConfidentiality(self) -> "MacSecConfidentiality":
        """
        AUTOSAR-compliant getter for confidentiality.
        
        Returns:
            The confidentiality value
        
        Note:
            Delegates to confidentiality property (CODING_RULE_V2_00017)
        """
        return self.confidentiality  # Delegates to property

    def setConfidentiality(self, value: "MacSecConfidentiality") -> "MacSecCryptoAlgoConfig":
        """
        AUTOSAR-compliant setter for confidentiality with method chaining.
        
        Args:
            value: The confidentiality to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to confidentiality property setter (gets validation automatically)
        """
        self.confidentiality = value  # Delegates to property setter
        return self

    def getReplayProtection(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for replayProtection.
        
        Returns:
            The replayProtection value
        
        Note:
            Delegates to replay_protection property (CODING_RULE_V2_00017)
        """
        return self.replay_protection  # Delegates to property

    def setReplayProtection(self, value: "PositiveInteger") -> "MacSecCryptoAlgoConfig":
        """
        AUTOSAR-compliant setter for replayProtection with method chaining.
        
        Args:
            value: The replayProtection to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to replay_protection property setter (gets validation automatically)
        """
        self.replay_protection = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_capability(self, value: Optional["MacSecCapabilityEnum"]) -> "MacSecCryptoAlgoConfig":
        """
        Set capability and return self for chaining.
        
        Args:
            value: The capability to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_capability("value")
        """
        self.capability = value  # Use property setter (gets validation)
        return self

    def with_cipher_suite(self, value: "MacSecCipherSuite") -> "MacSecCryptoAlgoConfig":
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

    def with_confidentiality(self, value: Optional["MacSecConfidentiality"]) -> "MacSecCryptoAlgoConfig":
        """
        Set confidentiality and return self for chaining.
        
        Args:
            value: The confidentiality to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_confidentiality("value")
        """
        self.confidentiality = value  # Use property setter (gets validation)
        return self

    def with_replay_protection(self, value: Optional["PositiveInteger"]) -> "MacSecCryptoAlgoConfig":
        """
        Set replayProtection and return self for chaining.
        
        Args:
            value: The replayProtection to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_replay_protection("value")
        """
        self.replay_protection = value  # Use property setter (gets validation)
        return self