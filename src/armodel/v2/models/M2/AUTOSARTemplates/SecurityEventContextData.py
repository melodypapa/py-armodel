from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SecurityEventContextData(ARObject):
    """
    This meta-class represents the possibility that context data can be attached
    to the aggregating Security EventDefinition. If this meta-class does not
    exist for a SecurityEventDefinition, then no context data shall be provided
    for this SecurityEventDefinition.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::SecurityEventContextData

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 66, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
