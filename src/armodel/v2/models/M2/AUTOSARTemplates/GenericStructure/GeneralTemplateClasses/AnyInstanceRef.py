from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AnyInstanceRef(ARObject):
    """
    Describes a reference to any instance in an AUTOSAR model. This is the most
    generic form of an instance ref. Refer to the superclass notes for more
    details.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::AnyInstanceRef::AnyInstanceRef
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 289, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 970, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 1995, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 328, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the base from which navigation path begins.
        self._base: "AtpClassifier" = None

    @property
    def base(self) -> "AtpClassifier":
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: "AtpClassifier") -> None:
        """
        Set base with validation.
        
        Args:
            value: The base to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AtpClassifier):
            raise TypeError(
                f"base must be AtpClassifier, got {type(value).__name__}"
            )
        self._base = value
        # This is one step in the navigation path specified by the ref.
        self._contextElement: List["AtpFeature"] = []

    @property
    def context_element(self) -> List["AtpFeature"]:
        """Get contextElement (Pythonic accessor)."""
        return self._contextElement
        # This is the target of the instance ref.
        self._target: "AtpFeature" = None

    @property
    def target(self) -> "AtpFeature":
        """Get target (Pythonic accessor)."""
        return self._target

    @target.setter
    def target(self, value: "AtpFeature") -> None:
        """
        Set target with validation.
        
        Args:
            value: The target to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AtpFeature):
            raise TypeError(
                f"target must be AtpFeature, got {type(value).__name__}"
            )
        self._target = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "AtpClassifier":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "AtpClassifier") -> "AnyInstanceRef":
        """
        AUTOSAR-compliant setter for base with method chaining.
        
        Args:
            value: The base to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
        return self

    def getContextElement(self) -> List["AtpFeature"]:
        """
        AUTOSAR-compliant getter for contextElement.
        
        Returns:
            The contextElement value
        
        Note:
            Delegates to context_element property (CODING_RULE_V2_00017)
        """
        return self.context_element  # Delegates to property

    def getTarget(self) -> "AtpFeature":
        """
        AUTOSAR-compliant getter for target.
        
        Returns:
            The target value
        
        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    def setTarget(self, value: "AtpFeature") -> "AnyInstanceRef":
        """
        AUTOSAR-compliant setter for target with method chaining.
        
        Args:
            value: The target to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target property setter (gets validation automatically)
        """
        self.target = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: "AtpClassifier") -> "AnyInstanceRef":
        """
        Set base and return self for chaining.
        
        Args:
            value: The base to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_target(self, value: "AtpFeature") -> "AnyInstanceRef":
        """
        Set target and return self for chaining.
        
        Args:
            value: The target to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target("value")
        """
        self.target = value  # Use property setter (gets validation)
        return self