from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class VariationPointProxy(Identifiable):
    """
    that the technical details how to access the particular postBuildValueAccess
    are still considered internal to the RTE and are consequently not
    standardized. postBuildVariant PostBuildVariant * aggr This represents that
    applicable PostBuoldVariant Condition Condition Condition in the context of
    aVariationPointProxy. valueAccess AttributeValueVariation 0..1 aggr This
    value acts as Binding Function for the VariationPoint. Point Table 7.61:
    VariationPointProxy
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::VariantHandling::VariationPointProxy
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 613, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 479, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This condition acts as Binding Function for the Variation.
        self._conditionAccess: Optional["ConditionByFormula"] = None

    @property
    def condition_access(self) -> Optional["ConditionByFormula"]:
        """Get conditionAccess (Pythonic accessor)."""
        return self._conditionAccess

    @condition_access.setter
    def condition_access(self, value: Optional["ConditionByFormula"]) -> None:
        """
        Set conditionAccess with validation.
        
        Args:
            value: The conditionAccess to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._conditionAccess = None
            return

        if not isinstance(value, ConditionByFormula):
            raise TypeError(
                f"conditionAccess must be ConditionByFormula or None, got {type(value).__name__}"
            )
        self._conditionAccess = value
        # This association to ImplementationDataType shall be taken as an
        # implementation hint by the RTE generator.
        self._implementation: Optional["AbstractImplementation"] = None

    @property
    def implementation(self) -> Optional["AbstractImplementation"]:
        """Get implementation (Pythonic accessor)."""
        return self._implementation

    @implementation.setter
    def implementation(self, value: Optional["AbstractImplementation"]) -> None:
        """
        Set implementation with validation.
        
        Args:
            value: The implementation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implementation = None
            return

        if not isinstance(value, AbstractImplementation):
            raise TypeError(
                f"implementation must be AbstractImplementation or None, got {type(value).__name__}"
            )
        self._implementation = value
        # This represents the applicable PostBuildVariantCriterion in the context of a
        # VariationPointProxy.
        self._postBuildValue: Optional["PostBuildVariant"] = None

    @property
    def post_build_value(self) -> Optional["PostBuildVariant"]:
        """Get postBuildValue (Pythonic accessor)."""
        return self._postBuildValue

    @post_build_value.setter
    def post_build_value(self, value: Optional["PostBuildVariant"]) -> None:
        """
        Set postBuildValue with validation.
        
        Args:
            value: The postBuildValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._postBuildValue = None
            return

        if not isinstance(value, PostBuildVariant):
            raise TypeError(
                f"postBuildValue must be PostBuildVariant or None, got {type(value).__name__}"
            )
        self._postBuildValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConditionAccess(self) -> "ConditionByFormula":
        """
        AUTOSAR-compliant getter for conditionAccess.
        
        Returns:
            The conditionAccess value
        
        Note:
            Delegates to condition_access property (CODING_RULE_V2_00017)
        """
        return self.condition_access  # Delegates to property

    def setConditionAccess(self, value: "ConditionByFormula") -> "VariationPointProxy":
        """
        AUTOSAR-compliant setter for conditionAccess with method chaining.
        
        Args:
            value: The conditionAccess to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to condition_access property setter (gets validation automatically)
        """
        self.condition_access = value  # Delegates to property setter
        return self

    def getImplementation(self) -> "AbstractImplementation":
        """
        AUTOSAR-compliant getter for implementation.
        
        Returns:
            The implementation value
        
        Note:
            Delegates to implementation property (CODING_RULE_V2_00017)
        """
        return self.implementation  # Delegates to property

    def setImplementation(self, value: "AbstractImplementation") -> "VariationPointProxy":
        """
        AUTOSAR-compliant setter for implementation with method chaining.
        
        Args:
            value: The implementation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to implementation property setter (gets validation automatically)
        """
        self.implementation = value  # Delegates to property setter
        return self

    def getPostBuildValue(self) -> "PostBuildVariant":
        """
        AUTOSAR-compliant getter for postBuildValue.
        
        Returns:
            The postBuildValue value
        
        Note:
            Delegates to post_build_value property (CODING_RULE_V2_00017)
        """
        return self.post_build_value  # Delegates to property

    def setPostBuildValue(self, value: "PostBuildVariant") -> "VariationPointProxy":
        """
        AUTOSAR-compliant setter for postBuildValue with method chaining.
        
        Args:
            value: The postBuildValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to post_build_value property setter (gets validation automatically)
        """
        self.post_build_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_condition_access(self, value: Optional["ConditionByFormula"]) -> "VariationPointProxy":
        """
        Set conditionAccess and return self for chaining.
        
        Args:
            value: The conditionAccess to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_condition_access("value")
        """
        self.condition_access = value  # Use property setter (gets validation)
        return self

    def with_implementation(self, value: Optional["AbstractImplementation"]) -> "VariationPointProxy":
        """
        Set implementation and return self for chaining.
        
        Args:
            value: The implementation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_implementation("value")
        """
        self.implementation = value  # Use property setter (gets validation)
        return self

    def with_post_build_value(self, value: Optional["PostBuildVariant"]) -> "VariationPointProxy":
        """
        Set postBuildValue and return self for chaining.
        
        Args:
            value: The postBuildValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_post_build_value("value")
        """
        self.post_build_value = value  # Use property setter (gets validation)
        return self