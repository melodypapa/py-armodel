from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    FMFeatureModel,
    FMFeatureSelection,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


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
