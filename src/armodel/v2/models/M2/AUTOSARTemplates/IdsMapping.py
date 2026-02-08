from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.SecurityExtractTemplate import (
    IdsCommonElement,
)


class IdsMapping(IdsCommonElement, ABC):
    """
    This meta-class serves as abstract base class for mappings related to an IDS
    design.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 62, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is IdsMapping:
            raise TypeError("IdsMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
