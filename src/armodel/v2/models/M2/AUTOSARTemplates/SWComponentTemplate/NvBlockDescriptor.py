from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class NvBlockDescriptor(Identifiable):
    """
    Specifies the properties of exactly on NVRAM Block.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::NvBlockComponent

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
        self._dataType: List[RefType] = []

    @property
    def data_type(self) -> List[RefType]:
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
        self._nvBlockData: List[RefType] = []

    @property
    def nv_block_data(self) -> List[RefType]:
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
        self._ramBlock: RefType = None

    @property
    def ram_block(self) -> RefType:
        """Get ramBlock (Pythonic accessor)."""
        return self._ramBlock

    @ram_block.setter
    def ram_block(self, value: RefType) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"supportDirty must be Boolean or None, got {type(value).__name__}"
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

    def getDataType(self) -> List[RefType]:
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

    def getNvBlockData(self) -> List[RefType]:
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

    def getRamBlock(self) -> RefType:
        """
        AUTOSAR-compliant getter for ramBlock.

        Returns:
            The ramBlock value

        Note:
            Delegates to ram_block property (CODING_RULE_V2_00017)
        """
        return self.ram_block  # Delegates to property

    def setRamBlock(self, value: RefType) -> "NvBlockDescriptor":
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
