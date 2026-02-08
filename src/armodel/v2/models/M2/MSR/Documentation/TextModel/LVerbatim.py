from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class LVerbatim(ARObject):
    """
    MixedContentForVerbatim in one particular language. The language is denoted
    in the attribute l.

    Package: M2::MSR::Documentation::TextModel::LanguageDataModel::LVerbatim

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 347, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
