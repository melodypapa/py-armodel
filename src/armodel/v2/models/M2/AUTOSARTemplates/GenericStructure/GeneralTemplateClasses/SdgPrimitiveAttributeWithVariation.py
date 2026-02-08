from armodel.v2.models.M2.AUTOSARTemplates import SdgAbstractPrimitiveAttribute


class SdgPrimitiveAttributeWithVariation(SdgAbstractPrimitiveAttribute):
    """
    Describes a primitive numerical special data attribute with variation. This
    class accepts a special data "sdf" element.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgPrimitiveAttributeWithVariation

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 101, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
