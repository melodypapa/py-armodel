from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class EcucDerivationSpecification(ARObject):
    """
    Allows to define configuration items that are calculated based on the value
    of • other parameter values • elements (attributes/classes) defined in other
    AUTOSAR templates such as System template and SW component template
    
    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucDerivationSpecification
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 87, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the formula used to calculate the value of the configuration
        # element.
        self._calculation: Optional["EcucParameter"] = None

    @property
    def calculation(self) -> Optional["EcucParameter"]:
        """Get calculation (Pythonic accessor)."""
        return self._calculation

    @calculation.setter
    def calculation(self, value: Optional["EcucParameter"]) -> None:
        """
        Set calculation with validation.
        
        Args:
            value: The calculation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calculation = None
            return

        if not isinstance(value, EcucParameter):
            raise TypeError(
                f"calculation must be EcucParameter or None, got {type(value).__name__}"
            )
        self._calculation = value
        # Query to the ECU Configuration Description.
        self._ecucQuery: List["EcucQuery"] = []

    @property
    def ecuc_query(self) -> List["EcucQuery"]:
        """Get ecucQuery (Pythonic accessor)."""
        return self._ecucQuery
        # Informal description of the derivation used to calculate the the
        # configuration element.
        self._informalFormula: Optional["MlFormula"] = None

    @property
    def informal_formula(self) -> Optional["MlFormula"]:
        """Get informalFormula (Pythonic accessor)."""
        return self._informalFormula

    @informal_formula.setter
    def informal_formula(self, value: Optional["MlFormula"]) -> None:
        """
        Set informalFormula with validation.
        
        Args:
            value: The informalFormula to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._informalFormula = None
            return

        if not isinstance(value, MlFormula):
            raise TypeError(
                f"informalFormula must be MlFormula or None, got {type(value).__name__}"
            )
        self._informalFormula = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalculation(self) -> "EcucParameter":
        """
        AUTOSAR-compliant getter for calculation.
        
        Returns:
            The calculation value
        
        Note:
            Delegates to calculation property (CODING_RULE_V2_00017)
        """
        return self.calculation  # Delegates to property

    def setCalculation(self, value: "EcucParameter") -> "EcucDerivationSpecification":
        """
        AUTOSAR-compliant setter for calculation with method chaining.
        
        Args:
            value: The calculation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to calculation property setter (gets validation automatically)
        """
        self.calculation = value  # Delegates to property setter
        return self

    def getEcucQuery(self) -> List["EcucQuery"]:
        """
        AUTOSAR-compliant getter for ecucQuery.
        
        Returns:
            The ecucQuery value
        
        Note:
            Delegates to ecuc_query property (CODING_RULE_V2_00017)
        """
        return self.ecuc_query  # Delegates to property

    def getInformalFormula(self) -> "MlFormula":
        """
        AUTOSAR-compliant getter for informalFormula.
        
        Returns:
            The informalFormula value
        
        Note:
            Delegates to informal_formula property (CODING_RULE_V2_00017)
        """
        return self.informal_formula  # Delegates to property

    def setInformalFormula(self, value: "MlFormula") -> "EcucDerivationSpecification":
        """
        AUTOSAR-compliant setter for informalFormula with method chaining.
        
        Args:
            value: The informalFormula to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to informal_formula property setter (gets validation automatically)
        """
        self.informal_formula = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_calculation(self, value: Optional["EcucParameter"]) -> "EcucDerivationSpecification":
        """
        Set calculation and return self for chaining.
        
        Args:
            value: The calculation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_calculation("value")
        """
        self.calculation = value  # Use property setter (gets validation)
        return self

    def with_informal_formula(self, value: Optional["MlFormula"]) -> "EcucDerivationSpecification":
        """
        Set informalFormula and return self for chaining.
        
        Args:
            value: The informalFormula to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_informal_formula("value")
        """
        self.informal_formula = value  # Use property setter (gets validation)
        return self