"""
Tests for reading ROLE-BASED-PORT-ASSIGNMENT elements — RoleBasedPortAssignment, Table 7.54 (p.605, R23-11).

RoleBasedPortAssignment (Base = ARObject) carries two own attributes whose reader element
set follows the XSD group ROLE-BASED-PORT-ASSIGNMENT (AUTOSAR_00052.xsd): PORT-PROTOTYPE-REF
and ROLE (each 0..1, order-independent on read). It is aggregated by
NvBlockDescriptor.clientServerPort and SwcServiceDependency.assignedPort and read through
readNvBlockDescriptor / readSwcServiceDependencyAssignedPorts → getRoleBasedPortAssignment.

Round-trip counterpart: tests/test_armodel/writer/test_role_based_port_assignment.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import (
    RoleBasedPortAssignment,
    SwcServiceDependency,
)
from tests.test_armodel.parser._helpers import NS

PORT_ASSIGNMENT_XML = "<ROLE-BASED-PORT-ASSIGNMENT>" "<PORT-PROTOTYPE-REF DEST='R-PORT-PROTOTYPE'>/Swc/PortPrototype</PORT-PROTOTYPE-REF>" "<ROLE>NvMService</ROLE>" "</ROLE-BASED-PORT-ASSIGNMENT>"


def _wrap(inner: str) -> ET.Element:
    """Wrap the ROLE-BASED-PORT-ASSIGNMENT fragment in a namespaced parent element."""
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


class TestGetRoleBasedPortAssignment:
    """Tests for getRoleBasedPortAssignment — own element field values (Table 7.54)."""

    def test_own_element_field_values(self, parser):
        """Test that both attribute elements are read with their field values."""
        element = _wrap(PORT_ASSIGNMENT_XML)

        assignment = parser.getRoleBasedPortAssignment(element[0])

        assert assignment is not None
        assert isinstance(assignment, RoleBasedPortAssignment)
        port_ref = assignment.getPortPrototypeRef()
        assert isinstance(port_ref, RefType)
        assert port_ref.getValue() == "/Swc/PortPrototype"
        assert port_ref.getDest() == "R-PORT-PROTOTYPE"
        role = assignment.getRole()
        assert isinstance(role, Identifier)
        assert role.getValue() == "NvMService"

    def test_empty_element(self, parser):
        """Test that an empty element yields an instance with all fields unset."""
        element = _wrap("<ROLE-BASED-PORT-ASSIGNMENT></ROLE-BASED-PORT-ASSIGNMENT>")

        assignment = parser.getRoleBasedPortAssignment(element[0])

        assert assignment is not None
        assert assignment.getPortPrototypeRef() is None
        assert assignment.getRole() is None

    def test_absent_port_prototype_ref(self, parser):
        """Test that an absent PORT-PROTOTYPE-REF element leaves the reference unset while the role is read."""
        element = _wrap("<ROLE-BASED-PORT-ASSIGNMENT><ROLE>NvMService</ROLE></ROLE-BASED-PORT-ASSIGNMENT>")

        assignment = parser.getRoleBasedPortAssignment(element[0])

        assert assignment.getPortPrototypeRef() is None
        assert assignment.getRole().getValue() == "NvMService"

    def test_absent_role(self, parser):
        """Test that an absent ROLE element leaves the role unset while the reference is read."""
        element = _wrap("<ROLE-BASED-PORT-ASSIGNMENT><PORT-PROTOTYPE-REF DEST='R-PORT-PROTOTYPE'>/Swc/PortPrototype</PORT-PROTOTYPE-REF></ROLE-BASED-PORT-ASSIGNMENT>")

        assignment = parser.getRoleBasedPortAssignment(element[0])

        assert assignment.getRole() is None
        assert assignment.getPortPrototypeRef().getValue() == "/Swc/PortPrototype"

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><ROLE-BASED-PORT-ASSIGNMENT S='abc123' T='2024-01-01T12:00:00+00:00'></ROLE-BASED-PORT-ASSIGNMENT></ROOT>")

        assignment = parser.getRoleBasedPortAssignment(element[0])

        assert assignment is not None
        assert assignment.getChecksum() is not None
        assert assignment.getChecksum().getValue() == "abc123"
        assert assignment.getTimestamp() is not None


class TestReadRoleBasedPortAssignmentDispatch:
    """Tests for the NvBlockDescriptor.clientServerPort and SwcServiceDependency.assignedPort dispatch."""

    def test_dispatch_via_swc_service_dependency(self, parser):
        """Test that readSwcServiceDependencyAssignedPorts reads the assigned port with field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        dependency = SwcServiceDependency(root, "Dep")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><SWC-SERVICE-DEPENDENCY><SHORT-NAME>Dep</SHORT-NAME><ASSIGNED-PORTS>{PORT_ASSIGNMENT_XML}</ASSIGNED-PORTS></SWC-SERVICE-DEPENDENCY></ROOT>")

        parser.readSwcServiceDependencyAssignedPorts(element[0], dependency)

        ports = dependency.getAssignedPorts()
        assert len(ports) == 1
        assignment = ports[0]
        assert isinstance(assignment, RoleBasedPortAssignment)
        assert assignment.getPortPrototypeRef().getValue() == "/Swc/PortPrototype"
        assert assignment.getRole().getValue() == "NvMService"

    def test_dispatch_via_nv_block_descriptor(self, parser):
        """Test that readNvBlockDescriptor reads the client server port with field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "Descriptor")
        element = ET.fromstring(
            f"<ROOT xmlns='{NS}'><NV-BLOCK-DESCRIPTOR><SHORT-NAME>Descriptor</SHORT-NAME><CLIENT-SERVER-PORTS>{PORT_ASSIGNMENT_XML}</CLIENT-SERVER-PORTS></NV-BLOCK-DESCRIPTOR></ROOT>"
        )

        parser.readNvBlockDescriptor(element[0], descriptor)

        ports = descriptor.getClientServerPorts()
        assert len(ports) == 1
        assignment = ports[0]
        assert isinstance(assignment, RoleBasedPortAssignment)
        assert assignment.getPortPrototypeRef().getValue() == "/Swc/PortPrototype"
        assert assignment.getRole().getValue() == "NvMService"

    def test_dispatch_absent_assigned_ports(self, parser):
        """Test that a dependency without ASSIGNED-PORTS leaves the assigned ports empty."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        dependency = SwcServiceDependency(root, "Dep")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><SWC-SERVICE-DEPENDENCY><SHORT-NAME>Dep</SHORT-NAME></SWC-SERVICE-DEPENDENCY></ROOT>")

        parser.readSwcServiceDependencyAssignedPorts(element[0], dependency)

        assert dependency.getAssignedPorts() == []
