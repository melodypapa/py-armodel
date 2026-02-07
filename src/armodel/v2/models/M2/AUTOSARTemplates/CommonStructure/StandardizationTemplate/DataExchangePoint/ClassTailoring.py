from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ClassTailoring(ARObject, ABC):
    """
    The ClassTailoring is an abstract class that allows the tailoring of its
    attributes, applicable constraints and Sdgs.
    
    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::ClassTailoring
    
    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 102, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is ClassTailoring:
            raise TypeError("ClassTailoring is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the accepted / not accepted content of the All rules apply that
        # fullfill the condition of the Class.
        self._classContent: List["ClassContent"] = []

    @property
    def class_content(self) -> List["ClassContent"]:
        """Get classContent (Pythonic accessor)."""
        return self._classContent
        # Specifies the multiplicity of the class in the current context.
        self._multiplicity: Optional["MultiplicityRestriction"] = None

    @property
    def multiplicity(self) -> Optional["MultiplicityRestriction"]:
        """Get multiplicity (Pythonic accessor)."""
        return self._multiplicity

    @multiplicity.setter
    def multiplicity(self, value: Optional["MultiplicityRestriction"]) -> None:
        """
        Set multiplicity with validation.
        
        Args:
            value: The multiplicity to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._multiplicity = None
            return

        if not isinstance(value, MultiplicityRestriction):
            raise TypeError(
                f"multiplicity must be MultiplicityRestriction or None, got {type(value).__name__}"
            )
        self._multiplicity = value
        # Specifies restrictions on the usage of variant handling.
        # Tags: xml.
        # sequenceOffset=20.
        self._variation: Optional["VariationRestrictionWith"] = None

    @property
    def variation(self) -> Optional["VariationRestrictionWith"]:
        """Get variation (Pythonic accessor)."""
        return self._variation

    @variation.setter
    def variation(self, value: Optional["VariationRestrictionWith"]) -> None:
        """
        Set variation with validation.
        
        Args:
            value: The variation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variation = None
            return

        if not isinstance(value, VariationRestrictionWith):
            raise TypeError(
                f"variation must be VariationRestrictionWith or None, got {type(value).__name__}"
            )
        self._variation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClassContent(self) -> List["ClassContent"]:
        """
        AUTOSAR-compliant getter for classContent.
        
        Returns:
            The classContent value
        
        Note:
            Delegates to class_content property (CODING_RULE_V2_00017)
        """
        return self.class_content  # Delegates to property

    def getMultiplicity(self) -> "MultiplicityRestriction":
        """
        AUTOSAR-compliant getter for multiplicity.
        
        Returns:
            The multiplicity value
        
        Note:
            Delegates to multiplicity property (CODING_RULE_V2_00017)
        """
        return self.multiplicity  # Delegates to property

    def setMultiplicity(self, value: "MultiplicityRestriction") -> "ClassTailoring":
        """
        AUTOSAR-compliant setter for multiplicity with method chaining.
        
        Args:
            value: The multiplicity to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to multiplicity property setter (gets validation automatically)
        """
        self.multiplicity = value  # Delegates to property setter
        return self

    def getVariation(self) -> "VariationRestrictionWith":
        """
        AUTOSAR-compliant getter for variation.
        
        Returns:
            The variation value
        
        Note:
            Delegates to variation property (CODING_RULE_V2_00017)
        """
        return self.variation  # Delegates to property

    def setVariation(self, value: "VariationRestrictionWith") -> "ClassTailoring":
        """
        AUTOSAR-compliant setter for variation with method chaining.
        
        Args:
            value: The variation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to variation property setter (gets validation automatically)
        """
        self.variation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_multiplicity(self, value: Optional["MultiplicityRestriction"]) -> "ClassTailoring":
        """
        Set multiplicity and return self for chaining.
        
        Args:
            value: The multiplicity to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_multiplicity("value")
        """
        self.multiplicity = value  # Use property setter (gets validation)
        return self

    def with_variation(self, value: Optional["VariationRestrictionWith"]) -> "ClassTailoring":
        """
        Set variation and return self for chaining.
        
        Args:
            value: The variation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_variation("value")
        """
        self.variation = value  # Use property setter (gets validation)
        return self