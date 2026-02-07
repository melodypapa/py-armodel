from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class RestrictionWithSeverity(ARObject, ABC):
    """
    A restriction that has a severity. The severity describes the severity level
    that is reported in case the restriction is violated.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Common::RestrictionWithSeverity
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 86, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is RestrictionWithSeverity:
            raise TypeError("RestrictionWithSeverity is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Severity level that is reported in case the restriction is.
        self._severity: "SeverityEnum" = None

    @property
    def severity(self) -> "SeverityEnum":
        """Get severity (Pythonic accessor)."""
        return self._severity

    @severity.setter
    def severity(self, value: "SeverityEnum") -> None:
        """
        Set severity with validation.
        
        Args:
            value: The severity to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, SeverityEnum):
            raise TypeError(
                f"severity must be SeverityEnum, got {type(value).__name__}"
            )
        self._severity = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSeverity(self) -> "SeverityEnum":
        """
        AUTOSAR-compliant getter for severity.
        
        Returns:
            The severity value
        
        Note:
            Delegates to severity property (CODING_RULE_V2_00017)
        """
        return self.severity  # Delegates to property

    def setSeverity(self, value: "SeverityEnum") -> "RestrictionWithSeverity":
        """
        AUTOSAR-compliant setter for severity with method chaining.
        
        Args:
            value: The severity to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to severity property setter (gets validation automatically)
        """
        self.severity = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_severity(self, value: "SeverityEnum") -> "RestrictionWithSeverity":
        """
        Set severity and return self for chaining.
        
        Args:
            value: The severity to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_severity("value")
        """
        self.severity = value  # Use property setter (gets validation)
        return self