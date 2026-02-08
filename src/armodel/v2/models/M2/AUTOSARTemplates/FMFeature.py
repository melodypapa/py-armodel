from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    BindingTimeEnum,
    FMAttributeDef,
    FMFeatureRelation,
    FMFeatureRestriction,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


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
        self._attributeDef: List["FMAttributeDef"] = []

    @property
    def attribute_def(self) -> List["FMAttributeDef"]:
        """Get attributeDef (Pythonic accessor)."""
        return self._attributeDef
        # Lists the sub-features of a feature.
        self._decompositionDecomposition: List["FMFeature"] = []

    @property
    def decomposition_decomposition(self) -> List["FMFeature"]:
        """Get decompositionDecomposition (Pythonic accessor)."""
        return self._decompositionDecomposition
        # Defines an upper bound for the binding time of the points that are associated
                # with the FMFeature.
        # attribute is meant as a hint for the development.
        self._maximum: Optional["BindingTimeEnum"] = None

    @property
    def maximum(self) -> Optional["BindingTimeEnum"]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional["BindingTimeEnum"]) -> None:
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
        # Defines a lower bound for the binding time of the variation that are
                # associated with the FMFeature.
        # This is meant as a hint for the development process.
        self._minimum: Optional["BindingTimeEnum"] = None

    @property
    def minimum(self) -> Optional["BindingTimeEnum"]:
        """Get minimum (Pythonic accessor)."""
        return self._minimum

    @minimum.setter
    def minimum(self, value: Optional["BindingTimeEnum"]) -> None:
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
        # Defines relations for FMFeatures, for example other FMFeatures, or conflicts
        # with A FMFeature can only be part of a all its relations are fulfilled.
        self._relation: List["FMFeatureRelation"] = []

    @property
    def relation(self) -> List["FMFeatureRelation"]:
        """Get relation (Pythonic accessor)."""
        return self._relation
        # Defines restrictions for FMFeatures.
        # A FMFeature can part of a FMFeatureSelectionSet if at least one of evaluates
                # to true.
        self._restriction: List["FMFeatureRestriction"] = []

    @property
    def restriction(self) -> List["FMFeatureRestriction"]:
        """Get restriction (Pythonic accessor)."""
        return self._restriction

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttributeDef(self) -> List["FMAttributeDef"]:
        """
        AUTOSAR-compliant getter for attributeDef.

        Returns:
            The attributeDef value

        Note:
            Delegates to attribute_def property (CODING_RULE_V2_00017)
        """
        return self.attribute_def  # Delegates to property

    def getDecompositionDecomposition(self) -> List["FMFeature"]:
        """
        AUTOSAR-compliant getter for decompositionDecomposition.

        Returns:
            The decompositionDecomposition value

        Note:
            Delegates to decomposition_decomposition property (CODING_RULE_V2_00017)
        """
        return self.decomposition_decomposition  # Delegates to property

    def getMaximum(self) -> "BindingTimeEnum":
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: "BindingTimeEnum") -> "FMFeature":
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

    def getMinimum(self) -> "BindingTimeEnum":
        """
        AUTOSAR-compliant getter for minimum.

        Returns:
            The minimum value

        Note:
            Delegates to minimum property (CODING_RULE_V2_00017)
        """
        return self.minimum  # Delegates to property

    def setMinimum(self, value: "BindingTimeEnum") -> "FMFeature":
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

    def getRelation(self) -> List["FMFeatureRelation"]:
        """
        AUTOSAR-compliant getter for relation.

        Returns:
            The relation value

        Note:
            Delegates to relation property (CODING_RULE_V2_00017)
        """
        return self.relation  # Delegates to property

    def getRestriction(self) -> List["FMFeatureRestriction"]:
        """
        AUTOSAR-compliant getter for restriction.

        Returns:
            The restriction value

        Note:
            Delegates to restriction property (CODING_RULE_V2_00017)
        """
        return self.restriction  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_maximum(self, value: Optional["BindingTimeEnum"]) -> "FMFeature":
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

    def with_minimum(self, value: Optional["BindingTimeEnum"]) -> "FMFeature":
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
