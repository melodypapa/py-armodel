from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class BulkNvDataDescriptor(Identifiable):
    """
    This meta-class represents one bulk NV Data Block that is read-only for the
    application software. The purpose of a bulk NV Data Block is to provide
    access to information uploaded to the vehicle at e.g. the end of the
    production line.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::NvBlockComponent::BulkNvDataDescriptor
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 692, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents the actual bulk NVBlock.
        self._bulkNvBlock: RefType = None

    @property
    def bulk_nv_block(self) -> RefType:
        """Get bulkNvBlock (Pythonic accessor)."""
        return self._bulkNvBlock

    @bulk_nv_block.setter
    def bulk_nv_block(self, value: RefType) -> None:
        """
        Set bulkNvBlock with validation.
        
        Args:
            value: The bulkNvBlock to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bulkNvBlock = None
            return

        self._bulkNvBlock = value
        # Defines the mapping between the VariableData in the NvBlockComponents ports
                # and the the non-volatile memory.
        # of NvBlockDataMapping is subject to the purpose to support the conditional nv
                # data ports.
        # atpVariation.
        self._nvBlockData: List[RefType] = []

    @property
    def nv_block_data(self) -> List[RefType]:
        """Get nvBlockData (Pythonic accessor)."""
        return self._nvBlockData

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBulkNvBlock(self) -> RefType:
        """
        AUTOSAR-compliant getter for bulkNvBlock.
        
        Returns:
            The bulkNvBlock value
        
        Note:
            Delegates to bulk_nv_block property (CODING_RULE_V2_00017)
        """
        return self.bulk_nv_block  # Delegates to property

    def setBulkNvBlock(self, value: RefType) -> "BulkNvDataDescriptor":
        """
        AUTOSAR-compliant setter for bulkNvBlock with method chaining.
        
        Args:
            value: The bulkNvBlock to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to bulk_nv_block property setter (gets validation automatically)
        """
        self.bulk_nv_block = value  # Delegates to property setter
        return self

    def getNvBlockData(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for nvBlockData.
        
        Returns:
            The nvBlockData value
        
        Note:
            Delegates to nv_block_data property (CODING_RULE_V2_00017)
        """
        return self.nv_block_data  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bulk_nv_block(self, value: Optional[RefType]) -> "BulkNvDataDescriptor":
        """
        Set bulkNvBlock and return self for chaining.
        
        Args:
            value: The bulkNvBlock to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_bulk_nv_block("value")
        """
        self.bulk_nv_block = value  # Use property setter (gets validation)
        return self