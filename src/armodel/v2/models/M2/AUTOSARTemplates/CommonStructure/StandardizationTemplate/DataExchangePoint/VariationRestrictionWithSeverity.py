from armodel.v2.models.M2.AUTOSARTemplates import RestrictionWithSeverity


class VariationRestrictionWithSeverity(RestrictionWithSeverity):
    """
    Defines constraints on the usage of variation and on the valid binding
    times.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::VariationRestrictionWithSeverity

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 88, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
