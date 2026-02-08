from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import BusspecificNmEcu

class J1939NmEcu(BusspecificNmEcu):
    """
    J1939 NmEcu specific attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement::J1939NmEcu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 694, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
