from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticEnvironmentalCondition(DiagnosticCommonElement):
    """
    The meta-class DiagnosticEnvironmentalCondition formalizes the idea of a
    condition which is evaluated during runtime of the ECU by looking at
    "environmental" states (e.g. one such condition is that the vehicle is not
    driving, i.e. vehicle speed == 0).
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvironmentalCondition
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 79, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the formula part of the.
        self._formula: Optional["DiagnosticEnvCondition"] = None

    @property
    def formula(self) -> Optional["DiagnosticEnvCondition"]:
        """Get formula (Pythonic accessor)."""
        return self._formula

    @formula.setter
    def formula(self, value: Optional["DiagnosticEnvCondition"]) -> None:
        """
        Set formula with validation.
        
        Args:
            value: The formula to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._formula = None
            return

        if not isinstance(value, DiagnosticEnvCondition):
            raise TypeError(
                f"formula must be DiagnosticEnvCondition or None, got {type(value).__name__}"
            )
        self._formula = value
        # This aggregation contains a representation of Mode in the context of a
        # DiagnosticEnvironmental.
        self._modeElement: List["DiagnosticEnvMode"] = []

    @property
    def mode_element(self) -> List["DiagnosticEnvMode"]:
        """Get modeElement (Pythonic accessor)."""
        return self._modeElement

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFormula(self) -> "DiagnosticEnvCondition":
        """
        AUTOSAR-compliant getter for formula.
        
        Returns:
            The formula value
        
        Note:
            Delegates to formula property (CODING_RULE_V2_00017)
        """
        return self.formula  # Delegates to property

    def setFormula(self, value: "DiagnosticEnvCondition") -> "DiagnosticEnvironmentalCondition":
        """
        AUTOSAR-compliant setter for formula with method chaining.
        
        Args:
            value: The formula to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to formula property setter (gets validation automatically)
        """
        self.formula = value  # Delegates to property setter
        return self

    def getModeElement(self) -> List["DiagnosticEnvMode"]:
        """
        AUTOSAR-compliant getter for modeElement.
        
        Returns:
            The modeElement value
        
        Note:
            Delegates to mode_element property (CODING_RULE_V2_00017)
        """
        return self.mode_element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_formula(self, value: Optional["DiagnosticEnvCondition"]) -> "DiagnosticEnvironmentalCondition":
        """
        Set formula and return self for chaining.
        
        Args:
            value: The formula to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_formula("value")
        """
        self.formula = value  # Use property setter (gets validation)
        return self