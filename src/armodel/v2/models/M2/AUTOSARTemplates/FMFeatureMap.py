from typing import List


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
        self._mapping: List["FMFeatureMapElement"] = []

    @property
    def mapping(self) -> List["FMFeatureMapElement"]:
        """Get mapping (Pythonic accessor)."""
        return self._mapping

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMapping(self) -> List["FMFeatureMapElement"]:
        """
        AUTOSAR-compliant getter for mapping.

        Returns:
            The mapping value

        Note:
            Delegates to mapping property (CODING_RULE_V2_00017)
        """
        return self.mapping  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
