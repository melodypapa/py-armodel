from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import DataInterface

    RefType,
)


class NvDataInterface(DataInterface):
    """
    A non volatile data interface declares a number of VariableDataPrototypes to
    be exchanged between non volatile block components and atomic software
    components.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::NvDataInterface

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 324, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 664, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2041, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 457, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The VariableDataPrototype of this nv data interface.
        self._nvData: List[RefType] = []

    @property
    def nv_data(self) -> List[RefType]:
        """Get nvData (Pythonic accessor)."""
        return self._nvData

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNvData(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for nvData.

        Returns:
            The nvData value

        Note:
            Delegates to nv_data property (CODING_RULE_V2_00017)
        """
        return self.nv_data  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
