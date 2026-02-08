from abc import ABC


class BswScheduleEvent(BswEvent, ABC):
    """
    BswEvent that is able to start a BswSchedulabeEntity.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswScheduleEvent

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 88, Classic
      Platform R23-11)
    """
    def __init__(self):
        if type(self) is BswScheduleEvent:
            raise TypeError("BswScheduleEvent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
