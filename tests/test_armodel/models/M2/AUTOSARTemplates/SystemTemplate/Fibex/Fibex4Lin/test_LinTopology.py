"""
Test suite for LinTopology classes in AUTOSAR System Template.

This module contains comprehensive unit tests for LIN communication topology classes
including LIN communication controllers, master nodes, connectors, and related components.
Each test validates the functionality, inheritance, and setter/getter methods
of the respective classes.
"""

import sys
from typing import Optional, get_type_hints

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinCommunicationConnector, LinCommunicationController, LinConfigurableFrame, LinMaster, LinSlaveConfigIdent
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationConnector, CommunicationController


class MockParent(ARObject):
    """
    Mock parent class for testing purposes.

    This class extends ARObject to provide a concrete implementation
    that can be used as a parent for testing classes that require
    an ARObject instance during initialization.
    """

    def __init__(self):
        super().__init__()


class _ConcreteController(LinCommunicationController):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class TestLinCommunicationController:
    """
    LIN bus specific communication controller attributes.
    """

    def test_abstract_instantiation(self):
        parent = MockParent()

        with pytest.raises(TypeError, match="LinCommunicationController is an abstract class"):
            LinCommunicationController(parent, "TestController")

    def test_initialization(self):
        parent = MockParent()
        controller = _ConcreteController(parent, "TestController")

        assert controller.getShortName() == "TestController"
        assert isinstance(controller, CommunicationController)
        assert controller.getProtocolVersion() is None

    def test_get_set_protocol_version(self):
        parent = MockParent()
        controller = _ConcreteController(parent, "TestController")

        assert controller == controller.setProtocolVersion("LIN22")
        assert controller.getProtocolVersion() == "LIN22"

        assert controller == controller.setProtocolVersion(None)
        assert controller.getProtocolVersion() == "LIN22"

    def test_type_annotations(self):
        import ast
        import inspect

        getter_hints = get_type_hints(_ConcreteController.getProtocolVersion)
        assert getter_hints["return"] == Optional[String]

        setter_hints = get_type_hints(_ConcreteController.setProtocolVersion)
        assert setter_hints["value"] == Optional[String]
        assert setter_hints["return"] == LinCommunicationController

        src = inspect.getsource(sys.modules[LinCommunicationController.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "LinCommunicationController")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.unparse(node.annotation)
        assert annotations["protocolVersion"] == "Optional[String]"


class TestLinSlaveConfigIdent:
    """
    This meta-class is created to add the ability to become the target of a reference to the non-Referrable Lin SlaveConfig.
    """

    def test_initialization(self):
        parent = MockParent()
        ident = LinSlaveConfigIdent(parent, "SlaveConfigIdent")

        assert ident.getShortName() == "SlaveConfigIdent"
        assert isinstance(ident, Referrable)
        assert isinstance(ident, ARObject)
        assert ident.getParent() is parent

    def test_no_own_attributes(self):
        import ast
        import inspect

        src = inspect.getsource(sys.modules[LinSlaveConfigIdent.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "LinSlaveConfigIdent")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.unparse(node.annotation)
        assert annotations == {}


class TestLinTopology:
    """
    Test class for LinTopology module functionality.

    This class contains test methods for validating the behavior of
    LIN communication topology classes, including their initialization,
    inheritance relationships, and property accessors.
    """

    def test_lin_communication_controller(self):
        """
        Test the LinCommunicationController abstract class.
        """
        parent = MockParent()

        # Test that LinCommunicationController cannot be instantiated directly
        with pytest.raises(TypeError, match="LinCommunicationController is an abstract class"):
            LinCommunicationController(parent, "TestController")

        # Test that a concrete subclass can be instantiated
        controller = LinMaster(parent, "TestController")

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


class TestLinConfigurableFrame:
    """
    Assignment of messageIds to Frames. This element shall be used for the LIN 2.0 Assign-Frame command.
    """

    def test_initialization(self):
        obj = LinConfigurableFrame()

        assert isinstance(obj, ARObject)
        assert obj.parent is None
        assert obj.getFrameRef() is None
        assert obj.getMessageId() is None

    def test_get_set_frame_ref(self):
        obj = LinConfigurableFrame()

        ref = "/System/LinFrame"
        assert obj == obj.setFrameRef(ref)
        assert obj.getFrameRef() == ref

        assert obj == obj.setFrameRef(None)
        assert obj.getFrameRef() == ref

    def test_get_set_message_id(self):
        obj = LinConfigurableFrame()

        assert obj == obj.setMessageId(42)
        assert obj.getMessageId() == 42

        assert obj == obj.setMessageId(None)
        assert obj.getMessageId() == 42

    def test_type_annotations(self):
        import ast
        import inspect

        getter_hints = get_type_hints(LinConfigurableFrame.getFrameRef)
        assert getter_hints["return"] == Optional[RefType]

        setter_hints = get_type_hints(LinConfigurableFrame.setFrameRef)
        assert setter_hints["value"] == Optional[RefType]
        assert setter_hints["return"] == LinConfigurableFrame

        getter_hints = get_type_hints(LinConfigurableFrame.getMessageId)
        assert getter_hints["return"] == Optional[PositiveInteger]

        setter_hints = get_type_hints(LinConfigurableFrame.setMessageId)
        assert setter_hints["value"] == Optional[PositiveInteger]
        assert setter_hints["return"] == LinConfigurableFrame

        src = inspect.getsource(sys.modules[LinConfigurableFrame.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "LinConfigurableFrame")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.unparse(node.annotation)
        assert annotations["frameRef"] == "Optional[RefType]"
        assert annotations["messageId"] == "Optional[PositiveInteger]"
