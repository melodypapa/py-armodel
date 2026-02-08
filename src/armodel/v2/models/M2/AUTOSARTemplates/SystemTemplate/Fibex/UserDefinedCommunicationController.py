from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class UserDefinedCommunicationController(ARObject):
    """
    This element allows the modeling of arbitrary Communication Controllers.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::CddSupport

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 180, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
