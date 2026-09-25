"""
Tests for reading NV-BLOCK-DESCRIPTOR elements — NvBlockDescriptor, Table 11.6 (p.670, R23-11).

NvBlockDescriptor (Base = AtpStructureElement) carries twelve members whose reader
dispatch must follow the XSD group order (AUTOSAR_00052.xsd group NV-BLOCK-DESCRIPTOR):
CLIENT-SERVER-PORTS, CONSTANT-VALUE-MAPPING-REFS, DATA-TYPE-MAPPING-REFS,
INSTANTIATION-DATA-DEF-PROPSS, MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS,
NV-BLOCK-DATA-MAPPINGS, NV-BLOCK-NEEDS, RAM-BLOCK, ROM-BLOCK, SUPPORT-DIRTY-FLAG,
TIMING-EVENT-REF, WRITING-STRATEGYS. Identifiable-derived children (NV-BLOCK-NEEDS,
RAM-BLOCK, ROM-BLOCK) are materialized through the create-factories so the elements
registry stays consistent.

Round-trip counterpart: tests/test_armodel/writer/test_nv_block_descriptor.py
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import NvBlockNeeds
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import ParameterDataPrototype, VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor
from tests.test_armodel.parser._helpers import _snip


class TestReadNvBlockDescriptor:
    """Tests for readNvBlockDescriptor — member field values (Table 11.6)."""

    def test_identifiable_children_via_create_factories(self, parser):
        """Test that NV-BLOCK-NEEDS, RAM-BLOCK and ROM-BLOCK are materialized through the create-factories with their short names."""
        element = _snip(
            "<SHORT-NAME>Desc</SHORT-NAME>"
            "<NV-BLOCK-NEEDS><SHORT-NAME>Needs</SHORT-NAME></NV-BLOCK-NEEDS>"
            "<RAM-BLOCK><SHORT-NAME>Ram</SHORT-NAME></RAM-BLOCK>"
            "<ROM-BLOCK><SHORT-NAME>Rom</SHORT-NAME></ROM-BLOCK>",
            root_tag="NV-BLOCK-DESCRIPTOR",
        )

        descriptor = NvBlockDescriptor(None, "Desc")
        parser.readNvBlockDescriptor(element, descriptor)

        needs = descriptor.getNvBlockNeeds()
        assert isinstance(needs, NvBlockNeeds)
        assert needs.getShortName() == "Needs"
        ram_block = descriptor.getRamBlock()
        assert isinstance(ram_block, VariableDataPrototype)
        assert ram_block.getShortName() == "Ram"
        rom_block = descriptor.getRomBlock()
        assert isinstance(rom_block, ParameterDataPrototype)
        assert rom_block.getShortName() == "Rom"

    def test_scalar_members_field_values(self, parser):
        """Test that SUPPORT-DIRTY-FLAG and TIMING-EVENT-REF are read with their spec-typed values."""
        element = _snip(
            "<SUPPORT-DIRTY-FLAG>true</SUPPORT-DIRTY-FLAG>" "<TIMING-EVENT-REF DEST='TIMING-EVENT'>/TimingEvent</TIMING-EVENT-REF>",
            root_tag="NV-BLOCK-DESCRIPTOR",
        )

        descriptor = NvBlockDescriptor(None, "Desc")
        parser.readNvBlockDescriptor(element, descriptor)

        flag = descriptor.getSupportDirtyFlag()
        assert isinstance(flag, Boolean)
        assert flag.getValue() is True
        ref = descriptor.getTimingEventRef()
        assert isinstance(ref, RefType)
        assert ref.getValue() == "/TimingEvent"
        assert ref.getDest() == "TIMING-EVENT"

    def test_list_members_read_in_wrapper_form(self, parser):
        """Test that the wrapper-form list members are read into their dedicated lists."""
        element = _snip(
            "<CONSTANT-VALUE-MAPPING-REFS><CONSTANT-VALUE-MAPPING-REF DEST='CONSTANT-SPECIFICATION'>/ConstMap</CONSTANT-VALUE-MAPPING-REF></CONSTANT-VALUE-MAPPING-REFS>"
            "<NV-BLOCK-DATA-MAPPINGS><NV-BLOCK-DATA-MAPPING/></NV-BLOCK-DATA-MAPPINGS>",
            root_tag="NV-BLOCK-DESCRIPTOR",
        )

        descriptor = NvBlockDescriptor(None, "Desc")
        parser.readNvBlockDescriptor(element, descriptor)

        assert len(descriptor.getConstantValueMappingRefs()) == 1
        assert descriptor.getConstantValueMappingRefs()[0].getValue() == "/ConstMap"
        assert len(descriptor.getNvBlockDataMappings()) == 1

    def test_absent_members_left_at_defaults(self, parser):
        """Test that an empty element leaves every member at its default."""
        element = _snip("", root_tag="NV-BLOCK-DESCRIPTOR")

        descriptor = NvBlockDescriptor(None, "Desc")
        parser.readNvBlockDescriptor(element, descriptor)

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
