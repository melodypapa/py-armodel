from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class LifeCycleState(Identifiable):
    """
    This meta class represents one particular state in the LifeCycle.

    Package: M2::AUTOSARTemplates::GenericStructure::LifeCycles::LifeCycleState

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 388, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 196, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
