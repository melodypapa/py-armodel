import inspect
import sys
from typing import List, Optional, get_type_hints

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    ApplicationEntry,
    AssignFrameId,
    AssignFrameIdRange,
    AssignNad,
    ConditionalChangeNad,
    DataDumpEntry,
    FramePid,
    FreeFormat,
    FreeFormatEntry,
    LinConfigurationEntry,
    LinErrorResponse,
    LinFrame,
    LinFrameTriggering,
    LinScheduleTable,
    LinUnconditionalFrame,
    ResumePosition,
    RunMode,
    SaveConfigurationEntry,
    ScheduleTableEntry,
    UnassignFrameId,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCommunicationConnector, LinCommunicationController, LinMaster, LinSlaveConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector, CommunicationController
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock

CLASS_NOTE_RESUME_POSITION = "Defines, where a schedule table shall be proceeded in case if it has been interrupted by a run-once table or MRF/SRF."


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


LIN_ERROR_RESPONSE_CLASS_NOTE = (
    "Each slave node shall publish a one bit signal, named response_error, to the master node in one of its transmitted unconditional frames. "
    "The response_error signal shall be set whenever a frame (except for event triggered frame responses) that is transmitted or received by the slave node contains an error in the frame response. "
    "The response_error signal shall be cleared when the unconditional frame containing the response_error signal is successfully transmitted."
)
LIN_ERROR_RESPONSE_RESPONSE_ERROR_NOTE = "This ISignal shall be taken to transport the responseError bit."


class TestLinErrorResponse:
    """Test cases for LinErrorResponse (Table 3.42, p.97)."""

    def test_inheritance(self):
        """Test the most-derived base from the Base chain (Table 3.42: ARObject)"""
        assert issubclass(LinErrorResponse, ARObject)

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.42)"""
        assert inspect.cleandoc(LinErrorResponse.__doc__).strip() == LIN_ERROR_RESPONSE_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert LinErrorResponse.__init__.__doc__ is None

    def test_initialization(self):
        obj = LinErrorResponse()

        assert isinstance(obj, ARObject)
        assert obj.parent is None
        assert obj.getResponseErrorRef() is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.42: responseError)"""
        source = inspect.getsource(LinErrorResponse.__init__)
        assert source.index("self.responseErrorRef") >= 0

    def test_get_set_response_error_ref(self):
        obj = LinErrorResponse()

        ref = RefType()
        ref.setValue("/System/ISignalTriggering")

        assert obj == obj.setResponseErrorRef(ref)
        assert obj.getResponseErrorRef() == ref

        assert obj == obj.setResponseErrorRef(None)
        assert obj.getResponseErrorRef() == ref

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_member_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.42)"""
        self._assert_docstring(LinErrorResponse.getResponseErrorRef, LIN_ERROR_RESPONSE_RESPONSE_ERROR_NOTE)
        self._assert_docstring(LinErrorResponse.setResponseErrorRef, LIN_ERROR_RESPONSE_RESPONSE_ERROR_NOTE, "responseErrorRef")

    def test_type_annotations(self):
        import ast
        import inspect

        getter_hints = get_type_hints(LinErrorResponse.getResponseErrorRef)
        assert getter_hints["return"] == Optional[RefType]

        setter_hints = get_type_hints(LinErrorResponse.setResponseErrorRef)
        assert setter_hints["value"] == Optional[RefType]
        assert setter_hints["return"] == LinErrorResponse

        src = inspect.getsource(sys.modules[LinErrorResponse.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "LinErrorResponse")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["responseErrorRef"] == "Optional[RefType]"


class TestResumePosition:
    """Test cases for ResumePosition (Table 6.95, p.432)."""

    def test_member_presence_and_values(self):
        assert ResumePosition.CONTINUE_AT_IT_POSITION == "CONTINUE-AT-IT-POSITION"
        assert ResumePosition.START_FROM_BEGINNING == "START-FROM-BEGINNING"
        assert list(ResumePosition().getEnumValues()) == ["CONTINUE-AT-IT-POSITION", "START-FROM-BEGINNING"]

    def test_instantiability(self):
        enum = ResumePosition()
        assert enum == enum.setValue(ResumePosition.CONTINUE_AT_IT_POSITION)
        assert enum.getValue() == ResumePosition.CONTINUE_AT_IT_POSITION

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ResumePosition.__doc__) == CLASS_NOTE_RESUME_POSITION


class Test_Fibex4LinCommunication:
    """Test cases for Fibex4Lin Communication classes."""

    def test_LinFrame(self):
        """Test LinFrame abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(TypeError):
            LinFrame(parent, "test_lin_frame")

    def test_LinUnconditionalFrame(self):
        """Test LinUnconditionalFrame class functionality."""
        parent = MockParent()
        frame = LinUnconditionalFrame(parent, "test_lin_unconditional_frame")

        assert isinstance(frame, Frame)
        assert isinstance(frame, LinFrame)

    def test_LinFrameTriggering(self):
        """Test LinFrameTriggering class functionality."""
        parent = MockParent()
        triggering = LinFrameTriggering(parent, "test_lin_frame_triggering")

        assert isinstance(triggering, FrameTriggering)

        # Test default values
        assert triggering.getIdentifier() is None
        assert triggering.getLinChecksum() is None

        # Test setter/getter methods with method chaining
        result = triggering.setIdentifier(60)
        assert triggering.getIdentifier() == 60
        assert result == triggering  # Test method chaining

        # Test setting None value to cover 'if value is not None' condition
        # The setter doesn't actually set the value to None, it just returns self
        result = triggering.setIdentifier(None)
        assert triggering.getIdentifier() == 60  # Value should still be 60 since None was not set
        assert result == triggering  # Test method chaining

        result = triggering.setLinChecksum("checksum")
        assert triggering.getLinChecksum() == "checksum"
        assert result == triggering  # Test method chaining

        result = triggering.setLinChecksum(None)
        assert triggering.getLinChecksum() == "checksum"  # Value should still be "checksum" since None was not set
        assert result == triggering  # Test method chaining

    def test_ResumePosition(self):
        """Test ResumePosition enum functionality."""
        enum = ResumePosition()
        assert enum is not None
        assert ResumePosition.CONTINUE_AT_IT_POSITION in enum.getEnumValues()
        assert ResumePosition.START_FROM_BEGINNING in enum.getEnumValues()

    def test_ScheduleTableEntry(self):
        """Test ScheduleTableEntry abstract class instantiation."""
        with pytest.raises(TypeError):
            ScheduleTableEntry()

    def test_ApplicationEntry(self):
        """Test ApplicationEntry class functionality."""
        entry = ApplicationEntry()

        assert isinstance(entry, ScheduleTableEntry)

        # Test default values
        assert entry.getFrameTriggeringRef() is None
        assert entry.getDelay() is None
        assert entry.getIntroduction() is None
        assert entry.getPositionInTable() is None

        # Test setter/getter methods with method chaining
        result = entry.setFrameTriggeringRef("triggering_ref")
        assert entry.getFrameTriggeringRef() == "triggering_ref"
        assert result == entry  # Test method chaining

        # Test setting None value to cover 'if value is not None' condition
        # The setter doesn't actually set the value to None, it just returns self
        result = entry.setFrameTriggeringRef(None)
        assert entry.getFrameTriggeringRef() == "triggering_ref"  # Value should still be "triggering_ref" since None was not set
        assert result == entry  # Test method chaining

        result = entry.setDelay("10ms")
        assert entry.getDelay() == "10ms"
        assert result == entry  # Test method chaining

        # Test setting None value to cover 'if value is not None' condition
        result = entry.setDelay(None)
        assert entry.getDelay() == "10ms"  # Value should still be "10ms" since None was not set
        assert result == entry  # Test method chaining

        result = entry.setIntroduction("intro_text")
        assert entry.getIntroduction() == "intro_text"
        assert result == entry  # Test method chaining

        # Test setting None value to cover 'if value is not None' condition
        result = entry.setIntroduction(None)
        assert entry.getIntroduction() == "intro_text"  # Value should still be "intro_text" since None was not set
        assert result == entry  # Test method chaining

        result = entry.setPositionInTable(5)
        assert entry.getPositionInTable() == 5
        assert result == entry  # Test method chaining

        # Test setting None value to cover 'if value is not None' condition
        # setPositionInTable also has the 'if value is not None:' check
        result = entry.setPositionInTable(None)
        assert entry.getPositionInTable() == 5  # Value should still be 5 since None was not set
        assert result == entry  # Test method chaining

    def test_FreeFormatEntry(self):
        """Test FreeFormatEntry abstract class functionality."""
        # Test that FreeFormatEntry cannot be instantiated directly
        with pytest.raises(TypeError, match="FreeFormatEntry is an abstract class"):
            FreeFormatEntry()

        # Test that a concrete subclass can be instantiated and use inherited methods
        class ConcreteFreeFormatEntry(FreeFormatEntry):
            pass

        entry = ConcreteFreeFormatEntry()

        assert isinstance(entry, ScheduleTableEntry)

        # Test inherited setter/getter methods with method chaining
        result = entry.setDelay("5ms")
        assert entry.getDelay() == "5ms"
        assert result == entry  # Test method chaining

        # Test setting None value to cover 'if value is not None' condition
        result = entry.setDelay(None)
        assert entry.getDelay() == "5ms"  # Value should still be "5ms" since None was not set
        assert result == entry  # Test method chaining

        result = entry.setIntroduction("free_format_intro")
        assert entry.getIntroduction() == "free_format_intro"
        assert result == entry  # Test method chaining

        # Test setting None value to cover 'if value is not None' condition
        result = entry.setIntroduction(None)
        assert entry.getIntroduction() == "free_format_intro"  # Value should still be "free_format_intro" since None was not set
        assert result == entry  # Test method chaining

        result = entry.setPositionInTable(10)
        assert entry.getPositionInTable() == 10
        assert result == entry  # Test method chaining

    def test_LinConfigurationEntry(self):
        """Test LinConfigurationEntry abstract class instantiation."""
        with pytest.raises(TypeError):
            LinConfigurationEntry()

    def test_LinScheduleTable(self):
        """Test LinScheduleTable class functionality."""
        parent = MockParent()
        table = LinScheduleTable(parent, "test_lin_schedule_table")

        assert isinstance(table, Identifiable)

        # Test default values
        assert table.getResumePosition() is None
        assert table.getRunMode() is None
        assert table.getTableEntries() == []

        # Test setter/getter methods with method chaining
        result = table.setResumePosition(ResumePosition.START_FROM_BEGINNING)
        assert table.getResumePosition() == ResumePosition.START_FROM_BEGINNING
        assert result == table  # Test method chaining

        # Test setting None value to ensure we cover the 'if value is not None' condition
        # This should not change the value since the condition prevents setting None
        result = table.setResumePosition(None)
        assert table.getResumePosition() == ResumePosition.START_FROM_BEGINNING  # Still the original value
        assert result == table  # Test method chaining

        result = table.setRunMode("run_mode")
        assert table.getRunMode() == "run_mode"
        assert result == table  # Test method chaining

        # Test setting None value for run mode to cover 'if value is not None' condition
        result = table.setRunMode(None)
        assert table.getRunMode() == "run_mode"  # Value should still be "run_mode" since None was not set
        assert result == table  # Test method chaining

        # Test adding table entries with method chaining
        entry = ApplicationEntry()
        result = table.addTableEntry(entry)
        assert table.getTableEntries() == [entry]
        assert result == table  # Test method chaining

        # Test adding None to table entries to cover 'if value is not None' condition
        result = table.addTableEntry(None)
        assert table.getTableEntries() == [entry]  # Should still be [entry] since None was not added
        assert result == table  # Test method chaining


class TestLinFrame:
    """
    Lin specific Frame element.
    """

    def test_abstract_instantiation(self):
        with pytest.raises(TypeError):
            LinFrame(MockParent(), "test_lin_frame")

    def test_concrete_subclass(self):
        frame = LinUnconditionalFrame(MockParent(), "test_lin_unconditional_frame")

        assert isinstance(frame, Frame)
        assert isinstance(frame, LinFrame)


class ConcreteLinConfigurationEntry(LinConfigurationEntry):
    pass


class TestScheduleTableEntry:
    """
    Table entry in a LinScheduleTable. Specifies what will be done in the frame slot.
    """

    def test_abstract_instantiation(self):
        with pytest.raises(TypeError):
            ScheduleTableEntry()

    def test_initialization(self):
        entry = ApplicationEntry()

        assert isinstance(entry, ARObject)
        assert isinstance(entry, ScheduleTableEntry)
        assert entry.getDelay() is None
        assert entry.getIntroduction() is None
        assert entry.getPositionInTable() is None

    def test_get_set_delay(self):
        entry = ApplicationEntry()
        delay = TimeValue().setValue(0.01)

        assert entry == entry.setDelay(delay)
        assert entry.getDelay() == delay

        entry.setDelay(None)
        assert entry.getDelay() == delay

    def test_get_set_introduction(self):
        entry = ApplicationEntry()
        block = DocumentationBlock()

        assert entry == entry.setIntroduction(block)
        assert entry.getIntroduction() == block

        entry.setIntroduction(None)
        assert entry.getIntroduction() == block

    def test_get_set_position_in_table(self):
        entry = ApplicationEntry()
        position = Integer().setValue(2)

        assert entry == entry.setPositionInTable(position)
        assert entry.getPositionInTable() == position

        entry.setPositionInTable(None)
        assert entry.getPositionInTable() == position

    def test_type_annotations(self):
        import ast
        import inspect

        getter_hints = get_type_hints(ScheduleTableEntry.getDelay)
        assert getter_hints["return"] == Optional[TimeValue]

        setter_hints = get_type_hints(ScheduleTableEntry.setDelay)
        assert setter_hints["value"] == Optional[TimeValue]
        assert setter_hints["return"] == ScheduleTableEntry

        src = inspect.getsource(sys.modules[ScheduleTableEntry.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "ScheduleTableEntry")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["delay"] == "Optional[TimeValue]"
        assert annotations["introduction"] == "Optional[DocumentationBlock]"
        assert annotations["positionInTable"] == "Optional[Integer]"


CLASS_NOTE_APPLICATION_ENTRY = "Schedule table entry for application messages."


class TestApplicationEntry:
    """Test cases for ApplicationEntry (Table 6.97, p.433)."""

    def test_initialization(self):
        entry = ApplicationEntry()

        assert isinstance(entry, ARObject)
        assert isinstance(entry, ScheduleTableEntry)
        assert entry.getFrameTriggeringRef() is None

    def test_get_set_frame_triggering_ref(self):
        entry = ApplicationEntry()

        ref = RefType()
        ref.setDest("LIN-FRAME-TRIGGERING")
        ref.setValue("/LinCluster/LinFrameTriggering")

        assert entry == entry.setFrameTriggeringRef(ref)
        assert entry.getFrameTriggeringRef() == ref

        assert entry == entry.setFrameTriggeringRef(None)
        assert entry.getFrameTriggeringRef() == ref

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ApplicationEntry.__doc__) == CLASS_NOTE_APPLICATION_ENTRY

    def test_type_annotations(self):
        import ast

        getter_hints = get_type_hints(ApplicationEntry.getFrameTriggeringRef)
        assert getter_hints["return"] == Optional[RefType]

        setter_hints = get_type_hints(ApplicationEntry.setFrameTriggeringRef)
        assert setter_hints["value"] == Optional[RefType]
        assert setter_hints["return"] == ApplicationEntry

        src = inspect.getsource(sys.modules[ApplicationEntry.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "ApplicationEntry")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["frameTriggeringRef"] == "Optional[RefType]"


CLASS_NOTE_RUN_MODE = "The schedule table can be executed in two different modes."


class TestRunMode:
    """Test cases for RunMode (Table 6.94, p.432)."""

    def test_member_presence_and_values(self):
        assert RunMode.RUN_CONTINUOUS == "RUN-CONTINUOUS"
        assert RunMode.RUN_ONCE == "RUN-ONCE"
        assert list(RunMode().getEnumValues()) == ["RUN-CONTINUOUS", "RUN-ONCE"]

    def test_instantiability(self):
        enum = RunMode()
        assert enum == enum.setValue(RunMode.RUN_CONTINUOUS)
        assert enum.getValue() == RunMode.RUN_CONTINUOUS

    def test_class_docstring_note(self):
        assert inspect.cleandoc(RunMode.__doc__) == CLASS_NOTE_RUN_MODE


CLASS_NOTE_LIN_SCHEDULE_TABLE = (
    "The master task (in the master node) transmits frame headers based on a schedule table. "
    "The schedule table specifies the identifiers for each header and the interval between the start of a frame and the start of the following frame."
)


class TestLinScheduleTable:
    """Test cases for LinScheduleTable (Table 6.93, p.432)."""

    def test_initialization(self):
        parent = MockParent()
        table = LinScheduleTable(parent, "tbl")

        assert isinstance(table, Identifiable)
        assert isinstance(table, VariationPointCapable)
        assert table.getResumePosition() is None
        assert table.getRunMode() is None
        assert table.getTableEntries() == []

    def test_get_set_resume_position(self):
        parent = MockParent()
        table = LinScheduleTable(parent, "tbl")
        position = ResumePosition().setValue(ResumePosition.CONTINUE_AT_IT_POSITION)

        assert table == table.setResumePosition(position)
        assert table.getResumePosition() == position

        assert table == table.setResumePosition(None)
        assert table.getResumePosition() == position

    def test_get_set_run_mode(self):
        parent = MockParent()
        table = LinScheduleTable(parent, "tbl")
        mode = RunMode().setValue(RunMode.RUN_CONTINUOUS)

        assert table == table.setRunMode(mode)
        assert table.getRunMode() == mode

        assert table == table.setRunMode(None)
        assert table.getRunMode() == mode

    def test_add_table_entry(self):
        parent = MockParent()
        table = LinScheduleTable(parent, "tbl")
        entry = ApplicationEntry()

        assert table == table.addTableEntry(entry)
        assert table.getTableEntries() == [entry]

        second = ApplicationEntry()
        table.addTableEntry(second)
        assert table.getTableEntries() == [entry, second]

        assert table == table.addTableEntry(None)
        assert table.getTableEntries() == [entry, second]

    def test_class_docstring_note(self):
        assert inspect.cleandoc(LinScheduleTable.__doc__) == CLASS_NOTE_LIN_SCHEDULE_TABLE

    def test_type_annotations(self):
        import ast

        getter_hints = get_type_hints(LinScheduleTable.getResumePosition)
        assert getter_hints["return"] == Optional[ResumePosition]

        setter_hints = get_type_hints(LinScheduleTable.setResumePosition)
        assert setter_hints["value"] == Optional[ResumePosition]
        assert setter_hints["return"] == LinScheduleTable

        getter_hints = get_type_hints(LinScheduleTable.getRunMode)
        assert getter_hints["return"] == Optional[RunMode]

        setter_hints = get_type_hints(LinScheduleTable.setRunMode)
        assert setter_hints["value"] == Optional[RunMode]
        assert setter_hints["return"] == LinScheduleTable

        entries_hints = get_type_hints(LinScheduleTable.getTableEntries)
        assert entries_hints["return"] == List[ScheduleTableEntry]

        add_hints = get_type_hints(LinScheduleTable.addTableEntry)
        assert add_hints["value"] == Optional[ScheduleTableEntry]
        assert add_hints["return"] == LinScheduleTable

        src = inspect.getsource(sys.modules[LinScheduleTable.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "LinScheduleTable")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["resumePosition"] == "Optional[ResumePosition]"
        assert annotations["runMode"] == "Optional[RunMode]"
        assert annotations["tableEntries"] == "List[ScheduleTableEntry]"


class TestLinConfigurationEntry:
    """
    A ScheduleTableEntry which contains LIN specific assignments.
    """

    def _create_entry(self) -> ConcreteLinConfigurationEntry:
        return ConcreteLinConfigurationEntry()

    def test_initialization(self):
        entry = self._create_entry()

        assert isinstance(entry, ScheduleTableEntry)
        assert entry.getAssignedControllerRef() is None
        assert entry.getAssignedLinSlaveConfigRef() is None

    def test_get_set_assigned_controller_ref(self):
        entry = self._create_entry()

        ref = "/System/LinCluster/Connector"
        assert entry == entry.setAssignedControllerRef(ref)
        assert entry.getAssignedControllerRef() == ref

        assert entry == entry.setAssignedControllerRef(None)
        assert entry.getAssignedControllerRef() == ref

    def test_get_set_assigned_lin_slave_config_ref(self):
        entry = self._create_entry()

        ref = "/System/LinCluster/SlaveConfigIdent"
        assert entry == entry.setAssignedLinSlaveConfigRef(ref)
        assert entry.getAssignedLinSlaveConfigRef() == ref

        assert entry == entry.setAssignedLinSlaveConfigRef(None)
        assert entry.getAssignedLinSlaveConfigRef() == ref

    def test_type_annotations(self):
        import ast
        import inspect

        getter_hints = get_type_hints(LinConfigurationEntry.getAssignedControllerRef)
        assert getter_hints["return"] == Optional[RefType]

        setter_hints = get_type_hints(LinConfigurationEntry.setAssignedControllerRef)
        assert setter_hints["value"] == Optional[RefType]
        assert setter_hints["return"] == LinConfigurationEntry

        config_getter_hints = get_type_hints(LinConfigurationEntry.getAssignedLinSlaveConfigRef)
        assert config_getter_hints["return"] == Optional[RefType]

        config_setter_hints = get_type_hints(LinConfigurationEntry.setAssignedLinSlaveConfigRef)
        assert config_setter_hints["value"] == Optional[RefType]
        assert config_setter_hints["return"] == LinConfigurationEntry

        src = inspect.getsource(sys.modules[LinConfigurationEntry.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "LinConfigurationEntry")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["assignedControllerRef"] == "Optional[RefType]"
        assert annotations["assignedLinSlaveConfigRef"] == "Optional[RefType]"


class ConcreteFreeFormatEntry(FreeFormatEntry):
    pass


class TestLinConfigurationEntryFamily:
    """Concrete LinConfigurationEntry subclasses and FramePid (Tables 6.100-6.108)."""

    def test_frame_pid(self):
        frame_pid = FramePid()
        assert frame_pid.getIndex() is None
        assert frame_pid.getPid() is None

        assert frame_pid == frame_pid.setIndex(2)
        assert frame_pid.getIndex() == 2
        assert frame_pid == frame_pid.setPid(0x30)
        assert frame_pid.getPid() == 0x30

        assert frame_pid == frame_pid.setIndex(None)
        assert frame_pid.getIndex() == 2
        assert frame_pid == frame_pid.setPid(None)
        assert frame_pid.getPid() == 0x30

    def test_assign_frame_id(self):
        entry = AssignFrameId()
        assert isinstance(entry, LinConfigurationEntry)
        assert entry.getAssignedFrameTriggeringRef() is None
        assert entry.getAssignedControllerRef() is None
        assert entry.getAssignedLinSlaveConfigRef() is None

        assert entry == entry.setAssignedFrameTriggeringRef("/Cluster/FT")
        assert entry.getAssignedFrameTriggeringRef() == "/Cluster/FT"
        assert entry == entry.setAssignedControllerRef("/Cluster/Slave")
        assert entry == entry.setAssignedLinSlaveConfigRef("/Cluster/Ident")

        assert entry == entry.setAssignedFrameTriggeringRef(None)
        assert entry.getAssignedFrameTriggeringRef() == "/Cluster/FT"

    def test_unassign_frame_id(self):
        entry = UnassignFrameId()
        assert isinstance(entry, LinConfigurationEntry)
        assert entry.getUnassignedFrameTriggeringRef() is None

        assert entry == entry.setUnassignedFrameTriggeringRef("/Cluster/FT")
        assert entry.getUnassignedFrameTriggeringRef() == "/Cluster/FT"
        assert entry == entry.setUnassignedFrameTriggeringRef(None)
        assert entry.getUnassignedFrameTriggeringRef() == "/Cluster/FT"

    def test_assign_frame_id_range(self):
        entry = AssignFrameIdRange()
        assert isinstance(entry, LinConfigurationEntry)
        assert entry.getFramePids() == []
        assert entry.getStartIndex() is None

        frame_pid = FramePid()
        assert entry == entry.addFramePid(frame_pid)
        assert entry.getFramePids() == [frame_pid]
        assert entry == entry.addFramePid(None)
        assert entry.getFramePids() == [frame_pid]

        assert entry == entry.setStartIndex(3)
        assert entry.getStartIndex() == 3
        assert entry == entry.setStartIndex(None)
        assert entry.getStartIndex() == 3

    def test_assign_nad(self):
        entry = AssignNad()
        assert isinstance(entry, LinConfigurationEntry)
        assert entry.getNewNad() is None

        assert entry == entry.setNewNad(0x7F)
        assert entry.getNewNad() == 0x7F
        assert entry == entry.setNewNad(None)
        assert entry.getNewNad() == 0x7F

    def test_conditional_change_nad(self):
        entry = ConditionalChangeNad()
        assert isinstance(entry, LinConfigurationEntry)
        assert entry.getByte() is None
        assert entry.getId() is None
        assert entry.getInvert() is None
        assert entry.getMask() is None
        assert entry.getNewNad() is None

        assert entry == entry.setByte(1)
        assert entry == entry.setId(2)
        assert entry == entry.setInvert(3)
        assert entry == entry.setMask(4)
        assert entry == entry.setNewNad(5)
        assert (entry.getByte(), entry.getId(), entry.getInvert(), entry.getMask(), entry.getNewNad()) == (1, 2, 3, 4, 5)

        assert entry == entry.setId(None)
        assert entry.getId() == 2

    def test_save_configuration_entry(self):
        entry = SaveConfigurationEntry()
        assert isinstance(entry, LinConfigurationEntry)

    def test_data_dump_entry(self):
        entry = DataDumpEntry()
        assert isinstance(entry, LinConfigurationEntry)
        assert entry.getByteValues() == []

        assert entry == entry.addByteValue(1)
        assert entry == entry.addByteValue(2)
        assert entry.getByteValues() == [1, 2]
        assert entry == entry.addByteValue(None)
        assert entry.getByteValues() == [1, 2]

    def test_free_format(self):
        entry = FreeFormat()
        assert isinstance(entry, FreeFormatEntry)
        assert entry.getByteValues() == []

        assert entry == entry.addByteValue(0x10)
        assert entry == entry.addByteValue(0x20)
        assert entry.getByteValues() == [0x10, 0x20]
        assert entry == entry.addByteValue(None)
        assert entry.getByteValues() == [0x10, 0x20]


CONDITIONAL_CHANGE_NAD_CLASS_NOTE = "Generates an conditional change NAD request. See ISO 17987 protocol specification for more information."
CONDITIONAL_CHANGE_NAD_BYTE_NOTE = "Byte Position of Data Byte that should be used for the bitwise XOR with Invert and the bitwise AND with Mask."
CONDITIONAL_CHANGE_NAD_ID_NOTE = "Byte Position of Id."
CONDITIONAL_CHANGE_NAD_INVERT_NOTE = "Byte Position of Invert."
CONDITIONAL_CHANGE_NAD_MASK_NOTE = "Byte Position of Mask."
CONDITIONAL_CHANGE_NAD_NEW_NAD_NOTE = "The newly assigned NAD value (Byte Position)."


class TestConditionalChangeNad:
    """Test cases for ConditionalChangeNad (Table 6.105, p.438)."""

    def test_inheritance(self):
        """Test the most-derived base from the Base chain (Table 6.105: ARObject, LinConfigurationEntry, ScheduleTableEntry)"""
        assert issubclass(ConditionalChangeNad, LinConfigurationEntry)
        assert issubclass(ConditionalChangeNad, ScheduleTableEntry)

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 6.105)"""
        assert inspect.cleandoc(ConditionalChangeNad.__doc__).strip() == CONDITIONAL_CHANGE_NAD_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert ConditionalChangeNad.__init__.__doc__ is None

    def test_initialization(self):
        entry = ConditionalChangeNad()

        assert isinstance(entry, ARObject)
        assert entry.getByte() is None
        assert entry.getId() is None
        assert entry.getInvert() is None
        assert entry.getMask() is None
        assert entry.getNewNad() is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 6.105: byte, id, invert, mask, newNad)"""
        source = inspect.getsource(ConditionalChangeNad.__init__)
        assert source.index("self.byte") < source.index("self.id")
        assert source.index("self.id") < source.index("self.invert")
        assert source.index("self.invert") < source.index("self.mask")
        assert source.index("self.mask") < source.index("self.newNad")

    def test_get_set_byte(self):
        entry = ConditionalChangeNad()

        byte = Integer()
        byte.setValue(1)

        assert entry == entry.setByte(byte)
        assert entry.getByte() == byte

        assert entry == entry.setByte(None)
        assert entry.getByte() == byte

    def test_get_set_id(self):
        entry = ConditionalChangeNad()

        pid = PositiveInteger()
        pid.setValue(2)

        assert entry == entry.setId(pid)
        assert entry.getId() == pid

        assert entry == entry.setId(None)
        assert entry.getId() == pid

    def test_get_set_invert(self):
        entry = ConditionalChangeNad()

        invert = Integer()
        invert.setValue(3)

        assert entry == entry.setInvert(invert)
        assert entry.getInvert() == invert

        assert entry == entry.setInvert(None)
        assert entry.getInvert() == invert

    def test_get_set_mask(self):
        entry = ConditionalChangeNad()

        mask = Integer()
        mask.setValue(4)

        assert entry == entry.setMask(mask)
        assert entry.getMask() == mask

        assert entry == entry.setMask(None)
        assert entry.getMask() == mask

    def test_get_set_new_nad(self):
        entry = ConditionalChangeNad()

        new_nad = Integer()
        new_nad.setValue(5)

        assert entry == entry.setNewNad(new_nad)
        assert entry.getNewNad() == new_nad

        assert entry == entry.setNewNad(None)
        assert entry.getNewNad() == new_nad

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_member_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 6.105)"""
        self._assert_docstring(ConditionalChangeNad.getByte, CONDITIONAL_CHANGE_NAD_BYTE_NOTE)
        self._assert_docstring(ConditionalChangeNad.setByte, CONDITIONAL_CHANGE_NAD_BYTE_NOTE, "byte")
        self._assert_docstring(ConditionalChangeNad.getId, CONDITIONAL_CHANGE_NAD_ID_NOTE)
        self._assert_docstring(ConditionalChangeNad.setId, CONDITIONAL_CHANGE_NAD_ID_NOTE, "id")
        self._assert_docstring(ConditionalChangeNad.getInvert, CONDITIONAL_CHANGE_NAD_INVERT_NOTE)
        self._assert_docstring(ConditionalChangeNad.setInvert, CONDITIONAL_CHANGE_NAD_INVERT_NOTE, "invert")
        self._assert_docstring(ConditionalChangeNad.getMask, CONDITIONAL_CHANGE_NAD_MASK_NOTE)
        self._assert_docstring(ConditionalChangeNad.setMask, CONDITIONAL_CHANGE_NAD_MASK_NOTE, "mask")
        self._assert_docstring(ConditionalChangeNad.getNewNad, CONDITIONAL_CHANGE_NAD_NEW_NAD_NOTE)
        self._assert_docstring(ConditionalChangeNad.setNewNad, CONDITIONAL_CHANGE_NAD_NEW_NAD_NOTE, "newNad")

    def test_type_annotations(self):
        import ast

        expected_members = {
            "byte": (Integer, "Optional[Integer]"),
            "id": (PositiveInteger, "Optional[PositiveInteger]"),
            "invert": (Integer, "Optional[Integer]"),
            "mask": (Integer, "Optional[Integer]"),
            "newNad": (Integer, "Optional[Integer]"),
        }
        for attr, (py_type, annotation) in expected_members.items():
            getter = getattr(ConditionalChangeNad, "get%s%s" % (attr[0].upper(), attr[1:]))
            setter = getattr(ConditionalChangeNad, "set%s%s" % (attr[0].upper(), attr[1:]))

            getter_hints = get_type_hints(getter)
            assert getter_hints["return"] == Optional[py_type]

            setter_hints = get_type_hints(setter)
            assert setter_hints["value"] == Optional[py_type]
            assert setter_hints["return"] == ConditionalChangeNad

        src = inspect.getsource(sys.modules[ConditionalChangeNad.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "ConditionalChangeNad")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        for attr, (_, annotation) in expected_members.items():
            assert annotations[attr] == annotation


SAVE_CONFIGURATION_ENTRY_CLASS_NOTE = "This service is used to notify a slave node to store its configuration."


class TestSaveConfigurationEntry:
    """Test cases for SaveConfigurationEntry (Table 6.106, p.439)."""

    def test_inheritance(self):
        """Test the most-derived base from the Base chain (Table 6.106: ARObject, LinConfigurationEntry, ScheduleTableEntry)"""
        assert issubclass(SaveConfigurationEntry, LinConfigurationEntry)
        assert issubclass(SaveConfigurationEntry, ScheduleTableEntry)

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 6.106)"""
        assert inspect.cleandoc(SaveConfigurationEntry.__doc__).strip() == SAVE_CONFIGURATION_ENTRY_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert SaveConfigurationEntry.__init__.__doc__ is None

    def test_initialization(self):
        entry = SaveConfigurationEntry()

        assert isinstance(entry, ARObject)
        assert entry.getAssignedControllerRef() is None
        assert entry.getAssignedLinSlaveConfigRef() is None


class Test_Fibex4LinTopology:
    """Test cases for Fibex4Lin Topology classes."""

    def test_LinCommunicationController(self):
        """Test LinCommunicationController class functionality."""
        parent = MockParent()
        controller = LinMaster(parent, "test_lin_comm_controller")

        assert isinstance(controller, CommunicationController)

        # Test default values
        assert controller.getProtocolVersion() is None

        # Test setter/getter methods with method chaining
        result = controller.setProtocolVersion("2.1")
        assert controller.getProtocolVersion() == "2.1"
        assert result == controller  # Test method chaining

        # Test setting None value to cover 'if value is not None' condition
        result = controller.setProtocolVersion(None)
        assert controller.getProtocolVersion() == "2.1"  # Value should still be "2.1" since None was not set
        assert result == controller  # Test method chaining

    def test_LinMaster(self):
        """Test LinMaster class functionality."""
        parent = MockParent()
        master = LinMaster(parent, "test_lin_master")

        assert isinstance(master, LinCommunicationController)

        # Test default values
        assert master.getLinSlaves() == []
        assert master.getTimeBase() is None
        assert master.getTimeBaseJitter() is None

        # Test setter/getter methods with method chaining
        result = master.setTimeBase("100ms")
        assert master.getTimeBase() == "100ms"
        assert result == master  # Test method chaining

        # Test setting None value to cover 'if value is not None' condition (if it has that pattern)
        result = master.setTimeBase(None)
        assert master.getTimeBase() == "100ms"  # Value should still be "100ms" since None was not set
        assert result == master  # Test method chaining

        result = master.setTimeBaseJitter("5ms")
        assert master.getTimeBaseJitter() == "5ms"
        assert result == master  # Test method chaining

        result = master.setTimeBaseJitter(None)
        assert master.getTimeBaseJitter() == "5ms"  # Value should still be "5ms" since None was not set
        assert result == master  # Test method chaining

        # Test adding LIN slaves with method chaining
        result = master.addLinSlave(LinSlaveConfig())
        assert len(master.getLinSlaves()) == 1
        assert result == master  # Test method chaining

    def test_LinCommunicationConnector(self):
        """Test LinCommunicationConnector class functionality."""
        parent = MockParent()
        connector = LinCommunicationConnector(parent, "test_lin_comm_connector")

        assert isinstance(connector, CommunicationConnector)

        # Test default values
        assert connector.getInitialNad() is None
        assert connector.getLinConfigurableFrames() == []
        assert connector.getLinOrderedConfigurableFrames() == []
        assert connector.getScheduleChangeNextTimeBase() is None

        # Test setter/getter methods with method chaining
        result = connector.setInitialNad(10)
        assert connector.getInitialNad() == 10
        assert result == connector  # Test method chaining

        result = connector.setInitialNad(None)
        assert connector.getInitialNad() == 10  # Value should still be 10 since None was not set
        assert result == connector  # Test method chaining

        result = connector.setScheduleChangeNextTimeBase(True)
        assert connector.getScheduleChangeNextTimeBase() is True
        assert result == connector  # Test method chaining

        # Test setting None value for Boolean field
        result = connector.setScheduleChangeNextTimeBase(None)
        assert connector.getScheduleChangeNextTimeBase() is True  # Value should still be True since None was not set
        assert result == connector  # Test method chaining

        # Test adding LIN configurable frames with method chaining
        result = connector.addLinConfigurableFrame("frame_ref")
        assert connector.getLinConfigurableFrames() == ["frame_ref"]
        assert result == connector  # Test method chaining

        # Test adding LIN ordered configurable frames with method chaining
        result = connector.addLinOrderedConfigurableFrame("ordered_frame_ref")
        assert connector.getLinOrderedConfigurableFrames() == ["ordered_frame_ref"]
        assert result == connector  # Test method chaining

    def test_LinConfigurationEntry_concrete_subclass(self):
        """Test LinConfigurationEntry via concrete subclass to cover line 153 (super().__init__())."""
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinConfigurationEntry

        # Create a concrete subclass to test the abstract class
        class ConcreteLinConfigurationEntry(LinConfigurationEntry):
            def __init__(self):
                super().__init__()

        # Instantiate the concrete subclass, which calls super().__init__() on line 153
        entry = ConcreteLinConfigurationEntry()
        assert entry is not None
        # The super().__init__() call is now covered
