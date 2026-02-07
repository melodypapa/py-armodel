from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class GlobalTimeCouplingPortProps(ARObject):
    """
    Defines properties for the usage of the CouplingPort in the scope of Global
    Time Sync.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::GlobalTimeCouplingPortProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 875, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If cyclic propagation delay measurement is enabled, this represents the
        # default value of the propagation the first actually measured propagation
        # delay is cyclic propagation delay measurement is parameter defines a fixed
        # value for the.
        self._propagation: Optional["TimeValue"] = None

    @property
    def propagation(self) -> Optional["TimeValue"]:
        """Get propagation (Pythonic accessor)."""
        return self._propagation

    @propagation.setter
    def propagation(self, value: Optional["TimeValue"]) -> None:
        """
        Set propagation with validation.
        
        Args:
            value: The propagation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._propagation = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"propagation must be TimeValue or None, got {type(value).__name__}"
            )
        self._propagation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPropagation(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for propagation.
        
        Returns:
            The propagation value
        
        Note:
            Delegates to propagation property (CODING_RULE_V2_00017)
        """
        return self.propagation  # Delegates to property

    def setPropagation(self, value: "TimeValue") -> "GlobalTimeCouplingPortProps":
        """
        AUTOSAR-compliant setter for propagation with method chaining.
        
        Args:
            value: The propagation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to propagation property setter (gets validation automatically)
        """
        self.propagation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_propagation(self, value: Optional["TimeValue"]) -> "GlobalTimeCouplingPortProps":
        """
        Set propagation and return self for chaining.
        
        Args:
            value: The propagation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_propagation("value")
        """
        self.propagation = value  # Use property setter (gets validation)
        return self