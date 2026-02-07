from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class DdsOwnership(ARObject):
    """
    Describes the DDS OWNERSHIP QoS policy.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsOwnership
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 532, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "OWNERSHIP" chapter of DDS.
        # atp.
        # Status=candidate.
        self._ownershipKind: Optional["DdsOwnershipKind"] = None

    @property
    def ownership_kind(self) -> Optional["DdsOwnershipKind"]:
        """Get ownershipKind (Pythonic accessor)."""
        return self._ownershipKind

    @ownership_kind.setter
    def ownership_kind(self, value: Optional["DdsOwnershipKind"]) -> None:
        """
        Set ownershipKind with validation.
        
        Args:
            value: The ownershipKind to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ownershipKind = None
            return

        if not isinstance(value, DdsOwnershipKind):
            raise TypeError(
                f"ownershipKind must be DdsOwnershipKind or None, got {type(value).__name__}"
            )
        self._ownershipKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOwnershipKind(self) -> "DdsOwnershipKind":
        """
        AUTOSAR-compliant getter for ownershipKind.
        
        Returns:
            The ownershipKind value
        
        Note:
            Delegates to ownership_kind property (CODING_RULE_V2_00017)
        """
        return self.ownership_kind  # Delegates to property

    def setOwnershipKind(self, value: "DdsOwnershipKind") -> "DdsOwnership":
        """
        AUTOSAR-compliant setter for ownershipKind with method chaining.
        
        Args:
            value: The ownershipKind to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ownership_kind property setter (gets validation automatically)
        """
        self.ownership_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ownership_kind(self, value: Optional["DdsOwnershipKind"]) -> "DdsOwnership":
        """
        Set ownershipKind and return self for chaining.
        
        Args:
            value: The ownershipKind to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ownership_kind("value")
        """
        self.ownership_kind = value  # Use property setter (gets validation)
        return self