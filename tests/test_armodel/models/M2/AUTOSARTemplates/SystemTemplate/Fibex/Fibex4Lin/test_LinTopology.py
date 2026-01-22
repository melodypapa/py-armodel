"""
Test suite for LinTopology classes in AUTOSAR System Template.

This module contains comprehensive unit tests for LIN communication topology classes
including LIN communication controllers, master nodes, connectors, and related components.
Each test validates the functionality, inheritance, and setter/getter methods
of the respective classes.
"""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import (
    LinCommunicationController,
    LinMaster,
    LinCommunicationConnector
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationController, CommunicationConnector


class MockParent(ARObject):
    """
    Mock parent class for testing purposes.
    
    This class extends ARObject to provide a concrete implementation
    that can be used as a parent for testing classes that require
    an ARObject instance during initialization.
    """
    def __init__(self):
        super().__init__()


class TestLinTopology:
    """
    Test class for LinTopology module functionality.
    
    This class contains test methods for validating the behavior of
    LIN communication topology classes, including their initialization,
    inheritance relationships, and property accessors.
    """

    def test_lin_communication_controller(self):
        """
        Test the LinCommunicationController class initialization and methods.
        """
        parent = MockParent()
        controller = LinCommunicationController(parent, "TestController")
        
        assert controller.getShortName() == "TestController"
        assert isinstance(controller, CommunicationController)
        assert controller.getProtocolVersion() is None
        
        # Test setting protocol version
        controller.setProtocolVersion("2.1")
        assert controller.getProtocolVersion() == "2.1"

    def test_lin_master(self):
        """
        Test the LinMaster class initialization and methods.
        """
        parent = MockParent()
        master = LinMaster(parent, "TestMaster")
        
        assert master.getShortName() == "TestMaster"
        assert isinstance(master, LinCommunicationController)
        assert master.getLinSlaves() == []
        assert master.getTimeBase() is None
        assert master.getTimeBaseJitter() is None
        
        # Test setting values
        master.setTimeBase("10ms")
        master.setTimeBaseJitter("0.1ms")
        
        assert master.getTimeBase() == "10ms"
        assert master.getTimeBaseJitter() == "0.1ms"
        
        # Test adding LIN slaves
        master.addLinSlaves("slave1")
        master.addLinSlaves("slave2")
        assert master.getLinSlaves() == ["slave1", "slave2"]

    def test_lin_communication_connector(self):
        """
        Test the LinCommunicationConnector class initialization and methods.
        """
        parent = MockParent()
        connector = LinCommunicationConnector(parent, "TestConnector")
        
        assert connector.getShortName() == "TestConnector"
        assert isinstance(connector, CommunicationConnector)
        assert connector.getInitialNad() is None
        assert connector.getLinConfigurableFrames() == []
        assert connector.getLinOrderedConfigurableFrames() == []
        assert connector.getScheduleChangeNextTimeBase() is None
        
        # Test setting values
        connector.setInitialNad(10)
        connector.setScheduleChangeNextTimeBase(True)
        
        assert connector.getInitialNad() == 10
        assert connector.getScheduleChangeNextTimeBase() is True
        
        # Test adding configurable frames
        connector.addLinConfigurableFrame("frame1")
        connector.addLinConfigurableFrame("frame2")
        assert connector.getLinConfigurableFrames() == ["frame1", "frame2"]
        
        # Test adding ordered configurable frames
        connector.addLinOrderedConfigurableFrame("ordered_frame1")
        connector.addLinOrderedConfigurableFrame("ordered_frame2")
        assert connector.getLinOrderedConfigurableFrames() == ["ordered_frame1", "ordered_frame2"]