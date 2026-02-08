from abc import ABC
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Constants import ValueSpecification


class AbstractRuleBasedValueSpecification(ValueSpecification, ABC):
    """
    This represents an abstract base class for all rule-based value
    specifications.

    Package: M2::AUTOSARTemplates::CommonStructure::Constants::AbstractRuleBasedValueSpecification

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 462, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractRuleBasedValueSpecification:
            raise TypeError("AbstractRuleBasedValueSpecification is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
