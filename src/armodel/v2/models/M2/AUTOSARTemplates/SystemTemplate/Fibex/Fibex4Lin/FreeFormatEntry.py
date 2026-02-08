from abc import ABC


class FreeFormatEntry(ScheduleTableEntry, ABC):
    """
    FreeFormat transmits a fixed master request frame with the eight data bytes
    provided. This may for instance be used to issue user specific fixed frames.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinCommunication::FreeFormatEntry

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 433, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is FreeFormatEntry:
            raise TypeError("FreeFormatEntry is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
