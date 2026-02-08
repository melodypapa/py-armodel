from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class HwAttributeLiteralDef(Identifiable):
    """
    One available EnumerationLiteral of the Enumeration definition. Only
    applicable if the category of the Hw AttributeDef equals Enumeration.

    Package: M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory

    Sources:
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 26, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
