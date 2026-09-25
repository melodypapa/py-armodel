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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
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


NBD_CLASS_NOTE = "Specifies the properties of exactly on NVRAM Block."

NBD_CONSTRAINT_1981 = "[constr_1981] Existence of attribute NvBlockDescriptor.nvBlockNeeds: " "For each NvBlockDescriptor, attribute nvBlockNeeds shall exist at the time when the RTE is generated."

NBD_ATTR_NOTES = {
    "clientServerPorts": (
        "The RoleBasedPortAssignement defines which client server port of the NvBlockSwComponentType serves for which kind of service or notification. "
        'In case of notifications one common callback function is provided by the RTE for each individual kind of notification defined by the "role". '
        "The aggregation of RoleBasedPortAssignment is subject to variability with the purpose to support the conditional existence of ports."
    ),
    "constantValueMappingRefs": "Reference to the ConstantSpecificationMapping to be applied for the particular NVRAM Block",
    "dataTypeMappingRefs": "Reference to the DataTypeMapping to be applied for the particular NVRAM Block.",
    "instantiationDataDefPropss": (
        "The purpose of InstantiationDataDefProps are the refinement of some data def properties of individual instantiations within the context of a NvBlockSwComponentType. "
        "The aggregation of InstantiationDataDefProps is subject to variability with the purpose to support the conditional existence of ports, component internal memory objects and those attributes."
    ),
    "modeSwitchEventTriggeredActivitys": "This represents the collection of ModeSwitchEventTriggeredActivities related to the enclosing NvBlockDescriptor.",
    "nvBlockDataMappings": (
        "Defines the mapping between the VariableDataPrototypes in the NvBlockComponents ports and the VariableDataPrototypes of the RAM Block. "
        "The aggregation of NvBlockDataMapping is subject to variability with the purpose to support the conditional existence of nv data ports."
    ),
    "nvBlockNeeds": (
        "Specifies the abstract needs on the configuration of the NVRAM Manager for the single NVRAM Block described by this NvBlockDescriptor. "
        "In addition, it may define requirements for writing strategies in an implementation of an NvBlockSwComponentType by the RTE. "
        "Please note that the attributes nDataSets and nRomBlocks are not relevant for this aggregation because the RTE will allocate just one block anyway. "
        "In a different context, however, they do make sense."
    ),
    "ramBlock": "Defines the RAM Block of the NVRAM Block provided by NvBlockSwComponentType.",
    "romBlock": "Defines the ROM Block of the NVRAM Block provided by NvBlockSwComponentType.",
    "supportDirtyFlag": "Specifies whether calling of NvM functions for writing and/or status control of potentially modified RAM Blocks to NV memory shall be controlled by the RTE.",
    "timingEventRef": "this reference can be taken to identify the TimingEvent to be used by the RTE for implementing a cyclic writing strategy for this block",
    "writingStrategies": "This attribute allows for assigning a specific writing strategy for an incoming AutosarDataPrototype.",
}

NBD_LIST_ACCESSORS = {
    "clientServerPorts": ("getClientServerPorts", "addClientServerPort"),
    "constantValueMappingRefs": ("getConstantValueMappingRefs", "addConstantValueMappingRef"),
    "dataTypeMappingRefs": ("getDataTypeMappingRefs", "addDataTypeMappingRef"),
    "instantiationDataDefPropss": ("getInstantiationDataDefPropss", "addInstantiationDataDefProps"),
    "modeSwitchEventTriggeredActivitys": ("getModeSwitchEventTriggeredActivitys", "addModeSwitchEventTriggeredActivity"),
    "nvBlockDataMappings": ("getNvBlockDataMappings", "addNvBlockDataMapping"),
    "writingStrategies": ("getWritingStrategies", "addWritingStrategy"),
}

NBD_CREATE_ACCESSORS = {
    "nvBlockNeeds": ("getNvBlockNeeds", "createNvBlockNeeds"),
    "ramBlock": ("getRamBlock", "createRamBlock"),
    "romBlock": ("getRomBlock", "createRomBlock"),
}


class TestNvBlockDescriptor:
    def test_spec_notes_are_verbatim(self):
        """Test that the class docstring and every accessor docstring is the spec Note verbatim (Table 11.6)"""
        import inspect

        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor

        assert inspect.cleandoc(NvBlockDescriptor.__doc__) == (NBD_CLASS_NOTE + "\n\n" + NBD_CONSTRAINT_1981)
        for attr, note in NBD_ATTR_NOTES.items():
            if attr in NBD_LIST_ACCESSORS:
                getter, mutator = NBD_LIST_ACCESSORS[attr]
                assert getattr(NvBlockDescriptor, getter).__doc__.strip() == note, attr
                assert getattr(NvBlockDescriptor, mutator).__doc__.strip() == (note + " A None value is a no-op and does not append anything."), attr
            elif attr in NBD_CREATE_ACCESSORS:
                getter, factory = NBD_CREATE_ACCESSORS[attr]
                assert getattr(NvBlockDescriptor, getter).__doc__.strip() == note, attr
                assert getattr(NvBlockDescriptor, factory).__doc__.strip() == note, attr
            else:
                getter = "get" + attr[0].upper() + attr[1:]
                setter = "set" + attr[0].upper() + attr[1:]
                assert getattr(NvBlockDescriptor, getter).__doc__.strip() == note, attr
                assert getattr(NvBlockDescriptor, setter).__doc__.strip() == (note + " A None value is a no-op and does not overwrite an existing %s." % attr), attr

    def test_base_shape(self):
        """Test the base chain, Identifiable construction and the typed accessor signatures (own attributes only — inherited members are not flattened)"""
        import typing

        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import NvBlockNeeds, RoleBasedDataAssignment
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity, NvBlockDataMapping, NvBlockDescriptor
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedPortAssignment

        assert issubclass(NvBlockDescriptor, AtpStructureElement)
        assert issubclass(NvBlockDescriptor, VariationPointCapable)

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")
        assert descriptor.getShortName() == "NvBlockDesc"

        field_types = {
            "clientServerPorts": RoleBasedPortAssignment,
            "constantValueMappingRefs": RefType,
            "dataTypeMappingRefs": RefType,
            "instantiationDataDefPropss": InstantiationDataDefProps,
            "modeSwitchEventTriggeredActivitys": ModeSwitchEventTriggeredActivity,
            "nvBlockDataMappings": NvBlockDataMapping,
            "nvBlockNeeds": NvBlockNeeds,
            "ramBlock": VariableDataPrototype,
            "romBlock": ParameterDataPrototype,
            "supportDirtyFlag": Boolean,
            "timingEventRef": RefType,
            "writingStrategies": RoleBasedDataAssignment,
        }
        for attr, field_type in field_types.items():
            if attr in NBD_LIST_ACCESSORS:
                getter, mutator = NBD_LIST_ACCESSORS[attr]
                hints = typing.get_type_hints(getattr(NvBlockDescriptor, getter))
                assert hints["return"] == typing.List[field_type], attr
                hints = typing.get_type_hints(getattr(NvBlockDescriptor, mutator))
                assert hints["value"] == typing.Optional[field_type], attr
                assert hints["return"] is NvBlockDescriptor, attr
            elif attr in NBD_CREATE_ACCESSORS:
                getter, factory = NBD_CREATE_ACCESSORS[attr]
                hints = typing.get_type_hints(getattr(NvBlockDescriptor, getter))
                assert hints["return"] == typing.Optional[field_type], attr
                hints = typing.get_type_hints(getattr(NvBlockDescriptor, factory))
                assert hints["short_name"] is str, attr
                assert hints["return"] is field_type, attr
            else:
                getter = "get" + attr[0].upper() + attr[1:]
                setter = "set" + attr[0].upper() + attr[1:]
                hints = typing.get_type_hints(getattr(NvBlockDescriptor, getter))
                assert hints["return"] == typing.Optional[field_type], attr
                hints = typing.get_type_hints(getattr(NvBlockDescriptor, setter))
                assert hints["value"] == typing.Optional[field_type], attr
                assert hints["return"] is NvBlockDescriptor, attr

    def test_initialization(self):
        """Test NvBlockDescriptor initialization"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor is not None
        assert descriptor.short_name == "NvBlockDesc"
        for attr in NBD_ATTR_NOTES:
            value = getattr(descriptor, attr)
            if attr in NBD_LIST_ACCESSORS:
                assert value == [], attr
            else:
                assert value is None, attr

    def test_add_get_client_server_ports(self):
        """Test addClientServerPort and getClientServerPorts methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedPortAssignment

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getClientServerPorts() == []
        assignment = RoleBasedPortAssignment()
        assert descriptor.addClientServerPort(assignment) is descriptor
        assert descriptor.getClientServerPorts() == [assignment]
        descriptor.addClientServerPort(assignment)
        assert descriptor.getClientServerPorts() == [assignment]
        descriptor.addClientServerPort(None)
        assert descriptor.getClientServerPorts() == [assignment]

    def test_add_get_constant_value_mapping_refs(self):
        """Test addConstantValueMappingRef and getConstantValueMappingRefs methods"""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getConstantValueMappingRefs() == []
        ref = RefType()
        ref.setValue("/ConstantMapping")
        assert descriptor.addConstantValueMappingRef(ref) is descriptor
        assert descriptor.getConstantValueMappingRefs() == [ref]
        descriptor.addConstantValueMappingRef(ref)
        assert descriptor.getConstantValueMappingRefs() == [ref]
        descriptor.addConstantValueMappingRef(None)
        assert descriptor.getConstantValueMappingRefs() == [ref]

    def test_add_get_data_type_mapping_refs(self):
        """Test addDataTypeMappingRef and getDataTypeMappingRefs methods"""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getDataTypeMappingRefs() == []
        ref = RefType()
        ref.setValue("/DataTypeMapping")
        assert descriptor.addDataTypeMappingRef(ref) is descriptor
        assert descriptor.getDataTypeMappingRefs() == [ref]
        descriptor.addDataTypeMappingRef(ref)
        assert descriptor.getDataTypeMappingRefs() == [ref]
        descriptor.addDataTypeMappingRef(None)
        assert descriptor.getDataTypeMappingRefs() == [ref]

    def test_add_get_instantiation_data_def_propss(self):
        """Test addInstantiationDataDefProps and getInstantiationDataDefPropss methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getInstantiationDataDefPropss() == []
        props = InstantiationDataDefProps()
        assert descriptor.addInstantiationDataDefProps(props) is descriptor
        assert descriptor.getInstantiationDataDefPropss() == [props]
        descriptor.addInstantiationDataDefProps(props)
        assert descriptor.getInstantiationDataDefPropss() == [props]
        descriptor.addInstantiationDataDefProps(None)
        assert descriptor.getInstantiationDataDefPropss() == [props]

    def test_add_get_mode_switch_event_triggered_activitys(self):
        """Test addModeSwitchEventTriggeredActivity and getModeSwitchEventTriggeredActivitys methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity, NvBlockDescriptor

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getModeSwitchEventTriggeredActivitys() == []
        activity = ModeSwitchEventTriggeredActivity()
        assert descriptor.addModeSwitchEventTriggeredActivity(activity) is descriptor
        assert descriptor.getModeSwitchEventTriggeredActivitys() == [activity]
        descriptor.addModeSwitchEventTriggeredActivity(activity)
        assert descriptor.getModeSwitchEventTriggeredActivitys() == [activity]
        descriptor.addModeSwitchEventTriggeredActivity(None)
        assert descriptor.getModeSwitchEventTriggeredActivitys() == [activity]

    def test_add_get_nv_block_data_mappings(self):
        """Test addNvBlockDataMapping and getNvBlockDataMappings methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping, NvBlockDescriptor

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getNvBlockDataMappings() == []
        mapping = NvBlockDataMapping()
        assert descriptor.addNvBlockDataMapping(mapping) is descriptor
        assert descriptor.getNvBlockDataMappings() == [mapping]
        descriptor.addNvBlockDataMapping(mapping)
        assert descriptor.getNvBlockDataMappings() == [mapping]
        descriptor.addNvBlockDataMapping(None)
        assert descriptor.getNvBlockDataMappings() == [mapping]

    def test_add_get_writing_strategies(self):
        """Test addWritingStrategy and getWritingStrategies methods"""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataAssignment
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getWritingStrategies() == []
        strategy = RoleBasedDataAssignment()
        assert descriptor.addWritingStrategy(strategy) is descriptor
        assert descriptor.getWritingStrategies() == [strategy]
        descriptor.addWritingStrategy(strategy)
        assert descriptor.getWritingStrategies() == [strategy]
        descriptor.addWritingStrategy(None)
        assert descriptor.getWritingStrategies() == [strategy]

    def test_create_get_nv_block_needs(self):
        """Test createNvBlockNeeds and getNvBlockNeeds methods"""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import NvBlockNeeds
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getNvBlockNeeds() is None
        needs = descriptor.createNvBlockNeeds("NvNeeds")
        assert isinstance(needs, NvBlockNeeds)
        assert needs.getShortName() == "NvNeeds"
        assert descriptor.getNvBlockNeeds() is needs
        assert descriptor.createNvBlockNeeds("NvNeeds") is needs
        assert descriptor.getNvBlockNeeds() is needs

    def test_create_get_ram_block(self):
        """Test createRamBlock and getRamBlock methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getRamBlock() is None
        block = descriptor.createRamBlock("RamBlock")
        assert isinstance(block, VariableDataPrototype)
        assert block.getShortName() == "RamBlock"
        assert descriptor.getRamBlock() is block
        assert descriptor.createRamBlock("RamBlock") is block
        assert descriptor.getRamBlock() is block

    def test_create_get_rom_block(self):
        """Test createRomBlock and getRomBlock methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getRomBlock() is None
        block = descriptor.createRomBlock("RomBlock")
        assert isinstance(block, ParameterDataPrototype)
        assert block.getShortName() == "RomBlock"
        assert descriptor.getRomBlock() is block
        assert descriptor.createRomBlock("RomBlock") is block
        assert descriptor.getRomBlock() is block

    def test_get_set_support_dirty_flag(self):
        """Test getSupportDirtyFlag and setSupportDirtyFlag methods"""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getSupportDirtyFlag() is None
        value = Boolean().setValue(True)
        assert descriptor.setSupportDirtyFlag(value) is descriptor
        assert descriptor.getSupportDirtyFlag() is value
        assert descriptor.getSupportDirtyFlag().getValue() is True

        # None is a no-op
        descriptor.setSupportDirtyFlag(None)
        assert descriptor.getSupportDirtyFlag() is value

    def test_get_set_timing_event_ref(self):
        """Test getTimingEventRef and setTimingEventRef methods"""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor

        descriptor = NvBlockDescriptor(None, "NvBlockDesc")

        assert descriptor.getTimingEventRef() is None
        ref = RefType()
        ref.setValue("/TimingEvent")
        assert descriptor.setTimingEventRef(ref) is descriptor
        assert descriptor.getTimingEventRef() is ref

        # None is a no-op
        descriptor.setTimingEventRef(None)
        assert descriptor.getTimingEventRef() is ref


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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
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
