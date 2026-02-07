from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AtpBlueprintMapping(ARObject, ABC):
    """
    This meta-class represents the ability to express a particular mapping
    between a blueprint and an element derived from this blueprint. Particular
    mappings are defined by specializations of this meta-class.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure::AtpBlueprintMapping
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 161, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AtpBlueprintMapping:
            raise TypeError("AtpBlueprintMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the blueprint.
        # atpUriDef.
        self._atpBlueprint: "AtpBlueprint" = None

    @property
    def atp_blueprint(self) -> "AtpBlueprint":
        """Get atpBlueprint (Pythonic accessor)."""
        return self._atpBlueprint

    @atp_blueprint.setter
    def atp_blueprint(self, value: "AtpBlueprint") -> None:
        """
        Set atpBlueprint with validation.
        
        Args:
            value: The atpBlueprint to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AtpBlueprint):
            raise TypeError(
                f"atpBlueprint must be AtpBlueprint, got {type(value).__name__}"
            )
        self._atpBlueprint = value
        # This represents the bluprinted elements which shall be to the blueprint.
        self._atpBlueprinted: "AtpBlueprintable" = None

    @property
    def atp_blueprinted(self) -> "AtpBlueprintable":
        """Get atpBlueprinted (Pythonic accessor)."""
        return self._atpBlueprinted

    @atp_blueprinted.setter
    def atp_blueprinted(self, value: "AtpBlueprintable") -> None:
        """
        Set atpBlueprinted with validation.
        
        Args:
            value: The atpBlueprinted to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AtpBlueprintable):
            raise TypeError(
                f"atpBlueprinted must be AtpBlueprintable, got {type(value).__name__}"
            )
        self._atpBlueprinted = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAtpBlueprint(self) -> "AtpBlueprint":
        """
        AUTOSAR-compliant getter for atpBlueprint.
        
        Returns:
            The atpBlueprint value
        
        Note:
            Delegates to atp_blueprint property (CODING_RULE_V2_00017)
        """
        return self.atp_blueprint  # Delegates to property

    def setAtpBlueprint(self, value: "AtpBlueprint") -> "AtpBlueprintMapping":
        """
        AUTOSAR-compliant setter for atpBlueprint with method chaining.
        
        Args:
            value: The atpBlueprint to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to atp_blueprint property setter (gets validation automatically)
        """
        self.atp_blueprint = value  # Delegates to property setter
        return self

    def getAtpBlueprinted(self) -> "AtpBlueprintable":
        """
        AUTOSAR-compliant getter for atpBlueprinted.
        
        Returns:
            The atpBlueprinted value
        
        Note:
            Delegates to atp_blueprinted property (CODING_RULE_V2_00017)
        """
        return self.atp_blueprinted  # Delegates to property

    def setAtpBlueprinted(self, value: "AtpBlueprintable") -> "AtpBlueprintMapping":
        """
        AUTOSAR-compliant setter for atpBlueprinted with method chaining.
        
        Args:
            value: The atpBlueprinted to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to atp_blueprinted property setter (gets validation automatically)
        """
        self.atp_blueprinted = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_atp_blueprint(self, value: "AtpBlueprint") -> "AtpBlueprintMapping":
        """
        Set atpBlueprint and return self for chaining.
        
        Args:
            value: The atpBlueprint to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_atp_blueprint("value")
        """
        self.atp_blueprint = value  # Use property setter (gets validation)
        return self

    def with_atp_blueprinted(self, value: "AtpBlueprintable") -> "AtpBlueprintMapping":
        """
        Set atpBlueprinted and return self for chaining.
        
        Args:
            value: The atpBlueprinted to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_atp_blueprinted("value")
        """
        self.atp_blueprinted = value  # Use property setter (gets validation)
        return self