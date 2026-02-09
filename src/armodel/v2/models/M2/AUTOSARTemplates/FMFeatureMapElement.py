from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class FMFeatureMapElement(Identifiable):
    """
    Defines value sets for system constants and postbuild variant criterions
    that shall be chosen whenever a certain combination of features (and system
    constants) is encountered.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate

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
