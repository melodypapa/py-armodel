from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class SdgAttribute(Identifiable, ABC):
    """
    Describes the attributes of an Sdg.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgAttribute

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 100, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is SdgAttribute:
            raise TypeError("SdgAttribute is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
