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
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean

    b = Boolean()
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


def _real_variable_ref(port_value):
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import (
        VariableInAtomicSWCTypeInstanceRef,
    )

    port_ref = RefType()
    port_ref.setValue(port_value)
    port_ref.setDest("PORT-PROTOTYPE")
    ref = AutosarVariableRef()
    iref = VariableInAtomicSWCTypeInstanceRef()
    iref.setPortPrototypeRef(port_ref)
    ref.setAutosarVariableIRef(iref)
    return ref


def _full_mapping():
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, String

    mapping = NvBlockDataMapping()
    mapping.setBitfieldTextTableMaskNvBlockDescriptor(_posint(10))
    mapping.setBitfieldTextTableMaskPortPrototype(_posint(32))
    mapping.setNvRamBlockElement(_real_variable_ref("/ramPort"))
    mapping.setReadNvData(_real_variable_ref("/readPort"))
    mapping.setWrittenNvData(_real_variable_ref("/writtenPort"))
    mapping.setWrittenReadNvData(_real_variable_ref("/writtenReadPort"))

    checksum = String()
    checksum.setValue("abc123")
    mapping.setChecksum(checksum)
    timestamp = DateTime()
    timestamp.setValue("2024-01-01T12:00:00+00:00")
    mapping.setTimestamp(timestamp)
    return mapping


XSD_ELEMENT_ORDER = [
    "BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR",
    "BITFIELD-TEXT-TABLE-MASK-PORT-PROTOTYPE",
    "NV-RAM-BLOCK-ELEMENT",
    "READ-NV-DATA",
    "WRITTEN-NV-DATA",
    "WRITTEN-READ-NV-DATA",
]


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

    def test_write_nv_block_data_mapping_field_values(self, writer):
        """Test that all six Table 11.11 attribute elements are emitted with their values read through the getters."""
        parent = _parent()
        writer.writeNvBlockDataMapping(parent, _full_mapping())

        elem = parent.find("NV-BLOCK-DATA-MAPPING")
        assert elem is not None
        assert elem.find("BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR").text == "10"
        assert elem.find("BITFIELD-TEXT-TABLE-MASK-PORT-PROTOTYPE").text == "32"
        for tag, expected in [
            ("NV-RAM-BLOCK-ELEMENT", "/ramPort"),
            ("READ-NV-DATA", "/readPort"),
            ("WRITTEN-NV-DATA", "/writtenPort"),
            ("WRITTEN-READ-NV-DATA", "/writtenReadPort"),
        ]:
            ref_element = elem.find(tag)
            assert ref_element is not None
            assert ref_element.find("AUTOSAR-VARIABLE-IREF/PORT-PROTOTYPE-REF").text == expected

    def test_write_nv_block_data_mapping_xsd_element_order(self, writer):
        """Test that the element order follows the XSD group NV-BLOCK-DATA-MAPPING sequence."""
        parent = _parent()
        writer.writeNvBlockDataMapping(parent, _full_mapping())

        elem = parent.find("NV-BLOCK-DATA-MAPPING")
        assert [child.tag for child in elem] == XSD_ELEMENT_ORDER

    def test_write_nv_block_data_mapping_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) are emitted."""
        parent = _parent()
        writer.writeNvBlockDataMapping(parent, _full_mapping())

        elem = parent.find("NV-BLOCK-DATA-MAPPING")
        assert elem.attrib.get("S") == "abc123"
        assert elem.attrib.get("T") is not None


class TestNvBlockDataMappingRoundTrip:
    """Write → re-parse round-trip with field values (Table 11.11)."""

    NS = "http://autosar.org/schema/r4.0"

    def test_round_trip_field_values(self, writer):
        from armodel.parser.arxml_parser import ARXMLParser

        parent = _parent()
        writer.writeNvBlockDataMapping(parent, _full_mapping())
        elem = parent.find("NV-BLOCK-DATA-MAPPING")
        xml_text = ET.tostring(elem, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("NV-BLOCK-DATA-MAPPING", f"NV-BLOCK-DATA-MAPPING xmlns='{self.NS}'", 1))

        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping

        reloaded = NvBlockDataMapping()
        ARXMLParser().readNvBlockDataMapping(reloaded_element, reloaded)

        assert reloaded.getBitfieldTextTableMaskNvBlockDescriptor().getValue() == 10
        assert reloaded.getBitfieldTextTableMaskPortPrototype().getValue() == 32
        for getter, expected in [
            (reloaded.getNvRamBlockElement, "/ramPort"),
            (reloaded.getReadNvData, "/readPort"),
            (reloaded.getWrittenNvData, "/writtenPort"),
            (reloaded.getWrittenReadNvData, "/writtenReadPort"),
        ]:
            assert getter().getAutosarVariableIRef().getPortPrototypeRef().getValue() == expected
        assert reloaded.getChecksum() is not None
        assert reloaded.getChecksum().getValue() == "abc123"
        assert reloaded.getTimestamp() is not None

    def test_round_trip_absent_elements(self, writer):
        """Test that a mapping with unset fields round-trips without emitting the absent elements."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDataMapping
        from armodel.parser.arxml_parser import ARXMLParser

        parent = _parent()
        writer.writeNvBlockDataMapping(parent, NvBlockDataMapping())
        elem = parent.find("NV-BLOCK-DATA-MAPPING")
        assert elem.find("BITFIELD-TEXT-TABLE-MASK-NV-BLOCK-DESCRIPTOR") is None
        assert elem.find("WRITTEN-READ-NV-DATA") is None
        xml_text = ET.tostring(elem, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("NV-BLOCK-DATA-MAPPING", f"NV-BLOCK-DATA-MAPPING xmlns='{self.NS}'", 1))

        reloaded = NvBlockDataMapping()
        ARXMLParser().readNvBlockDataMapping(reloaded_element, reloaded)
        assert reloaded.getBitfieldTextTableMaskNvBlockDescriptor() is None
        assert reloaded.getNvRamBlockElement() is None
        assert reloaded.getReadNvData() is None
        assert reloaded.getWrittenNvData() is None
        assert reloaded.getWrittenReadNvData() is None


class TestWriteBulkNvDataDescriptor:
    """Exercise the writeBulkNvDataDescriptor handler."""

    def test_write_bulk_nv_data_descriptor_full(self, writer):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor  # noqa E501

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = BulkNvDataDescriptor(root, "BulkDesc")
        descriptor.createBulkNvBlock("RamBlock")
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

    def test_write_bulk_nv_data_descriptor_field_values(self, writer):
        """Test that both Table 11.12 attribute elements are emitted with values read through the getters."""
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor  # noqa E501

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = BulkNvDataDescriptor(root, "BulkDesc")
        descriptor.createBulkNvBlock("RamBlock")
        mapping = NvBlockDataMapping()
        mapping.setReadNvData(_real_variable_ref("/readPort"))
        mapping.setWrittenNvData(_real_variable_ref("/writtenPort"))
        descriptor.addNvBlockDataMapping(mapping)
        parent = _parent()
        writer.writeBulkNvDataDescriptor(parent, descriptor)

        elem = parent.find("BULK-NV-DATA-DESCRIPTOR")
        assert elem is not None
        assert elem.find("BULK-NV-BLOCK/VARIABLE-DATA-PROTOTYPE/SHORT-NAME").text == "RamBlock"
        mappings_elem = elem.find("NV-BLOCK-DATA-MAPPINGS")
        assert mappings_elem is not None
        mappings = mappings_elem.findall("NV-BLOCK-DATA-MAPPING")
        assert len(mappings) == 1
        assert mappings[0].find("READ-NV-DATA/AUTOSAR-VARIABLE-IREF/PORT-PROTOTYPE-REF").text == "/readPort"
        assert mappings[0].find("WRITTEN-NV-DATA/AUTOSAR-VARIABLE-IREF/PORT-PROTOTYPE-REF").text == "/writtenPort"

    def test_write_bulk_nv_data_descriptor_xsd_element_order(self, writer):
        """Test that the element order follows the XSD group BULK-NV-DATA-DESCRIPTOR sequence."""
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor  # noqa E501

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = BulkNvDataDescriptor(root, "BulkDesc")
        descriptor.createBulkNvBlock("RamBlock")
        descriptor.addNvBlockDataMapping(NvBlockDataMapping())
        parent = _parent()
        writer.writeBulkNvDataDescriptor(parent, descriptor)

        elem = parent.find("BULK-NV-DATA-DESCRIPTOR")
        assert [child.tag for child in elem] == ["SHORT-NAME", "BULK-NV-BLOCK", "NV-BLOCK-DATA-MAPPINGS"]


class TestBulkNvDataDescriptorRoundTrip:
    """Write → re-parse round-trip with field values (Table 11.12)."""

    NS = "http://autosar.org/schema/r4.0"

    def _round_trip(self, writer, descriptor):
        from armodel.parser.arxml_parser import ARXMLParser

        parent = _parent()
        writer.writeBulkNvDataDescriptor(parent, descriptor)
        elem = parent.find("BULK-NV-DATA-DESCRIPTOR")
        xml_text = ET.tostring(elem, encoding="unicode")
        reloaded_element = ET.fromstring(xml_text.replace("BULK-NV-DATA-DESCRIPTOR", f"BULK-NV-DATA-DESCRIPTOR xmlns='{self.NS}'", 1))

        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor

        root = AUTOSAR.getInstance().createARPackage("RtPkg")
        reloaded = BulkNvDataDescriptor(root, "BulkDesc")
        ARXMLParser().readBulkNvDataDescriptor(reloaded_element, reloaded)
        return reloaded

    def test_round_trip_field_values(self, writer):
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor, NvBlockDataMapping

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = BulkNvDataDescriptor(root, "BulkDesc")
        descriptor.createBulkNvBlock("RamBlock")
        mapping = NvBlockDataMapping()
        mapping.setReadNvData(_real_variable_ref("/readPort"))
        mapping.setWrittenReadNvData(_real_variable_ref("/prPort"))
        descriptor.addNvBlockDataMapping(mapping)
        checksum = String()
        checksum.setValue("bulkS")
        descriptor.setChecksum(checksum)

        reloaded = self._round_trip(writer, descriptor)

        assert reloaded.getShortName() == "BulkDesc"
        assert reloaded.getBulkNvBlock() is not None
        assert reloaded.getBulkNvBlock().getShortName() == "RamBlock"
        mappings = reloaded.getNvBlockDataMappings()
        assert len(mappings) == 1
        assert mappings[0].getReadNvData().getAutosarVariableIRef().getPortPrototypeRef().getValue() == "/readPort"
        assert mappings[0].getWrittenReadNvData().getAutosarVariableIRef().getPortPrototypeRef().getValue() == "/prPort"
        assert reloaded.getChecksum() is not None
        assert reloaded.getChecksum().getValue() == "bulkS"

    def test_round_trip_absent_elements(self, writer):
        """Test that an empty descriptor round-trips without emitting BULK-NV-BLOCK or the NV-BLOCK-DATA-MAPPINGS wrapper."""
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import BulkNvDataDescriptor

        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = BulkNvDataDescriptor(root, "BulkDesc")

        parent = _parent()
        writer.writeBulkNvDataDescriptor(parent, descriptor)
        elem = parent.find("BULK-NV-DATA-DESCRIPTOR")
        assert elem.find("BULK-NV-BLOCK") is None
        assert elem.find("NV-BLOCK-DATA-MAPPINGS") is None

        reloaded = self._round_trip(writer, descriptor)
        assert reloaded.getBulkNvBlock() is None
        assert reloaded.getNvBlockDataMappings() == []


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
        descriptor.createNvBlockNeeds("NvNeeds")
        descriptor.createRamBlock("RamBlock")
        descriptor.createRomBlock("RomBlock")
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
