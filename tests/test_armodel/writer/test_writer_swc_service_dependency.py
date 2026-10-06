"""Writer tests for SwcServiceDependency (Swc TPS Table 7.56, p.609).

writeSwcServiceDependency emits the inherited SERVICE-DEPENDENCY group via
writeServiceDependency (Rule 0025: base helper called exactly once) and the
own group in XSD order (AUTOSAR_00052.xsd line 117470): ASSIGNED-DATAS,
ASSIGNED-PORTS, REPRESENTED-PORT-GROUP-REF, SERVICE-NEEDS. Wrapper elements
are emitted only when non-empty; serviceNeeds is the single 0..1 slot.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DltUserNeeds,
    RoleBasedDataAssignment,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedPortAssignment
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _make_dependency(short_name: str = "Dep"):
    package = AUTOSAR.getInstance().createARPackage("Pkg")
    swc = package.createApplicationSwComponentType("Swc")
    behavior = swc.createSwcInternalBehavior("IB")
    return behavior.createSwcServiceDependency(short_name)


def _write_to_string(dependency) -> str:
    parent = ET.Element("PARENT")
    ARXMLWriter().writeSwcServiceDependency(parent, dependency)
    return ET.tostring(parent, encoding="unicode")


class TestWriteSwcServiceDependency:
    def test_write_empty_dependency_emits_no_own_wrappers(self):
        """A dependency with nothing set emits no ASSIGNED-DATAS/ASSIGNED-PORTS/REPRESENTED-PORT-GROUP-REF/SERVICE-NEEDS."""
        dependency = _make_dependency("Empty")
        output = _write_to_string(dependency)

        child = ET.fromstring(output).find("SWC-SERVICE-DEPENDENCY")
        assert child.find("SHORT-NAME").text == "Empty"
        for absent in ("ASSIGNED-DATAS", "ASSIGNED-PORTS", "REPRESENTED-PORT-GROUP-REF", "SERVICE-NEEDS"):
            assert child.find(absent) is None

    def test_write_own_group_in_xsd_order(self):
        """REPRESENTED-PORT-GROUP-REF precedes SERVICE-NEEDS per the XSD group sequenceOffset."""
        dependency = _make_dependency("Full")

        data_assignment = RoleBasedDataAssignment()
        role = Identifier()
        role.setValue("ramMirror")
        data_assignment.setRole(role)
        dependency.AddAssignedData(data_assignment)

        port_assignment = RoleBasedPortAssignment()
        port_ref = RefType()
        port_ref.setValue("/Pkg/Swc/Port")
        port_assignment.setPortPrototypeRef(port_ref)
        dependency.AddAssignedPort(port_assignment)

        dependency.setRepresentedPortGroupRef(RefType().setValue("/Pkg/PortGroup"))
        dependency.createDltUserNeeds("DltNeeds")

        output = _write_to_string(dependency)
        child = ET.fromstring(output).find("SWC-SERVICE-DEPENDENCY")

        tags = [c.tag for c in child]
        assert tags.index("REPRESENTED-PORT-GROUP-REF") < tags.index("SERVICE-NEEDS")

        assert child.find("REPRESENTED-PORT-GROUP-REF").text == "/Pkg/PortGroup"
        needs = child.find("SERVICE-NEEDS")
        assert needs is not None
        assert needs.find("DLT-USER-NEEDS") is not None
        assert child.find("ASSIGNED-DATAS/ROLE-BASED-DATA-ASSIGNMENT/ROLE").text == "ramMirror"
        assert child.find("ASSIGNED-PORTS/ROLE-BASED-PORT-ASSIGNMENT/PORT-PROTOTYPE-REF").text == "/Pkg/Swc/Port"

    def test_round_trip_field_values(self):
        """Set -> save -> reload: every own attribute survives with its field value."""
        document = AUTOSAR.getInstance()
        document.clear()
        package = document.createARPackage("Pkg")
        swc = package.createApplicationSwComponentType("Swc")
        behavior = swc.createSwcInternalBehavior("IB")
        dependency = behavior.createSwcServiceDependency("Dep")

        data_assignment = RoleBasedDataAssignment()
        role = Identifier()
        role.setValue("ramMirror")
        data_assignment.setRole(role)
        data_assignment.setUsedPimRef(RefType().setValue("/Pkg/Swc/IB/Pim"))
        dependency.AddAssignedData(data_assignment)

        port_assignment = RoleBasedPortAssignment()
        port_assignment.setPortPrototypeRef(RefType().setValue("/Pkg/Swc/Port"))
        port_role = Identifier()
        port_role.setValue("NvMService")
        port_assignment.setRole(port_role)
        dependency.AddAssignedPort(port_assignment)

        dependency.setRepresentedPortGroupRef(RefType().setValue("/Pkg/PortGroup"))
        dlt = dependency.createDltUserNeeds("DltNeeds")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getSwComponentTypes()[0]
            dependency_2 = swc_2.getInternalBehavior().getSwcServiceDependencies()[0]

            assert dependency_2.short_name == "Dep"
            assert len(dependency_2.getAssignedData()) == 1
            assert dependency_2.getAssignedData()[0].getRole().getValue() == "ramMirror"
            assert dependency_2.getAssignedData()[0].getUsedPimRef().getValue() == "/Pkg/Swc/IB/Pim"
            assert len(dependency_2.getAssignedPorts()) == 1
            assert dependency_2.getAssignedPorts()[0].getPortPrototypeRef().getValue() == "/Pkg/Swc/Port"
            assert dependency_2.getAssignedPorts()[0].getRole().getValue() == "NvMService"
            assert dependency_2.getRepresentedPortGroupRef().getValue() == "/Pkg/PortGroup"

            needs_2 = dependency_2.getServiceNeeds()
            assert isinstance(needs_2, DltUserNeeds)
            assert needs_2.short_name == dlt.short_name
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
