from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates import PortInterface


class DataInterface(PortInterface, ABC):
    """
    The purpose of this meta-class is to act as an abstract base class for
    subclasses that share the semantics of being concerned about data (as
    opposed to e.g. operations).

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::DataInterface

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 310, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 87, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DataInterface:
            raise TypeError("DataInterface is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
