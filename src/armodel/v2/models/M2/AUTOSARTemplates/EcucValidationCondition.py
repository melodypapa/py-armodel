from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class EcucValidationCondition(Identifiable):
    """
    Validation condition to perform a formula calculation based on EcucQueries.
    
    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucValidationCondition
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 103, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Query to the ECU Configuration Description.
        self._ecucQuery: List["EcucQuery"] = []

    @property
    def ecuc_query(self) -> List["EcucQuery"]:
        """Get ecucQuery (Pythonic accessor)."""
        return self._ecucQuery
        # Definition of the formula used to define validation.
        self._validation: Optional["EcucConditionFormula"] = None

    @property
    def validation(self) -> Optional["EcucConditionFormula"]:
        """Get validation (Pythonic accessor)."""
        return self._validation

    @validation.setter
    def validation(self, value: Optional["EcucConditionFormula"]) -> None:
        """
        Set validation with validation.
        
        Args:
            value: The validation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._validation = None
            return

        if not isinstance(value, EcucConditionFormula):
            raise TypeError(
                f"validation must be EcucConditionFormula or None, got {type(value).__name__}"
            )
        self._validation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcucQuery(self) -> List["EcucQuery"]:
        """
        AUTOSAR-compliant getter for ecucQuery.
        
        Returns:
            The ecucQuery value
        
        Note:
            Delegates to ecuc_query property (CODING_RULE_V2_00017)
        """
        return self.ecuc_query  # Delegates to property

    def getValidation(self) -> "EcucConditionFormula":
        """
        AUTOSAR-compliant getter for validation.
        
        Returns:
            The validation value
        
        Note:
            Delegates to validation property (CODING_RULE_V2_00017)
        """
        return self.validation  # Delegates to property

    def setValidation(self, value: "EcucConditionFormula") -> "EcucValidationCondition":
        """
        AUTOSAR-compliant setter for validation with method chaining.
        
        Args:
            value: The validation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to validation property setter (gets validation automatically)
        """
        self.validation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_validation(self, value: Optional["EcucConditionFormula"]) -> "EcucValidationCondition":
        """
        Set validation and return self for chaining.
        
        Args:
            value: The validation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_validation("value")
        """
        self.validation = value  # Use property setter (gets validation)
        return self