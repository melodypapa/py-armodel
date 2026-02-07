from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AtpPrototype(Identifiable, ABC):
    """
    A prototype is a typed feature. A prototype in a classifier indicates that
    instances of that classifier will have a feature, and the structure of that
    feature is given by the its type. An instance of that type will play the
    role indicated by the feature in the owning classifier. A feature is not an
    instance but an indication of an instance-to-be.
    
    Package: M2::AUTOSARTemplates::GenericStructure::AbstractStructure::AtpPrototype
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 175, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AtpPrototype:
            raise TypeError("AtpPrototype is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the type of the feature.
        self._atpType: "AtpType" = None

    @property
    def atp_type(self) -> "AtpType":
        """Get atpType (Pythonic accessor)."""
        return self._atpType

    @atp_type.setter
    def atp_type(self, value: "AtpType") -> None:
        """
        Set atpType with validation.
        
        Args:
            value: The atpType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AtpType):
            raise TypeError(
                f"atpType must be AtpType, got {type(value).__name__}"
            )
        self._atpType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAtpType(self) -> "AtpType":
        """
        AUTOSAR-compliant getter for atpType.
        
        Returns:
            The atpType value
        
        Note:
            Delegates to atp_type property (CODING_RULE_V2_00017)
        """
        return self.atp_type  # Delegates to property

    def setAtpType(self, value: "AtpType") -> "AtpPrototype":
        """
        AUTOSAR-compliant setter for atpType with method chaining.
        
        Args:
            value: The atpType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to atp_type property setter (gets validation automatically)
        """
        self.atp_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_atp_type(self, value: "AtpType") -> "AtpPrototype":
        """
        Set atpType and return self for chaining.
        
        Args:
            value: The atpType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_atp_type("value")
        """
        self.atp_type = value  # Use property setter (gets validation)
        return self