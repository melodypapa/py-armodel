"""
Tests for reading ROLE-BASED-DATA-ASSIGNMENT elements — RoleBasedDataAssignment, Table 12.4 (p.227, R23-11).

RoleBasedDataAssignment (Base = ARObject) carries four own attributes whose reader element set
follows the XSD group ROLE-BASED-DATA-ASSIGNMENT (AUTOSAR_00052.xsd): ROLE (type IDENTIFIER),
USED-DATA-ELEMENT (type AUTOSAR-VARIABLE-REF), USED-PARAMETER-ELEMENT (type
AUTOSAR-PARAMETER-REF) and USED-PIM-REF (REF with required DEST) — each 0..1,
order-independent on read. The ARObject base attributes (S checksum, T timestamp) belong to the
element set via the XSD AR-OBJECT attributeGroup. The class is aggregated by
BswServiceDependency.assignedData, NvBlockDescriptor.writingStrategy and
SwcServiceDependency.assignedData, and read through getRoleBasedDataAssignment at each call site.

Round-trip counterpart: tests/test_armodel/writer/test_role_based_data_assignment.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataAssignment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, AutosarVariableRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import VariableInAtomicSWCTypeInstanceRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import SwcServiceDependency
from tests.test_armodel.parser._helpers import NS

ASSIGNMENT_CONTENT = (
    "<ROLE>ramBlock</ROLE>"
    "<USED-DATA-ELEMENT>"
    "<AUTOSAR-VARIABLE-IREF>"
    "<PORT-PROTOTYPE-REF DEST='P-PORT-PROTOTYPE'>/Swc/DataPort</PORT-PROTOTYPE-REF>"
    "</AUTOSAR-VARIABLE-IREF>"
    "</USED-DATA-ELEMENT>"
    "<USED-PARAMETER-ELEMENT>"
    "<LOCAL-PARAMETER-REF DEST='PARAMETER-DATA-PROTOTYPE'>/Swc/LocalParameter</LOCAL-PARAMETER-REF>"
    "</USED-PARAMETER-ELEMENT>"
    "<USED-PIM-REF DEST='PER-INSTANCE-MEMORY'>/Swc/Pim</USED-PIM-REF>"
)

ASSIGNMENT_XML = f"<ROLE-BASED-DATA-ASSIGNMENT>{ASSIGNMENT_CONTENT}</ROLE-BASED-DATA-ASSIGNMENT>"


def _wrap(inner: str) -> ET.Element:
    """Wrap the ROLE-BASED-DATA-ASSIGNMENT fragment in a namespaced parent element."""
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


class TestGetRoleBasedDataAssignment:
    """Tests for getRoleBasedDataAssignment — own element field values (Table 12.4)."""

    def test_own_element_field_values(self, parser):
        """Test that all four attribute elements are read with their field values."""
        element = _wrap(ASSIGNMENT_XML)[0]

        assignment = parser.getRoleBasedDataAssignment(element)

        assert assignment is not None
        assert isinstance(assignment, RoleBasedDataAssignment)
        role = assignment.getRole()
        assert isinstance(role, Identifier)
        assert role.getValue() == "ramBlock"
        used_data = assignment.getUsedDataElement()
        assert isinstance(used_data, AutosarVariableRef)
        iref = used_data.getAutosarVariableIRef()
        assert isinstance(iref, VariableInAtomicSWCTypeInstanceRef)
        assert iref.getPortPrototypeRef().getValue() == "/Swc/DataPort"
        assert iref.getPortPrototypeRef().getDest() == "P-PORT-PROTOTYPE"
        used_parameter = assignment.getUsedParameterElement()
        assert isinstance(used_parameter, AutosarParameterRef)
        assert used_parameter.getLocalParameterRef().getValue() == "/Swc/LocalParameter"
        pim_ref = assignment.getUsedPimRef()
        assert isinstance(pim_ref, RefType)
        assert pim_ref.getValue() == "/Swc/Pim"
        assert pim_ref.getDest() == "PER-INSTANCE-MEMORY"

    def test_empty_element(self, parser):
        """Test that an empty element yields an instance with all fields unset."""
        element = _wrap("<ROLE-BASED-DATA-ASSIGNMENT></ROLE-BASED-DATA-ASSIGNMENT>")[0]

        assignment = parser.getRoleBasedDataAssignment(element)

        assert assignment is not None
        assert assignment.getRole() is None
        assert assignment.getUsedDataElement() is None
        assert assignment.getUsedParameterElement() is None
        assert assignment.getUsedPimRef() is None

    def test_absent_children(self, parser):
        """Test that an element with only some children leaves the absent fields unset."""
        element = _wrap("<ROLE-BASED-DATA-ASSIGNMENT><ROLE>ramBlock</ROLE></ROLE-BASED-DATA-ASSIGNMENT>")[0]

        assignment = parser.getRoleBasedDataAssignment(element)

        assert assignment.getRole().getValue() == "ramBlock"
        assert assignment.getUsedDataElement() is None
        assert assignment.getUsedParameterElement() is None
        assert assignment.getUsedPimRef() is None

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        element = _wrap("<ROLE-BASED-DATA-ASSIGNMENT S='ck1' T='2024-01-01T12:00:00+00:00'></ROLE-BASED-DATA-ASSIGNMENT>")[0]

        assignment = parser.getRoleBasedDataAssignment(element)

        assert assignment is not None
        assert assignment.getChecksum() is not None
        assert assignment.getChecksum().getValue() == "ck1"
        assert assignment.getTimestamp() is not None


class TestReadRoleBasedDataAssignmentDispatch:
    """Tests for the SwcServiceDependency.assignedData dispatch."""

    def test_dispatch_via_swc_service_dependency(self, parser):
        """Test that readSwcServiceDependencyAssignedData reads assigned data with field values."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        dependency = SwcServiceDependency(root, "dep1")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><ASSIGNED-DATAS>{ASSIGNMENT_XML}</ASSIGNED-DATAS></ROOT>")

        parser.readSwcServiceDependencyAssignedData(element, dependency)

        assigned = dependency.getAssignedData()
        assert len(assigned) == 1
        assignment = assigned[0]
        assert isinstance(assignment, RoleBasedDataAssignment)
        assert assignment.getRole().getValue() == "ramBlock"
        assert isinstance(assignment.getUsedDataElement(), AutosarVariableRef)
        assert assignment.getUsedDataElement().getAutosarVariableIRef().getPortPrototypeRef().getValue() == "/Swc/DataPort"
        assert assignment.getUsedParameterElement().getLocalParameterRef().getValue() == "/Swc/LocalParameter"
        assert assignment.getUsedPimRef().getValue() == "/Swc/Pim"

    def test_dispatch_absent_assigned_data(self, parser):
        """Test that a service dependency without ASSIGNED-DATAS leaves the aggregation empty."""
        root = AUTOSAR.getInstance().createARPackage("Pkg")
        dependency = SwcServiceDependency(root, "dep1")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><SHORT-NAME>dep1</SHORT-NAME></ROOT>")

        parser.readSwcServiceDependencyAssignedData(element, dependency)

        assert dependency.getAssignedData() == []
