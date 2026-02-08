from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    BusspecificNmEcu,
)


class UdpNmEcu(BusspecificNmEcu):
    """
    Udp NM specific ECU attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::NetworkManagement

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 688, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
