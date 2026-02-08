"""
AUTOSAR Package - VariantHandling

Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    NameToken,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)




class PostBuildVariantCriterion(ARElement):
    """
    This class specifies one particular PostBuildVariantSelector.
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::PostBuildVariantCriterion
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 304, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 614, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 76, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 232, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The compuMethod specifies the possible values for the serving as an
        # enumerator.
        self._compuMethod: "CompuMethod" = None

    @property
    def compu_method(self) -> "CompuMethod":
        """Get compuMethod (Pythonic accessor)."""
        return self._compuMethod

    @compu_method.setter
    def compu_method(self, value: "CompuMethod") -> None:
        """
        Set compuMethod with validation.
        
        Args:
            value: The compuMethod to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, CompuMethod):
            raise TypeError(
                f"compuMethod must be CompuMethod, got {type(value).__name__}"
            )
        self._compuMethod = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuMethod(self) -> "CompuMethod":
        """
        AUTOSAR-compliant getter for compuMethod.
        
        Returns:
            The compuMethod value
        
        Note:
            Delegates to compu_method property (CODING_RULE_V2_00017)
        """
        return self.compu_method  # Delegates to property

    def setCompuMethod(self, value: "CompuMethod") -> "PostBuildVariantCriterion":
        """
        AUTOSAR-compliant setter for compuMethod with method chaining.
        
        Args:
            value: The compuMethod to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to compu_method property setter (gets validation automatically)
        """
        self.compu_method = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_method(self, value: "CompuMethod") -> "PostBuildVariantCriterion":
        """
        Set compuMethod and return self for chaining.
        
        Args:
            value: The compuMethod to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_compu_method("value")
        """
        self.compu_method = value  # Use property setter (gets validation)
        return self



class PostBuildVariantCriterionValue(ARObject):
    """
    This class specifies the value which shall be assigned to a particular
    variant criterion in order to bind the variation point. If multiple
    criterion/value pairs are specified, they all shall match to bind the
    variation point.
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::PostBuildVariantCriterionValue
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 305, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 77, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 258, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This provides the ability to add information why the value like it is.
        self._annotation: List["Annotation"] = []

    @property
    def annotation(self) -> List["Annotation"]:
        """Get annotation (Pythonic accessor)."""
        return self._annotation
        # This is the particular value of the post-build variant.
        self._value: "Integer" = None

    @property
    def value(self) -> "Integer":
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: "Integer") -> None:
        """
        Set value with validation.
        
        Args:
            value: The value to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"value must be Integer or int, got {type(value).__name__}"
            )
        self._value = value
        # This association selects the variant criterion whose value specified.
        self._variantCriterion: "PostBuildVariant" = None

    @property
    def variant_criterion(self) -> "PostBuildVariant":
        """Get variantCriterion (Pythonic accessor)."""
        return self._variantCriterion

    @variant_criterion.setter
    def variant_criterion(self, value: "PostBuildVariant") -> None:
        """
        Set variantCriterion with validation.
        
        Args:
            value: The variantCriterion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PostBuildVariant):
            raise TypeError(
                f"variantCriterion must be PostBuildVariant, got {type(value).__name__}"
            )
        self._variantCriterion = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAnnotation(self) -> List["Annotation"]:
        """
        AUTOSAR-compliant getter for annotation.
        
        Returns:
            The annotation value
        
        Note:
            Delegates to annotation property (CODING_RULE_V2_00017)
        """
        return self.annotation  # Delegates to property

    def getValue(self) -> "Integer":
        """
        AUTOSAR-compliant getter for value.
        
        Returns:
            The value value
        
        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "Integer") -> "PostBuildVariantCriterionValue":
        """
        AUTOSAR-compliant setter for value with method chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    def getVariantCriterion(self) -> "PostBuildVariant":
        """
        AUTOSAR-compliant getter for variantCriterion.
        
        Returns:
            The variantCriterion value
        
        Note:
            Delegates to variant_criterion property (CODING_RULE_V2_00017)
        """
        return self.variant_criterion  # Delegates to property

    def setVariantCriterion(self, value: "PostBuildVariant") -> "PostBuildVariantCriterionValue":
        """
        AUTOSAR-compliant setter for variantCriterion with method chaining.
        
        Args:
            value: The variantCriterion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to variant_criterion property setter (gets validation automatically)
        """
        self.variant_criterion = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: "Integer") -> "PostBuildVariantCriterionValue":
        """
        Set value and return self for chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

    def with_variant_criterion(self, value: "PostBuildVariant") -> "PostBuildVariantCriterionValue":
        """
        Set variantCriterion and return self for chaining.
        
        Args:
            value: The variantCriterion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_variant_criterion("value")
        """
        self.variant_criterion = value  # Use property setter (gets validation)
        return self



class PredefinedVariant(ARElement):
    """
    This specifies one predefined variant. It is characterized by the union of
    all system constant values and post-build variant criterion values
    aggregated within all referenced system constant value sets and post build
    variant criterion value sets plus the value sets of the included variants.
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::PredefinedVariant
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 305, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 77, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 257, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The associated variants are considered part of this means the settings of the
        # are included in the settings of the Nevertheless the included be included in
        # several predefined variants.
        self._includedVariant: List["PredefinedVariant"] = []

    @property
    def included_variant(self) -> List["PredefinedVariant"]:
        """Get includedVariant (Pythonic accessor)."""
        return self._includedVariant
        # This is the postBuildVariantCriterionValueSet contributing to the predefinded
        # variant.
        self._postBuildVariant: List["PostBuildVariant"] = []

    @property
    def post_build_variant(self) -> List["PostBuildVariant"]:
        """Get postBuildVariant (Pythonic accessor)."""
        return self._postBuildVariant
        # This ist the set of Systemconstant Values contributing to the predefined
        # variant.
        self._sw: List["SwSystemconstant"] = []

    @property
    def sw(self) -> List["SwSystemconstant"]:
        """Get sw (Pythonic accessor)."""
        return self._sw

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIncludedVariant(self) -> List["PredefinedVariant"]:
        """
        AUTOSAR-compliant getter for includedVariant.
        
        Returns:
            The includedVariant value
        
        Note:
            Delegates to included_variant property (CODING_RULE_V2_00017)
        """
        return self.included_variant  # Delegates to property

    def getPostBuildVariant(self) -> List["PostBuildVariant"]:
        """
        AUTOSAR-compliant getter for postBuildVariant.
        
        Returns:
            The postBuildVariant value
        
        Note:
            Delegates to post_build_variant property (CODING_RULE_V2_00017)
        """
        return self.post_build_variant  # Delegates to property

    def getSw(self) -> List["SwSystemconstant"]:
        """
        AUTOSAR-compliant getter for sw.
        
        Returns:
            The sw value
        
        Note:
            Delegates to sw property (CODING_RULE_V2_00017)
        """
        return self.sw  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SwSystemconstantValueSet(ARElement):
    """
    This meta-class represents the ability to specify a set of system constant
    values.
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::SwSystemconstantValueSet
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 313, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1007, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2069, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 246, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 56, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 258, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular value of a system constant.
        self._sw: List["SwSystemconstValue"] = []

    @property
    def sw(self) -> List["SwSystemconstValue"]:
        """Get sw (Pythonic accessor)."""
        return self._sw

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSw(self) -> List["SwSystemconstValue"]:
        """
        AUTOSAR-compliant getter for sw.
        
        Returns:
            The sw value
        
        Note:
            Delegates to sw property (CODING_RULE_V2_00017)
        """
        return self.sw  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class VariationPoint(ARObject):
    """
    that variationPoints are not allowed within a formal BlueprintGenerator.
    postBuildVariant PostBuildVariant * aggr This is the set of post build
    variant conditions which all Condition Condition shall be fulfilled in order
    to (postbuild) bind the variation point. sdg Sdg 0..1 aggr An optional
    special data group is attached to every variation point. These data can be
    used by external software systems to attach application specific data. For
    example, a variant management system might add an identifier, an URL or a
    specific classifier. shortLabel Identifier 0..1 attr This provides a name to
    the particular variation point to support the RTE generator. It is necessary
    for supporting splitable aggregations and if binding time is later than
    codeGenerationTime, as well as some RTE conditions. It needs to be unique
    with in the enclosing Identifiables with the same ShortName. Stereotypes:
    atpIdentityContributor (cid:53) 315 of 318 Document ID 87:
    AUTOSAR_CP_TPS_ECUConfiguration Specification of ECU Configuration AUTOSAR
    CP R23-11 (cid:52)
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::VariationPoint
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 315, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1010, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2078, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 80, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 226, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 39, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a description that documents how the point shall be resolved
        # when deriving objects blueprint.
        self._blueprint: Optional["DocumentationBlock"] = None

    @property
    def blueprint(self) -> Optional["DocumentationBlock"]:
        """Get blueprint (Pythonic accessor)."""
        return self._blueprint

    @blueprint.setter
    def blueprint(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set blueprint with validation.
        
        Args:
            value: The blueprint to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._blueprint = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"blueprint must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._blueprint = value
        # This condition acts as Binding Function for the Variation that the
                # multiplicity is 0.
        # 1 in order to support variants.
        self._swSyscond: Optional["ConditionByFormula"] = None

    @property
    def sw_syscond(self) -> Optional["ConditionByFormula"]:
        """Get swSyscond (Pythonic accessor)."""
        return self._swSyscond

    @sw_syscond.setter
    def sw_syscond(self, value: Optional["ConditionByFormula"]) -> None:
        """
        Set swSyscond with validation.
        
        Args:
            value: The swSyscond to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swSyscond = None
            return

        if not isinstance(value, ConditionByFormula):
            raise TypeError(
                f"swSyscond must be ConditionByFormula or None, got {type(value).__name__}"
            )
        self._swSyscond = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlueprint(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for blueprint.
        
        Returns:
            The blueprint value
        
        Note:
            Delegates to blueprint property (CODING_RULE_V2_00017)
        """
        return self.blueprint  # Delegates to property

    def setBlueprint(self, value: "DocumentationBlock") -> "VariationPoint":
        """
        AUTOSAR-compliant setter for blueprint with method chaining.
        
        Args:
            value: The blueprint to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to blueprint property setter (gets validation automatically)
        """
        self.blueprint = value  # Delegates to property setter
        return self

    def getSwSyscond(self) -> "ConditionByFormula":
        """
        AUTOSAR-compliant getter for swSyscond.
        
        Returns:
            The swSyscond value
        
        Note:
            Delegates to sw_syscond property (CODING_RULE_V2_00017)
        """
        return self.sw_syscond  # Delegates to property

    def setSwSyscond(self, value: "ConditionByFormula") -> "VariationPoint":
        """
        AUTOSAR-compliant setter for swSyscond with method chaining.
        
        Args:
            value: The swSyscond to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_syscond property setter (gets validation automatically)
        """
        self.sw_syscond = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_blueprint(self, value: Optional["DocumentationBlock"]) -> "VariationPoint":
        """
        Set blueprint and return self for chaining.
        
        Args:
            value: The blueprint to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_blueprint("value")
        """
        self.blueprint = value  # Use property setter (gets validation)
        return self

    def with_sw_syscond(self, value: Optional["ConditionByFormula"]) -> "VariationPoint":
        """
        Set swSyscond and return self for chaining.
        
        Args:
            value: The swSyscond to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_syscond("value")
        """
        self.sw_syscond = value  # Use property setter (gets validation)
        return self



class ConditionByFormula(ARObject):
    """
    This class represents a condition which is computed based on system
    constants according to the specified expression. The expected result is
    considered as boolean value. The result of the expression is interpreted as
    a condition. • "0" represents "false"; • a value other than zero is
    considered "true"
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::ConditionByFormula
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 613, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2012, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 73, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 231, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the point in time when condition evaluated at
                # earliest.
        # At this point in time all constants shall have a value.
        self._bindingTime: "BindingTimeEnum" = None

    @property
    def binding_time(self) -> "BindingTimeEnum":
        """Get bindingTime (Pythonic accessor)."""
        return self._bindingTime

    @binding_time.setter
    def binding_time(self, value: "BindingTimeEnum") -> None:
        """
        Set bindingTime with validation.
        
        Args:
            value: The bindingTime to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, BindingTimeEnum):
            raise TypeError(
                f"bindingTime must be BindingTimeEnum, got {type(value).__name__}"
            )
        self._bindingTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBindingTime(self) -> "BindingTimeEnum":
        """
        AUTOSAR-compliant getter for bindingTime.
        
        Returns:
            The bindingTime value
        
        Note:
            Delegates to binding_time property (CODING_RULE_V2_00017)
        """
        return self.binding_time  # Delegates to property

    def setBindingTime(self, value: "BindingTimeEnum") -> "ConditionByFormula":
        """
        AUTOSAR-compliant setter for bindingTime with method chaining.
        
        Args:
            value: The bindingTime to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to binding_time property setter (gets validation automatically)
        """
        self.binding_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_binding_time(self, value: "BindingTimeEnum") -> "ConditionByFormula":
        """
        Set bindingTime and return self for chaining.
        
        Args:
            value: The bindingTime to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_binding_time("value")
        """
        self.binding_time = value  # Use property setter (gets validation)
        return self



class PostBuildVariantCondition(ARObject):
    """
    This class specifies the value which shall be assigned to a particular
    variant criterion in order to bind the variation point. If multiple
    criterion/value pairs are specified, they shall all match to bind the
    variation point. In other words binding can be represented by (criterion1 ==
    value1) && (condition2 == value2) ...
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::PostBuildVariantCondition
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 614, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 76, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 232, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the criterion which needs to match the value in order to make the
        # PostbuildVariantCondition to be true.
        self._matching: "PostBuildVariant" = None

    @property
    def matching(self) -> "PostBuildVariant":
        """Get matching (Pythonic accessor)."""
        return self._matching

    @matching.setter
    def matching(self, value: "PostBuildVariant") -> None:
        """
        Set matching with validation.
        
        Args:
            value: The matching to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PostBuildVariant):
            raise TypeError(
                f"matching must be PostBuildVariant, got {type(value).__name__}"
            )
        self._matching = value
        # This is the particular value of the post-build variant.
        self._value: "Integer" = None

    @property
    def value(self) -> "Integer":
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: "Integer") -> None:
        """
        Set value with validation.
        
        Args:
            value: The value to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"value must be Integer or int, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMatching(self) -> "PostBuildVariant":
        """
        AUTOSAR-compliant getter for matching.
        
        Returns:
            The matching value
        
        Note:
            Delegates to matching property (CODING_RULE_V2_00017)
        """
        return self.matching  # Delegates to property

    def setMatching(self, value: "PostBuildVariant") -> "PostBuildVariantCondition":
        """
        AUTOSAR-compliant setter for matching with method chaining.
        
        Args:
            value: The matching to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to matching property setter (gets validation automatically)
        """
        self.matching = value  # Delegates to property setter
        return self

    def getValue(self) -> "Integer":
        """
        AUTOSAR-compliant getter for value.
        
        Returns:
            The value value
        
        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "Integer") -> "PostBuildVariantCondition":
        """
        AUTOSAR-compliant setter for value with method chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_matching(self, value: "PostBuildVariant") -> "PostBuildVariantCondition":
        """
        Set matching and return self for chaining.
        
        Args:
            value: The matching to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_matching("value")
        """
        self.matching = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: "Integer") -> "PostBuildVariantCondition":
        """
        Set value and return self for chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self



class PostBuildVariantCriterionValueSet(ARElement):
    """
    This meta-class represents the ability to denote one set of
    postBuildVariantCriterionValues.
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::PostBuildVariantCriterionValueSet
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1000, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 56, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 258, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is is one particular postbuild variant criterion/value pair being part
        # of the PostBuildVariantSet.
        self._postBuildVariant: List["PostBuildVariant"] = []

    @property
    def post_build_variant(self) -> List["PostBuildVariant"]:
        """Get postBuildVariant (Pythonic accessor)."""
        return self._postBuildVariant

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPostBuildVariant(self) -> List["PostBuildVariant"]:
        """
        AUTOSAR-compliant getter for postBuildVariant.
        
        Returns:
            The postBuildVariant value
        
        Note:
            Delegates to post_build_variant property (CODING_RULE_V2_00017)
        """
        return self.post_build_variant  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SwSystemconstDependentFormula(ARObject, ABC):
    """
    This class represents an expression depending on system constants.
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::SwSystemconstDependentFormula
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1006, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 79, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 240, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is SwSystemconstDependentFormula:
            raise TypeError("SwSystemconstDependentFormula is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This refers to a system constant.
        # The internal (coded) the system constant shall be used.
        self._sysc: Optional["SwSystemconst"] = None

    @property
    def sysc(self) -> Optional["SwSystemconst"]:
        """Get sysc (Pythonic accessor)."""
        return self._sysc

    @sysc.setter
    def sysc(self, value: Optional["SwSystemconst"]) -> None:
        """
        Set sysc with validation.
        
        Args:
            value: The sysc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sysc = None
            return

        if not isinstance(value, SwSystemconst):
            raise TypeError(
                f"sysc must be SwSystemconst or None, got {type(value).__name__}"
            )
        self._sysc = value
        # syscString indicates that the referenced system constant evaluated as a
        # string according to.
        self._syscString: Optional["SwSystemconst"] = None

    @property
    def sysc_string(self) -> Optional["SwSystemconst"]:
        """Get syscString (Pythonic accessor)."""
        return self._syscString

    @sysc_string.setter
    def sysc_string(self, value: Optional["SwSystemconst"]) -> None:
        """
        Set syscString with validation.
        
        Args:
            value: The syscString to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syscString = None
            return

        if not isinstance(value, SwSystemconst):
            raise TypeError(
                f"syscString must be SwSystemconst or None, got {type(value).__name__}"
            )
        self._syscString = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSysc(self) -> "SwSystemconst":
        """
        AUTOSAR-compliant getter for sysc.
        
        Returns:
            The sysc value
        
        Note:
            Delegates to sysc property (CODING_RULE_V2_00017)
        """
        return self.sysc  # Delegates to property

    def setSysc(self, value: "SwSystemconst") -> "SwSystemconstDependentFormula":
        """
        AUTOSAR-compliant setter for sysc with method chaining.
        
        Args:
            value: The sysc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sysc property setter (gets validation automatically)
        """
        self.sysc = value  # Delegates to property setter
        return self

    def getSyscString(self) -> "SwSystemconst":
        """
        AUTOSAR-compliant getter for syscString.
        
        Returns:
            The syscString value
        
        Note:
            Delegates to sysc_string property (CODING_RULE_V2_00017)
        """
        return self.sysc_string  # Delegates to property

    def setSyscString(self, value: "SwSystemconst") -> "SwSystemconstDependentFormula":
        """
        AUTOSAR-compliant setter for syscString with method chaining.
        
        Args:
            value: The syscString to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sysc_string property setter (gets validation automatically)
        """
        self.sysc_string = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sysc(self, value: Optional["SwSystemconst"]) -> "SwSystemconstDependentFormula":
        """
        Set sysc and return self for chaining.
        
        Args:
            value: The sysc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sysc("value")
        """
        self.sysc = value  # Use property setter (gets validation)
        return self

    def with_sysc_string(self, value: Optional["SwSystemconst"]) -> "SwSystemconstDependentFormula":
        """
        Set syscString and return self for chaining.
        
        Args:
            value: The syscString to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sysc_string("value")
        """
        self.sysc_string = value  # Use property setter (gets validation)
        return self



class SwSystemconstValue(ARObject):
    """
    This meta-class assigns a particular value to a system constant.
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::SwSystemconstValue
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2068, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 80, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 235, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This provides the ability to add information why the value like it is.
        self._annotation: List["Annotation"] = []

    @property
    def annotation(self) -> List["Annotation"]:
        """Get annotation (Pythonic accessor)."""
        return self._annotation
        # This is the system constant to which the value applies.
        self._swSystemconst: "SwSystemconst" = None

    @property
    def sw_systemconst(self) -> "SwSystemconst":
        """Get swSystemconst (Pythonic accessor)."""
        return self._swSystemconst

    @sw_systemconst.setter
    def sw_systemconst(self, value: "SwSystemconst") -> None:
        """
        Set swSystemconst with validation.
        
        Args:
            value: The swSystemconst to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, SwSystemconst):
            raise TypeError(
                f"swSystemconst must be SwSystemconst, got {type(value).__name__}"
            )
        self._swSystemconst = value
        # This is the particular value of a system constant.
        # It is Numerical.
        # Further restrictions may apply by of the system constant.
        # attribute defines the internal value of the Sw it is processed in the Formula
                # Language.
        self._value: "Numerical" = None

    @property
    def value(self) -> "Numerical":
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: "Numerical") -> None:
        """
        Set value with validation.
        
        Args:
            value: The value to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Numerical):
            raise TypeError(
                f"value must be Numerical, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAnnotation(self) -> List["Annotation"]:
        """
        AUTOSAR-compliant getter for annotation.
        
        Returns:
            The annotation value
        
        Note:
            Delegates to annotation property (CODING_RULE_V2_00017)
        """
        return self.annotation  # Delegates to property

    def getSwSystemconst(self) -> "SwSystemconst":
        """
        AUTOSAR-compliant getter for swSystemconst.
        
        Returns:
            The swSystemconst value
        
        Note:
            Delegates to sw_systemconst property (CODING_RULE_V2_00017)
        """
        return self.sw_systemconst  # Delegates to property

    def setSwSystemconst(self, value: "SwSystemconst") -> "SwSystemconstValue":
        """
        AUTOSAR-compliant setter for swSystemconst with method chaining.
        
        Args:
            value: The swSystemconst to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_systemconst property setter (gets validation automatically)
        """
        self.sw_systemconst = value  # Delegates to property setter
        return self

    def getValue(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for value.
        
        Returns:
            The value value
        
        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "Numerical") -> "SwSystemconstValue":
        """
        AUTOSAR-compliant setter for value with method chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_systemconst(self, value: "SwSystemconst") -> "SwSystemconstValue":
        """
        Set swSystemconst and return self for chaining.
        
        Args:
            value: The swSystemconst to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_systemconst("value")
        """
        self.sw_systemconst = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: "Numerical") -> "SwSystemconstValue":
        """
        Set value and return self for chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self



class EvaluatedVariantSet(ARElement):
    """
    that the EvaluatedVariantSet is a CollectableElement. This allows to
    establish a hierarchy of EvaluatedVariantSets.
    
    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::EvaluatedVariantSet
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 257, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the approval status of a predefined variant.
        # Two predefined: "APPROVED" and "REJECTED": variants are known to work.
        # variants are known NOT to work.
        # can be approved on a per-company basis; only "APPROVED" and "REJECTED"
                # recognized.
        self._approvalStatus: "NameToken" = None

    @property
    def approval_status(self) -> "NameToken":
        """Get approvalStatus (Pythonic accessor)."""
        return self._approvalStatus

    @approval_status.setter
    def approval_status(self, value: "NameToken") -> None:
        """
        Set approvalStatus with validation.
        
        Args:
            value: The approvalStatus to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"approvalStatus must be NameToken or str, got {type(value).__name__}"
            )
        self._approvalStatus = value
        # This metaclass represents one particular variant which evaluated.
        # LowerMultiplicity is set to 0 to support a.
        self._evaluated: List["PredefinedVariant"] = []

    @property
    def evaluated(self) -> List["PredefinedVariant"]:
        """Get evaluated (Pythonic accessor)."""
        return self._evaluated

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApprovalStatus(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for approvalStatus.
        
        Returns:
            The approvalStatus value
        
        Note:
            Delegates to approval_status property (CODING_RULE_V2_00017)
        """
        return self.approval_status  # Delegates to property

    def setApprovalStatus(self, value: "NameToken") -> "EvaluatedVariantSet":
        """
        AUTOSAR-compliant setter for approvalStatus with method chaining.
        
        Args:
            value: The approvalStatus to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to approval_status property setter (gets validation automatically)
        """
        self.approval_status = value  # Delegates to property setter
        return self

    def getEvaluated(self) -> List["PredefinedVariant"]:
        """
        AUTOSAR-compliant getter for evaluated.
        
        Returns:
            The evaluated value
        
        Note:
            Delegates to evaluated property (CODING_RULE_V2_00017)
        """
        return self.evaluated  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_approval_status(self, value: "NameToken") -> "EvaluatedVariantSet":
        """
        Set approvalStatus and return self for chaining.
        
        Args:
            value: The approvalStatus to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_approval_status("value")
        """
        self.approval_status = value  # Use property setter (gets validation)
        return self


class AdditionalBindingTimeEnum(AREnum):
    """
    AdditionalBindingTimeEnum enumeration

This enumeration specifies the additional binding times applicable for vh.latestBindingTime of variation points.

Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    """
    # The point in time when an object is created from a blueprint.
    blueprintDerivationTime = "0"

    # After the executable has been built.
    postBuild = "1"



class BindingTimeEnum(AREnum):
    """
    BindingTimeEnum enumeration

This enumerator specifies the applicable binding times for the pre build variation points. Aggregated by AttributeValueVariationPoint.bindingTime, ConditionByFormula.bindingTime, FMFeature.maximum IntendedBindingTime, FMFeature.minimumIntendedBindingTime, FMFeatureSelection.maximum SelectedBindingTime, FMFeatureSelection.minimumSelectedBindingTime

Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling
    """
    # • Coding by hand, based on requirements document.
    codeGenerationTime = "0"

    # Configure what is included in object code, and what is omitted Based on which variant(s) are selected
    linkTime = "1"

    # This is typically the C-Preprocessor. Exclude parts of the code from the compilation process, e.g., because they are not required for the selected variant, because they are incompatible with the selected variant, because they require resources that are not present in the selected variant. Object code is only generated for the selected variant(s). The code that is excluded at this stage code will not be available at later stages.
    preCompileTime = "2"

    # • Designing the VFB.
    systemDesignTime = "3"
