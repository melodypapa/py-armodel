from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class Br(ARObject):
    """
    This element is the same as function here as in a HTML document i.e. it
    forces a line break.

    Package: M2::MSR::Documentation::TextModel::InlineTextElements

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 316, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
