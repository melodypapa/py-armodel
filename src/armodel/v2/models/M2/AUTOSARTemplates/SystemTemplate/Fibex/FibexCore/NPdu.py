from armodel.v2.models.M2.AUTOSARTemplates import IPdu


class NPdu(IPdu):
    """
    This is a Pdu of the Transport Layer. The main purpose of the TP Layer is to
    segment and reassemble IPdus.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::NPdu

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 301, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 343, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
