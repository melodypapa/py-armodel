from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class NvBlockDataMapping(ARObject):
    """
    Defines the mapping between the VariableDataPrototypes in the
    NvBlockComponents ports and the VariableDataPrototypes of the RAM Block. The
    data types of the referenced VariableDataPrototypes in the ports and the
    referenced sub-element (inside a CompositeDataType) of the
    VariableDataPrototype representing the RAM Block shall be compatible.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::NvBlockComponent::NvBlockDataMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 688, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute identifies the applicable bit mask on the side the
        # PortPrototype.
        self._bitfieldTextTable: Optional["PositiveInteger"] = None

    @property
    def bitfield_text_table(self) -> Optional["PositiveInteger"]:
        """Get bitfieldTextTable (Pythonic accessor)."""
        return self._bitfieldTextTable

    @bitfield_text_table.setter
    def bitfield_text_table(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set bitfieldTextTable with validation.
        
        Args:
            value: The bitfieldTextTable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bitfieldTextTable = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"bitfieldTextTable must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._bitfieldTextTable = value
        # Reference to a VariableDataPrototype of a RAM Block.
        self._nvRamBlock: RefType = None

    @property
    def nv_ram_block(self) -> RefType:
        """Get nvRamBlock (Pythonic accessor)."""
        return self._nvRamBlock

    @nv_ram_block.setter
    def nv_ram_block(self, value: RefType) -> None:
        """
        Set nvRamBlock with validation.
        
        Args:
            value: The nvRamBlock to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nvRamBlock = None
            return

        self._nvRamBlock = value
        # Reference to a VariableDataPrototype of a pPort of the read access to the RAM
        # is no PortPrototype providing read access reference can be omitted.
        self._readNvData: RefType = None

    @property
    def read_nv_data(self) -> RefType:
        """Get readNvData (Pythonic accessor)."""
        return self._readNvData

    @read_nv_data.setter
    def read_nv_data(self, value: RefType) -> None:
        """
        Set readNvData with validation.
        
        Args:
            value: The readNvData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._readNvData = None
            return

        self._readNvData = value
        # Reference to a VariableDataPrototype of a rPort of the Nv write access to the
        # RAM there is no port providing write access reference can be omitted.
        self._writtenNvData: RefType = None

    @property
    def written_nv_data(self) -> RefType:
        """Get writtenNvData (Pythonic accessor)."""
        return self._writtenNvData

    @written_nv_data.setter
    def written_nv_data(self, value: RefType) -> None:
        """
        Set writtenNvData with validation.
        
        Args:
            value: The writtenNvData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._writtenNvData = None
            return

        self._writtenNvData = value
        # Reference to a VariableDataPrototype of a PRPort of the
        # NvBlockSwComponentType providing read access to the RAM Block.
        self._writtenReadNv: RefType = None

    @property
    def written_read_nv(self) -> RefType:
        """Get writtenReadNv (Pythonic accessor)."""
        return self._writtenReadNv

    @written_read_nv.setter
    def written_read_nv(self, value: RefType) -> None:
        """
        Set writtenReadNv with validation.
        
        Args:
            value: The writtenReadNv to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._writtenReadNv = None
            return

        self._writtenReadNv = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBitfieldTextTable(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for bitfieldTextTable.
        
        Returns:
            The bitfieldTextTable value
        
        Note:
            Delegates to bitfield_text_table property (CODING_RULE_V2_00017)
        """
        return self.bitfield_text_table  # Delegates to property

    def setBitfieldTextTable(self, value: "PositiveInteger") -> "NvBlockDataMapping":
        """
        AUTOSAR-compliant setter for bitfieldTextTable with method chaining.
        
        Args:
            value: The bitfieldTextTable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to bitfield_text_table property setter (gets validation automatically)
        """
        self.bitfield_text_table = value  # Delegates to property setter
        return self

    def getNvRamBlock(self) -> RefType:
        """
        AUTOSAR-compliant getter for nvRamBlock.
        
        Returns:
            The nvRamBlock value
        
        Note:
            Delegates to nv_ram_block property (CODING_RULE_V2_00017)
        """
        return self.nv_ram_block  # Delegates to property

    def setNvRamBlock(self, value: RefType) -> "NvBlockDataMapping":
        """
        AUTOSAR-compliant setter for nvRamBlock with method chaining.
        
        Args:
            value: The nvRamBlock to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to nv_ram_block property setter (gets validation automatically)
        """
        self.nv_ram_block = value  # Delegates to property setter
        return self

    def getReadNvData(self) -> RefType:
        """
        AUTOSAR-compliant getter for readNvData.
        
        Returns:
            The readNvData value
        
        Note:
            Delegates to read_nv_data property (CODING_RULE_V2_00017)
        """
        return self.read_nv_data  # Delegates to property

    def setReadNvData(self, value: RefType) -> "NvBlockDataMapping":
        """
        AUTOSAR-compliant setter for readNvData with method chaining.
        
        Args:
            value: The readNvData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to read_nv_data property setter (gets validation automatically)
        """
        self.read_nv_data = value  # Delegates to property setter
        return self

    def getWrittenNvData(self) -> RefType:
        """
        AUTOSAR-compliant getter for writtenNvData.
        
        Returns:
            The writtenNvData value
        
        Note:
            Delegates to written_nv_data property (CODING_RULE_V2_00017)
        """
        return self.written_nv_data  # Delegates to property

    def setWrittenNvData(self, value: RefType) -> "NvBlockDataMapping":
        """
        AUTOSAR-compliant setter for writtenNvData with method chaining.
        
        Args:
            value: The writtenNvData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to written_nv_data property setter (gets validation automatically)
        """
        self.written_nv_data = value  # Delegates to property setter
        return self

    def getWrittenReadNv(self) -> RefType:
        """
        AUTOSAR-compliant getter for writtenReadNv.
        
        Returns:
            The writtenReadNv value
        
        Note:
            Delegates to written_read_nv property (CODING_RULE_V2_00017)
        """
        return self.written_read_nv  # Delegates to property

    def setWrittenReadNv(self, value: RefType) -> "NvBlockDataMapping":
        """
        AUTOSAR-compliant setter for writtenReadNv with method chaining.
        
        Args:
            value: The writtenReadNv to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to written_read_nv property setter (gets validation automatically)
        """
        self.written_read_nv = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bitfield_text_table(self, value: Optional["PositiveInteger"]) -> "NvBlockDataMapping":
        """
        Set bitfieldTextTable and return self for chaining.
        
        Args:
            value: The bitfieldTextTable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_bitfield_text_table("value")
        """
        self.bitfield_text_table = value  # Use property setter (gets validation)
        return self

    def with_nv_ram_block(self, value: Optional[RefType]) -> "NvBlockDataMapping":
        """
        Set nvRamBlock and return self for chaining.
        
        Args:
            value: The nvRamBlock to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_nv_ram_block("value")
        """
        self.nv_ram_block = value  # Use property setter (gets validation)
        return self

    def with_read_nv_data(self, value: Optional[RefType]) -> "NvBlockDataMapping":
        """
        Set readNvData and return self for chaining.
        
        Args:
            value: The readNvData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_read_nv_data("value")
        """
        self.read_nv_data = value  # Use property setter (gets validation)
        return self

    def with_written_nv_data(self, value: Optional[RefType]) -> "NvBlockDataMapping":
        """
        Set writtenNvData and return self for chaining.
        
        Args:
            value: The writtenNvData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_written_nv_data("value")
        """
        self.written_nv_data = value  # Use property setter (gets validation)
        return self

    def with_written_read_nv(self, value: Optional[RefType]) -> "NvBlockDataMapping":
        """
        Set writtenReadNv and return self for chaining.
        
        Args:
            value: The writtenReadNv to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_written_read_nv("value")
        """
        self.written_read_nv = value  # Use property setter (gets validation)
        return self