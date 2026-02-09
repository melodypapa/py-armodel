"""
AUTOSAR Package - NvBlockComponent

Package: M2::AUTOSARTemplates::SWComponentTemplate::NvBlockComponent
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class NvBlockDescriptor(Identifiable):
    """
    Specifies the properties of exactly on NVRAM Block.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::NvBlockComponent::NvBlockDescriptor
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 669, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The RoleBasedPortAssignement defines which client port of the
                # NvBlockSwComponentType serves for of service or notification.
        # In case of common callback function is provided by for each individual kind
                # of notification defined by of RoleBasedPortAssignment is subject with the
                # purpose to support the conditional ports.
        # atpVariation.
        self._clientServerPort: List["RoleBasedPort"] = []

    @property
    def client_server_port(self) -> List["RoleBasedPort"]:
        """Get clientServerPort (Pythonic accessor)."""
        return self._clientServerPort
        # Reference to the ConstantSpecificationMapping to be applied for the
        # particular NVRAM Block.
        self._constantValue: List["ConstantSpecification"] = []

    @property
    def constant_value(self) -> List["ConstantSpecification"]:
        """Get constantValue (Pythonic accessor)."""
        return self._constantValue
        # Reference to the DataTypeMapping to be applied for the NVRAM Block.
        self._dataType: List["RefType"] = []

    @property
    def data_type(self) -> List["RefType"]:
        """Get dataType (Pythonic accessor)."""
        return self._dataType
        # The purpose of InstantiationDataDefProps are the refinement of some data def
                # properties of individual the context of a NvBlockSw of
                # InstantiationDataDefProps is subject with the purpose to support the
                # conditional ports, component internal memory objects attributes.
        # atpVariation.
        self._instantiation: List["InstantiationDataDef"] = []

    @property
    def instantiation(self) -> List["InstantiationDataDef"]:
        """Get instantiation (Pythonic accessor)."""
        return self._instantiation
        # This represents the collection of ModeSwitchEvent TriggeredActivities related
        # to the enclosing NvBlock atpVariation 1228 Document ID 62:
        # AUTOSAR_CP_TPS_SoftwareComponentTemplate Template R23-11.
        self._modeSwitch: List["ModeSwitchEvent"] = []

    @property
    def mode_switch(self) -> List["ModeSwitchEvent"]:
        """Get modeSwitch (Pythonic accessor)."""
        return self._modeSwitch
        # Defines the mapping between the VariableData in the NvBlockComponents ports
                # and the the RAM Block.
        # of NvBlockDataMapping is subject to the purpose to support the conditional nv
                # data ports.
        # atpVariation.
        self._nvBlockData: List["RefType"] = []

    @property
    def nv_block_data(self) -> List["RefType"]:
        """Get nvBlockData (Pythonic accessor)."""
        return self._nvBlockData
        # Specifies the abstract needs on the configuration of the for the single NVRAM
                # Block described NvBlockDescriptor.
        # it may define requirements for writing an implementation of an NvBlockSw the
                # RTE.
        # that the attributes nDataSets and nRom not relevant for this aggregation
                # because the allocate just one block anyway.
        # In a different they do make sense.
        self._nvBlockNeeds: Optional["NvBlockNeeds"] = None

    @property
    def nv_block_needs(self) -> Optional["NvBlockNeeds"]:
        """Get nvBlockNeeds (Pythonic accessor)."""
        return self._nvBlockNeeds

    @nv_block_needs.setter
    def nv_block_needs(self, value: Optional["NvBlockNeeds"]) -> None:
        """
        Set nvBlockNeeds with validation.
        
        Args:
            value: The nvBlockNeeds to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nvBlockNeeds = None
            return

        if not isinstance(value, NvBlockNeeds):
            raise TypeError(
                f"nvBlockNeeds must be NvBlockNeeds or None, got {type(value).__name__}"
            )
        self._nvBlockNeeds = value
        # Defines the RAM Block of the NVRAM Block provided by.
        self._ramBlock: Optional["RefType"] = None

    @property
    def ram_block(self) -> Optional["RefType"]:
        """Get ramBlock (Pythonic accessor)."""
        return self._ramBlock

    @ram_block.setter
    def ram_block(self, value: Optional["RefType"]) -> None:
        """
        Set ramBlock with validation.
        
        Args:
            value: The ramBlock to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ramBlock = None
            return

        self._ramBlock = value
        # Defines the ROM Block of the NVRAM Block provided by.
        self._romBlock: Optional["ParameterData"] = None

    @property
    def rom_block(self) -> Optional["ParameterData"]:
        """Get romBlock (Pythonic accessor)."""
        return self._romBlock

    @rom_block.setter
    def rom_block(self, value: Optional["ParameterData"]) -> None:
        """
        Set romBlock with validation.
        
        Args:
            value: The romBlock to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._romBlock = None
            return

        if not isinstance(value, ParameterData):
            raise TypeError(
                f"romBlock must be ParameterData or None, got {type(value).__name__}"
            )
        self._romBlock = value
        # Specifies whether calling of NvM functions for writing and/ status control of
        # potentially modified RAM Blocks to NV be controlled by the RTE.
        self._supportDirty: Optional["Boolean"] = None

    @property
    def support_dirty(self) -> Optional["Boolean"]:
        """Get supportDirty (Pythonic accessor)."""
        return self._supportDirty

    @support_dirty.setter
    def support_dirty(self, value: Optional["Boolean"]) -> None:
        """
        Set supportDirty with validation.
        
        Args:
            value: The supportDirty to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supportDirty = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"supportDirty must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._supportDirty = value
        # this reference can be taken to identify the TimingEvent to by the RTE for
        # implementing a cyclic writing this block.
        self._timingEvent: Optional["TimingEvent"] = None

    @property
    def timing_event(self) -> Optional["TimingEvent"]:
        """Get timingEvent (Pythonic accessor)."""
        return self._timingEvent

    @timing_event.setter
    def timing_event(self, value: Optional["TimingEvent"]) -> None:
        """
        Set timingEvent with validation.
        
        Args:
            value: The timingEvent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timingEvent = None
            return

        if not isinstance(value, TimingEvent):
            raise TypeError(
                f"timingEvent must be TimingEvent or None, got {type(value).__name__}"
            )
        self._timingEvent = value
        # This attribute allows for assigning a specific writing for an incoming
        # AutosarDataPrototype.
        self._writingStrategy: List["RoleBasedData"] = []

    @property
    def writing_strategy(self) -> List["RoleBasedData"]:
        """Get writingStrategy (Pythonic accessor)."""
        return self._writingStrategy

    def with_client_server_port(self, value):
        """
        Set client_server_port and return self for chaining.

        Args:
            value: The client_server_port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_client_server_port("value")
        """
        self.client_server_port = value  # Use property setter (gets validation)
        return self

    def with_constant_value(self, value):
        """
        Set constant_value and return self for chaining.

        Args:
            value: The constant_value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_constant_value("value")
        """
        self.constant_value = value  # Use property setter (gets validation)
        return self

    def with_data_type(self, value):
        """
        Set data_type and return self for chaining.

        Args:
            value: The data_type to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_type("value")
        """
        self.data_type = value  # Use property setter (gets validation)
        return self

    def with_instantiation(self, value):
        """
        Set instantiation and return self for chaining.

        Args:
            value: The instantiation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_instantiation("value")
        """
        self.instantiation = value  # Use property setter (gets validation)
        return self

    def with_mode_switch(self, value):
        """
        Set mode_switch and return self for chaining.

        Args:
            value: The mode_switch to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_switch("value")
        """
        self.mode_switch = value  # Use property setter (gets validation)
        return self

    def with_nv_block_data(self, value):
        """
        Set nv_block_data and return self for chaining.

        Args:
            value: The nv_block_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nv_block_data("value")
        """
        self.nv_block_data = value  # Use property setter (gets validation)
        return self

    def with_writing_strategy(self, value):
        """
        Set writing_strategy and return self for chaining.

        Args:
            value: The writing_strategy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_writing_strategy("value")
        """
        self.writing_strategy = value  # Use property setter (gets validation)
        return self

    def with_nv_block_data(self, value):
        """
        Set nv_block_data and return self for chaining.

        Args:
            value: The nv_block_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nv_block_data("value")
        """
        self.nv_block_data = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClientServerPort(self) -> List["RoleBasedPort"]:
        """
        AUTOSAR-compliant getter for clientServerPort.
        
        Returns:
            The clientServerPort value
        
        Note:
            Delegates to client_server_port property (CODING_RULE_V2_00017)
        """
        return self.client_server_port  # Delegates to property

    def getConstantValue(self) -> List["ConstantSpecification"]:
        """
        AUTOSAR-compliant getter for constantValue.
        
        Returns:
            The constantValue value
        
        Note:
            Delegates to constant_value property (CODING_RULE_V2_00017)
        """
        return self.constant_value  # Delegates to property

    def getDataType(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for dataType.
        
        Returns:
            The dataType value
        
        Note:
            Delegates to data_type property (CODING_RULE_V2_00017)
        """
        return self.data_type  # Delegates to property

    def getInstantiation(self) -> List["InstantiationDataDef"]:
        """
        AUTOSAR-compliant getter for instantiation.
        
        Returns:
            The instantiation value
        
        Note:
            Delegates to instantiation property (CODING_RULE_V2_00017)
        """
        return self.instantiation  # Delegates to property

    def getModeSwitch(self) -> List["ModeSwitchEvent"]:
        """
        AUTOSAR-compliant getter for modeSwitch.
        
        Returns:
            The modeSwitch value
        
        Note:
            Delegates to mode_switch property (CODING_RULE_V2_00017)
        """
        return self.mode_switch  # Delegates to property

    def getNvBlockData(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for nvBlockData.
        
        Returns:
            The nvBlockData value
        
        Note:
            Delegates to nv_block_data property (CODING_RULE_V2_00017)
        """
        return self.nv_block_data  # Delegates to property

    def getNvBlockNeeds(self) -> "NvBlockNeeds":
        """
        AUTOSAR-compliant getter for nvBlockNeeds.
        
        Returns:
            The nvBlockNeeds value
        
        Note:
            Delegates to nv_block_needs property (CODING_RULE_V2_00017)
        """
        return self.nv_block_needs  # Delegates to property

    def setNvBlockNeeds(self, value: "NvBlockNeeds") -> "NvBlockDescriptor":
        """
        AUTOSAR-compliant setter for nvBlockNeeds with method chaining.
        
        Args:
            value: The nvBlockNeeds to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to nv_block_needs property setter (gets validation automatically)
        """
        self.nv_block_needs = value  # Delegates to property setter
        return self

    def getRamBlock(self) -> "RefType":
        """
        AUTOSAR-compliant getter for ramBlock.
        
        Returns:
            The ramBlock value
        
        Note:
            Delegates to ram_block property (CODING_RULE_V2_00017)
        """
        return self.ram_block  # Delegates to property

    def setRamBlock(self, value: "RefType") -> "NvBlockDescriptor":
        """
        AUTOSAR-compliant setter for ramBlock with method chaining.
        
        Args:
            value: The ramBlock to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ram_block property setter (gets validation automatically)
        """
        self.ram_block = value  # Delegates to property setter
        return self

    def getRomBlock(self) -> "ParameterData":
        """
        AUTOSAR-compliant getter for romBlock.
        
        Returns:
            The romBlock value
        
        Note:
            Delegates to rom_block property (CODING_RULE_V2_00017)
        """
        return self.rom_block  # Delegates to property

    def setRomBlock(self, value: "ParameterData") -> "NvBlockDescriptor":
        """
        AUTOSAR-compliant setter for romBlock with method chaining.
        
        Args:
            value: The romBlock to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rom_block property setter (gets validation automatically)
        """
        self.rom_block = value  # Delegates to property setter
        return self

    def getSupportDirty(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for supportDirty.
        
        Returns:
            The supportDirty value
        
        Note:
            Delegates to support_dirty property (CODING_RULE_V2_00017)
        """
        return self.support_dirty  # Delegates to property

    def setSupportDirty(self, value: "Boolean") -> "NvBlockDescriptor":
        """
        AUTOSAR-compliant setter for supportDirty with method chaining.
        
        Args:
            value: The supportDirty to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to support_dirty property setter (gets validation automatically)
        """
        self.support_dirty = value  # Delegates to property setter
        return self

    def getTimingEvent(self) -> "TimingEvent":
        """
        AUTOSAR-compliant getter for timingEvent.
        
        Returns:
            The timingEvent value
        
        Note:
            Delegates to timing_event property (CODING_RULE_V2_00017)
        """
        return self.timing_event  # Delegates to property

    def setTimingEvent(self, value: "TimingEvent") -> "NvBlockDescriptor":
        """
        AUTOSAR-compliant setter for timingEvent with method chaining.
        
        Args:
            value: The timingEvent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timing_event property setter (gets validation automatically)
        """
        self.timing_event = value  # Delegates to property setter
        return self

    def getWritingStrategy(self) -> List["RoleBasedData"]:
        """
        AUTOSAR-compliant getter for writingStrategy.
        
        Returns:
            The writingStrategy value
        
        Note:
            Delegates to writing_strategy property (CODING_RULE_V2_00017)
        """
        return self.writing_strategy  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nv_block_needs(self, value: Optional["NvBlockNeeds"]) -> "NvBlockDescriptor":
        """
        Set nvBlockNeeds and return self for chaining.
        
        Args:
            value: The nvBlockNeeds to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_nv_block_needs("value")
        """
        self.nv_block_needs = value  # Use property setter (gets validation)
        return self

    def with_ram_block(self, value: Optional[RefType]) -> "NvBlockDescriptor":
        """
        Set ramBlock and return self for chaining.
        
        Args:
            value: The ramBlock to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ram_block("value")
        """
        self.ram_block = value  # Use property setter (gets validation)
        return self

    def with_rom_block(self, value: Optional["ParameterData"]) -> "NvBlockDescriptor":
        """
        Set romBlock and return self for chaining.
        
        Args:
            value: The romBlock to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rom_block("value")
        """
        self.rom_block = value  # Use property setter (gets validation)
        return self

    def with_support_dirty(self, value: Optional["Boolean"]) -> "NvBlockDescriptor":
        """
        Set supportDirty and return self for chaining.
        
        Args:
            value: The supportDirty to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_support_dirty("value")
        """
        self.support_dirty = value  # Use property setter (gets validation)
        return self

    def with_timing_event(self, value: Optional["TimingEvent"]) -> "NvBlockDescriptor":
        """
        Set timingEvent and return self for chaining.
        
        Args:
            value: The timingEvent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timing_event("value")
        """
        self.timing_event = value  # Use property setter (gets validation)
        return self



class ModeSwitchEventTriggeredActivity(ARObject):
    """
    This meta-class defines an activity of the NvBlockSwComponentType for a
    specific NvBlock which is triggered by a ModeSwitchEvent.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::NvBlockComponent::ModeSwitchEventTriggeredActivity
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 675, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute indicates which service of the NvM for the be requested.
        self._role: Optional["Identifier"] = None

    @property
    def role(self) -> Optional["Identifier"]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: Optional["Identifier"]) -> None:
        """
        Set role with validation.
        
        Args:
            value: The role to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._role = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"role must be Identifier or str or None, got {type(value).__name__}"
            )
        self._role = value
        # This reference identifies the SwcModeSwitchEvent that the activity.
        self._swcModeSwitch: Optional["SwcModeSwitchEvent"] = None

    @property
    def swc_mode_switch(self) -> Optional["SwcModeSwitchEvent"]:
        """Get swcModeSwitch (Pythonic accessor)."""
        return self._swcModeSwitch

    @swc_mode_switch.setter
    def swc_mode_switch(self, value: Optional["SwcModeSwitchEvent"]) -> None:
        """
        Set swcModeSwitch with validation.
        
        Args:
            value: The swcModeSwitch to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcModeSwitch = None
            return

        if not isinstance(value, SwcModeSwitchEvent):
            raise TypeError(
                f"swcModeSwitch must be SwcModeSwitchEvent or None, got {type(value).__name__}"
            )
        self._swcModeSwitch = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRole(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for role.
        
        Returns:
            The role value
        
        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "Identifier") -> "ModeSwitchEventTriggeredActivity":
        """
        AUTOSAR-compliant setter for role with method chaining.
        
        Args:
            value: The role to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to role property setter (gets validation automatically)
        """
        self.role = value  # Delegates to property setter
        return self

    def getSwcModeSwitch(self) -> "SwcModeSwitchEvent":
        """
        AUTOSAR-compliant getter for swcModeSwitch.
        
        Returns:
            The swcModeSwitch value
        
        Note:
            Delegates to swc_mode_switch property (CODING_RULE_V2_00017)
        """
        return self.swc_mode_switch  # Delegates to property

    def setSwcModeSwitch(self, value: "SwcModeSwitchEvent") -> "ModeSwitchEventTriggeredActivity":
        """
        AUTOSAR-compliant setter for swcModeSwitch with method chaining.
        
        Args:
            value: The swcModeSwitch to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to swc_mode_switch property setter (gets validation automatically)
        """
        self.swc_mode_switch = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_role(self, value: Optional["Identifier"]) -> "ModeSwitchEventTriggeredActivity":
        """
        Set role and return self for chaining.
        
        Args:
            value: The role to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_role("value")
        """
        self.role = value  # Use property setter (gets validation)
        return self

    def with_swc_mode_switch(self, value: Optional["SwcModeSwitchEvent"]) -> "ModeSwitchEventTriggeredActivity":
        """
        Set swcModeSwitch and return self for chaining.
        
        Args:
            value: The swcModeSwitch to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_swc_mode_switch("value")
        """
        self.swc_mode_switch = value  # Use property setter (gets validation)
        return self



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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"bitfieldTextTable must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._bitfieldTextTable = value
        # Reference to a VariableDataPrototype of a RAM Block.
        self._nvRamBlock: Optional["RefType"] = None

    @property
    def nv_ram_block(self) -> Optional["RefType"]:
        """Get nvRamBlock (Pythonic accessor)."""
        return self._nvRamBlock

    @nv_ram_block.setter
    def nv_ram_block(self, value: Optional["RefType"]) -> None:
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
        self._readNvData: Optional["RefType"] = None

    @property
    def read_nv_data(self) -> Optional["RefType"]:
        """Get readNvData (Pythonic accessor)."""
        return self._readNvData

    @read_nv_data.setter
    def read_nv_data(self, value: Optional["RefType"]) -> None:
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
        self._writtenNvData: Optional["RefType"] = None

    @property
    def written_nv_data(self) -> Optional["RefType"]:
        """Get writtenNvData (Pythonic accessor)."""
        return self._writtenNvData

    @written_nv_data.setter
    def written_nv_data(self, value: Optional["RefType"]) -> None:
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
        self._writtenReadNv: Optional["RefType"] = None

    @property
    def written_read_nv(self) -> Optional["RefType"]:
        """Get writtenReadNv (Pythonic accessor)."""
        return self._writtenReadNv

    @written_read_nv.setter
    def written_read_nv(self, value: Optional["RefType"]) -> None:
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

    def getNvRamBlock(self) -> "RefType":
        """
        AUTOSAR-compliant getter for nvRamBlock.
        
        Returns:
            The nvRamBlock value
        
        Note:
            Delegates to nv_ram_block property (CODING_RULE_V2_00017)
        """
        return self.nv_ram_block  # Delegates to property

    def setNvRamBlock(self, value: "RefType") -> "NvBlockDataMapping":
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

    def getReadNvData(self) -> "RefType":
        """
        AUTOSAR-compliant getter for readNvData.
        
        Returns:
            The readNvData value
        
        Note:
            Delegates to read_nv_data property (CODING_RULE_V2_00017)
        """
        return self.read_nv_data  # Delegates to property

    def setReadNvData(self, value: "RefType") -> "NvBlockDataMapping":
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

    def getWrittenNvData(self) -> "RefType":
        """
        AUTOSAR-compliant getter for writtenNvData.
        
        Returns:
            The writtenNvData value
        
        Note:
            Delegates to written_nv_data property (CODING_RULE_V2_00017)
        """
        return self.written_nv_data  # Delegates to property

    def setWrittenNvData(self, value: "RefType") -> "NvBlockDataMapping":
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

    def getWrittenReadNv(self) -> "RefType":
        """
        AUTOSAR-compliant getter for writtenReadNv.
        
        Returns:
            The writtenReadNv value
        
        Note:
            Delegates to written_read_nv property (CODING_RULE_V2_00017)
        """
        return self.written_read_nv  # Delegates to property

    def setWrittenReadNv(self, value: "RefType") -> "NvBlockDataMapping":
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
        self._bulkNvBlock: Optional["RefType"] = None

    @property
    def bulk_nv_block(self) -> Optional["RefType"]:
        """Get bulkNvBlock (Pythonic accessor)."""
        return self._bulkNvBlock

    @bulk_nv_block.setter
    def bulk_nv_block(self, value: Optional["RefType"]) -> None:
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
        self._nvBlockData: List["RefType"] = []

    @property
    def nv_block_data(self) -> List["RefType"]:
        """Get nvBlockData (Pythonic accessor)."""
        return self._nvBlockData

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBulkNvBlock(self) -> "RefType":
        """
        AUTOSAR-compliant getter for bulkNvBlock.
        
        Returns:
            The bulkNvBlock value
        
        Note:
            Delegates to bulk_nv_block property (CODING_RULE_V2_00017)
        """
        return self.bulk_nv_block  # Delegates to property

    def setBulkNvBlock(self, value: "RefType") -> "BulkNvDataDescriptor":
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

    def getNvBlockData(self) -> List["RefType"]:
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


class RamBlockStatusControlEnum(AREnum):
    """
    RamBlockStatusControlEnum enumeration

This enumeration type defines options for how the management of the ramBlock status is controlled. Aggregated by NvBlockNeeds.ramBlockStatusControl

Package: M2::AUTOSARTemplates::SWComponentTemplate::NvBlockComponent
    """
    # The ramBlock status is controlled via service interface by usage of the SetRamBlockStatus operation.
    api = "0"

    # The ramBlock status is controlled exclusively by the Nv Ram Manager.
    nvRamManager = "1"
