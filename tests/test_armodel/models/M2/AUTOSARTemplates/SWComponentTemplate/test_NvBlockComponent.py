class TestNvBlockDataMapping:
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
        mapping.setBitfieldTextTableMaskNvBlockDescriptor(10)
        assert mapping.getBitfieldTextTableMaskNvBlockDescriptor() == 10
        mapping.setBitfieldTextTableMaskNvBlockDescriptor(None)
        assert mapping.getBitfieldTextTableMaskNvBlockDescriptor() == 10

    def test_get_set_bitfield_text_table_mask_port_prototype(self):
        """Test getBitfieldTextTableMaskPortPrototype and setBitfieldTextTableMaskPortPrototype methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        mapping = NvBlockDataMapping()

        assert mapping.getBitfieldTextTableMaskPortPrototype() is None
        mapping.setBitfieldTextTableMaskPortPrototype(32)
        assert mapping.getBitfieldTextTableMaskPortPrototype() == 32
        mapping.setBitfieldTextTableMaskPortPrototype(None)
        assert mapping.getBitfieldTextTableMaskPortPrototype() == 32

    def test_get_set_nv_ram_block_element(self):
        """Test getNvRamBlockElement and setNvRamBlockElement methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        mapping = NvBlockDataMapping()

        assert mapping.getNvRamBlockElement() is None
        mapping.setNvRamBlockElement("NvRamBlockElement")
        assert mapping.getNvRamBlockElement() == "NvRamBlockElement"

    def test_get_set_read_nv_data(self):
        """Test getReadNvData and setReadNvData methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        mapping = NvBlockDataMapping()

        assert mapping.getReadNvData() is None
        mapping.setReadNvData("ReadNvData")
        assert mapping.getReadNvData() == "ReadNvData"

    def test_get_set_written_nv_data(self):
        """Test getWrittenNvData and setWrittenNvData methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        mapping = NvBlockDataMapping()

        assert mapping.getWrittenNvData() is None
        mapping.setWrittenNvData("WrittenNvData")
        assert mapping.getWrittenNvData() == "WrittenNvData"

    def test_get_set_written_read_nv_data(self):
        """Test getWrittenReadNvData and setWrittenReadNvData methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        mapping = NvBlockDataMapping()

        assert mapping.getWrittenReadNvData() is None
        mapping.setWrittenReadNvData("WrittenReadNvData")
        assert mapping.getWrittenReadNvData() == "WrittenReadNvData"


class TestBulkNvDataDescriptor:
    def test_initialization(self):
        """Test BulkNvDataDescriptor initialization"""
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        descriptor = BulkNvDataDescriptor(ar_root, "BulkDescriptor")

        assert descriptor is not None
        assert descriptor.parent == ar_root
        assert descriptor.short_name == "BulkDescriptor"
        assert descriptor.bulkNvBlock is None
        assert descriptor.nvBlockDataMappings == []

    def test_get_set_bulk_nv_block(self):
        """Test getBulkNvBlock and setBulkNvBlock methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype  # noqa E501
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor

        descriptor = BulkNvDataDescriptor(None, "BulkDescriptor")

        assert descriptor.getBulkNvBlock() is None
        block = VariableDataPrototype(None, "RamBlock")
        descriptor.setBulkNvBlock(block)
        assert descriptor.getBulkNvBlock() == block
        descriptor.setBulkNvBlock(None)
        assert descriptor.getBulkNvBlock() == block

    def test_add_get_nv_block_data_mappings(self):
        """Test addNvBlockDataMapping and getNvBlockDataMappings methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor, NvBlockDataMapping

        descriptor = BulkNvDataDescriptor(None, "BulkDescriptor")

        assert descriptor.getNvBlockDataMappings() == []
        mapping = NvBlockDataMapping()
        descriptor.addNvBlockDataMapping(mapping)
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
    def test_initialization(self):
        """Test ModeSwitchEventTriggeredActivity initialization"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity  # noqa E501

        activity = ModeSwitchEventTriggeredActivity()

        assert activity is not None
        assert activity is not None
        assert activity.role is None
        assert activity.swcModeSwitchEventRef is None

    def test_get_set_role(self):
        """Test getRole and setRole methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity  # noqa E501

        activity = ModeSwitchEventTriggeredActivity()

        assert activity.getRole() is None
        activity.setRole("WriteBlock")
        assert activity.getRole() == "WriteBlock"

    def test_get_set_swc_mode_switch_event_ref(self):
        """Test getSwcModeSwitchEventRef and setSwcModeSwitchEventRef methods"""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity  # noqa E501

        activity = ModeSwitchEventTriggeredActivity()

        assert activity.getSwcModeSwitchEventRef() is None
        ref = RefType()
        ref.setValue("/SwcModeSwitchEvent")
        activity.setSwcModeSwitchEventRef(ref)
        assert activity.getSwcModeSwitchEventRef() == ref
        activity.setSwcModeSwitchEventRef(None)
        assert activity.getSwcModeSwitchEventRef() == ref
