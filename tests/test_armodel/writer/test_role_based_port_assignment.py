"""
Tests for writing ROLE-BASED-PORT-ASSIGNMENT elements — RoleBasedPortAssignment, Table 7.54 (p.605, R23-11).

RoleBasedPortAssignment (Base = ARObject) carries two own attributes whose writer element
order must follow the XSD sequence (AUTOSAR_00052.xsd group ROLE-BASED-PORT-ASSIGNMENT):
PORT-PROTOTYPE-REF → ROLE (VARIATION-POINT carries sequenceOffset 10000 and sorts last when
present). The ASSIGNED-PORTS wrapper is emitted only when non-empty. The set-level round-trip
goes through the aggregations (writeSwcServiceDependencyAssignedPorts →
readSwcServiceDependencyAssignedPorts, writeNvBlockDescriptor → readNvBlockDescriptor).

Round-trip counterpart: tests/test_armodel/parser/test_role_based_port_assignment.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Identifier, RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import (
    RoleBasedPortAssignment,
    SwcServiceDependency,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ELEMENT_ORDER = [
    "PORT-PROTOTYPE-REF",
    "ROLE",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _filled_assignment():
    assignment = RoleBasedPortAssignment()
    port_ref = RefType()
    port_ref.setValue("/Swc/PortPrototype")
    port_ref.setDest("R-PORT-PROTOTYPE")
    assignment.setPortPrototypeRef(port_ref)
    role = Identifier()
    role.setValue("NvMService")
    assignment.setRole(role)
    return assignment


class TestWriteRoleBasedPortAssignment:
    """Tests for writeRoleBasedPortAssignment — own element field values (Table 7.54)."""

    def test_write_field_values(self, writer):
        """Test that both attribute elements are emitted with their values read through the getters."""
        parent = ET.Element("PARENT")

        writer.writeRoleBasedPortAssignment(parent, _filled_assignment())

        element = parent.find("ROLE-BASED-PORT-ASSIGNMENT")
        assert element is not None
        port_ref_element = element.find("PORT-PROTOTYPE-REF")
        assert port_ref_element.text == "/Swc/PortPrototype"
        assert port_ref_element.attrib.get("DEST") == "R-PORT-PROTOTYPE"
        assert element.find("ROLE").text == "NvMService"

    def test_write_xsd_element_order(self, writer):
        """Test that the element order follows the XSD group sequenceOffset order."""
        parent = ET.Element("PARENT")

        writer.writeRoleBasedPortAssignment(parent, _filled_assignment())

        element = parent.find("ROLE-BASED-PORT-ASSIGNMENT")
        assert [elem.tag for elem in element] == XSD_ELEMENT_ORDER

    def test_write_unset_assignment_emits_no_children(self, writer):
        """Test that an assignment without fields emits the element only, with no attribute children."""
        parent = ET.Element("PARENT")

        writer.writeRoleBasedPortAssignment(parent, RoleBasedPortAssignment())

        element = parent.find("ROLE-BASED-PORT-ASSIGNMENT")
        assert element is not None
        assert element.find("PORT-PROTOTYPE-REF") is None
        assert element.find("ROLE") is None

    def test_write_ar_object_attributes(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) are emitted."""
        assignment = RoleBasedPortAssignment()
        checksum = String()
        checksum.setValue("abc123")
        assignment.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+00:00")
        assignment.setTimestamp(timestamp)

        parent = ET.Element("PARENT")
        writer.writeRoleBasedPortAssignment(parent, assignment)

        element = parent.find("ROLE-BASED-PORT-ASSIGNMENT")
        assert element.attrib.get("S") == "abc123"
        assert element.attrib.get("T") is not None


class TestRoleBasedPortAssignmentRoundTrip:
    """Tests for the aggregation round-trips."""

    def _reparse(self, parent_element, root_tag):
        xml_text = ET.tostring(parent_element, encoding="unicode")
        return ET.fromstring(xml_text.replace(root_tag, f"{root_tag} xmlns='{NS}'", 1))

    def test_round_trip_via_swc_service_dependency(self, writer):
        """Test the assigned-port aggregation round-trip with field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        dependency = SwcServiceDependency(root, "Dep")
        dependency.AddAssignedPort(_filled_assignment())

        parent = ET.Element("SWC-SERVICE-DEPENDENCY")
        writer.writeSwcServiceDependencyAssignedPorts(parent, dependency)

        assert parent.find("ASSIGNED-PORTS") is not None
        reloaded_element = self._reparse(parent, "SWC-SERVICE-DEPENDENCY")

        root2 = AUTOSAR.getInstance().createARPackage("Pkg2")
        reloaded = SwcServiceDependency(root2, "OtherName")
        ARXMLParser().readSwcServiceDependencyAssignedPorts(reloaded_element, reloaded)

        ports = reloaded.getAssignedPorts()
        assert len(ports) == 1
        assignment = ports[0]
        assert isinstance(assignment, RoleBasedPortAssignment)
        assert assignment.getPortPrototypeRef().getValue() == "/Swc/PortPrototype"
        assert assignment.getPortPrototypeRef().getDest() == "R-PORT-PROTOTYPE"
        assert isinstance(assignment.getRole(), Identifier)
        assert assignment.getRole().getValue() == "NvMService"

    def test_round_trip_via_nv_block_descriptor(self, writer):
        """Test the client-server-port aggregation round-trip with field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        descriptor = NvBlockDescriptor(root, "Descriptor")
        descriptor.addClientServerPort(_filled_assignment())

        parent = ET.Element("PARENT")
        writer.writeNvBlockDescriptor(parent, descriptor)

        element = parent.find("NV-BLOCK-DESCRIPTOR")
        assert element is not None
        reloaded_element = self._reparse(element, "NV-BLOCK-DESCRIPTOR")

        root2 = AUTOSAR.getInstance().createARPackage("Pkg2")
        reloaded = NvBlockDescriptor(root2, "OtherName")
        ARXMLParser().readNvBlockDescriptor(reloaded_element, reloaded)

        ports = reloaded.getClientServerPorts()
        assert len(ports) == 1
        assignment = ports[0]
        assert isinstance(assignment, RoleBasedPortAssignment)
        assert assignment.getPortPrototypeRef().getValue() == "/Swc/PortPrototype"
        assert isinstance(assignment.getRole(), Identifier)
        assert assignment.getRole().getValue() == "NvMService"

    def test_round_trip_absent_assigned_ports_emits_no_wrapper(self, writer):
        """Test that a dependency without assigned ports emits no SWC-SERVICE-DEPENDENCY element at all."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        dependency = SwcServiceDependency(root, "Dep")

        parent = ET.Element("PARENT")
        writer.writeSwcServiceDependencyAssignedPorts(parent, dependency)

        assert parent.find("SWC-SERVICE-DEPENDENCY") is None
