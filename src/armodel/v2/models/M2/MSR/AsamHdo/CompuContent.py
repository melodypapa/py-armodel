from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CompuContent(ARObject, ABC):
    """
    This abstract meta-class represents the various definition means of a
    computation method.

    Package: M2::MSR::AsamHdo::ComputationMethod

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 386, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is CompuContent:
            raise TypeError("CompuContent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
