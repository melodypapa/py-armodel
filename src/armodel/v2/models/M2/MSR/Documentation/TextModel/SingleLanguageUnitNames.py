from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SingleLanguageUnitNames(ARObject):
    """
    This represents the ability to express a display name.

    Package: M2::MSR::Documentation::TextModel::SingleLanguageData

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 400, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
