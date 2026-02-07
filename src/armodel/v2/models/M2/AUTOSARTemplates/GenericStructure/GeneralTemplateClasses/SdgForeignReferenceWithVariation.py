
class SdgForeignReferenceWithVariation(SdgAbstractForeignReference):
    """
    A reference with variation support that can point to any referrable object
    in an AUTOSAR Model. This class accepts the special data "Sdxf" reference.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgForeignReferenceWithVariation

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 102, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
