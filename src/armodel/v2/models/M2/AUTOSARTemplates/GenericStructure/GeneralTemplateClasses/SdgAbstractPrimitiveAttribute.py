from abc import ABC


class SdgAbstractPrimitiveAttribute(SdgElementWithGid, ABC):
    """
    Describes primitive attributes of a special data group.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgAbstractPrimitiveAttribute

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 100, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is SdgAbstractPrimitiveAttribute:
            raise TypeError("SdgAbstractPrimitiveAttribute is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
