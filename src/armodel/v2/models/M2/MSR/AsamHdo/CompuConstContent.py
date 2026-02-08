from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class CompuConstContent(ARObject, ABC):
    """
    This meta-class represents the fact that the constant value of the
    computation method can be numerical or textual.

    Package: M2::MSR::AsamHdo::ComputationMethod

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 390, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is CompuConstContent:
            raise TypeError("CompuConstContent is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
