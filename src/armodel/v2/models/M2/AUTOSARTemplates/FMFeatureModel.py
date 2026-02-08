from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import FMFeature
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
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
        self._feature: List["FMFeature"] = []

    @property
    def feature(self) -> List["FMFeature"]:
        """Get feature (Pythonic accessor)."""
        return self._feature
        # The features of a feature model define a tree.
        # The points to the root of this tree.
        self._root: Optional["FMFeature"] = None

    @property
    def root(self) -> Optional["FMFeature"]:
        """Get root (Pythonic accessor)."""
        return self._root

    @root.setter
    def root(self, value: Optional["FMFeature"]) -> None:
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFeature(self) -> List["FMFeature"]:
        """
        AUTOSAR-compliant getter for feature.

        Returns:
            The feature value

        Note:
            Delegates to feature property (CODING_RULE_V2_00017)
        """
        return self.feature  # Delegates to property

    def getRoot(self) -> "FMFeature":
        """
        AUTOSAR-compliant getter for root.

        Returns:
            The root value

        Note:
            Delegates to root property (CODING_RULE_V2_00017)
        """
        return self.root  # Delegates to property

    def setRoot(self, value: "FMFeature") -> "FMFeatureModel":
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

    def with_root(self, value: Optional["FMFeature"]) -> "FMFeatureModel":
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
