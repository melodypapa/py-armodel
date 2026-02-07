from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class TlsCryptoServiceMapping(CryptoServiceMapping):
    """
    This meta-class has the ability to represent a crypto service mapping for
    the socket-based configuration of Transport Layer Security (TLS).
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication::TlsCryptoServiceMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 559, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the shared(i.
        # e.
        # applicable for the aggregated cipher suites) crypto service the execution of
                # key exchange during the.
        self._keyExchange: List["CryptoServicePrimitive"] = []

    @property
    def key_exchange(self) -> List["CryptoServicePrimitive"]:
        """Get keyExchange (Pythonic accessor)."""
        return self._keyExchange
        # This aggregation represents the collection of supported.
        self._tlsCipherSuite: List["TlsCryptoCipherSuite"] = []

    @property
    def tls_cipher_suite(self) -> List["TlsCryptoCipherSuite"]:
        """Get tlsCipherSuite (Pythonic accessor)."""
        return self._tlsCipherSuite
        # Defines if client authentication shall be applied for this connection.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._useClient: Optional["Boolean"] = None

    @property
    def use_client(self) -> Optional["Boolean"]:
        """Get useClient (Pythonic accessor)."""
        return self._useClient

    @use_client.setter
    def use_client(self, value: Optional["Boolean"]) -> None:
        """
        Set useClient with validation.
        
        Args:
            value: The useClient to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useClient = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"useClient must be Boolean or None, got {type(value).__name__}"
            )
        self._useClient = value
        # Defines if the security extension for max_fragment_length be supported as
        # defined in IETF RFC 8449, chapter.
        self._useSecurity: Optional["Boolean"] = None

    @property
    def use_security(self) -> Optional["Boolean"]:
        """Get useSecurity (Pythonic accessor)."""
        return self._useSecurity

    @use_security.setter
    def use_security(self, value: Optional["Boolean"]) -> None:
        """
        Set useSecurity with validation.
        
        Args:
            value: The useSecurity to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useSecurity = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"useSecurity must be Boolean or None, got {type(value).__name__}"
            )
        self._useSecurity = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getKeyExchange(self) -> List["CryptoServicePrimitive"]:
        """
        AUTOSAR-compliant getter for keyExchange.
        
        Returns:
            The keyExchange value
        
        Note:
            Delegates to key_exchange property (CODING_RULE_V2_00017)
        """
        return self.key_exchange  # Delegates to property

    def getTlsCipherSuite(self) -> List["TlsCryptoCipherSuite"]:
        """
        AUTOSAR-compliant getter for tlsCipherSuite.
        
        Returns:
            The tlsCipherSuite value
        
        Note:
            Delegates to tls_cipher_suite property (CODING_RULE_V2_00017)
        """
        return self.tls_cipher_suite  # Delegates to property

    def getUseClient(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useClient.
        
        Returns:
            The useClient value
        
        Note:
            Delegates to use_client property (CODING_RULE_V2_00017)
        """
        return self.use_client  # Delegates to property

    def setUseClient(self, value: "Boolean") -> "TlsCryptoServiceMapping":
        """
        AUTOSAR-compliant setter for useClient with method chaining.
        
        Args:
            value: The useClient to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to use_client property setter (gets validation automatically)
        """
        self.use_client = value  # Delegates to property setter
        return self

    def getUseSecurity(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useSecurity.
        
        Returns:
            The useSecurity value
        
        Note:
            Delegates to use_security property (CODING_RULE_V2_00017)
        """
        return self.use_security  # Delegates to property

    def setUseSecurity(self, value: "Boolean") -> "TlsCryptoServiceMapping":
        """
        AUTOSAR-compliant setter for useSecurity with method chaining.
        
        Args:
            value: The useSecurity to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to use_security property setter (gets validation automatically)
        """
        self.use_security = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_use_client(self, value: Optional["Boolean"]) -> "TlsCryptoServiceMapping":
        """
        Set useClient and return self for chaining.
        
        Args:
            value: The useClient to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_use_client("value")
        """
        self.use_client = value  # Use property setter (gets validation)
        return self

    def with_use_security(self, value: Optional["Boolean"]) -> "TlsCryptoServiceMapping":
        """
        Set useSecurity and return self for chaining.
        
        Args:
            value: The useSecurity to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_use_security("value")
        """
        self.use_security = value  # Use property setter (gets validation)
        return self