"""
Test suite for LinTopology classes in AUTOSAR System Template.

This module contains comprehensive unit tests for LIN communication topology classes
including LIN communication controllers, master nodes, connectors, and related components.
Each test validates the functionality, inheritance, and setter/getter methods
of the respective classes.
"""

import ast
import inspect
import sys
from typing import List, Optional, get_type_hints

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, PositiveInteger, RefType, String, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinErrorResponse
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import (
    LinCluster,
    LinCommunicationConnector,
    LinCommunicationController,
    LinConfigurableFrame,
    LinMaster,
    LinOrderedConfigurableFrame,
    LinSlave,
    LinSlaveConfig,
    LinSlaveConfigIdent,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import CommunicationCluster, CommunicationConnector, CommunicationController, FibexElement


class MockParent(ARObject):
    """
    Mock parent class for testing purposes.

    This class extends ARObject to provide a concrete implementation
    that can be used as a parent for testing classes that require
    an ARObject instance during initialization.
    """

    def __init__(self):
        super().__init__()


LIN_COMMUNICATION_CONTROLLER_CLASS_NOTE = "LIN bus specific communication controller attributes."
LIN_MASTER_CLASS_NOTE = "Describing the properties of the refering ecu as a LIN master."
LIN_SLAVE_CLASS_NOTE = "Describing the properties of the referring ecu as a LIN slave."
LIN_SLAVE_NOTE = "LinSlaves that are handled by the LinMaster."
LIN_SLAVE_ASSIGN_NAD_NOTE = "This attribute has the ability to control whether the node configuration command 'Assign NAD' is supported."
LIN_SLAVE_CONFIGURED_NAD_NOTE = "To distinguish LIN slaves that are used twice or more within the same cluster."
LIN_SLAVE_FUNCTION_ID_NOTE = "LIN function ID"
LIN_SLAVE_INITIAL_NAD_NOTE = "This attribute represents the initial NAD."
LIN_SLAVE_LIN_ERROR_RESPONSE_NOTE = "Each slave node shall publish one response error in one of its transmitted unconditional frames."
LIN_SLAVE_NAS_TIMEOUT_NOTE = "Value of the N_AS timeout. Unit: seconds."
LIN_SLAVE_SUPPLIER_ID_NOTE = "LIN Supplier ID"
LIN_SLAVE_VARIANT_ID_NOTE = "Specifies the Variant ID"
TIME_BASE_NOTE = 'Time base is mandatory for the master. It is not used for slaves. LIN 2.0 Spec states: "The time_base value specifies the used time base in the master node to generate the maximum allowed frame transfer time." The time base shall be specified AUTOSAR conform in seconds.'
TIME_BASE_JITTER_NOTE = 'The attribute timeBaseJitter is a mandatory attribute for the master and not used for slaves. LIN 2.0 Spec states: "The jitter value specifies the differences between the maximum and minimum delay from time base start point to the frame header sending start point (falling edge of BREAK signal)." The jitter shall be specified AUTOSAR conform in seconds.'
PROTOCOL_VERSION_NOTE = "Version specifier for a communication protocol."


class _ConcreteController(LinCommunicationController):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class TestLinCommunicationController:
    """
    LIN bus specific communication controller attributes.
    """

    def test_inheritance(self):
        """Test the most-derived base from the Base chain (Table 3.37: ARObject, CommunicationController, Identifiable, MultilanguageReferrable, Referrable)"""
        assert issubclass(LinCommunicationController, CommunicationController)
        assert issubclass(LinCommunicationController, ARObject)

    def test_abstract_instantiation(self):
        parent = MockParent()

        with pytest.raises(TypeError, match="LinCommunicationController is an abstract class"):
            LinCommunicationController(parent, "TestController")

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.37)"""
        assert inspect.cleandoc(LinCommunicationController.__doc__).strip() == LIN_COMMUNICATION_CONTROLLER_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert LinCommunicationController.__init__.__doc__ is None

    def test_initialization(self):
        parent = MockParent()
        controller = _ConcreteController(parent, "TestController")

        assert controller.getShortName() == "TestController"
        assert isinstance(controller, CommunicationController)
        assert controller.getProtocolVersion() is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.37)"""
        source = inspect.getsource(LinCommunicationController.__init__)
        assert source.index("self.protocolVersion") >= 0

    def test_get_set_protocol_version(self):
        parent = MockParent()
        controller = _ConcreteController(parent, "TestController")

        assert controller == controller.setProtocolVersion("LIN22")
        assert controller.getProtocolVersion() == "LIN22"

        assert controller == controller.setProtocolVersion(None)
        assert controller.getProtocolVersion() == "LIN22"

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_protocol_version_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.37)"""
        self._assert_docstring(LinCommunicationController.getProtocolVersion, PROTOCOL_VERSION_NOTE)
        self._assert_docstring(LinCommunicationController.setProtocolVersion, PROTOCOL_VERSION_NOTE, "protocolVersion")

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
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["protocolVersion"] == "Optional[String]"


class TestLinMaster:
    """
    Describing the properties of the refering ecu as a LIN master.
    """

    def test_inheritance(self):
        """Test the most-derived base from the Base chain (Table 3.38: ARObject, CommunicationController, Identifiable, LinCommunicationController, MultilanguageReferrable, Referrable)"""
        assert issubclass(LinMaster, LinCommunicationController)
        assert issubclass(LinMaster, CommunicationController)
        assert issubclass(LinMaster, ARObject)

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.38)"""
        assert inspect.cleandoc(LinMaster.__doc__).strip() == LIN_MASTER_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert LinMaster.__init__.__doc__ is None

    def test_initialization(self):
        parent = MockParent()
        master = LinMaster(parent, "TestMaster")

        assert master.getShortName() == "TestMaster"
        assert master.getParent() is parent
        assert isinstance(master, LinCommunicationController)
        assert isinstance(master, CommunicationController)
        assert isinstance(master, ARObject)

        assert master.getProtocolVersion() is None
        assert master.getLinSlaves() == []
        assert master.getTimeBase() is None
        assert master.getTimeBaseJitter() is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.38: linSlave, timeBase, timeBaseJitter)"""
        source = inspect.getsource(LinMaster.__init__)
        assert source.index("self.linSlaves") < source.index("self.timeBase")
        assert source.index("self.timeBase") < source.index("self.timeBaseJitter")

    def test_add_lin_slave(self):
        parent = MockParent()
        master = LinMaster(parent, "TestMaster")
        slave1 = LinSlaveConfig()
        slave2 = LinSlaveConfig()

        assert master == master.addLinSlave(slave1)
        assert master == master.addLinSlave(slave2)
        assert master.getLinSlaves() == [slave1, slave2]

        assert master == master.addLinSlave(None)
        assert master.getLinSlaves() == [slave1, slave2]

    def test_get_set_time_base(self):
        parent = MockParent()
        master = LinMaster(parent, "TestMaster")

        assert master == master.setTimeBase(0.01)
        assert master.getTimeBase() == 0.01

        assert master == master.setTimeBase(None)
        assert master.getTimeBase() == 0.01

    def test_get_set_time_base_jitter(self):
        parent = MockParent()
        master = LinMaster(parent, "TestMaster")

        assert master == master.setTimeBaseJitter(0.001)
        assert master.getTimeBaseJitter() == 0.001

        assert master == master.setTimeBaseJitter(None)
        assert master.getTimeBaseJitter() == 0.001

    def _assert_docstring(self, method, note):
        doc = method.__doc__
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == note

    def test_member_docstrings_are_spec_note(self):
        """Test getter/setter/adder docstrings carry the spec Note verbatim (Table 3.38)"""
        self._assert_docstring(LinMaster.getLinSlaves, LIN_SLAVE_NOTE)
        self._assert_docstring(LinMaster.addLinSlave, LIN_SLAVE_NOTE + "\nA None value is a no-op and does not extend linSlaves.")

        self._assert_docstring(LinMaster.getTimeBase, TIME_BASE_NOTE)
        self._assert_docstring(LinMaster.setTimeBase, TIME_BASE_NOTE + "\nA None value is a no-op and does not overwrite an existing timeBase.")

        self._assert_docstring(LinMaster.getTimeBaseJitter, TIME_BASE_JITTER_NOTE)
        self._assert_docstring(LinMaster.setTimeBaseJitter, TIME_BASE_JITTER_NOTE + "\nA None value is a no-op and does not overwrite an existing timeBaseJitter.")

    def test_type_annotations(self):
        import ast
        import inspect

        getter_hints = get_type_hints(LinMaster.getLinSlaves)
        assert getter_hints["return"] == List[LinSlaveConfig]

        add_hints = get_type_hints(LinMaster.addLinSlave)
        assert add_hints["value"] == LinSlaveConfig
        assert add_hints["return"] == LinMaster

        getter_hints = get_type_hints(LinMaster.getTimeBase)
        assert getter_hints["return"] == Optional[TimeValue]

        setter_hints = get_type_hints(LinMaster.setTimeBase)
        assert setter_hints["value"] == Optional[TimeValue]
        assert setter_hints["return"] == LinMaster

        getter_hints = get_type_hints(LinMaster.getTimeBaseJitter)
        assert getter_hints["return"] == Optional[TimeValue]

        setter_hints = get_type_hints(LinMaster.setTimeBaseJitter)
        assert setter_hints["value"] == Optional[TimeValue]
        assert setter_hints["return"] == LinMaster

        src = inspect.getsource(sys.modules[LinMaster.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "LinMaster")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["linSlaves"] == "List[LinSlaveConfig]"
        assert annotations["timeBase"] == "Optional[TimeValue]"
        assert annotations["timeBaseJitter"] == "Optional[TimeValue]"


class TestLinSlave:
    """
    Describing the properties of the referring ecu as a LIN slave.
    """

    def test_inheritance(self):
        """Test the most-derived base from the Base chain (Table 3.41: ARObject, CommunicationController, Identifiable, LinCommunicationController, MultilanguageReferrable, Referrable)"""
        assert issubclass(LinSlave, LinCommunicationController)
        assert issubclass(LinSlave, CommunicationController)
        assert issubclass(LinSlave, ARObject)

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.41)"""
        assert inspect.cleandoc(LinSlave.__doc__).strip() == LIN_SLAVE_CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert LinSlave.__init__.__doc__ is None

    def test_initialization(self):
        parent = MockParent()
        slave = LinSlave(parent, "TestSlave")

        assert slave.getShortName() == "TestSlave"
        assert slave.getParent() is parent
        assert isinstance(slave, LinCommunicationController)
        assert isinstance(slave, CommunicationController)
        assert isinstance(slave, ARObject)

        assert slave.getProtocolVersion() is None
        assert slave.getAssignNad() is None
        assert slave.getConfiguredNad() is None
        assert slave.getFunctionId() is None
        assert slave.getInitialNad() is None
        assert slave.getLinErrorResponse() is None
        assert slave.getNasTimeout() is None
        assert slave.getSupplierId() is None
        assert slave.getVariantId() is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.41: assignNad, configuredNad, functionId, initialNad, linErrorResponse, nasTimeout, supplierId, variantId)"""
        source = inspect.getsource(LinSlave.__init__)
        assert source.index("self.assignNad") < source.index("self.configuredNad")
        assert source.index("self.configuredNad") < source.index("self.functionId")
        assert source.index("self.functionId") < source.index("self.initialNad")
        assert source.index("self.initialNad") < source.index("self.linErrorResponse")
        assert source.index("self.linErrorResponse") < source.index("self.nasTimeout")
        assert source.index("self.nasTimeout") < source.index("self.supplierId")
        assert source.index("self.supplierId") < source.index("self.variantId")

    def test_get_set_assign_nad(self):
        parent = MockParent()
        slave = LinSlave(parent, "TestSlave")

        assert slave == slave.setAssignNad(True)
        assert slave.getAssignNad() is True

        assert slave == slave.setAssignNad(None)
        assert slave.getAssignNad() is True

    def test_get_set_configured_nad(self):
        parent = MockParent()
        slave = LinSlave(parent, "TestSlave")

        assert slave == slave.setConfiguredNad(3)
        assert slave.getConfiguredNad() == 3

        assert slave == slave.setConfiguredNad(None)
        assert slave.getConfiguredNad() == 3

    def test_get_set_function_id(self):
        parent = MockParent()
        slave = LinSlave(parent, "TestSlave")

        assert slave == slave.setFunctionId(17)
        assert slave.getFunctionId() == 17

        assert slave == slave.setFunctionId(None)
        assert slave.getFunctionId() == 17

    def test_get_set_initial_nad(self):
        parent = MockParent()
        slave = LinSlave(parent, "TestSlave")

        assert slave == slave.setInitialNad(1)
        assert slave.getInitialNad() == 1

        assert slave == slave.setInitialNad(None)
        assert slave.getInitialNad() == 1

    def test_set_lin_error_response(self):
        parent = MockParent()
        slave = LinSlave(parent, "TestSlave")
        response = LinErrorResponse()

        assert slave == slave.setLinErrorResponse(response)
        assert slave.getLinErrorResponse() is response

        assert slave == slave.setLinErrorResponse(None)
        assert slave.getLinErrorResponse() is response

    def test_get_set_nas_timeout(self):
        parent = MockParent()
        slave = LinSlave(parent, "TestSlave")

        assert slave == slave.setNasTimeout(0.1)
        assert slave.getNasTimeout() == 0.1

        assert slave == slave.setNasTimeout(None)
        assert slave.getNasTimeout() == 0.1

    def test_get_set_supplier_id(self):
        parent = MockParent()
        slave = LinSlave(parent, "TestSlave")

        assert slave == slave.setSupplierId(2721)
        assert slave.getSupplierId() == 2721

        assert slave == slave.setSupplierId(None)
        assert slave.getSupplierId() == 2721

    def test_get_set_variant_id(self):
        parent = MockParent()
        slave = LinSlave(parent, "TestSlave")

        assert slave == slave.setVariantId(5)
        assert slave.getVariantId() == 5

        assert slave == slave.setVariantId(None)
        assert slave.getVariantId() == 5

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_member_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.41)"""
        self._assert_docstring(LinSlave.getAssignNad, LIN_SLAVE_ASSIGN_NAD_NOTE)
        self._assert_docstring(LinSlave.setAssignNad, LIN_SLAVE_ASSIGN_NAD_NOTE, "assignNad")

        self._assert_docstring(LinSlave.getConfiguredNad, LIN_SLAVE_CONFIGURED_NAD_NOTE)
        self._assert_docstring(LinSlave.setConfiguredNad, LIN_SLAVE_CONFIGURED_NAD_NOTE, "configuredNad")

        self._assert_docstring(LinSlave.getFunctionId, LIN_SLAVE_FUNCTION_ID_NOTE)
        self._assert_docstring(LinSlave.setFunctionId, LIN_SLAVE_FUNCTION_ID_NOTE, "functionId")

        self._assert_docstring(LinSlave.getInitialNad, LIN_SLAVE_INITIAL_NAD_NOTE)
        self._assert_docstring(LinSlave.setInitialNad, LIN_SLAVE_INITIAL_NAD_NOTE, "initialNad")

        self._assert_docstring(LinSlave.getLinErrorResponse, LIN_SLAVE_LIN_ERROR_RESPONSE_NOTE)
        self._assert_docstring(LinSlave.setLinErrorResponse, LIN_SLAVE_LIN_ERROR_RESPONSE_NOTE, "linErrorResponse")

        self._assert_docstring(LinSlave.getNasTimeout, LIN_SLAVE_NAS_TIMEOUT_NOTE)
        self._assert_docstring(LinSlave.setNasTimeout, LIN_SLAVE_NAS_TIMEOUT_NOTE, "nasTimeout")

        self._assert_docstring(LinSlave.getSupplierId, LIN_SLAVE_SUPPLIER_ID_NOTE)
        self._assert_docstring(LinSlave.setSupplierId, LIN_SLAVE_SUPPLIER_ID_NOTE, "supplierId")

        self._assert_docstring(LinSlave.getVariantId, LIN_SLAVE_VARIANT_ID_NOTE)
        self._assert_docstring(LinSlave.setVariantId, LIN_SLAVE_VARIANT_ID_NOTE, "variantId")

    def test_type_annotations(self):
        import ast
        import inspect

        expected_getters = {
            "getAssignNad": (Optional[Boolean], LIN_SLAVE_ASSIGN_NAD_NOTE),
            "getConfiguredNad": (Optional[Integer], LIN_SLAVE_CONFIGURED_NAD_NOTE),
            "getFunctionId": (Optional[PositiveInteger], LIN_SLAVE_FUNCTION_ID_NOTE),
            "getInitialNad": (Optional[Integer], LIN_SLAVE_INITIAL_NAD_NOTE),
            "getLinErrorResponse": (Optional[LinErrorResponse], LIN_SLAVE_LIN_ERROR_RESPONSE_NOTE),
            "getNasTimeout": (Optional[TimeValue], LIN_SLAVE_NAS_TIMEOUT_NOTE),
            "getSupplierId": (Optional[PositiveInteger], LIN_SLAVE_SUPPLIER_ID_NOTE),
            "getVariantId": (Optional[PositiveInteger], LIN_SLAVE_VARIANT_ID_NOTE),
        }
        for name, (return_hint, _) in expected_getters.items():
            getter_hints = get_type_hints(getattr(LinSlave, name))
            assert getter_hints["return"] == return_hint

            setter_hints = get_type_hints(getattr(LinSlave, "set" + name[3:]))
            assert setter_hints["value"] == return_hint
            assert setter_hints["return"] == LinSlave

        src = inspect.getsource(sys.modules[LinSlave.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "LinSlave")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["assignNad"] == "Optional[Boolean]"
        assert annotations["configuredNad"] == "Optional[Integer]"
        assert annotations["functionId"] == "Optional[PositiveInteger]"
        assert annotations["initialNad"] == "Optional[Integer]"
        assert annotations["linErrorResponse"] == "Optional[LinErrorResponse]"
        assert annotations["nasTimeout"] == "Optional[TimeValue]"
        assert annotations["supplierId"] == "Optional[PositiveInteger]"
        assert annotations["variantId"] == "Optional[PositiveInteger]"


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
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
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


LIN_COMMUNICATION_CONNECTOR_CLASS_NOTE = (
    "LIN bus specific communication connector attributes.\n"
    "\n"
    "[constr_3029] Assign-Frame command usage: For the LIN 2.0 Assign-Frame command the LinConfigurableFrame list shall be used. For the LIN 2.1 Assign-Frame-PID-Range command the LinOrderedConfigurableFrame list shall be used.\n"
    "\n"
    "[constr_5030] Uniqueness of LinOrderedConfigurableFrame.index: LinOrderedConfigurableFrame.index shall always be set and be unique in the context of the aggregating LinCommunicationConnector.\n"
    "\n"
    "[constr_5450] Existence of index: For each LinOrderedConfigurableFrame, the attribute shall index shall exist at the time when the System Description is complete.\n"
    "\n"
    "[constr_5451] Existence of LinOrderedConfigurableFrame.frame reference: For each LinOrderedConfigurableFrame, the reference to LinFrame in the role frame shall exist at the time when the System Description is complete.\n"
    "\n"
    "[constr_5452] Existence of LinConfigurableFrame.frame reference: For each LinConfigurableFrame, the reference to LinFrame in the role frame shall exist at the time when the System Description is complete."
)
INITIAL_NAD_NOTE = "Initial NAD of the LIN slave."
LIN_CONFIGURABLE_FRAME_NOTE = "LinConfigurableFrames shall list all frames (unconditional frames, event-triggered frames and sporadic frames) processed by the slave node. This element is necessary for the LIN 2.0 Assign-Frame command."
LIN_ORDERED_CONFIGURABLE_FRAME_NOTE = "LinOrderedConfigurableFrames shall list all frames (unconditional frames, event-triggered frames and sporadic frames) processed by the slave node. This element is necessary for the LIN 2.1 Assign-Frame-PID-Range command."
SCHEDULE_CHANGE_NEXT_TIME_BASE_NOTE = "This attribute defines the point in time where a schedule table switch is performed. If this attribute is set to false or not present, the schedule table shall be switched after the current entry of the active schedule table is ended. If this attribute is enabled, the schedule table shall be switched when message transmission or reception within an entry has been completed, ensured by status checks for transmission and reception."


class TestLinCommunicationConnector:
    def _make(self) -> LinCommunicationConnector:
        return LinCommunicationConnector(MockParent(), "test_lin_comm_connector")

    def _assert_docstring(self, method, note, attr_name=None, extends=False):
        tail = "does not extend %s" % attr_name if extends else "does not overwrite an existing %s" % attr_name
        expected = note if attr_name is None else note + "\nA None value is a no-op and %s." % tail
        assert method.__doc__ is not None
        assert inspect.cleandoc(method.__doc__).strip() == expected

    def test_initialization(self):
        connector = self._make()

        assert connector.getShortName() == "test_lin_comm_connector"
        assert isinstance(connector, CommunicationConnector)
        assert connector.getInitialNad() is None
        assert connector.getLinConfigurableFrames() == []
        assert connector.getLinOrderedConfigurableFrames() == []
        assert connector.getScheduleChangeNextTimeBase() is None

    def test_class_docstring_is_spec_note(self):
        assert inspect.cleandoc(LinCommunicationConnector.__doc__).strip() == LIN_COMMUNICATION_CONNECTOR_CLASS_NOTE

    def test_init_has_no_docstring(self):
        assert LinCommunicationConnector.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        source = inspect.getsource(LinCommunicationConnector.__init__)
        assert source.index("self.initialNad:") < source.index("self.linConfigurableFrames:")
        assert source.index("self.linConfigurableFrames:") < source.index("self.linOrderedConfigurableFrames:")
        assert source.index("self.linOrderedConfigurableFrames:") < source.index("self.scheduleChangeNextTimeBase:")

    def test_get_set_initial_nad(self):
        connector = self._make()

        assert connector.getInitialNad() is None

        nad = Integer()
        nad.setValue("5")
        assert connector == connector.setInitialNad(nad)
        assert connector.getInitialNad() == nad

        assert connector == connector.setInitialNad(None)
        assert connector.getInitialNad() == nad

        getter_hints = get_type_hints(LinCommunicationConnector.getInitialNad)
        assert getter_hints.get("return") == Optional[Integer]

        setter_hints = get_type_hints(LinCommunicationConnector.setInitialNad)
        assert setter_hints.get("value") == Optional[Integer]
        assert setter_hints.get("return") is LinCommunicationConnector

    def test_initial_nad_docstrings_are_spec_note(self):
        self._assert_docstring(LinCommunicationConnector.getInitialNad, INITIAL_NAD_NOTE)
        self._assert_docstring(LinCommunicationConnector.setInitialNad, INITIAL_NAD_NOTE, "initialNad")

    def test_add_lin_configurable_frame(self):
        connector = self._make()

        assert connector.getLinConfigurableFrames() == []

        frame = LinConfigurableFrame()
        assert connector == connector.addLinConfigurableFrame(frame)
        assert connector.getLinConfigurableFrames() == [frame]

        assert connector == connector.addLinConfigurableFrame(None)
        assert connector.getLinConfigurableFrames() == [frame]

        getter_hints = get_type_hints(LinCommunicationConnector.getLinConfigurableFrames)
        assert getter_hints.get("return") == List[LinConfigurableFrame]

        add_hints = get_type_hints(LinCommunicationConnector.addLinConfigurableFrame)
        assert add_hints.get("value") is LinConfigurableFrame
        assert add_hints.get("return") is LinCommunicationConnector

    def test_lin_configurable_frame_docstrings_are_spec_note(self):
        self._assert_docstring(LinCommunicationConnector.getLinConfigurableFrames, LIN_CONFIGURABLE_FRAME_NOTE)
        self._assert_docstring(LinCommunicationConnector.addLinConfigurableFrame, LIN_CONFIGURABLE_FRAME_NOTE, "linConfigurableFrames", extends=True)

    def test_add_lin_ordered_configurable_frame(self):
        connector = self._make()

        assert connector.getLinOrderedConfigurableFrames() == []

        frame = LinOrderedConfigurableFrame()
        assert connector == connector.addLinOrderedConfigurableFrame(frame)
        assert connector.getLinOrderedConfigurableFrames() == [frame]

        assert connector == connector.addLinOrderedConfigurableFrame(None)
        assert connector.getLinOrderedConfigurableFrames() == [frame]

        getter_hints = get_type_hints(LinCommunicationConnector.getLinOrderedConfigurableFrames)
        assert getter_hints.get("return") == List[LinOrderedConfigurableFrame]

        add_hints = get_type_hints(LinCommunicationConnector.addLinOrderedConfigurableFrame)
        assert add_hints.get("value") is LinOrderedConfigurableFrame
        assert add_hints.get("return") is LinCommunicationConnector

    def test_lin_ordered_configurable_frame_docstrings_are_spec_note(self):
        self._assert_docstring(LinCommunicationConnector.getLinOrderedConfigurableFrames, LIN_ORDERED_CONFIGURABLE_FRAME_NOTE)
        self._assert_docstring(LinCommunicationConnector.addLinOrderedConfigurableFrame, LIN_ORDERED_CONFIGURABLE_FRAME_NOTE, "linOrderedConfigurableFrames", extends=True)

    def test_get_set_schedule_change_next_time_base(self):
        connector = self._make()

        assert connector.getScheduleChangeNextTimeBase() is None

        flag = Boolean()
        flag.setValue(True)
        assert connector == connector.setScheduleChangeNextTimeBase(flag)
        assert connector.getScheduleChangeNextTimeBase() == flag

        assert connector == connector.setScheduleChangeNextTimeBase(None)
        assert connector.getScheduleChangeNextTimeBase() == flag

        getter_hints = get_type_hints(LinCommunicationConnector.getScheduleChangeNextTimeBase)
        assert getter_hints.get("return") == Optional[Boolean]

        setter_hints = get_type_hints(LinCommunicationConnector.setScheduleChangeNextTimeBase)
        assert setter_hints.get("value") == Optional[Boolean]
        assert setter_hints.get("return") is LinCommunicationConnector

    def test_schedule_change_next_time_base_docstrings_are_spec_note(self):
        self._assert_docstring(LinCommunicationConnector.getScheduleChangeNextTimeBase, SCHEDULE_CHANGE_NEXT_TIME_BASE_NOTE)
        self._assert_docstring(LinCommunicationConnector.setScheduleChangeNextTimeBase, SCHEDULE_CHANGE_NEXT_TIME_BASE_NOTE, "scheduleChangeNextTimeBase")

    def test_type_annotations(self):
        src = inspect.getsource(sys.modules[LinCommunicationConnector.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "LinCommunicationConnector")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["initialNad"] == "Optional[Integer]"
        assert annotations["linConfigurableFrames"] == "List[LinConfigurableFrame]"
        assert annotations["linOrderedConfigurableFrames"] == "List[LinOrderedConfigurableFrame]"
        assert annotations["scheduleChangeNextTimeBase"] == "Optional[Boolean]"


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
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["frameRef"] == "Optional[RefType]"
        assert annotations["messageId"] == "Optional[PositiveInteger]"


class TestLinOrderedConfigurableFrame:
    """
    With the assignment of the index to a frame a mapping of Pids to Frames is possible. This element shall be used for the LIN 2.1 Assign-Frame-PID-Range command.
    """

    def test_initialization(self):
        obj = LinOrderedConfigurableFrame()

        assert isinstance(obj, ARObject)
        assert obj.parent is None
        assert obj.getFrameRef() is None
        assert obj.getIndex() is None

    def test_get_set_frame_ref(self):
        obj = LinOrderedConfigurableFrame()

        ref = "/System/LinFrame"
        assert obj == obj.setFrameRef(ref)
        assert obj.getFrameRef() == ref

        assert obj == obj.setFrameRef(None)
        assert obj.getFrameRef() == ref

    def test_get_set_index(self):
        obj = LinOrderedConfigurableFrame()

        assert obj == obj.setIndex(3)
        assert obj.getIndex() == 3

        assert obj == obj.setIndex(None)
        assert obj.getIndex() == 3

    def test_type_annotations(self):
        import ast
        import inspect

        getter_hints = get_type_hints(LinOrderedConfigurableFrame.getFrameRef)
        assert getter_hints["return"] == Optional[RefType]

        setter_hints = get_type_hints(LinOrderedConfigurableFrame.setFrameRef)
        assert setter_hints["value"] == Optional[RefType]
        assert setter_hints["return"] == LinOrderedConfigurableFrame

        getter_hints = get_type_hints(LinOrderedConfigurableFrame.getIndex)
        assert getter_hints["return"] == Optional[Integer]

        setter_hints = get_type_hints(LinOrderedConfigurableFrame.setIndex)
        assert setter_hints["value"] == Optional[Integer]
        assert setter_hints["return"] == LinOrderedConfigurableFrame

        src = inspect.getsource(sys.modules[LinOrderedConfigurableFrame.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "LinOrderedConfigurableFrame")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["frameRef"] == "Optional[RefType]"
        assert annotations["index"] == "Optional[Integer]"


class TestLinSlaveConfig:
    """
    Node attributes of LIN slaves that are handled by the LinMaster. In the System Description LIN slaves may be described in the context of the Lin Master. In an ECU Extract of the LinMaster the LinSlave Ecus shall not be available. The information that is described here is necessary in the ECU Extract for the configuration of the Lin Master. The values of attributes of LinSlaveConfig and the corresponding LinSlave shall be identical (if both are defined in a System Description).
    """

    def test_initialization(self):
        obj = LinSlaveConfig()

        assert isinstance(obj, ARObject)
        assert obj.parent is None
        assert obj.getConfiguredNad() is None
        assert obj.getFunctionId() is None
        assert obj.getIdent() is None
        assert obj.getInitialNad() is None
        assert obj.getLinConfigurableFrames() == []
        assert obj.getLinErrorResponse() is None
        assert obj.getLinOrderedConfigurableFrames() == []
        assert obj.getProtocolVersion() is None
        assert obj.getSupplierId() is None
        assert obj.getVariantId() is None

    def test_get_set_configured_nad(self):
        obj = LinSlaveConfig()

        assert obj == obj.setConfiguredNad(3)
        assert obj.getConfiguredNad() == 3

        assert obj == obj.setConfiguredNad(None)
        assert obj.getConfiguredNad() == 3

    def test_get_set_function_id(self):
        obj = LinSlaveConfig()

        assert obj == obj.setFunctionId(24)
        assert obj.getFunctionId() == 24

        assert obj == obj.setFunctionId(None)
        assert obj.getFunctionId() == 24

    def test_get_set_ident(self):
        obj = LinSlaveConfig()
        ident = LinSlaveConfigIdent(obj, "Ident")

        assert obj == obj.setIdent(ident)
        assert obj.getIdent() == ident

        assert obj == obj.setIdent(None)
        assert obj.getIdent() == ident

    def test_get_set_initial_nad(self):
        obj = LinSlaveConfig()

        assert obj == obj.setInitialNad(1)
        assert obj.getInitialNad() == 1

        assert obj == obj.setInitialNad(None)
        assert obj.getInitialNad() == 1

    def test_add_lin_configurable_frame(self):
        obj = LinSlaveConfig()
        frame1 = LinConfigurableFrame()
        frame2 = LinConfigurableFrame()

        assert obj == obj.addLinConfigurableFrame(frame1)
        assert obj == obj.addLinConfigurableFrame(frame2)
        assert obj.getLinConfigurableFrames() == [frame1, frame2]

        assert obj == obj.addLinConfigurableFrame(None)
        assert obj.getLinConfigurableFrames() == [frame1, frame2]

    def test_get_set_lin_error_response(self):
        obj = LinSlaveConfig()
        response = LinErrorResponse()

        assert obj == obj.setLinErrorResponse(response)
        assert obj.getLinErrorResponse() == response

        assert obj == obj.setLinErrorResponse(None)
        assert obj.getLinErrorResponse() == response

    def test_add_lin_ordered_configurable_frame(self):
        obj = LinSlaveConfig()
        frame1 = LinOrderedConfigurableFrame()
        frame2 = LinOrderedConfigurableFrame()

        assert obj == obj.addLinOrderedConfigurableFrame(frame1)
        assert obj == obj.addLinOrderedConfigurableFrame(frame2)
        assert obj.getLinOrderedConfigurableFrames() == [frame1, frame2]

        assert obj == obj.addLinOrderedConfigurableFrame(None)
        assert obj.getLinOrderedConfigurableFrames() == [frame1, frame2]

    def test_get_set_protocol_version(self):
        obj = LinSlaveConfig()

        assert obj == obj.setProtocolVersion("2.1")
        assert obj.getProtocolVersion() == "2.1"

        assert obj == obj.setProtocolVersion(None)
        assert obj.getProtocolVersion() == "2.1"

    def test_get_set_supplier_id(self):
        obj = LinSlaveConfig()

        assert obj == obj.setSupplierId(17)
        assert obj.getSupplierId() == 17

        assert obj == obj.setSupplierId(None)
        assert obj.getSupplierId() == 17

    def test_get_set_variant_id(self):
        obj = LinSlaveConfig()

        assert obj == obj.setVariantId(9)
        assert obj.getVariantId() == 9

        assert obj == obj.setVariantId(None)
        assert obj.getVariantId() == 9

    def test_type_annotations(self):
        import ast
        import inspect

        src = inspect.getsource(sys.modules[LinSlaveConfig.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "LinSlaveConfig")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations["configuredNad"] == "Optional[Integer]"
        assert annotations["functionId"] == "Optional[PositiveInteger]"
        assert annotations["ident"] == "Optional[LinSlaveConfigIdent]"
        assert annotations["initialNad"] == "Optional[Integer]"
        assert annotations["linConfigurableFrames"] == "List[LinConfigurableFrame]"
        assert annotations["linErrorResponse"] == "Optional[LinErrorResponse]"
        assert annotations["linOrderedConfigurableFrames"] == "List[LinOrderedConfigurableFrame]"
        assert annotations["protocolVersion"] == "Optional[String]"
        assert annotations["supplierId"] == "Optional[PositiveInteger]"
        assert annotations["variantId"] == "Optional[PositiveInteger]"


class TestLinCluster:
    """
    LIN specific attributes Tags: atp.recommendedPackage=CommunicationClusters
    """

    def test_initialization(self):
        parent = MockParent()
        cluster = LinCluster(parent, "TestCluster")

        assert cluster.getShortName() == "TestCluster"
        assert cluster.getParent() is parent
        assert isinstance(cluster, CommunicationCluster)
        assert isinstance(cluster, FibexElement)
        assert isinstance(cluster, ARObject)

        assert cluster.getBaudrate() is None
        assert cluster.getPhysicalChannels() == []
        assert cluster.getProtocolName() is None
        assert cluster.getProtocolVersion() is None

    def test_no_own_attributes(self):
        import ast
        import inspect

        src = inspect.getsource(sys.modules[LinCluster.__module__])
        tree = ast.parse(src)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "LinCluster")
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        annotations = {}
        for node in ast.walk(init):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Attribute):
                annotations[node.target.attr] = ast.get_source_segment(src, node.annotation)
        assert annotations == {}

    def test_inherited_base_accessors(self):
        parent = MockParent()
        cluster = LinCluster(parent, "TestCluster")

        assert cluster == cluster.setBaudrate(19200)
        assert cluster.getBaudrate() == 19200

        assert cluster == cluster.setProtocolName("LIN")
        assert cluster.getProtocolName() == "LIN"

        assert cluster == cluster.setProtocolVersion("2.2")
        assert cluster.getProtocolVersion() == "2.2"

        assert cluster == cluster.setBaudrate(None)
        assert cluster.getBaudrate() == 19200

        assert cluster == cluster.setProtocolName(None)
        assert cluster.getProtocolName() == "LIN"

        assert cluster == cluster.setProtocolVersion(None)
        assert cluster.getProtocolVersion() == "2.2"

    def test_inheritance(self):
        assert issubclass(LinCluster, CommunicationCluster)
        assert issubclass(LinCluster, FibexElement)
        assert issubclass(LinCluster, ARObject)

    def test_concrete_instantiation(self):
        cluster = LinCluster(MockParent(), "cluster")  # Table 3.36 carries no abstract stereotype

        assert isinstance(cluster, CommunicationCluster)

    def test_class_docstring_is_spec_note(self):
        """Class docstring carries the spec Note verbatim (Table 3.36, p.93)."""
        assert LinCluster.__doc__.strip() == "LIN specific attributes Tags: atp.recommendedPackage=CommunicationClusters"

    def test_init_has_no_docstring(self):
        assert LinCluster.__init__.__doc__ is None
