from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceNeeds,
)


class NvBlockNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of a single NVRAM Block.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 231, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 679, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines if CRC (re)calculation for the permanent RAM is required.
        self._calcRamBlock: Optional["Boolean"] = None

    @property
    def calc_ram_block(self) -> Optional["Boolean"]:
        """Get calcRamBlock (Pythonic accessor)."""
        return self._calcRamBlock

    @calc_ram_block.setter
    def calc_ram_block(self, value: Optional["Boolean"]) -> None:
        """
        Set calcRamBlock with validation.

        Args:
            value: The calcRamBlock to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calcRamBlock = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"calcRamBlock must be Boolean or None, got {type(value).__name__}"
            )
        self._calcRamBlock = value
        # Defines if the Static Block Id check shall be enabled.
        self._checkStatic: Optional["Boolean"] = None

    @property
    def check_static(self) -> Optional["Boolean"]:
        """Get checkStatic (Pythonic accessor)."""
        return self._checkStatic

    @check_static.setter
    def check_static(self, value: Optional["Boolean"]) -> None:
        """
        Set checkStatic with validation.

        Args:
            value: The checkStatic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._checkStatic = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"checkStatic must be Boolean or None, got {type(value).__name__}"
            )
        self._checkStatic = value
        # This represents the period for cyclic writing of NvData to the associated RAM
        # Block.
        self._cyclicWriting: Optional["TimeValue"] = None

    @property
    def cyclic_writing(self) -> Optional["TimeValue"]:
        """Get cyclicWriting (Pythonic accessor)."""
        return self._cyclicWriting

    @cyclic_writing.setter
    def cyclic_writing(self, value: Optional["TimeValue"]) -> None:
        """
        Set cyclicWriting with validation.

        Args:
            value: The cyclicWriting to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cyclicWriting = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"cyclicWriting must be TimeValue or None, got {type(value).__name__}"
            )
        self._cyclicWriting = value
        # Number of data sets to be provided by the NVRAM this block.
        # This is the total number of ROM RAM Blocks.
        self._nDataSets: Optional["PositiveInteger"] = None

    @property
    def n_data_sets(self) -> Optional["PositiveInteger"]:
        """Get nDataSets (Pythonic accessor)."""
        return self._nDataSets

    @n_data_sets.setter
    def n_data_sets(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set nDataSets with validation.

        Args:
            value: The nDataSets to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nDataSets = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"nDataSets must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._nDataSets = value
        # Number of ROM Blocks to be provided by the NVRAM this block.
        # Please note that these multiple are given in a contiguous area.
        self._nRomBlocks: Optional["PositiveInteger"] = None

    @property
    def n_rom_blocks(self) -> Optional["PositiveInteger"]:
        """Get nRomBlocks (Pythonic accessor)."""
        return self._nRomBlocks

    @n_rom_blocks.setter
    def n_rom_blocks(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set nRomBlocks with validation.

        Args:
            value: The nRomBlocks to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nRomBlocks = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"nRomBlocks must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._nRomBlocks = value
        # This attribute defines how the management of the RAM Block status is
        # controlled.
        self._ramBlockStatus: Optional["RamBlockStatusControl"] = None

    @property
    def ram_block_status(self) -> Optional["RamBlockStatusControl"]:
        """Get ramBlockStatus (Pythonic accessor)."""
        return self._ramBlockStatus

    @ram_block_status.setter
    def ram_block_status(self, value: Optional["RamBlockStatusControl"]) -> None:
        """
        Set ramBlockStatus with validation.

        Args:
            value: The ramBlockStatus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ramBlockStatus = None
            return

        if not isinstance(value, RamBlockStatusControl):
            raise TypeError(
                f"ramBlockStatus must be RamBlockStatusControl or None, got {type(value).__name__}"
            )
        self._ramBlockStatus = value
        # true: data of this NVRAM Block are write protected for (but protection can be
        # disabled) restriction 381 Document ID 89:
        # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
        # R23-11.
        self._readonly: Optional["Boolean"] = None

    @property
    def readonly(self) -> Optional["Boolean"]:
        """Get readonly (Pythonic accessor)."""
        return self._readonly

    @readonly.setter
    def readonly(self, value: Optional["Boolean"]) -> None:
        """
        Set readonly with validation.

        Args:
            value: The readonly to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._readonly = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"readonly must be Boolean or None, got {type(value).__name__}"
            )
        self._readonly = value
        # Reliability against data loss on the non-volatile medium.
        self._reliability: Optional["NvBlockNeeds"] = None

    @property
    def reliability(self) -> Optional["NvBlockNeeds"]:
        """Get reliability (Pythonic accessor)."""
        return self._reliability

    @reliability.setter
    def reliability(self, value: Optional["NvBlockNeeds"]) -> None:
        """
        Set reliability with validation.

        Args:
            value: The reliability to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._reliability = None
            return

        if not isinstance(value, NvBlockNeeds):
            raise TypeError(
                f"reliability must be NvBlockNeeds or None, got {type(value).__name__}"
            )
        self._reliability = value
        # Defines whether an NVRAM Block shall be treated to configuration changes
                # (true) or not (false).
        # For to handle initialization in the latter case, to the NVRAM specification.
        self._resistantTo: Optional["Boolean"] = None

    @property
    def resistant_to(self) -> Optional["Boolean"]:
        """Get resistantTo (Pythonic accessor)."""
        return self._resistantTo

    @resistant_to.setter
    def resistant_to(self, value: Optional["Boolean"]) -> None:
        """
        Set resistantTo with validation.

        Args:
            value: The resistantTo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resistantTo = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"resistantTo must be Boolean or None, got {type(value).__name__}"
            )
        self._resistantTo = value
        # Defines whether the associated RAM Block shall be during startup by the basic
        # software.
        self._restoreAtStart: Optional["Boolean"] = None

    @property
    def restore_at_start(self) -> Optional["Boolean"]:
        """Get restoreAtStart (Pythonic accessor)."""
        return self._restoreAtStart

    @restore_at_start.setter
    def restore_at_start(self, value: Optional["Boolean"]) -> None:
        """
        Set restoreAtStart with validation.

        Args:
            value: The restoreAtStart to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._restoreAtStart = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"restoreAtStart must be Boolean or None, got {type(value).__name__}"
            )
        self._restoreAtStart = value
        # If this attribute is set to true the NvM shall process this in the
        # NvM_FirstInitAll() function.
        self._selectBlockFor: Optional["Boolean"] = None

    @property
    def select_block_for(self) -> Optional["Boolean"]:
        """Get selectBlockFor (Pythonic accessor)."""
        return self._selectBlockFor

    @select_block_for.setter
    def select_block_for(self, value: Optional["Boolean"]) -> None:
        """
        Set selectBlockFor with validation.

        Args:
            value: The selectBlockFor to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._selectBlockFor = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"selectBlockFor must be Boolean or None, got {type(value).__name__}"
            )
        self._selectBlockFor = value
        # Defines whether or not the associated RAM Block shall be stored during
        # shutdown by the basic software.
        self._storeAt: Optional["Boolean"] = None

    @property
    def store_at(self) -> Optional["Boolean"]:
        """Get storeAt (Pythonic accessor)."""
        return self._storeAt

    @store_at.setter
    def store_at(self, value: Optional["Boolean"]) -> None:
        """
        Set storeAt with validation.

        Args:
            value: The storeAt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._storeAt = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"storeAt must be Boolean or None, got {type(value).__name__}"
            )
        self._storeAt = value
        # Defines whether or not the associated RAM Block shall stored periodically by
        # the basic software.
        self._storeCyclic: Optional["Boolean"] = None

    @property
    def store_cyclic(self) -> Optional["Boolean"]:
        """Get storeCyclic (Pythonic accessor)."""
        return self._storeCyclic

    @store_cyclic.setter
    def store_cyclic(self, value: Optional["Boolean"]) -> None:
        """
        Set storeCyclic with validation.

        Args:
            value: The storeCyclic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._storeCyclic = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"storeCyclic must be Boolean or None, got {type(value).__name__}"
            )
        self._storeCyclic = value
        # Defines whether or not the associated RAM Block shall implicitly stored in
                # case of ECU failure (e.
        # g.
        # loss of the basic software.
        # If the attribute store set to true the associated RAM Block shall to have
                # immediate priority.
        self._store: Optional["Boolean"] = None

    @property
    def store(self) -> Optional["Boolean"]:
        """Get store (Pythonic accessor)."""
        return self._store

    @store.setter
    def store(self, value: Optional["Boolean"]) -> None:
        """
        Set store with validation.

        Args:
            value: The store to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._store = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"store must be Boolean or None, got {type(value).__name__}"
            )
        self._store = value
        # Defines whether or not the associated RAM Block shall stored immediately
        # during or after execution according SW-C RunnableEntity by the basic.
        self._storeImmediate: Optional["Boolean"] = None

    @property
    def store_immediate(self) -> Optional["Boolean"]:
        """Get storeImmediate (Pythonic accessor)."""
        return self._storeImmediate

    @store_immediate.setter
    def store_immediate(self, value: Optional["Boolean"]) -> None:
        """
        Set storeImmediate with validation.

        Args:
            value: The storeImmediate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._storeImmediate = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"storeImmediate must be Boolean or None, got {type(value).__name__}"
            )
        self._storeImmediate = value
        # This attribute defines whether the associated RAM Block stored immediately if
        # the written value is different value stored in the associated RAM Block(s)
        # during execution of the according SW-C RunnableEntity.
        self._storeOnChange: Optional["Boolean"] = None

    @property
    def store_on_change(self) -> Optional["Boolean"]:
        """Get storeOnChange (Pythonic accessor)."""
        return self._storeOnChange

    @store_on_change.setter
    def store_on_change(self, value: Optional["Boolean"]) -> None:
        """
        Set storeOnChange with validation.

        Args:
            value: The storeOnChange to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._storeOnChange = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"storeOnChange must be Boolean or None, got {type(value).__name__}"
            )
        self._storeOnChange = value
        # If set to true the RAM Block shall be auto validated during phase.
        self._useAuto: Optional["Boolean"] = None

    @property
    def use_auto(self) -> Optional["Boolean"]:
        """Get useAuto (Pythonic accessor)."""
        return self._useAuto

    @use_auto.setter
    def use_auto(self, value: Optional["Boolean"]) -> None:
        """
        Set useAuto with validation.

        Args:
            value: The useAuto to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useAuto = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"useAuto must be Boolean or None, got {type(value).__name__}"
            )
        self._useAuto = value
        # If set to true the CRC of the RAM Block shall be during a write job with the
        # CRC which was the last successful read or write job in skip unnecessary NVRAM
        # writings.
        self._useCRCComp: Optional["Boolean"] = None

    @property
    def use_crc_comp(self) -> Optional["Boolean"]:
        """Get useCRCComp (Pythonic accessor)."""
        return self._useCRCComp

    @use_crc_comp.setter
    def use_crc_comp(self, value: Optional["Boolean"]) -> None:
        """
        Set useCRCComp with validation.

        Args:
            value: The useCRCComp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useCRCComp = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"useCRCComp must be Boolean or None, got {type(value).__name__}"
            )
        self._useCRCComp = value
        # Defines write protection after first write: block is prevented from being
                # changed/erased replaced with the default ROM data after first the
                # software-component.
        # such restriction.
        self._writeOnlyOnce: Optional["Boolean"] = None

    @property
    def write_only_once(self) -> Optional["Boolean"]:
        """Get writeOnlyOnce (Pythonic accessor)."""
        return self._writeOnlyOnce

    @write_only_once.setter
    def write_only_once(self, value: Optional["Boolean"]) -> None:
        """
        Set writeOnlyOnce with validation.

        Args:
            value: The writeOnlyOnce to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._writeOnlyOnce = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"writeOnlyOnce must be Boolean or None, got {type(value).__name__}"
            )
        self._writeOnlyOnce = value
        # Defines if Write Verification shall be enabled for this.
        self._writeVerification: Optional["Boolean"] = None

    @property
    def write_verification(self) -> Optional["Boolean"]:
        """Get writeVerification (Pythonic accessor)."""
        return self._writeVerification

    @write_verification.setter
    def write_verification(self, value: Optional["Boolean"]) -> None:
        """
        Set writeVerification with validation.

        Args:
            value: The writeVerification to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._writeVerification = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"writeVerification must be Boolean or None, got {type(value).__name__}"
            )
        self._writeVerification = value
        # Provides the amount of updates to this block from the point of view.
        # It has to be provided in "number access per year".
        self._writing: Optional["PositiveInteger"] = None

    @property
    def writing(self) -> Optional["PositiveInteger"]:
        """Get writing (Pythonic accessor)."""
        return self._writing

    @writing.setter
    def writing(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set writing with validation.

        Args:
            value: The writing to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._writing = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"writing must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._writing = value
        # Requires the priority of writing this block in case of requests to write
        # other blocks.
        self._writingPriority: Optional["NvBlockNeedsWriting"] = None

    @property
    def writing_priority(self) -> Optional["NvBlockNeedsWriting"]:
        """Get writingPriority (Pythonic accessor)."""
        return self._writingPriority

    @writing_priority.setter
    def writing_priority(self, value: Optional["NvBlockNeedsWriting"]) -> None:
        """
        Set writingPriority with validation.

        Args:
            value: The writingPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._writingPriority = None
            return

        if not isinstance(value, NvBlockNeedsWriting):
            raise TypeError(
                f"writingPriority must be NvBlockNeedsWriting or None, got {type(value).__name__}"
            )
        self._writingPriority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalcRamBlock(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for calcRamBlock.

        Returns:
            The calcRamBlock value

        Note:
            Delegates to calc_ram_block property (CODING_RULE_V2_00017)
        """
        return self.calc_ram_block  # Delegates to property

    def setCalcRamBlock(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for calcRamBlock with method chaining.

        Args:
            value: The calcRamBlock to set

        Returns:
            self for method chaining

        Note:
            Delegates to calc_ram_block property setter (gets validation automatically)
        """
        self.calc_ram_block = value  # Delegates to property setter
        return self

    def getCheckStatic(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for checkStatic.

        Returns:
            The checkStatic value

        Note:
            Delegates to check_static property (CODING_RULE_V2_00017)
        """
        return self.check_static  # Delegates to property

    def setCheckStatic(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for checkStatic with method chaining.

        Args:
            value: The checkStatic to set

        Returns:
            self for method chaining

        Note:
            Delegates to check_static property setter (gets validation automatically)
        """
        self.check_static = value  # Delegates to property setter
        return self

    def getCyclicWriting(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for cyclicWriting.

        Returns:
            The cyclicWriting value

        Note:
            Delegates to cyclic_writing property (CODING_RULE_V2_00017)
        """
        return self.cyclic_writing  # Delegates to property

    def setCyclicWriting(self, value: "TimeValue") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for cyclicWriting with method chaining.

        Args:
            value: The cyclicWriting to set

        Returns:
            self for method chaining

        Note:
            Delegates to cyclic_writing property setter (gets validation automatically)
        """
        self.cyclic_writing = value  # Delegates to property setter
        return self

    def getNDataSets(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for nDataSets.

        Returns:
            The nDataSets value

        Note:
            Delegates to n_data_sets property (CODING_RULE_V2_00017)
        """
        return self.n_data_sets  # Delegates to property

    def setNDataSets(self, value: "PositiveInteger") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for nDataSets with method chaining.

        Args:
            value: The nDataSets to set

        Returns:
            self for method chaining

        Note:
            Delegates to n_data_sets property setter (gets validation automatically)
        """
        self.n_data_sets = value  # Delegates to property setter
        return self

    def getNRomBlocks(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for nRomBlocks.

        Returns:
            The nRomBlocks value

        Note:
            Delegates to n_rom_blocks property (CODING_RULE_V2_00017)
        """
        return self.n_rom_blocks  # Delegates to property

    def setNRomBlocks(self, value: "PositiveInteger") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for nRomBlocks with method chaining.

        Args:
            value: The nRomBlocks to set

        Returns:
            self for method chaining

        Note:
            Delegates to n_rom_blocks property setter (gets validation automatically)
        """
        self.n_rom_blocks = value  # Delegates to property setter
        return self

    def getRamBlockStatus(self) -> "RamBlockStatusControl":
        """
        AUTOSAR-compliant getter for ramBlockStatus.

        Returns:
            The ramBlockStatus value

        Note:
            Delegates to ram_block_status property (CODING_RULE_V2_00017)
        """
        return self.ram_block_status  # Delegates to property

    def setRamBlockStatus(self, value: "RamBlockStatusControl") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for ramBlockStatus with method chaining.

        Args:
            value: The ramBlockStatus to set

        Returns:
            self for method chaining

        Note:
            Delegates to ram_block_status property setter (gets validation automatically)
        """
        self.ram_block_status = value  # Delegates to property setter
        return self

    def getReadonly(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for readonly.

        Returns:
            The readonly value

        Note:
            Delegates to readonly property (CODING_RULE_V2_00017)
        """
        return self.readonly  # Delegates to property

    def setReadonly(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for readonly with method chaining.

        Args:
            value: The readonly to set

        Returns:
            self for method chaining

        Note:
            Delegates to readonly property setter (gets validation automatically)
        """
        self.readonly = value  # Delegates to property setter
        return self

    def getReliability(self) -> "NvBlockNeeds":
        """
        AUTOSAR-compliant getter for reliability.

        Returns:
            The reliability value

        Note:
            Delegates to reliability property (CODING_RULE_V2_00017)
        """
        return self.reliability  # Delegates to property

    def setReliability(self, value: "NvBlockNeeds") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for reliability with method chaining.

        Args:
            value: The reliability to set

        Returns:
            self for method chaining

        Note:
            Delegates to reliability property setter (gets validation automatically)
        """
        self.reliability = value  # Delegates to property setter
        return self

    def getResistantTo(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for resistantTo.

        Returns:
            The resistantTo value

        Note:
            Delegates to resistant_to property (CODING_RULE_V2_00017)
        """
        return self.resistant_to  # Delegates to property

    def setResistantTo(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for resistantTo with method chaining.

        Args:
            value: The resistantTo to set

        Returns:
            self for method chaining

        Note:
            Delegates to resistant_to property setter (gets validation automatically)
        """
        self.resistant_to = value  # Delegates to property setter
        return self

    def getRestoreAtStart(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for restoreAtStart.

        Returns:
            The restoreAtStart value

        Note:
            Delegates to restore_at_start property (CODING_RULE_V2_00017)
        """
        return self.restore_at_start  # Delegates to property

    def setRestoreAtStart(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for restoreAtStart with method chaining.

        Args:
            value: The restoreAtStart to set

        Returns:
            self for method chaining

        Note:
            Delegates to restore_at_start property setter (gets validation automatically)
        """
        self.restore_at_start = value  # Delegates to property setter
        return self

    def getSelectBlockFor(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for selectBlockFor.

        Returns:
            The selectBlockFor value

        Note:
            Delegates to select_block_for property (CODING_RULE_V2_00017)
        """
        return self.select_block_for  # Delegates to property

    def setSelectBlockFor(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for selectBlockFor with method chaining.

        Args:
            value: The selectBlockFor to set

        Returns:
            self for method chaining

        Note:
            Delegates to select_block_for property setter (gets validation automatically)
        """
        self.select_block_for = value  # Delegates to property setter
        return self

    def getStoreAt(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for storeAt.

        Returns:
            The storeAt value

        Note:
            Delegates to store_at property (CODING_RULE_V2_00017)
        """
        return self.store_at  # Delegates to property

    def setStoreAt(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for storeAt with method chaining.

        Args:
            value: The storeAt to set

        Returns:
            self for method chaining

        Note:
            Delegates to store_at property setter (gets validation automatically)
        """
        self.store_at = value  # Delegates to property setter
        return self

    def getStoreCyclic(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for storeCyclic.

        Returns:
            The storeCyclic value

        Note:
            Delegates to store_cyclic property (CODING_RULE_V2_00017)
        """
        return self.store_cyclic  # Delegates to property

    def setStoreCyclic(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for storeCyclic with method chaining.

        Args:
            value: The storeCyclic to set

        Returns:
            self for method chaining

        Note:
            Delegates to store_cyclic property setter (gets validation automatically)
        """
        self.store_cyclic = value  # Delegates to property setter
        return self

    def getStore(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for store.

        Returns:
            The store value

        Note:
            Delegates to store property (CODING_RULE_V2_00017)
        """
        return self.store  # Delegates to property

    def setStore(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for store with method chaining.

        Args:
            value: The store to set

        Returns:
            self for method chaining

        Note:
            Delegates to store property setter (gets validation automatically)
        """
        self.store = value  # Delegates to property setter
        return self

    def getStoreImmediate(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for storeImmediate.

        Returns:
            The storeImmediate value

        Note:
            Delegates to store_immediate property (CODING_RULE_V2_00017)
        """
        return self.store_immediate  # Delegates to property

    def setStoreImmediate(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for storeImmediate with method chaining.

        Args:
            value: The storeImmediate to set

        Returns:
            self for method chaining

        Note:
            Delegates to store_immediate property setter (gets validation automatically)
        """
        self.store_immediate = value  # Delegates to property setter
        return self

    def getStoreOnChange(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for storeOnChange.

        Returns:
            The storeOnChange value

        Note:
            Delegates to store_on_change property (CODING_RULE_V2_00017)
        """
        return self.store_on_change  # Delegates to property

    def setStoreOnChange(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for storeOnChange with method chaining.

        Args:
            value: The storeOnChange to set

        Returns:
            self for method chaining

        Note:
            Delegates to store_on_change property setter (gets validation automatically)
        """
        self.store_on_change = value  # Delegates to property setter
        return self

    def getUseAuto(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useAuto.

        Returns:
            The useAuto value

        Note:
            Delegates to use_auto property (CODING_RULE_V2_00017)
        """
        return self.use_auto  # Delegates to property

    def setUseAuto(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for useAuto with method chaining.

        Args:
            value: The useAuto to set

        Returns:
            self for method chaining

        Note:
            Delegates to use_auto property setter (gets validation automatically)
        """
        self.use_auto = value  # Delegates to property setter
        return self

    def getUseCRCComp(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useCRCComp.

        Returns:
            The useCRCComp value

        Note:
            Delegates to use_crc_comp property (CODING_RULE_V2_00017)
        """
        return self.use_crc_comp  # Delegates to property

    def setUseCRCComp(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for useCRCComp with method chaining.

        Args:
            value: The useCRCComp to set

        Returns:
            self for method chaining

        Note:
            Delegates to use_crc_comp property setter (gets validation automatically)
        """
        self.use_crc_comp = value  # Delegates to property setter
        return self

    def getWriteOnlyOnce(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for writeOnlyOnce.

        Returns:
            The writeOnlyOnce value

        Note:
            Delegates to write_only_once property (CODING_RULE_V2_00017)
        """
        return self.write_only_once  # Delegates to property

    def setWriteOnlyOnce(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for writeOnlyOnce with method chaining.

        Args:
            value: The writeOnlyOnce to set

        Returns:
            self for method chaining

        Note:
            Delegates to write_only_once property setter (gets validation automatically)
        """
        self.write_only_once = value  # Delegates to property setter
        return self

    def getWriteVerification(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for writeVerification.

        Returns:
            The writeVerification value

        Note:
            Delegates to write_verification property (CODING_RULE_V2_00017)
        """
        return self.write_verification  # Delegates to property

    def setWriteVerification(self, value: "Boolean") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for writeVerification with method chaining.

        Args:
            value: The writeVerification to set

        Returns:
            self for method chaining

        Note:
            Delegates to write_verification property setter (gets validation automatically)
        """
        self.write_verification = value  # Delegates to property setter
        return self

    def getWriting(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for writing.

        Returns:
            The writing value

        Note:
            Delegates to writing property (CODING_RULE_V2_00017)
        """
        return self.writing  # Delegates to property

    def setWriting(self, value: "PositiveInteger") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for writing with method chaining.

        Args:
            value: The writing to set

        Returns:
            self for method chaining

        Note:
            Delegates to writing property setter (gets validation automatically)
        """
        self.writing = value  # Delegates to property setter
        return self

    def getWritingPriority(self) -> "NvBlockNeedsWriting":
        """
        AUTOSAR-compliant getter for writingPriority.

        Returns:
            The writingPriority value

        Note:
            Delegates to writing_priority property (CODING_RULE_V2_00017)
        """
        return self.writing_priority  # Delegates to property

    def setWritingPriority(self, value: "NvBlockNeedsWriting") -> "NvBlockNeeds":
        """
        AUTOSAR-compliant setter for writingPriority with method chaining.

        Args:
            value: The writingPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to writing_priority property setter (gets validation automatically)
        """
        self.writing_priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_calc_ram_block(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set calcRamBlock and return self for chaining.

        Args:
            value: The calcRamBlock to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_calc_ram_block("value")
        """
        self.calc_ram_block = value  # Use property setter (gets validation)
        return self

    def with_check_static(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set checkStatic and return self for chaining.

        Args:
            value: The checkStatic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_check_static("value")
        """
        self.check_static = value  # Use property setter (gets validation)
        return self

    def with_cyclic_writing(self, value: Optional["TimeValue"]) -> "NvBlockNeeds":
        """
        Set cyclicWriting and return self for chaining.

        Args:
            value: The cyclicWriting to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cyclic_writing("value")
        """
        self.cyclic_writing = value  # Use property setter (gets validation)
        return self

    def with_n_data_sets(self, value: Optional["PositiveInteger"]) -> "NvBlockNeeds":
        """
        Set nDataSets and return self for chaining.

        Args:
            value: The nDataSets to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_n_data_sets("value")
        """
        self.n_data_sets = value  # Use property setter (gets validation)
        return self

    def with_n_rom_blocks(self, value: Optional["PositiveInteger"]) -> "NvBlockNeeds":
        """
        Set nRomBlocks and return self for chaining.

        Args:
            value: The nRomBlocks to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_n_rom_blocks("value")
        """
        self.n_rom_blocks = value  # Use property setter (gets validation)
        return self

    def with_ram_block_status(self, value: Optional["RamBlockStatusControl"]) -> "NvBlockNeeds":
        """
        Set ramBlockStatus and return self for chaining.

        Args:
            value: The ramBlockStatus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ram_block_status("value")
        """
        self.ram_block_status = value  # Use property setter (gets validation)
        return self

    def with_readonly(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set readonly and return self for chaining.

        Args:
            value: The readonly to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_readonly("value")
        """
        self.readonly = value  # Use property setter (gets validation)
        return self

    def with_reliability(self, value: Optional["NvBlockNeeds"]) -> "NvBlockNeeds":
        """
        Set reliability and return self for chaining.

        Args:
            value: The reliability to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reliability("value")
        """
        self.reliability = value  # Use property setter (gets validation)
        return self

    def with_resistant_to(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set resistantTo and return self for chaining.

        Args:
            value: The resistantTo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_resistant_to("value")
        """
        self.resistant_to = value  # Use property setter (gets validation)
        return self

    def with_restore_at_start(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set restoreAtStart and return self for chaining.

        Args:
            value: The restoreAtStart to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_restore_at_start("value")
        """
        self.restore_at_start = value  # Use property setter (gets validation)
        return self

    def with_select_block_for(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set selectBlockFor and return self for chaining.

        Args:
            value: The selectBlockFor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_select_block_for("value")
        """
        self.select_block_for = value  # Use property setter (gets validation)
        return self

    def with_store_at(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set storeAt and return self for chaining.

        Args:
            value: The storeAt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_store_at("value")
        """
        self.store_at = value  # Use property setter (gets validation)
        return self

    def with_store_cyclic(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set storeCyclic and return self for chaining.

        Args:
            value: The storeCyclic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_store_cyclic("value")
        """
        self.store_cyclic = value  # Use property setter (gets validation)
        return self

    def with_store(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set store and return self for chaining.

        Args:
            value: The store to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_store("value")
        """
        self.store = value  # Use property setter (gets validation)
        return self

    def with_store_immediate(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set storeImmediate and return self for chaining.

        Args:
            value: The storeImmediate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_store_immediate("value")
        """
        self.store_immediate = value  # Use property setter (gets validation)
        return self

    def with_store_on_change(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set storeOnChange and return self for chaining.

        Args:
            value: The storeOnChange to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_store_on_change("value")
        """
        self.store_on_change = value  # Use property setter (gets validation)
        return self

    def with_use_auto(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set useAuto and return self for chaining.

        Args:
            value: The useAuto to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_use_auto("value")
        """
        self.use_auto = value  # Use property setter (gets validation)
        return self

    def with_use_crc_comp(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set useCRCComp and return self for chaining.

        Args:
            value: The useCRCComp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_use_crc_comp("value")
        """
        self.use_crc_comp = value  # Use property setter (gets validation)
        return self

    def with_write_only_once(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set writeOnlyOnce and return self for chaining.

        Args:
            value: The writeOnlyOnce to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_write_only_once("value")
        """
        self.write_only_once = value  # Use property setter (gets validation)
        return self

    def with_write_verification(self, value: Optional["Boolean"]) -> "NvBlockNeeds":
        """
        Set writeVerification and return self for chaining.

        Args:
            value: The writeVerification to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_write_verification("value")
        """
        self.write_verification = value  # Use property setter (gets validation)
        return self

    def with_writing(self, value: Optional["PositiveInteger"]) -> "NvBlockNeeds":
        """
        Set writing and return self for chaining.

        Args:
            value: The writing to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_writing("value")
        """
        self.writing = value  # Use property setter (gets validation)
        return self

    def with_writing_priority(self, value: Optional["NvBlockNeedsWriting"]) -> "NvBlockNeeds":
        """
        Set writingPriority and return self for chaining.

        Args:
            value: The writingPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_writing_priority("value")
        """
        self.writing_priority = value  # Use property setter (gets validation)
        return self
