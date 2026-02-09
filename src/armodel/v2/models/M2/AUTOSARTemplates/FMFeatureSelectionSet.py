from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)

    RefType,
)


class FMFeatureSelectionSet(ARElement):
    """
    A FMFeatureSelectionSet is a set of FMFeatures that describes a specific
    product.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 44, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # All FMFeatures in this FMFeatureSelectionSet shall be the referenced
        # FMFeatureModel.
        self._featureModel: List["FMFeatureModel"] = []

    @property
    def feature_model(self) -> List["FMFeatureModel"]:
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
        self._selection: List["FMFeatureSelection"] = []

    @property
    def selection(self) -> List["FMFeatureSelection"]:
        """Get selection (Pythonic accessor)."""
        return self._selection

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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFeatureModel(self) -> List["FMFeatureModel"]:
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

    def getSelection(self) -> List["FMFeatureSelection"]:
        """
        AUTOSAR-compliant getter for selection.

        Returns:
            The selection value

        Note:
            Delegates to selection property (CODING_RULE_V2_00017)
        """
        return self.selection  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
