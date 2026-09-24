CLASS_NOTE = (
    "Defines the mapping between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the RAM Block. "
    "The data types of the referenced VariableDataPrototypes in the ports and the referenced sub-element (inside a CompositeDataType) of the VariableDataPrototype representing the RAM Block shall be compatible."
)
BITFIELD_MASK_NV_BLOCK_NOTE = "This attribute identifies the applicable bit mask on the side of the Nv Block."
BITFIELD_MASK_PORT_NOTE = "This attribute identifies the applicable bit mask on the side of the PortPrototype."
NV_RAM_BLOCK_ELEMENT_NOTE = "Reference to a VariableDataPrototype of a RAM Block."
READ_NV_DATA_NOTE = (
    "Reference to a VariableDataPrototype of a pPort of the NvBlockComponent providing read access to the RAM Block."
    "If there is no PortPrototype providing read access (write-only) the reference can be omitted."
)
WRITTEN_NV_DATA_NOTE = (
    "Reference to a VariableDataPrototype of a rPort of the NvBlockComponent providing write access to the RAM Block. "
    "If there is no port providing write access (read-only) the reference can be omitted."
)
WRITTEN_READ_NV_DATA_NOTE = "Reference to a VariableDataPrototype of a PRPortPrototype of the NvBlockSwComponentType providing write and read access to the RAM Block."

BULK_DESCRIPTOR_CLASS_NOTE = (
    "This meta-class represents one bulk NV Data Block that is read-only for the application software. "
    "The purpose of a bulk NV Data Block is to provide access to information uploaded to the vehicle at e.g. the end of the production line."
)
BULK_NV_BLOCK_NOTE = "This aggregation represents the actual bulk NVBlock."
BULK_NV_BLOCK_DATA_MAPPING_NOTE = (
    "Defines the mapping between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the non-volatile memory. "
    "The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports."
)


def _positive_integer(value):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

    integer = PositiveInteger()
    integer.setValue(str(value))
    return integer


def _ref(value, dest):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _variable_ref(port_value):
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarVariableRef
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import (
        VariableInAtomicSWCTypeInstanceRef,
    )

    ref = AutosarVariableRef()
    iref = VariableInAtomicSWCTypeInstanceRef()
    iref.setPortPrototypeRef(_ref(port_value, "PORT-PROTOTYPE"))
    ref.setAutosarVariableIRef(iref)
    return ref


class TestNvBlockDataMapping:
    def test_spec_notes_are_verbatim(self):
        """Test that the class docstring and every accessor docstring is the spec Note verbatim (Table 11.11)"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        assert NvBlockDataMapping.__doc__.strip() == CLASS_NOTE
        assert NvBlockDataMapping.getBitfieldTextTableMaskNvBlockDescriptor.__doc__.strip() == BITFIELD_MASK_NV_BLOCK_NOTE
        assert NvBlockDataMapping.setBitfieldTextTableMaskNvBlockDescriptor.__doc__.strip() == (
            BITFIELD_MASK_NV_BLOCK_NOTE + " A None value is a no-op and does not overwrite an existing bitfieldTextTableMaskNvBlockDescriptor."
        )
        assert NvBlockDataMapping.getBitfieldTextTableMaskPortPrototype.__doc__.strip() == BITFIELD_MASK_PORT_NOTE
        assert NvBlockDataMapping.setBitfieldTextTableMaskPortPrototype.__doc__.strip() == (
            BITFIELD_MASK_PORT_NOTE + " A None value is a no-op and does not overwrite an existing bitfieldTextTableMaskPortPrototype."
        )
        assert NvBlockDataMapping.getNvRamBlockElement.__doc__.strip() == NV_RAM_BLOCK_ELEMENT_NOTE
        assert NvBlockDataMapping.setNvRamBlockElement.__doc__.strip() == (NV_RAM_BLOCK_ELEMENT_NOTE + " A None value is a no-op and does not overwrite an existing nvRamBlockElement.")
        assert NvBlockDataMapping.getReadNvData.__doc__.strip() == READ_NV_DATA_NOTE
        assert NvBlockDataMapping.setReadNvData.__doc__.strip() == (READ_NV_DATA_NOTE + " A None value is a no-op and does not overwrite an existing readNvData.")
        assert NvBlockDataMapping.getWrittenNvData.__doc__.strip() == WRITTEN_NV_DATA_NOTE
        assert NvBlockDataMapping.setWrittenNvData.__doc__.strip() == (WRITTEN_NV_DATA_NOTE + " A None value is a no-op and does not overwrite an existing writtenNvData.")
        assert NvBlockDataMapping.getWrittenReadNvData.__doc__.strip() == WRITTEN_READ_NV_DATA_NOTE
        assert NvBlockDataMapping.setWrittenReadNvData.__doc__.strip() == (WRITTEN_READ_NV_DATA_NOTE + " A None value is a no-op and does not overwrite an existing writtenReadNvData.")

    def test_base_shape(self):
        """Test the base chain, no-arg __init__ and typed accessor signatures"""
        import typing

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarVariableRef

        assert issubclass(NvBlockDataMapping, ARObject)
        assert issubclass(NvBlockDataMapping, VariationPointCapable)
        assert NvBlockDataMapping().bitfieldTextTableMaskNvBlockDescriptor is None

        hints = typing.get_type_hints(NvBlockDataMapping.getBitfieldTextTableMaskNvBlockDescriptor)
        assert hints["return"] == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(NvBlockDataMapping.setBitfieldTextTableMaskNvBlockDescriptor)
        assert hints["value"] == typing.Optional[PositiveInteger]
        assert hints["return"] is NvBlockDataMapping
        hints = typing.get_type_hints(NvBlockDataMapping.getBitfieldTextTableMaskPortPrototype)
        assert hints["return"] == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(NvBlockDataMapping.setBitfieldTextTableMaskPortPrototype)
        assert hints["value"] == typing.Optional[PositiveInteger]
        assert hints["return"] is NvBlockDataMapping
        for getter, setter in [
            (NvBlockDataMapping.getNvRamBlockElement, NvBlockDataMapping.setNvRamBlockElement),
            (NvBlockDataMapping.getReadNvData, NvBlockDataMapping.setReadNvData),
            (NvBlockDataMapping.getWrittenNvData, NvBlockDataMapping.setWrittenNvData),
            (NvBlockDataMapping.getWrittenReadNvData, NvBlockDataMapping.setWrittenReadNvData),
        ]:
            assert typing.get_type_hints(getter)["return"] == typing.Optional[AutosarVariableRef]
            hints = typing.get_type_hints(setter)
            assert hints["value"] == typing.Optional[AutosarVariableRef]
            assert hints["return"] is NvBlockDataMapping

    def test_initialization(self):
        """Test NvBlockDataMapping initialization"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        mapping = NvBlockDataMapping()

        assert mapping is not None
        assert mapping.bitfieldTextTableMaskNvBlockDescriptor is None
        assert mapping.bitfieldTextTableMaskPortPrototype is None
        assert mapping.nvRamBlockElement is None
        assert mapping.readNvData is None
        assert mapping.writtenNvData is None
        assert mapping.writtenReadNvData is None

    def test_get_set_bitfield_text_table_mask_nv_block_descriptor(self):
        """Test getBitfieldTextTableMaskNvBlockDescriptor and setBitfieldTextTableMaskNvBlockDescriptor methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        mapping = NvBlockDataMapping()

        assert mapping.getBitfieldTextTableMaskNvBlockDescriptor() is None
        mask = _positive_integer(10)
        assert mapping.setBitfieldTextTableMaskNvBlockDescriptor(mask) is mapping
        assert mapping.getBitfieldTextTableMaskNvBlockDescriptor() is mask
        assert mapping.getBitfieldTextTableMaskNvBlockDescriptor().getValue() == 10
        mapping.setBitfieldTextTableMaskNvBlockDescriptor(None)
        assert mapping.getBitfieldTextTableMaskNvBlockDescriptor() is mask

    def test_get_set_bitfield_text_table_mask_port_prototype(self):
        """Test getBitfieldTextTableMaskPortPrototype and setBitfieldTextTableMaskPortPrototype methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        mapping = NvBlockDataMapping()

        assert mapping.getBitfieldTextTableMaskPortPrototype() is None
        mask = _positive_integer(32)
        assert mapping.setBitfieldTextTableMaskPortPrototype(mask) is mapping
        assert mapping.getBitfieldTextTableMaskPortPrototype() is mask
        assert mapping.getBitfieldTextTableMaskPortPrototype().getValue() == 32
        mapping.setBitfieldTextTableMaskPortPrototype(None)
        assert mapping.getBitfieldTextTableMaskPortPrototype() is mask

    def test_get_set_nv_ram_block_element(self):
        """Test getNvRamBlockElement and setNvRamBlockElement methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        mapping = NvBlockDataMapping()

        assert mapping.getNvRamBlockElement() is None
        ref = _variable_ref("/ramPP")
        assert mapping.setNvRamBlockElement(ref) is mapping
        assert mapping.getNvRamBlockElement() is ref
        assert mapping.getNvRamBlockElement().getAutosarVariableIRef().getPortPrototypeRef().getValue() == "/ramPP"
        mapping.setNvRamBlockElement(None)
        assert mapping.getNvRamBlockElement() is ref

    def test_get_set_read_nv_data(self):
        """Test getReadNvData and setReadNvData methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        mapping = NvBlockDataMapping()

        assert mapping.getReadNvData() is None
        ref = _variable_ref("/readPP")
        assert mapping.setReadNvData(ref) is mapping
        assert mapping.getReadNvData() is ref
        assert mapping.getReadNvData().getAutosarVariableIRef().getPortPrototypeRef().getValue() == "/readPP"
        mapping.setReadNvData(None)
        assert mapping.getReadNvData() is ref

    def test_get_set_written_nv_data(self):
        """Test getWrittenNvData and setWrittenNvData methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        mapping = NvBlockDataMapping()

        assert mapping.getWrittenNvData() is None
        ref = _variable_ref("/writtenPP")
        assert mapping.setWrittenNvData(ref) is mapping
        assert mapping.getWrittenNvData() is ref
        assert mapping.getWrittenNvData().getAutosarVariableIRef().getPortPrototypeRef().getValue() == "/writtenPP"
        mapping.setWrittenNvData(None)
        assert mapping.getWrittenNvData() is ref

    def test_get_set_written_read_nv_data(self):
        """Test getWrittenReadNvData and setWrittenReadNvData methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        mapping = NvBlockDataMapping()

        assert mapping.getWrittenReadNvData() is None
        ref = _variable_ref("/writtenReadPRPort")
        assert mapping.setWrittenReadNvData(ref) is mapping
        assert mapping.getWrittenReadNvData() is ref
        assert mapping.getWrittenReadNvData().getAutosarVariableIRef().getPortPrototypeRef().getValue() == "/writtenReadPRPort"
        mapping.setWrittenReadNvData(None)
        assert mapping.getWrittenReadNvData() is ref


class TestBulkNvDataDescriptor:
    def test_spec_notes_are_verbatim(self):
        """Test that the class docstring and every accessor docstring is the spec Note verbatim (Table 11.12)"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor

        assert BulkNvDataDescriptor.__doc__.strip() == BULK_DESCRIPTOR_CLASS_NOTE
        assert BulkNvDataDescriptor.createBulkNvBlock.__doc__.strip() == BULK_NV_BLOCK_NOTE
        assert BulkNvDataDescriptor.getBulkNvBlock.__doc__.strip() == BULK_NV_BLOCK_NOTE
        assert BulkNvDataDescriptor.getNvBlockDataMappings.__doc__.strip() == BULK_NV_BLOCK_DATA_MAPPING_NOTE
        assert BulkNvDataDescriptor.addNvBlockDataMapping.__doc__.strip() == (BULK_NV_BLOCK_DATA_MAPPING_NOTE + " A None value is a no-op and does not append anything.")

    def test_base_shape(self):
        """Test the base chain, constructor signature and typed accessor signatures"""
        import typing

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor, NvBlockDataMapping

        assert issubclass(BulkNvDataDescriptor, AtpStructureElement)
        assert issubclass(BulkNvDataDescriptor, VariationPointCapable)

        hints = typing.get_type_hints(BulkNvDataDescriptor.createBulkNvBlock)
        assert hints["short_name"] is str
        assert hints["return"] is VariableDataPrototype
        hints = typing.get_type_hints(BulkNvDataDescriptor.getBulkNvBlock)
        assert hints["return"] == typing.Optional[VariableDataPrototype]
        hints = typing.get_type_hints(BulkNvDataDescriptor.getNvBlockDataMappings)
        assert hints["return"] == typing.List[NvBlockDataMapping]
        hints = typing.get_type_hints(BulkNvDataDescriptor.addNvBlockDataMapping)
        assert hints["value"] == typing.Optional[NvBlockDataMapping]
        assert hints["return"] is BulkNvDataDescriptor

    def test_initialization(self):
        """Test BulkNvDataDescriptor initialization"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor

        descriptor = BulkNvDataDescriptor(None, "BulkDescriptor")

        assert descriptor is not None
        assert descriptor.short_name == "BulkDescriptor"
        assert descriptor.bulkNvBlock is None
        assert descriptor.nvBlockDataMappings == []

    def test_create_get_bulk_nv_block(self):
        """Test createBulkNvBlock and getBulkNvBlock methods (duplicate short name returns the existing element)"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor

        descriptor = BulkNvDataDescriptor(None, "BulkDescriptor")

        assert descriptor.getBulkNvBlock() is None
        block = descriptor.createBulkNvBlock("RamBlock")
        assert block.getShortName() == "RamBlock"
        assert descriptor.getBulkNvBlock() is block
        assert descriptor.createBulkNvBlock("RamBlock") is block
        assert descriptor.getBulkNvBlock() is block

    def test_add_get_nv_block_data_mappings(self):
        """Test addNvBlockDataMapping and getNvBlockDataMappings methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor, NvBlockDataMapping

        descriptor = BulkNvDataDescriptor(None, "BulkDescriptor")

        assert descriptor.getNvBlockDataMappings() == []
        mapping = NvBlockDataMapping()
        assert descriptor.addNvBlockDataMapping(mapping) is descriptor
        assert descriptor.getNvBlockDataMappings() == [mapping]
        descriptor.addNvBlockDataMapping(mapping)
        assert descriptor.getNvBlockDataMappings() == [mapping]
        descriptor.addNvBlockDataMapping(None)
        assert descriptor.getNvBlockDataMappings() == [mapping]


class TestNvBlockDescriptor:
    def test_initialization(self):
        """Test NvBlockDescriptor initialization"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor is not None
        assert descriptor.short_name == "NvBlockDesc"
        assert descriptor.nvBlockDataMappings == []
        assert descriptor.nvBlockNeeds is None
        assert descriptor.ramBlock is None
        assert descriptor.romBlock is None
        assert descriptor.supportDirtyFlag is None
        assert descriptor.timingEventRef is None
        assert descriptor.writingStrategies == []

    def test_add_get_nv_block_data_mappings(self):
        """Test addNvBlockDataMapping and getNvBlockDataMappings methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping, NvBlockDescriptor  # noqa E501

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getNvBlockDataMappings() == []
        mapping = NvBlockDataMapping()
        descriptor.addNvBlockDataMapping(mapping)
        assert descriptor.getNvBlockDataMappings() == [mapping]
        descriptor.addNvBlockDataMapping(mapping)
        assert descriptor.getNvBlockDataMappings() == [mapping]
        descriptor.addNvBlockDataMapping(None)
        assert descriptor.getNvBlockDataMappings() == [mapping]

    def test_get_set_nv_block_needs(self):
        """Test getNvBlockNeeds and setNvBlockNeeds methods"""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import NvBlockNeeds
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getNvBlockNeeds() is None
        needs = NvBlockNeeds(None, "NvBlockNeeds")
        descriptor.setNvBlockNeeds(needs)
        assert descriptor.getNvBlockNeeds() == needs
        descriptor.setNvBlockNeeds(None)
        assert descriptor.getNvBlockNeeds() == needs

    def test_get_set_ram_block(self):
        """Test getRamBlock and setRamBlock methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype  # noqa E501
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getRamBlock() is None
        block = VariableDataPrototype(None, "RamBlock")
        descriptor.setRamBlock(block)
        assert descriptor.getRamBlock() == block
        descriptor.setRamBlock(None)
        assert descriptor.getRamBlock() == block

    def test_get_set_rom_block(self):
        """Test getRomBlock and setRomBlock methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype  # noqa E501
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getRomBlock() is None
        block = ParameterDataPrototype(None, "RomBlock")
        descriptor.setRomBlock(block)
        assert descriptor.getRomBlock() == block
        descriptor.setRomBlock(None)
        assert descriptor.getRomBlock() == block

    def test_get_set_support_dirty_flag(self):
        """Test getSupportDirtyFlag and setSupportDirtyFlag methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getSupportDirtyFlag() is None
        descriptor.setSupportDirtyFlag(True)
        assert descriptor.getSupportDirtyFlag() is True
        descriptor.setSupportDirtyFlag(None)
        assert descriptor.getSupportDirtyFlag() is True

    def test_get_set_timing_event_ref(self):
        """Test getTimingEventRef and setTimingEventRef methods"""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getTimingEventRef() is None
        ref = RefType()
        ref.setValue("/TimingEventRef")
        descriptor.setTimingEventRef(ref)
        assert descriptor.getTimingEventRef() == ref

    def test_add_get_writing_strategies(self):
        """Test addWritingStrategy and getWritingStrategies methods"""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataAssignment  # noqa E501
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getWritingStrategies() == []
        strategy = RoleBasedDataAssignment()
        descriptor.addWritingStrategy(strategy)
        assert descriptor.getWritingStrategies() == [strategy]
        descriptor.addWritingStrategy(strategy)
        assert descriptor.getWritingStrategies() == [strategy]
        descriptor.addWritingStrategy(None)
        assert descriptor.getWritingStrategies() == [strategy]

    def test_add_get_client_server_ports(self):
        """Test addClientServerPort and getClientServerPorts methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedPortAssignment  # noqa E501

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getClientServerPorts() == []
        assignment = RoleBasedPortAssignment()
        descriptor.addClientServerPort(assignment)
        assert descriptor.getClientServerPorts() == [assignment]
        descriptor.addClientServerPort(assignment)
        assert descriptor.getClientServerPorts() == [assignment]
        descriptor.addClientServerPort(None)
        assert descriptor.getClientServerPorts() == [assignment]

    def test_add_get_constant_value_mapping_refs(self):
        """Test addConstantValueMappingRef and getConstantValueMappingRefs methods"""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getConstantValueMappingRefs() == []
        ref = RefType()
        ref.setValue("/ConstantMapping")
        descriptor.addConstantValueMappingRef(ref)
        assert descriptor.getConstantValueMappingRefs() == [ref]
        descriptor.addConstantValueMappingRef(ref)
        assert descriptor.getConstantValueMappingRefs() == [ref]
        descriptor.addConstantValueMappingRef(None)
        assert descriptor.getConstantValueMappingRefs() == [ref]

    def test_add_get_data_type_mapping_refs(self):
        """Test addDataTypeMappingRef and getDataTypeMappingRefs methods"""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getDataTypeMappingRefs() == []
        ref = RefType()
        ref.setValue("/DataTypeMapping")
        descriptor.addDataTypeMappingRef(ref)
        assert descriptor.getDataTypeMappingRefs() == [ref]
        descriptor.addDataTypeMappingRef(ref)
        assert descriptor.getDataTypeMappingRefs() == [ref]
        descriptor.addDataTypeMappingRef(None)
        assert descriptor.getDataTypeMappingRefs() == [ref]

    def test_add_get_instantiation_data_def_propss(self):
        """Test addInstantiationDataDefProps and getInstantiationDataDefPropss methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps  # noqa E501

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getInstantiationDataDefPropss() == []
        props = InstantiationDataDefProps()
        descriptor.addInstantiationDataDefProps(props)
        assert descriptor.getInstantiationDataDefPropss() == [props]
        descriptor.addInstantiationDataDefProps(props)
        assert descriptor.getInstantiationDataDefPropss() == [props]
        descriptor.addInstantiationDataDefProps(None)
        assert descriptor.getInstantiationDataDefPropss() == [props]

    def test_add_get_mode_switch_event_triggered_activitys(self):
        """Test addModeSwitchEventTriggeredActivity and getModeSwitchEventTriggeredActivitys methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity, NvBlockDescriptor  # noqa E501

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getModeSwitchEventTriggeredActivitys() == []
        activity = ModeSwitchEventTriggeredActivity()
        descriptor.addModeSwitchEventTriggeredActivity(activity)
        assert descriptor.getModeSwitchEventTriggeredActivitys() == [activity]
        descriptor.addModeSwitchEventTriggeredActivity(activity)
        assert descriptor.getModeSwitchEventTriggeredActivitys() == [activity]
        descriptor.addModeSwitchEventTriggeredActivity(None)
        assert descriptor.getModeSwitchEventTriggeredActivitys() == [activity]


class TestModeSwitchEventTriggeredActivity:
    def test_spec_notes_are_verbatim(self):
        """Test that the class docstring and every accessor docstring is the spec Note verbatim (Table 11.7)"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity  # noqa E501

        role_note = "This attribute indicates which service of the NvM for the NvBlock shall be requested."
        swc_mode_switch_event_note = "This reference identifies the SwcModeSwitchEvent that triggers the activity."

        assert ModeSwitchEventTriggeredActivity.__doc__.strip() == ("This meta-class defines an activity of the NvBlockSwComponentType for a specific NvBlock which is triggered by a ModeSwitchEvent.")
        assert ModeSwitchEventTriggeredActivity.getRole.__doc__.strip() == role_note
        assert ModeSwitchEventTriggeredActivity.setRole.__doc__.strip() == (role_note + " A None value is a no-op and does not overwrite an existing role.")
        assert ModeSwitchEventTriggeredActivity.getSwcModeSwitchEventRef.__doc__.strip() == swc_mode_switch_event_note
        assert ModeSwitchEventTriggeredActivity.setSwcModeSwitchEventRef.__doc__.strip() == (
            swc_mode_switch_event_note + " A None value is a no-op and does not overwrite an existing swcModeSwitchEventRef."
        )

    def test_base_shape(self):
        """Test the base chain, no-arg __init__ and typed accessor signatures"""
        import typing

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity  # noqa E501

        assert issubclass(ModeSwitchEventTriggeredActivity, ARObject)
        assert issubclass(ModeSwitchEventTriggeredActivity, VariationPointCapable)
        assert ModeSwitchEventTriggeredActivity().role is None

        hints = typing.get_type_hints(ModeSwitchEventTriggeredActivity.getRole)
        assert hints["return"] == typing.Optional[Identifier]
        hints = typing.get_type_hints(ModeSwitchEventTriggeredActivity.setRole)
        assert hints["value"] == typing.Optional[Identifier]
        assert hints["return"] is ModeSwitchEventTriggeredActivity
        hints = typing.get_type_hints(ModeSwitchEventTriggeredActivity.getSwcModeSwitchEventRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(ModeSwitchEventTriggeredActivity.setSwcModeSwitchEventRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is ModeSwitchEventTriggeredActivity

    def test_initialization(self):
        """Test ModeSwitchEventTriggeredActivity initialization"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity  # noqa E501

        activity = ModeSwitchEventTriggeredActivity()

        assert activity is not None
        assert activity.role is None
        assert activity.swcModeSwitchEventRef is None

    def test_get_set_role(self):
        """Test getRole and setRole methods"""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity  # noqa E501

        activity = ModeSwitchEventTriggeredActivity()

        assert activity.getRole() is None
        role = Identifier()
        role.setValue("WriteBlock")
        assert activity.setRole(role) is activity
        assert isinstance(activity.getRole(), Identifier)
        assert activity.getRole() is role
        assert activity.getRole().getValue() == "WriteBlock"
        activity.setRole(None)
        assert activity.getRole() is role

    def test_get_set_swc_mode_switch_event_ref(self):
        """Test getSwcModeSwitchEventRef and setSwcModeSwitchEventRef methods"""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity  # noqa E501

        activity = ModeSwitchEventTriggeredActivity()

        assert activity.getSwcModeSwitchEventRef() is None
        ref = RefType()
        ref.setValue("/SwcModeSwitchEvent")
        assert activity.setSwcModeSwitchEventRef(ref) is activity
        assert activity.getSwcModeSwitchEventRef() is ref
        activity.setSwcModeSwitchEventRef(None)
        assert activity.getSwcModeSwitchEventRef() is ref
