
class ApplicationPartition(ARElement):
    """
    ApplicationPartition to which SwComponentPrototypes are mapped at a point in
    time when the corresponding EcuInstance is not yet known or defined. In a
    later methodology step the Application Partition can be assigned to an
    EcuPartition.

    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping::ApplicationPartition

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 200, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
