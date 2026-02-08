from armodel.v2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswScheduleEvent

class BswBackgroundEvent(BswScheduleEvent):
    """
    A recurring BswEvent which is used to perform background activities. It is
    similar to a BswTimingEvent but has no fixed time period and is activated
    only with low priority.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswBackgroundEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 89, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
