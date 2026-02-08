from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ImpositionTime(Identifiable):
    """
    This meta class represents one particular imposition time.

    Package: M2::AUTOSARTemplates::GenericStructure::ImpositionTimes

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 194, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
