from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates import Describable


class TransformationComSpecProps(Describable, ABC):
    """
    TransformationComSpecProps holds all the attributes for transformers that
    are port specific.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::TransformationComSpecProps

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 196, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2075, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TransformationComSpecProps:
            raise TypeError("TransformationComSpecProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
