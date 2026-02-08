from armodel.v2.models.M2.AUTOSARTemplates import EngineeringObject


class AutosarEngineeringObject(EngineeringObject):
    """
    This denotes an engineering object being part of the process. It is a
    specialization of the abstract class EngineeringObject for usage within
    AUTOSAR.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::EngineeringObject::AutosarEngineeringObject

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 132, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 622, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 161, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
