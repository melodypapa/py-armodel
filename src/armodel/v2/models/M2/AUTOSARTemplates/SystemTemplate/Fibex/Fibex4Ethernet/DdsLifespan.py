from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class DdsLifespan(ARObject):
    """
    Describes the DDS LIFESPAN QoS policy.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsLifespan
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 536, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "LIFESPAN" chapter of DDS.
        # in seconds.
        self._lifespanDuration: Optional["Float"] = None

    @property
    def lifespan_duration(self) -> Optional["Float"]:
        """Get lifespanDuration (Pythonic accessor)."""
        return self._lifespanDuration

    @lifespan_duration.setter
    def lifespan_duration(self, value: Optional["Float"]) -> None:
        """
        Set lifespanDuration with validation.
        
        Args:
            value: The lifespanDuration to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lifespanDuration = None
            return

        if not isinstance(value, Float):
            raise TypeError(
                f"lifespanDuration must be Float or None, got {type(value).__name__}"
            )
        self._lifespanDuration = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLifespanDuration(self) -> "Float":
        """
        AUTOSAR-compliant getter for lifespanDuration.
        
        Returns:
            The lifespanDuration value
        
        Note:
            Delegates to lifespan_duration property (CODING_RULE_V2_00017)
        """
        return self.lifespan_duration  # Delegates to property

    def setLifespanDuration(self, value: "Float") -> "DdsLifespan":
        """
        AUTOSAR-compliant setter for lifespanDuration with method chaining.
        
        Args:
            value: The lifespanDuration to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to lifespan_duration property setter (gets validation automatically)
        """
        self.lifespan_duration = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_lifespan_duration(self, value: Optional["Float"]) -> "DdsLifespan":
        """
        Set lifespanDuration and return self for chaining.
        
        Args:
            value: The lifespanDuration to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_lifespan_duration("value")
        """
        self.lifespan_duration = value  # Use property setter (gets validation)
        return self