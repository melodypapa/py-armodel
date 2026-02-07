from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class EcucDestinationUriDef(Identifiable):
    """
    Description of an EcucDestinationUriDef that is used as target of
    EcucUriReferenceDefs.
    
    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucDestinationUriDef
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 82, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Description of the targeted EcucContainerDef.
        self._destinationUri: Optional["EcucDestinationUri"] = None

    @property
    def destination_uri(self) -> Optional["EcucDestinationUri"]:
        """Get destinationUri (Pythonic accessor)."""
        return self._destinationUri

    @destination_uri.setter
    def destination_uri(self, value: Optional["EcucDestinationUri"]) -> None:
        """
        Set destinationUri with validation.
        
        Args:
            value: The destinationUri to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationUri = None
            return

        if not isinstance(value, EcucDestinationUri):
            raise TypeError(
                f"destinationUri must be EcucDestinationUri or None, got {type(value).__name__}"
            )
        self._destinationUri = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationUri(self) -> "EcucDestinationUri":
        """
        AUTOSAR-compliant getter for destinationUri.
        
        Returns:
            The destinationUri value
        
        Note:
            Delegates to destination_uri property (CODING_RULE_V2_00017)
        """
        return self.destination_uri  # Delegates to property

    def setDestinationUri(self, value: "EcucDestinationUri") -> "EcucDestinationUriDef":
        """
        AUTOSAR-compliant setter for destinationUri with method chaining.
        
        Args:
            value: The destinationUri to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to destination_uri property setter (gets validation automatically)
        """
        self.destination_uri = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination_uri(self, value: Optional["EcucDestinationUri"]) -> "EcucDestinationUriDef":
        """
        Set destinationUri and return self for chaining.
        
        Args:
            value: The destinationUri to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_destination_uri("value")
        """
        self.destination_uri = value  # Use property setter (gets validation)
        return self