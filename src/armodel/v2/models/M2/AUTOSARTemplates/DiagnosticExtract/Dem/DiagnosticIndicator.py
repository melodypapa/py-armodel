"""
AUTOSAR Package - DiagnosticIndicator

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticIndicator
"""

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class DiagnosticIndicator(DiagnosticCommonElement):
    """
    Definition of an indicator.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticIndicator::DiagnosticIndicator
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 203, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the type of the indicator.
        # atpVariation.
        self._type: Optional["DiagnosticIndicatorType"] = None

    @property
    def type(self) -> Optional["DiagnosticIndicatorType"]:
        """Get type (Pythonic accessor)."""
        return self._type

    @type.setter
    def type(self, value: Optional["DiagnosticIndicatorType"]) -> None:
        """
        Set type with validation.
        
        Args:
            value: The type to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._type = None
            return

        if not isinstance(value, DiagnosticIndicatorType):
            raise TypeError(
                f"type must be DiagnosticIndicatorType or None, got {type(value).__name__}"
            )
        self._type = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getType(self) -> "DiagnosticIndicatorType":
        """
        AUTOSAR-compliant getter for type.
        
        Returns:
            The type value
        
        Note:
            Delegates to type property (CODING_RULE_V2_00017)
        """
        return self.type  # Delegates to property

    def setType(self, value: "DiagnosticIndicatorType") -> "DiagnosticIndicator":
        """
        AUTOSAR-compliant setter for type with method chaining.
        
        Args:
            value: The type to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to type property setter (gets validation automatically)
        """
        self.type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_type(self, value: Optional["DiagnosticIndicatorType"]) -> "DiagnosticIndicator":
        """
        Set type and return self for chaining.
        
        Args:
            value: The type to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_type("value")
        """
        self.type = value  # Use property setter (gets validation)
        return self


class DiagnosticIndicatorTypeEnum(AREnum):
    """
    DiagnosticIndicatorTypeEnum enumeration

Type of an indicator. Aggregated by DiagnosticIndicator.type, IndicatorStatusNeeds.type

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dem::DiagnosticIndicator
    """
    # Amber Warning Lamp
    amberWarning = "0"

    # Malfunction Indicator Lamp
    malfunction = "1"

    # Protect Lamp
    protectLamp = "2"

    # Red Stop Lamp
    redStopLamp = "3"

    # Warning
    warning = "4"
