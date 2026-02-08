from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BlockState(Identifiable):
    """
    This meta-class defines a block state that is part of the collection of
    block states belonging to a specific IdsmInstance. The IdsM shall discard
    any reported security event that is mapped to a filter chain containing a
    SecurityEventStateFilter that references the block state which is currently
    active in the IdsM.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 52, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
