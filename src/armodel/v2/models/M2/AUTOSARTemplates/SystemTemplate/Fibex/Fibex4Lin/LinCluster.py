from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class LinCluster(ARObject):
    """
    LIN specific attributes

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology::LinCluster

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 93, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
