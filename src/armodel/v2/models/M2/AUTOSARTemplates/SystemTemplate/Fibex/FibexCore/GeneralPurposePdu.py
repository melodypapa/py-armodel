
class GeneralPurposePdu(Pdu):
    """
    This element is used for AUTOSAR Pdus without additional attributes that are
    routed by a bus interface. Please note that the category name of such Pdus
    is standardized in the AUTOSAR System Template.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::GeneralPurposePdu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 344, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
