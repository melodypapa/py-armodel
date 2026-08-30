"""Tests for the NvBlockDataMapping writer handler."""

import xml.etree.cElementTree as ET
from unittest.mock import MagicMock

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarVariableRef  # noqa E501
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _posint(value):
    p = PositiveInteger()
    p.setValue(str(value))
    return p


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _bool(value):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean

    b = ARBoolean()
    b.setValue(value)
    return b


def _mapping():
    mapping = NvBlockDataMapping()
    mapping.setBitfieldTextTableMaskNvBlockDescriptor(_posint(10))
    mapping.setBitfieldTextTableMaskPortPrototype(_posint(32))

    read_ref = AutosarVariableRef()
    read_iref = MagicMock()
    read_iref.getPortPrototypeRef.return_value = _ref("/readPort")
    read_ref.setAutosarVariableIRef(read_iref)
    mapping.setReadNvData(read_ref)

    ram_ref = AutosarVariableRef()
    ram_iref = MagicMock()
    ram_iref.getPortPrototypeRef.return_value = _ref("/ramPort")
    ram_ref.setAutosarVariableIRef(ram_iref)
    mapping.setNvRamBlockElement(ram_ref)
    return mapping


class TestWriteNvBlockDataMapping:
    """Exercise the writeNvBlockDataMapping handler."""

    def test_write_nv_block_data_mapping_full(self, writer):
        parent = _parent()
        writer.writeNvBlockDataMapping(parent, _mapping())
        elem = parent.find("NV-BLOCK-DATA-MAPPING")
        assert elem is not None
        assert elem.find("BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR").text == "10"
        assert elem.find("BITFIELD-TEXT-TABLE-MASK-PORT-PROTOTYPE").text == "32"
        assert elem.find("NV-RAM-BLOCK-ELEMENT") is not None
        assert elem.find("READ-NV-DATA") is not None

    def test_write_nv_block_data_mapping_minimal(self, writer):
        parent = _parent()
        writer.writeNvBlockDataMapping(parent, NvBlockDataMapping())
        elem = parent.find("NV-BLOCK-DATA-MAPPING")
        assert elem is not None
        assert elem.find("BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR") is None
        assert elem.find("READ-NV-DATA") is None


class TestWriteBulkNvDataDescriptor:
    """Exercise the writeBulkNvDataDescriptor handler."""

    def test_write_bulk_nv_data_descriptor_full(self, writer):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype  # noqa E501
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor  # noqa E501

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = BulkNvDataDescriptor(root, "BulkDesc")
        block = VariableDataPrototype(root, "RamBlock")
        descriptor.setBulkNvBlock(block)
        descriptor.addNvBlockDataMapping(_mapping())
        parent = _parent()
        writer.writeBulkNvDataDescriptor(parent, descriptor)
        elem = parent.find("BULK-NV-DATA-DESCRIPTOR")
        assert elem is not None
        assert elem.find("SHORT-NAME").text == "BulkDesc"
        assert elem.find("BULK-NV-BLOCK/VARIABLE-DATA-PROTOTYPE/SHORT-NAME").text == "RamBlock"
        assert elem.find("NV-BLOCK-DATA-MAPPINGS/NV-BLOCK-DATA-MAPPING") is not None

    def test_write_bulk_nv_data_descriptor_minimal(self, writer):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor  # noqa E501

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = BulkNvDataDescriptor(root, "BulkDesc")
        parent = _parent()
        writer.writeBulkNvDataDescriptor(parent, descriptor)
        elem = parent.find("BULK-NV-DATA-DESCRIPTOR")
        assert elem is not None
        assert elem.find("BULK-NV-BLOCK") is None
        assert elem.find("NV-BLOCK-DATA-MAPPINGS") is None


class TestWriteNvBlockDescriptor:
    """Exercise the writeNvBlockDescriptor handler."""

    def test_write_nv_block_descriptor_full(self, writer):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import NvBlockNeeds, RoleBasedDataAssignment  # noqa E501
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (  # noqa E501
            ParameterDataPrototype,
            VariableDataPrototype,
        )
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "NvBlockDesc")
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity  # noqa E501
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps  # noqa E501
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedPortAssignment  # noqa E501

        descriptor.addClientServerPort(RoleBasedPortAssignment())
        descriptor.addConstantValueMappingRef(_ref("/ConstMapping"))
        descriptor.addDataTypeMappingRef(_ref("/DataTypeMapping"))
        descriptor.addInstantiationDataDefProps(InstantiationDataDefProps())
        descriptor.addModeSwitchEventTriggeredActivity(ModeSwitchEventTriggeredActivity())
        descriptor.addNvBlockDataMapping(_mapping())
        descriptor.setNvBlockNeeds(NvBlockNeeds(root, "NvNeeds"))
        descriptor.setRamBlock(VariableDataPrototype(root, "RamBlock"))
        descriptor.setRomBlock(ParameterDataPrototype(root, "RomBlock"))
        descriptor.setSupportDirtyFlag(_bool(True))
        descriptor.setTimingEventRef(_ref("/TimingEvent"))
        descriptor.addWritingStrategy(RoleBasedDataAssignment())
        parent = _parent()
        writer.writeNvBlockDescriptor(parent, descriptor)
        elem = parent.find("NV-BLOCK-DESCRIPTOR")
        assert elem is not None
        assert elem.find("SHORT-NAME").text == "NvBlockDesc"
        assert elem.find("CLIENT-SERVER-PORTS/ROLE-BASED-PORT-ASSIGNMENT") is not None
        assert elem.find("CONSTANT-VALUE-MAPPING-REFS/CONSTANT-VALUE-MAPPING-REF") is not None
        assert elem.find("DATA-TYPE-MAPPING-REFS/DATA-TYPE-MAPPING-REF") is not None
        assert elem.find("INSTANTIATION-DATA-DEF-PROPSS/INSTANTIATION-DATA-DEF-PROPS") is not None
        assert elem.find("MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS/MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY") is not None
        assert elem.find("NV-BLOCK-DATA-MAPPINGS/NV-BLOCK-DATA-MAPPING") is not None
        assert elem.find("NV-BLOCK-NEEDS") is not None
        assert elem.find("RAM-BLOCK/SHORT-NAME").text == "RamBlock"
        assert elem.find("ROM-BLOCK/SHORT-NAME").text == "RomBlock"
        assert elem.find("SUPPORT-DIRTY-FLAG").text == "true"
        assert elem.find("TIMING-EVENT-REF") is not None
        assert elem.find("WRITING-STRATEGYS/ROLE-BASED-DATA-ASSIGNMENT") is not None

    def test_write_nv_block_descriptor_minimal(self, writer):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor  # noqa E501

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "NvBlockDesc")
        parent = _parent()
        writer.writeNvBlockDescriptor(parent, descriptor)
        elem = parent.find("NV-BLOCK-DESCRIPTOR")
        assert elem is not None
        assert elem.find("NV-BLOCK-DATA-MAPPINGS") is None
        assert elem.find("NV-BLOCK-NEEDS") is None
        assert elem.find("RAM-BLOCK") is None
        assert elem.find("WRITING-STRATEGYS") is None

    def test_write_mode_switch_event_triggered_activity(self, writer):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import ModeSwitchEventTriggeredActivity  # noqa E501

        activity = ModeSwitchEventTriggeredActivity()
        role = ARLiteral()
        role.setValue("WriteBlock")
        activity.setRole(role)
        activity.setSwcModeSwitchEventRef(_ref("/SwcModeSwitchEvent"))
        parent = _parent()
        writer.writeModeSwitchEventTriggeredActivity(parent, activity)
        elem = parent.find("MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY")
        assert elem is not None
        assert elem.find("ROLE").text == "WriteBlock"
        assert elem.find("SWC-MODE-SWITCH-EVENT-REF") is not None
