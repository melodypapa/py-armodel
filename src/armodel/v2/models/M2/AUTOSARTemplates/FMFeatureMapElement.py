from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class FMFeatureMapElement(Identifiable):
    """
    Defines value sets for system constants and postbuild variant criterions
    that shall be chosen whenever a certain combination of features (and system
    constants) is encountered.
    
    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureMapElement
    
    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 53, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines a boolean expression based on features and constants which needs to
        # evaluate to true for this become active.
        self._assertion: List["FMFeatureMap"] = []

    @property
    def assertion(self) -> List["FMFeatureMap"]:
        """Get assertion (Pythonic accessor)."""
        return self._assertion
        # Defines a condition which needs to be fulfilled for this to become active.
        self._condition: List["FMFeatureMap"] = []

    @property
    def condition(self) -> List["FMFeatureMap"]:
        """Get condition (Pythonic accessor)."""
        return self._condition
        # Selects a set of values for postbuild variant criterions.
        self._postBuildVariant: List["PostBuildVariant"] = []

    @property
    def post_build_variant(self) -> List["PostBuildVariant"]:
        """Get postBuildVariant (Pythonic accessor)."""
        return self._postBuildVariant
        # Selects a set of values for system constants.
        self._swValueSet: List["SwSystemconstant"] = []

    @property
    def sw_value_set(self) -> List["SwSystemconstant"]:
        """Get swValueSet (Pythonic accessor)."""
        return self._swValueSet

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssertion(self) -> List["FMFeatureMap"]:
        """
        AUTOSAR-compliant getter for assertion.
        
        Returns:
            The assertion value
        
        Note:
            Delegates to assertion property (CODING_RULE_V2_00017)
        """
        return self.assertion  # Delegates to property

    def getCondition(self) -> List["FMFeatureMap"]:
        """
        AUTOSAR-compliant getter for condition.
        
        Returns:
            The condition value
        
        Note:
            Delegates to condition property (CODING_RULE_V2_00017)
        """
        return self.condition  # Delegates to property

    def getPostBuildVariant(self) -> List["PostBuildVariant"]:
        """
        AUTOSAR-compliant getter for postBuildVariant.
        
        Returns:
            The postBuildVariant value
        
        Note:
            Delegates to post_build_variant property (CODING_RULE_V2_00017)
        """
        return self.post_build_variant  # Delegates to property

    def getSwValueSet(self) -> List["SwSystemconstant"]:
        """
        AUTOSAR-compliant getter for swValueSet.
        
        Returns:
            The swValueSet value
        
        Note:
            Delegates to sw_value_set property (CODING_RULE_V2_00017)
        """
        return self.sw_value_set  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====