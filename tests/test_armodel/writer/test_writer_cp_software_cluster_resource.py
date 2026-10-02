"""
Tests for writing CP-SOFTWARE-CLUSTER-RESOURCE elements —
CpSoftwareClusterResource, Table 5.44 (p.271, R23-11) and
RoleBasedResourceDependency, Table 5.45 (p.272, R23-11).

Round-trip counterpart: tests/test_armodel/parser/test_cp_software_cluster_resource.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import RoleBasedResourceDependency
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CpSoftwareClusterResource
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, PositiveInteger, RefType
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteCpSoftwareClusterResource:
    """Tests for writeCpSoftwareClusterResource — own element field values (Table 5.44)."""

    def test_write_empty_wrapper(self):
        """Test that a CpSoftwareClusterResource without attributes emits only the IDENTIFIABLE wrapper content."""
        package = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        resource = CpSoftwareClusterResource(package, "Res1")

        child = ET.Element("CP-SOFTWARE-CLUSTER-RESOURCE")
        ARXMLWriter().writeCpSoftwareClusterResource(child, resource)

        assert child.find("SHORT-NAME").text == "Res1"
        assert [c.tag for c in child] == ["SHORT-NAME"]

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        package = AUTOSAR.getInstance().createARPackage("AUTOSAR")
        resource = CpSoftwareClusterResource(package, "Res1")
        dependency = RoleBasedResourceDependency()
        dependency.setResourceRef(RefType().setValue("/AUTOSAR/Resources/Res2").setDest("CP-SOFTWARE-CLUSTER-RESOURCE"))
        dependency.setRole(Identifier().setValue("consumer"))
        resource.addDependentResource(dependency)
        gid = PositiveInteger()
        gid.setValue("42")
        resource.setGlobalResourceId(gid)
        mandatory = Boolean()
        mandatory.setValue(True)
        resource.setIsMandatory(mandatory)

        child = ET.Element("CP-SOFTWARE-CLUSTER-RESOURCE")
        ARXMLWriter().writeCpSoftwareClusterResource(child, resource)

        assert [c.tag for c in child] == ["SHORT-NAME", "DEPENDENT-RESOURCES", "GLOBAL-RESOURCE-ID", "IS-MANDATORY"]
        dep_element = child.find("DEPENDENT-RESOURCES/ROLE-BASED-RESOURCE-DEPENDENCY")
        assert dep_element is not None
        assert dep_element.find("RESOURCE-REF").text == "/AUTOSAR/Resources/Res2"
        assert dep_element.find("ROLE").text == "consumer"
        assert child.find("GLOBAL-RESOURCE-ID").text == "42"
        assert child.find("IS-MANDATORY").text == "true"
