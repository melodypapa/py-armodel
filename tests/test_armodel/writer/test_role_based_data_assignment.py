"""
Tests for writing ROLE-BASED-DATA-ASSIGNMENT elements — RoleBasedDataAssignment, Table 12.4 (p.227, R23-11).

RoleBasedDataAssignment (Base = ARObject) carries four own attributes whose writer element
order must follow the XSD sequence (AUTOSAR_00052.xsd group ROLE-BASED-DATA-ASSIGNMENT):
ROLE → USED-DATA-ELEMENT → USED-PARAMETER-ELEMENT → USED-PIM-REF. The ARObject base
attributes (S checksum, T timestamp) belong to the element set via the XSD AR-OBJECT
attributeGroup. The ROLE-BASED-DATA-ASSIGNMENT element is emitted by
writeRoleBasedDataAssignment; its round-trip goes through getRoleBasedDataAssignment.

Round-trip counterpart: tests/test_armodel/parser/test_role_based_data_assignment.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataAssignment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Identifier, RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, AutosarVariableRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import VariableInAtomicSWCTypeInstanceRef
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ELEMENT_ORDER = [
    "ROLE",
    "USED-DATA-ELEMENT",
    "USED-PARAMETER-ELEMENT",
    "USED-PIM-REF",
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


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _filled_assignment():
    assignment = RoleBasedDataAssignment()
    assignment.setRole(Identifier().setValue("ramBlock"))

    used_data = AutosarVariableRef()
    variable_iref = VariableInAtomicSWCTypeInstanceRef()
    variable_iref.setPortPrototypeRef(_ref("/Swc/DataPort", "P-PORT-PROTOTYPE"))
    used_data.setAutosarVariableIRef(variable_iref)
    assignment.setUsedDataElement(used_data)

    used_parameter = AutosarParameterRef()
    used_parameter.setLocalParameterRef(_ref("/Swc/LocalParameter", "PARAMETER-DATA-PROTOTYPE"))
    assignment.setUsedParameterElement(used_parameter)

    assignment.setUsedPimRef(_ref("/Swc/Pim", "PER-INSTANCE-MEMORY"))
    return assignment


def _write_assignment(writer, assignment) -> ET.Element:
    parent = ET.Element("ROOT")
    writer.writeRoleBasedDataAssignment(parent, assignment)
    return parent.find("ROLE-BASED-DATA-ASSIGNMENT")


class TestWriteRoleBasedDataAssignment:
    """Tests for writeRoleBasedDataAssignment — own element field values (Table 12.4)."""

    def test_own_element_field_values(self, writer):
        """Test that all four attribute elements are emitted with their field values."""
        elem = _write_assignment(writer, _filled_assignment())

        assert elem is not None
        assert elem.find("ROLE").text == "ramBlock"
        used_data = elem.find("USED-DATA-ELEMENT")
        assert used_data.find("AUTOSAR-VARIABLE-IREF/PORT-PROTOTYPE-REF").text == "/Swc/DataPort"
        assert used_data.find("AUTOSAR-VARIABLE-IREF/PORT-PROTOTYPE-REF").get("DEST") == "P-PORT-PROTOTYPE"
        assert elem.find("USED-PARAMETER-ELEMENT/LOCAL-PARAMETER-REF").text == "/Swc/LocalParameter"
        assert elem.find("USED-PARAMETER-ELEMENT/LOCAL-PARAMETER-REF").get("DEST") == "PARAMETER-DATA-PROTOTYPE"
        assert elem.find("USED-PIM-REF").text == "/Swc/Pim"
        assert elem.find("USED-PIM-REF").get("DEST") == "PER-INSTANCE-MEMORY"

    def test_xsd_element_order(self, writer):
        """Test that the emitted element order follows the XSD group sequence."""
        elem = _write_assignment(writer, _filled_assignment())

        children = [child.tag for child in elem]
        assert children == XSD_ELEMENT_ORDER

    def test_ar_object_attributes_written(self, writer):
        """Test that the ARObject base attributes (S checksum, T timestamp) are written."""
        assignment = _filled_assignment()
        checksum = String()
        checksum.setValue("ck1")
        assignment.setChecksum(checksum)
        timestamp = DateTime()
        timestamp.setValue("2024-01-01T12:00:00+01:00")
        assignment.setTimestamp(timestamp)

        elem = _write_assignment(writer, assignment)

        assert elem.get("S") == "ck1"
        assert elem.get("T") is not None

    def test_empty_assignment(self, writer):
        """Test that an assignment without any set field emits the wrapper element only."""
        elem = _write_assignment(writer, RoleBasedDataAssignment())

        assert elem is not None
        assert list(elem) == []


class TestWriteReadRoundTrip:
    """Write → re-parse round-trip through getRoleBasedDataAssignment."""

    def test_round_trip_field_values(self, writer):
        """Test that write and re-parse preserve every field value one level down."""
        original = _filled_assignment()

        elem = _write_assignment(writer, original)
        xml = ET.tostring(elem, encoding="unicode")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'>{xml}</ROOT>")[0]

        parser = ARXMLParser()
        reloaded = parser.getRoleBasedDataAssignment(element)

        assert isinstance(reloaded.getRole(), Identifier)
        assert reloaded.getRole().getValue() == "ramBlock"
        assert isinstance(reloaded.getUsedDataElement(), AutosarVariableRef)
        iref = reloaded.getUsedDataElement().getAutosarVariableIRef()
        assert isinstance(iref, VariableInAtomicSWCTypeInstanceRef)
        assert iref.getPortPrototypeRef().getValue() == "/Swc/DataPort"
        assert reloaded.getUsedParameterElement().getLocalParameterRef().getValue() == "/Swc/LocalParameter"
        assert reloaded.getUsedPimRef().getValue() == "/Swc/Pim"
        assert reloaded.getUsedPimRef().getDest() == "PER-INSTANCE-MEMORY"

    def test_round_trip_absent_elements(self, writer):
        """Test that absent attribute elements are not emitted and re-parse to None."""
        assignment = RoleBasedDataAssignment()
        assignment.setRole(Identifier().setValue("ramBlock"))

        elem = _write_assignment(writer, assignment)
        assert elem.find("USED-DATA-ELEMENT") is None
        assert elem.find("USED-PARAMETER-ELEMENT") is None
        assert elem.find("USED-PIM-REF") is None

        xml = ET.tostring(elem, encoding="unicode")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'>{xml}</ROOT>")[0]

        parser = ARXMLParser()
        reloaded = parser.getRoleBasedDataAssignment(element)

        assert reloaded.getRole().getValue() == "ramBlock"
        assert reloaded.getUsedDataElement() is None
        assert reloaded.getUsedParameterElement() is None
        assert reloaded.getUsedPimRef() is None
