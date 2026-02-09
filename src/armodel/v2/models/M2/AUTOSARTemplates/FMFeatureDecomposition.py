from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class FMFeatureDecomposition(ARObject):
    """
    A FMFeatureDecomposition describes dependencies between a list of features
    and their parent feature (i.e., the FMFeature that aggregates the
    FMFeatureDecomposition). The kind of dependency is defined by the attribute
    category.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 27, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The category of a FMFeatureDecomposition defines the dependency that is
        # defined by the FMFeature are four different categories: MULTIPLEFEATURE.
        self._category: Optional["CategoryString"] = None

    @property
    def category(self) -> Optional["CategoryString"]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional["CategoryString"]) -> None:
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
        # The features that are affected by the dependency defined
                # FMFeatureDecomposition.
        # 92 Document ID 606: AUTOSAR_FO_TPS_FeatureModelExchangeFormat Model Exchange
                # Format R23-11.
        self._feature: List["FMFeature"] = []

    @property
    def feature(self) -> List["FMFeature"]:
        """Get feature (Pythonic accessor)."""
        return self._feature
        # For a dependency of category MULTIPLEFEATURE, this maximum number of features
        # allowed.
        self._max: Optional["PositiveInteger"] = None

    @property
    def max(self) -> Optional["PositiveInteger"]:
        """Get max (Pythonic accessor)."""
        return self._max

    @max.setter
    def max(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"max must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._max = value
        # For a dependency of category MULTIPLEFEATURE, this minimum number of features
        # allowed.
        self._min: Optional["PositiveInteger"] = None

    @property
    def min(self) -> Optional["PositiveInteger"]:
        """Get min (Pythonic accessor)."""
        return self._min

    @min.setter
    def min(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"min must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._min = value

    def with_feature(self, value):
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCategory(self) -> "CategoryString":
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "CategoryString") -> "FMFeatureDecomposition":
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

    def getFeature(self) -> List["FMFeature"]:
        """
        AUTOSAR-compliant getter for feature.

        Returns:
            The feature value

        Note:
            Delegates to feature property (CODING_RULE_V2_00017)
        """
        return self.feature  # Delegates to property

    def getMax(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for max.

        Returns:
            The max value

        Note:
            Delegates to max property (CODING_RULE_V2_00017)
        """
        return self.max  # Delegates to property

    def setMax(self, value: "PositiveInteger") -> "FMFeatureDecomposition":
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

    def getMin(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for min.

        Returns:
            The min value

        Note:
            Delegates to min property (CODING_RULE_V2_00017)
        """
        return self.min  # Delegates to property

    def setMin(self, value: "PositiveInteger") -> "FMFeatureDecomposition":
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

    def with_category(self, value: Optional["CategoryString"]) -> "FMFeatureDecomposition":
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

    def with_max(self, value: Optional["PositiveInteger"]) -> "FMFeatureDecomposition":
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

    def with_min(self, value: Optional["PositiveInteger"]) -> "FMFeatureDecomposition":
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
