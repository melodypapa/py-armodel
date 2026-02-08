from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef import (
    SdgAbstractForeignReference,
)


class SdgForeignReference(SdgAbstractForeignReference):
    """
    A reference without variation support that can point to any referrable
    object in an AUTOSAR Model. This class accepts the special data "Sdx"
    reference.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 102, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
