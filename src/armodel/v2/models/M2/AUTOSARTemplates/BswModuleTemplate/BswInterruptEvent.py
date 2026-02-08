
class BswInterruptEvent(BswEvent):
    """
    This meta-class represents an event triggered by an interrupt.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswInterruptEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 88, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
