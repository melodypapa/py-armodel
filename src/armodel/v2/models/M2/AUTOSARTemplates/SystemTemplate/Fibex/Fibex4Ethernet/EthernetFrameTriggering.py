from armodel.v2.models.M2.AUTOSARTemplates import FrameTriggering


class EthernetFrameTriggering(FrameTriggering):
    """
    Ethernet specific Frame element.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetFrame::EthernetFrameTriggering

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 578, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
