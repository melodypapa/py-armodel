from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
    Referrable,
)


class PncMappingIdent(Referrable):
    """
    This meta-class is created to add the ability to become the target of a
    reference to the non-Referrable PncMapping.

    Package: M2::AUTOSARTemplates::SystemTemplate::PncMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2044, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
