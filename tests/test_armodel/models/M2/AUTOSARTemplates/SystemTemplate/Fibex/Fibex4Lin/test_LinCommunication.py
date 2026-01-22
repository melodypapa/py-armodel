import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import (
    LinFrame,
    LinUnconditionalFrame,
    LinFrameTriggering,
    ResumePosition,
    ScheduleTableEntry,
    ApplicationEntry,
    FreeFormatEntry,
    LinConfigurationEntry,
    LinScheduleTable
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame, FrameTriggering
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


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


from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import (
    LinCommunicationController,
    LinMaster,
    LinCommunicationConnector
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationController, CommunicationConnector


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
        result = master.addLinSlaves("slave_ref")
        assert master.getLinSlaves() == ["slave_ref"]
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

