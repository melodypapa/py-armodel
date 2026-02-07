from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ModeDeclarationMapping(Identifiable):
    """
    This meta-class implements a concrete mapping of two ModeDeclarations.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::ModeDeclarationMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 132, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the first ModeDeclaration of the Mode reference has the
                # multiplicity 1 to support use cases where e.
        # g.
        # one mode of the is mapped to several modes of the mode.
        self._firstMode: List["ModeDeclaration"] = []

    @property
    def first_mode(self) -> List["ModeDeclaration"]:
        """Get firstMode (Pythonic accessor)."""
        return self._firstMode
        # This represents the second ModeDeclaration of the Mode.
        self._secondMode: Optional["ModeDeclaration"] = None

    @property
    def second_mode(self) -> Optional["ModeDeclaration"]:
        """Get secondMode (Pythonic accessor)."""
        return self._secondMode

    @second_mode.setter
    def second_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set secondMode with validation.
        
        Args:
            value: The secondMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"secondMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._secondMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstMode(self) -> List["ModeDeclaration"]:
        """
        AUTOSAR-compliant getter for firstMode.
        
        Returns:
            The firstMode value
        
        Note:
            Delegates to first_mode property (CODING_RULE_V2_00017)
        """
        return self.first_mode  # Delegates to property

    def getSecondMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for secondMode.
        
        Returns:
            The secondMode value
        
        Note:
            Delegates to second_mode property (CODING_RULE_V2_00017)
        """
        return self.second_mode  # Delegates to property

    def setSecondMode(self, value: "ModeDeclaration") -> "ModeDeclarationMapping":
        """
        AUTOSAR-compliant setter for secondMode with method chaining.
        
        Args:
            value: The secondMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to second_mode property setter (gets validation automatically)
        """
        self.second_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_second_mode(self, value: Optional["ModeDeclaration"]) -> "ModeDeclarationMapping":
        """
        Set secondMode and return self for chaining.
        
        Args:
            value: The secondMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_second_mode("value")
        """
        self.second_mode = value  # Use property setter (gets validation)
        return self