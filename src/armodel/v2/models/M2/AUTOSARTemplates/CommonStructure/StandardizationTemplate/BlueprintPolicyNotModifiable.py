from armodel.v2.models.M2.AUTOSARTemplates import BlueprintPolicy


class BlueprintPolicyNotModifiable(BlueprintPolicy):
    """
    The class represents that the related attribute is not modifiable during the
    blueprinting.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure::BlueprintPolicyNotModifiable

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 164, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
