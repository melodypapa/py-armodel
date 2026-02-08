from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class SubElementRef(ARObject, ABC):
    """
    This meta-class provides the ability to reference elements of composite data
    type.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 138, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is SubElementRef:
            raise TypeError("SubElementRef is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
