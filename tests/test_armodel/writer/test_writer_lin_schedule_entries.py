"""Round-trip tests for LIN schedule table entries (Tables 6.96-6.108)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    ApplicationEntry,
    AssignFrameId,
    AssignFrameIdRange,
    AssignNad,
    ConditionalChangeNad,
    DataDumpEntry,
    FramePid,
    FreeFormat,
    LinScheduleTable,
    SaveConfigurationEntry,
    UnassignFrameId,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
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


def _pkg():
    autosar = AUTOSAR.getInstance()
    return autosar.createARPackage("Pkg")


def _int(value):
    val = Integer()
    val.setValue(value)
    return val


def _pos_int(value):
    val = PositiveInteger()
    val.setValue(value)
    return val


def _time(value):
    val = TimeValue()
    val.setValue(value)
    return val


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _doc_block(text):
    block = DocumentationBlock()
    paragraph = MultiLanguageParagraph()
    l1 = LOverviewParagraph()
    l1.setL("EN")
    l1.setValue(text)
    paragraph.addL1(l1)
    block.addP(paragraph)
    return block


def _build_table(pkg) -> LinScheduleTable:
    table = LinScheduleTable(pkg, "Table")

    application = ApplicationEntry()
    application.setDelay(_time("0.01"))
    application.setPositionInTable(_int(0))
    application.setFrameTriggeringRef(_ref("LIN-FRAME-TRIGGERING", "/ft0"))
    table.addTableEntry(application)

    free_format = FreeFormat()
    free_format.setDelay(_time("0.02"))
    free_format.setPositionInTable(_int(1))
    free_format.addByteValue(_int(1))
    free_format.addByteValue(_int(2))
    table.addTableEntry(free_format)

    assign_frame_id = AssignFrameId()
    assign_frame_id.setDelay(_time("0.03"))
    assign_frame_id.setAssignedControllerRef(_ref("LIN-SLAVE", "/slave"))
    assign_frame_id.setAssignedLinSlaveConfigRef(_ref("LIN-SLAVE-CONFIG-IDENT", "/ident"))
    assign_frame_id.setAssignedFrameTriggeringRef(_ref("LIN-FRAME-TRIGGERING", "/ft1"))
    table.addTableEntry(assign_frame_id)

    unassign_frame_id = UnassignFrameId()
    unassign_frame_id.setPositionInTable(_int(2))
    unassign_frame_id.setUnassignedFrameTriggeringRef(_ref("LIN-FRAME-TRIGGERING", "/ft2"))
    table.addTableEntry(unassign_frame_id)

    frame_pid = FramePid()
    frame_pid.setIndex(_int(0))
    frame_pid.setPid(_pos_int(0x30))
    range_entry = AssignFrameIdRange()
    range_entry.setStartIndex(_int(4))
    range_entry.addFramePid(frame_pid)
    table.addTableEntry(range_entry)

    assign_nad = AssignNad()
    assign_nad.setNewNad(_int(0x7F))
    table.addTableEntry(assign_nad)

    conditional_change_nad = ConditionalChangeNad()
    conditional_change_nad.setByte(_int(1))
    conditional_change_nad.setId(_pos_int(2))
    conditional_change_nad.setInvert(_int(3))
    conditional_change_nad.setMask(_int(4))
    conditional_change_nad.setNewNad(_int(5))
    table.addTableEntry(conditional_change_nad)

    save_configuration = SaveConfigurationEntry()
    save_configuration.setPositionInTable(_int(3))
    table.addTableEntry(save_configuration)

    data_dump = DataDumpEntry()
    data_dump.addByteValue(_int(8))
    data_dump.addByteValue(_int(9))
    table.addTableEntry(data_dump)

    return table


class TestLinScheduleTableEntriesRoundTrip:
    def test_roundtrip_all_entry_types(self, writer):
        pkg = _pkg()
        table = _build_table(pkg)

        parent = _parent()
        writer.writeLinScheduleTable(parent, table)

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = LinScheduleTable(pkg, "Table2")
        parser.readLinScheduleTable(ET.fromstring(xml_str)[0], reloaded)

        entries = reloaded.getTableEntries()
        assert len(entries) == 9

        application = entries[0]
        assert isinstance(application, ApplicationEntry)
        assert application.getDelay().getValue() == 0.01
        assert application.getPositionInTable().getValue() == 0
        assert application.getFrameTriggeringRef().getValue() == "/ft0"

        free_format = entries[1]
        assert isinstance(free_format, FreeFormat)
        assert [v.getValue() for v in free_format.getByteValues()] == [1, 2]

        assign_frame_id = entries[2]
        assert isinstance(assign_frame_id, AssignFrameId)
        assert assign_frame_id.getDelay().getValue() == 0.03
        assert assign_frame_id.getAssignedControllerRef().getValue() == "/slave"
        assert assign_frame_id.getAssignedControllerRef().getDest() == "LIN-SLAVE"
        assert assign_frame_id.getAssignedLinSlaveConfigRef().getValue() == "/ident"
        assert assign_frame_id.getAssignedFrameTriggeringRef().getValue() == "/ft1"

        unassign_frame_id = entries[3]
        assert isinstance(unassign_frame_id, UnassignFrameId)
        assert unassign_frame_id.getUnassignedFrameTriggeringRef().getValue() == "/ft2"

        range_entry = entries[4]
        assert isinstance(range_entry, AssignFrameIdRange)
        assert range_entry.getStartIndex().getValue() == 4
        assert len(range_entry.getFramePids()) == 1
        assert range_entry.getFramePids()[0].getIndex().getValue() == 0
        assert range_entry.getFramePids()[0].getPid().getValue() == 0x30

        assign_nad = entries[5]
        assert isinstance(assign_nad, AssignNad)
        assert assign_nad.getNewNad().getValue() == 0x7F

        conditional_change_nad = entries[6]
        assert isinstance(conditional_change_nad, ConditionalChangeNad)
        assert conditional_change_nad.getByte().getValue() == 1
        assert conditional_change_nad.getId().getValue() == 2
        assert conditional_change_nad.getInvert().getValue() == 3
        assert conditional_change_nad.getMask().getValue() == 4
        assert conditional_change_nad.getNewNad().getValue() == 5

        save_configuration = entries[7]
        assert isinstance(save_configuration, SaveConfigurationEntry)
        assert save_configuration.getPositionInTable().getValue() == 3

        data_dump = entries[8]
        assert isinstance(data_dump, DataDumpEntry)
        assert [v.getValue() for v in data_dump.getByteValues()] == [8, 9]

    def test_written_xml_element_structure(self, writer):
        pkg = _pkg()
        table = _build_table(pkg)

        parent = _parent()
        writer.writeLinScheduleTable(parent, table)

        child = parent.find("LIN-SCHEDULE-TABLE")
        assert child is not None
        entries_element = child.find("TABLE-ENTRYS")
        assert entries_element is not None

        tags = [e.tag for e in entries_element]
        assert tags == [
            "APPLICATION-ENTRY",
            "FREE-FORMAT",
            "ASSIGN-FRAME-ID",
            "UNASSIGN-FRAME-ID",
            "ASSIGN-FRAME-ID-RANGE",
            "ASSIGN-NAD",
            "CONDITIONAL-CHANGE-NAD",
            "SAVE-CONFIGURATION-ENTRY",
            "DATA-DUMP-ENTRY",
        ]

        assign_frame_id_element = entries_element.find("ASSIGN-FRAME-ID")
        assert assign_frame_id_element.find("DELAY") is not None
        assert assign_frame_id_element.find("POSITION-IN-TABLE") is None
        assert assign_frame_id_element.find("ASSIGNED-CONTROLLER-REF").text == "/slave"
        assert assign_frame_id_element.find("ASSIGNED-LIN-SLAVE-CONFIG-REF").text == "/ident"
        assert assign_frame_id_element.find("ASSIGNED-FRAME-TRIGGERING-REF").text == "/ft1"

    def test_roundtrip_introduction_before_delay(self, writer):
        pkg = _pkg()
        table = LinScheduleTable(pkg, "Table")

        entry = FreeFormat()
        entry.setDelay(_time("0.05"))
        entry.setIntroduction(_doc_block("entry introduction"))
        entry.setPositionInTable(_int(7))
        table.addTableEntry(entry)

        parent = _parent()
        writer.writeLinScheduleTable(parent, table)

        entry_element = parent.find("LIN-SCHEDULE-TABLE/TABLE-ENTRYS/FREE-FORMAT")
        assert entry_element is not None
        tags = [e.tag for e in entry_element]
        assert tags.index("INTRODUCTION") < tags.index("DELAY")
        assert tags.index("DELAY") < tags.index("POSITION-IN-TABLE")

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = LinScheduleTable(pkg, "Table2")
        parser.readLinScheduleTable(ET.fromstring(xml_str)[0], reloaded)

        loaded = reloaded.getTableEntries()[0]
        assert isinstance(loaded, FreeFormat)
        assert loaded.getIntroduction() is not None
        assert loaded.getIntroduction().getPs()[0].getL1s()[0].getValue() == "entry introduction"
        assert loaded.getDelay().getValue() == 0.05
        assert loaded.getPositionInTable().getValue() == 7

    def test_roundtrip_empty_base_fields(self, writer):
        pkg = _pkg()
        table = LinScheduleTable(pkg, "Table")

        entry = AssignNad()
        entry.setNewNad(_int(0x7F))
        table.addTableEntry(entry)

        parent = _parent()
        writer.writeLinScheduleTable(parent, table)

        entry_element = parent.find("LIN-SCHEDULE-TABLE/TABLE-ENTRYS/ASSIGN-NAD")
        assert entry_element is not None
        assert entry_element.find("DELAY") is None
        assert entry_element.find("INTRODUCTION") is None
        assert entry_element.find("POSITION-IN-TABLE") is None

        xml_str = ET.tostring(parent, encoding="unicode").replace("<PARENT>", "<PARENT xmlns='http://autosar.org/schema/r4.0'>", 1)
        parser = ARXMLParser()
        reloaded = LinScheduleTable(pkg, "Table2")
        parser.readLinScheduleTable(ET.fromstring(xml_str)[0], reloaded)

        loaded = reloaded.getTableEntries()[0]
        assert isinstance(loaded, AssignNad)
        assert loaded.getDelay() is None
        assert loaded.getIntroduction() is None
        assert loaded.getPositionInTable() is None
        assert loaded.getNewNad().getValue() == 0x7F
