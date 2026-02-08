from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DoIpServiceNeeds

class FurtherActionByteNeeds(DoIpServiceNeeds):
    """
    The FurtherActionByteNeeds indicates that the software-component is able to
    provide the "further action byte" to the DoIp Service Component.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::FurtherActionByteNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 812, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
