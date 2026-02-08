from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import AtomicSwComponentType


class NvBlockSwComponentType(AtomicSwComponentType):
    """
    The NvBlockSwComponentType defines non volatile data which data can be
    shared between Sw ComponentPrototypes. The non volatile data of the
    NvBlockSwComponentType are accessible via provided and required ports.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::NvBlockSwComponentType

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 663, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2040, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation formally defines the bulk Nv Blocks that provided to the
        # application software by the enclosing atpVariation.
        self._bulkNvData: List["BulkNvDataDescriptor"] = []

    @property
    def bulk_nv_data(self) -> List["BulkNvDataDescriptor"]:
        """Get bulkNvData (Pythonic accessor)."""
        return self._bulkNvData
        # Specification of the properties of exactly one NVRAM atpVariation.
        self._nvBlock: List["NvBlockDescriptor"] = []

    @property
    def nv_block(self) -> List["NvBlockDescriptor"]:
        """Get nvBlock (Pythonic accessor)."""
        return self._nvBlock

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBulkNvData(self) -> List["BulkNvDataDescriptor"]:
        """
        AUTOSAR-compliant getter for bulkNvData.

        Returns:
            The bulkNvData value

        Note:
            Delegates to bulk_nv_data property (CODING_RULE_V2_00017)
        """
        return self.bulk_nv_data  # Delegates to property

    def getNvBlock(self) -> List["NvBlockDescriptor"]:
        """
        AUTOSAR-compliant getter for nvBlock.

        Returns:
            The nvBlock value

        Note:
            Delegates to nv_block property (CODING_RULE_V2_00017)
        """
        return self.nv_block  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
