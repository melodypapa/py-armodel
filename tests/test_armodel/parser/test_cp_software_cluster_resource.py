"""Parser tests for CpSoftwareClusterResource (Table 5.44, p.271) and
RoleBasedResourceDependency (Table 5.45, p.272).

XSD group CP-SOFTWARE-CLUSTER-RESOURCE (l.24427) element order:
DEPENDENT-RESOURCES/ROLE-BASED-RESOURCE-DEPENDENCY, GLOBAL-RESOURCE-ID, IS-MANDATORY.
XSD group ROLE-BASED-RESOURCE-DEPENDENCY (l.99145): RESOURCE-REF, ROLE.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import RoleBasedResourceDependency
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CpSoftwareClusterResource

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "CP-SOFTWARE-CLUSTER-RESOURCE") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadCpSoftwareClusterResource:
    def test_read_sets_all_fields(self, parser):
        resource = CpSoftwareClusterResource(AUTOSAR.getInstance(), "Res")
        element = _snip(
            "<SHORT-NAME>Res</SHORT-NAME>"
            "<DEPENDENT-RESOURCES>"
            "<ROLE-BASED-RESOURCE-DEPENDENCY>"
            "<RESOURCE-REF DEST='CP-SOFTWARE-CLUSTER-RESOURCE'>/AUTOSAR/Resources/Res2</RESOURCE-REF>"
            "<ROLE>consumer</ROLE>"
            "</ROLE-BASED-RESOURCE-DEPENDENCY>"
            "</DEPENDENT-RESOURCES>"
            "<GLOBAL-RESOURCE-ID>42</GLOBAL-RESOURCE-ID>"
            "<IS-MANDATORY>true</IS-MANDATORY>"
        )
        parser.readCpSoftwareClusterResource(element, resource)
        assert resource.getShortName() == "Res"
        deps = resource.getDependentResources()
        assert len(deps) == 1
        assert deps[0].getResourceRef().getValue() == "/AUTOSAR/Resources/Res2"
        assert deps[0].getRole().getValue() == "consumer"
        assert resource.getGlobalResourceId().getValue() == 42
        assert resource.getIsMandatory().getValue() is True

    def test_read_empty(self, parser):
        resource = CpSoftwareClusterResource(AUTOSAR.getInstance(), "Res")
        element = _snip("")
        parser.readCpSoftwareClusterResource(element, resource)
        assert resource.getDependentResources() == []
        assert resource.getGlobalResourceId() is None
        assert resource.getIsMandatory() is None


class TestReadRoleBasedResourceDependency:
    def test_read_sets_all_fields(self, parser):
        dependency = RoleBasedResourceDependency()
        element = _snip(
            "<RESOURCE-REF DEST='CP-SOFTWARE-CLUSTER-RESOURCE'>/AUTOSAR/Resources/Res2</RESOURCE-REF>"
            "<ROLE>provider</ROLE>",
            root_tag="ROLE-BASED-RESOURCE-DEPENDENCY",
        )
        parser.readRoleBasedResourceDependency(element, dependency)
        assert dependency.getResourceRef().getValue() == "/AUTOSAR/Resources/Res2"
        assert dependency.getRole().getValue() == "provider"

    def test_read_empty(self, parser):
        dependency = RoleBasedResourceDependency()
        element = _snip("", root_tag="ROLE-BASED-RESOURCE-DEPENDENCY")
        parser.readRoleBasedResourceDependency(element, dependency)
        assert dependency.getResourceRef() is None
        assert dependency.getRole() is None
