"""Tests for the NvBlockDataMapping parser handler."""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

NS = "http://autosar.org/schema/r4.0"


def _snip(inner: str, root_tag: str = "NV-BLOCK-DATA-MAPPING") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _autosar_root():
    return AUTOSAR.getInstance()


class TestNvBlockDataMappingHandlers:
    """Exercise the NvBlockDataMapping parser handler."""

    def test_read_nv_block_data_mapping_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        element = _snip(
            "<BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR>10</BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR>"
            "<BITFIELD-TEXT-TABLE-MASK-PORT-PROTOTYPE>32</BITFIELD-TEXT-TABLE-MASK-PORT-PROTOTYPE>"
            "<NV-RAM-BLOCK-ELEMENT>"
            "<AUTOSAR-VARIABLE-IREF><PORT-PROTOTYPE-REF DEST='P-PORT-PROTOTYPE'>/ramPP</PORT-PROTOTYPE-REF></AUTOSAR-VARIABLE-IREF>"
            "</NV-RAM-BLOCK-ELEMENT>"
            "<READ-NV-DATA><AUTOSAR-VARIABLE-IREF><PORT-PROTOTYPE-REF DEST='P-PORT-PROTOTYPE'>/readPP</PORT-PROTOTYPE-REF></AUTOSAR-VARIABLE-IREF></READ-NV-DATA>",
            root_tag="NV-BLOCK-DATA-MAPPING",
        )
        mapping = NvBlockDataMapping()
        parser.readNvBlockDataMapping(element, mapping)
        assert mapping.getBitfieldTextTableMaskNvBlockDescriptor().getValue() == 10
        assert mapping.getBitfieldTextTableMaskPortPrototype().getValue() == 32
        assert mapping.getNvRamBlockElement() is not None
        assert mapping.getReadNvData() is not None
        assert mapping.getWrittenNvData() is None
        assert mapping.getWrittenReadNvData() is None

    def test_read_nv_block_data_mapping_minimal(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        mapping = NvBlockDataMapping()
        parser.readNvBlockDataMapping(_snip("", root_tag="NV-BLOCK-DATA-MAPPING"), mapping)
        assert mapping.getBitfieldTextTableMaskNvBlockDescriptor() is None
        assert mapping.getNvRamBlockElement() is None
        assert mapping.getReadNvData() is None

    def test_read_nv_block_data_mapping_all_elements_field_values(self, parser):
        """Test that all six Table 11.11 attribute elements are read with their field values."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarVariableRef

        element = _snip(
            "<BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR>10</BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR>"
            "<BITFIELD-TEXT-TABLE-MASK-PORT-PROTOTYPE>32</BITFIELD-TEXT-TABLE-MASK-PORT-PROTOTYPE>"
            "<NV-RAM-BLOCK-ELEMENT><AUTOSAR-VARIABLE-IREF><PORT-PROTOTYPE-REF DEST='PORT-PROTOTYPE'>/ramPP</PORT-PROTOTYPE-REF></AUTOSAR-VARIABLE-IREF></NV-RAM-BLOCK-ELEMENT>"
            "<READ-NV-DATA><AUTOSAR-VARIABLE-IREF><PORT-PROTOTYPE-REF DEST='PORT-PROTOTYPE'>/readPP</PORT-PROTOTYPE-REF></AUTOSAR-VARIABLE-IREF></READ-NV-DATA>"
            "<WRITTEN-NV-DATA><AUTOSAR-VARIABLE-IREF><PORT-PROTOTYPE-REF DEST='PORT-PROTOTYPE'>/writtenPP</PORT-PROTOTYPE-REF></AUTOSAR-VARIABLE-IREF></WRITTEN-NV-DATA>"
            "<WRITTEN-READ-NV-DATA><AUTOSAR-VARIABLE-IREF><PORT-PROTOTYPE-REF DEST='PORT-PROTOTYPE'>/writtenReadPP</PORT-PROTOTYPE-REF></AUTOSAR-VARIABLE-IREF></WRITTEN-READ-NV-DATA>"
        )
        mapping = NvBlockDataMapping()
        parser.readNvBlockDataMapping(element, mapping)

        assert mapping.getBitfieldTextTableMaskNvBlockDescriptor().getValue() == 10
        assert mapping.getBitfieldTextTableMaskPortPrototype().getValue() == 32
        for getter, expected in [
            (mapping.getNvRamBlockElement, "/ramPP"),
            (mapping.getReadNvData, "/readPP"),
            (mapping.getWrittenNvData, "/writtenPP"),
            (mapping.getWrittenReadNvData, "/writtenReadPP"),
        ]:
            ref = getter()
            assert isinstance(ref, AutosarVariableRef)
            assert ref.getAutosarVariableIRef().getPortPrototypeRef().getValue() == expected

    def test_read_nv_block_data_mapping_ar_object_attributes(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read (XSD AR-OBJECT attributeGroup)."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        element = ET.fromstring(
            f"<NV-BLOCK-DATA-MAPPING xmlns='{NS}' S='abc123' T='2024-01-01T12:00:00+00:00'>"
            "<BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR>10</BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR>"
            "</NV-BLOCK-DATA-MAPPING>"
        )
        mapping = NvBlockDataMapping()
        parser.readNvBlockDataMapping(element, mapping)

        assert mapping.getChecksum() is not None
        assert mapping.getChecksum().getValue() == "abc123"
        assert mapping.getTimestamp() is not None


class TestBulkNvDataDescriptorHandlers:
    """Exercise the BulkNvDataDescriptor parser handler."""

    def test_read_bulk_nv_data_descriptor_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor  # noqa E501

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = BulkNvDataDescriptor(root, "BulkDesc")
        element = _snip(
            "<SHORT-NAME>BulkDesc</SHORT-NAME>"
            "<BULK-NV-BLOCK><VARIABLE-DATA-PROTOTYPE><SHORT-NAME>RamBlock</SHORT-NAME></VARIABLE-DATA-PROTOTYPE></BULK-NV-BLOCK>"
            "<NV-BLOCK-DATA-MAPPINGS><NV-BLOCK-DATA-MAPPING><READ-NV-DATA><AUTOSAR-VARIABLE-IREF><PORT-PROTOTYPE-REF DEST='P-PORT-PROTOTYPE'>/readPP</PORT-PROTOTYPE-REF></AUTOSAR-VARIABLE-IREF></READ-NV-DATA></NV-BLOCK-DATA-MAPPING></NV-BLOCK-DATA-MAPPINGS>",
            root_tag="BULK-NV-DATA-DESCRIPTOR",
        )
        parser.readBulkNvDataDescriptor(element, descriptor)
        assert descriptor.getShortName() == "BulkDesc"
        assert descriptor.getBulkNvBlock() is not None
        assert descriptor.getBulkNvBlock().getShortName() == "RamBlock"
        mappings = descriptor.getNvBlockDataMappings()
        assert len(mappings) == 1
        assert mappings[0].getReadNvData() is not None

    def test_read_bulk_nv_data_descriptor_minimal(self, parser):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor  # noqa E501

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = BulkNvDataDescriptor(root, "BulkDesc")
        parser.readBulkNvDataDescriptor(_snip("<SHORT-NAME>BulkDesc</SHORT-NAME>", root_tag="BULK-NV-DATA-DESCRIPTOR"), descriptor)
        assert descriptor.getBulkNvBlock() is None
        assert descriptor.getNvBlockDataMappings() == []


class TestNvBlockDescriptorHandlers:
    """Exercise the NvBlockDescriptor parser handler."""

    def test_read_nv_block_descriptor_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "NvBlockDesc")
        element = _snip(
            "<SHORT-NAME>NvBlockDesc</SHORT-NAME>"
            "<CLIENT-SERVER-PORTS><ROLE-BASED-PORT-ASSIGNMENT><ROLE>calibration</ROLE></ROLE-BASED-PORT-ASSIGNMENT></CLIENT-SERVER-PORTS>"
            "<CONSTANT-VALUE-MAPPING-REFS><CONSTANT-VALUE-MAPPING-REF DEST='CONSTANT-SPECIFICATION-MAPPING-SET'>/ConstMapping</CONSTANT-VALUE-MAPPING-REF></CONSTANT-VALUE-MAPPING-REFS>"
            "<DATA-TYPE-MAPPING-REFS><DATA-TYPE-MAPPING-REF DEST='DATA-TYPE-MAPPING-SET'>/DataTypeMapping</DATA-TYPE-MAPPING-REF></DATA-TYPE-MAPPING-REFS>"
            "<INSTANTIATION-DATA-DEF-PROPSS><INSTANTIATION-DATA-DEF-PROPS></INSTANTIATION-DATA-DEF-PROPS></INSTANTIATION-DATA-DEF-PROPSS>"
            "<MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS><MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY><ROLE>WriteBlock</ROLE><SWC-MODE-SWITCH-EVENT-REF DEST='SWC-MODE-SWITCH-EVENT'>/SwcModeSwitchEvent</SWC-MODE-SWITCH-EVENT-REF></MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY></MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS>"
            "<NV-BLOCK-DATA-MAPPINGS><NV-BLOCK-DATA-MAPPING><READ-NV-DATA><AUTOSAR-VARIABLE-IREF><PORT-PROTOTYPE-REF DEST='P-PORT-PROTOTYPE'>/readPP</PORT-PROTOTYPE-REF></AUTOSAR-VARIABLE-IREF></READ-NV-DATA></NV-BLOCK-DATA-MAPPING></NV-BLOCK-DATA-MAPPINGS>"
            "<NV-BLOCK-NEEDS><SHORT-NAME>NvNeeds</SHORT-NAME><N-DATA-SETS>3</N-DATA-SETS></NV-BLOCK-NEEDS>"
            "<RAM-BLOCK><SHORT-NAME>RamBlock</SHORT-NAME></RAM-BLOCK>"
            "<ROM-BLOCK><SHORT-NAME>RomBlock</SHORT-NAME></ROM-BLOCK>"
            "<SUPPORT-DIRTY-FLAG>true</SUPPORT-DIRTY-FLAG>"
            "<TIMING-EVENT-REF DEST='TIMING-EVENT'>/TimingEvent</TIMING-EVENT-REF>"
            "<WRITING-STRATEGYS><ROLE-BASED-DATA-ASSIGNMENT><ROLE>callout</ROLE></ROLE-BASED-DATA-ASSIGNMENT></WRITING-STRATEGYS>",
            root_tag="NV-BLOCK-DESCRIPTOR",
        )
        parser.readNvBlockDescriptor(element, descriptor)
        assert descriptor.getShortName() == "NvBlockDesc"
        assert len(descriptor.getClientServerPorts()) == 1
        assert len(descriptor.getConstantValueMappingRefs()) == 1
        assert len(descriptor.getDataTypeMappingRefs()) == 1
        assert len(descriptor.getInstantiationDataDefPropss()) == 1
        assert len(descriptor.getModeSwitchEventTriggeredActivitys()) == 1
        activities = descriptor.getModeSwitchEventTriggeredActivitys()
        assert activities[0].getRole().getValue() == "WriteBlock"
        assert activities[0].getSwcModeSwitchEventRef() is not None
        assert len(descriptor.getNvBlockDataMappings()) == 1
        assert descriptor.getNvBlockDataMappings()[0].getReadNvData() is not None
        assert descriptor.getNvBlockNeeds() is not None
        assert descriptor.getNvBlockNeeds().getShortName() == "NvNeeds"
        assert descriptor.getRamBlock() is not None
        assert descriptor.getRamBlock().getShortName() == "RamBlock"
        assert descriptor.getRomBlock() is not None
        assert descriptor.getRomBlock().getShortName() == "RomBlock"
        assert descriptor.getSupportDirtyFlag() is not None
        assert descriptor.getSupportDirtyFlag().getValue() is True
        assert descriptor.getTimingEventRef() is not None
        strategies = descriptor.getWritingStrategies()
        assert len(strategies) == 1
        assert strategies[0].getRole() is not None

    def test_read_nv_block_descriptor_minimal(self, parser):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "NvBlockDesc")
        parser.readNvBlockDescriptor(_snip("<SHORT-NAME>NvBlockDesc</SHORT-NAME>", root_tag="NV-BLOCK-DESCRIPTOR"), descriptor)
        assert descriptor.getClientServerPorts() == []
        assert descriptor.getConstantValueMappingRefs() == []
        assert descriptor.getDataTypeMappingRefs() == []
        assert descriptor.getInstantiationDataDefPropss() == []
        assert descriptor.getModeSwitchEventTriggeredActivitys() == []
        assert descriptor.getNvBlockDataMappings() == []
        assert descriptor.getNvBlockNeeds() is None
        assert descriptor.getRamBlock() is None
        assert descriptor.getRomBlock() is None
        assert descriptor.getSupportDirtyFlag() is None
        assert descriptor.getTimingEventRef() is None
        assert descriptor.getWritingStrategies() == []
