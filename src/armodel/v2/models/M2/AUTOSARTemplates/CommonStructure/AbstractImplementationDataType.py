from abc import ABC
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import AutosarDataType


class AbstractImplementationDataType(AutosarDataType, ABC):
    """
    This meta-class represents an abstract base class for different flavors of
    ImplementationDataType.

    Package: M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes::AbstractImplementationDataType

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 267, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 42, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is AbstractImplementationDataType:
            raise TypeError("AbstractImplementationDataType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
