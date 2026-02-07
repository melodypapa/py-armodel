from typing import List


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
