from armodel.v2.models.M2.AUTOSARTemplates import AbstractCanPhysicalChannel


class CanPhysicalChannel(AbstractCanPhysicalChannel):
    """
    CAN bus specific physical channel attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Can::CanTopology::CanPhysicalChannel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 73, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
