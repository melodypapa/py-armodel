from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class DdsOwnershipStrength(ARObject):
    """
    Describes the DDS OWNERSHIP_STRENGTH QoS policy.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsOwnershipStrength
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 533, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "OWNERSHIP_STRENGTH" chapter of DDS.
        # atp.
        # Status=candidate.
        self._ownership: Optional["PositiveInteger"] = None

    @property
    def ownership(self) -> Optional["PositiveInteger"]:
        """Get ownership (Pythonic accessor)."""
        return self._ownership

    @ownership.setter
    def ownership(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set ownership with validation.
        
        Args:
            value: The ownership to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ownership = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"ownership must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._ownership = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOwnership(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for ownership.
        
        Returns:
            The ownership value
        
        Note:
            Delegates to ownership property (CODING_RULE_V2_00017)
        """
        return self.ownership  # Delegates to property

    def setOwnership(self, value: "PositiveInteger") -> "DdsOwnershipStrength":
        """
        AUTOSAR-compliant setter for ownership with method chaining.
        
        Args:
            value: The ownership to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ownership property setter (gets validation automatically)
        """
        self.ownership = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ownership(self, value: Optional["PositiveInteger"]) -> "DdsOwnershipStrength":
        """
        Set ownership and return self for chaining.
        
        Args:
            value: The ownership to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ownership("value")
        """
        self.ownership = value  # Use property setter (gets validation)
        return self