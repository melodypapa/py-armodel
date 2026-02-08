from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    TransformationComSpecProps,
)


class UserDefinedTransformationComSpecProps(TransformationComSpecProps):
    """
    The UserDefinedTransformationComSpecProps is used to specify port specific
    configuration properties for custom transformers.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 200, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
