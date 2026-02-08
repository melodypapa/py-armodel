from abc import ABC
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable


class TransformationDescription(Describable, ABC):
    """
    The TransformationDescription is the abstract class that can be used by
    specific transformers to add transformer specific properties.

    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::TransformationDescription

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 199, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 770, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TransformationDescription:
            raise TypeError("TransformationDescription is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
