from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class FMFormulaByFeaturesAndAttributes(ARObject, ABC):
    """
    An expression that has the syntax of the AUTOSAR formula language but uses
    only references to features or feature attributes (not system constants) as
    operands.
    
    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFormulaByFeaturesAndAttributes
    
    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 61, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is FMFormulaByFeaturesAndAttributes:
            raise TypeError("FMFormulaByFeaturesAndAttributes is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # An expression of type FMFormulaByFeaturesAnd refer to attributes of
        # FMFeatures.
        self._attribute: Optional["FMAttributeDef"] = None

    @property
    def attribute(self) -> Optional["FMAttributeDef"]:
        """Get attribute (Pythonic accessor)."""
        return self._attribute

    @attribute.setter
    def attribute(self, value: Optional["FMAttributeDef"]) -> None:
        """
        Set attribute with validation.
        
        Args:
            value: The attribute to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._attribute = None
            return

        if not isinstance(value, FMAttributeDef):
            raise TypeError(
                f"attribute must be FMAttributeDef or None, got {type(value).__name__}"
            )
        self._attribute = value
        # An expression of type FMFormulaByFeaturesAnd refer to FMFeatures.
        self._feature: Optional["FMFeature"] = None

    @property
    def feature(self) -> Optional["FMFeature"]:
        """Get feature (Pythonic accessor)."""
        return self._feature

    @feature.setter
    def feature(self, value: Optional["FMFeature"]) -> None:
        """
        Set feature with validation.
        
        Args:
            value: The feature to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._feature = None
            return

        if not isinstance(value, FMFeature):
            raise TypeError(
                f"feature must be FMFeature or None, got {type(value).__name__}"
            )
        self._feature = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttribute(self) -> "FMAttributeDef":
        """
        AUTOSAR-compliant getter for attribute.
        
        Returns:
            The attribute value
        
        Note:
            Delegates to attribute property (CODING_RULE_V2_00017)
        """
        return self.attribute  # Delegates to property

    def setAttribute(self, value: "FMAttributeDef") -> "FMFormulaByFeaturesAndAttributes":
        """
        AUTOSAR-compliant setter for attribute with method chaining.
        
        Args:
            value: The attribute to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to attribute property setter (gets validation automatically)
        """
        self.attribute = value  # Delegates to property setter
        return self

    def getFeature(self) -> "FMFeature":
        """
        AUTOSAR-compliant getter for feature.
        
        Returns:
            The feature value
        
        Note:
            Delegates to feature property (CODING_RULE_V2_00017)
        """
        return self.feature  # Delegates to property

    def setFeature(self, value: "FMFeature") -> "FMFormulaByFeaturesAndAttributes":
        """
        AUTOSAR-compliant setter for feature with method chaining.
        
        Args:
            value: The feature to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to feature property setter (gets validation automatically)
        """
        self.feature = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_attribute(self, value: Optional["FMAttributeDef"]) -> "FMFormulaByFeaturesAndAttributes":
        """
        Set attribute and return self for chaining.
        
        Args:
            value: The attribute to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_attribute("value")
        """
        self.attribute = value  # Use property setter (gets validation)
        return self

    def with_feature(self, value: Optional["FMFeature"]) -> "FMFormulaByFeaturesAndAttributes":
        """
        Set feature and return self for chaining.
        
        Args:
            value: The feature to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_feature("value")
        """
        self.feature = value  # Use property setter (gets validation)
        return self