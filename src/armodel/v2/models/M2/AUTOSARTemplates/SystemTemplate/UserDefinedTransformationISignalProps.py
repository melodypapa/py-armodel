from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class UserDefinedTransformationISignalProps(ARObject):
    """
    The UserDefinedTransformationISignalProps is used to specify ISignal
    specific configuration properties for custom transformers.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 828, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
