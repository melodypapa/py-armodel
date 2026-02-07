from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class BinaryManifestRequireResource(BinaryManifestResource):
    """
    This meta-class represents a required resource in the binary manifest.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::BinaryManifest::BinaryManifestRequireResource
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 916, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute indicates whether the connection of the BinaryManifestResource
        # is mandatory.
        self._connectionIs: Optional["Boolean"] = None

    @property
    def connection_is(self) -> Optional["Boolean"]:
        """Get connectionIs (Pythonic accessor)."""
        return self._connectionIs

    @connection_is.setter
    def connection_is(self, value: Optional["Boolean"]) -> None:
        """
        Set connectionIs with validation.
        
        Args:
            value: The connectionIs to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connectionIs = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"connectionIs must be Boolean or None, got {type(value).__name__}"
            )
        self._connectionIs = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnectionIs(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for connectionIs.
        
        Returns:
            The connectionIs value
        
        Note:
            Delegates to connection_is property (CODING_RULE_V2_00017)
        """
        return self.connection_is  # Delegates to property

    def setConnectionIs(self, value: "Boolean") -> "BinaryManifestRequireResource":
        """
        AUTOSAR-compliant setter for connectionIs with method chaining.
        
        Args:
            value: The connectionIs to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to connection_is property setter (gets validation automatically)
        """
        self.connection_is = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_connection_is(self, value: Optional["Boolean"]) -> "BinaryManifestRequireResource":
        """
        Set connectionIs and return self for chaining.
        
        Args:
            value: The connectionIs to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_connection_is("value")
        """
        self.connection_is = value  # Use property setter (gets validation)
        return self