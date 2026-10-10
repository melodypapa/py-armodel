"""Reader tests for the CpSoftwareClusterToResourceMapping class (Table 11.16, p.907)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CpSoftwareClusterToResourceMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadCpSoftwareClusterToResourceMapping:
    def test_read_all_elements(self, parser):
        """
        The three Table 11.16 rows are read; the base Identifiable level (SHORT-NAME,
        UUID) is populated by the base helper. The unbounded REQUESTER-REF choice is
        wrapped in the 0..1 REQUESTER-REFS wrapper per the XSD group (AUTOSAR_00052.xsd
        l.24782).
        """
        element = ET.fromstring(
            "<CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING xmlns='%(ns)s' UUID='1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d'>"
            "<SHORT-NAME>mapping1</SHORT-NAME>"
            "<PROVIDER-REF DEST='CP-SOFTWARE-CLUSTER'>/Clusters/ProvidingCluster</PROVIDER-REF>"
            "<REQUESTER-REFS>"
            "<REQUESTER-REF DEST='CP-SOFTWARE-CLUSTER'>/Clusters/RequestingClusterA</REQUESTER-REF>"
            "<REQUESTER-REF DEST='CP-SOFTWARE-CLUSTER'>/Clusters/RequestingClusterB</REQUESTER-REF>"
            "</REQUESTER-REFS>"
            "<SERVICE-RESOURCE-REF DEST='CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE'>/Resources/MyServiceResource</SERVICE-RESOURCE-REF>"
            "</CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING>" % {"ns": NS}
        )

        mapping = parser.readCpSoftwareClusterToResourceMapping(element, CpSoftwareClusterToResourceMapping(None, "mapping1"))

        assert mapping.getShortName() == "mapping1"
        assert mapping.getUuid().getValue() == "1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"

        assert mapping.getProviderRef().getValue() == "/Clusters/ProvidingCluster"
        assert mapping.getProviderRef().getDest() == "CP-SOFTWARE-CLUSTER"

        requester_refs = mapping.getRequesterRefs()
        assert [ref.getValue() for ref in requester_refs] == ["/Clusters/RequestingClusterA", "/Clusters/RequestingClusterB"]
        assert all(ref.getDest() == "CP-SOFTWARE-CLUSTER" for ref in requester_refs)

        assert mapping.getServiceResourceRef().getValue() == "/Resources/MyServiceResource"
        assert mapping.getServiceResourceRef().getDest() == "CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE"

    def test_read_empty_element(self, parser):
        """
        A mapping without group content leaves all fields unset.
        """
        element = ET.fromstring("<CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING xmlns='%s'><SHORT-NAME>mapping2</SHORT-NAME></CP-SOFTWARE-CLUSTER-TO-RESOURCE-MAPPING>" % NS)

        mapping = parser.readCpSoftwareClusterToResourceMapping(element, CpSoftwareClusterToResourceMapping(None, "mapping2"))

        assert mapping.getProviderRef() is None
        assert mapping.getRequesterRefs() == []
        assert mapping.getServiceResourceRef() is None
