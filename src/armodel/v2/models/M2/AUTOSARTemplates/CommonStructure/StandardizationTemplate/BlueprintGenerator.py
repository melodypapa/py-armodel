"""
AUTOSAR Package - BlueprintGenerator

Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintGenerator
"""

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class BlueprintGenerator(ARObject):
    """
    This class express the Extended Language to generate blueprint derivates in
    complex descriptions.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintGenerator::BlueprintGenerator
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 424, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a formal term in the expression based on language.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._expression: Optional["VerbatimString"] = None

    @property
    def expression(self) -> Optional["VerbatimString"]:
        """Get expression (Pythonic accessor)."""
        return self._expression

    @expression.setter
    def expression(self, value: Optional["VerbatimString"]) -> None:
        """
        Set expression with validation.
        
        Args:
            value: The expression to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._expression = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"expression must be VerbatimString or None, got {type(value).__name__}"
            )
        self._expression = value
        # This represents a description that documents how the shall be resolved when
        # deriving blueprints.
        self._introduction: Optional["DocumentationBlock"] = None

    @property
    def introduction(self) -> Optional["DocumentationBlock"]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set introduction with validation.
        
        Args:
            value: The introduction to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._introduction = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._introduction = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getExpression(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for expression.
        
        Returns:
            The expression value
        
        Note:
            Delegates to expression property (CODING_RULE_V2_00017)
        """
        return self.expression  # Delegates to property

    def setExpression(self, value: "VerbatimString") -> "BlueprintGenerator":
        """
        AUTOSAR-compliant setter for expression with method chaining.
        
        Args:
            value: The expression to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to expression property setter (gets validation automatically)
        """
        self.expression = value  # Delegates to property setter
        return self

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.
        
        Returns:
            The introduction value
        
        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> "BlueprintGenerator":
        """
        AUTOSAR-compliant setter for introduction with method chaining.
        
        Args:
            value: The introduction to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_expression(self, value: Optional["VerbatimString"]) -> "BlueprintGenerator":
        """
        Set expression and return self for chaining.
        
        Args:
            value: The expression to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_expression("value")
        """
        self.expression = value  # Use property setter (gets validation)
        return self

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> "BlueprintGenerator":
        """
        Set introduction and return self for chaining.
        
        Args:
            value: The introduction to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self
