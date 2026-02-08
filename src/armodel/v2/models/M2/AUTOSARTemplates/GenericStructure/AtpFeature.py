from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class AtpFeature(Identifiable, ABC):
    """
    Features are properties via which a classifier classifies instances. Or: a
    classifier has features and every M0 instance of it will have those
    features.

    Package: M2::AUTOSARTemplates::GenericStructure::AbstractStructure::AtpFeature

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 173, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AtpFeature:
            raise TypeError("AtpFeature is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
