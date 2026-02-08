from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates import (
    AbstractMultiplicityRestriction,
)


class AttributeCondition(AbstractMultiplicityRestriction, ABC):
    """
    The AttributeCondition evaluates to true, if the referenced attribute is
    accepted by all rules of this condition.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Data::AttributeCondition

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 102, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AttributeCondition:
            raise TypeError("AttributeCondition is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
