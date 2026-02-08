from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class MixedContentForPlainText(ARObject, ABC):
    """
    This represents a plain text which conceptually is handled as mixed
    contents. It is modeled as such for symmetry reasons.

    Package: M2::MSR::Documentation::TextModel::InlineTextModel::MixedContentForPlainText

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 349, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is MixedContentForPlainText:
            raise TypeError("MixedContentForPlainText is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
