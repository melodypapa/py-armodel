"""Reader tests for the CpSoftwareClusterResourcePool aggregator (Table 11.5, p.901)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import CpSoftwareClusterResourcePool
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    CpSoftwareClusterCommunicationResource,
    CpSoftwareClusterServiceResource,
)
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


class TestReadCpSoftwareClusterResourcePool:
    def test_read_all_elements(self, parser):
        """
        Both Table 11.5 rows are read: the ECU-SCOPE-REFS reference wrapper and the
        RESOURCES aggregation wrapper dispatching to the concrete resource subtypes.
        """
        element = ET.fromstring(
            "<CP-SOFTWARE-CLUSTER-RESOURCE-POOL xmlns='%s' UUID='1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d'>"
            "<SHORT-NAME>pool1</SHORT-NAME>"
            "<ECU-SCOPE-REFS>"
            "<ECU-SCOPE-REF DEST='ECU-INSTANCE'>/Ecu/Ecu1</ECU-SCOPE-REF>"
            "<ECU-SCOPE-REF DEST='ECU-INSTANCE'>/Ecu/Ecu2</ECU-SCOPE-REF>"
            "</ECU-SCOPE-REFS>"
            "<RESOURCES>"
            "<CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE><SHORT-NAME>comm1</SHORT-NAME>"
            "<GLOBAL-RESOURCE-ID>5</GLOBAL-RESOURCE-ID>"
            "<IS-MANDATORY>true</IS-MANDATORY>"
            "</CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE>"
            "<CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE><SHORT-NAME>service1</SHORT-NAME></CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE>"
            "</RESOURCES>"
            "</CP-SOFTWARE-CLUSTER-RESOURCE-POOL>" % NS
        )

        pool = parser.readCpSoftwareClusterResourcePool(element, CpSoftwareClusterResourcePool(None, "pool1"))

        assert pool.getShortName() == "pool1"
        assert pool.getUuid().getValue() == "1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"

        refs = pool.getEcuScopeRefs()
        assert [ref.getValue() for ref in refs] == ["/Ecu/Ecu1", "/Ecu/Ecu2"]
        assert refs[0].getDest() == "ECU-INSTANCE"
        assert refs[1].getDest() == "ECU-INSTANCE"

        resources = pool.getResources()
        assert len(resources) == 2
        assert isinstance(resources[0], CpSoftwareClusterCommunicationResource)
        assert resources[0].getShortName() == "comm1"
        assert resources[0].getGlobalResourceId().getValue() == 5
        assert resources[0].getIsMandatory().getValue() is True
        assert isinstance(resources[1], CpSoftwareClusterServiceResource)
        assert resources[1].getShortName() == "service1"

    def test_read_empty_element(self, parser):
        """
        A pool without group content leaves all fields unset.
        """
        element = ET.fromstring("<CP-SOFTWARE-CLUSTER-RESOURCE-POOL xmlns='%s'><SHORT-NAME>pool2</SHORT-NAME></CP-SOFTWARE-CLUSTER-RESOURCE-POOL>" % NS)

        pool = parser.readCpSoftwareClusterResourcePool(element, CpSoftwareClusterResourcePool(None, "pool2"))

        assert pool.getEcuScopeRefs() == []
        assert pool.getResources() == []
