from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    TransformationDescription,
)


class UserDefinedTransformationDescription(TransformationDescription):
    """
    The UserDefinedTransformationDescription is used to specify details and
    documentation for custom transformers.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 771, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
