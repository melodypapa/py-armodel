from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common import RestrictionWithSeverity

class MultiplicityRestrictionWithSeverity(RestrictionWithSeverity):
    """
    Restriction that specifies the valid number of occurrences of an element in
    the current context.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::MultiplicityRestrictionWithSeverity

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 87, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
