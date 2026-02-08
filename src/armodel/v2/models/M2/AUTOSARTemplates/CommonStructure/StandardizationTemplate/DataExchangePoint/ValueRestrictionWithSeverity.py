from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common import RestrictionWithSeverity

class ValueRestrictionWithSeverity(RestrictionWithSeverity):
    """
    Specifies valid values of primitive data types. A value is valid if all
    rules defined by this ValueRestriction evaluate to true.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::ValueRestrictionWithSeverity

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 87, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
