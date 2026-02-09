from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class SwSystemconstantValueSet(ARElement):
    """
    This meta-class represents the ability to specify a set of system constant
    values.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling

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

    def with_sw(self, value):
        """
        Set sw and return self for chaining.

        Args:
            value: The sw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw("value")
        """
        self.sw = value  # Use property setter (gets validation)
        return self

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
