
class J1939RmOutgoingRequestServiceNeeds(ServiceNeeds):
    """
    This meta-class shall be used to specify needs with respect to the
    configuration of the J1939Rm, in particular for the case where an
    ApplicationSwComponentType needs to send a request to another J1939 node.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::J1939RmOutgoingRequestServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 829, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
