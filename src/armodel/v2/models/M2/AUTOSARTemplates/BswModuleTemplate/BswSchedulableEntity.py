from armodel.v2.models.M2.AUTOSARTemplates import BswModuleEntity


class BswSchedulableEntity(BswModuleEntity):
    """
    BSW module entity, which is designed for control by the BSW Scheduler. It
    may for example implement a so-called "main" function.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswSchedulableEntity

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 75, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 978, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
