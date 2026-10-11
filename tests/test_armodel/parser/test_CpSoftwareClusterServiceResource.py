"""Reader tests for the CpSoftwareClusterServiceResource class (Table 11.14, p.904)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CpSoftwareClusterServiceResource
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadCpSoftwareClusterServiceResource:
    def test_read_all_elements(self, parser):
        """
        The Table 11.14 resourceNeeds row is read: the 0..1 RESOURCE-NEEDS-REFS
        wrapper holds the unbounded RESOURCE-NEEDS-REF references; the base
        CpSoftwareClusterResource level (GLOBAL-RESOURCE-ID, IS-MANDATORY) is
        populated by the base helper.
        """
        element = ET.fromstring(
            "<CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE xmlns='%s' UUID='1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d'>"
            "<SHORT-NAME>service1</SHORT-NAME>"
            "<RESOURCE-NEEDS-REFS>"
            "<RESOURCE-NEEDS-REF DEST='ECUC-CONTAINER-VALUE'>/Config/Container1</RESOURCE-NEEDS-REF>"
            "<RESOURCE-NEEDS-REF DEST='ECUC-CONTAINER-VALUE'>/Config/Container2</RESOURCE-NEEDS-REF>"
            "</RESOURCE-NEEDS-REFS>"
            "<GLOBAL-RESOURCE-ID>7</GLOBAL-RESOURCE-ID>"
            "<IS-MANDATORY>true</IS-MANDATORY>"
            "</CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE>" % NS
        )

        resource = parser.readCpSoftwareClusterServiceResource(element, CpSoftwareClusterServiceResource(None, "service1"))

        assert resource.getShortName() == "service1"
        assert resource.getUuid().getValue() == "1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"

        refs = resource.getResourceNeedsRefs()
        assert [ref.getValue() for ref in refs] == ["/Config/Container1", "/Config/Container2"]
        assert refs[0].getDest() == "ECUC-CONTAINER-VALUE"
        assert refs[1].getDest() == "ECUC-CONTAINER-VALUE"

        assert resource.getGlobalResourceId().getValue() == 7
        assert resource.getIsMandatory().getValue() is True

    def test_read_empty_element(self, parser):
        """
        A resource without group content leaves all fields unset.
        """
        element = ET.fromstring("<CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE xmlns='%s'><SHORT-NAME>service2</SHORT-NAME></CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE>" % NS)

        resource = parser.readCpSoftwareClusterServiceResource(element, CpSoftwareClusterServiceResource(None, "service2"))

        assert resource.getResourceNeedsRefs() == []
        assert resource.getGlobalResourceId() is None
        assert resource.getIsMandatory() is None
