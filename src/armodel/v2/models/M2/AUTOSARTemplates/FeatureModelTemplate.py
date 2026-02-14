"""
AUTOSAR Package - FeatureModelTemplate

Package: M2::AUTOSARTemplates::FeatureModelTemplate
"""


from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    SwSystemconstant,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    CategoryString,
    Limit,
    Numerical,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    BindingTimeEnum,
    PostBuildVariant,
)


class FMFeatureModel(ARElement):
    """
    A Feature model describes the features of a product line and their
    dependencies. Feature models are an optional part of an AUTOSAR model.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureModel

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 21, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 444, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # "feature" holds the list of features of the feature model.
        # No be contained twice in this list.
        # Also, each be contained on only one feature model.
        self._feature: List[FMFeature] = []

    @property
    def feature(self) -> List[FMFeature]:
        """Get feature (Pythonic accessor)."""
        return self._feature
        # The features of a feature model define a tree.
        # The points to the root of this tree.
        self._root: Optional[FMFeature] = None

    @property
    def root(self) -> Optional[FMFeature]:
        """Get root (Pythonic accessor)."""
        return self._root

    @root.setter
    def root(self, value: Optional[FMFeature]) -> None:
        """
        Set root with validation.

        Args:
            value: The root to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._root = None
            return

        if not isinstance(value, FMFeature):
            raise TypeError(
                f"root must be FMFeature or None, got {type(value).__name__}"
            )
        self._root = value

    def with_attribute_def(self, value):
        """
        Set attribute_def and return self for chaining.

        Args:
            value: The attribute_def to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_attribute_def("value")
        """
        self.attribute_def = value  # Use property setter (gets validation)
        return self

    def with_decomposition_decomposition(self, value):
        """
        Set decomposition_decomposition and return self for chaining.

        Args:
            value: The decomposition_decomposition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_decomposition_decomposition("value")
        """
        self.decomposition_decomposition = value  # Use property setter (gets validation)
        return self

    def with_relation(self, value):
        """
        Set relation and return self for chaining.

        Args:
            value: The relation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_relation("value")
        """
        self.relation = value  # Use property setter (gets validation)
        return self

    def with_attribute_value(self, value):
        """
        Set attribute_value and return self for chaining.

        Args:
            value: The attribute_value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_attribute_value("value")
        """
        self.attribute_value = value  # Use property setter (gets validation)
        return self

    def with_feature_model(self, value):
        """
        Set feature_model and return self for chaining.

        Args:
            value: The feature_model to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_feature_model("value")
        """
        self.feature_model = value  # Use property setter (gets validation)
        return self

    def with_include(self, value):
        """
        Set include and return self for chaining.

        Args:
            value: The include to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_include("value")
        """
        self.include = value  # Use property setter (gets validation)
        return self

    def with_selection(self, value):
        """
        Set selection and return self for chaining.

        Args:
            value: The selection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_selection("value")
        """
        self.selection = value  # Use property setter (gets validation)
        return self

    def with_mapping(self, value):
        """
        Set mapping and return self for chaining.

        Args:
            value: The mapping to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mapping("value")
        """
        self.mapping = value  # Use property setter (gets validation)
        return self

    def with_assertion(self, value):
        """
        Set assertion and return self for chaining.

        Args:
            value: The assertion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assertion("value")
        """
        self.assertion = value  # Use property setter (gets validation)
        return self

    def with_condition(self, value):
        """
        Set condition and return self for chaining.

        Args:
            value: The condition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_condition("value")
        """
        self.condition = value  # Use property setter (gets validation)
        return self

    def with_post_build_variant(self, value):
        """
        Set post_build_variant and return self for chaining.

        Args:
            value: The post_build_variant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_post_build_variant("value")
        """
        self.post_build_variant = value  # Use property setter (gets validation)
        return self

    def with_sw_value_set(self, value):
        """
        Set sw_value_set and return self for chaining.

        Args:
            value: The sw_value_set to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_value_set("value")
        """
        self.sw_value_set = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFeature(self) -> List[FMFeature]:
        """
        AUTOSAR-compliant getter for feature.

        Returns:
            The feature value

        Note:
            Delegates to feature property (CODING_RULE_V2_00017)
        """
        return self.feature  # Delegates to property

    def getRoot(self) -> FMFeature:
        """
        AUTOSAR-compliant getter for root.

        Returns:
            The root value

        Note:
            Delegates to root property (CODING_RULE_V2_00017)
        """
        return self.root  # Delegates to property

    def setRoot(self, value: FMFeature) -> FMFeatureModel:
        """
        AUTOSAR-compliant setter for root with method chaining.

        Args:
            value: The root to set

        Returns:
            self for method chaining

        Note:
            Delegates to root property setter (gets validation automatically)
        """
        self.root = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_root(self, value: Optional[FMFeature]) -> FMFeatureModel:
        """
        Set root and return self for chaining.

        Args:
            value: The root to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_root("value")
        """
        self.root = value  # Use property setter (gets validation)
        return self



class FMFeature(ARElement):
    """
    A FMFeature describes an essential characteristic of a product. Each
    FMFeature is contained in exactly one FMFeatureModel.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeature

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 24, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 444, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines the attributes of the given feature.
        self._attributeDef: List[FMAttributeDef] = []

    @property
    def attribute_def(self) -> List[FMAttributeDef]:
        """Get attributeDef (Pythonic accessor)."""
        return self._attributeDef
        # Lists the sub-features of a feature.
        self._decompositionDecomposition: List[FMFeature] = []

    @property
    def decomposition_decomposition(self) -> List[FMFeature]:
        """Get decompositionDecomposition (Pythonic accessor)."""
        return self._decompositionDecomposition
        # Defines an upper bound for the binding time of the points that are associated
                # with the FMFeature.
        # attribute is meant as a hint for the development.
        self._maximum: Optional[BindingTimeEnum] = None

    @property
    def maximum(self) -> Optional[BindingTimeEnum]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional[BindingTimeEnum]) -> None:
        """
        Set maximum with validation.

        Args:
            value: The maximum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, BindingTimeEnum):
            raise TypeError(
                f"maximum must be BindingTimeEnum or None, got {type(value).__name__}"
            )
        self._maximum = value
                # associated with the FMFeature.
        # This is meant as a hint for the development process.
        self._minimum: Optional[BindingTimeEnum] = None

    @property
    def minimum(self) -> Optional[BindingTimeEnum]:
        """Get minimum (Pythonic accessor)."""
        return self._minimum

    @minimum.setter
    def minimum(self, value: Optional[BindingTimeEnum]) -> None:
        """
        Set minimum with validation.

        Args:
            value: The minimum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimum = None
            return

        if not isinstance(value, BindingTimeEnum):
            raise TypeError(
                f"minimum must be BindingTimeEnum or None, got {type(value).__name__}"
            )
        self._minimum = value
        # with A FMFeature can only be part of a all its relations are fulfilled.
        self._relation: List[FMFeatureRelation] = []

    @property
    def relation(self) -> List[FMFeatureRelation]:
        """Get relation (Pythonic accessor)."""
        return self._relation
        # Defines restrictions for FMFeatures.
        # A FMFeature can part of a FMFeatureSelectionSet if at least one of evaluates
                # to true.
        self._restriction: List[FMFeatureRestriction] = []

    @property
    def restriction(self) -> List[FMFeatureRestriction]:
        """Get restriction (Pythonic accessor)."""
        return self._restriction

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttributeDef(self) -> List[FMAttributeDef]:
        """
        AUTOSAR-compliant getter for attributeDef.

        Returns:
            The attributeDef value

        Note:
            Delegates to attribute_def property (CODING_RULE_V2_00017)
        """
        return self.attribute_def  # Delegates to property

    def getDecompositionDecomposition(self) -> List[FMFeature]:
        """
        AUTOSAR-compliant getter for decompositionDecomposition.

        Returns:
            The decompositionDecomposition value

        Note:
            Delegates to decomposition_decomposition property (CODING_RULE_V2_00017)
        """
        return self.decomposition_decomposition  # Delegates to property

    def getMaximum(self) -> BindingTimeEnum:
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: BindingTimeEnum) -> FMFeature:
        """
        AUTOSAR-compliant setter for maximum with method chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    def getMinimum(self) -> BindingTimeEnum:
        """
        AUTOSAR-compliant getter for minimum.

        Returns:
            The minimum value

        Note:
            Delegates to minimum property (CODING_RULE_V2_00017)
        """
        return self.minimum  # Delegates to property

    def setMinimum(self, value: BindingTimeEnum) -> FMFeature:
        """
        AUTOSAR-compliant setter for minimum with method chaining.

        Args:
            value: The minimum to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum property setter (gets validation automatically)
        """
        self.minimum = value  # Delegates to property setter
        return self

    def getRelation(self) -> List[FMFeatureRelation]:
        """
        AUTOSAR-compliant getter for relation.

        Returns:
            The relation value

        Note:
            Delegates to relation property (CODING_RULE_V2_00017)
        """
        return self.relation  # Delegates to property

    def getRestriction(self) -> List[FMFeatureRestriction]:
        """
        AUTOSAR-compliant getter for restriction.

        Returns:
            The restriction value

        Note:
            Delegates to restriction property (CODING_RULE_V2_00017)
        """
        return self.restriction  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_maximum(self, value: Optional[BindingTimeEnum]) -> FMFeature:
        """
        Set maximum and return self for chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self

    def with_minimum(self, value: Optional[BindingTimeEnum]) -> FMFeature:
        """
        Set minimum and return self for chaining.

        Args:
            value: The minimum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum("value")
        """
        self.minimum = value  # Use property setter (gets validation)
        return self



class FMAttributeDef(Identifiable):
    """
    This metaclass represents the ability to define attributes for a feature.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMAttributeDef

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 26, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the default value of the attribute.
        self._defaultValue: Optional[Numerical] = None

    @property
    def default_value(self) -> Optional[Numerical]:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: Optional[Numerical]) -> None:
        """
        Set defaultValue with validation.

        Args:
            value: The defaultValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultValue = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"defaultValue must be Numerical or None, got {type(value).__name__}"
            )
        self._defaultValue = value
        self._max: Optional[Limit] = None

    @property
    def max(self) -> Optional[Limit]:
        """Get max (Pythonic accessor)."""
        return self._max

    @max.setter
    def max(self, value: Optional[Limit]) -> None:
        """
        Set max with validation.

        Args:
            value: The max to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._max = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"max must be Limit or None, got {type(value).__name__}"
            )
        self._max = value
        self._min: Optional[Limit] = None

    @property
    def min(self) -> Optional[Limit]:
        """Get min (Pythonic accessor)."""
        return self._min

    @min.setter
    def min(self, value: Optional[Limit]) -> None:
        """
        Set min with validation.

        Args:
            value: The min to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._min = None
            return

        if not isinstance(value, Limit):
            raise TypeError(
                f"min must be Limit or None, got {type(value).__name__}"
            )
        self._min = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> Numerical:
        """
        AUTOSAR-compliant getter for defaultValue.

        Returns:
            The defaultValue value

        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: Numerical) -> FMAttributeDef:
        """
        AUTOSAR-compliant setter for defaultValue with method chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to default_value property setter (gets validation automatically)
        """
        self.default_value = value  # Delegates to property setter
        return self

    def getMax(self) -> Limit:
        """
        AUTOSAR-compliant getter for max.

        Returns:
            The max value

        Note:
            Delegates to max property (CODING_RULE_V2_00017)
        """
        return self.max  # Delegates to property

    def setMax(self, value: Limit) -> FMAttributeDef:
        """
        AUTOSAR-compliant setter for max with method chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Note:
            Delegates to max property setter (gets validation automatically)
        """
        self.max = value  # Delegates to property setter
        return self

    def getMin(self) -> Limit:
        """
        AUTOSAR-compliant getter for min.

        Returns:
            The min value

        Note:
            Delegates to min property (CODING_RULE_V2_00017)
        """
        return self.min  # Delegates to property

    def setMin(self, value: Limit) -> FMAttributeDef:
        """
        AUTOSAR-compliant setter for min with method chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Note:
            Delegates to min property setter (gets validation automatically)
        """
        self.min = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional[Numerical]) -> FMAttributeDef:
        """
        Set defaultValue and return self for chaining.

        Args:
            value: The defaultValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_default_value("value")
        """
        self.default_value = value  # Use property setter (gets validation)
        return self

    def with_max(self, value: Optional[Limit]) -> FMAttributeDef:
        """
        Set max and return self for chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max("value")
        """
        self.max = value  # Use property setter (gets validation)
        return self

    def with_min(self, value: Optional[Limit]) -> FMAttributeDef:
        """
        Set min and return self for chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min("value")
        """
        self.min = value  # Use property setter (gets validation)
        return self



class FMFeatureDecomposition(ARObject):
    """
    A FMFeatureDecomposition describes dependencies between a list of features
    and their parent feature (i.e., the FMFeature that aggregates the
    FMFeatureDecomposition). The kind of dependency is defined by the attribute
    category.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureDecomposition

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 27, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The category of a FMFeatureDecomposition defines the dependency that is
        # defined by the FMFeature are four different categories: MULTIPLEFEATURE.
        self._category: Optional[CategoryString] = None

    @property
    def category(self) -> Optional[CategoryString]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional[CategoryString]) -> None:
        """
        Set category with validation.

        Args:
            value: The category to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, CategoryString):
            raise TypeError(
                f"category must be CategoryString or None, got {type(value).__name__}"
            )
        self._category = value
                # FMFeatureDecomposition.
        # 92 Document ID 606: AUTOSAR_FO_TPS_FeatureModelExchangeFormat Model Exchange
                # Format R23-11.
        self._feature: List[FMFeature] = []

    @property
    def feature(self) -> List[FMFeature]:
        """Get feature (Pythonic accessor)."""
        return self._feature
        # For a dependency of category MULTIPLEFEATURE, this maximum number of features
        # allowed.
        self._max: Optional[PositiveInteger] = None

    @property
    def max(self) -> Optional[PositiveInteger]:
        """Get max (Pythonic accessor)."""
        return self._max

    @max.setter
    def max(self, value: Optional[PositiveInteger]) -> None:
        """
        Set max with validation.

        Args:
            value: The max to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._max = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"max must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._max = value
        # allowed.
        self._min: Optional[PositiveInteger] = None

    @property
    def min(self) -> Optional[PositiveInteger]:
        """Get min (Pythonic accessor)."""
        return self._min

    @min.setter
    def min(self, value: Optional[PositiveInteger]) -> None:
        """
        Set min with validation.

        Args:
            value: The min to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._min = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"min must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._min = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCategory(self) -> CategoryString:
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: CategoryString) -> FMFeatureDecomposition:
        """
        AUTOSAR-compliant setter for category with method chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getFeature(self) -> List[FMFeature]:
        """
        AUTOSAR-compliant getter for feature.

        Returns:
            The feature value

        Note:
            Delegates to feature property (CODING_RULE_V2_00017)
        """
        return self.feature  # Delegates to property

    def getMax(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for max.

        Returns:
            The max value

        Note:
            Delegates to max property (CODING_RULE_V2_00017)
        """
        return self.max  # Delegates to property

    def setMax(self, value: PositiveInteger) -> FMFeatureDecomposition:
        """
        AUTOSAR-compliant setter for max with method chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Note:
            Delegates to max property setter (gets validation automatically)
        """
        self.max = value  # Delegates to property setter
        return self

    def getMin(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for min.

        Returns:
            The min value

        Note:
            Delegates to min property (CODING_RULE_V2_00017)
        """
        return self.min  # Delegates to property

    def setMin(self, value: PositiveInteger) -> FMFeatureDecomposition:
        """
        AUTOSAR-compliant setter for min with method chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Note:
            Delegates to min property setter (gets validation automatically)
        """
        self.min = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_category(self, value: Optional[CategoryString]) -> FMFeatureDecomposition:
        """
        Set category and return self for chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_max(self, value: Optional[PositiveInteger]) -> FMFeatureDecomposition:
        """
        Set max and return self for chaining.

        Args:
            value: The max to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max("value")
        """
        self.max = value  # Use property setter (gets validation)
        return self

    def with_min(self, value: Optional[PositiveInteger]) -> FMFeatureDecomposition:
        """
        Set min and return self for chaining.

        Args:
            value: The min to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min("value")
        """
        self.min = value  # Use property setter (gets validation)
        return self



class FMFeatureRestriction(Identifiable):
    """
    Defines restrictions for FMFeatures. A FMFeature can only be part of a
    FMFeatureSelectionSet if at least one of its restrictions evaluate to true.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureRestriction

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 32, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A formula that contains the actual restriction.
        self._restrictionAndAttributes: Optional[FMConditionByFeaturesAndAttributes] = None

    @property
    def restriction_and_attributes(self) -> Optional[FMConditionByFeaturesAndAttributes]:
        """Get restrictionAndAttributes (Pythonic accessor)."""
        return self._restrictionAndAttributes

    @restriction_and_attributes.setter
    def restriction_and_attributes(self, value: Optional[FMConditionByFeaturesAndAttributes]) -> None:
        """
        Set restrictionAndAttributes with validation.

        Args:
            value: The restrictionAndAttributes to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._restrictionAndAttributes = None
            return

        if not isinstance(value, FMConditionByFeaturesAndAttributes):
            raise TypeError(
                f"restrictionAndAttributes must be FMConditionByFeaturesAndAttributes or None, got {type(value).__name__}"
            )
        self._restrictionAndAttributes = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRestrictionAndAttributes(self) -> FMConditionByFeaturesAndAttributes:
        """
        AUTOSAR-compliant getter for restrictionAndAttributes.

        Returns:
            The restrictionAndAttributes value

        Note:
            Delegates to restriction_and_attributes property (CODING_RULE_V2_00017)
        """
        return self.restriction_and_attributes  # Delegates to property

    def setRestrictionAndAttributes(self, value: FMConditionByFeaturesAndAttributes) -> FMFeatureRestriction:
        """
        AUTOSAR-compliant setter for restrictionAndAttributes with method chaining.

        Args:
            value: The restrictionAndAttributes to set

        Returns:
            self for method chaining

        Note:
            Delegates to restriction_and_attributes property setter (gets validation automatically)
        """
        self.restriction_and_attributes = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_restriction_and_attributes(self, value: Optional[FMConditionByFeaturesAndAttributes]) -> FMFeatureRestriction:
        """
        Set restrictionAndAttributes and return self for chaining.

        Args:
            value: The restrictionAndAttributes to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_restriction_and_attributes("value")
        """
        self.restriction_and_attributes = value  # Use property setter (gets validation)
        return self



class FMFeatureRelation(Identifiable):
    """
    Defines relations for FMFeatures, for example dependencies on other
    FMFeatures, or conflicts with other FMFeatures. A FMFeature can only be part
    of a FMFeatureSelectionSet if all its relations are fulfilled.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureRelation

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 34, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The FMFeature that is targeted by this FMFeature.
        self._feature: List[FMFeature] = []

    @property
    def feature(self) -> List[FMFeature]:
        """Get feature (Pythonic accessor)."""
        return self._feature
        # If given, the condition shall evaluate to true, in order for
        # FMFeatureRelation to be active.
        self._restriction: Optional[FMConditionByFeaturesAndAttributes] = None

    @property
    def restriction(self) -> Optional[FMConditionByFeaturesAndAttributes]:
        """Get restriction (Pythonic accessor)."""
        return self._restriction

    @restriction.setter
    def restriction(self, value: Optional[FMConditionByFeaturesAndAttributes]) -> None:
        """
        Set restriction with validation.

        Args:
            value: The restriction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._restriction = None
            return

        if not isinstance(value, FMConditionByFeaturesAndAttributes):
            raise TypeError(
                f"restriction must be FMConditionByFeaturesAndAttributes or None, got {type(value).__name__}"
            )
        self._restriction = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFeature(self) -> List[FMFeature]:
        """
        AUTOSAR-compliant getter for feature.

        Returns:
            The feature value

        Note:
            Delegates to feature property (CODING_RULE_V2_00017)
        """
        return self.feature  # Delegates to property

    def getRestriction(self) -> FMConditionByFeaturesAndAttributes:
        """
        AUTOSAR-compliant getter for restriction.

        Returns:
            The restriction value

        Note:
            Delegates to restriction property (CODING_RULE_V2_00017)
        """
        return self.restriction  # Delegates to property

    def setRestriction(self, value: FMConditionByFeaturesAndAttributes) -> FMFeatureRelation:
        """
        AUTOSAR-compliant setter for restriction with method chaining.

        Args:
            value: The restriction to set

        Returns:
            self for method chaining

        Note:
            Delegates to restriction property setter (gets validation automatically)
        """
        self.restriction = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_restriction(self, value: Optional[FMConditionByFeaturesAndAttributes]) -> FMFeatureRelation:
        """
        Set restriction and return self for chaining.

        Args:
            value: The restriction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_restriction("value")
        """
        self.restriction = value  # Use property setter (gets validation)
        return self



class FMFeatureSelection(Identifiable):
    """
    that a FMFeatureSelection cannot include two FMAttributeValues that refer to
    the same FMAttributeDef in the role definition. feature FMFeature 0..1 ref
    The FMFeature whose state is defined by this FMFeature Selection. maximum
    BindingTimeEnum 0..1 attr Defines an upper bound for the binding time of the
    SelectedBinding variation points that are associated with the FMFeature,
    Time and refines its maximumIntendedBindingTime. This attribute is meant as
    a hint for the development process. minimum BindingTimeEnum 0..1 attr
    Defines a lower bound for the binding time of the variation SelectedBinding
    points that are associated with the FMFeature, and Time refines its
    minimumIntendedBindingTime. This attribute is meant as a hint for the
    development process. state FMFeatureSelection 0..1 attr Defines how the
    FMFeature that is described by this State FMFeatureSelection contributes to
    the FMFeature SelectionSet. A FMFeature may have the state selected,
    deselected or undecided. Table 5.2: FMFeatureSelection [constr_3661]
    Multiplicity of FMFeatureSelection.feature (cid:100)For each FMFea-
    tureSelection the reference in the role feature shall exist.(cid:99)()
    [constr_3662] Multiplicity of FMFeatureSelection.state (cid:100)For each
    FMFea- tureSelection the attribute state shall exist.(cid:99)() 40 of 92
    Document ID 606: AUTOSAR_FO_TPS_FeatureModelExchangeFormat AUTOSAR Feature
    Model Exchange Format AUTOSAR FO R23-11 5.2.1 Reference feature The
    reference feature points to the feature that is described by this
    FMFeatureSe- lection. 5.2.2 Attribute state FMFeatureSelection has an
    attribute state that defines how the feature referred to by feature
    contributes to the selection.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureSelection

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 40, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines a value for the attribute that is referred to in definition.
        self._attributeValue: List[FMAttributeValue] = []

    @property
    def attribute_value(self) -> List[FMAttributeValue]:
        """Get attributeValue (Pythonic accessor)."""
        return self._attributeValue

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttributeValue(self) -> List[FMAttributeValue]:
        """
        AUTOSAR-compliant getter for attributeValue.

        Returns:
            The attributeValue value

        Note:
            Delegates to attribute_value property (CODING_RULE_V2_00017)
        """
        return self.attribute_value  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class FMAttributeValue(ARObject):
    """
    This defines a value for the attribute that is referred to in the role
    definition.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMAttributeValue

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 42, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This refers to the definition of this attribute.
        self._definition: Optional[FMAttributeDef] = None

    @property
    def definition(self) -> Optional[FMAttributeDef]:
        """Get definition (Pythonic accessor)."""
        return self._definition

    @definition.setter
    def definition(self, value: Optional[FMAttributeDef]) -> None:
        """
        Set definition with validation.

        Args:
            value: The definition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._definition = None
            return

        if not isinstance(value, FMAttributeDef):
            raise TypeError(
                f"definition must be FMAttributeDef or None, got {type(value).__name__}"
            )
        self._definition = value
        self._value: Optional[Numerical] = None

    @property
    def value(self) -> Optional[Numerical]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional[Numerical]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"value must be Numerical or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefinition(self) -> FMAttributeDef:
        """
        AUTOSAR-compliant getter for definition.

        Returns:
            The definition value

        Note:
            Delegates to definition property (CODING_RULE_V2_00017)
        """
        return self.definition  # Delegates to property

    def setDefinition(self, value: FMAttributeDef) -> FMAttributeValue:
        """
        AUTOSAR-compliant setter for definition with method chaining.

        Args:
            value: The definition to set

        Returns:
            self for method chaining

        Note:
            Delegates to definition property setter (gets validation automatically)
        """
        self.definition = value  # Delegates to property setter
        return self

    def getValue(self) -> Numerical:
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: Numerical) -> FMAttributeValue:
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

    def with_definition(self, value: Optional[FMAttributeDef]) -> FMAttributeValue:
        """
        Set definition and return self for chaining.

        Args:
            value: The definition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_definition("value")
        """
        self.definition = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: Optional[Numerical]) -> FMAttributeValue:
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



class FMFeatureSelectionSet(ARElement):
    """
    A FMFeatureSelectionSet is a set of FMFeatures that describes a specific
    product.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureSelectionSet

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 44, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # All FMFeatures in this FMFeatureSelectionSet shall be the referenced
        # FMFeatureModel.
        self._featureModel: List[FMFeatureModel] = []

    @property
    def feature_model(self) -> List[FMFeatureModel]:
        """Get featureModel (Pythonic accessor)."""
        return self._featureModel
        # Each FMFeatureSelectionSet may include one or more establishes a hierarchy
        # See constr_5003 and details.
        self._include: List[RefType] = []

    @property
    def include(self) -> List[RefType]:
        """Get include (Pythonic accessor)."""
        return self._include
        # The set of FMFeatureSelections of this FMFeature.
        self._selection: List[FMFeatureSelection] = []

    @property
    def selection(self) -> List[FMFeatureSelection]:
        """Get selection (Pythonic accessor)."""
        return self._selection

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFeatureModel(self) -> List[FMFeatureModel]:
        """
        AUTOSAR-compliant getter for featureModel.

        Returns:
            The featureModel value

        Note:
            Delegates to feature_model property (CODING_RULE_V2_00017)
        """
        return self.feature_model  # Delegates to property

    def getInclude(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for include.

        Returns:
            The include value

        Note:
            Delegates to include property (CODING_RULE_V2_00017)
        """
        return self.include  # Delegates to property

    def getSelection(self) -> List[FMFeatureSelection]:
        """
        AUTOSAR-compliant getter for selection.

        Returns:
            The selection value

        Note:
            Delegates to selection property (CODING_RULE_V2_00017)
        """
        return self.selection  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class FMFeatureMap(ARElement):
    """
    A FMFeatureMap associates FMFeatures with variation points in the AUTOSAR
    model. To do this, it defines value sets for system constants and postbuild
    variant criterions that shall be chosen whenever a certain combination of
    features (and system constants) is encountered.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureMap

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 53, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Set of mappings defined by this FMFeatureMap.
        self._mapping: List[FMFeatureMapElement] = []

    @property
    def mapping(self) -> List[FMFeatureMapElement]:
        """Get mapping (Pythonic accessor)."""
        return self._mapping

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMapping(self) -> List[FMFeatureMapElement]:
        """
        AUTOSAR-compliant getter for mapping.

        Returns:
            The mapping value

        Note:
            Delegates to mapping property (CODING_RULE_V2_00017)
        """
        return self.mapping  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



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
        self._assertion: List[FMFeatureMap] = []

    @property
    def assertion(self) -> List[FMFeatureMap]:
        """Get assertion (Pythonic accessor)."""
        return self._assertion
        # Defines a condition which needs to be fulfilled for this to become active.
        self._condition: List[FMFeatureMap] = []

    @property
    def condition(self) -> List[FMFeatureMap]:
        """Get condition (Pythonic accessor)."""
        return self._condition
        # Selects a set of values for postbuild variant criterions.
        self._postBuildVariant: List[PostBuildVariant] = []

    @property
    def post_build_variant(self) -> List[PostBuildVariant]:
        """Get postBuildVariant (Pythonic accessor)."""
        return self._postBuildVariant
        # Selects a set of values for system constants.
        self._swValueSet: List[SwSystemconstant] = []

    @property
    def sw_value_set(self) -> List[SwSystemconstant]:
        """Get swValueSet (Pythonic accessor)."""
        return self._swValueSet

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssertion(self) -> List[FMFeatureMap]:
        """
        AUTOSAR-compliant getter for assertion.

        Returns:
            The assertion value

        Note:
            Delegates to assertion property (CODING_RULE_V2_00017)
        """
        return self.assertion  # Delegates to property

    def getCondition(self) -> List[FMFeatureMap]:
        """
        AUTOSAR-compliant getter for condition.

        Returns:
            The condition value

        Note:
            Delegates to condition property (CODING_RULE_V2_00017)
        """
        return self.condition  # Delegates to property

    def getPostBuildVariant(self) -> List[PostBuildVariant]:
        """
        AUTOSAR-compliant getter for postBuildVariant.

        Returns:
            The postBuildVariant value

        Note:
            Delegates to post_build_variant property (CODING_RULE_V2_00017)
        """
        return self.post_build_variant  # Delegates to property

    def getSwValueSet(self) -> List[SwSystemconstant]:
        """
        AUTOSAR-compliant getter for swValueSet.

        Returns:
            The swValueSet value

        Note:
            Delegates to sw_value_set property (CODING_RULE_V2_00017)
        """
        return self.sw_value_set  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class FMFeatureMapCondition(Identifiable):
    """
    Defines a condition which needs to be fulfilled for this mapping to become
    active. The condition is implemented as formula that is based on features
    and attributes and is defined by fmCond.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureMapCondition

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 55, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The formula that implements the condition.
        self._fmCondAndAttributes: Optional[FMConditionByFeaturesAndAttributes] = None

    @property
    def fm_cond_and_attributes(self) -> Optional[FMConditionByFeaturesAndAttributes]:
        """Get fmCondAndAttributes (Pythonic accessor)."""
        return self._fmCondAndAttributes

    @fm_cond_and_attributes.setter
    def fm_cond_and_attributes(self, value: Optional[FMConditionByFeaturesAndAttributes]) -> None:
        """
        Set fmCondAndAttributes with validation.

        Args:
            value: The fmCondAndAttributes to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fmCondAndAttributes = None
            return

        if not isinstance(value, FMConditionByFeaturesAndAttributes):
            raise TypeError(
                f"fmCondAndAttributes must be FMConditionByFeaturesAndAttributes or None, got {type(value).__name__}"
            )
        self._fmCondAndAttributes = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFmCondAndAttributes(self) -> FMConditionByFeaturesAndAttributes:
        """
        AUTOSAR-compliant getter for fmCondAndAttributes.

        Returns:
            The fmCondAndAttributes value

        Note:
            Delegates to fm_cond_and_attributes property (CODING_RULE_V2_00017)
        """
        return self.fm_cond_and_attributes  # Delegates to property

    def setFmCondAndAttributes(self, value: FMConditionByFeaturesAndAttributes) -> FMFeatureMapCondition:
        """
        AUTOSAR-compliant setter for fmCondAndAttributes with method chaining.

        Args:
            value: The fmCondAndAttributes to set

        Returns:
            self for method chaining

        Note:
            Delegates to fm_cond_and_attributes property setter (gets validation automatically)
        """
        self.fm_cond_and_attributes = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_fm_cond_and_attributes(self, value: Optional[FMConditionByFeaturesAndAttributes]) -> FMFeatureMapCondition:
        """
        Set fmCondAndAttributes and return self for chaining.

        Args:
            value: The fmCondAndAttributes to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fm_cond_and_attributes("value")
        """
        self.fm_cond_and_attributes = value  # Use property setter (gets validation)
        return self



class FMFeatureMapAssertion(Identifiable):
    """
    Defines a boolean expression which shall evaluate to true for this mapping
    to become active. The expression is a formula that is based on features and
    system constants, and is defined by fmSyscond.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFeatureMapAssertion

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 55, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The formula that implements the assertion.
        self._fmSyscondAndSwSystemconsts: Optional[FMConditionByFeaturesAndSwSystemconsts] = None

    @property
    def fm_syscond_and_sw_systemconsts(self) -> Optional[FMConditionByFeaturesAndSwSystemconsts]:
        """Get fmSyscondAndSwSystemconsts (Pythonic accessor)."""
        return self._fmSyscondAndSwSystemconsts

    @fm_syscond_and_sw_systemconsts.setter
    def fm_syscond_and_sw_systemconsts(self, value: Optional[FMConditionByFeaturesAndSwSystemconsts]) -> None:
        """
        Set fmSyscondAndSwSystemconsts with validation.

        Args:
            value: The fmSyscondAndSwSystemconsts to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fmSyscondAndSwSystemconsts = None
            return

        if not isinstance(value, FMConditionByFeaturesAndSwSystemconsts):
            raise TypeError(
                f"fmSyscondAndSwSystemconsts must be FMConditionByFeaturesAndSwSystemconsts or None, got {type(value).__name__}"
            )
        self._fmSyscondAndSwSystemconsts = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFmSyscondAndSwSystemconsts(self) -> FMConditionByFeaturesAndSwSystemconsts:
        """
        AUTOSAR-compliant getter for fmSyscondAndSwSystemconsts.

        Returns:
            The fmSyscondAndSwSystemconsts value

        Note:
            Delegates to fm_syscond_and_sw_systemconsts property (CODING_RULE_V2_00017)
        """
        return self.fm_syscond_and_sw_systemconsts  # Delegates to property

    def setFmSyscondAndSwSystemconsts(self, value: FMConditionByFeaturesAndSwSystemconsts) -> FMFeatureMapAssertion:
        """
        AUTOSAR-compliant setter for fmSyscondAndSwSystemconsts with method chaining.

        Args:
            value: The fmSyscondAndSwSystemconsts to set

        Returns:
            self for method chaining

        Note:
            Delegates to fm_syscond_and_sw_systemconsts property setter (gets validation automatically)
        """
        self.fm_syscond_and_sw_systemconsts = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_fm_syscond_and_sw_systemconsts(self, value: Optional[FMConditionByFeaturesAndSwSystemconsts]) -> FMFeatureMapAssertion:
        """
        Set fmSyscondAndSwSystemconsts and return self for chaining.

        Args:
            value: The fmSyscondAndSwSystemconsts to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fm_syscond_and_sw_systemconsts("value")
        """
        self.fm_syscond_and_sw_systemconsts = value  # Use property setter (gets validation)
        return self



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
        self._attribute: Optional[FMAttributeDef] = None

    @property
    def attribute(self) -> Optional[FMAttributeDef]:
        """Get attribute (Pythonic accessor)."""
        return self._attribute

    @attribute.setter
    def attribute(self, value: Optional[FMAttributeDef]) -> None:
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
        self._feature: Optional[FMFeature] = None

    @property
    def feature(self) -> Optional[FMFeature]:
        """Get feature (Pythonic accessor)."""
        return self._feature

    @feature.setter
    def feature(self, value: Optional[FMFeature]) -> None:
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

    def getAttribute(self) -> FMAttributeDef:
        """
        AUTOSAR-compliant getter for attribute.

        Returns:
            The attribute value

        Note:
            Delegates to attribute property (CODING_RULE_V2_00017)
        """
        return self.attribute  # Delegates to property

    def setAttribute(self, value: FMAttributeDef) -> FMFormulaByFeaturesAndAttributes:
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

    def getFeature(self) -> FMFeature:
        """
        AUTOSAR-compliant getter for feature.

        Returns:
            The feature value

        Note:
            Delegates to feature property (CODING_RULE_V2_00017)
        """
        return self.feature  # Delegates to property

    def setFeature(self, value: FMFeature) -> FMFormulaByFeaturesAndAttributes:
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

    def with_attribute(self, value: Optional[FMAttributeDef]) -> FMFormulaByFeaturesAndAttributes:
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

    def with_feature(self, value: Optional[FMFeature]) -> FMFormulaByFeaturesAndAttributes:
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



class FMConditionByFeaturesAndAttributes(ARObject):
    """
    A boolean expression that has the syntax of the AUTOSAR formula language but
    uses only references to features or feature attributes (not system
    constants) as operands.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMConditionByFeaturesAndAttributes

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 62, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class FMFormulaByFeaturesAndSwSystemconsts(ARObject, ABC):
    """
    An expression that has the syntax of the AUTOSAR formula language and may
    use references to features or system constants as operands.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMFormulaByFeaturesAndSwSystemconsts

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 63, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is FMFormulaByFeaturesAndSwSystemconsts:
            raise TypeError("FMFormulaByFeaturesAndSwSystemconsts is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # An expression of type FMFormulaByFeaturesAndSw refer to FMFeatures.
        self._feature: Optional[FMFeature] = None

    @property
    def feature(self) -> Optional[FMFeature]:
        """Get feature (Pythonic accessor)."""
        return self._feature

    @feature.setter
    def feature(self, value: Optional[FMFeature]) -> None:
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

    def getFeature(self) -> FMFeature:
        """
        AUTOSAR-compliant getter for feature.

        Returns:
            The feature value

        Note:
            Delegates to feature property (CODING_RULE_V2_00017)
        """
        return self.feature  # Delegates to property

    def setFeature(self, value: FMFeature) -> FMFormulaByFeaturesAndSwSystemconsts:
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

    def with_feature(self, value: Optional[FMFeature]) -> FMFormulaByFeaturesAndSwSystemconsts:
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



class FMConditionByFeaturesAndSwSystemconsts(ARObject):
    """
    A boolean expression that has the syntax of the AUTOSAR formula language and
    may use references to features or system constants as operands.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate::FMConditionByFeaturesAndSwSystemconsts

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 63, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


class FMFeatureSelectionState(AREnum):
    """
    FMFeatureSelectionState enumeration

Defines how a particular FMFeature contributes to a FMFSelectionSet. Aggregated by FMFeatureSelection.state

Package: M2::AUTOSARTemplates::FeatureModelTemplate
    """
    # The feature is excluded from the selection.
    deselected = "0"

    # The feature is included in the selection.
    selected = "1"

    # It is not yet decided whether the feature shall be included into or excluded from the selection.
    undecided = "2"
