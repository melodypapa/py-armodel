from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class TransformationProps(Identifiable, ABC):
    """
    This meta-class represents a abstract base class for transformation
    settings.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 782, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TransformationProps:
            raise TypeError("TransformationProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
