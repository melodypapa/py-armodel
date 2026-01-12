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
        with pytest.raises(NotImplementedError):
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
        
        # Test setter/getter methods
        triggering.setIdentifier(60)
        assert triggering.getIdentifier() == 60

    def test_ResumePosition(self):
        """Test ResumePosition enum functionality."""
        enum = ResumePosition()
        assert enum is not None
        assert ResumePosition.CONTINUE_AT_IT_POSITION in enum.getEnumValues()
        assert ResumePosition.START_FROM_BEGINNING in enum.getEnumValues()

    def test_ScheduleTableEntry(self):
        """Test ScheduleTableEntry abstract class instantiation."""
        with pytest.raises(NotImplementedError):
            ScheduleTableEntry()

    def test_ApplicationEntry(self):
        """Test ApplicationEntry class functionality."""
        entry = ApplicationEntry()

        assert isinstance(entry, ScheduleTableEntry)
        
        # Test default values
        assert entry.getFrameTriggeringRef() is None
        
        # Test setter/getter methods
        entry.setFrameTriggeringRef("triggering_ref")
        assert entry.getFrameTriggeringRef() == "triggering_ref"

    def test_FreeFormatEntry(self):
        """Test FreeFormatEntry class functionality."""
        entry = FreeFormatEntry()

        assert isinstance(entry, ScheduleTableEntry)

    def test_LinConfigurationEntry(self):
        """Test LinConfigurationEntry abstract class instantiation."""
        with pytest.raises(NotImplementedError):
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
        
        # Test setter/getter methods
        table.setResumePosition(ResumePosition.START_FROM_BEGINNING)
        assert table.getResumePosition() == ResumePosition.START_FROM_BEGINNING
        
        # Test adding table entries
        entry = ApplicationEntry()
        table.addTableEntry(entry)
        assert table.getTableEntries() == [entry]


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
        controller = LinCommunicationController(parent, "test_lin_comm_controller")

        assert isinstance(controller, CommunicationController)
        
        # Test default values
        assert controller.getProtocolVersion() is None
        
        # Test setter/getter methods
        controller.setProtocolVersion("2.1")
        assert controller.getProtocolVersion() == "2.1"

    def test_LinMaster(self):
        """Test LinMaster class functionality."""
        parent = MockParent()
        master = LinMaster(parent, "test_lin_master")

        assert isinstance(master, LinCommunicationController)
        
        # Test default values
        assert master.getLinSlaves() == []
        assert master.getTimeBase() is None
        assert master.getTimeBaseJitter() is None
        
        # Test setter/getter methods
        master.setTimeBase("100ms")
        assert master.getTimeBase() == "100ms"
        
        # Test adding LIN slaves
        master.addLinSlaves("slave_ref")
        assert master.getLinSlaves() == ["slave_ref"]

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
        
        # Test setter/getter methods
        connector.setInitialNad(10)
        assert connector.getInitialNad() == 10
        
        connector.setScheduleChangeNextTimeBase(True)
        assert connector.getScheduleChangeNextTimeBase() is True