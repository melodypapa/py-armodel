from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class ConstraintTailoring(RestrictionWithSeverity):
    """
    Tailoring of constraints. If a constraint is in scope, then the severity
    defines its Error Severity Level. If it is not in scope, then the constraint
    is disabled.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::ConstraintTailoring
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 117, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to custom specification of constraint.
        self._constraint: Optional["TraceableText"] = None

    @property
    def constraint(self) -> Optional["TraceableText"]:
        """Get constraint (Pythonic accessor)."""
        return self._constraint

    @constraint.setter
    def constraint(self, value: Optional["TraceableText"]) -> None:
        """
        Set constraint with validation.
        
        Args:
            value: The constraint to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._constraint = None
            return

        if not isinstance(value, TraceableText):
            raise TypeError(
                f"constraint must be TraceableText or None, got {type(value).__name__}"
            )
        self._constraint = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConstraint(self) -> "TraceableText":
        """
        AUTOSAR-compliant getter for constraint.
        
        Returns:
            The constraint value
        
        Note:
            Delegates to constraint property (CODING_RULE_V2_00017)
        """
        return self.constraint  # Delegates to property

    def setConstraint(self, value: "TraceableText") -> "ConstraintTailoring":
        """
        AUTOSAR-compliant setter for constraint with method chaining.
        
        Args:
            value: The constraint to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to constraint property setter (gets validation automatically)
        """
        self.constraint = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_constraint(self, value: Optional["TraceableText"]) -> "ConstraintTailoring":
        """
        Set constraint and return self for chaining.
        
        Args:
            value: The constraint to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_constraint("value")
        """
        self.constraint = value  # Use property setter (gets validation)
        return self