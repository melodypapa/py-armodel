from armodel.v2.models.M2.AUTOSARTemplates import AbstractEthernetFrame


class UserDefinedEthernetFrame(AbstractEthernetFrame):
    """
    UserDefinedEthernetFrame allows the description of a frame-based
    communication to Complex Drivers that are located above the EthDrv.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetFrame::UserDefinedEthernetFrame

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 579, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
