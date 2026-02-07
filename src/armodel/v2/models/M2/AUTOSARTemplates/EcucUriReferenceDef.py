from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class EcucUriReferenceDef(EcucAbstractInternalReferenceDef):
    """
    Definition of reference with a destination that is specified via a
    destinationUri. With such a reference it is possible to define a reference
    to a EcucContainerDef in a different module independent from the concrete
    definition of the target container.
    
    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucUriReferenceDef
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 81, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 190, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Any EcucContainerDef with a destinationUri that is the destinationUri that is
        # referenced here valid target.
        self._destinationUri: Optional["EcucDestinationUriDef"] = None

    @property
    def destination_uri(self) -> Optional["EcucDestinationUriDef"]:
        """Get destinationUri (Pythonic accessor)."""
        return self._destinationUri

    @destination_uri.setter
    def destination_uri(self, value: Optional["EcucDestinationUriDef"]) -> None:
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

        if not isinstance(value, EcucDestinationUriDef):
            raise TypeError(
                f"destinationUri must be EcucDestinationUriDef or None, got {type(value).__name__}"
            )
        self._destinationUri = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestinationUri(self) -> "EcucDestinationUriDef":
        """
        AUTOSAR-compliant getter for destinationUri.
        
        Returns:
            The destinationUri value
        
        Note:
            Delegates to destination_uri property (CODING_RULE_V2_00017)
        """
        return self.destination_uri  # Delegates to property

    def setDestinationUri(self, value: "EcucDestinationUriDef") -> "EcucUriReferenceDef":
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

    def with_destination_uri(self, value: Optional["EcucDestinationUriDef"]) -> "EcucUriReferenceDef":
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